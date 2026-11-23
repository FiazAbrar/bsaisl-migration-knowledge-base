import { createHmac } from "node:crypto";
import { afterAll, beforeAll, describe, expect, it, vi } from "vitest";
import { type App, buildApp } from "../../src/app.ts";
import { loadConfig, telegramSecretFor } from "../../src/config.ts";
import { makeKb } from "../helpers/kb-fixture.ts";

const APP_SECRET = "test-app-secret";
const VERIFY = "verify-me";
const TG_TOKEN = "123456:TEST-token-abcdefghijklmnopqrstu";

interface Call {
  url: string;
  body: unknown;
}
const calls: Call[] = [];
const realFetch = globalThis.fetch;

/** Pretend to be Meta's Graph API and Telegram's Bot API; everything else is refused. */
async function fakeFetch(input: string | URL | Request, init?: RequestInit): Promise<Response> {
  const url = typeof input === "string" ? input : input instanceof URL ? input.href : input.url;
  const raw = init?.body ?? (input instanceof Request ? await input.text() : undefined);
  let body: unknown = raw;
  try {
    body = typeof raw === "string" ? JSON.parse(raw) : raw;
  } catch {
    // form bodies stay as they are
  }
  calls.push({ url, body });
  if (url.includes("graph.facebook.com")) {
    return Response.json({
      messaging_product: "whatsapp",
      messages: [{ id: `wamid.out${calls.length}` }],
      success: true,
    });
  }
  if (url.includes("api.telegram.org")) {
    return Response.json({
      ok: true,
      result: { message_id: calls.length, date: 0, chat: { id: 42, type: "private" } },
    });
  }
  return new Response("not allowed in tests", { status: 599 });
}

async function waitFor<T>(find: () => T | undefined, ms = 8000): Promise<T> {
  const until = Date.now() + ms;
  for (;;) {
    const found = find();
    if (found !== undefined) return found;
    if (Date.now() > until) {
      throw new Error(`timed out waiting; calls so far: ${JSON.stringify(calls).slice(0, 2000)}`);
    }
    await new Promise((r) => setTimeout(r, 25));
  }
}

let app: App;
let cleanupKb: () => Promise<void>;

beforeAll(async () => {
  vi.stubGlobal("fetch", fakeFetch);
  const kb = await makeKb();
  cleanupKb = kb.cleanup;
  const config = loadConfig({
    NODE_ENV: "test",
    KB_DIR: kb.dir,
    USER_HASH_SECRET: "test-user-hash-secret-0123456789abcdef",
    WHATSAPP_ACCESS_TOKEN: "wa-token",
    WHATSAPP_APP_SECRET: APP_SECRET,
    WHATSAPP_PHONE_NUMBER_ID: "1234567890",
    WHATSAPP_VERIFY_TOKEN: VERIFY,
    TELEGRAM_BOT_TOKEN: TG_TOKEN,
  });
  app = await buildApp({ config, memoryDatabase: true, skipTelegramSetup: true });
});

afterAll(async () => {
  await app.shutdown();
  await cleanupKb();
  vi.stubGlobal("fetch", realFetch);
});

function whatsappUpdate(id: string, text: string) {
  return JSON.stringify({
    object: "whatsapp_business_account",
    entry: [
      {
        id: "WABA",
        changes: [
          {
            field: "messages",
            value: {
              messaging_product: "whatsapp",
              metadata: { display_phone_number: "15550001111", phone_number_id: "1234567890" },
              contacts: [{ profile: { name: "Test" }, wa_id: "15551234567" }],
              messages: [
                { from: "15551234567", id, timestamp: "1700000000", type: "text", text: { body: text } },
              ],
            },
          },
        ],
      },
    ],
  });
}

const sign = (body: string) => `sha256=${createHmac("sha256", APP_SECRET).update(body).digest("hex")}`;

describe("/health", () => {
  it("reports the guides, database and channels", async () => {
    const res = await app.http.request("/health");
    expect(res.status).toBe(200);
    expect(await res.json()).toMatchObject({
      status: "ok",
      database: "pglite",
      ai: "test",
      kb_guides: 3,
      kb_commit: "local",
      channels: { whatsapp: true, telegram: true, web: true },
    });
  });
});

