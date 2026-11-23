import { sql } from "drizzle-orm";
import { afterEach, beforeEach, describe, expect, it } from "vitest";
import type { Database } from "../../src/db/client.ts";
import { DbKbBaselineStore } from "../../src/db/kb-state.ts";
import { Inbox } from "../../src/memory/inbox.ts";
import { MemoryStore, userKey } from "../../src/memory/store.ts";
import { memoryDb } from "../helpers/db.ts";

let database: Database;
let store: MemoryStore;

beforeEach(async () => {
  database = await memoryDb();
  store = new MemoryStore(database.db);
});
afterEach(() => database.close());

describe("userKey", () => {
  it("is a stable keyed hash that never contains the raw id", () => {
    const k = userKey("8801711000000", "secret");
    expect(k).toHaveLength(32);
    expect(k).toBe(userKey("8801711000000", "secret"));
    expect(k).not.toBe(userKey("8801711000000", "other-secret"));
    expect(k).not.toContain("8801711000000");
  });
});

describe("MemoryStore", () => {
  it("creates a person on first contact and remembers them after", async () => {
    expect((await store.touch("u1")).isNew).toBe(true);
    expect((await store.touch("u1")).isNew).toBe(false);
  });

  it("keeps country, profile, summary and turns, and forgets them all on request", async () => {
    await store.touch("u1");
    await store.setCountry("u1", "malaysia");
    await store.setProfile("u1", { stage: "agent found" });
    const a = await store.addTurn("u1", "user", "hello");
    const b = await store.addTurn("u1", "bot", "hi");
    await store.setSummary("u1", "Asked about Malaysia.", b);
    const user = await store.get("u1");
    expect(user).toMatchObject({ country: "malaysia", profile: { stage: "agent found" }, summarisedTo: b });
    expect((await store.recentTurns("u1", 10)).map((t) => t.text)).toEqual(["hello", "hi"]);
    expect((await store.recentTurns("u1", 10, a)).map((t) => t.text)).toEqual(["hi"]);
    expect((await store.turnsBetween("u1", 0, a)).map((t) => t.text)).toEqual(["hello"]);

    await store.forget("u1");
    expect(await store.get("u1")).toBeUndefined();
    expect(await store.recentTurns("u1", 10)).toEqual([]);
  });

  it("returns the newest turns, oldest first", async () => {
    await store.touch("u1");
    for (const t of ["1", "2", "3", "4"]) await store.addTurn("u1", "user", t);
    expect((await store.recentTurns("u1", 2)).map((t) => t.text)).toEqual(["3", "4"]);
  });

  it("deletes messages after 90 days and people 12 months after their last message", async () => {
    await store.touch("old");
    await store.touch("recent");
    await store.addTurn("recent", "user", "old message");
    await store.addTurn("recent", "user", "new message");
    await database.db.execute(
      sql`UPDATE users SET last_seen = now() - interval '366 days' WHERE user_key = 'old'`,
    );
    await database.db.execute(
      sql`UPDATE turns SET created_at = now() - interval '91 days' WHERE text = 'old message'`,
    );
    expect(await store.purge()).toEqual({ turns: 1, users: 1 });
    expect(await store.get("old")).toBeUndefined();
    expect((await store.recentTurns("recent", 10)).map((t) => t.text)).toEqual(["new message"]);
  });
});

describe("Inbox", () => {
  it("records a message once, and returns crash leftovers from the last hour", async () => {
    const inbox = new Inbox(database.db);
    const item = {
      id: "wa:1",
      channel: "whatsapp" as const,
      threadId: "whatsapp:1:2",
      userKey: "u",
      text: "hi",
    };
    expect(await inbox.receive(item)).toBe(true);
    expect(await inbox.receive(item)).toBe(false);
    const later = new Date(Date.now() + 60_000);
    expect((await inbox.leftovers(later)).map((i) => i.id)).toEqual(["wa:1"]);
    await inbox.done("wa:1");
    expect(await inbox.leftovers(later)).toEqual([]);
  });

  it("drops leftovers older than an hour and ones tried three times", async () => {
    const inbox = new Inbox(database.db);
    await inbox.receive({ id: "a", channel: "web", threadId: "t", userKey: "u", text: "x" });
    await inbox.receive({ id: "b", channel: "web", threadId: "t", userKey: "u", text: "y" });
    await database.db.execute(sql`UPDATE inbox SET received_at = now() - interval '2 hours' WHERE id = 'a'`);
    await inbox.retrying("b");
    await inbox.retrying("b");
    expect(await inbox.leftovers(new Date(Date.now() + 60_000))).toEqual([]);
  });
});

describe("DbKbBaselineStore", () => {
  it("saves and loads the last good version of the guides", async () => {
    const s = new DbKbBaselineStore(database.db);
    expect(await s.load()).toBeUndefined();
    await s.save({ commit: "abc", counts: { malaysia: 3 } });
    await s.save({ commit: "def", counts: { malaysia: 4 } });
    expect(await s.load()).toEqual({ commit: "def", counts: { malaysia: 4 } });
  });
});
