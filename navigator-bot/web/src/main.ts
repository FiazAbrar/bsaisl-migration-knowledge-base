/* Migration Navigator web chat.
 *
 * Safety rules for this file:
 * - Text from the visitor or the server is only ever placed with textContent or createTextNode.
 *   Never innerHTML, outerHTML, insertAdjacentHTML or document.write.
 * - Links in replies are rebuilt as <a> elements only for https URLs, opened with rel="noopener noreferrer".
 * - Icons are fixed shapes in index.html, referenced by fixed ids from this file; nothing from the server.
 * - No keys live here: the page talks only to its own server (/api/...), which holds the secrets.
 */
import { charCount, cleanText, maskPersonal } from "../../src/conversation/safeguards.ts";
import { readReply } from "./stream.ts";
import { type Lang, STR, type StrKey, TOPICS } from "./strings.ts";

const MIN_GAP_MS = 1500; // shortest time between two sends from this page
const REQUEST_TIMEOUT_MS = 90_000;
const TURNSTILE_SRC = "https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit";
const SVG_NS = "http://www.w3.org/2000/svg";

interface Country {
  slug: string;
  en: string;
  bn: string;
}

interface TurnstileApi {
  render(el: HTMLElement, opts: Record<string, unknown>): string;
  reset(id: string): void;
}
declare global {
  interface Window {
    turnstile?: TurnstileApi;
  }
}

function el<T extends HTMLElement>(id: string): T {
  const found = document.getElementById(id);
  if (!found) throw new Error(`Missing #${id}`);
  return found as T;
}

const chatEl = el("chat");
const feed = el("feed");
const form = el<HTMLFormElement>("composer");
const input = el<HTMLTextAreaElement>("composer-input");
const sendBtn = el<HTMLButtonElement>("send");
const counter = el("counter");
const statusEl = el("status");
const langBtn = el<HTMLButtonElement>("lang-toggle");
const langLabel = el("lang-label");
const themeBtn = el<HTMLButtonElement>("theme-toggle");
const sidebar = el("sidebar");
const scrim = el("scrim");
const menuBtn = el<HTMLButtonElement>("menu-btn");
const menuCloseBtn = el<HTMLButtonElement>("menu-close");
const guideChip = el<HTMLButtonElement>("guide-chip");
const guideLabel = el("guide-label");
const themeIcon = document.getElementById("theme-icon") as unknown as SVGUseElement;
const newChatBtn = el<HTMLButtonElement>("new-chat");
const forgetBtn = el<HTMLButtonElement>("forget");
const botCheckEl = el("bot-check");
const welcomeTpl = el<HTMLTemplateElement>("tpl-welcome");
const sideTopics = document.querySelector<HTMLElement>('[data-topics="list"]');

let lang: Lang = loadLang();
let maxChars = Number(input.getAttribute("maxlength")) || 500;
let siteKey = "";
let countries: Country[] = [];
let currentSlug: string | null = null; // the guide the server is answering from, as it last told us
let guidesUpdated = ""; // YYYY-MM-DD from /api/config
let busy = false;
let lastSend = 0;
let sessionPromise: Promise<void> | null = null;
let turnstileWidget: string | null = null;
let turnstileWaiter: { resolve: (t: string) => void; reject: (e: Error) => void } | null = null;
let conversationId = newId();

function newId(): string {
  return crypto.randomUUID ? crypto.randomUUID() : `${Date.now()}-${Math.random().toString(36).slice(2)}`;
}

// ---------- language ----------

function loadLang(): Lang {
  try {
    const saved = localStorage.getItem("navigator.lang");
    if (saved === "en" || saved === "bn") return saved;
  } catch {
    // storage blocked: fall back to Bangla
  }
  return "bn";
}

function t(key: StrKey, vars?: Record<string, string | number>): string {
  let s = STR[lang][key] || STR.en[key] || "";
  if (vars) for (const [k, v] of Object.entries(vars)) s = s.split(`{${k}}`).join(String(v));
  return s;
}

