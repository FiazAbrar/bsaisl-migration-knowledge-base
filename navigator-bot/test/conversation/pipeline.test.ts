import { afterAll, afterEach, beforeAll, beforeEach, describe, expect, it, vi } from "vitest";
import { type Answerer, TestModeAnswerer } from "../../src/conversation/answerer.ts";
import { buildContext, estimateTokens } from "../../src/conversation/context.ts";
import { MESSAGES } from "../../src/conversation/i18n.ts";
import { Conversation, type IncomingMessage } from "../../src/conversation/pipeline.ts";
import type { Database } from "../../src/db/client.ts";
import { Guard } from "../../src/guard/guard.ts";
import { KnowledgeBase } from "../../src/kb/index.ts";
import { MemoryStore } from "../../src/memory/store.ts";
import { memoryDb } from "../helpers/db.ts";
import { makeKb } from "../helpers/kb-fixture.ts";

let kb: KnowledgeBase;
let cleanupKb: () => Promise<void>;
let database: Database;
let store: MemoryStore;

beforeAll(async () => {
  const fixture = await makeKb();
  cleanupKb = fixture.cleanup;
  kb = await KnowledgeBase.build(fixture.dir);
  database = await memoryDb();
});
afterAll(async () => {
  await database.close();
  await cleanupKb();
});

let userN = 0;
let user: string;
beforeEach(() => {
  store = new MemoryStore(database.db);
  user = `user-${++userN}`;
});
afterEach(() => vi.unstubAllEnvs());

function conversation(answerer: Answerer = new TestModeAnswerer()) {
  return new Conversation({
    kb: () => kb,
    store,
    guard: new Guard(database.db),
    answerer,
    contextTokenBudget: 3000,
    privacyLink: "https://bot.example/privacy",
  });
}

const msg = (text: string, extra: Partial<IncomingMessage> = {}): IncomingMessage => ({
  channel: "whatsapp",
  userKey: user,
  kind: "text",
  text,
  ...extra,
});

describe("Conversation", () => {
  it("asks for text when a voice note or photo arrives, in both languages", async () => {
    const reply = await conversation().handle({ channel: "whatsapp", userKey: user, kind: "other" });
    expect(reply?.text).toContain(MESSAGES.bn.sendText);
    expect(reply?.text).toContain(MESSAGES.en.sendText);
  });

  it("welcomes a first 'hi' with the country list and the privacy notice", async () => {
    const reply = await conversation().handle(msg("hi"));
    expect(reply?.text).toContain("I have guides for: Saudi Arabia, Malaysia");
    expect(reply?.text).toContain("Privacy:");
    expect(reply?.text).toContain("https://bot.example/privacy");
    // Second time: no privacy notice.
    expect((await conversation().handle(msg("hello")))?.text).not.toContain("Privacy:");
  });

  it("replies in Bangla to Bangla", async () => {
    const reply = await conversation().handle(msg("হাই"));
    expect(reply?.lang).toBe("bn");
    expect(reply?.text).toContain("যেসব দেশের গাইড আছে: সৌদি আরব, মালয়েশিয়া");
  });

  it("remembers the guide and searches it", async () => {
    const c = conversation();
    const first = await c.handle(msg("Saudi Arabia"));
    expect(first?.text).toContain("OK, the **Saudi Arabia** guide.");
    expect(first?.country).toBe("saudi-arabia");
    const second = await c.handle(msg("medical test"));
    expect(second?.text).toContain("Closest sections in the **Saudi Arabia** guide:");
    expect(second?.text).toContain("**Work visa > Step 2: Medical test**");
    expect((await store.get(user))?.country).toBe("saudi-arabia");
  });

  it("asks which country when none is known, and ignores a saved guide that no longer exists", async () => {
    await store.touch(user);
    await store.setCountry(user, "atlantis");
    const reply = await conversation().handle(msg("visa fees"));
    expect(reply?.text).toContain("Which country are you asking about?");
  });

  it("removes personal numbers before storing and says so", async () => {
    const reply = await conversation().handle(msg("Malaysia, my passport is AB1234567"));
    expect(reply?.text).toContain(MESSAGES.en.personalRemoved);
    const turns = await store.recentTurns(user, 10);
    expect(turns[0]?.text).toBe("Malaysia, my passport is [number removed]");
  });

  it("deletes everything on 'delete my data' and starts over on 'reset'", async () => {
    const c = conversation();
    await c.handle(msg("Malaysia"));
    expect((await c.handle(msg("reset")))?.text).toBe(MESSAGES.en.reset);
    expect(await store.get(user)).toBeUndefined();
    await c.handle(msg("Malaysia"));
    expect((await c.handle(msg("আমার তথ্য মুছে দিন")))?.text).toBe(MESSAGES.bn.deleted);
    expect(await store.recentTurns(user, 10)).toEqual([]);
  });

  it("refuses long messages every time, and floods only once", async () => {
    const c = conversation();
    expect((await c.handle(msg("x".repeat(501))))?.text).toBe(MESSAGES.en.tooLong);
    vi.stubEnv("GUARD_WHATSAPP_PER_MINUTE", "1");
    await c.handle(msg("Malaysia"));
    expect((await c.handle(msg("calling visa")))?.text).toBe(MESSAGES.en.refusal.minute);
    expect(await c.handle(msg("calling visa"))).toBeNull();
  });

  it("answers /start with the welcome", async () => {
    const reply = await conversation().handle(msg("/start@NavigatorBot", { channel: "telegram" }));
    expect(reply?.text).toContain("Hello! I answer questions");
  });

  it("apologises when answering fails, and records AI cost", async () => {
    const failing: Answerer = { mode: "ai", answer: () => Promise.reject(new Error("model down")) };
    expect((await conversation(failing).handle(msg("Malaysia visa")))?.text).toBe(MESSAGES.en.error);
    const costly: Answerer = { mode: "ai", answer: async () => ({ text: "answer", costUsd: 0.25 }) };
    const guard = new Guard(database.db);
    const before = (await guard.spending()).whatsapp.spentUsd;
    await conversation(costly).handle(msg("Malaysia visa"));
    expect((await guard.spending()).whatsapp.spentUsd).toBeCloseTo(before + 0.25);
  });
});

describe("buildContext", () => {
  it("keeps the newest turns that fit the budget and reports the rest for the summary", async () => {
    await store.touch(user);
    const ids: number[] = [];
    for (let i = 0; i < 6; i++)
      ids.push(await store.addTurn(user, i % 2 ? "bot" : "user", "word ".repeat(40)));
    const u = await store.get(user);
    if (!u) throw new Error("no user");
    const perTurn = estimateTokens("word ".repeat(40)) + 4;
    const ctx = await buildContext(store, u, perTurn * 2);
    expect(ctx.turns.map((t) => t.id)).toEqual(ids.slice(-2));
    expect(ctx.overflow).toEqual({ fromId: 0, toId: ids[3] });
  });

  it("counts Bangla as more tokens per letter", () => {
    expect(estimateTokens("ভিসা")).toBeGreaterThan(estimateTokens("visa"));
  });
});
