/**
 * Points Telegram at this deployment (https://PUBLIC_DOMAIN/telegram) and sets the bot's command menu.
 * Skips both calls when the webhook already points here, so a restart sends nothing to Telegram.
 */
import { describeError, logger } from "../ops/logger.ts";

export const TELEGRAM_PATH = "/telegram";

const MENU = {
  en: [
    { command: "start", description: "Welcome and list of countries" },
    { command: "reset", description: "Start over" },
    { command: "delete", description: "Delete my conversation history" },
  ],
  bn: [
    { command: "start", description: "স্বাগতম ও দেশের তালিকা" },
    { command: "reset", description: "নতুন করে শুরু" },
    { command: "delete", description: "আমার কথোপকথন মুছে দিন" },
  ],
};

async function call(
  token: string,
  method: string,
  payload: Record<string, unknown>,
  fetchFn: typeof fetch,
): Promise<{ ok?: boolean; result?: Record<string, unknown>; description?: string }> {
  try {
    const res = await fetchFn(`https://api.telegram.org/bot${token}/${method}`, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(payload),
      signal: AbortSignal.timeout(15_000),
    });
    const data = (await res.json()) as {
      ok?: boolean;
      result?: Record<string, unknown>;
      description?: string;
    };
    if (!data.ok)
      logger.error(
        { method, status: res.status, description: data.description?.slice(0, 300) },
        "Telegram call failed",
      );
    return data;
  } catch (err) {
    // The error text can contain the URL, and so the token: log the type only.
    logger.error({ method, type: describeError(err).type }, "Telegram call failed");
    return {};
  }
}

export async function registerTelegramWebhook(
  token: string,
  secretToken: string,
  domain: string,
  fetchFn: typeof fetch = fetch,
): Promise<boolean> {
  const url = `https://${domain}${TELEGRAM_PATH}`;
  const info = await call(token, "getWebhookInfo", {}, fetchFn);
  if (info.result?.url === url) {
    logger.info({ url }, "Telegram webhook already points here");
    return true;
  }
  const set = await call(
    token,
    "setWebhook",
    { url, secret_token: secretToken, allowed_updates: ["message"], drop_pending_updates: false },
    fetchFn,
  );
  await call(token, "setMyCommands", { commands: MENU.en }, fetchFn);
  await call(token, "setMyCommands", { commands: MENU.bn, language_code: "bn" }, fetchFn);
  logger.info(
    { url, ok: Boolean(set.ok) },
    set.ok ? "Telegram webhook set" : "Telegram webhook could NOT be set",
  );
  return Boolean(set.ok);
}