function applyLang(): void {
  document.documentElement.lang = lang;
  document.title = t("title");
  for (const node of document.querySelectorAll<HTMLElement>("[data-i18n]")) {
    node.textContent = t(node.dataset.i18n as StrKey);
  }
  for (const node of document.querySelectorAll<HTMLElement>("[data-i18n-label]")) {
    node.setAttribute("aria-label", t(node.dataset.i18nLabel as StrKey));
  }
  for (const node of document.querySelectorAll<HTMLElement>("[data-i18n-placeholder]")) {
    node.setAttribute("placeholder", t(node.dataset.i18nPlaceholder as StrKey));
  }
  langLabel.textContent = t("langButton");
  langBtn.setAttribute("lang", lang === "bn" ? "en" : "bn");
  langBtn.setAttribute("aria-label", t("langLabel"));
  renderTopics(sideTopics, "row");
  renderWelcome();
  renderGuide();
  showTheme();
}

langBtn.addEventListener("click", () => {
  lang = lang === "bn" ? "en" : "bn";
  try {
    localStorage.setItem("navigator.lang", lang);
  } catch {
    // not saved; still applies to this visit
  }
  applyLang();
});

// ---------- colour theme: follow the phone, light or dark ----------

type Theme = "system" | "light" | "dark";
const THEMES: Theme[] = ["system", "light", "dark"];
const THEME_ICON: Record<Theme, string> = { system: "i-auto", light: "i-sun", dark: "i-moon" };
const THEME_LABEL: Record<Theme, StrKey> = { system: "themeSystem", light: "themeLight", dark: "themeDark" };

function currentTheme(): Theme {
  const theme = document.documentElement.getAttribute("data-theme");
  return theme === "light" || theme === "dark" ? theme : "system";
}

function showTheme(): void {
  const theme = currentTheme();
  themeIcon?.setAttribute("href", `#${THEME_ICON[theme]}`);
  themeBtn.setAttribute("aria-label", t(THEME_LABEL[theme]));
  themeBtn.setAttribute("title", t(THEME_LABEL[theme]));
}

themeBtn.addEventListener("click", () => {
  const next = THEMES[(THEMES.indexOf(currentTheme()) + 1) % THEMES.length] ?? "system";
  if (next === "system") document.documentElement.removeAttribute("data-theme");
  else document.documentElement.setAttribute("data-theme", next);
  try {
    if (next === "system") localStorage.removeItem("navigator.theme");
    else localStorage.setItem("navigator.theme", next);
  } catch {
    // not saved; still applies to this visit
  }
  showTheme();
});

// ---------- menu (phones): the sidebar slides in ----------

const narrow = window.matchMedia("(max-width: 1023px)");

function openMenu(): void {
  sidebar.classList.add("open");
  scrim.hidden = false;
  menuBtn.setAttribute("aria-expanded", "true");
  menuCloseBtn.focus();
}

function closeMenu(returnFocus = true): void {
  if (!sidebar.classList.contains("open")) return;
  sidebar.classList.remove("open");
  scrim.hidden = true;
  menuBtn.setAttribute("aria-expanded", "false");
  if (returnFocus) menuBtn.focus();
}

menuBtn.addEventListener("click", openMenu);
menuCloseBtn.addEventListener("click", () => closeMenu());
scrim.addEventListener("click", () => closeMenu());
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") closeMenu();
});
narrow.addEventListener("change", () => closeMenu(false));

// ---------- the guide in use ----------

function countryName(slug: string | null): string {
  const c = countries.find((x) => x.slug === slug);
  return c ? (lang === "bn" ? c.bn : c.en) : "";
}

function renderGuide(): void {
  const name = countryName(currentSlug);
  guideLabel.textContent = name || t("noCountry");
  guideChip.classList.toggle("empty", !name);
  for (const b of document.querySelectorAll<HTMLButtonElement>(".country")) {
    const on = b.dataset.slug === currentSlug;
    b.classList.toggle("active", on);
    b.setAttribute("aria-pressed", on ? "true" : "false");
  }
}

guideChip.addEventListener("click", () => {
  const section = feed.querySelector('[data-section="countries"]');
  if (!section) return;
  section.scrollIntoView({ block: "center" });
  const first =
    section.querySelector<HTMLElement>(".country.active") ?? section.querySelector<HTMLElement>(".country");
  first?.focus({ preventScroll: true });
});

// ---------- building blocks (text only, never HTML) ----------

function icon(id: string): SVGSVGElement {
  const svg = document.createElementNS(SVG_NS, "svg");
  svg.setAttribute("aria-hidden", "true");
  svg.setAttribute("focusable", "false");
  const use = document.createElementNS(SVG_NS, "use");
  use.setAttribute("href", `#${id}`);
  svg.appendChild(use);
  return svg;
}

