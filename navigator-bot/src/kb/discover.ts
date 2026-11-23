/**
 * Find every guide in the knowledge base: any folder holding a doc.md. Folders under countries/ are
 * destinations; every other guide (agencies/, global/<topic>/, ...) applies to all countries. A new folder
 * needs no code change.
 */
import { readdir } from "node:fs/promises";
import path from "node:path";

/** Folders never searched for guides: source archives, tooling, working files and the bot itself. */
export const SKIP_DIRS = new Set([
  ".git",
  ".github",
  ".venv",
  "__pycache__",
  "node_modules",
  "sources",
  "navigator-bot",
  "data",
  "datasets",
  "official-pdfs",
  "tools",
  "passes",
  "drafts",
  "manual",
  "verify",
  "work",
]);

export type GuideKind = "country" | "shared";

export interface GuideFile {
  slug: string;
  kind: GuideKind;
  /** Path of the folder relative to the knowledge base, with "/" separators. */
  folder: string;
  docPath: string;
}

export function isSkipped(folderName: string): boolean {
  return SKIP_DIRS.has(folderName) || folderName.startsWith(".");
}

/**
 * Give each guide its id: the folder name, or the whole path joined with "-" if two folders share a name.
 * `folders` are relative paths split into parts.
 */
export function slugsFor(folders: readonly string[][]): string[] {
  const names = folders.map((parts) => parts.at(-1) ?? "");
  return folders.map((parts) => {
    const name = parts.at(-1) ?? "";
    return names.filter((n) => n === name).length === 1 ? name : parts.join("-");
  });
}

export function kindFor(parts: readonly string[]): GuideKind {
  return parts.length === 2 && parts[0] === "countries" ? "country" : "shared";
}

export async function discover(kbDir: string): Promise<GuideFile[]> {
  const found: { parts: string[]; docPath: string }[] = [];

  async function walk(dir: string, parts: string[]): Promise<void> {
    const entries = await readdir(dir, { withFileTypes: true });
    if (parts.length > 0 && entries.some((e) => e.isFile() && e.name === "doc.md")) {
      found.push({ parts, docPath: path.join(dir, "doc.md") });
    }
    const subdirs = entries
      .filter((e) => e.isDirectory() && !isSkipped(e.name))
      .map((e) => e.name)
      .sort();
    for (const name of subdirs) await walk(path.join(dir, name), [...parts, name]);
  }

  await walk(kbDir, []);
  const slugs = slugsFor(found.map((f) => f.parts));
  return found.map((f, i) => ({
    slug: slugs[i] ?? f.parts.join("-"),
    kind: kindFor(f.parts),
    folder: f.parts.join("/"),
    docPath: f.docPath,
  }));
}
