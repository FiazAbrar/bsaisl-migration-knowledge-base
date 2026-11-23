/**
 * The knowledge base in memory: every guide split into sections, each cited fact's source, and a full-text
 * index over them. Built from the guides at start-up and after every update; never written back.
 */

import { execFile } from "node:child_process";
import { createHash } from "node:crypto";
import { readFile, stat } from "node:fs/promises";
import path from "node:path";
import { promisify } from "node:util";
import { create, insertMultiple, type Orama, search as oramaSearch } from "@orama/orama";
import { tokenizer as oramaTokenizer } from "@orama/orama/components";
import { parse as parseCsv } from "csv-parse/sync";
import { CountryMatcher } from "./countries.ts";
import { discover, type GuideKind } from "./discover.ts";
import { type FactKinds, parseDoc } from "./parse.ts";

const run = promisify(execFile);

export interface Guide {
  slug: string;
  title: string;
  kind: GuideKind;
  folder: string;
  docSha1: string;
  docModified: string;
}

export interface Section {
  id: number;
  slug: string;
  path: string;
  heading: string;
  level: number;
  part: number;
  text: string;
  facts: string[];
  openQuestions: boolean;
  words: number;
}

export interface Fact {
  id: string;
  slug: string;
  url: string;
  publisher: string;
  sourceType: string;
  status: string;
  pageDate: string;
}

export interface SearchHit {
  id: number;
  slug: string;
  path: string;
  part: number;
  openQuestions: boolean;
  snippet: string;
  score: number;
}

export interface KbMeta {
  builtAt: string;
  kbDir: string;
  guidesUpdated: string;
  commit: string | undefined;
  warnings: string[];
}

const STOPWORDS = new Set(
  (
    "a an the and or of to in on for with from by at is are was were be been can do does did how what " +
    "when where which who whom why will would should could i me my we our you your he she it they them " +
    "this that these those there here about into as if not no yes any all " +
    "hi hello hey salam assalamualaikum please thanks thank ok okay"
  ).split(" "),
);

const english = oramaTokenizer.createTokenizer({ language: "english", stemming: true });

/** Words in any script: letters, combining marks (Bangla vowel signs) and digits stay together. */
export function words(text: string): string[] {
  return (
    text
      .normalize("NFC")
      .toLowerCase()
      .match(/[\p{L}\p{M}\p{N}]+/gu) ?? []
  );
}

/** Search terms: English words are stemmed ("visas" → "visa"); other scripts are kept as typed. */
export function terms(text: string): string[] {
  return words(text).map((w) => (/^[a-z]+$/.test(w) ? (english.tokenize(w)[0] ?? w) : w));
}

const tokenizer = {
  language: "english",
  normalizationCache: new Map<string, string>(),
  tokenize: (raw: string) => terms(raw),
};

const schema = { slug: "enum", path: "string", text: "string" } as const;
type SectionDb = Orama<typeof schema>;

/** A short extract around the query words, like a search engine's snippet. */
export function snippet(text: string, query: readonly string[], size = 24): string {
  const tokens = text.split(/\s+/).filter(Boolean);
  if (tokens.length <= size) return tokens.join(" ");
  const wanted = new Set(query);
  const hits = tokens.map((t) => (terms(t).some((x) => wanted.has(x)) ? 1 : 0));
  let best = 0;
  let bestScore = -1;
  let window = hits.slice(0, size).reduce<number>((a, b) => a + b, 0);
  for (let start = 0; start + size <= tokens.length; start++) {
    if (start > 0) window += (hits[start + size - 1] ?? 0) - (hits[start - 1] ?? 0);
    if (window > bestScore) {
      bestScore = window;
      best = start;
    }
  }
  const pre = best > 0 ? "… " : "";
  const post = best + size < tokens.length ? " …" : "";
  return `${pre}${tokens.slice(best, best + size).join(" ")}${post}`;
}

export class KnowledgeBase {
  readonly meta: KbMeta;
  readonly guides: readonly Guide[];
  readonly sections: readonly Section[];
  readonly countries: CountryMatcher;
  private readonly facts: Map<string, Fact>;
  private readonly db: SectionDb;

