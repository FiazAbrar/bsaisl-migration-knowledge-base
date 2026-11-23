/**
 * Knowledge-base commands.
 *   npm run kb:index                         read every guide and print its section count
 *   npm run kb:check -- --base origin/main   the pull-request check (exit 1 if the bot would refuse)
 */
/* biome-ignore-all lint/suspicious/noConsole: a command-line tool prints to the console */
import { parseArgs } from "node:util";
import { config } from "../config.ts";
import { checkAgainst, KB_ROOT_FROM_BOT } from "./check.ts";
import { KnowledgeBase } from "./index.ts";

const { positionals, values } = parseArgs({
  allowPositionals: true,
  options: { base: { type: "string", default: "origin/main" }, kb: { type: "string" } },
});

function table(counts: Record<string, number>): void {
  for (const [slug, n] of Object.entries(counts).sort(([a], [b]) => a.localeCompare(b))) {
    console.log(`  ${slug.padEnd(28)} ${String(n).padStart(5)} sections`);
  }
}

async function main(): Promise<number> {
  const command = positionals[0] ?? "index";
  if (command === "index") {
    const kbDir = values.kb ?? config().kb.dir;
    const kb = await KnowledgeBase.build(kbDir);
    table(kb.sectionCounts());
    for (const w of kb.meta.warnings) console.log(`  warning: ${w}`);
    console.log(`${kb.guides.length} guides, ${kb.sections.length} sections, read from ${kbDir}`);
    return 0;
  }
  if (command === "check") {
    const kbDir = values.kb ?? KB_ROOT_FROM_BOT;
    const { counts, problems } = await checkAgainst(kbDir, values.base);
    const total = Object.values(counts).reduce((a, b) => a + b, 0);
    console.log(`Guides the bot can read: ${Object.keys(counts).length} (${total} sections)`);
    table(counts);
    if (problems.length > 0) {
      console.log("\nThe bot would refuse this version of the knowledge base:");
      for (const p of problems) console.log(`  - ${p}`);
      console.log(
        "\nIf a guide was moved or renamed on purpose, say so in the pull request; the bot picks up the new " +
          "folder by itself, but the check flags the old one as gone. The structure the bot expects is in " +
          "KB-STRUCTURE.md.",
      );
      return 1;
    }
    console.log("\nOK: every guide on the base branch is still there and readable.");
    return 0;
  }
  console.error(`Unknown command: ${command} (use "index" or "check")`);
  return 2;
}

process.exitCode = await main();
