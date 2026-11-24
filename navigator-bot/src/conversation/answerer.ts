/**
 * How a question becomes an answer. Two implementations:
 * - TestModeAnswerer (no AI key): lists the closest sections of the chosen guide, as before.
 * - AiAnswerer (src/ai/answerer.ts): searches and reads the guides with the AI model.
 */
import type { KnowledgeBase } from "../kb/index.ts";
import type { Channel } from "../memory/store.ts";
import type { ConversationContext } from "./context.ts";
import { type Lang, MESSAGES } from "./i18n.ts";

export interface AnswerInput {
  channel: Channel;
  userKey: string;
  /** The message, personal numbers already removed. */
  text: string;
  lang: Lang;
  /** The guide id chosen for this conversation, if any. */
  country: string | undefined;
  kb: KnowledgeBase;
  context: ConversationContext;
}

export interface Answer {
  text: string;
  /** What the AI call cost, for the daily budget. */
  costUsd?: number;
}

export interface Answerer {
  readonly mode: "test" | "ai";
  answer(input: AnswerInput): Promise<Answer>;
}

/** Destination guide names for a message, in the person's language. */
export function countryList(kb: KnowledgeBase, lang: Lang): string {
  return kb.countries
    .buttons()
    .map((b) => (lang === "bn" ? b.bn : b.en))
    .join(lang === "bn" ? ", " : ", ");
}

export function guideName(kb: KnowledgeBase, slug: string, lang: Lang): string {
  const button = kb.countries.buttons().find((b) => b.slug === slug);
  if (button) return lang === "bn" ? button.bn : button.en;
  const title = kb.guide(slug)?.title ?? slug;
  return (title.split(":")[0] ?? title).trim();
}

export class TestModeAnswerer implements Answerer {
  readonly mode = "test" as const;

  async answer({ text, lang, country, kb }: AnswerInput): Promise<Answer> {
    const m = MESSAGES[lang];
    if (!country) return { text: m.whichCountry(countryList(kb, lang)) };
    const guide = guideName(kb, country, lang);
    const query = kb.countries.strip(text);
    if (!query) return { text: `${m.testMode}\n${m.guideChosen(guide)}` };
    const hits = kb.search(query, country, 3);
    if (hits.length === 0) return { text: `${m.testMode}\n${m.noMatch(guide)}` };
    const lines = [m.testMode, m.closest(guide)];
    hits.forEach((h, i) => {
      lines.push(`${i + 1}. **${h.path}**\n   ${h.snippet.trim()}`);
    });
    return { text: lines.join("\n") };
  }
}
