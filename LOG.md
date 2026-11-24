# Work log

What has been done to this knowledge base, by whom, how it was checked, what was tried and dropped, and what is left open. Newest first. Git history says which lines changed; this log says why, and what a collaborator needs to know before picking the work up.

Every change to a doc, the tools, the agency list or the datasets gets an entry here in the same commit or pull request, whether the work was done by a person or by an agent. A check on every pull request fails if it changes those folders without changing this file (see `.github/workflows/log-check.yml`).

How to write an entry: add it at the top, under this line, in this shape. Keep it short; link to `passes/` for the full trace of a large pass.

```
## YYYY-MM-DD · <what, in a few words> · <who: name or GitHub account; "agent for <name>" if an agent did it>

- **Done:** what changed, with numbers (articles read, facts added, sections, docs).
- **Where:** folders, pull request, and the `passes/` folder if there is one.
- **Checked by:** how it was verified (independent checker, build, insider review), or "not yet".
- **Tried and dropped:** approaches that didn't work, and why, so nobody repeats them.
- **Open:** what is left, blocked or undecided, and on whom.
```

---

## 2026-11-24 · One list of pages to get by hand · agent for FiazAbrar

- **Done:** `MANUAL-DOWNLOADS.md`: a short "Get these first" table (pages that settle open questions, with where to save each) and a generated backlog of every page the docs' notes list as blocked and not yet saved (432 pages in 25 docs). `tools/manual_downloads.py` refreshes the backlog; CLAUDE.md now tells agents to add blocked pages there.
- **Where:** `MANUAL-DOWNLOADS.md`, `tools/manual_downloads.py`, CLAUDE.md (Research process, step 7), README.
- **Checked by:** the script run against main; it leaves out pages a doc has since saved.
- **Open:** most backlog pages are from the first research rounds and lower priority; the top table is what to save first.

## 2026-11-24 · Official-source research on the docs built from news; agency-flag check · agent for FiazAbrar

- **Done:** the official research pass CLAUDE.md requires on the six country docs and three global docs first built from Prothom Alo: about 1,280 facts from official sources (US 127, Canada 155, UK 220, India 107, Lebanon 96, Greece 96, money 126, services 127, other destinations 230), Need-to-know questions answered where official pages answer them, news claims replaced where official sources differ. Also: the 23 Nov articles checked for agency flags (one new row, Lamisa Enterprise); the Illegal routes doc's US visa-bond section and the FAQ's PKB loan lines aligned with the official pages; plans.md records the one-file-per-doc restructure.
- **Where:** the nine doc folders, `agencies/`, `global/illegal-routes`, `global/faq`; trace in `passes/2026-11-24-official-research/` (briefs, checker verdicts, agency-flag outputs, `PAGES-TO-DOWNLOAD.md`).
- **Checked by:** an independent check of every new or changed sentence, including that each official quote is in its saved page, each official source is official, and OCR'd or scanned text matches the image; 102 fixes applied.
- **Tried and dropped:** treating a third party's copy of an official page as official (AILA's copy of the State Department notice is now marked unofficial); deleting true statements that lacked a fact (the fact was logged from the saved source instead).
- **Open:** about 30 pages blocked automated reading (`PAGES-TO-DOWNLOAD.md`; the most important are Bangladesh Bank's skills-loan circular, the live State Department pages and BMET's country statistics). Some quotes were retyped from scanned PDFs and checked by eye. The one-file-per-doc restructure waits for the wider repo restructure.

## 2026-11-24 · Navigator bot rebuilt in TypeScript on Chat SDK and AI SDK · agent for Angkon-Dutta-Joy

