/**
 * The bot's own tables (Chat SDK keeps its locks and duplicate checks in its own chat_state_* tables).
 * Users appear only as `user_key`, a keyed hash of their WhatsApp number, Telegram id or web session.
 * Change this file, then `npm run db:generate` to write the migration.
 */
import { sql } from "drizzle-orm";
import {
  bigint,
  doublePrecision,
  index,
  integer,
  jsonb,
  pgTable,
  primaryKey,
  text,
  timestamp,
} from "drizzle-orm/pg-core";

/** What the bot remembers about a person between chats: kept 12 months after their last message. */
export const users = pgTable("users", {
  userKey: text("user_key").primaryKey(),
  country: text("country"),
  /** The profile card (destination, job, stage, money paid, agency, worries): see src/memory/profile.ts. */
  profile: jsonb("profile").$type<Record<string, unknown>>().notNull().default({}),
  /** Running summary of turns that no longer fit in the context budget. */
  summary: text("summary").notNull().default(""),
  /** Highest turn id already folded into the summary. */
  summarisedTo: bigint("summarised_to", { mode: "number" }).notNull().default(0),
  createdAt: timestamp("created_at", { withTimezone: true }).notNull().defaultNow(),
  lastSeen: timestamp("last_seen", { withTimezone: true }).notNull().defaultNow(),
});

/** Messages in both directions: kept 90 days. */
export const turns = pgTable(
  "turns",
  {
    id: bigint("id", { mode: "number" }).primaryKey().generatedAlwaysAsIdentity(),
    userKey: text("user_key")
      .notNull()
      .references(() => users.userKey, { onDelete: "cascade" }),
    role: text("role", { enum: ["user", "bot"] }).notNull(),
    text: text("text").notNull(),
    createdAt: timestamp("created_at", { withTimezone: true }).notNull().defaultNow(),
  },
  (t) => [index("turns_user_id").on(t.userKey, t.id), index("turns_created_at").on(t.createdAt)],
);

/**
 * Messages received but not yet answered, so a restart can't lose a reply. A row is deleted as soon as
 * the reply is sent; anything left after a crash is answered at start-up (or dropped after an hour).
 */
export const inbox = pgTable("inbox", {
  id: text("id").primaryKey(),
  channel: text("channel").notNull(),
  threadId: text("thread_id").notNull(),
  userKey: text("user_key").notNull(),
  text: text("text").notNull(),
  attempts: integer("attempts").notNull().default(0),
  receivedAt: timestamp("received_at", { withTimezone: true }).notNull().defaultNow(),
});

export const guardCounts = pgTable("guard_counts", {
  key: text("key").primaryKey(),
  n: integer("n").notNull(),
  expiresAt: timestamp("expires_at", { withTimezone: true }).notNull(),
});

export const guardSpend = pgTable(
  "guard_spend",
  {
    channel: text("channel").notNull(),
    day: integer("day").notNull(),
    usd: doublePrecision("usd").notNull().default(0),
  },
  (t) => [primaryKey({ columns: [t.channel, t.day] })],
);

/** The last version of the guides that passed the safe-swap check. One row. */
export const kbState = pgTable("kb_state", {
  id: integer("id").primaryKey().default(1),
  commit: text("commit"),
  counts: jsonb("counts").$type<Record<string, number>>().notNull(),
  updatedAt: timestamp("updated_at", { withTimezone: true }).notNull().default(sql`now()`),
});
