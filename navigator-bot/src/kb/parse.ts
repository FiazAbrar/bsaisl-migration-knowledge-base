/**
 * Turn one guide's doc.md into sections the bot can search and quote. The rules are written down for the
 * knowledge-base team in KB-STRUCTURE.md; keep the two in step.
 *
 * - `#` is the guide's title; every `##`..`######` heading starts a section whose path is its parent
 *   headings plus itself ("Work visa > Step 1 > Documents"). Text before the first heading is "Introduction".
 * - Citations like `[A0123, N0045]` are removed. When only news or NGO sources back a sentence it is marked
 *   "(news report)", and a year is added when the newest source is older than 2025.
 * - A `> **Need to know**` block becomes OPEN QUESTIONS, which the bot must never state as fact.
 * - Sections longer than MAX_WORDS are split into parts.
 */

export const MAX_WORDS = 900;

const CITE_RE = /\s?\[((?:[A-Z]{1,3}\d{3,5})(?:\s*,\s*[A-Z]{1,3}\d{3,5})*)\]/g;
const HEADING_RE = /^(#{1,6})\s+(.*?)\s*$/;

export const OPEN_QUESTIONS_LABEL = "OPEN QUESTIONS (not confirmed; never state these as facts):";

/** For each fact id: its source type ("official", "news", ...) and the year of its page. */
export type FactKinds = ReadonlyMap<string, { sourceType: string; year: string }>;

export interface ParsedSection {
  path: string;
  heading: string;
  level: number;
  part: number;
  text: string;
  facts: string[];
  openQuestions: boolean;
}

export interface ParsedDoc {
  title: string;
  sections: ParsedSection[];
}

export function wordCount(text: string): number {
  return text.split(/\s+/).filter(Boolean).length;
}

function splitIds(group: string): string[] {
  return group.split(",").map((id) => id.trim());
}

/** What the reader sees in place of a citation. */
export function citationMarker(ids: string[], kinds: FactKinds): string {
  const found = ids.map((id) => kinds.get(id)).filter((k) => k !== undefined);
  if (found.length === 0) return "";
  const official = found.filter((k) => k.sourceType.startsWith("official"));
  const use = official.length > 0 ? official : found;
  const years = use.map((k) => k.year).filter((y) => /^\d+$/.test(y));
  const year = years.length > 0 ? String(Math.max(...years.map(Number))) : "";
  const old = year && Number(year) < 2025 ? year : "";
  if (official.length > 0) return old ? ` (${old})` : "";
  return old ? ` (news report, ${old})` : " (news report)";
}

/** A section's markdown as plain text, the fact ids it cites, and whether it holds open questions. */
export function cleanSection(
  lines: readonly string[],
  kinds: FactKinds = new Map(),
): { body: string; facts: string[]; openQuestions: boolean } {
  const out: string[] = [];
  const facts: string[] = [];
  let openQuestions = false;
  let inNeedToKnow = false;
  for (const line of lines) {
    for (const m of line.matchAll(CITE_RE)) facts.push(...splitIds(m[1] ?? ""));
    const text = line
      .replace(CITE_RE, (_all, group: string) => citationMarker(splitIds(group), kinds))
      .trimEnd();
    const stripped = text.replace(/^[> ]+/, "").trim();
    if (text.startsWith(">") && stripped.toLowerCase().includes("need to know")) {
      inNeedToKnow = true;
      openQuestions = true;
      out.push(OPEN_QUESTIONS_LABEL);
      continue;
    }
    if (inNeedToKnow && text.startsWith(">")) {
      out.push(`  ${stripped}`);
      continue;
    }
    inNeedToKnow = false;
    out.push(text);
  }
  const body = out
    .join("\n")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
  return { body, facts: [...new Set(facts)], openQuestions };
}

/** Split a long section into parts of at most MAX_WORDS, at blank lines (or at lines inside a long list). */
export function splitLong(body: string): string[] {
  if (wordCount(body) <= MAX_WORDS) return [body];
  const blocks: string[] = [];
  for (const block of body.split("\n\n")) {
    if (wordCount(block) > MAX_WORDS) blocks.push(...block.split("\n"));
    else blocks.push(block);
  }
  const parts: string[] = [];
  let current: string[] = [];
  let count = 0;
  for (const block of blocks) {
    const n = wordCount(block);
    if (current.length > 0 && count + n > MAX_WORDS) {
      parts.push(current.join("\n\n"));
      current = [];
      count = 0;
    }
    current.push(block);
    count += n;
  }
  if (current.length > 0) parts.push(current.join("\n\n"));
  return parts;
}

export function parseDoc(markdown: string, slug: string, kinds: FactKinds = new Map()): ParsedDoc {
  const lines = markdown.split(/\r\n|\r|\n/);
  // Python's splitlines() drops the empty string after a final newline; keep the two in step.
  if (lines.length > 0 && lines[lines.length - 1] === "") lines.pop();
  let title = slug;
  let stack = new Map<number, string>();
  const sections: ParsedSection[] = [];
  let current = { heading: "Introduction", level: 1, lines: [] as string[] };

  const flush = () => {
    const { body, facts, openQuestions } = cleanSection(current.lines, kinds);
    if (!body) return;
    const parents = [...stack.entries()]
      .filter(([level]) => level < current.level)
      .sort(([a], [b]) => a - b)
      .map(([, heading]) => heading);
    const path = [...parents, current.heading].join(" > ");
    splitLong(body).forEach((text, i) => {
      sections.push({
        path,
        heading: current.heading,
        level: current.level,
        part: i + 1,
        text,
        facts,
        openQuestions,
      });
    });
  };

  for (const line of lines) {
    const m = HEADING_RE.exec(line);
    if (!m) {
      current.lines.push(line);
      continue;
    }
    const level = (m[1] ?? "").length;
    const heading = (m[2] ?? "").replace(CITE_RE, "").trim();
    if (level === 1) {
      title = heading;
      continue;
    }
    flush();
    stack = new Map([...stack].filter(([l]) => l < level));
    stack.set(level, heading);
    current = { heading, level, lines: [] };
  }
  flush();
  return { title, sections };
}