  private constructor(meta: KbMeta, guides: Guide[], sections: Section[], facts: Fact[], db: SectionDb) {
    this.meta = meta;
    this.guides = guides;
    this.sections = sections;
    this.facts = new Map(facts.map((f) => [`${f.slug}\u0000${f.id}`, f]));
    this.db = db;
    this.countries = new CountryMatcher(guides.filter((g) => g.kind === "country"));
  }

  /** Read every guide under kbDir. One broken guide is skipped with a warning; it never stops the rest. */
  static async build(kbDir: string, commit?: string): Promise<KnowledgeBase> {
    const files = await discover(kbDir);
    const warnings: string[] = [];
    const guides: Guide[] = [];
    const sections: Section[] = [];
    const facts: Fact[] = [];

    for (const file of files) {
      let factRows: Fact[] = [];
      try {
        factRows = await loadFacts(path.dirname(file.docPath), file.slug);
      } catch (err) {
        warnings.push(`${file.slug}: facts.csv unreadable (${(err as Error).name}); sources not labelled`);
      }
      const kinds: FactKinds = new Map(
        factRows.map((f) => [f.id, { sourceType: f.sourceType, year: f.pageDate.slice(0, 4) }]),
      );
      let raw: Buffer;
      try {
        raw = await readFile(file.docPath);
      } catch (err) {
        warnings.push(`${file.slug}: doc.md unreadable (${(err as Error).name}); guide skipped`);
        continue;
      }
      const parsed = parseDoc(new TextDecoder("utf-8", { fatal: false }).decode(raw), file.slug, kinds);
      if (parsed.sections.length === 0) {
        warnings.push(`${file.slug}: doc.md has no text under its headings; guide skipped`);
        continue;
      }
      const modified = (await stat(file.docPath)).mtime.toISOString().replace(/\.\d{3}Z$/, "Z");
      guides.push({
        slug: file.slug,
        title: parsed.title,
        kind: file.kind,
        folder: file.folder,
        docSha1: createHash("sha1").update(raw).digest("hex"),
        docModified: modified,
      });
      for (const s of parsed.sections) {
        sections.push({
          id: sections.length + 1,
          slug: file.slug,
          ...s,
          words: s.text.split(/\s+/).filter(Boolean).length,
        });
      }
      facts.push(...factRows);
    }

    const db = create({ schema, components: { tokenizer } });
    await insertMultiple(
      db,
      sections.map((s) => ({ id: String(s.id), slug: s.slug, path: s.path, text: s.text })),
    );

    const meta: KbMeta = {
      builtAt: new Date().toISOString().replace(/\.\d{3}Z$/, "Z"),
      kbDir,
      guidesUpdated: await guidesUpdated(kbDir),
      commit,
      warnings,
    };
    return new KnowledgeBase(meta, guides, sections, facts, db);
  }

  /** Number of sections per guide, used to refuse a broken update. */
  sectionCounts(): Record<string, number> {
    const counts: Record<string, number> = {};
    for (const s of this.sections) counts[s.slug] = (counts[s.slug] ?? 0) + 1;
    return counts;
  }

  guide(slug: string): Guide | undefined {
    return this.guides.find((g) => g.slug === slug);
  }

  listGuides(kind?: GuideKind): Guide[] {
    return this.guides.filter((g) => kind === undefined || g.kind === kind);
  }

  /** The headings of one guide, for the AI to pick sections from. */
  contents(slug: string): Pick<Section, "id" | "path" | "part" | "words" | "openQuestions">[] {
    return this.sections
      .filter((s) => s.slug === slug)
      .map(({ id, path, part, words, openQuestions }) => ({ id, path, part, words, openQuestions }));
  }

  section(id: number): (Section & { guide: string }) | undefined {
    const s = this.sections[id - 1];
    if (!s || s.id !== id) return undefined;
    return { ...s, guide: this.guide(s.slug)?.title ?? s.slug };
  }

