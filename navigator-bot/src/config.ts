/**
 * Every setting the bot reads, checked once at start-up. Values come from the environment (.env locally,
 * the host's settings in the cloud). `.env.example` lists them with explanations.
 *
 * Abuse limits (GUARD_* and BUDGET_*) are read separately by src/guard/limits.ts on every check, so they
 * can be changed on the host without a redeploy.
 */
import { createHash } from "node:crypto";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { z } from "zod";

/** The navigator-bot folder (this file is navigator-bot/src/config.ts). */
export const BOT_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

const text = z.string().trim();
const optionalText = text.optional().transform((v) => (v ? v : undefined));
const flag = (fallback: boolean) =>
  text
    .optional()
    .transform((v) =>
      v === undefined || v === "" ? fallback : !["0", "false", "no", "off"].includes(v.toLowerCase()),
    );
const int = (fallback: number, min = 0) =>
  text
    .optional()
    .transform((v) => (v === undefined || v === "" ? fallback : Number(v)))
    .pipe(z.number().int().min(min));

const schema = z.object({
  NODE_ENV: optionalText,
  PORT: int(8000, 1),
  LOG_LEVEL: text.optional().default("info"),
  DATA_DIR: optionalText,

  // Public address of this server (no https://). Used to register the Telegram webhook and to check
  // Turnstile tokens and browser Origin headers.
  PUBLIC_DOMAIN: optionalText,
  // Header that carries the visitor's IP behind a proxy (Render: X-Forwarded-For), and which proxy
  // addresses may set it. Default: loopback and private networks.
  PROXY_IP_HEADER: optionalText,
  TRUSTED_PROXIES: optionalText,

  // Keys the bot derives its secrets from. USER_HASH_SECRET turns WhatsApp numbers, Telegram ids and
  // web sessions into codes before anything is stored; changing it forgets every user.
  USER_HASH_SECRET: optionalText,
  WEB_SESSION_SECRET: optionalText,

  WHATSAPP_ACCESS_TOKEN: optionalText,
  WHATSAPP_APP_SECRET: optionalText,
  META_APP_SECRET: optionalText, // older name of WHATSAPP_APP_SECRET
  WHATSAPP_PHONE_NUMBER_ID: optionalText,
  WHATSAPP_VERIFY_TOKEN: optionalText,
  WHATSAPP_BUSINESS_ACCOUNT_ID: optionalText,
  WHATSAPP_API_VERSION: optionalText,
  GRAPH_API_VERSION: optionalText, // older name of WHATSAPP_API_VERSION

  TELEGRAM_BOT_TOKEN: optionalText,
  TELEGRAM_WEBHOOK_SECRET_TOKEN: optionalText,

  WEB_CHAT: flag(true),
  TURNSTILE_SITE_KEY: optionalText,
  TURNSTILE_SECRET_KEY: optionalText,

  KB_DIR: optionalText,
  KB_REPO: optionalText,
  KB_BRANCH: text.optional().default("main"),
  KB_SYNC_MINUTES: int(15, 1),
  KB_GITHUB_TOKEN: optionalText,
  KB_ACCEPT_COMMIT: optionalText,

  DATABASE_URL: optionalText,

  OPENROUTER_API_KEY: optionalText,
  LLM_MODEL: optionalText,
  LLM_FALLBACK_MODEL: optionalText,
  LLM_SMALL_MODEL: optionalText,
  LLM_TIMEOUT_MS: int(45_000, 1000),
  LLM_MAX_OUTPUT_TOKENS: int(900, 64),
  CONTEXT_TOKEN_BUDGET: int(3000, 200),
  EVAL_MODELS: optionalText,

  SENTRY_DSN: optionalText,
  SENTRY_ENVIRONMENT: optionalText,
});

export type Env = z.infer<typeof schema>;

export interface Config {
  env: "production" | "development" | "test";
  port: number;
  logLevel: string;
  dataDir: string;
  publicDomain: string | undefined;
  proxyIpHeader: string | undefined;
  trustedProxies: string | undefined;
  userHashSecret: string;
  webSessionSecret: string;
  whatsapp:
    | {
        accessToken: string;
        appSecret: string;
        phoneNumberId: string;
        verifyToken: string;
        businessAccountId: string | undefined;
        apiVersion: string;
      }
    | undefined;
  telegram: { botToken: string; secretToken: string } | undefined;
  web: { enabled: boolean; turnstileSiteKey: string | undefined; turnstileSecretKey: string | undefined };
  kb: {
    dir: string;
    repo: string | undefined;
    branch: string;
    syncMinutes: number;
    githubToken: string | undefined;
    acceptCommit: string | undefined;
  };
  databaseUrl: string | undefined;
  ai: {
    apiKey: string | undefined;
    model: string;
    fallbackModel: string | undefined;
    smallModel: string;
    timeoutMs: number;
    maxOutputTokens: number;
    contextTokenBudget: number;
    evalModels: string[];
  };
  sentry: { dsn: string | undefined; environment: string };
}

export class ConfigError extends Error {}

/** The Telegram webhook secret, derived from the bot token when not set (no extra secret to manage). */
export function telegramSecretFor(botToken: string): string {
  return createHash("sha256").update(`navigator-telegram-webhook:${botToken}`).digest("hex");
}

