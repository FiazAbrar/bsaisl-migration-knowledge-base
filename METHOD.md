# How a fact gets into a doc

This file describes how the country docs are actually researched, written and checked, so a new fellow can run the same process and anyone can trace a sentence back to its evidence. CLAUDE.md sets the rules; this file records how they were carried out on Cambodia, Italy, Kuwait and Kyrgyzstan (9 to 17 Nov 2026) and in the Prothom Alo archive passes. Sections marked **Observed** report what the checkers actually found; they describe past runs, not rules.

The one-line version: every sentence in `doc.md` cites fact ids; every fact id is a row in `facts.csv` holding an exact quote; every quote was machine-checked against a saved copy of its source; and every sentence was then read by a checker who had not done the research, until a round found nothing wrong.

## 1. Sources

1. **Save before you use.** Every page or PDF is saved with `tools/fetch.py <url> <name>`. It writes `sources/<name>.html` or `.pdf`, a text copy (`.md` from pandoc for HTML, `.txt` from pdftotext for PDF) and a row in `sources/_fetchlog.csv` (name, url, access date, HTTP status, method, files). It refuses a URL already saved, so the log doubles as a "have we got this?" index (`fetch.py --find <text>`).
2. **Name sources by publisher first**, lowercase with hyphens, specific enough not to clash with another agent's: `mlvt-kh-...`, `bdemb-bangkok-fb-...`, `news-prothomalo-cambodia-2026-05`.
3. **Register it** with `facts.py source` (publisher, title, official yes/no/archived/news-archived, page date). This feeds the reference list.
4. **Blocked pages**, in this order:
   - Firecrawl scrape with default settings only (no stealth, proxies or bot-check workarounds). Save the markdown as `sources/<name>.md` and log it with `fetch.py --log <url> <name> firecrawl`.
   - `tools/wayback.py <url> <name> official|news` for the newest archived copy. Also used for pages that were removed, and to date undated pages.
   - If both fail, list the page in the country's `notes.md` under "Pages we could not download" (and in `drafts/_blocked-pages.md`): exact URL, suggested file name, what it should prove, in priority order. A team member saves it by hand into `countries/<c>/manual/` (never straight into `sources/`), keeping the real extension: PDF, "Save page as" HTML, or a dated PNG screenshot. Facebook posts of official bodies count as official and usually arrive this way.
   - Hand-saved files are then read by an agent, copied into its work folder, logged with `fetch.py --log <url> <name> manual`, and turned into facts like any other source. An image-only file gets a faithful transcription (`<name>.md`, first line saying what was transcribed, when and from where) so quotes can be checked against text.
5. **Pages already saved for another country** (OEP, BMET, PKB, Welfare Board pages) may be copied across and logged as `manual`, but a fresh fetch is preferred because fees change, and every fact is logged again in the new country.
6. **Dates.** `tools/datepass.py` looks for real dates on undated or old sources (page metadata, Last-Modified headers) and writes `sources/_datepass.csv` for review.

## 2. Facts

A fact is one row of `facts.csv`: id, claim, quote, saved_file, url, page_date, access_date, source_type, status, optional visa/field/value, note.

