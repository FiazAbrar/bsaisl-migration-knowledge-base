import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import type { Database } from "../../src/db/client.ts";
import { bucket, bucketEnd, DAY, Guard, limit } from "../../src/guard/guard.ts";
import { memoryDb } from "../helpers/db.ts";

let database: Database;
let now: number;
let guard: Guard;

beforeEach(async () => {
  database = await memoryDb();
  // 2026-11-24 10:00:30 Bangladesh time (04:00:30 UTC).
  now = Date.UTC(2026, 10, 24, 4, 0, 30) / 1000;
  guard = new Guard(database.db, () => now);
});
afterEach(async () => {
  vi.unstubAllEnvs();
  await database.close();
});

describe("time windows", () => {
  it("starts days at midnight in Dhaka", () => {
    const end = bucketEnd(DAY, now);
    expect(new Date(end * 1000).toISOString()).toBe("2026-11-24T18:00:00.000Z"); // 00:00 on the 25th, UTC+6
    expect(bucket(DAY, end - 1)).toBe(bucket(DAY, now));
    expect(bucket(DAY, end)).toBe(bucket(DAY, now) + 1);
  });
});

describe("limit", () => {
  it("reads the environment and falls back to the default", () => {
    expect(limit("GUARD_WEB_PER_MINUTE", {})).toBe(20);
    expect(limit("GUARD_WEB_PER_MINUTE", { GUARD_WEB_PER_MINUTE: "6" })).toBe(6);
    expect(limit("GUARD_WEB_PER_MINUTE", { GUARD_WEB_PER_MINUTE: "lots" })).toBe(20);
  });
});

describe("Guard.check", () => {
  it("allows up to the per-minute limit, then refuses and tells the person once", async () => {
    vi.stubEnv("GUARD_WHATSAPP_PER_MINUTE", "2");
    expect((await guard.check("whatsapp", "u")).ok).toBe(true);
    expect((await guard.check("whatsapp", "u")).ok).toBe(true);
    const third = await guard.check("whatsapp", "u");
    expect(third).toMatchObject({ ok: false, reason: "minute", notify: true });
    expect(third.retryAfter).toBe(30);
    expect(await guard.check("whatsapp", "u")).toMatchObject({ ok: false, notify: false });
    // Another person is not affected.
    expect((await guard.check("whatsapp", "v")).ok).toBe(true);
    // The next minute starts fresh.
    now += 60;
    expect((await guard.check("whatsapp", "u")).ok).toBe(true);
  });

  it("does not count refused messages toward the day", async () => {
    vi.stubEnv("GUARD_TELEGRAM_PER_MINUTE", "1");
    vi.stubEnv("GUARD_TELEGRAM_PER_DAY", "2");
    expect((await guard.check("telegram", "u")).ok).toBe(true);
    expect((await guard.check("telegram", "u")).reason).toBe("minute"); // refused: not counted
    now += 60;
    expect((await guard.check("telegram", "u")).ok).toBe(true); // second of the day
    now += 60;
    expect((await guard.check("telegram", "u")).reason).toBe("day");
  });

  it("limits a web IP address and all web visitors together", async () => {
    vi.stubEnv("GUARD_IP_PER_DAY", "1");
    expect((await guard.check("web", "u1", "ip1")).ok).toBe(true);
    expect((await guard.check("web", "u2", "ip1")).reason).toBe("ip");
    vi.stubEnv("GUARD_WEB_ALL_PER_MINUTE", "1"); // u1 used the one place; u2's refusal was not counted
    expect((await guard.check("web", "u3", "ip2")).reason).toBe("busy");
  });

  it("pauses only the channel whose AI budget is spent", async () => {
    vi.stubEnv("BUDGET_WEB_USD", "1");
    await guard.addCost("web", 0.6);
    expect((await guard.check("web", "u")).ok).toBe(true);
    await guard.addCost("web", 0.5);
    expect((await guard.check("web", "u")).reason).toBe("budget");
    expect((await guard.check("whatsapp", "u")).ok).toBe(true);
    expect((await guard.spending()).web.spentUsd).toBeCloseTo(1.1);
  });
});

describe("Guard.command and newSession", () => {
  it("lets commands through even when the daily limit is used up", async () => {
    vi.stubEnv("GUARD_WEB_PER_DAY", "1");
    await guard.check("web", "u");
    expect((await guard.check("web", "u")).ok).toBe(false);
    expect((await guard.command("web", "u")).ok).toBe(true);
  });

  it("limits new web sessions per IP per hour", async () => {
    vi.stubEnv("GUARD_SESSIONS_PER_HOUR", "1");
    expect((await guard.newSession("ip")).ok).toBe(true);
    expect((await guard.newSession("ip")).reason).toBe("sessions");
  });
});
