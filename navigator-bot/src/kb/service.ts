/**
 * Keeps the guides the bot answers from up to date, safely.
 *
 * With KB_REPO set (servers), the bot keeps its own sparse git copy of only the files it reads (each doc.md,
 * facts.csv and sources.csv, never sources/ or the bot) and fetches the branch every KB_SYNC_MINUTES; a new
 * commit is read and swapped in. Without KB_REPO (a local PC) it reads KB_DIR and re-reads it on the same
 * schedule when a doc.md changed.
 *
 * Safe swap: a new version is refused if a guide disappeared or lost most of its sections; the bot keeps
 * answering from the last good version and reports the refusal on /health and to Sentry. The last good
 * commit and its section counts are kept in the database, so the check survives restarts: if the newest
 * commit is refused right after a restart, the bot loads the last good commit instead.
 */
import { execFile } from "node:child_process";
import { mkdir, rm, stat } from "node:fs/promises";
import path from "node:path";
import { promisify } from "node:util";
import { describeError, logger } from "../ops/logger.ts";
import { compareCounts, KnowledgeBase } from "./index.ts";

const run = promisify(execFile);

/** Any guide anywhere in the repository; never the source archives or the bot's own folder. */
export const SPARSE_PATTERNS = ["doc.md", "facts.csv", "sources.csv", "!/navigator-bot/", "!sources/"];

export interface KbBaseline {
  commit: string | undefined;
  counts: Record<string, number>;
}

/** Where the last good version is remembered (the database in production). */
export interface KbBaselineStore {
  load(): Promise<KbBaseline | undefined>;
  save(baseline: KbBaseline): Promise<void>;
}

export interface KbStatus {
  lastSync: string | undefined;
  commit: string | undefined;
  error: string | undefined;
  indexRefused: string | undefined;
}

export interface KbServiceOptions {
  dir: string;
  repo: string | undefined;
  branch: string;
  syncMinutes: number;
  githubToken: string | undefined;
  /**
   * A commit (its first 7+ characters) to load even if the check refuses it: for a guide renamed, moved
   * or cut on purpose (KB_ACCEPT_COMMIT). Remove the setting once that commit is loaded.
   */
  acceptCommit?: string | undefined;
  store: KbBaselineStore;
  /** Called when a version is refused or a sync keeps failing (Sentry in production). */
  onAlert?: (message: string) => void;
}

export class KbService {
  private kb: KnowledgeBase | undefined;
  private timer: NodeJS.Timeout | undefined;
  private queue: Promise<unknown> = Promise.resolve();
  readonly status: KbStatus = {
    lastSync: undefined,
    commit: undefined,
    error: undefined,
    indexRefused: undefined,
  };

  private readonly opts: KbServiceOptions;

  constructor(opts: KbServiceOptions) {
    this.opts = opts;
  }

  /** The guides in use; throws if none could be loaded yet. */
  get current(): KnowledgeBase {
    if (!this.kb) throw new Error("The guides are not loaded yet");
    return this.kb;
  }

  get ready(): boolean {
    return this.kb !== undefined;
  }

  /** Load the guides once (so the bot can answer), then keep them up to date in the background. */
  async start(): Promise<void> {
    try {
      await this.refresh(true);
    } catch (err) {
      this.status.error = `${describeError(err).type}: ${describeError(err).message.slice(0, 200)}`;
      logger.error({ err: describeError(err) }, "Loading the guides failed at start");
      this.opts.onAlert?.(`Loading the guides failed at start: ${this.status.error}`);
    }
    this.timer = setInterval(() => {
      this.refresh(false).catch((err) => {
        this.status.error = `${describeError(err).type}: ${describeError(err).message.slice(0, 200)}`;
        logger.error(
          { err: describeError(err) },
          "Updating the guides failed; keeping the last good version",
        );
      });
    }, Math.max(this.opts.syncMinutes, 1) * 60_000);
    this.timer.unref();
  }

  stop(): void {
    if (this.timer) clearInterval(this.timer);
  }

  /** Fetch (or re-read) the guides and swap them in if they changed and pass the check. */
  refresh(force: boolean): Promise<boolean> {
    const next = this.queue.then(() => (this.opts.repo ? this.syncFromGit(force) : this.readLocal(force)));
    this.queue = next.catch(() => undefined);
    return next;
  }

  private async readLocal(force: boolean): Promise<boolean> {
    const candidate = await KnowledgeBase.build(this.opts.dir);
    this.status.lastSync = new Date().toISOString();
    this.status.error = undefined;
    if (!force && this.kb && sameDocs(this.kb, candidate)) return false;
    return this.trySwap(candidate, { allowUnchecked: true });
  }

