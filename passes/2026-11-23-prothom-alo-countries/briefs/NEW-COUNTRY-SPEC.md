Starting a new country doc from Prothom Alo reporting: spec (one agent reads, logs and writes)

You are starting a country doc for Bangladeshis who go, or are sold a way to go, to one country that has no doc yet. Its readers include recruiting-agency staff, returnee workers and caseworkers. The chatbot that advises migrants answers from it. This first version is built from Prothom Alo reporting only; a later research pass will add official sources.

Repository: /Users/rarba/Programming/brac/bits-migration/kb-countries (a git worktree). Your doc folder is given in your instructions; create it and edit only it. Run no git commands.

Read first:
- The repository's CLAUDE.md in full: "Format" and "Quality rules" are binding.
- The headings and Background of one finished doc of a similar kind as a model of structure only (for a work destination countries/qatar/doc.md, for an irregular or study destination countries/italy/doc.md), and the headings of the global docs in global/ (faq, dalal-scams, departure, illegal-routes, money, services): your doc covers what is specific to this country and points to the global docs for the rest (see "<exact heading>" in the <doc title> doc).

Set up the folder (from the repo root):
  mkdir -p countries/<slug>/sources
  copy the header line of countries/qatar/facts.csv, countries/qatar/sources.csv and countries/qatar/sources/_fetchlog.csv into the same files in your folder.
  doc.md starts with "# <Country>: migration guide" and the same one-paragraph legend as countries/qatar/doc.md line 3, adapted, and saying this version is built from Prothom Alo reporting and needs official sources.

Input: a .jsonl file of Bangla Prothom Alo articles (2024 to Nov 2026), one per line: id, url, published, headline, earlier_summary (a pointer only; it has errors), text (the full Bangla article).

Goal: every usable fact in EVERY article ends up in the doc, cited, in the standard country structure.

Steps
1. Read every article IN FULL, one at a time with Python (print in slices if long).
2. Log the evidence. For each article you use, from inside your folder:
   python3 /Users/rarba/Programming/brac/bits-migration/prothom-alo-archive/extract/kb4/save_pa.py . <article id>
   then for each fact:
   python3 ../../tools/facts.py add --prefix <your prefix> --name <source name> --claim "<one self-contained English sentence>" --quote "<exact Bangla passage, contiguous, at most 300 characters>" --page-date <published date> --status unofficial
   Re-copy quotes programmatically from the text, never retype them. Claims keep the article's attribution and its numbers, dates and names exactly.
3. Write doc.md in the country format: the Background (In one minute, written last; Is it open now, and who can go?; How a job reaches you, and who takes a cut; What you pay, and what you earn and keep; What ties you to the employer; What goes wrong most, and what people wrongly believe), then an H2 for each route the reporting shows people using (work visa, student visa, visit visa, irregular entry and so on), with steps only where the reporting gives them, then the later sections the reporting supports (if you aren't paid, if a worker dies, coming home, contacts, and so on). Include a section only when you have content for it; don't add empty sections for uniformity. Where the reader would need something the articles don't give (the official visa rules, fees, the embassy's address), write a precise "Need to know" bullet so the research pass knows what to find.
4. Resolve conflicts yourself: trace each figure to its source; a primary document (or a report quoting one) beats a secondhand summary; a specific dated figure beats a vague restatement; an obvious misprint isn't a conflict. Record reasoning in notes.md under "Resolved conflicts". Only a conflict you truly cannot settle becomes a "Need to know".
5. Facts that are not about this country (Bangladesh-side rules common to all countries, other countries) go in the ledger's held list with an exact quote, not in the doc.
6. Build: python3 ../../tools/build.py from your folder; fix every error; delete any .pdf.
7. Line-by-line pass: each sentence matches its cited facts, no attribution dropped, no two cases merged, no advice of our own, every acronym explained at first use, every cross-reference uses an exact heading.
8. notes.md: what this version is built from, the sources an official research pass should start with (the country's immigration and labour ministries, the Bangladesh embassy, BMET's clearance figures), and the resolved conflicts.

Ledger JSON at the output path given: {"articles": [{"article_id": "...", "used": true|false, "fact_ids": [...], "reason_if_unused": "...", "held": [ {"target": "<global doc folder or countries/<country>>", "claim": "...", "quote": "..."} ]}]}. Every input article appears once.

Scratch files only under /tmp/<your prefix>/; no network requests; no sub-agents; do not edit any other folder.

Final message, at most 6 lines: articles read and used, facts logged, the doc's sections, items held, anything truly unsettled.