- **Done:** the bot in `navigator-bot/` is rewritten in TypeScript (Node 26 LTS) on Vercel's open-source Chat SDK (WhatsApp, Telegram and web adapters, Postgres state) and AI SDK (OpenRouter), as agreed with Abrar on 23 Nov ("don't reinvent the wheel"). Everything the Python bot did is kept: guide discovery and parsing, citation markers, open questions, safe swap, GitHub sync, the pull-request check, abuse limits and budgets, web chat with Turnstile, Telegram commands, test-mode replies. New: memory in the style of Claude Code (profile card, running summary, token-budgeted recent messages), retention of 90 days for messages and 12 months for the profile (was 30 days), a privacy notice in the first reply, fixed messages in Bangla and English, phone/NID/passport/card numbers removed before storage, a restart inbox so no reply is lost, Sentry alerts, the AI step with read-only tools and a number check (switched on by `OPENROUTER_API_KEY`), and an eval runner. The Python code is removed.
- **Where:** `navigator-bot/` (README, `.env.example`, `docs/PRIVACY.md`, `docs/bracit-setup.html` updated), `KB-STRUCTURE.md` (country names now in `src/kb/countries.ts`; a deliberate rename is confirmed with `KB_ACCEPT_COMMIT`), `.github/workflows/bot-ci.yml` (new: lint, type-check, tests, Docker build) and `bot-kb-check.yml` (now Node).
- **Checked by:** 86 automated tests (unit, embedded Postgres, end to end: a signed WhatsApp message answered once despite a repeat delivery, Telegram /start, web session and streamed answer, cross-site refusal; AI layer with a mock model). Parity: the TypeScript parser gives the same 29 guides and 3,573 sections as the Python one, text identical. The PR check passes against `main`. Web chat tried in a browser. Not yet: live WhatsApp and Telegram with real tokens, the Docker image on a server, a real AI model.
- **Tried and dropped:** pnpm (its installer is broken on the PC; npm comes with Node); rewriting the web page in React (the existing page is reviewed, accessible and small; it was moved to TypeScript instead, about 10 KB of script); a guessed default AI model (LLM_MODEL must be set with the key).
- **Open:** live test on the PC, then Phase B deploy (Neon, Render, Turnstile, UptimeRobot, Meta webhook switch). The AI step waits for an OpenRouter key and the model comparison. BRAC IT's answers in `docs/bracit-setup.html` part 15.

## 2026-11-23 · Bot reads every guide automatically; structure rules and a pull-request check · agent for Angkon-Dutta-Joy

- **Done:** the navigator bot now finds every folder with a `doc.md` by itself (countries under `countries/`, everything else shared), so new guides and countries such as `global/` and the UK, US, Canada, Greece, India and Lebanon need no bot change. Added `KB-STRUCTURE.md` (what the bot reads), a pointer to it in CLAUDE.md, and the pull-request check `.github/workflows/bot-kb-check.yml`, which fails if a guide on `main` would disappear, lose more than half of its sections (when it has 20 or more), or have no text. The live bot applies the same rule before swapping in a new index and otherwise keeps the last good one.
- **Where:** `KB-STRUCTURE.md`, `CLAUDE.md`, `.github/workflows/bot-kb-check.yml`, `navigator-bot/`.
- **Checked by:** the check run against `main` (29 guides, all readable); a deliberately broken copy (Saudi folder deleted, Qatar cut to 4 sections) was refused and the old index kept; a fresh server start pulled all 29 guides from GitHub in 12 seconds.
- **Tried and dropped:** a fixed list of guide folders in the bot (it silently missed `global/` when the cross-country doc was split).
- **Open:** a deliberate rename or deletion of a guide needs `python -m app.kb_index --force` on the server after merge; tell the bot team first.

## 2026-11-23 · Prothom Alo archive into the global docs; three new global docs · agent for FiazAbrar

- **Done:** about 2,115 new facts in the global docs: Illegal routes (465), FAQ (188), Departure bottlenecks (181), Dalal scams (116), and three new docs, Sending money home (428), Services for migrants and their families (357) and Other destinations (380, 24 countries). `questions.md` synced. The article-by-article coverage ledger added to the dataset: 1,904 stories, none unaccounted for.
- **Where:** `global/`; `datasets/prothom-alo-migration/coverage/ledger.csv`; trace in `passes/2026-11-23-prothom-alo-global/`. README, CLAUDE.md and the navigator bot list the new docs.
- **Checked by:** an independent final check of every new or changed sentence in all seven docs, including the FAQ against the fuller docs; 98 fixes applied. Conflicts settled from sources and recorded in each `notes.md`.
- **Tried and dropped:** putting remittance and service articles into the FAQ (too many; they got their own docs); a few cross-references that pointed to headings in another doc as if they were local (fixed in the final check).
- **Open:** the three new docs cite news only. PKB's language-loan page (pkb.gov.bd blocks automated reading) would settle whether Bangladesh Bank's 9% skills loan replaced PKB's 11% language loan. The 1,495 rejected stories with a single weak migration keyword were not checked.

