import { type Database, openDatabase } from "../../src/db/client.ts";

/** A fresh in-memory Postgres (PGlite) with every migration applied. */
export function memoryDb(): Promise<Database> {
  return openDatabase({ url: undefined, dataDir: "", memory: true });
}
