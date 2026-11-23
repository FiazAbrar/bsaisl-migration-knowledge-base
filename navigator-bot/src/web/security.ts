/**
 * Web chat security: no login, so every visitor first gets a signed session cookie after a bot check
 * (Cloudflare Turnstile, when TURNSTILE_SECRET_KEY is set). Requests from other websites are refused,
 * and the visitor's IP address is taken from the proxy header only when the proxy is trusted.
 */
import { createHmac, randomBytes, timingSafeEqual } from "node:crypto";
import { BlockList, isIP } from "node:net";
import { userKey } from "../memory/store.ts";

export const COOKIE = "nav_sid";
export const SESSION_SECONDS = 24 * 3600;
export const DEFAULT_TRUSTED = "127.0.0.0/8,::1/128,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16,fc00::/7";
export const TURNSTILE_VERIFY = "https://challenges.cloudflare.com/turnstile/v0/siteverify";

function sign(secret: string, sid: string, ts: string): string {
  const key = createHmac("sha256", secret).update("navigator-web-session").digest();
  return createHmac("sha256", key).update(`${sid}.${ts}`).digest("hex");
}

export function newSessionCookie(secret: string, nowS = Math.floor(Date.now() / 1000)): string {
  const sid = randomBytes(18).toString("base64url");
  const ts = String(nowS);
  return `${sid}.${ts}.${sign(secret, sid, ts)}`;
}

/** The session id in a cookie value, if we signed it less than a day ago. */
export function sessionId(
  secret: string,
  value: string | undefined,
  nowS = Date.now() / 1000,
): string | undefined {
  const parts = (value ?? "").split(".");
  if (parts.length !== 3) return undefined;
  const [sid = "", ts = "", sig = ""] = parts;
  if (!/^[\w-]{1,64}$/.test(sid) || !/^\d{1,12}$/.test(ts) || !/^[0-9a-f]{64}$/.test(sig)) return undefined;
  const expected = Buffer.from(sign(secret, sid, ts));
  if (!timingSafeEqual(expected, Buffer.from(sig))) return undefined;
  const age = nowS - Number(ts);
  return age >= 0 && age < SESSION_SECONDS ? sid : undefined;
}

export function trustedProxies(list: string | undefined): BlockList {
  const blocks = new BlockList();
  for (const entry of (list || DEFAULT_TRUSTED).split(",")) {
    const [addr = "", bits] = entry.trim().split("/");
    const type = isIP(addr) === 6 ? "ipv6" : isIP(addr) === 4 ? "ipv4" : undefined;
    if (!type) continue;
    blocks.addSubnet(addr, Number(bits ?? (type === "ipv6" ? 128 : 32)), type);
  }
  return blocks;
}

export function isTrustedPeer(blocks: BlockList, addr: string): boolean {
  const plain = addr.replace(/^::ffff:/, "");
  const type = isIP(plain) === 6 ? "ipv6" : isIP(plain) === 4 ? "ipv4" : undefined;
  return type !== undefined && blocks.check(plain, type);
}

/**
 * The visitor's address. Behind a proxy (Render, Cloudflare, ngrok) set PROXY_IP_HEADER, or every visitor
 * looks like the proxy and shares one limit. The header is believed only from a trusted proxy.
 */
export function clientIp(
  peer: string,
  headerValue: string | undefined,
  headerName: string | undefined,
  blocks: BlockList,
): string {
  const plainPeer = peer.replace(/^::ffff:/, "");
  if (!headerName || !isTrustedPeer(blocks, plainPeer)) return plainPeer;
  let value = headerValue ?? "";
  // X-Forwarded-For: the entry added by our own proxy is the last one; earlier ones can be forged.
  if (headerName.toLowerCase() === "x-forwarded-for") value = value.split(",").at(-1) ?? "";
  return value.trim() || plainPeer;
}

/** The hashed address used by the limits; IPv6 counts by its /64 block. */
export function ipKey(ip: string, secret: string): string {
  let id = ip;
  if (isIP(ip) === 6) {
    const groups = expandIpv6(ip).slice(0, 4);
    id = `${groups.join(":")}::/64`;
  }
  return userKey(`ip:${id}`, secret);
}

function expandIpv6(ip: string): string[] {
  const [head = "", tail = ""] = ip.split("::");
  const h = head ? head.split(":") : [];
  const t = tail ? tail.split(":") : [];
  const missing = ip.includes("::") ? 8 - h.length - t.length : 0;
  return [...h, ...Array.from({ length: missing }, () => "0"), ...t].map((g) =>
    g.toLowerCase().replace(/^0+(?=.)/, ""),
  );
}

/** Refuse requests sent by another website's page (cross-site request forgery). */
export function sameSite(
  secFetchSite: string | undefined,
  origin: string | undefined,
  host: string | undefined,
  publicDomain: string | undefined,
): boolean {
  if (secFetchSite === "cross-site") return false;
  if (!origin) return true; // not sent by a browser page; the cookie and bot check still apply
  let originHost: string;
  try {
    originHost = new URL(origin).host;
  } catch {
    return false;
  }
  return [host, publicDomain].filter(Boolean).includes(originHost);
}

export async function verifyTurnstile(
  secret: string,
  token: string,
  remoteIp: string,
  expectedHostname: string | undefined,
  fetchFn: typeof fetch = fetch,
): Promise<boolean> {
  try {
    const res = await fetchFn(TURNSTILE_VERIFY, {
      method: "POST",
      body: new URLSearchParams({ secret, response: token, remoteip: remoteIp }),
      signal: AbortSignal.timeout(8000),
    });
    const data = (await res.json()) as { success?: boolean; hostname?: string };
    return data.success === true && (!expectedHostname || data.hostname === expectedHostname);
  } catch {
    return false;
  }
}
