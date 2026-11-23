/**
 * Abuse limits and daily AI spending caps, shared by every channel. Every message is checked before any
 * answer is worked out, so a flood costs almost nothing. Days run on Bangladesh time (UTC+6).
 *
 * Limits come from the environment (read on every check, so the host can change them without a
 * redeploy). Defaults are lenient, for testing; the suggested public values are in brackets.
 * - Per person, by channel (WhatsApp and Telegram users are real numbers, so they get more room):
 *     web       GUARD_WEB_PER_MINUTE 20 [6],       GUARD_WEB_PER_DAY 200 [40]
 *     whatsapp  GUARD_WHATSAPP_PER_MINUTE 30 [20], GUARD_WHATSAPP_PER_DAY 500 [150]
 *     telegram  GUARD_TELEGRAM_PER_MINUTE 30 [15], GUARD_TELEGRAM_PER_DAY 500 [100]
 * - Web, per IP address: GUARD_IP_PER_DAY 1000 [200]; new sessions GUARD_SESSIONS_PER_HOUR 60 [20].
 *   Loose on purpose: Bangladeshi mobile operators put many customers behind one IP address.
 * - Web, all visitors together: GUARD_WEB_ALL_PER_MINUTE 200 [60].
 * - "reset" and "delete my data": GUARD_COMMANDS_PER_MINUTE 30, never counted toward the daily limit.
 * - AI spending per channel per day (USD): BUDGET_WEB_USD 3, BUDGET_WHATSAPP_USD 10, BUDGET_TELEGRAM_USD 3.
 *   When one channel's budget is spent only that channel pauses.
 *
 * A refused message is not counted. Only the first refusal in a window is "notify", so a flood gets one
 * reply, not hundreds. Counting is atomic in Postgres, so several bot instances share the limits exactly.
 */
import { eq, lt, sql } from "drizzle-orm";
import type { Db, Tx } from "../db/client.ts";
import { guardCounts, guardSpend } from "../db/schema.ts";
import type { Channel } from "../memory/store.ts";
import { logger } from "../ops/logger.ts";

export const BD_OFFSET_S = 6 * 3600;
export const MINUTE = 60;
export const HOUR = 3600;
export const DAY = 86_400;
export const MAX_CHARS = 500;

export const DEFAULT_LIMITS = {
  GUARD_WEB_PER_MINUTE: 20,
  GUARD_WEB_PER_DAY: 200,
  GUARD_WHATSAPP_PER_MINUTE: 30,
  GUARD_WHATSAPP_PER_DAY: 500,
  GUARD_TELEGRAM_PER_MINUTE: 30,
  GUARD_TELEGRAM_PER_DAY: 500,
  GUARD_IP_PER_DAY: 1000,
  GUARD_SESSIONS_PER_HOUR: 60,
  GUARD_WEB_ALL_PER_MINUTE: 200,
  GUARD_COMMANDS_PER_MINUTE: 30,
  BUDGET_WEB_USD: 3,
  BUDGET_WHATSAPP_USD: 10,
  BUDGET_TELEGRAM_USD: 3,
} as const;

export type LimitName = keyof typeof DEFAULT_LIMITS;

export type RefusalReason = "minute" | "day" | "ip" | "sessions" | "busy" | "budget";

export interface Decision {
  ok: boolean;
  reason?: RefusalReason;
  /** Seconds until the limit resets. */
  retryAfter?: number;
  /** False after the first refusal in a window, so a flood gets no further replies. */
  notify?: boolean;
}

/** A limit from the environment, or its default. */
export function limit(name: LimitName, env: NodeJS.ProcessEnv = process.env): number {
  const raw = env[name];
  const value = raw === undefined || raw.trim() === "" ? Number.NaN : Number(raw);
  return Number.isFinite(value) ? value : DEFAULT_LIMITS[name];
}

export function bucket(windowS: number, nowS: number): number {
  return Math.floor((nowS + BD_OFFSET_S) / windowS);
}

export function bucketEnd(windowS: number, nowS: number): number {
  return (bucket(windowS, nowS) + 1) * windowS - BD_OFFSET_S;
}

interface Rule {
  key: string;
  windowS: number;
  limit: number;
  reason: RefusalReason;
}

const upper = (c: Channel) => c.toUpperCase() as "WEB" | "WHATSAPP" | "TELEGRAM";

/** Thrown inside a transaction to undo the counting of a refused message. */
class Refused extends Error {
  readonly rule: Rule;
  constructor(rule: Rule) {
    super("refused");
    this.rule = rule;
  }
}

export class Guard {
  private readonly db: Db;
  private readonly now: () => number;
  private lastPurge = 0;

  /** `now` returns seconds since 1970 (replaceable in tests). */
  constructor(db: Db, now: () => number = () => Date.now() / 1000) {
    this.db = db;
    this.now = now;
  }

  /** Before answering one message. `user` and `ip` are hashes. */
  async check(channel: Channel, user: string, ip?: string): Promise<Decision> {
    const ch = upper(channel);
    const rules: Rule[] = [
      {
        key: `${channel}:u:${user}`,
        windowS: MINUTE,
        limit: limit(`GUARD_${ch}_PER_MINUTE`),
        reason: "minute",
      },
      { key: `${channel}:u:${user}`, windowS: DAY, limit: limit(`GUARD_${ch}_PER_DAY`), reason: "day" },
    ];
    if (ip)
      rules.push({
        key: `${channel}:ip:${ip}`,
        windowS: DAY,
        limit: limit("GUARD_IP_PER_DAY"),
        reason: "ip",
      });
    if (channel === "web") {
      rules.push({
        key: "web:all",
        windowS: MINUTE,
        limit: limit("GUARD_WEB_ALL_PER_MINUTE"),
        reason: "busy",
      });
    }
    return this.apply(rules, channel);
  }

