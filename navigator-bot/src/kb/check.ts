/**
 * Can the bot still read every guide? Run on every pull request (.github/workflows/bot-kb-check.yml).
 *
 * Compares the guides in this checkout with those on the base branch, using the same rules the live bot
 * uses before it swaps in a new version of the guides (src/kb/index.ts, compareCounts):
 * - a guide on the base branch must still exist (same folder, with its doc.md);
 * - a guide with 20 or more sections must keep at least half of them;
 * - every guide must have text under its headings.
 */
import { execFile } from "node:child_process";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { promisify } from "node:util";
import { discover, isSkipped, slugsFor } from "./discover.ts";
import { compareCounts } from "./index.ts";
import { parseDoc } from "./parse.ts";

const run = promisify(execFile);

export async function headCounts(
  kbDir: string,
): Promise<{ counts: Record<string, number>; problems: string[] }> {
  const counts: Record<string, number> = {};
  const problems: string[] = [];
  for (const g of await discover(kbDir)) {
    const rel = `${g.folder}/doc.md`;
    let markdown: string;
    try {
      markdown = await readFile(g.docPath, "utf-8");
    } catch (err) {
      problems.push(`${rel}: can't be read (${(err as Error).name})`);
      continue;
    }
    const n = parseDoc(markdown, g.slug).sections.length;
    if (n === 0) problems.push(`${rel}: has no text under its headings`);
    counts[g.slug] = n;
  }
  return { counts, problems };
}

/** Section counts of every guide on a git ref, read straight from git. */
export async function baseCounts(kbDir: string, ref: string): Promise<Record<string, number>> {
  const { stdout } = await run("git", ["-C", kbDir, "ls-tree", "-r", "--name-only", ref], {
    maxBuffer: 64 * 1024 * 1024,
  });
  const docPaths = stdout
    .split("\n")
    .filter((f) => f.endsWith("/doc.md"))
    .filter((f) => !f.split("/").slice(0, -1).some(isSkipped));
  const folders = docPaths.map((p) => p.split("/").slice(0, -1));
  const slugs = slugsFor(folders);
  const counts: Record<string, number> = {};
  for (const [i, docPath] of docPaths.entries()) {
    const { stdout: markdown } = await run("git", ["-C", kbDir, "show", `${ref}:${docPath}`], {
      maxBuffer: 64 * 1024 * 1024,
    });
    counts[slugs[i] ?? docPath] = parseDoc(markdown, slugs[i] ?? docPath).sections.length;
  }
  return counts;
}

export async function checkAgainst(
  kbDir: string,
  ref: string,
): Promise<{ counts: Record<string, number>; problems: string[] }> {
  const head = await headCounts(kbDir);
  const problems = [...head.problems, ...compareCounts(await baseCounts(kbDir, ref), head.counts)];
  return { counts: head.counts, problems };
}

export const KB_ROOT_FROM_BOT = path.resolve(import.meta.dirname, "..", "..", "..");
