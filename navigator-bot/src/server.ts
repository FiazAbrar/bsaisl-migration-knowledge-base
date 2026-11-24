/**
 * The HTTP server: one app for every channel.
 *   GET  /health          status for the host and UptimeRobot (no secrets, no budgets)
 *   GET  /webhook         Meta's verification handshake      POST /webhook   WhatsApp messages
 *   POST /telegram        Telegram updates
 *   GET  /                the web chat page                   GET  /privacy   the privacy notice
 *   GET  /api/config      what the page needs to start        POST /api/session  bot check → session cookie
 *   POST /api/chat        one web message (AI SDK stream)     GET  /api/me    the guide this chat is about
 */
import { existsSync } from "node:fs";
import path from "node:path";
import { getConnInfo } from "@hono/node-server/conninfo";
import { serveStatic } from "@hono/node-server/serve-static";
import { type Context, Hono } from "hono";
import { bodyLimit } from "hono/body-limit";
import { getCookie, setCookie } from "hono/cookie";
import { secureHeaders } from "hono/secure-headers";
import type { Bot } from "./channels/bot.ts";
import { TELEGRAM_PATH } from "./channels/telegram-setup.ts";
import { BOT_ROOT, type Config } from "./config.ts";
import { type Guard, MAX_CHARS } from "./guard/guard.ts";
import type { KbService } from "./kb/service.ts";
import { type MemoryStore, userKey } from "./memory/store.ts";
import { describeError, logger } from "./ops/logger.ts";
import {
  COOKIE,
  clientIp,
  ipKey,
  isTrustedPeer,
  newSessionCookie,
  SESSION_SECONDS,
  sameSite,
  sessionId,
  trustedProxies,
  verifyTurnstile,
} from "./web/security.ts";

export const WEB_DIST = path.join(BOT_ROOT, "web", "dist");
const MAX_WEB_IN_FLIGHT = 4; // web answers worked on at once, so the open page can't starve WhatsApp
const SESSION_BODY_MAX = 4096;
const CHAT_BODY_MAX = 16 * 1024;
const WEBHOOK_BODY_MAX = 1024 * 1024;

export interface ServerDeps {
  config: Config;
  bot: Bot;
  kb: KbService;
  guard: Guard;
  store: MemoryStore;
  database: string;
  aiMode: "test" | "ai";
  /** Keeps background work (answers after the webhook returned) alive; awaited on shutdown. */
  waitUntil: (task: Promise<unknown>) => void;
  fetchFn?: typeof fetch;
}

/** The hashed IP of the web request that carried each session's latest message (read by the handler). */
export class WebIpRegistry {
  private readonly bySession = new Map<string, { key: string; at: number }>();

  set(sid: string, key: string): void {
    this.bySession.set(sid, { key, at: Date.now() });
    if (this.bySession.size > 10_000) {
      const cutoff = Date.now() - 10 * 60_000;
      for (const [s, v] of this.bySession) if (v.at < cutoff) this.bySession.delete(s);
    }
  }

  /** For a web thread id ("web:{sid}:{conversation}"). */
  forThread(threadId: string): string | undefined {
    const sid = threadId.split(":")[1];
    return sid ? this.bySession.get(sid)?.key : undefined;
  }
}

const CSP = [
  "default-src 'self'",
  "script-src 'self' https://challenges.cloudflare.com",
  "frame-src https://challenges.cloudflare.com",
  "connect-src 'self'",
  "style-src 'self'",
  "img-src 'self' data:",
  "object-src 'none'",
  "base-uri 'none'",
  "form-action 'none'",
  "frame-ancestors 'none'",
].join("; ");

