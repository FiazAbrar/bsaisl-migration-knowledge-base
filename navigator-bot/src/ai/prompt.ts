/**
 * The system prompt: prompts/system.md (written and tested with the knowledge-base team) with its four
 * placeholders filled, then what the bot remembers about this person. The fixed part comes first so
 * providers that cache prompts can reuse it.
 */
import { readFileSync } from "node:fs";
import path from "node:path";
import { BOT_ROOT } from "../config.ts";
import type { ConversationContext } from "../conversation/context.ts";
import { profileCard } from "../conversation/context.ts";
import type { KnowledgeBase } from "../kb/index.ts";

let template: string | undefined;

export function promptTemplate(): string {
  template ??= readFileSync(path.join(BOT_ROOT, "prompts", "system.md"), "utf-8");
  return template;
}

const title = (t: string) => (t.split(":")[0] ?? t).trim();

export function systemPrompt(
  kb: KnowledgeBase,
  ctx: { context: ConversationContext; country: string | undefined; channel: string },
  today = new Date(),
): string {
  const countries = kb
    .listGuides("country")
    .map((g) => `${title(g.title)} (${g.slug})`)
    .join(", ");
  const shared = kb
    .listGuides("shared")
    .map((g) => `${title(g.title)} (${g.slug})`)
    .join(", ");
  const filled = promptTemplate()
    .replaceAll("{{TODAY}}", today.toISOString().slice(0, 10))
    .replaceAll("{{COUNTRIES}}", countries)
    .replaceAll("{{SHARED_GUIDES}}", shared)
    .replaceAll("{{KB_BUILT_AT}}", kb.meta.guidesUpdated);

  const memory: string[] = [];
  memory.push(`Channel: ${ctx.channel}.`);
  if (ctx.country) memory.push(`Guide chosen in this conversation: ${ctx.country}.`);
  const card = profileCard(ctx.context.profile);
  if (card)
    memory.push(`What you know about this person from earlier messages (may be out of date):\n${card}`);
  if (ctx.context.summary) memory.push(`Summary of the earlier conversation:\n${ctx.context.summary}`);
  return `${filled}\n\n## This conversation\n\n${memory.join("\n\n")}`;
}