  sourcesFor(slug: string, factIds: readonly string[]): Fact[] {
    return factIds.map((id) => this.facts.get(`${slug}\u0000${id}`)).filter((f) => f !== undefined);
  }

  /** Full-text search; a match in the heading path counts four times a match in the text. */
  search(query: string, slug?: string, limit = 6): SearchHit[] {
    const queryTerms = [...new Set(words(query).filter((w) => w.length > 1 && !STOPWORDS.has(w)))];
    if (queryTerms.length === 0) return [];
    const result = oramaSearch(this.db, {
      term: queryTerms.join(" "),
      properties: ["path", "text"],
      boost: { path: 4 },
      threshold: 1,
      tolerance: 0,
      limit,
      ...(slug ? { where: { slug: { eq: slug } } } : {}),
    });
    if (result instanceof Promise) throw new Error("Orama search unexpectedly returned a promise");
    const stemmed = queryTerms.flatMap(terms);
    return result.hits.map((hit) => {
      const s = this.sections[Number(hit.id) - 1] as Section;
      return {
        id: s.id,
        slug: s.slug,
        path: s.path,
        part: s.part,
        openQuestions: s.openQuestions,
        snippet: snippet(s.text, stemmed),
        score: hit.score,
      };
    });
  }

  info(): KbMeta & { sections: number; guides: number } {
    return { ...this.meta, sections: this.sections.length, guides: this.guides.length };
  }
}

async function loadFacts(folder: string, slug: string): Promise<Fact[]> {
  let factsCsv: string;
  try {
    factsCsv = await readFile(path.join(folder, "facts.csv"), "utf-8");
  } catch {
    return [];
  }
  const publishers = new Map<string, string>();
  try {
    const sources = parseCsv(await readFile(path.join(folder, "sources.csv"), "utf-8"), {
      columns: true,
      bom: true,
      skip_empty_lines: true,
      relax_column_count: true,
    }) as Record<string, string>[];
    for (const r of sources) publishers.set(r.url ?? "", r.publisher ?? "");
  } catch {
    // No sources.csv: facts keep an empty publisher.
  }
  const rows = parseCsv(factsCsv, {
    columns: true,
    bom: true,
    skip_empty_lines: true,
    relax_column_count: true,
  }) as Record<string, string>[];
  return rows.map((r) => {
    if (r.id === undefined) throw new Error("facts.csv has no id column");
    return {
      id: r.id,
      slug,
      url: r.url ?? "",
      publisher: publishers.get(r.url ?? "") ?? "",
      sourceType: r.source_type ?? "",
      status: r.status ?? "",
      pageDate: r.page_date ?? "",
    };
  });
}

/** Date (YYYY-MM-DD) of the newest commit that changed the guides, or of the newest commit, or today. */
async function guidesUpdated(kbDir: string): Promise<string> {
  for (const args of [
    ["log", "-1", "--format=%cs", "--", "countries", "global", "agencies"],
    ["log", "-1", "--format=%cs"],
  ]) {
    try {
      const { stdout } = await run("git", ["-C", kbDir, ...args], { timeout: 20_000 });
      if (/^\d{4}-\d{2}-\d{2}$/.test(stdout.trim())) return stdout.trim();
    } catch {
      break;
    }
  }
  return new Date().toISOString().slice(0, 10);
}

export const SHRINK_LIMIT = 0.5;
export const SHRINK_MIN_SECTIONS = 20;

/** Reasons a new set of guides looks broken next to the old one (empty = fine). */
export function compareCounts(old: Record<string, number>, next: Record<string, number>): string[] {
  const problems = Object.keys(old)
    .sort()
    .filter((slug) => !(slug in next))
    .map((slug) => `guide '${slug}' disappeared`);
  for (const [slug, nOld] of Object.entries(old).sort(([a], [b]) => a.localeCompare(b))) {
    const nNew = next[slug];
    if (nNew !== undefined && nOld >= SHRINK_MIN_SECTIONS && nNew < SHRINK_LIMIT * nOld) {
      problems.push(`guide '${slug}' shrank from ${nOld} to ${nNew} sections`);
    }
  }
  return problems;
}
