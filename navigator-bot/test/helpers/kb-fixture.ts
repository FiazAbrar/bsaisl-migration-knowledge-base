import { mkdir, mkdtemp, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";

export const SAUDI_DOC = `# Saudi Arabia: working there

Intro text about the corridor [A0001].

## Background

### Is it open now?

The corridor is open [A0001]. Fees are capped at 165,000 taka [N0002].

> **Need to know**
> - What does a house-driver visa sell for in Dhaka?

## Work visa

### Step 1: Find a job

Ask licensed agencies for the BMET permission letter [A0001, N0002].

### Step 2: Medical test

Book the GAMCA medical test [N0003].
`;

export const SAUDI_FACTS = `id,claim,url,source_type,status,page_date
A0001,open,https://bmet.gov.bd/a,official,ok,2026-02-01
N0002,cap,https://news.example/b,news,ok,2026-03-01
N0003,medical,https://news.example/c,news,ok,2023-05-01
`;

export const SAUDI_SOURCES = `url,publisher,title
https://bmet.gov.bd/a,BMET,Notice
https://news.example/b,Prothom Alo,Report
`;

export const MALAYSIA_DOC = `# Malaysia: working there

## Work visa

### Step 1: Calling visa

A calling visa arrives through the agency.
`;

export const FAQ_DOC = `# FAQ

## Common questions

What is the safest way to go abroad?
`;

/** A small knowledge base on disk: two countries and one shared guide. */
export async function makeKb(
  extra: Record<string, string> = {},
): Promise<{ dir: string; cleanup: () => Promise<void> }> {
  const dir = await mkdtemp(path.join(tmpdir(), "kb-"));
  const files: Record<string, string> = {
    "countries/saudi-arabia/doc.md": SAUDI_DOC,
    "countries/saudi-arabia/facts.csv": SAUDI_FACTS,
    "countries/saudi-arabia/sources.csv": SAUDI_SOURCES,
    "countries/malaysia/doc.md": MALAYSIA_DOC,
    "global/faq/doc.md": FAQ_DOC,
    "countries/saudi-arabia/sources/ignored/doc.md": "# Should be skipped\n\n## X\n\ntext\n",
    "navigator-bot/doc.md": "# Bot\n\n## X\n\ntext\n",
    ...extra,
  };
  for (const [rel, content] of Object.entries(files)) {
    const full = path.join(dir, rel);
    await mkdir(path.dirname(full), { recursive: true });
    await writeFile(full, content, "utf-8");
  }
  return { dir, cleanup: () => rm(dir, { recursive: true, force: true }) };
}
