/**
 * Restart safety. Every message is written here before it is answered and deleted once the reply is sent.
 * At start-up, anything left from the last hour (the server restarted mid-answer) is answered again;
 * older leftovers are dropped. The raw thread id (needed to reply) stays here only until the reply is sent.
 */
import { and, asc, eq, gt, lt, sql } from "drizzle-orm";
import type { Db } from "../db/client.ts";
import { inbox } from "../db/schema.ts";
import type { Channel } from "./store.ts";

export const REPLAY_WINDOW_MS = 60 * 60_000;
export const MAX_ATTEMPTS = 3;

export interface InboxItem {
  id: string;
  channel: Channel;
  threadId: string;
  userKey: string;
  text: string;
  attempts: number;
}

export class Inbox {
  private readonly db: Db;

  constructor(db: Db) {
    this.db = db;
  }

  /** Record a message before answering it. Returns false if it is already there (a repeat delivery). */
  async receive(item: Omit<InboxItem, "attempts">): Promise<boolean> {
    const rows = await this.db
      .insert(inbox)
      .values({ ...item, attempts: 1 })
      .onConflictDoNothing()
      .returning({ id: inbox.id });
    return rows.length === 1;
  }

  async done(id: string): Promise<void> {
    await this.db.delete(inbox).where(eq(inbox.id, id));
  }

  /** Messages left unanswered by a crash: received within the window, before `before`, not tried too often. */
  async leftovers(before: Date, now = new Date()): Promise<InboxItem[]> {
    const since = new Date(now.getTime() - REPLAY_WINDOW_MS);
    await this.db.delete(inbox).where(lt(inbox.receivedAt, since));
    const rows = await this.db
      .select()
      .from(inbox)
      .where(and(gt(inbox.receivedAt, since), lt(inbox.receivedAt, before), lt(inbox.attempts, MAX_ATTEMPTS)))
      .orderBy(asc(inbox.receivedAt));
    return rows.map((r) => ({ ...r, channel: r.channel as Channel }));
  }

  async retrying(id: string): Promise<void> {
    await this.db
      .update(inbox)
      .set({ attempts: sql`${inbox.attempts} + 1` })
      .where(eq(inbox.id, id));
  }
}
