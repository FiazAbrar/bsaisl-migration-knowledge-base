/**
 * Picks how questions are answered: with the AI model when OPENROUTER_API_KEY is set, otherwise the
 * test mode that lists the closest guide sections. Model ids are OpenRouter's (LLM_MODEL,
 * LLM_FALLBACK_MODEL, LLM_SMALL_MODEL), so models can be compared and changed without code changes.
 */
import { createOpenRouter } from "@openrouter/ai-sdk-provider";
import type { LanguageModel } from "ai";
import type { Config } from "../config.ts";
import { type Answerer, TestModeAnswerer } from "../conversation/answerer.ts";
import type { ConversationDeps } from "../conversation/pipeline.ts";
import type { Guard } from "../guard/guard.ts";
import type { MemoryStore } from "../memory/store.ts";
import { AiAnswerer } from "./answerer.ts";
import { createMemoryUpdater } from "./memory.ts";

export interface AnswererSetup {
  answerer: Answerer;
  afterAnswer?: ConversationDeps["afterAnswer"];
}

/** An OpenRouter model that only uses providers that don't keep data, and reports what it cost. */
export function openRouterModel(apiKey: string, model: string, fallback?: string): LanguageModel {
  const openrouter = createOpenRouter({ apiKey, appName: "BSAISL Migration Navigator" });
  return openrouter.chat(model, {
    ...(fallback ? { models: [fallback] } : {}),
    usage: { include: true },
    provider: { data_collection: "deny" },
  });
}

export function createAnswerer(config: Config, deps: { store: MemoryStore; guard: Guard }): AnswererSetup {
  const { ai } = config;
  if (!ai.apiKey) return { answerer: new TestModeAnswerer() };
  const answerer = new AiAnswerer({
    model: openRouterModel(ai.apiKey, ai.model, ai.fallbackModel),
    maxOutputTokens: ai.maxOutputTokens,
    timeoutMs: ai.timeoutMs,
  });
  const afterAnswer = createMemoryUpdater({
    model: openRouterModel(ai.apiKey, ai.smallModel),
    store: deps.store,
    guard: deps.guard,
    contextTokenBudget: ai.contextTokenBudget,
    timeoutMs: ai.timeoutMs,
  });
  return { answerer, afterAnswer };
}
