/**
 * What the bot remembers about each person: the guide they asked about, a short profile card, a running
 * summary and the recent messages. People are stored only as a keyed hash of their channel id.
 *
 * Retention (docs/PRIVACY.md): messages are deleted after 90 days; the person (profile, summary, guide)
 * 12 months after their last message. "delete my data" removes everything at once.
 */
import { createHmac } from "node:crypto";
import { and, asc, desc, eq, gt, lt, sql } from "drizzle-orm";
import type { Db } from "../db/client.ts";
import { turns, users } from "../db/schema.ts";

export const TURN_RETENTION_DAYS = 90;
export const USER_RETENTION_DAYS = 365;

export type Channel = "whatsapp" | "telegram" | "web";

/** A person's id as stored: HMAC-SHA256 of their channel id, so a database leak reveals no numbers. */
export function userKey(rawId: string, secret: string): string {
  return createHmac("sha256", secret).update(rawId).digest("hex").slice(0, 32);
}

export interface Turn {
  id: number;
  role: "user" | "bot";
  text: string;
  createdAt: Date;
}

export interface UserRecord {
  userKey: string;
  country: string | null;
  profile: Record<string, unknown>;
  summary: string;
  summarisedTo: number;
  createdAt: Date;
  lastSeen: Date;
}

export class MemoryStore {
  private readonly db: Db;

  constructor(db: Db) {
    this.db = db;
  }

  /** The person's record, created on first contact. `isNew` is true the first time. */
  async touch(key: string): Promise<{ user: UserRecord; isNew: boolean }> {
    const rows = await this.db
      .insert(users)
      .values({ userKey: key })
      .onConflictDoUpdate({ target: users.userKey, set: { lastSeen: sql`now()` } })
      .returning({
        userKey: users.userKey,
        country: users.country,
        profile: users.profile,
        summary: users.summary,
        summarisedTo: users.summarisedTo,
        createdAt: users.createdAt,
        lastSeen: users.lastSeen,
        // Postgres: xmax is 0 on a freshly inserted row and set when an existing row was updated.
        inserted: sql<boolean>`(xmax = 0)`,
      });
    const row = rows[0];
    if (!row) throw new Error("Could not save the user");
    const { inserted, ...user } = row;
    return { user, isNew: Boolean(inserted) };
  }

  async get(key: string): Promise<UserRecord | undefined> {
    const rows = await this.db.select().from(users).where(eq(users.userKey, key)).limit(1);
    return rows[0];
  }

  async setCountry(key: string, slug: string): Promise<void> {
    await this.db.update(users).set({ country: slug }).where(eq(users.userKey, key));
  }

  async setProfile(key: string, profile: Record<string, unknown>): Promise<void> {
    await this.db.update(users).set({ profile }).where(eq(users.userKey, key));
  }

  async setSummary(key: string, summary: string, summarisedTo: number): Promise<void> {
    await this.db.update(users).set({ summary, summarisedTo }).where(eq(users.userKey, key));
  }

  async addTurn(key: string, role: "user" | "bot", text: string): Promise<number> {
    const rows = await this.db.insert(turns).values({ userKey: key, role, text }).returning({ id: turns.id });
    return rows[0]?.id ?? 0;
  }

  /** The newest turns (up to `limit`), oldest first, after turn id `afterId`. */
  async recentTurns(key: string, limit: number, afterId = 0): Promise<Turn[]> {
    const rows = await this.db
      .select({ id: turns.id, role: turns.role, text: turns.text, createdAt: turns.createdAt })
      .from(turns)
      .where(and(eq(turns.userKey, key), gt(turns.id, afterId)))
      .orderBy(desc(turns.id))
      .limit(limit);
    return rows.reverse();
  }

  /** Turns from `fromId` (exclusive) to `toId` (inclusive), oldest first: what a summary update folds in. */
  async turnsBetween(key: string, fromId: number, toId: number): Promise<Turn[]> {
    return this.db
      .select({ id: turns.id, role: turns.role, text: turns.text, createdAt: turns.createdAt })
      .from(turns)
      .where(and(eq(turns.userKey, key), gt(turns.id, fromId), sql`${turns.id} <= ${toId}`))
      .orderBy(asc(turns.id));
  }

  /** Delete everything stored about one person ("delete my data" and "reset"). */
  async forget(key: string): Promise<void> {
    await this.db.delete(users).where(eq(users.userKey, key)); // turns go with it (ON DELETE CASCADE)
  }

  /** Apply the retention rules. Returns how many rows were deleted. */
  async purge(now = new Date()): Promise<{ turns: number; users: number }> {
    const turnCutoff = new Date(now.getTime() - TURN_RETENTION_DAYS * 86_400_000);
    const userCutoff = new Date(now.getTime() - USER_RETENTION_DAYS * 86_400_000);
    const t = await this.db.delete(turns).where(lt(turns.createdAt, turnCutoff)).returning({ id: turns.id });
    const u = await this.db
      .delete(users)
      .where(lt(users.lastSeen, userCutoff))
      .returning({ k: users.userKey });
    return { turns: t.length, users: u.length };
  }
}
