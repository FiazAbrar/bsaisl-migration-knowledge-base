/**
 * Answers with the AI model (through OpenRouter, so models can be compared and swapped by setting
 * LLM_MODEL). The model searches and reads the guides with read-only tools, then answers following
 * prompts/system.md. Code-side safeguards: a step limit, an output-length cap, a timeout with a fallback
 * model, providers that don't keep data, cost recorded against the daily budget, and the number check.
 */
import { generateText, type LanguageModel, type ModelMessage, stepCountIs } from "ai";
import type { Answer, Answerer, AnswerInput } from "../conversation/answerer.ts";
import { logger } from "../ops/logger.ts";
import { unsupportedNumbers } from "./numbers.ts";
import { systemPrompt } from "./prompt.ts";
import { guideTools, type ToolSession } from "./tools.ts";

export const MAX_STEPS = 8;

export interface AiAnswererOptions {
  model: LanguageModel;
  maxOutputTokens: number;
  timeoutMs: number;
  /** Extra options passed to the provider (OpenRouter: privacy and usage accounting). */
  providerOptions?: Record<string, Record<string, unknown>>;
}

/** The prompt asks for WhatsApp-style *bold*; replies are Markdown, where bold is **bold**. */
export function toMarkdownBold(text: string): string {
  return text.replace(/(?<![*\w])\*(?![\s*])([^*\n]+?)(?<!\s)\*(?![*\w])/g, "**$1**");
}

/** What the model was charged, when the provider reports it (OpenRouter usage accounting). */
export function costOf(providerMetadata: unknown): number {
  const cost = (providerMetadata as { openrouter?: { usage?: { cost?: unknown } } } | undefined)?.openrouter
    ?.usage?.cost;
  return typeof cost === "number" && Number.isFinite(cost) ? cost : 0;
}

export class AiAnswerer implements Answerer {
  readonly mode = "ai" as const;
  private readonly opts: AiAnswererOptions;

  constructor(opts: AiAnswererOptions) {
    this.opts = opts;
  }

  async answer(input: AnswerInput): Promise<Answer> {
    const session: ToolSession = { seen: [] };
    const system = systemPrompt(input.kb, {
      context: input.context,
      country: input.country,
      channel: input.channel,
    });
    const messages: ModelMessage[] = [
      ...input.context.turns.map(
        (t): ModelMessage =>
          t.role === "user" ? { role: "user", content: t.text } : { role: "assistant", content: t.text },
      ),
      { role: "user", content: input.text },
    ];

    let { text, cost } = await this.generate(system, messages, input, session);
    const missing = unsupportedNumbers(text, session.seen);
    if (missing.length > 0) {
      logger.warn({ count: missing.length }, "Answer had numbers not found in the guides; asking again");
      const retry = await this.generate(
        system,
        [
          ...messages,
          { role: "assistant", content: text },
          {
            role: "user",
            content:
              `[Automatic check, not from the person] These numbers in your reply are not in the guide text you ` +
              `read: ${missing.join(", ")}. Check them in the guides and correct them, or remove them. ` +
              "Reply again with the full corrected answer only.",
          },
        ],
        input,
        session,
      );
      cost += retry.cost;
      const stillMissing = unsupportedNumbers(retry.text, session.seen);
      if (stillMissing.length > 0)
        logger.warn({ count: stillMissing.length }, "Numbers still unconfirmed after a retry");
      text = retry.text;
    }
    return { text: toMarkdownBold(text.trim()), costUsd: cost };
  }

  private async generate(
    system: string,
    messages: ModelMessage[],
    input: AnswerInput,
    session: ToolSession,
  ): Promise<{ text: string; cost: number }> {
    const result = await generateText({
      model: this.opts.model,
      system,
      messages,
      tools: guideTools(input.kb, session),
      stopWhen: stepCountIs(MAX_STEPS),
      maxOutputTokens: this.opts.maxOutputTokens,
      abortSignal: AbortSignal.timeout(this.opts.timeoutMs),
      maxRetries: 1,
      ...(this.opts.providerOptions ? { providerOptions: this.opts.providerOptions as never } : {}),
    });
    const cost = result.steps.reduce((sum, step) => sum + costOf(step.providerMetadata), 0);
    if (!result.text.trim()) throw new Error("The model returned no text");
    return { text: result.text, cost };
  }
}
