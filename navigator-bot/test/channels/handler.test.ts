import { describe, expect, it } from "vitest";
import { isPlaceholder, toIncoming } from "../../src/channels/handler.ts";

const msg = (text: string) => ({ text, attachments: [] });

describe("isPlaceholder", () => {
  it.each([
    "[Voice message]",
    "[Audio message]",
    "[Image]",
    "[Sticker]",
    "[Video]",
    "[Document: cv.pdf]",
    "[Location: Dhaka - Mirpur]",
  ])("treats %s as not typed by the person", (text) => expect(isPlaceholder(text)).toBe(true));
  it("keeps real text, including text in brackets", () => {
    expect(isPlaceholder("Saudi visa [urgent]")).toBe(false);
    expect(isPlaceholder("[visa cost?]")).toBe(false);
  });
});

describe("toIncoming", () => {
  it("turns a voice note or photo into 'other'", () => {
    expect(toIncoming("whatsapp", "u", [msg("[Voice message]")]).kind).toBe("other");
    expect(toIncoming("whatsapp", "u", [msg("")]).kind).toBe("other");
  });
  it("keeps a photo's caption as the question, and joins quick follow-ups", () => {
    expect(toIncoming("whatsapp", "u", [msg("[Image]"), msg("Is this visa real?")])).toMatchObject({
      kind: "text",
      text: "Is this visa real?",
    });
    expect(toIncoming("telegram", "u", [msg("Saudi"), msg("medical test")]).text).toBe("Saudi\nmedical test");
  });
});
