import { describe, expect, it } from "vitest";
import {
  citationMarker,
  MAX_WORDS,
  OPEN_QUESTIONS_LABEL,
  parseDoc,
  splitLong,
  withoutOpenQuestions,
} from "../../src/kb/parse.ts";
import { SAUDI_DOC } from "../helpers/kb-fixture.ts";

const kinds = new Map([
  ["A0001", { sourceType: "official", year: "2026" }],
  ["N0002", { sourceType: "news", year: "2026" }],
  ["N0003", { sourceType: "news", year: "2023" }],
  ["A0004", { sourceType: "official", year: "2022" }],
]);

describe("citationMarker", () => {
  it("hides official sources and marks news-only claims", () => {
    expect(citationMarker(["A0001"], kinds)).toBe("");
    expect(citationMarker(["A0001", "N0002"], kinds)).toBe("");
    expect(citationMarker(["N0002"], kinds)).toBe(" (news report)");
  });
  it("adds the year when the newest source is older than 2025", () => {
    expect(citationMarker(["N0003"], kinds)).toBe(" (news report, 2023)");
    expect(citationMarker(["A0004"], kinds)).toBe(" (2022)");
  });
  it("drops unknown ids", () => {
    expect(citationMarker(["Z9999"], kinds)).toBe("");
  });
});

describe("parseDoc", () => {
  const doc = parseDoc(SAUDI_DOC, "saudi-arabia", kinds);

  it("takes the title from the # heading", () => {
    expect(doc.title).toBe("Saudi Arabia: working there");
  });

  it("builds section paths from parent headings and keeps text before the first heading", () => {
    expect(doc.sections.map((s) => s.path)).toEqual([
      "Introduction",
      "Background > Is it open now?",
      "Work visa > Step 1: Find a job",
      "Work visa > Step 2: Medical test",
    ]);
  });

  it("replaces citations with markers and collects fact ids", () => {
    const open = doc.sections[1];
    expect(open?.text).toContain("The corridor is open. Fees are capped at 165,000 taka (news report).");
    expect(open?.facts).toEqual(["A0001", "N0002"]);
    expect(doc.sections[3]?.text).toContain("GAMCA medical test (news report, 2023).");
  });

  it("turns Need to know blocks into open questions", () => {
    const open = doc.sections[1];
    expect(open?.openQuestions).toBe(true);
    expect(open?.text).toContain(OPEN_QUESTIONS_LABEL);
    expect(open?.text).toContain("  - What does a house-driver visa sell for in Dhaka?");
    expect(doc.sections[2]?.openQuestions).toBe(false);
  });

  it("finds a Need to know block indented inside a numbered step", () => {
    const md = [
      "# T",
      "",
      "## Step 1",
      "",
      "1. **Enrol** on OEP.",
      "",
      "   > **Need to know**",
      "   > - Does the app still work?",
      "",
      "2. **Attend** all 3 days.",
    ].join("\n");
    const s = parseDoc(md, "x").sections[0];
    expect(s?.openQuestions).toBe(true);
    expect(s?.text).toContain(`   ${OPEN_QUESTIONS_LABEL}\n     - Does the app still work?`);
    expect(s?.text).not.toContain("**Need to know**");
  });

  it("removes citations from headings", () => {
    const d = parseDoc("# T\n\n## Fees [A0001]\n\nText\n", "x");
    expect(d.sections[0]?.path).toBe("Fees");
  });

  it("skips headings with no text under them", () => {
    const d = parseDoc("# T\n\n## Empty\n\n## Full\n\nText\n", "x");
    expect(d.sections.map((s) => s.path)).toEqual(["Full"]);
  });
});

describe("splitLong", () => {
  it("splits long sections into parts of at most MAX_WORDS", () => {
    const para = Array.from({ length: 400 }, () => "word").join(" ");
    const parts = splitLong([para, para, para].join("\n\n"));
    expect(parts.length).toBe(2); // 400 + 400 words fit in one part; the third starts a new one
    for (const p of parts) expect(p.split(/\s+/).length).toBeLessThanOrEqual(MAX_WORDS);
  });
  it("splits one long list block by line", () => {
    const list = Array.from({ length: 200 }, (_, i) => `- item ${i} has five words`).join("\n");
    expect(splitLong(list).length).toBeGreaterThan(1);
  });
});

describe("withoutOpenQuestions", () => {
  it("drops open-question blocks, top-level and indented, and keeps the rest", () => {
    const md = [
      "# T",
      "",
      "## A",
      "",
      "Fees are Tk 200.",
      "",
      "> **Need to know**",
      "> - Is it Tk 250?",
      "",
      "1. **Enrol** on OEP.",
      "",
      "   > **Need to know**",
      "   > - Does the app work?",
      "",
      "2. **Attend** all 3 days.",
    ].join("\n");
    const text = parseDoc(md, "x").sections[0]?.text ?? "";
    const clean = withoutOpenQuestions(text);
    expect(clean).not.toContain(OPEN_QUESTIONS_LABEL);
    expect(clean).not.toContain("Tk 250");
    expect(clean).not.toContain("Does the app work");
    expect(clean).toContain("Fees are Tk 200.");
    expect(clean).toContain("2. **Attend** all 3 days.");
  });
});
