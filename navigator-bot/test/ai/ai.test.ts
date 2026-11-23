import { MockLanguageModelV4 } from "ai/test";
import { afterAll, beforeAll, describe, expect, it } from "vitest";
import { AiAnswerer, costOf, toMarkdownBold } from "../../src/ai/answerer.ts";
import { createMemoryUpdater } from "../../src/ai/memory.ts";
import { significantNumbers, unsupportedNumbers } from "../../src/ai/numbers.ts";
import { systemPrompt } from "../../src/ai/prompt.ts";
import type { Database } from "../../src/db/client.ts";
import { Guard } from "../../src/guard/guard.ts";
import { KnowledgeBase } from "../../src/kb/index.ts";
import { MemoryStore } from "../../src/memory/store.ts";
import { memoryDb } from "../helpers/db.ts";
import { makeKb } from "../helpers/kb-fixture.ts";

type DoGenerate = NonNullable<
  NonNullable<ConstructorParameters<typeof MockLanguageModelV4>[0]>["doGenerate"]
>;
type GenerateResult =
  Extract<DoGenerate, (...args: never[]) => unknown> extends (...args: never[]) => PromiseLike<infer R>
    ? R
    : never;

const usage = {
  inputTokens: { total: 10, noCache: 10, cacheRead: 0, cacheWrite: 0 },
  outputTokens: { total: 5, text: 5, reasoning: 0 },
};
const text = (t: string, cost = 0.001) => ({
  content: [{ type: "text" as const, text: t }],
  finishReason: { unified: "stop" as const, raw: "stop" },
  usage,
  providerMetadata: { openrouter: { usage: { cost } } },
  warnings: [],
});
const toolCall = (name: string, input: unknown, id = "c1") => ({
  content: [{ type: "tool-call" as const, toolCallId: id, toolName: name, input: JSON.stringify(input) }],
  finishReason: { unified: "tool-calls" as const, raw: "tool_calls" },
  usage,
  providerMetadata: { openrouter: { usage: { cost: 0.002 } } },
  warnings: [],
});

/** A fake model that returns the given results one after another and records what it was sent. */
function scripted(results: unknown[]) {
  const prompts: unknown[] = [];
  let i = 0;
  const model = new MockLanguageModelV4({
    doGenerate: async (options) => {
      prompts.push(options.prompt);
      const next = results[Math.min(i, results.length - 1)];
      i++;
      return next as GenerateResult;
    },
  });
  return { model, prompts };
}

let kb: KnowledgeBase;
let cleanup: () => Promise<void>;
let database: Database;

beforeAll(async () => {
  const fixture = await makeKb();
  cleanup = fixture.cleanup;
  kb = await KnowledgeBase.build(fixture.dir);
  database = await memoryDb();
});
afterAll(async () => {
  await database.close();
  await cleanup();
});

const emptyContext = { profile: {}, summary: "", turns: [], overflow: undefined };

describe("numbers check", () => {
  it("finds fees, phone numbers and years, ignoring small step numbers", () => {
    expect(significantNumbers("Pay 165,000 taka by 2026. Step 2. Call ০১৭১১")).toEqual([
      "165000",
      "2026",
      "01711",
    ]);
  });
  it("accepts numbers the guides contain and the help lines", () => {
    expect(unsupportedNumbers("The cap is 165,000 taka; call 16135.", ["capped at 165,000 taka"])).toEqual(
      [],
    );
    expect(unsupportedNumbers("The cap is 200,000 taka.", ["capped at 165,000 taka"])).toEqual(["200000"]);
  });
});

describe("helpers", () => {
  it("turns WhatsApp-style bold into Markdown bold, leaving lists and existing bold alone", () => {
    expect(toMarkdownBold("Send *delete my data* now")).toBe("Send **delete my data** now");
    expect(toMarkdownBold("* a list item")).toBe("* a list item");
    expect(toMarkdownBold("already **bold** here")).toBe("already **bold** here");
  });
  it("reads OpenRouter's reported cost", () => {
    expect(costOf({ openrouter: { usage: { cost: 0.0123 } } })).toBe(0.0123);
    expect(costOf(undefined)).toBe(0);
  });
  it("fills the prompt's placeholders and adds what the bot remembers", () => {
    const prompt = systemPrompt(
      kb,
      {
        context: { ...emptyContext, profile: { stage: "abroad" }, summary: "Asked about wages." },
        country: "malaysia",
        channel: "whatsapp",
      },
      new Date("2026-11-24T00:00:00Z"),
    );
    expect(prompt).toContain("Today is 2026-11-24.");
    expect(prompt).toContain("Malaysia (malaysia)");
    expect(prompt).not.toContain("{{");
    expect(prompt).toContain("- stage: abroad");
    expect(prompt).toContain("Asked about wages.");
    expect(prompt).toContain("Guide chosen in this conversation: malaysia.");
  });
});

describe("AiAnswerer", () => {
  const input = (text: string) => ({
    channel: "whatsapp" as const,
    userKey: "u",
    text,
    lang: "en" as const,
    country: "saudi-arabia",
    kb,
    context: emptyContext,
  });

  it("searches, reads a section, answers from it and adds up the cost", async () => {
    const section = kb.sections.find((s) => s.path.includes("Is it open now"));
    const { model, prompts } = scripted([
      toolCall("search_guides", { query: "fees cap", guide: "saudi-arabia" }, "c1"),
      toolCall("read_section", { section_id: section?.id }, "c2"),
      text("Reports say fees are capped at *165,000 taka*."),
    ]);
    const answer = await new AiAnswerer({ model, maxOutputTokens: 500, timeoutMs: 10_000 }).answer(
      input("cost?"),
    );
    expect(answer.text).toBe("Reports say fees are capped at **165,000 taka**.");
    expect(answer.costUsd).toBeCloseTo(0.005);
    expect(JSON.stringify(prompts.at(-1))).toContain("165,000 taka (news report)");
  });

  it("asks again when the answer has a number the guides don't contain", async () => {
    const { model, prompts } = scripted([
      text("The fee is 999,999 taka."),
      text("I couldn't confirm the fee in the guide."),
    ]);
    const answer = await new AiAnswerer({ model, maxOutputTokens: 500, timeoutMs: 10_000 }).answer(
      input("fee?"),
    );
    expect(answer.text).toBe("I couldn't confirm the fee in the guide.");
    expect(JSON.stringify(prompts.at(-1))).toContain("999999");
  });
});

describe("memory updater", () => {
  it("updates the profile card and folds old turns into the summary", async () => {
    const store = new MemoryStore(database.db);
    const guard = new Guard(database.db);
    await store.touch("m1");
    for (let i = 0; i < 6; i++)
      await store.addTurn("m1", i % 2 ? "bot" : "user", `message ${i} ${"word ".repeat(60)}`);
    const { model } = scripted([
      text(JSON.stringify({ destination: "Malaysia", stage: "papers in progress", worries: [] })),
      text("They are getting papers for Malaysia."),
    ]);
    const update = createMemoryUpdater({ model, store, guard, contextTokenBudget: 200, timeoutMs: 10_000 });
    await update({ userKey: "m1", lang: "en", channel: "web" });
    const user = await store.get("m1");
    expect(user?.profile).toEqual({ destination: "Malaysia", stage: "papers in progress" });
    expect(user?.summary).toBe("They are getting papers for Malaysia.");
    expect(user?.summarisedTo).toBeGreaterThan(0);
  });
});