## 2026-11-23 · Prothom Alo archive into the country docs · agent for FiazAbrar

- **Done:** about 1,960 new facts from Prothom Alo (2024 to Nov 2026) in 15 existing country docs (largest: Italy 416, UAE 185, Japan 115) and six new first-version docs built from the reporting: United States (221), Canada (167), United Kingdom (163), India (141), Lebanon (89), Greece (88). `questions.md` synced for every changed doc.
- **Where:** `countries/`; trace in `passes/2026-11-23-prothom-alo-countries/` (briefs, ledgers, checker verdicts, scripts); METHOD.md section 12 (the simplified process).
- **Checked by:** an independent final check of every new or changed sentence in all 21 docs; 245 fixes applied. Conflicts settled from sources and recorded in each `notes.md` (for example Kuwait nurse pay and experience settled on BOESL's circular; Oman's September 2023 departures on BMET's count; women need no mahram for Umrah, per Saudi Arabia's Hajj minister).
- **Tried and dropped:** the five-step draft, check, log, write and check pipeline of the earlier passes (too many hand-offs; replaced by section 12); leaving source conflicts for a human (Abrar asked that agents settle them).
- **Open:** the six new docs have no official sources yet; their "Need to know" bullets are the research list. PKB's loan page (pkb.gov.bd) blocks automated reading and would settle whether the 9% skills loan replaced the 11% language loan.

## 2026-11-23 · Work log started · agent for FiazAbrar

- **Done:** this file, with entries back-filled from the commit history and pull requests #1 to #10; a rule in CLAUDE.md that every change adds an entry; a pull-request check that enforces it.
- **Where:** `LOG.md`, `CLAUDE.md` ("Work log"), `.github/workflows/log-check.yml`, `tools/check_log.py`.
- **Checked by:** the check script run against this branch and against a branch with a doc change and no log entry.
- **Open:** the back-filled entries before 22 Nov are summaries of commit messages; collaborators can correct or add to their own.

## 2026-11-23 · Prothom Alo archive as an open dataset · agent for FiazAbrar

- **Done:** `datasets/prothom-alo-migration/`: all 27,907 stories the migration searches returned (1 Jan 2024 to 22 Nov 2026, full text, compressed), the 1,787 flagged as migration-related, the extractions (8,542 facts, 184 scam cases, 262 agency flags) and the harvester and filter scripts, with a README for every file and field.
- **Where:** pull request #10 (open).
- **Tried and dropped:** keeping the archive private; Abrar decided to publish it in full, since the pages are public.
- **Open:** a coverage ledger (which pass used each article, or why not) to be added when the current passes finish.

## 2026-11-23 · Cross-country doc split into four global docs · agent for FiazAbrar

- **Done:** `cross-country/` became `global/faq`, `global/dalal-scams`, `global/departure` and `global/illegal-routes`, one per part of the old doc; no sentence rewritten; facts and sources follow the doc that cites them; 26 cross-references rewritten to name the other doc. README, CLAUDE.md and the navigator bot updated.
- **Where:** pull request #9 (open); trace in `passes/2026-11-23-global-modules-split/`.
- **Checked by:** each doc builds with no citation errors; every source file of the old folder accounted for.

## 2026-11-23 · Method written down; open questions synced · agent for FiazAbrar

- **Done:** `METHOD.md` (how docs are researched, written and verified, sections 1 to 11) and `passes/` (briefs, drafts, checks and scripts of each archive pass, with a fact-prefix register); 104 new open questions added to the `questions.md` files.
- **Where:** pull requests #6 and #8 (merged).

## 2026-11-23 · Malaysia and Saudi Arabia: the rest of the Prothom Alo reporting · agent for FiazAbrar

- **Done:** 912 claims drafted from the archive, 901 cited (prefixes MP, SP, CQ); 70 fixes from the final check applied; Saudi attestation rule corrected (one-worker letters exempt since 22 Dec 2024); Malaysia medical instruction updated to the 19 Nov position.
- **Where:** pull request #7 (merged); `passes/2026-11-23-prothom-alo-malaysia-saudi/`.
- **Checked by:** independent claim check, then a sentence-by-sentence final check.
- **Tried and dropped:** a separate claim-check stage before writing; dropped later as it duplicated the final check.

