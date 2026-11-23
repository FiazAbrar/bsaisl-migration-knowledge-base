/**
 * Long-term memory, written after the reply is sent (it never delays an answer):
 * - the profile card: a few facts about the person's situation, updated from the latest exchange;
 * - the summary: when older messages no longer fit the context budget, a small model folds them into
 *   a short running summary, so nothing important is forgotten.
 * Both use a small, cheap model (LLM_SMALL_MODEL) and never store ID numbers (they are removed earlier).
 */
import { generateText, type LanguageModel, Output } from "ai";
import { z } from "zod";
import { buildContext } from "../conversation/context.ts";
import type { Lang } from "../conversation/i18n.ts";
import type { Guard } from "../guard/guard.ts";
import type { Channel, MemoryStore } from "../memory/store.ts";
import { costOf } from "./answerer.ts";

/** The assessment layer's first version: what helps the bot help this person next time. */
export const profileSchema = z.object({
  destination: z.string().max(60).optional().describe("Country they want to go to or are in"),
  job: z.string().max(80).optional().describe("Job or visa type they mention"),
  stage: z
    .enum([
      "thinking",
      "talking to an agency or dalal",
      "papers in progress",
      "visa received",
      "abroad",
      "back home",
    ])
    .optional(),
  moneyPaid: z.string().max(80).optional().describe("Amount paid so far and to whom, as they said it"),
  agency: z.string().max(80).optional().describe("Agency or dalal they named"),
  sex: z.enum(["woman", "man"]).optional(),
  worries: z.array(z.string().max(80)).max(4).optional().describe("Open problems or fears they mentioned"),
  language: z.enum(["bn", "en", "banglish"]).optional(),
});
export type Profile = z.infer<typeof profileSchema>;

const PROFILE_INSTRUCTIONS =
  "You keep a short profile of a person asking a migration help bot, so the bot can help them next time. " +
  "Update the profile from the latest exchange. Keep what is still true, change what they corrected, and " +
  "add only what they said about themselves. Never guess. Never record names, phone, NID, passport or bank " +
  "numbers. Leave a field out when unknown.";

const SUMMARY_INSTRUCTIONS =
  "Fold the older messages into the running summary of a conversation between a person and a migration " +
  "help bot. Keep the person's situation, what they asked, what the bot told them (facts, steps, warnings) " +
  "and anything left open. At most 120 words. Plain English. No names, phone, NID, passport or bank numbers.";

export interface MemoryUpdaterOptions {
  model: LanguageModel;
  store: MemoryStore;
  guard: Guard;
  contextTokenBudget: number;
  timeoutMs: number;
  providerOptions?: Record<string, Record<string, unknown>>;
}

export function createMemoryUpdater(opts: MemoryUpdaterOptions) {
  const common = {
    model: opts.model,
    maxRetries: 1,
    ...(opts.providerOptions ? { providerOptions: opts.providerOptions as never } : {}),
  };

  return async function afterAnswer({ userKey, channel }: { userKey: string; lang: Lang; channel: Channel }) {
    const user = await opts.store.get(userKey);
    if (!user) return; // deleted meanwhile
    const latest = await opts.store.recentTurns(userKey, 2);
    if (latest.length > 0) {
      const result = await generateText({
        ...common,
        system: PROFILE_INSTRUCTIONS,
        prompt:
          `Current profile (JSON): ${JSON.stringify(user.profile)}\n\nLatest exchange:\n` +
          latest.map((t) => `${t.role === "user" ? "Person" : "Bot"}: ${t.text}`).join("\n"),
        output: Output.object({ schema: profileSchema }),
        maxOutputTokens: 300,
        abortSignal: AbortSignal.timeout(opts.timeoutMs),
      });
      await opts.store.setProfile(userKey, stripEmpty(result.output));
      await opts.guard.addCost(channel, costOf(result.providerMetadata));
    }

    const context = await buildContext(opts.store, user, opts.contextTokenBudget);
    if (!context.overflow) return;
    const older = await opts.store.turnsBetween(userKey, context.overflow.fromId, context.overflow.toId);
    if (older.length === 0) return;
    const result = await generateText({
      ...common,
      system: SUMMARY_INSTRUCTIONS,
      prompt:
        `Running summary so far:\n${user.summary || "(none)"}\n\nOlder messages to fold in:\n` +
        older.map((t) => `${t.role === "user" ? "Person" : "Bot"}: ${t.text}`).join("\n"),
      maxOutputTokens: 400,
      abortSignal: AbortSignal.timeout(opts.timeoutMs),
    });
    await opts.store.setSummary(userKey, result.text.trim(), context.overflow.toId);
    await opts.guard.addCost(channel, costOf(result.providerMetadata));
  };
}

function stripEmpty(profile: Profile): Record<string, unknown> {
  return Object.fromEntries(
    Object.entries(profile).filter(
      ([, v]) => v !== undefined && v !== "" && !(Array.isArray(v) && v.length === 0),
    ),
  );
}
