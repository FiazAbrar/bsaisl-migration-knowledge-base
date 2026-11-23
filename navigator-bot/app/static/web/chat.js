/* Migration Navigator web chat.
 *
 * Safety rules for this file:
 * - Text from the visitor or the server is only ever placed with textContent or createTextNode.
 *   Never innerHTML, outerHTML, insertAdjacentHTML or document.write.
 * - Links in replies are rebuilt as <a> elements only for https URLs, opened with rel="noopener noreferrer".
 * - Icons are fixed shapes in index.html, referenced by fixed ids from this file; nothing from the server.
 * - No keys live here: the page talks only to its own server (/api/...), which holds the secrets.
 */
(() => {
  "use strict";

  const MIN_GAP_MS = 1500;      // shortest time between two sends from this page
  const REQUEST_TIMEOUT_MS = 60000;
  const TURNSTILE_SRC = "https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit";
  const SVG_NS = "http://www.w3.org/2000/svg";

  // Topic buttons: icon id in index.html, and text keys in STR (topic_<id> label, topicq_<id> question).
  const TOPICS = [
    { id: "cost", icon: "i-cost" },
    { id: "steps", icon: "i-steps" },
    { id: "agency", icon: "i-shield" },
    { id: "scams", icon: "i-alert" },
    { id: "problems", icon: "i-buoy" },
    { id: "loans", icon: "i-wallet" },
  ];

  const STR = {
    en: {
      title: "Migration Navigator",
      tagline: "Safe, legal steps for working abroad",
      newChat: "New chat",
      skip: "Skip to the message box",
      langButton: "বাংলা",
      langLabel: "Switch to Bangla",
      feedLabel: "Conversation",
      inputLabel: "Your question",
      placeholder: "Type your question…",
      send: "Send",
      hint: "Enter to send · Shift+Enter for a new line",
      forget: "Delete my data",
      forgetCommand: "delete my data",
      confirmForget: "Delete this chat's history from our system?",
      you: "You",
      bot: "Navigator",
      typing: "Navigator is writing a reply",
      welcomeTitle: "Going abroad for work? Start here.",
      welcome: "I'm an AI assistant. Ask me about the legal steps, the real costs, the traps to avoid and where to get help. I answer from guides our team researched and sourced. Write in Bangla or English.",
      noteDate: "Guides updated {date}",
      note: "Rules and fees can change, and I can get things wrong. Before you pay or sign anything, check the important steps with BMET or the 16135 helpline.",
      badgeSourced: "Researched, sourced guides",
      chooseCountry: "Choose a country",
      orAsk: "Or ask about",
      topicsTitle: "What I can help with",
      helpTitle: "Need help now?",
      helpFree: "free from Bangladesh",
      helpAbroad: "from abroad",
      helpNote: "Probashi call centre, Wage Earners' Welfare Board",
      helpShort: "Help:",
      helpAbroadShort: "(abroad)",
      menuLabel: "Menu",
      menuOpen: "Open menu",
      menuClose: "Close menu",
      guide: "Guide:",
      callShort: "Help line",
      noCountry: "Choose a country",
      badgeLegal: "Guidance, not legal advice",
      badgeId: "Never share ID or bank numbers",
      themeSystem: "Colours: follow my phone (tap for light)",
      themeLight: "Colours: light (tap for dark)",
      themeDark: "Colours: dark (tap to follow my phone)",
      copy: "Copy",
      copied: "Copied",
      piiWarn: "Your message seems to contain an ID, passport, card or phone number. For your safety, don't share these here. Send it anyway?",
      topic_cost: "Legal cost and real cost",
      topicq_cost: "What is the legal cost of going, and what do people really pay?",
      topic_steps: "Steps to get a work visa",
      topicq_steps: "What are the steps to get a work visa?",
      topic_agency: "Check an agency or dalal",
      topicq_agency: "How do I check if a recruiting agency or dalal is genuine?",
      topic_scams: "Common scams",
      topicq_scams: "What are the common scams, and how do I avoid them?",
      topic_problems: "Trouble abroad or not paid",
      topicq_problems: "What can I do if I'm not paid or in trouble abroad?",
      topic_loans: "Loans and sending money home",
      topicq_loans: "Where can I get a migration loan, and how do I send money home safely?",
      rateLimited: "You're sending messages quickly. Please wait {s} seconds and try again.",
      dailyLimit: "You've reached today's limit for this chat. Please come back tomorrow, or call 16135 for help.",
      ipLimit: "Too many questions are coming from your network today. Please try again tomorrow.",
      busy: "The Navigator is very busy right now. Please try again later, or call 16135 for help.",
      tooLong: "Please keep your question under {n} characters.",
      network: "Couldn't reach the Navigator. Check your internet connection and try again.",
      server: "Something went wrong on our side. Please try again in a moment.",
      botCheck: "We couldn't confirm you're a person. Please reload the page and try again.",
      checking: "Checking your connection…",
    },
    bn: {
      title: "মাইগ্রেশন নেভিগেটর",
      tagline: "বিদেশে কাজের নিরাপদ ও বৈধ পথ",
      newChat: "নতুন চ্যাট",
      skip: "বার্তা লেখার জায়গায় যান",
      langButton: "English",
      langLabel: "ইংরেজিতে দেখুন",
      feedLabel: "কথোপকথন",
      inputLabel: "আপনার প্রশ্ন",
      placeholder: "আপনার প্রশ্ন লিখুন…",
      send: "পাঠান",
      hint: "পাঠাতে Enter · নতুন লাইনে Shift+Enter",
      forget: "আমার তথ্য মুছুন",
      forgetCommand: "আমার তথ্য মুছে দিন",
      confirmForget: "এই চ্যাটের ইতিহাস আমাদের সিস্টেম থেকে মুছে ফেলবেন?",
      you: "আপনি",
      bot: "নেভিগেটর",
      typing: "নেভিগেটর উত্তর লিখছে",
      welcomeTitle: "কাজ নিয়ে বিদেশ যেতে চান? এখান থেকে শুরু করুন।",
      welcome: "আমি একটি এআই সহকারী। বৈধ ধাপ, আসল খরচ, কোন ফাঁদ এড়াতে হবে আর কোথায় সাহায্য পাবেন, জিজ্ঞেস করুন। আমাদের দলের গবেষণা করা, উৎসসহ গাইড থেকে উত্তর দিই। বাংলা বা ইংরেজিতে লিখুন।",
      noteDate: "গাইড হালনাগাদ {date}",
      note: "নিয়ম ও খরচ বদলাতে পারে, আর আমারও ভুল হতে পারে। টাকা দেওয়া বা কিছুতে সই করার আগে গুরুত্বপূর্ণ ধাপগুলো বিএমইটি বা 16135 হেল্পলাইনে যাচাই করে নিন।",
      badgeSourced: "গবেষণাভিত্তিক, উৎসসহ গাইড",
      chooseCountry: "একটি দেশ বেছে নিন",
      orAsk: "অথবা জিজ্ঞেস করুন",
      topicsTitle: "আমি যেসব বিষয়ে সাহায্য করতে পারি",
      helpTitle: "এখনই সাহায্য দরকার?",
      helpFree: "বাংলাদেশ থেকে বিনামূল্যে",
      helpAbroad: "বিদেশ থেকে",
      helpNote: "প্রবাসী কল সেন্টার, ওয়েজ আর্নার্স কল্যাণ বোর্ড",
      helpShort: "সাহায্য:",
      helpAbroadShort: "(বিদেশ থেকে)",
      menuLabel: "মেনু",
      menuOpen: "মেনু খুলুন",
      menuClose: "মেনু বন্ধ করুন",
      guide: "গাইড:",
      callShort: "হেল্পলাইন",
      noCountry: "দেশ বেছে নিন",
      badgeLegal: "নির্দেশনা, আইনি পরামর্শ নয়",
      badgeId: "আইডি বা ব্যাংক নম্বর দেবেন না",
      themeSystem: "রং: ফোনের সেটিং অনুযায়ী (লাইটের জন্য চাপুন)",
      themeLight: "রং: লাইট (ডার্কের জন্য চাপুন)",
      themeDark: "রং: ডার্ক (ফোনের সেটিংয়ে ফিরতে চাপুন)",
      copy: "কপি",
      copied: "কপি হয়েছে",
      piiWarn: "আপনার বার্তায় এনআইডি, পাসপোর্ট, কার্ড বা ফোন নম্বরের মতো কিছু আছে। নিরাপত্তার জন্য এখানে এগুলো দেবেন না। তবুও পাঠাবেন?",
      topic_cost: "আইনি খরচ ও আসল খরচ",
      topicq_cost: "যেতে আইনত কত খরচ, আর মানুষ আসলে কত দেয়?",
      topic_steps: "কাজের ভিসা পাওয়ার ধাপ",
      topicq_steps: "কাজের ভিসা পাওয়ার ধাপগুলো কী?",
      topic_agency: "এজেন্সি বা দালাল যাচাই",
      topicq_agency: "রিক্রুটিং এজেন্সি বা দালাল আসল কি না কীভাবে যাচাই করব?",
      topic_scams: "সাধারণ প্রতারণা",
      topicq_scams: "সাধারণ প্রতারণাগুলো কী, আর কীভাবে এড়াব?",
      topic_problems: "বিদেশে বিপদ বা বেতন না পেলে",
      topicq_problems: "বেতন না পেলে বা বিদেশে বিপদে পড়লে কী করতে পারি?",
      topic_loans: "ঋণ ও দেশে টাকা পাঠানো",
      topicq_loans: "বিদেশ যাওয়ার ঋণ কোথায় পাব, আর নিরাপদে দেশে টাকা কীভাবে পাঠাব?",
      rateLimited: "আপনি খুব দ্রুত বার্তা পাঠাচ্ছেন। {s} সেকেন্ড পর আবার চেষ্টা করুন।",
      dailyLimit: "এই চ্যাটে আজকের সীমা শেষ। আগামীকাল আবার আসুন, অথবা সাহায্যের জন্য 16135 নম্বরে কল করুন।",
      ipLimit: "আজ আপনার নেটওয়ার্ক থেকে অনেক বেশি প্রশ্ন এসেছে। আগামীকাল আবার চেষ্টা করুন।",
      busy: "নেভিগেটর এখন খুব ব্যস্ত। একটু পরে আবার চেষ্টা করুন, অথবা সাহায্যের জন্য 16135 নম্বরে কল করুন।",
      tooLong: "প্রশ্নটি {n} অক্ষরের মধ্যে রাখুন।",
      network: "নেভিগেটরের সাথে সংযোগ হয়নি। ইন্টারনেট সংযোগ দেখে আবার চেষ্টা করুন।",
      server: "আমাদের দিকে একটি সমস্যা হয়েছে। একটু পরে আবার চেষ্টা করুন।",
      botCheck: "আপনি মানুষ কি না নিশ্চিত করা যায়নি। পেজটি রিলোড করে আবার চেষ্টা করুন।",
      checking: "সংযোগ যাচাই করা হচ্ছে…",
    },
  };

  const $ = (id) => document.getElementById(id);
  const chatEl = $("chat");
  const feed = $("feed");
  const form = $("composer");
  const input = $("composer-input");
  const sendBtn = $("send");
  const counter = $("counter");
  const statusEl = $("status");
  const langBtn = $("lang-toggle");
  const langLabel = $("lang-label");
  const themeBtn = $("theme-toggle");
  const sidebar = $("sidebar");
  const scrim = $("scrim");
  const menuBtn = $("menu-btn");
  const menuCloseBtn = $("menu-close");
  const guideChip = $("guide-chip");
  const guideLabel = $("guide-label");
  const themeIcon = $("theme-icon");
  const newChatBtn = $("new-chat");
  const forgetBtn = $("forget");
  const botCheckEl = $("bot-check");
  const welcomeTpl = $("tpl-welcome");
  const sideTopics = document.querySelector('[data-topics="list"]');

  let lang = loadLang();
  let maxChars = Number(input.getAttribute("maxlength")) || 500;
  let siteKey = "";
  let countries = [];          // [{slug, en, bn}] from /api/config
  let currentSlug = null;      // the guide the server is answering from, as it last told us
  let guidesUpdated = "";      // YYYY-MM-DD from /api/config
  let busy = false;
  let lastSend = 0;
  let sessionPromise = null;
  let turnstileWidget = null;
  let turnstileWaiter = null;

  // ---------- language ----------

  function loadLang() {
    try {
      const saved = localStorage.getItem("navigator.lang");
      if (saved === "en" || saved === "bn") return saved;
    } catch (e) { /* storage blocked: fall back to Bangla */ }
    return "bn";
  }

  function t(key, vars) {
    let s = (STR[lang] && STR[lang][key]) || STR.en[key] || "";
    if (vars) for (const [k, v] of Object.entries(vars)) s = s.split(`{${k}}`).join(String(v));
    return s;
  }

  function applyLang() {
    document.documentElement.lang = lang;
    document.title = t("title");
    document.querySelectorAll("[data-i18n]").forEach((el) => { el.textContent = t(el.dataset.i18n); });
    document.querySelectorAll("[data-i18n-label]").forEach((el) => { el.setAttribute("aria-label", t(el.dataset.i18nLabel)); });
    document.querySelectorAll("[data-i18n-placeholder]").forEach((el) => { el.setAttribute("placeholder", t(el.dataset.i18nPlaceholder)); });
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
    try { localStorage.setItem("navigator.lang", lang); } catch (e) { /* ignore */ }
    applyLang();
  });

  // ---------- colour theme: follow the phone, light or dark ----------

  const THEMES = ["system", "light", "dark"];
  const THEME_ICON = { system: "i-auto", light: "i-sun", dark: "i-moon" };
  const THEME_LABEL = { system: "themeSystem", light: "themeLight", dark: "themeDark" };

  function currentTheme() {
    const t = document.documentElement.getAttribute("data-theme");
    return t === "light" || t === "dark" ? t : "system";
  }

  function showTheme() {
    const theme = currentTheme();
    themeIcon.setAttribute("href", `#${THEME_ICON[theme]}`);
    themeBtn.setAttribute("aria-label", t(THEME_LABEL[theme]));
    themeBtn.setAttribute("title", t(THEME_LABEL[theme]));
  }

  themeBtn.addEventListener("click", () => {
    const next = THEMES[(THEMES.indexOf(currentTheme()) + 1) % THEMES.length];
    if (next === "system") document.documentElement.removeAttribute("data-theme");
    else document.documentElement.setAttribute("data-theme", next);
    try {
      if (next === "system") localStorage.removeItem("navigator.theme");
      else localStorage.setItem("navigator.theme", next);
    } catch (e) { /* not saved; still applies to this visit */ }
    showTheme();
  });

  // ---------- menu (phones): the sidebar slides in ----------

  const narrow = window.matchMedia("(max-width: 1023px)");

  function openMenu() {
    sidebar.classList.add("open");
    scrim.hidden = false;
    menuBtn.setAttribute("aria-expanded", "true");
    menuCloseBtn.focus();
  }

  function closeMenu(returnFocus = true) {
    if (!sidebar.classList.contains("open")) return;
    sidebar.classList.remove("open");
    scrim.hidden = true;
    menuBtn.setAttribute("aria-expanded", "false");
    if (returnFocus) menuBtn.focus();
  }

  menuBtn.addEventListener("click", openMenu);
  menuCloseBtn.addEventListener("click", () => closeMenu());
  scrim.addEventListener("click", () => closeMenu());
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeMenu(); });
  narrow.addEventListener("change", () => closeMenu(false));

  // ---------- the guide in use ----------

  function countryName(slug) {
    const c = countries.find((x) => x.slug === slug);
    return c ? (lang === "bn" ? c.bn : c.en) : "";
  }

  function renderGuide() {
    const name = countryName(currentSlug);
    guideLabel.textContent = name || t("noCountry");
    guideChip.classList.toggle("empty", !name);
    document.querySelectorAll(".country").forEach((b) => {
      const on = b.dataset.slug === currentSlug;
      b.classList.toggle("active", on);
      b.setAttribute("aria-pressed", on ? "true" : "false");
    });
  }

  guideChip.addEventListener("click", () => {
    const section = feed.querySelector('[data-section="countries"]');
    if (!section) return;
    section.scrollIntoView({ block: "center" });
    const first = section.querySelector(".country.active") || section.querySelector(".country");
    if (first) first.focus({ preventScroll: true });
  });

  // ---------- building blocks (text only, never HTML) ----------

  function icon(id) {
    const svg = document.createElementNS(SVG_NS, "svg");
    svg.setAttribute("aria-hidden", "true");
    svg.setAttribute("focusable", "false");
    const use = document.createElementNS(SVG_NS, "use");
    use.setAttribute("href", `#${id}`);
    svg.appendChild(use);
    return svg;
  }

  function avatar() {
    const a = document.createElement("span");
    a.className = "avatar";
    a.setAttribute("aria-hidden", "true");
    a.appendChild(icon("i-compass"));
    return a;
  }

  function renderTopics(container, kind) {
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
      label.textContent = t(`topic_${topic.id}`);
      b.append(ic, label);
      b.addEventListener("click", () => { closeMenu(false); send(t(`topicq_${topic.id}`)); });
      container.appendChild(b);
    }
  }

  function renderCountries(container) {
    container.replaceChildren();
    for (const c of countries) {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "country";
      b.dataset.slug = c.slug;
      b.disabled = busy;
      const name = lang === "bn" ? c.bn : c.en;
      b.textContent = name;
      b.addEventListener("click", () => send(name));
      container.appendChild(b);
    }
    container.closest(".welcome-section").hidden = countries.length === 0;
    renderGuide();
  }

  function formatDate(iso) {
    const [y, m, d] = iso.split("-").map(Number);
    const date = new Date(Date.UTC(y, m - 1, d));
    try {
      return date.toLocaleDateString(lang === "bn" ? "bn-BD" : "en-GB",
        { day: "numeric", month: "long", year: "numeric", timeZone: "UTC" });
    } catch (e) {
      return iso;
    }
  }

  // The welcome card sits at the top of the conversation; it is rebuilt when the language changes.
  function renderWelcome() {
    const node = welcomeTpl.content.firstElementChild.cloneNode(true);
    node.querySelectorAll("[data-w]").forEach((el) => { el.textContent = t(el.dataset.w); });
    const dateEl = node.querySelector("[data-note-date]");
    dateEl.textContent = guidesUpdated ? t("noteDate", { date: formatDate(guidesUpdated) }) : "";
    renderCountries(node.querySelector("[data-countries]"));
    renderTopics(node.querySelector('[data-topics="grid"]'), "card");
    const old = feed.querySelector(".welcome");
    if (old) old.replaceWith(node);
    else feed.prepend(node);
  }

  const TOKEN_RE = /(\*\*[^*\n]+?\*\*|\*[^*\n]+?\*|https?:\/\/[^\s<>"'`]+)/g;

  function formatTime(d) {
    try {
      return d.toLocaleTimeString(lang === "bn" ? "bn-BD" : "en-GB", { hour: "2-digit", minute: "2-digit", hour12: false });
    } catch (e) {
      return `${String(d.getHours()).padStart(2, "0")}:${String(d.getMinutes()).padStart(2, "0")}`;
    }
  }

  function safeLink(raw) {
    try {
      const url = new URL(raw);
      if (url.protocol !== "https:") return null;  // plain http and every other scheme stay as text
      const a = document.createElement("a");
      a.href = url.href;
      a.textContent = raw;
      a.target = "_blank";
      a.rel = "noopener noreferrer nofollow";
      return a;
    } catch (e) {
      return null;
    }
  }

  // Bot replies use a tiny Markdown subset: *bold*, **bold**, bare links and line breaks.
  function appendInline(parent, line) {
    let last = 0;
    for (const m of line.matchAll(TOKEN_RE)) {
      if (m.index > last) parent.appendChild(document.createTextNode(line.slice(last, m.index)));
      const tok = m[0];
      if (tok.startsWith("http")) {
        const trimmed = tok.replace(/[.,;:!?)\]]+$/, "");
        const link = safeLink(trimmed);
        parent.appendChild(link || document.createTextNode(trimmed));
        if (trimmed.length < tok.length) parent.appendChild(document.createTextNode(tok.slice(trimmed.length)));
      } else {
        const strong = document.createElement("strong");
        strong.textContent = tok.replace(/^\*{1,2}|\*{1,2}$/g, "");
        parent.appendChild(strong);
      }
      last = m.index + tok.length;
    }
    if (last < line.length) parent.appendChild(document.createTextNode(line.slice(last)));
  }

  function renderRich(el, text) {
    for (const line of String(text).split("\n")) {
      const p = document.createElement("p");
      if (line.trim()) appendInline(p, line);
      else p.className = "gap";
      el.appendChild(p);
    }
  }

  function scrollToEnd() {
    chatEl.scrollTop = chatEl.scrollHeight;
  }

  function addMessage(role, text, { error = false } = {}) {
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
    return row;
  }

  function copyButton(bubble) {
    const b = document.createElement("button");
    b.type = "button";
    b.className = "copy-btn";
    const ic = icon("i-copy");
    const label = document.createElement("span");
    label.textContent = t("copy");
    b.append(ic, label);
    b.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(bubble.innerText);
        label.textContent = t("copied");
        ic.firstChild.setAttribute("href", "#i-check");
        setTimeout(() => { label.textContent = t("copy"); ic.firstChild.setAttribute("href", "#i-copy"); }, 1800);
      } catch (e) { /* copying not allowed here; nothing to do */ }
    });
    return b;
  }

  function showTyping() {
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

  function setStatus(text) {
    statusEl.textContent = text || "";
  }

  // ---------- input ----------

  function cleanText(s) {
    return String(s).replace(/\r\n?/g, "\n").replace(/[\u0000-\u0008\u000B-\u001F\u007F]/g, "").trim();
  }

  // Numbers that look like an NID, passport, bank card or phone number. Checked before a typed message
  // is sent, so people are warned before personal details leave their phone (the server never asks for them).
  const BN_DIGITS = "০১২৩৪৫৬৭৮৯";
  const PII_PATTERNS = [
    /(?:\+?880|\b0)1[3-9]\d{8}\b/,       // Bangladeshi mobile number
    /\b(?:\d{10}|\d{13}|\d{17})\b/,       // NID (10, 13 or 17 digits)
    /\b[A-Z]{1,2}\d{7,8}\b/i,             // passport number
    /\b(?:\d[ -]?){13,19}\b/,             // bank card number
  ];

  function looksPersonal(text) {
    const ascii = text.replace(/[০-৯]/g, (d) => String(BN_DIGITS.indexOf(d)));
    return PII_PATTERNS.some((re) => re.test(ascii));
  }

  function charCount(s) {
    return Array.from(s).length;
  }

  function refreshInput() {
    input.style.height = "";  // empty box: CSS height (one line)
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

  function setBusy(on) {
    busy = on;
    form.setAttribute("aria-busy", on ? "true" : "false");
    document.querySelectorAll(".country, .topic-card, .topic-row").forEach((b) => { b.disabled = on; });
    newChatBtn.disabled = on;
    forgetBtn.disabled = on;
    refreshInput();
  }

  input.addEventListener("input", refreshInput);
  input.addEventListener("keydown", (e) => {
    // isComposing: don't send while a Bangla keyboard is still building a letter.
    if (e.key === "Enter" && !e.shiftKey && !e.isComposing && e.keyCode !== 229) {
      e.preventDefault();
      form.requestSubmit ? form.requestSubmit() : form.dispatchEvent(new Event("submit", { cancelable: true }));
    }
  });
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    send(input.value, { fromInput: true });
  });

  // ---------- server ----------

  async function readJson(res) {
    try {
      if (!(res.headers.get("content-type") || "").includes("application/json")) return null;
      return await res.json();
    } catch (e) {
      return null;
    }
  }

  async function post(path, body) {
    const ctrl = new AbortController();
    const timer = setTimeout(() => ctrl.abort(), REQUEST_TIMEOUT_MS);
    try {
      return await fetch(path, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "same-origin",
        cache: "no-store",
        body: JSON.stringify(body),
        signal: ctrl.signal,
      });
    } finally {
      clearTimeout(timer);
    }
  }

  function validCountry(c) {
    return c && typeof c.slug === "string" && typeof c.en === "string" && typeof c.bn === "string"
      && c.en.length <= 60 && c.bn.length <= 60;
  }

  async function loadConfig() {
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
    } catch (e) { /* the page still works; the first send will report any problem */ }
    refreshInput();
  }

  function loadTurnstile() {
    if (window.turnstile) return Promise.resolve(window.turnstile);
    return new Promise((resolve, reject) => {
      const s = document.createElement("script");
      s.src = TURNSTILE_SRC;
      s.async = true;
      s.onload = () => (window.turnstile ? resolve(window.turnstile) : reject(new Error("turnstile")));
      s.onerror = () => reject(new Error("turnstile"));
      document.head.appendChild(s);
    });
  }

  // A fresh bot-check token (Cloudflare Turnstile). Usually invisible; shows a box only if needed.
  async function botCheckToken() {
    const ts = await loadTurnstile();
    return new Promise((resolve, reject) => {
      turnstileWaiter = { resolve, reject };
      if (turnstileWidget === null) {
        turnstileWidget = ts.render(botCheckEl, {
          sitekey: siteKey,
          appearance: "interaction-only",
          language: "auto",
          callback: (token) => { if (turnstileWaiter) turnstileWaiter.resolve(token); turnstileWaiter = null; },
          "error-callback": () => { if (turnstileWaiter) turnstileWaiter.reject(new Error("bot_check")); turnstileWaiter = null; },
        });
      } else {
        ts.reset(turnstileWidget);
      }
    });
  }

  function ensureSession(force = false) {
    if (sessionPromise && !force) return sessionPromise;
    sessionPromise = (async () => {
      let token = "";
      if (siteKey) {
        setStatus(t("checking"));
        try { token = await botCheckToken(); } finally { setStatus(""); }
      }
      const res = await post("/api/session", { turnstile_token: token });
      if (!res.ok) {
        const data = await readJson(res);
        const err = new Error((data && data.error) || "session");
        err.status = res.status;
        err.data = data;
        throw err;
      }
    })();
    sessionPromise.catch(() => { sessionPromise = null; });
    return sessionPromise;
  }

  function errorText(status, data) {
    const code = data && data.error;
    if (status === 429) {
      if (data && data.scope === "day") return t("dailyLimit");
      if (data && (data.scope === "ip" || data.scope === "sessions")) return t("ipLimit");
      const s = Math.min(Math.max(Number(data && data.retry_after) || 30, 1), 3600);
      return t("rateLimited", { s });
    }
    if (status === 503 || code === "busy") return t("busy");
    if (code === "too_long") return t("tooLong", { n: maxChars });
    if (code === "bot_check") return t("botCheck");
    return t("server");
  }

  async function send(raw, { fromInput = false, silent = false, noNewSession = false } = {}) {
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
    const typing = silent ? null : showTyping();
    let restore = fromInput;
    try {
      // Use the cookie we may already have. Ask for a new session only when the server says there is
      // none, so reloading the page doesn't use up a shared network's session allowance.
      let res = await post("/api/chat", { message: text });
      if (res.status === 401 && !noNewSession) {
        await ensureSession(true);
        res = await post("/api/chat", { message: text });
      }
      const data = await readJson(res);
      if (res.ok && data && typeof data.reply === "string") {
        restore = false;
        if (typeof data.country === "string" || data.country === null) {
          currentSlug = countries.some((c) => c.slug === data.country) ? data.country : null;
          renderGuide();
        }
        if (!silent) addMessage("bot", data.reply);
      } else if (!silent) {
        addMessage("bot", errorText(res.status, data), { error: true });
      }
    } catch (e) {
      if (!silent) {
        const msg = e && e.status ? errorText(e.status, e.data) : (e && e.message === "bot_check" ? t("botCheck") : t("network"));
        addMessage("bot", msg, { error: true });
      }
    } finally {
      if (typing) typing.remove();
      if (restore && !input.value) input.value = text;  // keep the question so it can be resent
      setBusy(false);
      if (fromInput) input.focus();
    }
  }

  // ---------- buttons ----------

  newChatBtn.addEventListener("click", async () => {
    if (busy) return;
    closeMenu(false);
    await send("reset", { silent: true, noNewSession: true });  // clears the server-side memory, if any
    currentSlug = null;
    setStatus("");
    feed.replaceChildren();
    renderWelcome();
    chatEl.scrollTop = 0;
    input.focus();
  });

  forgetBtn.addEventListener("click", () => {
    if (busy) return;
    if (window.confirm(t("confirmForget"))) send(t("forgetCommand"));
  });

  // ---------- start ----------

  applyLang();
  refreshInput();
  loadConfig();
})();
