/**
 * One message in, at most one reply out, the same way for every channel:
 *   not text → "send text" · empty → "send text" · command (reset, delete, /start) → done
 *   → too long → abuse limits → personal numbers removed → remember → guide → answer → remember.
 * A refused message gets a reply only the first time in a window (Decision.notify), so a flood gets
 * silence. Channels turn the reply's *bold* into their own format.
 */
import { type Guard, MAX_CHARS } from "../guard/guard.ts";
import type { KnowledgeBase } from "../kb/index.ts";
import type { Channel, MemoryStore } from "../memory/store.ts";
import { describeError, logger } from "../ops/logger.ts";
import { type Answerer, countryList, guideName } from "./answerer.ts";
import { isGreeting, parseCommand } from "./commands.ts";
import { buildContext } from "./context.ts";
import { bilingual, detectLang, type Lang, MESSAGES } from "./i18n.ts";
import { charCount, cleanText, maskPersonal } from "./safeguards.ts";

export interface IncomingMessage {
  channel: Channel;
  /** The person, already hashed (memory/store.ts userKey). */
  userKey: string;
  /** Web only: the visitor's IP address, hashed. */
  ipKey?: string;
  /** "other" for voice notes, photos, stickers and anything else that isn't text. */
  kind: "text" | "other";
  text?: string;
}

export interface Reply {
  text: string;
  lang: Lang;
  /** The guide this conversation is about, for the web page's guide chip. */
  country?: string;
}

export interface ConversationDeps {
  kb: () => KnowledgeBase;
  store: MemoryStore;
  guard: Guard;
  answerer: Answerer;
  contextTokenBudget: number;
  /** Link to the privacy notice, shown in the first reply. */
  privacyLink?: string;
  /** Runs work after the reply is sent (profile and summary updates). */
  defer?: (task: Promise<unknown>) => void;
  /** Called after each answered message (the AI layer updates the profile and summary here). */
  afterAnswer?: (info: { userKey: string; lang: Lang; channel: Channel }) => Promise<void>;
}

export class Conversation {
  private readonly deps: ConversationDeps;

  constructor(deps: ConversationDeps) {
    this.deps = deps;
  }

  async handle(msg: IncomingMessage): Promise<Reply | null> {
    if (msg.kind !== "text") return { text: bilingual((m) => m.sendText), lang: "bn" };
    const text = cleanText(msg.text ?? "");
    if (!text) return { text: bilingual((m) => m.sendText), lang: "bn" };
    const lang = detectLang(text);
    const m = MESSAGES[lang];
    const { store, guard } = this.deps;

    const command = parseCommand(text);
    if (command) {
      const decision = await guard.command(msg.channel, msg.userKey);
      if (!decision.ok)
        return decision.notify ? { text: m.refusal[decision.reason ?? "minute"], lang } : null;
      if (command === "delete") {
        await store.forget(msg.userKey);
        return { text: m.deleted, lang };
      }
      if (command === "reset") {
        await store.forget(msg.userKey);
        return { text: m.reset, lang };
      }
      const { isNew } = await store.touch(msg.userKey);
      return { text: this.welcome(lang, isNew), lang };
    }

    if (charCount(text) > MAX_CHARS) return { text: m.tooLong, lang };

    const decision = await guard.check(msg.channel, msg.userKey, msg.ipKey);
    if (!decision.ok) return decision.notify ? { text: m.refusal[decision.reason ?? "minute"], lang } : null;

    const { text: safeText, masked } = maskPersonal(text);
    const { user, isNew } = await store.touch(msg.userKey);
    const kb = this.deps.kb();

    if (isGreeting(safeText)) {
      await store.addTurn(msg.userKey, "user", safeText);
      const current = user.country && kb.guide(user.country) ? user.country : undefined;
      const reply = current
        ? MESSAGES[lang].welcomeBack(guideName(kb, current, lang))
        : this.welcome(lang, isNew);
      await store.addTurn(msg.userKey, "bot", reply);
      return { text: reply, lang };
    }

    // The guide: one named in this message, else the one chosen earlier (if it still exists).
    let country = kb.countries.detect(safeText);
    if (country && country !== user.country) await store.setCountry(msg.userKey, country);
    if (!country && user.country && kb.guide(user.country)) country = user.country;

    const context = await buildContext(store, user, this.deps.contextTokenBudget);
    await store.addTurn(msg.userKey, "user", safeText);
    let answerText: string;
    try {
      const answer = await this.deps.answerer.answer({
        channel: msg.channel,
        userKey: msg.userKey,
        text: safeText,
        lang,
        country,
        kb,
        context,
      });
      answerText = answer.text;
      if (answer.costUsd) await guard.addCost(msg.channel, answer.costUsd);
    } catch (err) {
      logger.error({ err: describeError(err), channel: msg.channel }, "Answering failed");
      return { text: m.error, lang, ...(country ? { country } : {}) };
    }

    const parts = [
      masked ? m.personalRemoved : "",
      answerText,
      isNew ? m.privacy(this.deps.privacyLink) : "",
    ];
    const reply = parts.filter(Boolean).join("\n\n");
    await store.addTurn(msg.userKey, "bot", answerText);
    if (this.deps.afterAnswer) {
      const task = this.deps
        .afterAnswer({ userKey: msg.userKey, lang, channel: msg.channel })
        .catch((err) => logger.warn({ err: describeError(err) }, "Updating the profile or summary failed"));
      if (this.deps.defer) this.deps.defer(task);
    }
    return { text: reply, lang, ...(country ? { country } : {}) };
  }

  /** The welcome (Telegram /start, or a first "hi"), with the privacy notice for a new person. */
  private welcome(lang: Lang, isNew: boolean): string {
    const m = MESSAGES[lang];
    const welcome = m.welcome(countryList(this.deps.kb(), lang));
    return isNew ? `${welcome}\n\n${m.privacy(this.deps.privacyLink)}` : welcome;
  }
}
