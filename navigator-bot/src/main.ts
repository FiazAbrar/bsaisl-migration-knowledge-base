/**
 * Start the bot:  npm run dev  (local, reloads on change)  ·  npm start  (servers, Docker)
 */
import { serve } from "@hono/node-server";
import { buildApp } from "./app.ts";
import { ConfigError, config } from "./config.ts";
import { describeError, logger } from "./ops/logger.ts";
import { captureError, flushSentry, initSentry } from "./ops/sentry.ts";

async function main(): Promise<void> {
  let settings: ReturnType<typeof config>;
  try {
    settings = config();
  } catch (err) {
    if (err instanceof ConfigError) {
      logger.fatal(err.message);
      process.exit(1);
    }
    throw err;
  }
  initSentry(settings.sentry.dsn, settings.sentry.environment, process.env.RENDER_GIT_COMMIT);
  if (settings.web.enabled && !settings.web.turnstileSecretKey) {
    logger.warn(
      "The web chat is on without a bot check: set TURNSTILE_SITE_KEY and TURNSTILE_SECRET_KEY before going public",
    );
  }

  const app = await buildApp({ config: settings });
  const server = serve({ fetch: app.http.fetch, port: settings.port, hostname: "0.0.0.0" }, (info) => {
    logger.info(
      {
        port: info.port,
        channels: Object.keys(app.bot.webhooks),
        database: app.database.kind,
      },
      "Navigator bot is listening",
    );
  });

  void app.replayLeftovers().catch((err) => captureError(err, { area: "replay" }));
  void app.purge().catch((err) => captureError(err, { area: "retention" }));

  let stopping = false;
  const stop = async (signal: string) => {
    if (stopping) return;
    stopping = true;
    logger.info({ signal }, "Stopping: finishing answers in progress");
    server.close();
    await app.shutdown();
    await flushSentry();
    process.exit(0);
  };
  process.on("SIGTERM", () => void stop("SIGTERM"));
  process.on("SIGINT", () => void stop("SIGINT"));
  process.on("unhandledRejection", (err) => {
    logger.error({ err: describeError(err) }, "Unhandled promise rejection");
    captureError(err, { area: "unhandled" });
  });
}

main().catch(async (err) => {
  logger.fatal({ err: describeError(err) }, "The bot could not start");
  captureError(err, { area: "startup" });
  await flushSentry();
  process.exit(1);
});