## 2026-11-23 · Agency red flags from the archive · agent for FiazAbrar

- **Done:** 70 new press-flag rows (prefix PF) in `agencies/flags-press.csv`; RL numbers matched only when printed, exact, or backed by owner, address or official action; other matches listed as unconfirmed.
- **Where:** pull request #5 (merged); `passes/2026-11-23-prothom-alo-agency-flags/`.

## 2026-11-22 to 23 · Prothom Alo scam and harm cases · agent for FiazAbrar

- **Done:** scam sections of the cross-country doc from 184 case reports (pull request #3: 106 claims), then every remaining scam and harm case (pull request #4: 987 claims, 978 cited, 128 fixes from the final check).
- **Where:** pull requests #3 and #4 (merged); `passes/2026-11-22-prothom-alo-scams-1/`, `passes/2026-11-23-prothom-alo-scams-2/`.
- **Tried and dropped:** the first pass used only about 48 of 111 cases; Abrar asked for full coverage, and every case was then used.

## 2026-11-22 · Prothom Alo archive harvested and extracted · agent for FiazAbrar

- **Done:** 27,907 stories from Prothom Alo's public search API (2024 to 22 Nov 2026); 1,787 flagged by a rule-based filter; 1,597 read in full by AI readers (1,394 relevant, 8,542 facts).
- **Where:** `passes/2026-11-22-prothom-alo-harvest-and-extraction/`; the data itself in pull request #10.
- **Tried and dropped:** harvesting from 2009 (too much for the value; restarted from 2024); one keyword pass (Bangla search matches whole words only, so a second pass with 245 inflected forms and a third for Bangladeshis abroad were added); reading only parts of articles (replaced by full reads).

## 2026-11-22 · Navigator bot · Angkon-Dutta-Joy

- **Done:** `navigator-bot/`, a WhatsApp bot that answers from this knowledge base, then Telegram too; six contradictions found by the bot's prompt test fixed in Saudi Arabia and the cross-country doc.
- **Tried and dropped:** cloud-hosting work committed by mistake and reverted.

## 2026-11-19 · South Korea, Japan, Brunei, cross-country doc · bsaisl4

- **Done:** new docs for South Korea, Japan and Brunei; the cross-country doc (FAQ, dalal scams, departure bottlenecks, illegal routes).

## 2026-11-17 · Reverification · Angkon-Dutta-Joy

- **Done:** a reverification pass over the knowledge base.

## 2026-11-10 to 14 · Italy, Kyrgyzstan, Cambodia, Singapore, Oman, Jordan · Angkon-Dutta-Joy, bsaisl4

- **Done:** Italy (14 research agents, 1,657 facts, 449 sources, then 162 facts from team-saved official files), Kyrgyzstan (1,098 facts, 313 sources) and Cambodia (1,347 facts), each checked to zero failures over several rounds with a coverage audit (Angkon-Dutta-Joy); Singapore, Oman and Jordan, with plain-language "Start here" sections for Singapore and Oman (bsaisl4).
- **Open:** pull request #2 (bring Jordan, Singapore and Oman in line with the repo norms) is still open.

## 2026-11-08 to 09 · Qatar, UAE, Maldives, Kuwait; clarity rewrite · Angkon-Dutta-Joy, FiazAbrar

- **Done:** Qatar, UAE, Maldives (1,120 facts, 337 sources, checked to zero failures in four rounds) and Kuwait (1,557 facts, 432 sources); a three-step clarity rewrite of the early docs (338 to 214 to 128 failures, then each section fixed and checked).

## 2026-11-07 to 08 · Rules, build and agency list · FiazAbrar

- **Done:** one shared CLAUDE.md and toolset; the five-part Background; "form follows function"; Need to know as its own block; numbered headings with fixed links; specific cross-references the build links; superscript citations and a Contents list; the agency list (179 most active agencies with cited red flags, then v2 with the visa-sale chain); open-questions files per country.

## 2026-11-06 to 07 · Repository started · FiazAbrar, Angkon-Dutta-Joy

- **Done:** method, the Saudi Arabia doc and shared sources (FiazAbrar); Malaysia (Angkon-Dutta-Joy, pull request #1).