function avatar(): HTMLElement {
  const a = document.createElement("span");
  a.className = "avatar";
  a.setAttribute("aria-hidden", "true");
  a.appendChild(icon("i-compass"));
  return a;
}

function renderTopics(container: HTMLElement | null, kind: "row" | "card"): void {
  if (!container) return;
  container.replaceChildren();
  for (const topic of TOPICS) {
    const b = document.createElement("button");
    b.type = "button";
    b.className = kind === "row" ? "topic-row" : "topic-card";
    b.disabled = busy;
    const ic = document.createElement("span");
    ic.className = "topic-icon";
    ic.appendChild(icon(topic.icon));
    const label = document.createElement("span");
    label.textContent = t(`topic_${topic.id}` as StrKey);
    b.append(ic, label);
    b.addEventListener("click", () => {
      closeMenu(false);
      void send(t(`topicq_${topic.id}` as StrKey));
    });
    container.appendChild(b);
  }
}

function renderCountries(container: HTMLElement): void {
  container.replaceChildren();
  for (const c of countries) {
    const b = document.createElement("button");
    b.type = "button";
    b.className = "country";
    b.dataset.slug = c.slug;
    b.disabled = busy;
    const name = lang === "bn" ? c.bn : c.en;
    b.textContent = name;
    b.addEventListener("click", () => void send(name));
    container.appendChild(b);
  }
  const section = container.closest<HTMLElement>(".welcome-section");
  if (section) section.hidden = countries.length === 0;
  renderGuide();
}

function formatDate(iso: string): string {
  const [y = 0, m = 1, d = 1] = iso.split("-").map(Number);
  const date = new Date(Date.UTC(y, m - 1, d));
  try {
    return date.toLocaleDateString(lang === "bn" ? "bn-BD" : "en-GB", {
      day: "numeric",
      month: "long",
      year: "numeric",
      timeZone: "UTC",
    });
  } catch {
    return iso;
  }
}

// The welcome card sits at the top of the conversation; it is rebuilt when the language changes.
function renderWelcome(): void {
  const node = welcomeTpl.content.firstElementChild?.cloneNode(true) as HTMLElement | undefined;
  if (!node) return;
  for (const w of node.querySelectorAll<HTMLElement>("[data-w]")) w.textContent = t(w.dataset.w as StrKey);
  const dateEl = node.querySelector("[data-note-date]");
  if (dateEl) dateEl.textContent = guidesUpdated ? t("noteDate", { date: formatDate(guidesUpdated) }) : "";
  const grid = node.querySelector<HTMLElement>("[data-countries]");
  if (grid) renderCountries(grid);
  renderTopics(node.querySelector<HTMLElement>('[data-topics="grid"]'), "card");
  const old = feed.querySelector(".welcome");
  if (old) old.replaceWith(node);
  else feed.prepend(node);
}

const TOKEN_RE = /(\*\*[^*\n]+?\*\*|\*[^*\n]+?\*|https?:\/\/[^\s<>"'`]+)/g;

function formatTime(d: Date): string {
  try {
    return d.toLocaleTimeString(lang === "bn" ? "bn-BD" : "en-GB", {
      hour: "2-digit",
      minute: "2-digit",
      hour12: false,
    });
  } catch {
    return `${String(d.getHours()).padStart(2, "0")}:${String(d.getMinutes()).padStart(2, "0")}`;
  }
}

function safeLink(raw: string): HTMLAnchorElement | null {
  try {
    const url = new URL(raw);
    if (url.protocol !== "https:") return null; // plain http and every other scheme stay as text
    const a = document.createElement("a");
    a.href = url.href;
    a.textContent = raw;
    a.target = "_blank";
    a.rel = "noopener noreferrer nofollow";
    return a;
  } catch {
    return null;
  }
}

// Bot replies use a tiny Markdown subset: **bold**, bare links and line breaks.
function appendInline(parent: HTMLElement, line: string): void {
  let last = 0;
  for (const m of line.matchAll(TOKEN_RE)) {
    const at = m.index ?? 0;
    if (at > last) parent.appendChild(document.createTextNode(line.slice(last, at)));
    const tok = m[0];
    if (tok.startsWith("http")) {
      const trimmed = tok.replace(/[.,;:!?)\]]+$/, "");
      parent.appendChild(safeLink(trimmed) ?? document.createTextNode(trimmed));
      if (trimmed.length < tok.length) parent.appendChild(document.createTextNode(tok.slice(trimmed.length)));
    } else {
      const strong = document.createElement("strong");
      strong.textContent = tok.replace(/^\*{1,2}|\*{1,2}$/g, "");
      parent.appendChild(strong);
    }
    last = at + tok.length;
  }
  if (last < line.length) parent.appendChild(document.createTextNode(line.slice(last)));
}