export function loadConfig(source: NodeJS.ProcessEnv = process.env): Config {
  const parsed = schema.safeParse(source);
  if (!parsed.success) {
    const issues = parsed.error.issues.map((i) => `${i.path.join(".")}: ${i.message}`).join("; ");
    throw new ConfigError(`Invalid settings: ${issues}`);
  }
  const e = parsed.data;
  const env = e.NODE_ENV === "production" ? "production" : e.NODE_ENV === "test" ? "test" : "development";

  const userHashSecret =
    e.USER_HASH_SECRET ?? (env === "production" ? undefined : "dev-only-user-hash-secret");
  if (!userHashSecret) throw new ConfigError("USER_HASH_SECRET must be set (see .env.example).");
  if (env === "production" && userHashSecret.length < 32) {
    throw new ConfigError("USER_HASH_SECRET must be at least 32 characters.");
  }

  if (e.OPENROUTER_API_KEY && !e.LLM_MODEL) {
    throw new ConfigError("With OPENROUTER_API_KEY set, LLM_MODEL must name the OpenRouter model to use.");
  }

  const appSecret = e.WHATSAPP_APP_SECRET ?? e.META_APP_SECRET;
  const waParts = [e.WHATSAPP_ACCESS_TOKEN, appSecret, e.WHATSAPP_PHONE_NUMBER_ID, e.WHATSAPP_VERIFY_TOKEN];
  if (waParts.some(Boolean) && !waParts.every(Boolean)) {
    throw new ConfigError(
      "WhatsApp needs all of WHATSAPP_ACCESS_TOKEN, WHATSAPP_APP_SECRET, WHATSAPP_PHONE_NUMBER_ID and WHATSAPP_VERIFY_TOKEN (or none, to switch it off).",
    );
  }

  const dataDir = path.resolve(BOT_ROOT, e.DATA_DIR ?? "data");
  const kbDir = e.KB_REPO ? path.join(dataDir, "kb-repo") : path.resolve(BOT_ROOT, e.KB_DIR ?? "..");

  return {
    env,
    port: e.PORT,
    logLevel: e.LOG_LEVEL,
    dataDir,
    publicDomain: e.PUBLIC_DOMAIN?.replace(/^https?:\/\//, "").replace(/\/+$/, ""),
    proxyIpHeader: e.PROXY_IP_HEADER,
    trustedProxies: e.TRUSTED_PROXIES,
    userHashSecret,
    webSessionSecret: e.WEB_SESSION_SECRET ?? `${userHashSecret}:web-session`,
    whatsapp:
      e.WHATSAPP_ACCESS_TOKEN && appSecret && e.WHATSAPP_PHONE_NUMBER_ID && e.WHATSAPP_VERIFY_TOKEN
        ? {
            accessToken: e.WHATSAPP_ACCESS_TOKEN,
            appSecret,
            phoneNumberId: e.WHATSAPP_PHONE_NUMBER_ID,
            verifyToken: e.WHATSAPP_VERIFY_TOKEN,
            businessAccountId: e.WHATSAPP_BUSINESS_ACCOUNT_ID,
            apiVersion: e.WHATSAPP_API_VERSION ?? e.GRAPH_API_VERSION ?? "v27.0",
          }
        : undefined,
    telegram: e.TELEGRAM_BOT_TOKEN
      ? {
          botToken: e.TELEGRAM_BOT_TOKEN,
          secretToken: e.TELEGRAM_WEBHOOK_SECRET_TOKEN ?? telegramSecretFor(e.TELEGRAM_BOT_TOKEN),
        }
      : undefined,
    web: {
      enabled: e.WEB_CHAT,
      turnstileSiteKey: e.TURNSTILE_SITE_KEY,
      turnstileSecretKey: e.TURNSTILE_SECRET_KEY,
    },
    kb: {
      dir: kbDir,
      repo: e.KB_REPO,
      branch: e.KB_BRANCH,
      syncMinutes: e.KB_SYNC_MINUTES,
      githubToken: e.KB_GITHUB_TOKEN,
      acceptCommit: e.KB_ACCEPT_COMMIT,
    },
    databaseUrl: e.DATABASE_URL,
    ai: {
      apiKey: e.OPENROUTER_API_KEY,
      model: e.LLM_MODEL ?? "",
      fallbackModel: e.LLM_FALLBACK_MODEL,
      smallModel: e.LLM_SMALL_MODEL ?? e.LLM_MODEL ?? "",
      timeoutMs: e.LLM_TIMEOUT_MS,
      maxOutputTokens: e.LLM_MAX_OUTPUT_TOKENS,
      contextTokenBudget: e.CONTEXT_TOKEN_BUDGET,
      evalModels: (e.EVAL_MODELS ?? "")
        .split(",")
        .map((m) => m.trim())
        .filter(Boolean),
    },
    sentry: { dsn: e.SENTRY_DSN, environment: e.SENTRY_ENVIRONMENT ?? env },
  };
}

let cached: Config | undefined;

/** The settings for this process (loaded on first use). */
export function config(): Config {
  cached ??= loadConfig();
  return cached;
}

/** Tests only: replace the cached settings. */
export function setConfigForTests(next: Config | undefined): void {
  cached = next;
}
