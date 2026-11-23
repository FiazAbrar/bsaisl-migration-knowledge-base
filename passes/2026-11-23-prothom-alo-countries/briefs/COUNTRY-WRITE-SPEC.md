Adding Prothom Alo reporting to a country doc: spec (simplified process, one agent reads, logs and writes)

You are improving one country doc for Bangladeshis who want to work in that country. Its readers include recruiting-agency staff, returnee workers and caseworkers, who can tell real ground-level knowledge from generic advice. The chatbot that advises migrants answers from this doc.

Repository: /Users/rarba/Programming/brac/bits-migration/kb-countries (a git worktree). Your doc folder is given in your instructions.

Read first:
- The repository's CLAUDE.md in full: sections "Format" and "Quality rules" are binding.
- Your doc.md: its heading list, then IN FULL every section you will add to. Add only what is new. Other agents may be editing OTHER country folders at the same time; never touch any folder but yours. Run no git commands.

Input: a .jsonl file of Bangla Prothom Alo articles (2024 to Nov 2026), one per line: id, url, published, headline, earlier_summary (a pointer only; it has errors), text (the full Bangla article).

Goal: every usable fact in EVERY article ends up in the doc, cited. Full coverage, not a selection.

Steps
1. Read every article IN FULL, one at a time with Python (print in slices if long). Never work from the headline or summary alone.
2. Decide what each article adds that the doc lacks: status and timelines (openings, closures, quotas, agreements, amnesties, deadlines); rules (visas, permits, medicals, tests, attestation, labour law, penalties); costs (official caps, what people actually paid and to whom, wages promised and paid, deductions); how things work in practice (where, what to bring, how long, who takes a cut); what goes wrong (unpaid or stranded workers, detention, deportation, deaths, compensation, bodies sent home), with numbers and cases; services and contacts and whether help reached people; numbers (departures, stock, remittances, deaths, returns, with period); named actors with the allegation and who made it.
3. Log the evidence. For each article you use, from inside your doc folder:
   python3 /Users/rarba/Programming/brac/bits-migration/prothom-alo-archive/extract/kb4/save_pa.py . <article id>
   prints the source name. Then for each fact:
   python3 ../../tools/facts.py add --prefix <your prefix> --name <source name> --claim "<one self-contained English sentence>" --quote "<exact Bangla passage, contiguous, at most 300 characters>" --page-date <published date> --status unofficial
   The tool refuses a quote not in the saved text; re-copy it programmatically from the article text, never retype it (the text mixes Unicode forms). The claim says only what the article states, with its attribution ("the minister said", "according to the family", "police said"), and numbers, dates, names exactly as printed. Never infer or generalise.
4. Write into doc.md, citing the ids [XX0001]. Use the doc's own structure: the Background parts and their H4s, the visa sections and steps, and the later sections (if you aren't paid, changing employer, leaving, sending money home, if a worker dies, coming home, contacts and so on). Follow the Format rules: the shape the content has (numbered actions, lists for things scanned, prose for how something works); attribution kept so allegations never read as established; dated statements ("in March 2025, ...") for things that change; every acronym and organisation explained at first use; cases kept specific (who, where, what, how much, what happened) but trimmed of trivia that changes nothing for a reader. New H3/H4 sections are fine when the content needs one (for example a "Cases" list under a problem section, or a section the doc lacks); place them where a reader would look. If an article conflicts with the doc (different figure, date or rule), keep the doc's sourced statement, add the new one dated and attributed, and add a "Need to know" bullet if the conflict changes what someone would do. Where an article answers an existing "Need to know" bullet, answer it in the text and remove the bullet. Where a fact is not specific to this country (Bangladesh-side rules common to all countries, general broker tricks), do NOT write it in this doc; record it in the hold file instead (below).
5. Build: cd to your folder and run python3 ../../tools/build.py; fix every error it reports (a citation with no fact, a broken cross-reference).
6. Line-by-line pass over everything you added: each sentence matches its cited facts (number, date, name, place, who said it), no attribution dropped, no two cases merged, no advice or conclusion of your own, every cross-reference uses an exact heading.

Resolve conflicts yourself before leaving them open: find where each figure comes from (open the saved sources and read the passages). A primary document (an official letter, circular, notice or page, or a news report that quotes one directly) beats a secondhand summary; a specific, dated figure beats a vague or later restatement; an obvious misprint (a transposed digit) is not a conflict. Keep the winning statement, stop citing the losing one, and record the reasoning in notes.md under "Resolved conflicts". Only a conflict you truly cannot settle from the sources becomes a "Need to know", and your final message must say why it could not be settled.

Account for every article. Write a ledger JSON to the output path given: {"articles": [{"article_id": "...", "used": true|false, "fact_ids": [...], "reason_if_unused": "...", "held_for_global": [ {"claim": "...", "quote": "...", "suggested_module": "faq|scams|departure|illegal-routes|other: ..."} ]}]}. Every input article appears once. "Unused" needs a reason (duplicate of a fact already in the doc: give that id; not about this country; no usable fact). Bangladesh-side or general facts go in held_for_global with an exact quote, so the global modules can use them later.

Scratch files only under /tmp/<your prefix>/; no network requests; no sub-agents; do not edit any other folder.

Final message, at most 6 lines: articles read, articles used, facts logged, sections added or changed (names), items held for global modules, anything a human should decide.