function renderRich(target: HTMLElement, text: string): void {
  target.replaceChildren();
  for (const line of text.split("\n")) {
    const p = document.createElement("p");
    if (line.trim()) appendInline(p, line);
    else p.className = "gap";
    target.appendChild(p);
  }
}

function scrollToEnd(): void {
  chatEl.scrollTop = chatEl.scrollHeight;
}

function addMessage(
  role: "user" | "bot",
  text: string,
  { error = false } = {},
): { row: HTMLElement; bubble: HTMLElement } {
  const row = document.createElement("div");
  row.className = `msg msg-${role}${error ? " msg-error" : ""}`;
  const body = document.createElement("div");
  body.className = "msg-body";
  const bubble = document.createElement("div");
  bubble.className = "bubble";
  if (role === "bot") renderRich(bubble, text);
  else bubble.textContent = text;
  const meta = document.createElement("div");
  meta.className = "meta";
  const who = document.createElement("span");
  who.textContent = role === "user" ? t("you") : t("bot");
  const now = new Date();
  const time = document.createElement("time");
  time.dateTime = now.toISOString();
  time.textContent = formatTime(now);
  meta.append(who, document.createTextNode("·"), time);
  if (role === "bot" && !error && navigator.clipboard) meta.appendChild(copyButton(bubble));
  body.append(bubble, meta);
  if (role === "bot") row.appendChild(avatar());
  row.appendChild(body);
  feed.appendChild(row);
  scrollToEnd();
  return { row, bubble };
}

function copyButton(bubble: HTMLElement): HTMLButtonElement {
  const b = document.createElement("button");
  b.type = "button";
  b.className = "copy-btn";
  const ic = icon("i-copy");
  const label = document.createElement("span");
  label.textContent = t("copy");
  b.append(ic, label);
  b.addEventListener("click", async () => {
    try {
      // innerText, not textContent: it keeps the line breaks between paragraphs.
      // biome-ignore lint/performance/useDomNodeTextContent: line breaks matter when copying
      await navigator.clipboard.writeText(bubble.innerText);
      label.textContent = t("copied");
      ic.firstElementChild?.setAttribute("href", "#i-check");
      setTimeout(() => {
        label.textContent = t("copy");
        ic.firstElementChild?.setAttribute("href", "#i-copy");
      }, 1800);
    } catch {
      // copying not allowed here; nothing to do
    }
  });
  return b;
}

function showTyping(): HTMLElement {
  const row = document.createElement("div");
  row.className = "msg msg-bot";
  row.setAttribute("role", "status");
  row.setAttribute("aria-label", t("typing"));
  const bubble = document.createElement("div");
  bubble.className = "bubble typing";
  for (let i = 0; i < 3; i++) bubble.appendChild(document.createElement("span"));
  const body = document.createElement("div");
  body.className = "msg-body";
  body.appendChild(bubble);
  row.append(avatar(), body);
  feed.appendChild(row);
  scrollToEnd();
  return row;
}

function setStatus(text: string): void {
  statusEl.textContent = text || "";
}

// ---------- input ----------

function looksPersonal(text: string): boolean {
  return maskPersonal(text).masked;
}

function refreshInput(): void {
  input.style.height = ""; // empty box: CSS height (one line)
  input.style.overflowY = "";
  if (input.value) {
    input.style.height = "auto";
    const want = input.scrollHeight;
    input.style.height = `${Math.max(42, Math.min(want, 160))}px`;
    if (want > 160) input.style.overflowY = "auto";
  }
  const n = charCount(input.value);
  counter.textContent = `${n}/${maxChars}`;
  counter.classList.toggle("near", n > maxChars * 0.9);
  sendBtn.disabled = busy || !cleanText(input.value) || n > maxChars;
}

function setBusy(on: boolean): void {
  busy = on;
  form.setAttribute("aria-busy", on ? "true" : "false");
  for (const b of document.querySelectorAll<HTMLButtonElement>(".country, .topic-card, .topic-row"))
    b.disabled = on;
  newChatBtn.disabled = on;
  forgetBtn.disabled = on;
  refreshInput();
}

