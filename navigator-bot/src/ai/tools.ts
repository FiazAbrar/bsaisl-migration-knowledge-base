/**
 * The only things the AI can do: search the guides, read a guide's contents list, and open a section.
 * All read-only, all from the bot's own copy of the guides; no web access. Every text returned is also
 * collected (`seen`), so the answer's numbers can be checked against what the AI actually read.
 */
import { tool } from "ai";
import { z } from "zod";
import type { KnowledgeBase } from "../kb/index.ts";

export interface ToolSession {
  /** Text of everything the tools returned for this question. */
  seen: string[];
}

export function guideTools(kb: KnowledgeBase, session: ToolSession) {
  const guideIds = kb.guides.map((g) => g.slug);
  const remember = <T>(value: T): T => {
    session.seen.push(JSON.stringify(value));
    return value;
  };

  return {
    search_guides: tool({
      description:
        "Search the guides with a few English keywords. Returns matching sections with a short snippet. " +
        "Set `guide` to a country's guide id (or a shared guide id) to search only that guide.",
      inputSchema: z.object({
        query: z.string().min(1).max(200).describe("A few English keywords, e.g. 'medical test cost'"),
        guide: z
          .string()
          .optional()
          .describe(`Guide id, one of: ${guideIds.join(", ")}`),
      }),
      execute: async ({ query, guide }) =>
        remember(
          kb.search(query, guide && guideIds.includes(guide) ? guide : undefined, 8).map((h) => ({
            section_id: h.id,
            guide: h.slug,
            section: h.path,
            part: h.part,
            has_open_questions: h.openQuestions,
            snippet: h.snippet,
          })),
        ),
    }),

    list_guide_sections: tool({
      description:
        "The contents list of one guide: every section's id and heading path, to pick sections to open.",
      inputSchema: z.object({ guide: z.string().describe(`Guide id, one of: ${guideIds.join(", ")}`) }),
      execute: async ({ guide }) =>
        guideIds.includes(guide)
          ? kb
              .contents(guide)
              .map((s) => ({ section_id: s.id, section: s.path, part: s.part, words: s.words }))
          : { error: `No guide called '${guide}'. Guides: ${guideIds.join(", ")}` },
    }),

    read_section: tool({
      description:
        "Open one section in full, with its sources. Read sections before answering; snippets are not enough.",
      inputSchema: z.object({ section_id: z.number().int().positive() }),
      execute: async ({ section_id }) => {
        const s = kb.section(section_id);
        if (!s) return { error: `No section ${section_id}` };
        const sources = kb.sourcesFor(s.slug, s.facts).map((f) => ({
          publisher: f.publisher || undefined,
          type: f.sourceType,
          date: f.pageDate || undefined,
        }));
        return remember({
          guide: s.guide,
          section: s.path,
          part: s.part,
          text: s.text,
          sources: dedupe(sources),
        });
      },
    }),
  };
}

function dedupe<T>(items: T[]): T[] {
  const seen = new Set<string>();
  return items.filter((i) => {
    const key = JSON.stringify(i);
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
  });
}
