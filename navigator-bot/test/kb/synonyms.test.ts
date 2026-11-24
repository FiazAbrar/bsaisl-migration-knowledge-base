import { afterAll, beforeAll, describe, expect, it } from "vitest";
import { KnowledgeBase } from "../../src/kb/index.ts";
import { englishFor } from "../../src/kb/synonyms.ts";
import { makeKb } from "../helpers/kb-fixture.ts";

describe("englishFor", () => {
  it("maps Bangla words, with their case endings, to English", () => {
    expect(englishFor("ভিসা".normalize("NFC"))).toEqual(["visa"]);
    expect(englishFor("ভিসায়".normalize("NFC"))).toEqual(["visa"]);
    expect(englishFor("খরচের".normalize("NFC"))).toEqual(["cost"]);
  });

  it("maps Banglish words whole", () => {
    expect(englishFor("khoroch")).toEqual(["cost"]);
    expect(englishFor("huroob")).toEqual(["huroob", "absent"]);
  });

  it("doesn't match a different word that starts the same", () => {
    expect(englishFor("জেলা".normalize("NFC"))).toEqual([]); // district, not jail
    expect(englishFor("ফিরে".normalize("NFC"))).toEqual([]); // returning, not fee
  });
});

describe("search in Bangla and Banglish", () => {
  let kb: KnowledgeBase;
  let cleanup: () => Promise<void>;
  beforeAll(async () => {
    const fixture = await makeKb();
    cleanup = fixture.cleanup;
    kb = await KnowledgeBase.build(fixture.dir);
  });
  afterAll(() => cleanup());

  it("finds the English section for a Bangla question", () => {
    expect(kb.search("মেডিকেলের নিয়ম কী", "saudi-arabia")[0]?.path).toBe("Work visa > Step 2: Medical test");
  });

  it("ignores Banglish filler words", () => {
    expect(kb.search("ki kivabe ache")).toEqual([]);
  });
});
