/**
 * Run the evaluation questions (evals/questions.csv) against the bot.
 *
 *   npm run eval                      test mode (no AI key): does search find the expected section?
 *   npm run eval -- --models a,b      with OPENROUTER_API_KEY: answer every question with each model and
 *                                     have a judge model grade it against must_include / must_not
 *   npm run eval -- --only Q01,Q07    a few questions only
 *
 * Results go to evals/results/<date>-<mode>.csv (not committed) and a summary is printed.
 * Every AI run costs money: the summary prints what OpenRouter reported.
 */
/* biome-ignore-all lint/suspicious/noConsole: a command-line tool prints to the console */
import { mkdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { parseArgs } from "node:util";
import { generateText, Output } from "ai";
import { parse as parseCsv } from "csv-parse/sync";
import { z } from "zod";
import { AiAnswerer, costOf } from "../src/ai/answerer.ts";
import { openRouterModel } from "../src/ai/factory.ts";
import { BOT_ROOT, config } from "../src/config.ts";
import { KnowledgeBase } from "../src/kb/index.ts";

interface Question {
  id: string;
  country: string;
  language: string;
  category: string;
  question: string;
  must_include: string;
  must_not: string;
  source_section: string;
}

const { values } = parseArgs({
  options: {
    models: { type: "string" },
    judge: { type: "string" },
    only: { type: "string" },
    kb: { type: "string" },
  },
});

const csvField = (v: string) => `"${v.replaceAll('"', '""')}"`;

async function loadQuestions(): Promise<Question[]> {
  const raw = await readFile(path.join(BOT_ROOT, "evals", "questions.csv"), "utf-8");
  const rows = parseCsv(raw, { columns: true, bom: true, skip_empty_lines: true }) as Question[];
  const only = values.only?.split(",").map((s) => s.trim());
  return only ? rows.filter((r) => only.includes(r.id)) : rows;
}

/** Test mode: is the expected section among the top 5 search results for the question? */
function retrievalRun(kb: KnowledgeBase, questions: Question[]): string[][] {
  const rows: string[][] = [["id", "language", "expected", "found", "top_hit"]];
  const byLang = new Map<string, { hit: number; total: number }>();
  for (const q of questions) {
    if (!q.source_section) continue;
    const country = q.country || kb.countries.detect(q.question);
    const hits = kb.search(kb.countries.strip(q.question), country, 5);
    const expected = q.source_section.trim().toLowerCase();
    const found = hits.some(
      (h) => h.path.toLowerCase().startsWith(expected) || expected.startsWith(h.path.toLowerCase()),
    );
    const stat = byLang.get(q.language) ?? { hit: 0, total: 0 };
    stat.total++;
    if (found) stat.hit++;
    byLang.set(q.language, stat);
    rows.push([q.id, q.language, q.source_section, found ? "yes" : "no", hits[0]?.path ?? ""]);
  }
  console.log("Search finds the expected section (top 5):");
  for (const [lang, s] of byLang) console.log(`  ${lang.padEnd(9)} ${s.hit}/${s.total}`);
  return rows;
}

const verdictSchema = z.object({
  pass: z.boolean(),
  missing: z.array(z.string()).describe("Required points the answer leaves out or gets wrong"),
  violations: z.array(z.string()).describe("Things the answer does that it must not"),
});

async function aiRun(
  kb: KnowledgeBase,
  questions: Question[],
  models: string[],
  judgeModel: string,
): Promise<string[][]> {
  const settings = config();
  const apiKey = settings.ai.apiKey;
  if (!apiKey) throw new Error("Set OPENROUTER_API_KEY (and LLM_MODEL or --models) for an AI run.");
  const judge = openRouterModel(apiKey, judgeModel);
  const rows: string[][] = [
    ["id", "model", "language", "pass", "missing", "violations", "answer", "cost_usd"],
  ];
  let total = 0;
  for (const modelId of models) {
    const answerer = new AiAnswerer({
      model: openRouterModel(apiKey, modelId),
      maxOutputTokens: settings.ai.maxOutputTokens,
      timeoutMs: settings.ai.timeoutMs,
    });
    let passed = 0;
    for (const q of questions) {
      let answer = "";
      let cost = 0;
      try {
        const a = await answerer.answer({
          channel: "web",
          userKey: "eval",
          text: q.question,
          lang: /[ঀ-৿]/.test(q.question) ? "bn" : "en",
          country: q.country || kb.countries.detect(q.question),
          kb,
          context: { profile: {}, summary: "", turns: [], overflow: undefined },
        });
        answer = a.text;
        cost = a.costUsd ?? 0;
      } catch (err) {
        answer = `ERROR: ${(err as Error).message}`;
      }
      const verdict = await generateText({
        model: judge,
        system:
          "You grade a migration help bot's answer. It passes only if it covers every required point (the gist, " +
          "in any language) and does none of the forbidden things. Be strict about numbers and dates.",
        prompt: `Question: ${q.question}\n\nRequired points: ${q.must_include}\n\nMust not: ${q.must_not}\n\nAnswer:\n${answer}`,
        output: Output.object({ schema: verdictSchema }),
      });
      cost += costOf(verdict.providerMetadata);
      total += cost;
      if (verdict.output.pass) passed++;
      rows.push([
        q.id,
        modelId,
        q.language,
        verdict.output.pass ? "yes" : "no",
        verdict.output.missing.join("; "),
        verdict.output.violations.join("; "),
        answer,
        cost.toFixed(4),
      ]);
      console.log(`  ${modelId} ${q.id} ${verdict.output.pass ? "pass" : "FAIL"}`);
    }
    console.log(`${modelId}: ${passed}/${questions.length} passed`);
  }
  console.log(`Total cost reported by OpenRouter: $${total.toFixed(4)}`);
  return rows;
}

async function main(): Promise<void> {
  const settings = config();
  const kb = await KnowledgeBase.build(values.kb ?? settings.kb.dir);
  const questions = await loadQuestions();
  const models = (values.models ?? "")
    .split(",")
    .map((m) => m.trim())
    .filter(Boolean);
  const modelList =
    models.length > 0
      ? models
      : settings.ai.evalModels.length > 0
        ? settings.ai.evalModels
        : [settings.ai.model].filter(Boolean);
  const ai = Boolean(settings.ai.apiKey) && modelList.length > 0;
  const rows = ai
    ? await aiRun(kb, questions, modelList, values.judge ?? modelList[0] ?? "")
    : retrievalRun(kb, questions);
  const dir = path.join(BOT_ROOT, "evals", "results");
  await mkdir(dir, { recursive: true });
  const file = path.join(
    dir,
    `${new Date().toISOString().slice(0, 16).replace(/[:T]/g, "-")}-${ai ? "ai" : "search"}.csv`,
  );
  await writeFile(file, `﻿${rows.map((r) => r.map(csvField).join(",")).join("\n")}\n`, "utf-8");
  console.log(`Results: ${path.relative(process.cwd(), file)}`);
}

await main();
