Adding Prothom Alo reporting to a global doc: spec (one agent reads, logs and writes)

Global docs apply to every destination country. Their readers include recruiting-agency staff, returnee workers and caseworkers, who can tell real ground-level knowledge from generic advice. The chatbot that advises migrants answers from them.

Repository: /Users/rarba/Programming/brac/bits-migration/kb-modules (a git worktree). Global docs live in global/: faq, dalal-scams, departure, illegal-routes, money (sending money home), services (services for migrants and their families). Your doc folder is given in your instructions; edit only that folder. Run no git commands.

Read first:
- The repository's CLAUDE.md in full ("Format" and "Quality rules" are binding; the Background/visa structure is for country docs only).
- Your doc.md in full. If it is new or nearly empty, also read the headings of the other global docs and the sections of global/faq/doc.md that touch your topic, so your doc does not contradict them; where the FAQ answers a question briefly, your doc gives the full picture.

Input: a .jsonl file of Bangla Prothom Alo articles (2024 to Nov 2026), one per line: id, url, published, headline, earlier_summary (a pointer only; it has errors), text (the full Bangla article). The articles were routed to your doc by topic; some will also carry facts for other docs.

Goal: every usable fact in EVERY article ends up in a doc, cited. Full coverage, not a selection.

Steps
1. Read every article IN FULL, one at a time with Python (print in slices if long). Never work from the headline or summary alone.
2. Decide what each article adds that your doc lacks: rules and how they work in practice (where to go, what to bring, the cost, how long, what you get back); real costs and who takes them; what goes wrong, with dated cases (who, where, what, how much, what happened); services and whether help actually reached people; numbers that bear on a decision or explain the forces at work (with period and source); named actors with the allegation and who made it. Many articles repeat the same monthly figure or speech: use the newest or most specific, and record the others as duplicates in the ledger.
3. Log the evidence. For each article you use, from inside your doc folder:
   python3 /Users/rarba/Programming/brac/bits-migration/prothom-alo-archive/extract/kb4/save_pa.py . <article id>
   prints the source name. Then for each fact:
   python3 ../../tools/facts.py add --prefix <your prefix> --name <source name> --claim "<one self-contained English sentence>" --quote "<exact Bangla passage, contiguous, at most 300 characters>" --page-date <published date> --status unofficial
   The tool refuses a quote not in the saved text; re-copy it programmatically from the article text, never retype it (the text mixes Unicode forms). The claim says only what the article states, with its attribution ("the minister said", "according to the family", "police said"), and numbers, dates, names exactly as printed. Never infer or generalise.
4. Write into doc.md, citing the ids [XX0001]. In an existing doc, use its structure and add H2/H3 sections where content needs them. In a new doc, start with "## In one minute" (a short plain story of how this area works for a migrant, written last), then H2 sections by what a migrant needs to decide or do, H3 below them (at most H4). Follow the Format rules: the shape the content has (numbered actions, lists for things scanned, prose for how something works); attribution kept so allegations never read as established; dated statements for things that change; every acronym and organisation explained at first use; no advice or conclusions of our own; gaps as "Need to know" blocks with precise questions. If an article conflicts with the doc, keep the doc's sourced statement, add the new one dated and attributed, and a "Need to know" bullet if it changes what someone would do. Where an article answers an existing "Need to know", answer it and remove the bullet. Cross-references use exact heading text; for another doc write: see "<exact heading>" in the <doc title> doc.
5. Facts that belong in another global doc or in one country's doc: do NOT write them there (other agents are editing those); record them in the ledger's held list with an exact quote.
6. Build: from your folder run python3 ../../tools/build.py; fix every error it reports. Delete any .pdf it makes.
7. Line-by-line pass over everything you added: each sentence matches its cited facts (number, date, name, place, who said it), no attribution dropped, no two cases merged, every cross-reference uses an exact heading.

Resolve conflicts yourself before leaving them open: find where each figure comes from (open the saved sources and read the passages). A primary document (an official letter, circular, notice or page, or a news report that quotes one directly) beats a secondhand summary; a specific, dated figure beats a vague or later restatement; an obvious misprint (a transposed digit) is not a conflict. Keep the winning statement, stop citing the losing one, and record the reasoning in notes.md under "Resolved conflicts". Only a conflict you truly cannot settle from the sources becomes a "Need to know", and your final message must say why it could not be settled.

Ledger JSON at the output path given: {"articles": [{"article_id": "...", "used": true|false, "fact_ids": [...], "reason_if_unused": "...", "held": [ {"target": "<global doc folder or countries/<country>>", "claim": "...", "quote": "..."} ]}]}. Every input article appears once. "Unused" needs a reason (duplicate of fact <id>; no usable fact).

Scratch files only under /tmp/<your prefix>/; no network requests; no sub-agents; do not edit any other folder.

Final message, at most 6 lines: articles read, articles used, facts logged, sections added or changed, items held for other docs, anything a human should decide.
