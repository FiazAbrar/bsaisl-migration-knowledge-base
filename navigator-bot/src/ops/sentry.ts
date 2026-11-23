/**
 * Error alerts. With SENTRY_DSN set, crashes, failed answers and refused guide updates reach Sentry
 * (sentry.io, free plan), which emails the team. Without it, they are only logged.
 * Personal data is not sent: no request bodies, cookies, IP addresses or message texts.
 */
import * as Sentry from "@sentry/node";
import { logger, scrub } from "./logger.ts";

let enabled = false;

export function initSentry(dsn: string | undefined, environment: string, release?: string): void {
  if (!dsn) return;
  Sentry.init({
    dsn,
    environment,
    ...(release ? { release } : {}),
    includeServerName: false,
    tracesSampleRate: 0,
    beforeSend(event) {
      if (event.request) {
        delete event.request.data;
        delete event.request.cookies;
        delete event.request.headers;
        delete event.request.query_string;
      }
      delete event.user;
      if (event.message) event.message = scrub(event.message);
      for (const ex of event.exception?.values ?? []) if (ex.value) ex.value = scrub(ex.value);
      return event;
    },
  });
  enabled = true;
  logger.info("Error alerts go to Sentry");
}

export function captureError(err: unknown, tags: Record<string, string> = {}): void {
  if (enabled) Sentry.captureException(err, { tags });
}

/** An alert that is not an exception: a refused guide update, a budget nearly spent. */
export function alert(message: string, tags: Record<string, string> = {}): void {
  logger.warn({ tags }, message);
  if (enabled) Sentry.captureMessage(scrub(message), { level: "warning", tags });
}

export async function flushSentry(): Promise<void> {
  if (enabled) await Sentry.flush(2000);
}