describe("WhatsApp", () => {
  it("answers Meta's verification handshake only with the right token", async () => {
    const ok = await app.http.request(
      `/webhook?hub.mode=subscribe&hub.verify_token=${VERIFY}&hub.challenge=12345`,
    );
    expect(ok.status).toBe(200);
    expect(await ok.text()).toBe("12345");
    const bad = await app.http.request("/webhook?hub.mode=subscribe&hub.verify_token=wrong&hub.challenge=1");
    expect(bad.status).toBe(403);
  });

  it("refuses an unsigned message", async () => {
    const body = whatsappUpdate("wamid.bad", "hi");
    const res = await app.http.request("/webhook", {
      method: "POST",
      body,
      headers: { "x-hub-signature-256": "sha256=00" },
    });
    expect(res.status).toBeGreaterThanOrEqual(400);
  });

  it("answers a signed message once, even if Meta delivers it twice", async () => {
    calls.length = 0;
    const body = whatsappUpdate("wamid.1", "Malaysia calling visa");
    const headers = { "x-hub-signature-256": sign(body), "content-type": "application/json" };
    expect((await app.http.request("/webhook", { method: "POST", body, headers })).status).toBe(200);
    expect((await app.http.request("/webhook", { method: "POST", body, headers })).status).toBe(200);
    const sent = await waitFor(() =>
      calls.find(
        (c) => c.url.endsWith("/1234567890/messages") && JSON.stringify(c.body).includes("Calling visa"),
      ),
    );
    expect(JSON.stringify(sent.body)).toContain("Closest sections in the *Malaysia* guide");
    await new Promise((r) => setTimeout(r, 300));
    const replies = calls.filter((c) => JSON.stringify(c.body).includes("Closest sections"));
    expect(replies).toHaveLength(1);
  });
});

describe("Telegram", () => {
  const update = (updateId: number, text: string, entities?: unknown[]) =>
    JSON.stringify({
      update_id: updateId,
      message: {
        message_id: updateId,
        date: 1700000000,
        chat: { id: 42, type: "private", first_name: "T" },
        from: { id: 42, is_bot: false, first_name: "T" },
        text,
        ...(entities ? { entities } : {}),
      },
    });

  it("refuses an update without the secret token", async () => {
    const res = await app.http.request("/telegram", { method: "POST", body: update(1, "hi") });
    expect(res.status).toBeGreaterThanOrEqual(400);
  });

  it("answers /start with the welcome", async () => {
    calls.length = 0;
    const res = await app.http.request("/telegram", {
      method: "POST",
      body: update(2, "/start", [{ type: "bot_command", offset: 0, length: 6 }]),
      headers: {
        "x-telegram-bot-api-secret-token": telegramSecretFor(TG_TOKEN),
        "content-type": "application/json",
      },
    });
    expect(res.status).toBe(200);
    const sent = await waitFor(() =>
      calls.find((c) => JSON.stringify(c.body).includes("I answer questions")),
    );
    expect(sent.url).toContain("api.telegram.org");
  });
});

describe("web chat", () => {
  it("gives a session, then answers through the AI SDK stream", async () => {
    const config = await (await app.http.request("/api/config")).json();
    expect(config).toMatchObject({ max_chars: 500, turnstile_site_key: null });
    expect((config as { countries: { slug: string }[] }).countries.map((c) => c.slug)).toEqual([
      "saudi-arabia",
      "malaysia",
    ]);

    const noSession = await app.http.request("/api/chat", { method: "POST", body: "{}" });
    expect(noSession.status).toBe(401);

    const session = await app.http.request("/api/session", {
      method: "POST",
      body: "{}",
      headers: { "content-type": "application/json" },
    });
    expect(session.status).toBe(200);
    const cookie = (session.headers.get("set-cookie") ?? "").split(";")[0] ?? "";
    expect(cookie).toMatch(/^nav_sid=/);

    const chat = await app.http.request("/api/chat", {
      method: "POST",
      headers: { "content-type": "application/json", cookie },
      body: JSON.stringify({
        id: "conv1",
        trigger: "submit-message",
        messages: [{ id: "m1", role: "user", parts: [{ type: "text", text: "Saudi medical test" }] }],
      }),
    });
    expect(chat.status).toBe(200);
    const stream = await chat.text();
    expect(stream).toContain("Medical test");

    const me = await app.http.request("/api/me", { headers: { cookie } });
    expect(await me.json()).toEqual({ country: "saudi-arabia" });
  });

  it("refuses requests from another website", async () => {
    const res = await app.http.request("/api/session", {
      method: "POST",
      body: "{}",
      headers: { "content-type": "application/json", origin: "https://evil.example", host: "localhost" },
    });
    expect(res.status).toBe(403);
  });
});
