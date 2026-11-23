import { describe, expect, it } from "vitest";
import { CountryMatcher } from "../../src/kb/countries.ts";

const matcher = new CountryMatcher([
  { slug: "saudi-arabia", title: "Saudi Arabia: working there" },
  { slug: "malaysia", title: "Malaysia: working there" },
  { slug: "maldives", title: "Maldives" },
  { slug: "south-korea", title: "South Korea" },
  { slug: "new-zealand", title: "New Zealand: a guide" },
]);

describe("CountryMatcher.detect", () => {
  it("finds English, Bangla and Banglish names", () => {
    expect(matcher.detect("How do I go to Saudi?")).toBe("saudi-arabia");
    expect(matcher.detect("সৌদি আরবে কাজের ভিসা")).toBe("saudi-arabia");
    expect(matcher.detect("malayshia jete koto taka lage")).toBe("malaysia");
    expect(matcher.detect("soudi visa")).toBe("saudi-arabia");
  });

  it("matches both Unicode spellings of Bangla য়", () => {
    const ya = "য়"; // precomposed য়
    const yaNukta = "য়"; // য + nukta
    expect(matcher.detect(`মাল${ya}েশি${ya}া`)).toBe("malaysia");
    expect(matcher.detect(`মাল${yaNukta}েশি${yaNukta}া`)).toBe("malaysia");
  });

  it("returns the country named first", () => {
    expect(matcher.detect("Malaysia or Saudi, which is cheaper?")).toBe("malaysia");
  });

  it("does not read 'male' as the Maldives", () => {
    expect(matcher.detect("I am male, 25 years old")).toBeUndefined();
    expect(matcher.detect("female workers")).toBeUndefined();
  });

  it("knows a new country guide by its folder name and title", () => {
    expect(matcher.detect("jobs in new zealand")).toBe("new-zealand");
  });

  it("ignores countries that have no guide", () => {
    expect(matcher.detect("I want to go to Qatar")).toBeUndefined();
  });
});

describe("CountryMatcher.strip", () => {
  it("removes country names before a search", () => {
    expect(matcher.strip("Saudi Arabia visa fees")).toBe("visa fees");
    expect(matcher.strip("সৌদি আরব ভিসা")).toBe("ভিসা");
  });
});

describe("CountryMatcher.buttons", () => {
  it("lists known countries in display order, then new guides", () => {
    expect(matcher.buttons().map((b) => b.slug)).toEqual([
      "saudi-arabia",
      "malaysia",
      "maldives",
      "south-korea",
      "new-zealand",
    ]);
    expect(matcher.buttons().at(-1)).toEqual({ slug: "new-zealand", en: "New Zealand", bn: "New Zealand" });
  });
});