  /** Before "reset" or "delete my data": a loose per-minute limit that never blocks them for the day. */
  async command(channel: Channel, user: string): Promise<Decision> {
    return this.apply([
      {
        key: `${channel}:cmd:${user}`,
        windowS: MINUTE,
        limit: limit("GUARD_COMMANDS_PER_MINUTE"),
        reason: "minute",
      },
    ]);
  }

  /** Before giving a web visitor a new chat session. `ip` is a hash. */
  async newSession(ip: string): Promise<Decision> {
    return this.apply([
      {
        key: `sessions:ip:${ip}`,
        windowS: HOUR,
        limit: limit("GUARD_SESSIONS_PER_HOUR"),
        reason: "sessions",
      },
    ]);
  }

  /** Record what one AI reply cost. Warns once when a channel passes 80% of its daily budget. */
  async addCost(channel: Channel, usd: number): Promise<void> {
    if (!(usd > 0)) return;
    const day = bucket(DAY, this.now());
    const rows = await this.db
      .insert(guardSpend)
      .values({ channel, day, usd })
      .onConflictDoUpdate({
        target: [guardSpend.channel, guardSpend.day],
        set: { usd: sql`${guardSpend.usd} + ${usd}` },
      })
      .returning({ usd: guardSpend.usd });
    const after = rows[0]?.usd ?? usd;
    const budget = limit(`BUDGET_${upper(channel)}_USD`);
    if (after - usd < 0.8 * budget && 0.8 * budget <= after) {
      logger.warn({ channel, spent: after, budget }, "A channel has used 80% of today's AI budget");
    }
  }

  /** Today's spending per channel (kept off the public /health page). */
  async spending(): Promise<Record<Channel, { spentUsd: number; budgetUsd: number }>> {
    const day = bucket(DAY, this.now());
    const out = {} as Record<Channel, { spentUsd: number; budgetUsd: number }>;
    for (const ch of ["web", "whatsapp", "telegram"] as const) {
      out[ch] = { spentUsd: await this.spent(this.db, ch, day), budgetUsd: limit(`BUDGET_${upper(ch)}_USD`) };
    }
    return out;
  }

  private async spent(db: Db | Tx, channel: Channel, day: number): Promise<number> {
    const rows = await db
      .select({ usd: guardSpend.usd })
      .from(guardSpend)
      .where(sql`${guardSpend.channel} = ${channel} AND ${guardSpend.day} = ${day}`)
      .limit(1);
    return rows[0]?.usd ?? 0;
  }

  private async apply(rules: Rule[], channel?: Channel): Promise<Decision> {
    const nowS = this.now();
    if (channel) {
      const spent = await this.spent(this.db, channel, bucket(DAY, nowS));
      if (spent >= limit(`BUDGET_${upper(channel)}_USD`)) {
        return this.refuse(
          {
            ...(rules[0] as Rule),
            key: `budget:${channel}:${rules[0]?.key}`,
            windowS: DAY,
            reason: "budget",
          },
          nowS,
        );
      }
    }
    try {
      // Count the message against every rule; if any is now over its limit, undo it all and refuse.
      await this.db.transaction(async (tx) => {
        for (const rule of rules) {
          const n = await this.increment(tx, this.bucketKey(rule, nowS), bucketEnd(rule.windowS, nowS) + 60);
          if (n > rule.limit) throw new Refused(rule);
        }
      });
    } catch (err) {
      if (err instanceof Refused)
        return this.refuse({ ...err.rule, key: this.bucketKey(err.rule, nowS) }, nowS);
      throw err;
    }
    await this.maybePurge(nowS);
    return { ok: true };
  }

  private bucketKey(rule: Rule, nowS: number): string {
    return `${rule.key}:${rule.windowS}:${bucket(rule.windowS, nowS)}`;
  }

  private async refuse(rule: Rule, nowS: number): Promise<Decision> {
    const end = bucketEnd(rule.windowS, nowS);
    const first = (await this.increment(this.db, `refused:${rule.key}`, end + 60)) === 1;
    return { ok: false, reason: rule.reason, retryAfter: Math.max(1, Math.floor(end - nowS)), notify: first };
  }

  private async increment(db: Db | Tx, key: string, expiresS: number): Promise<number> {
    const rows = await db
      .insert(guardCounts)
      .values({ key, n: 1, expiresAt: new Date(expiresS * 1000) })
      .onConflictDoUpdate({ target: guardCounts.key, set: { n: sql`${guardCounts.n} + 1` } })
      .returning({ n: guardCounts.n });
    return rows[0]?.n ?? 1;
  }

  private async maybePurge(nowS: number): Promise<void> {
    if (nowS - this.lastPurge < HOUR) return;
    this.lastPurge = nowS;
    await this.db.delete(guardCounts).where(lt(guardCounts.expiresAt, new Date(nowS * 1000)));
    await this.db.delete(guardSpend).where(lt(guardSpend.day, bucket(DAY, nowS) - 60));
  }

  /** Tests and admin: forget a counter. */
  async clear(key: string): Promise<void> {
    await this.db.delete(guardCounts).where(eq(guardCounts.key, key));
  }
}
