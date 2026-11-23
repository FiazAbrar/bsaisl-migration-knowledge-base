/**
 * One JSON logger for the whole bot. Secrets and user identifiers are redacted by key, and helpers below
 * keep phone numbers and tokens out of free-text messages.
 */
import pino from "pino";

const REDACT = [
  "*.token",
  "*.accessToken",
  "*.apiKey",
  "*.secret",
  "*.password",
  "*.authorization",
  "*.phone",
  "*.wa_id",
  "*.from",
  "*.threadId",
  "*.text",
  "req.headers.authorization",
  "req.headers.cookie",
];

function level(): string {
  if (process.env.NODE_ENV === "test") return process.env.LOG_LEVEL || "silent";
  return process.env.LOG_LEVEL || "info";
}

export const logger = pino({
  level: level(),
  base: { service: "navigator-bot" },
  redact: { paths: REDACT, censor: "[redacted]" },
  timestamp: pino.stdTimeFunctions.isoTime,
});

/** Remove anything that looks like a phone number, bot token or bearer token from a message. */
export function scrub(message: string): string {
  return message
    .replace(/bot\d{6,}:[\w-]{20,}/g, "bot[redacted]")
    .replace(/Bearer\s+[\w.-]+/gi, "Bearer [redacted]")
    .replace(/\+?\d[\d\s-]{8,}\d/g, "[number]");
}

/** An error's type and scrubbed message, safe to log. */
export function describeError(err: unknown): { type: string; message: string } {
  if (err instanceof Error) return { type: err.name, message: scrub(err.message).slice(0, 500) };
  return { type: typeof err, message: scrub(String(err)).slice(0, 500) };
}
