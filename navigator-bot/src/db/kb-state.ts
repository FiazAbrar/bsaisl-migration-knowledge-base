/** Remembers the last version of the guides that passed the safe-swap check (src/kb/service.ts). */
import { eq } from "drizzle-orm";
import type { KbBaseline, KbBaselineStore } from "../kb/service.ts";
import type { Db } from "./client.ts";
import { kbState } from "./schema.ts";

export class DbKbBaselineStore implements KbBaselineStore {
  private readonly db: Db;

  constructor(db: Db) {
    this.db = db;
  }

  async load(): Promise<KbBaseline | undefined> {
    const rows = await this.db.select().from(kbState).where(eq(kbState.id, 1)).limit(1);
    const row = rows[0];
    return row ? { commit: row.commit ?? undefined, counts: row.counts } : undefined;
  }

  async save(baseline: KbBaseline): Promise<void> {
    const values = { id: 1, commit: baseline.commit ?? null, counts: baseline.counts, updatedAt: new Date() };
    await this.db.insert(kbState).values(values).onConflictDoUpdate({ target: kbState.id, set: values });
  }
}