- **Logged with `facts.py add`.** It normalises whitespace, markdown and quote marks, then refuses the fact if the quote (at least 12 characters) is not found in the saved text copy. This is the only defence against facts written from memory, so never get round it. The one exception is `--no-quote-check`, which demands a `--note` saying why (garbled Bangla PDF text layer, a table whose rows pdftotext shifts); those facts are checked by eye against the rendered page.
- **One fact per number or rule.** The quote must prove the claim, including every number in it. Keep quotes short and exact.
- **Statuses:** `verified` (official, dated within 12 months), `possibly-outdated` (official, older or undated), `conflict` (sources disagree; one row per side, each note naming the other id), `unofficial` (news, NGO or guide reporting what happens in practice), `lead` (third-party source used only after an official search failed). In the doc, official sources print as `[n]`, the rest as `[Nn]`.
- **Prefixes.** Each agent or person working at the same time gets its own prefix, so ids never clash when folders are merged. Country research uses one letter per topic: N corridor and money in practice, W destination-side work route, B Bangladesh side, L law and work, V visits, study and family, U irregular routes and asylum, G money, plus country-specific letters (S scam compounds in Cambodia; D domestic or seasonal work and F family in Italy and Kuwait; A asylum in Italy; L1/L2 in Kuwait, where two law agents ran). Later passes use their own: K gap agent for official texts, M and P hand-saved files (P: Italy's first batch of 10 official files), R restore agent, Q/QA/QB/QC Italy's second batch of hand-saved files, ZZ facts added by hand to the merged file. Archive passes use two-letter prefixes (LB, AA, AB, FV, MA, MB, RU, OA, OB, MP, SP, CQ, PF).
- **Many facts at once:** write a JSON list and run `work/addm.py x.json` from the agent's folder; it calls `facts.py` for each item, so every quote is still checked. Run each JSON batch once (rerunning duplicates facts); put new facts in a new file.
- `facts.py cited doc.md <start> <end>` lists the facts behind a stretch of the doc, for checking.

## 3. Research rounds and agent roles

A country is done by a lead plus agents, each with a written brief. The briefs are kept in `countries/<c>/drafts/`.

1. **Lead sets up** `drafts/`, `verify/`, `manual/`, `sources/` and `work/<X>/sources/` for each letter, copies the helper scripts into `work/` (merge.py, apply.py, questions.py, addm.py), and writes the outline for the user's OK.
2. **Research agents (7 to 10 in parallel), one per topic**, from one shared brief (`drafts/_brief.md`): the rules, the style, starting numbers to verify, official sites and news to search in English, Bangla and the local language, the outline, and "who does what" by letter. Each works only in `work/<X>/` (own `sources/`, `sources.csv`, `facts.csv`), never writes to the merged files, never commits. Time box about 40 minutes. Output: `drafts/<X>-findings.md` with (a) draft doc text for its sections, every sentence cited with its own ids, (b) notes: searches run, conflicts, practice, facts logged but not used and why, (c) blocked pages, (d) open insider questions.
3. **Resume.** If agents are stopped before writing findings (Cambodia: stopped after about 50 minutes with 948 facts logged and no findings files), `drafts/_resume.md` records where things stand and `drafts/_resume-brief.md` relaunches them: keep existing facts and sources, don't refetch or re-log, fill the biggest gap for 10 minutes, then write findings.
4. **Merge.** `python work/merge.py` (from the country folder) rebuilds `sources/`, `sources/_fetchlog.csv`, `sources.csv` and `facts.csv` from scratch out of every `work/<X>/`. Identical files saved by two agents are kept once; a name clash with different content is renamed `<name>-<x>` and that agent's facts repointed. Every quote is re-checked against the merged copies and problems are printed.
5. **Gap agent (K).** After merging, one agent fetches official texts the others couldn't get (laws, ministerial orders, fee tables), logs them, and proposes edits (`verify/k-inserts.md`, same FAIL/old/new format as below).
6. **Blocked-pages list to the user**, once, in priority order; work continues without waiting. Hand-saved files go through an M (or Q) agent that logs facts and proposes edits (`verify/m-inserts.md`, Italy `verify/q-<X>.md`).
7. **Writers (6 or 7 in parallel)**, from `drafts/_writer-brief.md`: each assembles one part of `doc.md` (`drafts/part-<N>.md`) from the findings, with exact headings, the lead's known decisions (which status figure to use, what not to name, the exchange rate and the fact id to cite with it), and the rule to cite only ids that exist in the merged `facts.csv`, chosen by reading their claims. No web research. The lead concatenates the parts into `doc.md` and builds with `tools/build.py`, which stops on any citation without a fact.
8. **Verification rounds** (section 4).
9. **Coverage audit** (`drafts/_coverage-brief.md`): one agent, no web research, runs the three audits of CLAUDE.md step 9 (migrant's questions, aim per visa, insider test) using only facts already logged, and reviews every logged-but-uncited fact. It proposes up to about 25 edits in FAIL/old/new format (`verify/coverage.md` or `cov-1.md`); a gap no fact fills is appended as `NEEDTOKNOW: <question>`, which apply.py turns into a Need to know block.
10. **Restore (Italy only).** Verifiers narrow or cut details their cited facts don't carry, even when the saved source does say them. A restore agent (R) logged 14 facts for such details and put them back (`verify/restore-1.md`). Kuwait's notes list four such details still to log.
11. **Wrap-up.** `work/questions.py` writes `questions.md` from the Need to know blocks. The lead records the run in `notes.md` under "Writing and independent check": rounds and failure counts, decisions taken, known weak points, what to recheck and when.

## 4. The verification loop

**Who:** checker agents who have not seen the research. Round 1 splits the whole doc into line ranges (`verify/r1-lines-<N>.txt`, e.g. `1-211`) across 6 or 7 checkers, about 15 minutes each.

**What a checker does** (`drafts/_verifier-brief.md`), for every sentence and fact-bearing list item in its range:
1. Look up every cited id in `facts.csv` and read the claim and the quote; open the saved source when in doubt.
2. FAIL if: an id doesn't exist; the quotes don't support the sentence; any number, fee, date, duration, percentage or name is not in the cited facts; the sentence says more than the facts ("always", "most", a wrong year, a different job); the sentence or list item has no citation; a currency conversion is more than 3% off the logged rate.
3. Also FAIL research narration ("source X says", "reports conflict"), notes to the editor, our own advice, and vague cross-references ("see above", "(item 4)"). Later briefs added: a sentence that contradicts another in the same paragraph; a fact repeated in the same paragraph; a local-language term left unexplained at first use in the section.
4. Skipped: headings, Need to know bullets, and ready-to-use "Sample wording" templates.

**Output format** (`verify/r<round>-<N>.md`), failures only, or `No failures.`:

```
### FAIL <line number>
reason: <one line>
old: <exact fragment from doc.md, unique, at least 30 characters>
new: <final doc wording with correct citations, or (delete)>
```

`new:` must be final text, never an instruction. Checkers prefer narrowing the sentence to what the facts support, or re-citing to the right existing id, over deleting.

**Applying:** the lead snapshots the doc (`drafts/doc-before-r<N>.md`, or `verify/doc-before-*` in Italy and Kuwait), reads the fixes, overrules any that are wrong (Italy: one, which would have deleted a sample letter), then runs `python work/apply.py verify/r1-*.md`. It replaces each `old` with `new` once and prints any `old` it couldn't find.

**Next rounds** check only the lines that changed: the lead lists their line numbers in `verify/r<round>-lines-<N>.txt` and the round brief (`_verifier-brief-r<round>.md`) says what changed and any new rule. Any batch of new material (coverage edits, gap-agent facts, hand-saved files) is followed by a round on the lines it touched. **The loop stops when a round on all changed lines returns no failures.**

**Observed rounds** (failures per round, from `verify/` and `notes.md`):

- Cambodia: 68, 17, then coverage (25 edits) and gap agent K (47 edits), 21, 4, 1, 0. Hand-saved files M (26 edits): 5, 2, 2, 0.
- Italy: 79, then restore (14 facts) and coverage (10), 24, 4, 0. Second batch of hand-saved files (162 facts, 85 edits): 20, 7, 2, 2, 0.
- Kuwait: 87, 10, then coverage (8), 2, 0.
- Kyrgyzstan: 79, 6, then coverage (22 points, 9 Need to know), 11, 1, 1, 0. A later round after hand-saved files found 1 failure (one word: "Banks" narrowed to "Banks such as Optima Bank"); the fix is applied, but no round rechecked it.

## 5. Conflicts and gaps

- Keep both sides in `facts.csv` with status `conflict` and notes naming each other. In the doc, state the newer or official version with its citation; if the conflict changes what a migrant would do, add one Need to know bullet. Write the reasoning in `notes.md` (for example the 17 Nov 2026 Welfare Board insurance start date: WEWB notice ZZ0001 against BMET's undated leaflet, applied to every country doc).
- A Need to know is written only after searching official sites, Bangla news, agency guides, NGO reports and embassy pages. It sits in its own block right after the paragraph it belongs to, one precise question per bullet. Writers cut any question a fact now answers; checkers and the lead remove duplicates.

## 6. Matching agencies to licence numbers (RL)

From `agencies/notes.md` ("RL matching") and `FLAG-SPEC.md`:

- RL numbers come from BMET's licence list, `data/oep-agency-list-2026-10-28.csv`.
- **Best evidence is the RL printed in the source.** Otherwise match by name, and record how: exact, spelling variant, or uncertain with the reason. A similar name is not enough: also check address, district, owner and licence date where the source gives them, and look for contradictions (Imperial Overseas: OEP's RL0428 is too old for the 2021 licence Prothom Alo gives, so it was left blank).
- Non-exact matches say so in the evidence column ("RL matched by name to OEP list entry '...'") or the summary ("RL inferred"). A Bangla-to-English transliteration can point to the wrong agency: check before naming any agency in a doc.
- Confirm from a second official record where one exists. Japan's OTIT list prints RLs and settled Binimoy International as RL0351, not RL0816.
- Leave the RL blank when unsure. Travel agencies and consultancies usually have no RL. Record the agency's status on the OEP list (Active, Cancelled, Suspended, Expired, Server Locked) with its date.
- Naming an agency in a country doc needs outside evidence; high volume and a matched RL are not evidence of fair practice.

## 7. News-archive passes (Prothom Alo)

These passes ran outside the repo, on a Prothom Alo archive (2024 to Nov 2026); their specs, inputs and outputs are in `prothom-alo-archive/extract/`. Only their facts (pa-*.md sources and the prefixed facts) entered the repo.

1. **Full-read extraction** (`GENERAL-SPEC.md`; `SPEC.md` for scam cases). Agents read every article in full, to the last character, printing one article at a time, and write one JSON record per article: relevant or not (with the reason), kinds, countries, summary, every usable fact (typed, dated, self-contained, attributed), named actors, individual cases, and one exact Bangla quote checked by Python. These records act as an index; later steps reread the articles.
2. **Drafting** (`kb2/DRAFT-SPEC.md` for the cross-country doc, `kb3/COUNTRY-DRAFT-SPEC.md` for country docs). Drafters read the target sections and every article in full, then write draft sentences, each with a target section and one to three exact Bangla quotes (checked as substrings by Python), keeping the article's attribution. Every article is accounted for: drafts or a "nothing to add" reason.
3. **Independent claim check** (`kb2/CHECK-SPEC.md`). A second agent reads each article in full and gives each draft a verdict (supported, partly, unsupported), the problem, a corrected claim and fresh quotes.
4. **Logging.** `kb2/add_facts2.py` (and `kb3/add_facts3.py`) saves each article as a source and logs each checked claim with its quotes through `facts.py`, so the usual quote check applies.
5. **Writers own disjoint sections** (`kb2/jobs/WRITE-SPEC.md`, `owned-sections.json`). Each writer places every claim in its own sections or lists it as unused with one of three reasons (duplicate, merged, no bearing). Output is REPLACE/NEW blocks per section, not edits to the doc, with Python checks that no existing citation was lost and every cross-reference exists. `kb2/jobs/splice.py` applies the blocks.
6. **Final sentence check** (`kb2/jobs/FINAL-CHECK-SPEC.md`). An independent checker diffs each rewritten section against git HEAD and checks every new or reworded sentence against its facts and, where in doubt, the article: unsupported detail, dropped attribution, merged people or cases, a wrong id, no citation, own conclusions, changed meaning, broken cross-references, lead sentences not true of every case below them, unexplained acronyms. It outputs `{old_str, new_str, problem}`; `kb2/jobs/apply_fixes.py` applies those with exactly one match and logs them to `fixes-applied.json`.
7. **Agency flags** (`agencies/FLAG-SPEC.md`): full read of every article, one row per firm and event, with RL matching as in section 6 and a check against existing flags.

**The simplified two-stage version now in use:** draft with saved quotes, then write, then the final sentence check. The separate claim check (step 3) was dropped. It largely duplicated the final check, and saving quotes at extraction means articles need not be reread to check them. In `kb3`, 700 of 916 drafts went through the claim check; the rest were logged as `unchecked` and left to the final check (`add_facts3.py`).

**Lessons from these passes:**
- Read every article in full. Keyword searches and partial reads produced false "misses" (facts reported absent that were in the article).
- Save quotes at extraction so later steps can check without rereading.
- Drafters tend to bring in details from other articles, drop attributions, and over-generalise lead sentences. The checkers catch these, so never skip the final check.
- An RL match needs evidence beyond a similar name.

## 8. What each check typically catches

**Observed.** Counts come from the files named. Categories were assigned by keyword matching on each failure's `reason`/`problem` line and then spot-read, so read the percentages as rough sizes, not exact figures.

**Country verifiers** (all `verify/r*-*.md` in the four countries: 423 failures, 313 of them in round 1):
- About 28%: a detail not in the cited facts (a place, a job, a qualifier, a step), often present in the source or in another fact.
- About 22%: the cited fact says something different or narrower (another office, one bank and not all banks, grounds for annulment and not for refusal, a plan reported as done).
- About 17%: overstatement or generalisation ("most", "mostly rejected" for "rejected in large numbers", one case written as a rule).
- About 6%: a sentence or list item with no citation (Italy and Kyrgyzstan most).
- About 5%: arithmetic or Taka conversion (11 of Kyrgyzstan's 79 round-1 failures, from som/RP conversions with no logged rate until R0001 was added).
- About 4%: the wrong id cited where the right fact exists. This is undercounted: many "not in the cited facts" reasons also name the id that does support it.
- About 2% each: research narration ("the Embassy's FAQ gives"), our own advice or inference; about 1% each: contradictions or wrong order of events, vague cross-references. One id did not exist.
- Only 6 of the 423 fixes deleted a sentence; the rest narrowed or re-cited it.
- Round 1 found about one failure per 20 to 30 doc lines (68 to 87 per doc of 1,490 to 2,170 lines, counting headings and blank lines). Inserted material failed at a higher rate: Italy's second batch had 20 failures on 91 changed lines.

**Coverage audits** added 8 to 25 points per doc from facts already logged (Kuwait 8, Italy 10, Kyrgyzstan 22, Cambodia 25), mostly logged-but-uncited facts on costs, contacts and procedures. Kuwait had 372 uncited facts left at the end, mostly duplicates between agents, superseded figures and statistics with no bearing on a decision.

**Archive claim check:** `kb2` gave 879 supported and 108 partly (11%) of 987 drafts, none unsupported. `kb3` gave 529 supported and 171 partly (24%) of 700 checked. Among the problems, dropped or changed attribution came first, about a third ("stated as fact, but the article gives it as what the case complaint says"). Then came details not in the article, and wrong dates, including the press-release date given as the event date and a plan reported as done, each about one in six. Wrong numbers and names were fewer.

**Archive final check:** `kb2` produced 128 fixes for 987 claims written. About a quarter were cross-references, acronyms and structure, about a quarter attribution, and about one in eight lead sentences or merged cases; only 5 were deletions. For `kb3`, fix files exist only for the Malaysia sections (14 fixes); none are in the folder for Saudi Arabia or the cross-country sections.

**Agency flags:** 262 flag rows. RL matches: 135 exact, 52 spelling variants, 18 uncertain and 39 unmatched (the rest unlabelled). 166 rows were events already flagged, and 93 new flags were written.

## 9. Where each trace is kept

In each country folder:
- `drafts/`: every brief (`_brief.md`, `_writer-brief.md`, `_verifier-brief*.md`, `_coverage-brief.md`, `_resume*.md`, `_q-brief.md`), research findings (`<X>-findings.md`), writer parts (`part-<N>.md`), `_blocked-pages.md`, and doc snapshots before each round (`doc-r0.md`, `doc-before-*.md`).
- `verify/`: checker outputs (`r<round>-<N>.md`), the line lists they were given (`r<round>-lines-<N>.txt`), coverage (`coverage.md`, `cov-1.md`), gap and hand-saved-file edits (`k-inserts.md`, `m-inserts.md`, `q-*.md`), restore (`restore-1.md`), and in Italy and Kuwait the doc snapshots.
- `work/<X>/`: each agent's own `sources/` (with `_fetchlog.csv`), `sources.csv`, `facts.csv` and its JSON batches and logs; `work/*.py` are the merge, apply, question and batch scripts.
- `manual/`: files saved by hand from blocked sites.
- `sources/`, `sources.csv`, `facts.csv`: the merged evidence (rebuilt by merge.py; ZZ facts added by hand afterwards).
- `notes.md`: searches, conflicts, practice, facts not used, blocked pages, and the "Writing and independent check" record of rounds and decisions.

The Prothom Alo passes are traced in `prothom-alo-archive/extract/` (outside this repo): specs, inputs (`in-*.jsonl`), drafts, `checked-*.json`, writer `out-*.md` and `-unused.json`, `fix-*.json` and `fixes-applied.json`, `keymap2.json`/`keymap3.json` (claim key to fact ids).

## 10. Audit: is everything in work/ also in the merged files?

Method: for each country, every row of each `work/<X>/sources/_fetchlog.csv` was looked up in the main `sources/_fetchlog.csv` by URL and by name (allowing merge.py's `-<x>` renames). Every file in `work/<X>/sources/` was matched by name or MD5 content hash. Every fact in `work/<X>/facts.csv` was looked up in the main `facts.csv` by normalised quote text (facts.py's own normalisation), then by id and claim. Nothing was moved or changed.

- Cambodia: 1,428 work facts, 0 only in work; 1,153 work files, 0 only in work; 1 fetch-log row whose files exist nowhere.
- Italy: 1,819 work facts, 0 only in work; 1,368 work files, 2 only in work; 0 such log rows.
- Kuwait: 1,557 work facts, 0 only in work; 1,404 work files, 1 only in work; 1 such log row.
- Kyrgyzstan: 1,105 work facts, 0 only in work; 999 work files, 0 only in work; 4 such log rows.

- **Facts:** every work fact is in the main `facts.csv` with the same id, claim and quote. Each main file has exactly one extra fact, ZZ0001 (the Welfare Board insurance notice), added by hand on 17 Nov 2026 and explained in `notes.md`.
- **Italy, files only in work:** `work/F/sources/esteri-ambdhaka-family-communique-2025-05-13.png` and `...-2025-05-19.png`, the original images of the Embassy's May 2025 family-reunification notices. The main folder has only the 19 May transcription (`...-05-19-transcript.md`), which facts cite. The 13 May image has no transcription and no fact. merge.py copies only files whose names start with a logged name, which is why the images stayed behind.
- **Kuwait, file only in work:** `work/M/sources/amiridiwan-decree-114-2024-summary-user.html`. It isn't in any fetch log, and no fact or note refers to it.
- **Fetch-log rows whose files exist nowhere** (no fact cites any of them): Cambodia `work/W` `dfdl-kh-p62335` (https://www.dfdl.com/?p=62335). Kuwait `work/G` `bb-exchange-rate-2026-11-09` (Bangladesh Bank exchange-rate page). Kyrgyzstan `work/L` `spinform-kg-labour-code-2025`, `continent-kg-doc-30296269`, `news-tbsbangla-kyrgyzstan-399186` and `ombudsman-kg-home`. The logs say these were fetched with files, so the files were probably deleted or renamed after logging.
- So the merged folders hold all the evidence the docs rely on. The four `work/` folders could be dropped from future commits without losing a fact, apart from the three stray files above if anyone wants them.

## 11. One place for pass traces

Started on 23 Nov 2026 with the Prothom Alo passes, which now live in `passes/` (see passes/README.md). Existing country folders are unchanged; the rest of this section is the proposal for future passes.

Today the traces of a country's first build sit in `drafts/`, `verify/` and `work/`, sorted by file type, with rounds told apart only by file-name prefixes. Later passes add more prefixes to the same folders (`k-`, `m-`, `q-`, `restore-`). The archive passes live outside the repo altogether. Proposal:

- **One folder per pass:** `passes/<yyyy-mm-dd>-<slug>/` at the repo root (for example `passes/2026-11-11-cambodia-build/`, `passes/2026-11-20-prothom-alo-malaysia/`). Root level because passes often touch several docs.
- **Inside each pass folder:**
  - `PASS.md`: the goal, docs touched, fact prefixes used, agent roles, rounds with failure counts, decisions, and when and why it stopped.
  - `briefs/`: the specs exactly as given.
  - `drafts/`: findings, claims and parts.
  - `checks/`: one file per checker per round, plus the line lists.
  - `fixes-applied.json`: every fix applied, overruled or not found, with its round.
  - `scripts/`: the exact versions run.
  - Inputs too large for git (article dumps) stay outside, with a checksum and path in `PASS.md`.
- **A prefix register,** `passes/README.md`: every fact prefix, which pass created it, and what it covers.
- **Merged evidence stays where it is:** `sources/`, `facts.csv`, `notes.md`. A country's `notes.md` links each "Writing and independent check" entry to its pass folder.
- **Per-agent work folders** are transient staging. After a clean merge and this audit they need not be committed (the `work/` folders across all countries hold about 5,250 tracked files), which also helps the repo-size problem in `plans.md`.
- **One format for checker output** across country and archive passes. The JSON `{old_str, new_str, problem}` form applies more safely (it refuses ambiguous matches; apply.py silently replaces the first match). Keep a `round` field in every entry.
- **Existing folders stay where they are;** a short `PASS.md` for each past pass can point to them.
