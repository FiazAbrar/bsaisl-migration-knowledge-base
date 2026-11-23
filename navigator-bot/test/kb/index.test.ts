import { writeFile } from "node:fs/promises";
import path from "node:path";
import { afterAll, beforeAll, describe, expect, it } from "vitest";
import { compareCounts, KnowledgeBase, snippet, terms } from "../../src/kb/index.ts";
import { type KbBaseline, KbService } from "../../src/kb/service.ts";
import { makeKb } from "../helpers/kb-fixture.ts";

let kbDir: string;
let cleanup: () => Promise<void>;
let kb: KnowledgeBase;

beforeAll(async () => {
  ({ dir: kbDir, cleanup } = await makeKb());
  kb = await KnowledgeBase.build(kbDir);
});
afterAll(() => cleanup());

describe("KnowledgeBase.build", () => {
  it("finds guides, skipping sources/ and the bot folder", () => {
    expect(kb.guides.map((g) => [g.slug, g.kind])).toEqual([
      ["malaysia", "country"],
      ["saudi-arabia", "country"],
      ["faq", "shared"],
    ]);
  });

  it("labels sources from facts.csv and sources.csv", () => {
    expect(kb.sourcesFor("saudi-arabia", ["A0001", "N0002"])).toEqual([
      expect.objectContaining({ id: "A0001", publisher: "BMET", sourceType: "official" }),
      expect.objectContaining({ id: "N0002", publisher: "Prothom Alo", sourceType: "news" }),
    ]);
  });

  it("counts sections per guide", () => {
    expect(kb.sectionCounts()).toEqual({ "saudi-arabia": 4, malaysia: 1, faq: 1 });
  });
});

describe("KnowledgeBase.search", () => {
  it("finds sections within one guide, headings first", () => {
    const hits = kb.search("medical test", "saudi-arabia");
    expect(hits[0]?.path).toBe("Work visa > Step 2: Medical test");
    expect(hits.every((h) => h.slug === "saudi-arabia")).toBe(true);
  });

  it("matches any of the words and stems English", () => {
    expect(kb.search("calling visas", "malaysia")[0]?.path).toBe("Work visa > Step 1: Calling visa");
  });

  it("returns nothing for stopwords only", () => {
    expect(kb.search("what is the")).toEqual([]);
  });

  it("matches Bangla words whole, vowel signs included", async () => {
    const extra = await makeKb({ "countries/oman/doc.md": "# Oman\n\n## ভিসা খরচ\n\nভিসার খরচ কত টাকা\n" });
    const k = await KnowledgeBase.build(extra.dir);
    expect(k.search("ভিসা", "oman")[0]?.path).toBe("ভিসা খরচ");
    await extra.cleanup();
  });
});

describe("helpers", () => {
  it("stems English terms and keeps Bangla", () => {
    expect(terms("Visas ভিসা")).toEqual(["visa", "ভিসা"]);
  });
  it("cuts a snippet around the query words", () => {
    const text = `${"filler ".repeat(40)}the medical test is here ${"filler ".repeat(40)}`;
    const s = snippet(text, terms("medical"), 6);
    expect(s).toContain("medical");
    expect(s.startsWith("…")).toBe(true);
  });
});

describe("compareCounts", () => {
  it("refuses a vanished guide or one that lost more than half of 20+ sections", () => {
    expect(compareCounts({ a: 30, b: 5 }, { a: 30, b: 5 })).toEqual([]);
    expect(compareCounts({ a: 30, b: 5 }, { b: 5 })).toEqual(["guide 'a' disappeared"]);
    expect(compareCounts({ a: 30 }, { a: 14 })).toEqual(["guide 'a' shrank from 30 to 14 sections"]);
    expect(compareCounts({ a: 30 }, { a: 15 })).toEqual([]);
    expect(compareCounts({ a: 10 }, { a: 1 })).toEqual([]);
  });
});

describe("KbService (local guides)", () => {
  function memoryStore(initial?: KbBaseline) {
    let saved = initial;
    return {
      load: async () => saved,
      save: async (b: KbBaseline) => {
        saved = b;
      },
      get: () => saved,
    };
  }

  it("loads local guides, remembers them, and refuses a later broken version", async () => {
    const local = await makeKb();
    const store = memoryStore();
    const alerts: string[] = [];
    const svc = new KbService({
      dir: local.dir,
      repo: undefined,
      branch: "main",
      syncMinutes: 60,
      githubToken: undefined,
      store,
      onAlert: (m) => alerts.push(m),
    });
    expect(await svc.refresh(true)).toBe(true);
    expect(store.get()?.counts["saudi-arabia"]).toBe(4);

    // Saudi grows to 30 sections, then is cut to 3: the cut is refused and the bot keeps 30.
    const big = `# Saudi\n\n${Array.from({ length: 30 }, (_, i) => `## S${i}\n\nText ${i}\n`).join("\n")}`;
    await writeFile(path.join(local.dir, "countries/saudi-arabia/doc.md"), big);
    expect(await svc.refresh(false)).toBe(true);
    await writeFile(
      path.join(local.dir, "countries/saudi-arabia/doc.md"),
      "# Saudi\n\n## A\n\nx\n\n## B\n\ny\n\n## C\n\nz\n",
    );
    expect(await svc.refresh(false)).toBe(false);
    expect(svc.current.sectionCounts()["saudi-arabia"]).toBe(30);
    expect(svc.status.indexRefused).toContain("shrank from 30 to 3");
    expect(alerts).toHaveLength(1);
    svc.stop();
    await local.cleanup();
  });
});
