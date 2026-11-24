/**
 * Country names people type, in English, Bangla and Banglish, mapped to guide ids (folder names).
 * A country guide added later works without touching this file: its folder name and the start of its
 * title are recognised automatically, and it gets a web button under its English name.
 */

/** Nicknames, cities and spellings, per guide id. Bangla is matched anywhere; Latin as whole words. */
export const ALIASES: Readonly<Record<string, readonly string[]>> = {
  "saudi-arabia": ["saudi", "soudi", "sowdi", "saudia", "ksa", "riyadh", "jeddah", "সৌদি", "সৌদি আরব"],
  malaysia: [
    "malaysia",
    "malaysian",
    "malayshia",
    "malaysiya",
    "maleshia",
    "kuala lumpur",
    "মালয়েশিয়া",
    "মালয়শিয়া",
    "মালেশিয়া",
  ],
  qatar: ["qatar", "katar", "kotar", "doha", "কাতার"],
  "united-arab-emirates": ["uae", "emirates", "dubai", "abu dhabi", "sharjah", "দুবাই", "আমিরাত", "আরব আমিরাত"],
  singapore: ["singapore", "singapur", "shingapur", "সিঙ্গাপুর", "সিংগাপুর"],
  kuwait: ["kuwait", "kuweit", "koweit", "কুয়েত"],
  oman: ["oman", "muscat", "ওমান"],
  // Not "male" (Malé): it would match "I am male".
  maldives: ["maldives", "maldip", "maldwip", "মালদ্বীপ"],
  jordan: ["jordan", "amman", "জর্ডান"],
  italy: ["italy", "italia", "itali", "rome", "ইতালি"],
  cambodia: ["cambodia", "phnom penh", "কম্বোডিয়া"],
  kyrgyzstan: ["kyrgyzstan", "kyrgyz", "bishkek", "কিরগিজস্তান", "কিরগিস্তান"],
  brunei: ["brunei", "bandar seri begawan", "ব্রুনাই"],
  japan: ["japan", "tokyo", "জাপান"],
  "south-korea": ["south korea", "korea", "koriya", "seoul", "eps korea", "দক্ষিণ কোরিয়া", "কোরিয়া"],
  canada: ["canada", "toronto", "কানাডা"],
  greece: ["greece", "athens", "গ্রিস", "গ্রীস"],
  india: ["india", "ভারত", "ইন্ডিয়া"],
  lebanon: ["lebanon", "beirut", "লেবানন"],
  "united-kingdom": [
    "uk",
    "united kingdom",
    "england",
    "britain",
    "london",
    "bilet",
    "যুক্তরাজ্য",
    "ইংল্যান্ড",
    "লন্ডন",
    "বিলেত",
  ],
  "united-states": ["usa", "united states", "america", "আমেরিকা", "যুক্তরাষ্ট্র"],
};

/** The web page's country buttons, in order: guide id, English name, Bangla name. */
export const DISPLAY: readonly (readonly [string, string, string])[] = [
  ["saudi-arabia", "Saudi Arabia", "সৌদি আরব"],
  ["malaysia", "Malaysia", "মালয়েশিয়া"],
  ["united-arab-emirates", "UAE", "সংযুক্ত আরব আমিরাত"],
  ["qatar", "Qatar", "কাতার"],
  ["oman", "Oman", "ওমান"],
  ["kuwait", "Kuwait", "কুয়েত"],
  ["singapore", "Singapore", "সিঙ্গাপুর"],
  ["maldives", "Maldives", "মালদ্বীপ"],
  ["jordan", "Jordan", "জর্ডান"],
  ["italy", "Italy", "ইতালি"],
  ["south-korea", "South Korea", "দক্ষিণ কোরিয়া"],
  ["japan", "Japan", "জাপান"],
  ["brunei", "Brunei", "ব্রুনাই"],
  ["cambodia", "Cambodia", "কম্বোডিয়া"],
  ["kyrgyzstan", "Kyrgyzstan", "কিরগিজস্তান"],
  ["united-kingdom", "United Kingdom", "যুক্তরাজ্য"],
  ["united-states", "United States", "যুক্তরাষ্ট্র"],
  ["canada", "Canada", "কানাডা"],
  ["greece", "Greece", "গ্রিস"],
  ["lebanon", "Lebanon", "লেবানন"],
  ["india", "India", "ভারত"],
];

export interface CountryGuide {
  slug: string;
  title: string;
}

/** Bangla য় has two Unicode spellings; normalising both sides makes them match. */
export function normalise(text: string): string {
  return text.normalize("NFC").toLowerCase();
}

/** The part of a guide title before ":" ("Saudi Arabia: working there" → "Saudi Arabia"). */
export function shortTitle(title: string): string {
  return (title.split(":")[0] ?? title).trim();
}

const isAscii = (s: string) => /^[\x20-\x7e]*$/.test(s);
const escapeRegExp = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

function patternFor(name: string, flags: string): RegExp {
  // Latin names must match as whole words ("male" not in "female"); Bangla as substrings.
  return isAscii(name)
    ? new RegExp(`\\b${escapeRegExp(name)}\\b`, flags)
    : new RegExp(escapeRegExp(name), flags);
}

export class CountryMatcher {
  private readonly aliases: Map<string, string[]>;
  private readonly guides: readonly CountryGuide[];

  constructor(indexedCountries: readonly CountryGuide[]) {
    this.guides = indexedCountries;
    this.aliases = new Map(Object.entries(ALIASES).map(([slug, names]) => [slug, names.map(normalise)]));
    for (const c of indexedCountries) {
      const names = this.aliases.get(c.slug) ?? [];
      for (const name of [c.slug.replaceAll("-", " "), shortTitle(c.title)].map(normalise)) {
        if (name && !names.includes(name)) names.push(name);
      }
      this.aliases.set(c.slug, names);
    }
  }

  /** The guide id of the first country named in the text, if any (only countries that have a guide). */
  detect(text: string): string | undefined {
    const low = normalise(text);
    const indexed = new Set(this.guides.map((g) => g.slug));
    let best: { at: number; slug: string } | undefined;
    for (const [slug, names] of this.aliases) {
      if (!indexed.has(slug)) continue;
      for (const name of names) {
        const m = patternFor(name, "").exec(low);
        if (m && (best === undefined || m.index < best.at)) best = { at: m.index, slug };
      }
    }
    return best?.slug;
  }

  /** The text without country names, so they don't skew a search inside that country's guide. */
  strip(text: string): string {
    let out = text.normalize("NFC");
    for (const names of this.aliases.values()) {
      for (const name of [...names].sort((a, b) => b.length - a.length)) {
        out = out.replace(patternFor(name, "gi"), " ");
      }
    }
    return out
      .replace(/\b(arabia|arab)\b/gi, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  /** Web buttons: DISPLAY first (only guides that exist), then newer country guides by their title. */
  buttons(): { slug: string; en: string; bn: string }[] {
    const indexed = new Map(this.guides.map((g) => [g.slug, g]));
    const known = new Set(DISPLAY.map(([slug]) => slug));
    const fixed = DISPLAY.filter(([slug]) => indexed.has(slug)).map(([slug, en, bn]) => ({ slug, en, bn }));
    const extra = this.guides
      .filter((g) => !known.has(g.slug))
      .map((g) => ({ slug: g.slug, en: shortTitle(g.title), bn: shortTitle(g.title) }));
    return [...fixed, ...extra];
  }
}
