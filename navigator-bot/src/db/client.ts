/**
 * The database: Postgres when DATABASE_URL is set (Neon in the cloud, BRAC IT's server later), otherwise
 * PGlite, a Postgres engine embedded in the bot that stores its files in data/pglite (local PCs and tests).
 * Migrations in drizzle/ are applied at start-up.
 */
import { mkdir } from "node:fs/promises";
import path from "node:path";
import { PGlite } from "@electric-sql/pglite";
import type { ExtractTablesWithRelations } from "drizzle-orm";
import { drizzle as drizzlePg } from "drizzle-orm/node-postgres";
import { migrate as migratePg } from "drizzle-orm/node-postgres/migrator";
import type { PgDatabase, PgQueryResultHKT, PgTransaction } from "drizzle-orm/pg-core";
import { drizzle as drizzleLite } from "drizzle-orm/pglite";
import { migrate as migrateLite } from "drizzle-orm/pglite/migrator";
import pg from "pg";
import { BOT_ROOT } from "../config.ts";
import * as schema from "./schema.ts";

export type Schema = typeof schema;
export type Db = PgDatabase<PgQueryResultHKT, Schema>;
export type Tx = PgTransaction<PgQueryResultHKT, Schema, ExtractTablesWithRelations<Schema>>;

export interface Database {
  db: Db;
  kind: "postgres" | "pglite";
  /** The Postgres pool, shared with Chat SDK's state adapter (Postgres only). */
  pool: pg.Pool | undefined;
  close(): Promise<void>;
}

const MIGRATIONS = path.join(BOT_ROOT, "drizzle");

export async function openDatabase(opts: {
  url: string | undefined;
  dataDir: string;
  memory?: boolean;
}): Promise<Database> {
  if (opts.url) {
    const pool = new pg.Pool({
      connectionString: opts.url,
      max: 5,
      connectionTimeoutMillis: 15_000,
      idleTimeoutMillis: 30_000,
    });
    // A dropped connection is replaced by the pool; log it instead of crashing.
    pool.on("error", () => undefined);
    const db = drizzlePg(pool, { schema }) as unknown as Db;
    await migratePg(drizzlePg(pool), { migrationsFolder: MIGRATIONS });
    return { db, kind: "postgres", pool, close: () => pool.end() };
  }
  let client: PGlite;
  if (opts.memory) {
    client = new PGlite();
  } else {
    const dir = path.join(opts.dataDir, "pglite");
    await mkdir(dir, { recursive: true });
    client = new PGlite(dir);
  }
  const lite = drizzleLite(client, { schema });
  await migrateLite(lite, { migrationsFolder: MIGRATIONS });
  return { db: lite as unknown as Db, kind: "pglite", pool: undefined, close: () => client.close() };
}