export function createServer(deps: ServerDeps, webIps: WebIpRegistry): Hono {
  const { config, bot, kb, guard, store } = deps;
  const app = new Hono();
  const proxies = trustedProxies(config.trustedProxies);
  let inFlight = 0;

  const peerOf = (c: Context): string => {
    try {
      return getConnInfo(c).remote.address ?? "";
    } catch {
      return "";
    }
  };
  const ipOf = (c: Context) =>
    clientIp(
      peerOf(c),
      config.proxyIpHeader ? c.req.header(config.proxyIpHeader) : undefined,
      config.proxyIpHeader,
      proxies,
    );
  // Behind a proxy the browser's https shows only in X-Forwarded-Proto, believed from a trusted proxy.
  const isHttps = (c: Context) =>
    new URL(c.req.url).protocol === "https:" ||
    (isTrustedPeer(proxies, peerOf(c)) &&
      c.req.header("x-forwarded-proto")?.split(",")[0]?.trim() === "https");
  const sessionOf = (c: Context) => sessionId(config.webSessionSecret, getCookie(c, COOKIE));

  app.use(
    "*",
    secureHeaders({
      contentSecurityPolicy: undefined,
      xFrameOptions: "DENY",
      referrerPolicy: "no-referrer",
      strictTransportSecurity: false,
      permissionsPolicy: { camera: [], microphone: [], geolocation: [] },
    }),
  );
  app.use("*", async (c, next) => {
    await next();
    if (isHttps(c)) c.header("Strict-Transport-Security", "max-age=31536000; includeSubDomains");
    if (c.req.path.startsWith("/api/")) c.header("Cache-Control", "no-store");
    if (c.res.headers.get("content-type")?.startsWith("text/html")) c.header("Content-Security-Policy", CSP);
  });
  app.onError((err, c) => {
    logger.error({ err: describeError(err), path: c.req.path }, "Request failed");
    return c.json({ error: "server" }, 500);
  });

  // ---------- health ----------
  app.get("/health", (c) => {
    const body = {
      status: kb.ready ? "ok" : "starting",
      database: deps.database,
      ai: deps.aiMode,
      channels: {
        whatsapp: Boolean(config.whatsapp),
        telegram: Boolean(config.telegram),
        web: config.web.enabled,
      },
      kb_sync: {
        last_sync: kb.status.lastSync ?? null,
        commit: kb.status.commit ?? null,
        error: kb.status.error ?? null,
        index_refused: kb.status.indexRefused ?? null,
      },
      ...(kb.ready
        ? (() => {
            const info = kb.current.info();
            return {
              kb_built_at: info.builtAt,
              kb_guides: info.guides,
              kb_sections: info.sections,
              kb_commit: info.commit?.slice(0, 7) ?? "local",
              kb_warnings: info.warnings,
            };
          })()
        : {}),
    };
    return c.json(body, kb.ready ? 200 : 500);
  });

  // ---------- WhatsApp ----------
  if (config.whatsapp) {
    const whatsapp = bot.webhooks.whatsapp;
    if (!whatsapp) throw new Error("WhatsApp adapter missing");
    app.get("/webhook", (c) => whatsapp(c.req.raw));
    app.post("/webhook", bodyLimit({ maxSize: WEBHOOK_BODY_MAX }), (c) =>
      whatsapp(c.req.raw, { waitUntil: deps.waitUntil }),
    );
  }

  // ---------- Telegram ----------
  if (config.telegram) {
    const telegram = bot.webhooks.telegram;
    if (!telegram) throw new Error("Telegram adapter missing");
    app.post(TELEGRAM_PATH, bodyLimit({ maxSize: WEBHOOK_BODY_MAX }), (c) =>
      telegram(c.req.raw, { waitUntil: deps.waitUntil }),
    );
  }

  // ---------- web chat ----------
  if (config.web.enabled) {
    const web = bot.webhooks.web;
    if (!web) throw new Error("Web adapter missing");
    const forbidden = (c: Context) =>
      !sameSite(
        c.req.header("sec-fetch-site"),
        c.req.header("origin"),
        c.req.header("host"),
        config.publicDomain,
      );

    app.get("/api/config", (c) => {
      const k = kb.ready ? kb.current : undefined;
      return c.json({
        turnstile_site_key: config.web.turnstileSecretKey ? (config.web.turnstileSiteKey ?? null) : null,
        max_chars: MAX_CHARS,
        countries: k ? k.countries.buttons() : [],
        guides_updated: k?.meta.guidesUpdated ?? null,
      });
    });

    app.post(
      "/api/session",
      bodyLimit({ maxSize: SESSION_BODY_MAX, onError: (c) => c.json({ error: "too_large" }, 413) }),
      async (c) => {
        if (forbidden(c)) return c.json({ error: "forbidden" }, 403);
        const data = await c.req.json<unknown>().catch(() => undefined);
        if (!data || typeof data !== "object" || Array.isArray(data))
          return c.json({ error: "bad_request" }, 400);
        const token = (data as { turnstile_token?: unknown }).turnstile_token;
        const secret = config.web.turnstileSecretKey;
        if (secret && (typeof token !== "string" || token.length === 0 || token.length > 2048)) {
          return c.json({ error: "bot_check" }, 403);
        }
        const ip = ipOf(c);
        const decision = await guard.newSession(ipKey(ip, config.userHashSecret));
        if (!decision.ok)
          return c.json(
            { error: "rate_limited", scope: decision.reason, retry_after: decision.retryAfter },
            429,
          );
        if (
          secret &&
          !(await verifyTurnstile(secret, token as string, ip, config.publicDomain, deps.fetchFn))
        ) {
          return c.json({ error: "bot_check" }, 403);
        }
        setCookie(c, COOKIE, newSessionCookie(config.webSessionSecret), {
          httpOnly: true,
          secure: isHttps(c),
          sameSite: "Strict",
          path: "/",
          maxAge: SESSION_SECONDS,
        });
        return c.json({ ok: true });
      },
    );

    app.post(
      "/api/chat",
      bodyLimit({ maxSize: CHAT_BODY_MAX, onError: (c) => c.json({ error: "too_large" }, 413) }),
      async (c) => {
        if (forbidden(c)) return c.json({ error: "forbidden" }, 403);
        const sid = sessionOf(c);
        if (!sid) return c.json({ error: "no_session" }, 401);
        if (inFlight >= MAX_WEB_IN_FLIGHT) return c.json({ error: "busy", retry_after: 5 }, 503);
        webIps.set(sid, ipKey(ipOf(c), config.userHashSecret));
        inFlight++;
        try {
          return await web(c.req.raw, { waitUntil: deps.waitUntil });
        } finally {
          inFlight--;
        }
      },
    );

    app.get("/api/me", async (c) => {
      const sid = sessionOf(c);
      if (!sid) return c.json({ error: "no_session" }, 401);
      const user = await store.get(userKey(`web:${sid}`, config.userHashSecret));
      const country = user?.country && kb.ready && kb.current.guide(user.country) ? user.country : null;
      return c.json({ country });
    });

    const root = path.relative(process.cwd(), WEB_DIST) || ".";
    if (!existsSync(WEB_DIST)) logger.warn("The web page is not built yet: run `npm run build:web`");
    app.get("/privacy", serveStatic({ root, path: "privacy.html" }));
    app.get(
      "/assets/*",
      serveStatic({
        root,
        onFound: (_p, c) => c.header("Cache-Control", "public, max-age=31536000, immutable"),
      }),
    );
    app.get("/favicon.svg", serveStatic({ root }));
    app.get("/theme.js", serveStatic({ root, onFound: (_p, c) => c.header("Cache-Control", "no-cache") }));
    app.get(
      "/",
      serveStatic({ root, path: "index.html", onFound: (_p, c) => c.header("Cache-Control", "no-cache") }),
    );
  }

  return app;
}
