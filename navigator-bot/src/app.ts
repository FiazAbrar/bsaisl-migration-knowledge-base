/**
 * Builds the whole bot from its settings: database, guides, conversation, channels and HTTP server.
 * src/main.ts runs it; tests build it with their own settings.
 */
import type { Hono } from "hono";
import { createAnswerer } from "./ai/factory.ts";
import { type Bot, createBot } from "./channels/bot.ts";
import { channelOf, MessageHandler, toIncoming } from "./channels/handler.ts";
import { registerTelegramWebhook } from "./channels/telegram-setup.ts";
import type { Config } from "./config.ts";
import { Conversation } from "./conversation/pipeline.ts";
import { type Database, openDatabase } from "./db/client.ts";
import { DbKbBaselineStore } from "./db/kb-state.ts";
import { Guard } from "./guard/guard.ts";
import { KbService } from "./kb/service.ts";
import { Inbox } from "./memory/inbox.ts";
import { MemoryStore } from "./memory/store.ts";
import { describeError, logger } from "./ops/logger.ts";
import { alert, captureError } from "./ops/sentry.ts";
import { createServer, WebIpRegistry } from "./server.ts";
import { sessionId } from "./web/security.ts";

export interface App {
  http: Hono;
  bot: Bot;
  kb: KbService;
  database: Database;
  /** Answer messages a crash left unanswered (run once, after start-up). */
  replayLeftovers(): Promise<number>;
  /** Apply the retention rules now (also runs daily). */
  purge(): Promise<void>;
  /** Stop timers, wait for answers in progress, close the database. */
  shutdown(): Promise<void>;
}

export interface BuildOptions {
  config: Config;
  /** Tests: an in-memory database. */
  memoryDatabase?: boolean;
  /** Tests: skip registering the Telegram webhook. */
  skipTelegramSetup?: boolean;
  fetchFn?: typeof fetch;
}

export async function buildApp({
  config,
  memoryDatabase,
  skipTelegramSetup,
  fetchFn,
}: BuildOptions): Promise<App> {
  const startedAt = new Date();
  const database = await openDatabase({
    url: config.databaseUrl,
    dataDir: config.dataDir,
    memory: memoryDatabase ?? false,
  });
  if (database.kind === "pglite" && config.env === "production") {
    logger.warn(
      "No DATABASE_URL: memory and limits are kept in data/pglite and are lost if the server's disk is wiped",
    );
  }

  const kb = new KbService({
    ...config.kb,
    store: new DbKbBaselineStore(database.db),
    onAlert: (message) => alert(message, { area: "guides" }),
  });
  await kb.start();

  const tasks = new Set<Promise<unknown>>();
  const waitUntil = (task: Promise<unknown>) => {
    const tracked = task.catch((err) => logger.error({ err: describeError(err) }, "Background task failed"));
    tasks.add(tracked);
    void tracked.finally(() => tasks.delete(tracked));
  };

  const store = new MemoryStore(database.db);
  const guard = new Guard(database.db);
  const inbox = new Inbox(database.db);
  const { answerer, afterAnswer } = createAnswerer(config, { store, guard });
  const conversation = new Conversation({
    kb: () => kb.current,
    store,
    guard,
    answerer,
    contextTokenBudget: config.ai.contextTokenBudget,
    ...(config.publicDomain ? { privacyLink: `https://${config.publicDomain}/privacy` } : {}),
    defer: waitUntil,
    ...(afterAnswer ? { afterAnswer } : {}),
  });
  const webIps = new WebIpRegistry();
  const handler = new MessageHandler({
    conversation,
    inbox,
    userHashSecret: config.userHashSecret,
    ipKeyFor: (threadId) => webIps.forThread(threadId),
    onError: (err, channel) => captureError(err, { channel }),
  });
  const bot = createBot({
    config,
    handler,
    pool: database.pool,
    webUser: (request) => {
      const cookie = request.headers.get("cookie") ?? "";
      const value = /(?:^|;\s*)nav_sid=([^;]+)/.exec(cookie)?.[1];
      return sessionId(config.webSessionSecret, value ? decodeURIComponent(value) : undefined);
    },
  });
  await bot.initialize();

  const http = createServer(
    {
      config,
      bot,
      kb,
      guard,
      store,
      database: database.kind,
      aiMode: answerer.mode,
      waitUntil,
      ...(fetchFn ? { fetchFn } : {}),
    },
    webIps,
  );

  if (config.telegram && config.publicDomain && !skipTelegramSetup) {
    waitUntil(
      registerTelegramWebhook(
        config.telegram.botToken,
        config.telegram.secretToken,
        config.publicDomain,
        fetchFn,
      ),
    );
  }

  const purge = async () => {
    const removed = await store.purge();
    if (removed.turns || removed.users) logger.info(removed, "Retention: old messages and people deleted");
  };
  const purgeTimer = setInterval(() => void purge().catch((e) => captureError(e)), 24 * 3600 * 1000);
  purgeTimer.unref();

  return {
    http,
    bot,
    kb,
    database,
    async replayLeftovers() {
      const leftovers = await inbox.leftovers(startedAt);
      let replayed = 0;
      for (const item of leftovers) {
        const channel = channelOf(item.threadId);
        // A web reply streams back on the request that asked; after a restart that browser is gone.
        if (!channel || channel === "web" || !kb.ready) {
          await inbox.done(item.id);
          continue;
        }
        await inbox.retrying(item.id);
        const incoming = toIncoming(channel, item.userKey, [{ text: item.text, attachments: [] }]);
        await handler.answer(bot.thread(item.threadId), incoming, item.id);
        replayed++;
      }
      if (replayed) logger.info({ replayed }, "Answered messages left unanswered by a restart");
      return replayed;
    },
    purge,
    async shutdown() {
      clearInterval(purgeTimer);
      kb.stop();
      await Promise.race([Promise.allSettled([...tasks]), new Promise((r) => setTimeout(r, 25_000))]);
      await bot.shutdown().catch(() => undefined);
      await database.close();
    },
  };
}
