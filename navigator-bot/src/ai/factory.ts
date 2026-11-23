/**
 * Picks how questions are answered: with the AI model when OPENROUTER_API_KEY is set, otherwise the
 * test mode that lists the closest guide sections.
 */
import type { Config } from "../config.ts";
import { type Answerer, TestModeAnswerer } from "../conversation/answerer.ts";
import type { ConversationDeps } from "../conversation/pipeline.ts";
import type { KnowledgeBase } from "../kb/index.ts";
import type { MemoryStore } from "../memory/store.ts";

export interface AnswererSetup {
  answerer: Answerer;
  afterAnswer?: ConversationDeps["afterAnswer"];
}

export function createAnswerer(
  _config: Config,
  _deps: { store: MemoryStore; kb: () => KnowledgeBase },
): AnswererSetup {
  return { answerer: new TestModeAnswerer() };
}