input.addEventListener("input", refreshInput);
input.addEventListener("keydown", (e) => {
  // isComposing: don't send while a Bangla keyboard is still building a letter.
  if (e.key === "Enter" && !e.shiftKey && !e.isComposing && e.keyCode !== 229) {
    e.preventDefault();
    form.requestSubmit();
  }
});
form.addEventListener("submit", (e) => {
  e.preventDefault();
  void send(input.value, { fromInput: true });
});

// ---------- server ----------

class HttpError extends Error {
  readonly status: number;
  readonly data: Record<string, unknown> | null;
  constructor(status: number, data: Record<string, unknown> | null) {
    super(String(data?.error ?? status));
    this.status = status;
    this.data = data;
  }
}

async function readJson(res: Response): Promise<Record<string, unknown> | null> {
  try {
    if (!(res.headers.get("content-type") ?? "").includes("application/json")) return null;
    const data = (await res.json()) as unknown;
    return data && typeof data === "object" ? (data as Record<string, unknown>) : null;
  } catch {
    return null;
  }
}

function post(path: string, body: unknown, signal?: AbortSignal): Promise<Response> {
  return fetch(path, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    credentials: "same-origin",
    cache: "no-store",
    body: JSON.stringify(body),
    signal: signal ?? AbortSignal.timeout(REQUEST_TIMEOUT_MS),
  });
}

function validCountry(c: unknown): c is Country {
  const x = c as Country;
  return (
    !!x &&
    typeof x.slug === "string" &&
    typeof x.en === "string" &&
    typeof x.bn === "string" &&
    x.en.length <= 60 &&
    x.bn.length <= 60
  );
}

async function loadConfig(): Promise<void> {
  try {
    const res = await fetch("/api/config", { credentials: "same-origin", cache: "no-store" });
    const data = res.ok ? await readJson(res) : null;
    if (data) {
      const n = Number(data.max_chars);
      if (Number.isInteger(n) && n > 0 && n <= 5000) {
        maxChars = n;
        input.setAttribute("maxlength", String(n));
      }
      if (typeof data.turnstile_site_key === "string" && /^[\w-]{1,100}$/.test(data.turnstile_site_key)) {
        siteKey = data.turnstile_site_key;
      }
      if (typeof data.guides_updated === "string" && /^\d{4}-\d{2}-\d{2}$/.test(data.guides_updated)) {
        guidesUpdated = data.guides_updated;
      }
      if (Array.isArray(data.countries)) {
        countries = data.countries.filter(validCountry).slice(0, 40);
        renderWelcome();
      }
    }
  } catch {
    // the page still works; the first send will report any problem
  }
  refreshInput();
}

function loadTurnstile(): Promise<TurnstileApi> {
  if (window.turnstile) return Promise.resolve(window.turnstile);
  return new Promise((resolve, reject) => {
    const s = document.createElement("script");
    s.src = TURNSTILE_SRC;
    s.async = true;
    s.onload = () => (window.turnstile ? resolve(window.turnstile) : reject(new Error("bot_check")));
    s.onerror = () => reject(new Error("bot_check"));
    document.head.appendChild(s);
  });
}

// A fresh bot-check token (Cloudflare Turnstile). Usually invisible; shows a box only if needed.
async function botCheckToken(): Promise<string> {
  const ts = await loadTurnstile();
  return new Promise((resolve, reject) => {
    turnstileWaiter = { resolve, reject };
    if (turnstileWidget === null) {
      turnstileWidget = ts.render(botCheckEl, {
        sitekey: siteKey,
        appearance: "interaction-only",
        language: "auto",
        callback: (token: string) => {
          turnstileWaiter?.resolve(token);
          turnstileWaiter = null;
        },
        "error-callback": () => {
          turnstileWaiter?.reject(new Error("bot_check"));
          turnstileWaiter = null;
        },
      });
    } else {
      ts.reset(turnstileWidget);
    }
  });
}

function ensureSession(force = false): Promise<void> {
  if (sessionPromise && !force) return sessionPromise;
  sessionPromise = (async () => {
    let token = "";
    if (siteKey) {
      setStatus(t("checking"));
      try {
        token = await botCheckToken();
      } finally {
        setStatus("");
      }
    }
    const res = await post("/api/session", { turnstile_token: token });
    if (!res.ok) throw new HttpError(res.status, await readJson(res));
  })();
  sessionPromise.catch(() => {
    sessionPromise = null;
  });
  return sessionPromise;
}