  private async syncFromGit(force: boolean): Promise<boolean> {
    const dir = this.opts.dir;
    let before = "";
    if (await exists(path.join(dir, ".git"))) {
      before = await this.git(["rev-parse", "HEAD"], dir);
      await this.git(["sparse-checkout", "set", "--no-cone", ...SPARSE_PATTERNS], dir);
      await this.git(["fetch", "--depth", "1", "origin", this.opts.branch], dir, true);
      await this.git(["reset", "--hard", "FETCH_HEAD"], dir);
    } else {
      await rm(dir, { recursive: true, force: true });
      await mkdir(path.dirname(dir), { recursive: true });
      try {
        await this.git(
          [
            "clone",
            "--depth",
            "1",
            "--filter=blob:none",
            "--no-checkout",
            "--branch",
            this.opts.branch,
            this.opts.repo ?? "",
            dir,
          ],
          undefined,
          true,
        );
        await this.git(["sparse-checkout", "set", "--no-cone", ...SPARSE_PATTERNS], dir);
        await this.git(["checkout", this.opts.branch], dir, true);
      } catch (err) {
        await rm(dir, { recursive: true, force: true }); // start from scratch next time
        throw err;
      }
    }
    const after = await this.git(["rev-parse", "HEAD"], dir);
    this.status.lastSync = new Date().toISOString();
    this.status.commit = after.slice(0, 7);
    this.status.error = undefined;
    if (after === before && !force && this.kb) return false;

    const candidate = await KnowledgeBase.build(dir, after);
    if (await this.trySwap(candidate, { allowUnchecked: false })) return true;
    if (!this.kb) await this.loadLastGood();
    return false;
  }

  /** Swap in a new version unless it looks broken next to the one in use (or the last good one). */
  private async trySwap(
    candidate: KnowledgeBase,
    { allowUnchecked }: { allowUnchecked: boolean },
  ): Promise<boolean> {
    const baseline = this.kb
      ? { commit: this.kb.meta.commit, counts: this.kb.sectionCounts() }
      : await this.loadBaseline();
    const counts = candidate.sectionCounts();
    const problems = baseline ? compareCounts(baseline.counts, counts) : [];
    const accepted =
      this.opts.acceptCommit !== undefined &&
      this.opts.acceptCommit.length >= 7 &&
      candidate.meta.commit?.startsWith(this.opts.acceptCommit) === true;
    if (problems.length > 0 && accepted) {
      logger.warn(
        { problems, commit: candidate.meta.commit?.slice(0, 7) },
        "Guides loaded despite the check (KB_ACCEPT_COMMIT)",
      );
    } else if (problems.length > 0 && !(allowUnchecked && !this.kb)) {
      const where = candidate.meta.commit ? `commit ${candidate.meta.commit.slice(0, 7)}` : "local guides";
      this.status.indexRefused = `${where}: ${problems.join("; ")}`;
      logger.error({ problems }, "New version of the guides NOT loaded; keeping the last good version");
      this.opts.onAlert?.(`Guides refused (${where}): ${problems.join("; ")}`);
      return false;
    } else if (problems.length > 0) logger.warn({ problems }, "Local guides changed sharply; loaded anyway");
    this.kb = candidate;
    this.status.indexRefused = undefined;
    await this.opts.store.save({ commit: candidate.meta.commit, counts }).catch((err) => {
      logger.warn({ err: describeError(err) }, "Could not remember the last good version of the guides");
    });
    for (const w of candidate.meta.warnings) logger.warn({ warning: w }, "Guide warning");
    logger.info(
      {
        commit: candidate.meta.commit?.slice(0, 7),
        guides: candidate.guides.length,
        sections: candidate.sections.length,
      },
      "Guides loaded",
    );
    return true;
  }

  /** After a restart with a refused newest commit: load the last good commit instead. */
  private async loadLastGood(): Promise<void> {
    const baseline = await this.loadBaseline();
    if (!baseline?.commit) return;
    const dir = this.opts.dir;
    await this.git(["fetch", "--depth", "1", "origin", baseline.commit], dir, true);
    await this.git(["checkout", "--detach", baseline.commit], dir);
    const kb = await KnowledgeBase.build(dir, baseline.commit);
    this.kb = kb;
    logger.warn({ commit: baseline.commit.slice(0, 7) }, "Loaded the last good version of the guides");
  }

  private async loadBaseline(): Promise<KbBaseline | undefined> {
    try {
      return await this.opts.store.load();
    } catch (err) {
      logger.warn({ err: describeError(err) }, "Could not read the last good version of the guides");
      return undefined;
    }
  }

  private async git(args: string[], cwd?: string, network = false): Promise<string> {
    const auth =
      network && this.opts.githubToken
        ? // Sent as a header, so the token never lands in .git/config or the logs.
          ["-c", `http.extraHeader=Authorization: Bearer ${this.opts.githubToken}`]
        : [];
    try {
      const { stdout } = await run("git", [...auth, ...args], {
        cwd,
        env: { ...process.env, GIT_TERMINAL_PROMPT: "0" },
        timeout: 300_000,
        maxBuffer: 16 * 1024 * 1024,
      });
      return stdout.trim();
    } catch (err) {
      const stderr = String((err as { stderr?: string }).stderr ?? "")
        .trim()
        .slice(-500);
      throw new Error(`git ${args[0]} failed: ${stderr || describeError(err).message}`);
    }
  }
}

function sameDocs(a: KnowledgeBase, b: KnowledgeBase): boolean {
  const key = (kb: KnowledgeBase) =>
    kb.guides
      .map((g) => `${g.slug}:${g.docSha1}`)
      .sort()
      .join(",");
  return key(a) === key(b);
}

async function exists(p: string): Promise<boolean> {
  try {
    await stat(p);
    return true;
  } catch {
    return false;
  }
}
