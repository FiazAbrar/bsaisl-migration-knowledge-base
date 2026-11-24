/**
 * Bangla and Banglish words people use, mapped to the English words the guides use, so a search
 * typed in Bangla or Banglish still finds the English guides (test mode searches the message as typed;
 * the AI translates first, but these help it too). Country names are handled in countries.ts.
 *
 * Bangla keys also match with a suffix ("ভিসার", "ভিসায়" → "ভিসা"); Banglish keys match whole words only.
 * Add a word here when the eval or real questions show search missing it; keep the English to words
 * the guides really use.
 */

/** Bangla and Banglish word → English search words. */
const MAP: Readonly<Record<string, string>> = {
  // money
  খরচ: "cost",
  টাকা: "cost",
  দাম: "price cost",
  ফি: "fee",
  বেতন: "salary wages pay",
  মজুরি: "wages pay",
  ঋণ: "loan borrow",
  লোন: "loan borrow",
  khoroch: "cost",
  khorch: "cost",
  taka: "cost",
  beton: "salary wages pay",
  loan: "loan borrow",
  // work and visas
  ভিসা: "visa",
  কাজ: "work job",
  চাকরি: "job work",
  কোম্পানি: "company",
  গৃহকর্মী: "domestic worker housemaid",
  ড্রাইভার: "driver",
  ফ্রি: "free",
  আজাদ: "free azad",
  কলিং: "calling visa",
  ওয়ার্ক: "work permit",
  পারমিট: "permit",
  চুক্তি: "contract",
  kaj: "work job",
  kajer: "work job",
  chakri: "job work",
  visa: "visa",
  fri: "free",
  // people and places
  এজেন্সি: "agency recruiting",
  দালাল: "broker dalal",
  মালিক: "employer",
  কফিল: "kafil employer sponsor",
  স্পন্সর: "sponsor employer",
  মহিলা: "women woman",
  নারী: "women woman",
  পরিবার: "family",
  স্ত্রী: "wife spouse family",
  সন্তান: "children family",
  এয়ারপোর্ট: "airport",
  বিমানবন্দর: "airport",
  দূতাবাস: "embassy",
  agency: "agency recruiting",
  dalal: "broker dalal",
  malik: "employer",
  kafil: "kafil employer sponsor",
  mohila: "women woman",
  // steps and papers
  মেডিকেল: "medical",
  ট্রেনিং: "training orientation",
  প্রশিক্ষণ: "training",
  ক্লিয়ারেন্স: "clearance",
  স্মার্ট: "smart card clearance",
  পাসপোর্ট: "passport",
  আকামা: "iqama residence",
  ইকামা: "iqama residence",
  বীমা: "insurance",
  নিবন্ধন: "registration register",
  রেজিস্ট্রেশন: "registration register",
  medical: "medical",
  akama: "iqama residence",
  iqama: "iqama residence",
  passport: "passport",
  // problems
  হুরুব: "huroob absent",
  পলাতক: "absent huroob",
  বদল: "change transfer",
  পরিবর্তন: "change",
  অভিযোগ: "complaint complain",
  প্রতারণা: "fraud scam cheated",
  প্রতারক: "fraud scam",
  ভুয়া: "fake",
  নকল: "fake forged",
  আসল: "genuine real check",
  যাচাই: "check verify",
  চেক: "check",
  মারা: "death died",
  মৃত্যু: "death died",
  লাশ: "body death",
  আহত: "injured injury",
  অসুস্থ: "sick illness",
  জেল: "jail prison",
  ছুটি: "leave holiday",
  ফেরত: "return home",
  আশ্রয়: "asylum",
  নির্যাতন: "abuse",
  huroob: "huroob absent",
  bodol: "change transfer",
  vua: "fake",
  bhua: "fake",
  asol: "genuine real check",
  chuti: "leave holiday",
  // status
  নিয়ম: "rules requirements",
  নতুন: "new",
  বন্ধ: "closed ban",
  খোলা: "open",
  niyom: "rules requirements",
};

/** Banglish filler words that never help a search ("ki", "ache", "kivabe"). */
export const BANGLISH_STOPWORDS = new Set(
  (
    "ki ache ase achhe hobe hoy jabe jay jete jai dite dibe chai chacche amar ami amake apni apnar " +
    "kivabe kibhabe keno kothay kokhon koto ar te er ta ti na ekhon pawa pabo pabe lage lagbe " +
    "kora kore korte korbo bolen bolun ektu dorkar"
  ).split(" "),
);

const norm = (s: string) => s.normalize("NFC").toLowerCase();
const isLatin = (s: string) => /^[a-z]+$/.test(s);

/** Bangla case and article endings allowed after a key: ভিসার, ভিসায়, খরচে, কাজের, এজেন্সিটা ... */
const SUFFIXES = [
  "",
  "র",
  "ের",
  "য়",
  "য়ের",
  "ে",
  "তে",
  "য়",
  "য়ের",
  "টা",
  "টি",
  "গুলো",
  "গুলোর",
  "দের",
  "কে",
  "ও",
  "ই",
].map(norm);

const ENTRIES = Object.entries(MAP).map(([k, v]) => [norm(k), v.split(" ")] as const);
const LATIN = new Map(ENTRIES.filter(([k]) => isLatin(k)));
const BANGLA = new Map(ENTRIES.filter(([k]) => !isLatin(k)));

/** The English search words for one typed word (already lower-cased and NFC), or none. */
export function englishFor(word: string): readonly string[] {
  if (isLatin(word)) return LATIN.get(word) ?? [];
  for (const suffix of SUFFIXES) {
    if (!word.endsWith(suffix)) continue;
    const english = BANGLA.get(word.slice(0, word.length - suffix.length));
    if (english) return english;
  }
  return [];
}
