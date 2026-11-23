/**
 * What the AI is shown of a conversation, the way Claude Code manages its own context:
 * 1. the profile card (always; small),
 * 2. the running summary of older messages (always; small),
 * 3. as many recent messages as fit the token budget, newest first.
 * Messages that no longer fit and are not yet in the summary are reported as `overflow`, so the summariser
 * can fold them in (src/ai/memory.ts). Guide text is never kept in the history: it is searched fresh
 * for every question.
 */
import type { MemoryStore, Turn, UserRecord } from "../memory/store.ts";

export const MAX_RECENT_TURNS = 40;

/** A rough token count, good enough for budgeting: Bangla takes about twice as many tokens per letter. */
export function estimateTokens(text: string): number {
  let bangla = 0;
  for (const ch of text) if (ch >= "ঀ" && ch <= "৿") bangla++;
  const other = text.length - bangla;
  return Math.ceil(bangla / 2 + other / 4);
}

export interface ConversationContext {
  profile: Record<string, unknown>;
  summary: string;
  turns: Turn[];
  overflow: { fromId: number; toId: number } | undefined;
}

export function profileCard(profile: Record<string, unknown>): string {
  const lines = Object.entries(profile)
    .filter(([, v]) => v !== null && v !== undefined && v !== "" && !(Array.isArray(v) && v.length === 0))
    .map(([k, v]) => `- ${k}: ${Array.isArray(v) ? v.join("; ") : String(v)}`);
  return lines.join("\n");
}

export async function buildContext(
  store: MemoryStore,
  user: UserRecord,
  budgetTokens: number,
): Promise<ConversationContext> {
  const fixed = estimateTokens(profileCard(user.profile)) + estimateTokens(user.summary);
  let remaining = Math.max(0, budgetTokens - fixed);
  const recent = await store.recentTurns(user.userKey, MAX_RECENT_TURNS, user.summarisedTo);
  const kept: Turn[] = [];
  for (let i = recent.length - 1; i >= 0; i--) {
    const turn = recent[i] as Turn;
    const cost = estimateTokens(turn.text) + 4;
    if (cost > remaining && kept.length > 0) break;
    kept.unshift(turn);
    remaining -= cost;
  }
  const firstKept = kept[0]?.id;
  const dropped = firstKept === undefined ? [] : recent.filter((t) => t.id < firstKept);
  const lastDropped = dropped.at(-1);
  return {
    profile: user.profile,
    summary: user.summary,
    turns: kept,
    overflow: lastDropped ? { fromId: user.summarisedTo, toId: lastDropped.id } : undefined,
  };
}
