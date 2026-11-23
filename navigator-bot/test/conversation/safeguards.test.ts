import { describe, expect, it } from "vitest";
import { isGreeting, parseCommand } from "../../src/conversation/commands.ts";
import { bnDigits, detectLang } from "../../src/conversation/i18n.ts";
import { charCount, cleanText, maskPersonal, REMOVED } from "../../src/conversation/safeguards.ts";

describe("maskPersonal", () => {
  it.each([
    ["call me on 01711223344", `call me on ${REMOVED}`],
    ["+8801711223344 is my number", `${REMOVED} is my number`],
    ["NID 1234567890", `NID ${REMOVED}`],
    ["passport A12345678 expired", `passport ${REMOVED} expired`],
    ["card 4111 1111 1111 1111 please", `card ${REMOVED} please`],
    ["আমার নম্বর ০১৭১১২২৩৩৪৪", `আমার নম্বর ${REMOVED}`],
  ])("removes %s", (input, expected) => {
    expect(maskPersonal(input)).toEqual({ text: expected, masked: true });
  });

  it("keeps fees, years and ordinary numbers", () => {
    for (const text of ["It costs 165,000 taka", "since 2024", "Step 3 of 12", "SAR 1500 a month"]) {
      expect(maskPersonal(text)).toEqual({ text, masked: false });
    }
  });
});

describe("cleanText and charCount", () => {
  it("removes control characters and normalises line endings", () => {
    expect(cleanText(" a\r\nb\u0007 ")).toBe("a\nb");
  });
  it("counts Bangla letters and emoji as people see them", () => {
    expect(charCount("👍🏽")).toBe(2);
    expect(charCount("ভিসা")).toBe(4);
  });
});

describe("commands", () => {
  it("matches commands in English, Bangla and Telegram form", () => {
    expect(parseCommand("Delete my data")).toBe("delete");
    expect(parseCommand("আমার তথ্য মুছে দিন।")).toBe("delete");
    expect(parseCommand("/reset@NavigatorBot")).toBe("reset");
    expect(parseCommand("  START OVER ")).toBe("reset");
    expect(parseCommand("/start")).toBe("start");
    expect(parseCommand("how do I reset my visa")).toBeUndefined();
  });
  it("recognises greetings", () => {
    expect(isGreeting("Hi!")).toBe(true);
    expect(isGreeting("আসসালামু আলাইকুম")).toBe(true);
    expect(isGreeting("hi, Saudi visa?")).toBe(false);
  });
});

describe("language", () => {
  it("uses Bangla for Bangla script and English otherwise (Banglish included)", () => {
    expect(detectLang("সৌদি ভিসা")).toBe("bn");
    expect(detectLang("saudi jete koto lage")).toBe("en");
    expect(bnDigits(500)).toBe("৫০০");
  });
});
