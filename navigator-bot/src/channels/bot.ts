/**
 * The Chat SDK instance: one bot, three channels. Each channel is switched on by its settings:
 * WhatsApp (WHATSAPP_*), Telegram (TELEGRAM_BOT_TOKEN) and the web page (WEB_CHAT, on by default).
 */

import { createMemoryState } from "@chat-adapter/state-memory";
import { createPostgresState } from "@chat-adapter/state-pg";
import { createTelegramAdapter } from "@chat-adapter/telegram";
import { createWebAdapter } from "@chat-adapter/web";
import { createWhatsAppAdapter } from "@chat-adapter/whatsapp";
import { type Adapter, Chat, type Logger } from "chat";
import type pg from "pg";
import type { Config } from "../config.ts";
import { logger } from "../ops/logger.ts";
import type { MessageHandler } from "./handler.ts";

/** Meta re-delivers a webhook for up to a few days if it gets no 200; remember message ids for 7. */
export const DEDUPE_TTL_MS = 7 * 24 * 3600 * 1000;

/** Chat SDK's logger interface on top of the bot's logger. */
function chatLogger(prefix = "chat"): Logger {
  const child = logger.child({ component: prefix });
  return {
    child: (p: string) => chatLogger(`${prefix}:${p}`),
    debug: (message: string, ...args: unknown[]) => child.debug({ args }, message),
    info: (message: string, ...args: unknown[]) => child.info({ args }, message),
    warn: (message: string, ...args: unknown[]) => child.warn({ args }, message),
    error: (message: string, ...args: unknown[]) => child.error({ args }, message),
  };
}

export interface BotOptions {
  config: Config;
  handler: MessageHandler;
  /** Postgres pool for Chat SDK's locks and duplicate checks; in-memory state without one. */
  pool: pg.Pool | undefined;
  /** Web only: the session id from the request's cookie. */
  webUser: (request: Request) => string | undefined;
}

export type Bot = Chat<Record<string, Adapter>>;

export function createBot({ config, handler, pool, webUser }: BotOptions): Bot {
  const adapters: Record<string, Adapter> = {};
  const userName = "navigator";
  if (config.whatsapp) {
    adapters.whatsapp = createWhatsAppAdapter({
      accessToken: config.whatsapp.accessToken,
      appSecret: config.whatsapp.appSecret,
      phoneNumberId: config.whatsapp.phoneNumberId,
      verifyToken: config.whatsapp.verifyToken,
      apiVersion: config.whatsapp.apiVersion,
      userName,
      logger: chatLogger("whatsapp"),
    });
  }
  if (config.telegram) {
    adapters.telegram = createTelegramAdapter({
      botToken: config.telegram.botToken,
      secretToken: config.telegram.secretToken,
      mode: "webhook",
      longMessages: "split",
      // The bot keeps its own (hashed, time-limited) memory; no second copy of every message.
      persistThreadHistory: false,
      userName,
      logger: chatLogger("telegram"),
    });
  }
  if (config.web.enabled) {
    adapters.web = createWebAdapter({
      userName,
      persistMessageHistory: false,
      getUser: (request) => {
        const sid = webUser(request);
        return sid ? { id: sid } : null;
      },
      logger: chatLogger("web"),
    });
  }

  const chat = new Chat({
    userName,
    adapters,
    state: pool ? createPostgresState({ client: pool, logger: chatLogger("state") }) : createMemoryState(),
    // Messages that arrive while one is being answered wait, then are answered together.
    concurrency: { strategy: "queue", maxQueueSize: 10, onQueueFull: "drop-oldest" },
    dedupeTtlMs: DEDUPE_TTL_MS,
    logger: chatLogger(),
  });

  chat.onDirectMessage((thread, message, _channel, context) => handler.onMessage(thread, message, context));

  if (config.telegram) {
    chat.onSlashCommand(["/start", "/reset", "/delete"], async (event) => {
      const raw = event.raw as { chat?: { type?: string } } | undefined;
      if (raw?.chat?.type !== "private") return; // groups and channels are ignored
      await handler.onCommand(
        (text) => event.channel.post({ markdown: text }),
        "telegram",
        event.user.userId,
        event.command,
      );
    });
  }
  return chat;
}
