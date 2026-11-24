/**
 * The number check (prompts/README.md, code-side safeguard 1): every amount, phone number, date or year in
 * an answer must appear in the guide text the AI read for that question. A wrong fee can cost someone a
 * year's income, so an answer that fails is regenerated once with the offending numbers named.
 */

const BN_DIGITS = "০১২৩৪৫৬৭৮৯";

/** Help lines the bot may always give (they are in the shared guides too). */
const ALWAYS_ALLOWED = new Set(["16135", "8809610102030", "09610102030"]);

function asciiDigits(text: string): string {
  return text.replace(/[০-৯]/g, (d) => String(BN_DIGITS.indexOf(d)));
}

/** Numbers worth checking: three or more digits once separators are removed (fees, phones, years). */
export function significantNumbers(text: string): string[] {
  const found = asciiDigits(text).match(/\+?\d[\d,.\s-]*\d|\d/g) ?? [];
  const out = new Set<string>();
  for (const raw of found) {
    const digits = raw.replace(/\D/g, "");
    if (digits.length >= 3) out.add(digits);
  }
  return [...out];
}

/** Numbers in the answer that appear nowhere in the sources (compared digit by digit). */
export function unsupportedNumbers(answer: string, sources: readonly string[]): string[] {
  const haystack = new Set(sources.flatMap(significantNumbers));
  const joined = asciiDigits(sources.join("\n")).replace(/\D/g, " ");
  return significantNumbers(answer).filter(
    (n) => !ALWAYS_ALLOWED.has(n) && !haystack.has(n) && !joined.includes(n),
  );
}
