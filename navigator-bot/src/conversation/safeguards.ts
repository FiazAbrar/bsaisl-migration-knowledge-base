/**
 * Checks on what people send, before it is stored or reaches the AI.
 * - Control characters are removed and line endings normalised.
 * - Numbers that look like a Bangladeshi mobile number, NID, passport or bank card are replaced, so they
 *   are never stored or sent on. The web page also warns before sending (web/src/personal.ts, same rules).
 */

const BN_DIGITS = "০১২৩৪৫৬৭৮৯";

export const PERSONAL_PATTERNS: readonly RegExp[] = [
  /(?:\+?880|\b0)1[3-9]\d{8}\b/g, // Bangladeshi mobile number
  /\b(?:\d{10}|\d{13}|\d{17})\b/g, // NID (10, 13 or 17 digits)
  /\b[A-Z]{1,2}\d{7,8}\b/gi, // passport number
  /\b\d(?:[ -]?\d){12,18}\b/g, // bank card number (13–19 digits, spaces or dashes between)
];

export const REMOVED = "[number removed]";

export function cleanText(text: string): string {
  return text
    .replace(/\r\n?/g, "\n")
    // biome-ignore lint/suspicious/noControlCharactersInRegex: removing control characters is the point
    .replace(/[\u0000-\u0008\u000B-\u001F\u007F]/g, "")
    .trim();
}

/** Characters as people count them (an emoji or a Bangla letter is one). */
export function charCount(text: string): number {
  return Array.from(text).length;
}

/** Bangla digits as ASCII digits; same length, so positions line up with the original text. */
function asciiDigits(text: string): string {
  return text.replace(/[০-৯]/g, (d) => String(BN_DIGITS.indexOf(d)));
}

/** The text with personal numbers replaced, and whether anything was replaced. */
export function maskPersonal(text: string): { text: string; masked: boolean } {
  const ascii = asciiDigits(text);
  const spans: [number, number][] = [];
  for (const pattern of PERSONAL_PATTERNS) {
    for (const m of ascii.matchAll(pattern)) spans.push([m.index, m.index + m[0].length]);
  }
  if (spans.length === 0) return { text, masked: false };
  spans.sort((a, b) => a[0] - b[0]);
  const merged: [number, number][] = [];
  for (const span of spans) {
    const last = merged.at(-1);
    if (last && span[0] <= last[1]) last[1] = Math.max(last[1], span[1]);
    else merged.push([...span]);
  }
  let out = "";
  let at = 0;
  for (const [start, end] of merged) {
    out += text.slice(at, start) + REMOVED;
    at = end;
  }
  return { text: out + text.slice(at), masked: true };
}