function errorText(status: number, data: Record<string, unknown> | null): string {
  const code = data?.error;
  if (status === 429) {
    if (data?.scope === "day") return t("dailyLimit");
    if (data?.scope === "ip" || data?.scope === "sessions") return t("ipLimit");
    const s = Math.min(Math.max(Number(data?.retry_after) || 30, 1), 3600);
    return t("rateLimited", { s });
  }
  if (status === 503 || code === "busy") return t("busy");
  if (status === 413 || code === "too_large" || code === "too_long") return t("tooLong", { n: maxChars });
  if (code === "bot_check") return t("botCheck");
  return t("server");
}

function chatBody(text: string) {
  // Only the new message: the server keeps the conversation itself.
  return {
    id: conversationId,
    trigger: "submit-message",
    messages: [{ id: newId(), role: "user", parts: [{ type: "text", text }] }],
  };
}

async function refreshGuide(): Promise<void> {
  try {
    const res = await fetch("/api/me", { credentials: "same-origin", cache: "no-store" });
    const data = res.ok ? await readJson(res) : null;
    if (data && (typeof data.country === "string" || data.country === null)) {
      currentSlug = countries.some((c) => c.slug === data.country) ? (data.country as string) : null;
      renderGuide();
    }
  } catch {
    // the chip just stays as it was
  }
}

async function send(
  raw: string,
  { fromInput = false, silent = false, noNewSession = false } = {},
): Promise<void> {
  const text = cleanText(raw);
  if (!text || busy) return;
  if (charCount(text) > maxChars) {
    setStatus(t("tooLong", { n: maxChars }));
    return;
  }
  if (fromInput && looksPersonal(text) && !window.confirm(t("piiWarn"))) return;
  const now = Date.now();
  if (!silent && now - lastSend < MIN_GAP_MS) return;
  if (!silent) lastSend = now;

  setStatus("");
  setBusy(true);
  if (!silent) addMessage("user", text);
  if (fromInput) {
    input.value = "";
    refreshInput();
  }
  let typing: HTMLElement | null = silent ? null : showTyping();
  let restore = fromInput;
  try {
    // Use the cookie we may already have. Ask for a new session only when the server says there is
    // none, so reloading the page doesn't use up a shared network's session allowance.
    let res = await post("/api/chat", chatBody(text));
    if (res.status === 401 && !noNewSession) {
      await ensureSession(true);
      res = await post("/api/chat", chatBody(text));
    }
    if (!res.ok || !res.body) throw new HttpError(res.status, await readJson(res));
    let bubble: HTMLElement | null = null;
    const reply = await readReply(res.body, (soFar) => {
      if (silent) return;
      if (!bubble) {
        typing?.remove();
        typing = null;
        bubble = addMessage("bot", soFar).bubble;
      } else {
        renderRich(bubble, soFar);
        scrollToEnd();
      }
    });
    restore = false;
    if (!silent && !reply) addMessage("bot", t("busy"), { error: true }); // the server sent nothing back
    void refreshGuide();
  } catch (e) {
    if (!silent) {
      const msg =
        e instanceof HttpError
          ? errorText(e.status, e.data)
          : e instanceof Error && e.message === "bot_check"
            ? t("botCheck")
            : t("network");
      addMessage("bot", msg, { error: true });
    }
  } finally {
    typing?.remove();
    if (restore && !input.value) input.value = text; // keep the question so it can be resent
    setBusy(false);
    if (fromInput) input.focus();
  }
}

// ---------- buttons ----------

newChatBtn.addEventListener("click", async () => {
  if (busy) return;
  closeMenu(false);
  await send("reset", { silent: true, noNewSession: true }); // clears the server-side memory, if any
  conversationId = newId();
  currentSlug = null;
  setStatus("");
  feed.replaceChildren();
  renderWelcome();
  chatEl.scrollTop = 0;
  input.focus();
});

forgetBtn.addEventListener("click", () => {
  if (busy) return;
  if (window.confirm(t("confirmForget"))) void send(t("forgetCommand"));
});

// ---------- start ----------

applyLang();
refreshInput();
void loadConfig();
