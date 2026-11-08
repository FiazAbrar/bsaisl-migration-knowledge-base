# BSAISL Migration Pathway Navigator: knowledge base

Context and rules for researching and writing the country docs. Read this in full before doing any work.

## The project

BSAISL (BRAC Student AI Solutions Lab) is run by BRAC IT. The Migration Pathway Navigator aims to give people who want to work abroad one legitimate channel for information, so brokers have no gap to fill. It works alongside the government's process for going abroad (the Overseas Employment Platform, OEP, run by BMET, the Bureau of Manpower, Employment and Training); it doesn't replace it.

By 3 December 2026 the Navigator is to have four parts, tested with users over several rounds:
1. Assessment of the person's situation.
2. Corridor information for all major destination countries.
3. Document fraud flags, plus guidance to verify documents with the issuing authority.
4. Service information: loans, training and recruitment, starting with BRAC's own.

It will be delivered mainly through WhatsApp, maybe a website; the delivery model isn't final. A frontier LLM answers from a curated, sourced knowledge base. The users are aspirant migrants.

## Your job here: the country docs

The country docs are the knowledge base behind part 2. Readers, in order:
1. The team. We must understand the whole process for each country; our own comprehension comes first.
2. Corridor experts, who fact-check the doc.
3. The chatbot, which answers from it.

So each doc is an extensive, practical, step-by-step guide, not a summary and not a research dump.

Two drafts exist: Saudi Arabia (`countries/saudi-arabia/`) and Malaysia (`countries/malaysia/`). Both are directionally right but not finished, so neither is a standard to copy. The rules below are the standard. Each country gets its own folder under `countries/`.

## What's in this repo

- `countries/<country>/`: one folder per country, always with the same files:
  - `doc.md`: the doc's text, with each fact cited by its id in `facts.csv`. The only file you edit to change the doc.
  - `README.md` and `<Country>.docx`: the finished doc, built from `doc.md` (GitHub shows `README.md` when you open the folder). Never edit them by hand.
  - `facts.csv`: one row per fact used in the doc: the claim, the exact quote that supports it, which saved source it comes from, the page's date, whether the source is official or news, and its status. Some rows also carry a visa, field and value, so the chatbot can look facts up directly.
  - `sources.csv` and `sources/`: every source used. `sources/` holds a saved copy of each page or PDF with a text copy, so the evidence survives when links break; `sources.csv` lists them with publisher, title, URL, date and whether each is official.
  - `notes.md`: research notes: what was searched, conflicts between sources, what happens in practice, open questions, and pages we could not download.
- `agencies/`: the shared list of the most active recruiting agencies (`agencies.csv`), counted from BMET's permission letters, with cited red flags, and a readable doc built the same way as a country doc. Country docs name an agency's flags from here.
- `tools/`: the shared scripts every country uses. Run them from inside your country folder.
- `official-pdfs/`: official Bangladesh-side documents. Most apply to every country: the Ministry of Expatriates' Welfare citizen charter, the Wage Earners' Welfare Board citizen charter and annual report, the Probashi Kallyan Bank (PKB) loan page and charter, and BMET's safe migration leaflet. The rest are Saudi-specific BMET notices (skill test, permission letter, Takamol warning), useful as examples of what to look for.
- `data/oep-agency-list-2026-10-28.csv`: BMET's full recruiting-agency licence list (licence, name, address, phone, status, expiry), pulled 28 Oct 2026.

## Format (settled: fix quality inside it, don't redesign it)

- One self-contained doc per country. Call it a "doc", not a "page". The Bangladesh-side steps (OEP, training at Technical Training Centres, police clearance, pre-departure orientation, BMET clearance, PKB loans, Welfare Board, insurance, coming home) sit where they happen in the journey. There is no separate "Leaving Bangladesh" doc.
- First, a **Background** section: the corridor's big picture, so the reader has the framework before the steps. Same five parts in every country, each opening with its answer in a sentence or two:
  0. *In one minute*: a short plain story of how the corridor works and what it means for the reader, written last. Someone who reads only this should understand the landscape.
  1. *Is it open now, and who can go?* A dated status line; the channels and the one most people use; who qualifies (age, sex, skill test); the size of the flow; what has closed it before.
  2. *How a job reaches you, and who takes a cut*: from the root (the quota or sponsorship that turns a job into a visa that can be sold) down the chain to the village; this corridor's choke point and who controls it. Name people and companies when it's necessary and useful to the reader, not otherwise; allegations are attributed and dated.
  3. *What you pay, and what you earn and keep*: the legal cap against what people really pay, how they pay, what the job pays after deductions, and how long the debt takes to repay.
  4. *What ties you to the employer*: one line each on whether you're tied to the employer to enter, renew, quit, change employer and leave; which law covers which jobs; what running away or an expired pass does to you.
  5. *What goes wrong most, and what people wrongly believe*: the top complaint types, common beliefs set against the facts, and how the irregular routes end.
  The Background explains; the steps instruct. Don't repeat a fact the steps already give: point to the step.
- Then every visa open to Bangladeshis, the most-used first. Then a short list of the visas not open to Bangladeshis, each with why it's closed.
- H2 per visa. Under it, H3 "Step 1", "Step 2"... in the order a worker acts, written as numbered actions. Then procedures for problems: if you aren't paid, changing employer, being reported absent (or the country's equivalent), leaving at the end of the job, going home on leave, bringing family, scams.
- After the visas: changing visa type; asylum; sending money home; going home without valid papers; if a worker dies, is injured or loses the job; coming home; contacts.
- Sections a migrant needs even though no source frames them that way: rights at work, how long you can stay, what can get you jailed.
- Sharp writing: every line earns its place and says the most in the fewest words. **Form follows function**: pick the shape the content has and the reader's use of it, never what looks tidy. Actions done in order are numbered steps; things a reader scans, compares or checks off (documents to bring, fees, options, the people named, a timeline) are a list, nested only when an item has parts the reader needs; an explanation of why or how something works is prose, because the connections are the point; a single fact is a sentence. No tables.
- Explain every term, acronym, organisation and platform inline the first time it appears. No glossary.
- Every sentence is cited. `[n]` is an official source. `[Nn]` is news, an NGO, a guide or another third party, listed under "Needs an official source". A source older than 2025 shows its year, like `[N3 (2022)]`. Prefer official sources; don't cite news where an official source exists.
- No conclusions, opinions or advice of our own.
- Gaps go in their own block right after the paragraph or step they belong to, never buried mid-paragraph: a quote block headed **Need to know**, with one bullet per precise question an insider could answer in a line:

  > **Need to know**
  > - Is there a public list of registered sub-agents a worker can check a broker's name against?
- Output: an editable .docx with a clickable Contents list and citations that link to their reference.
- English only. Write "people", "workers" or "migrants", never "beneficiaries".

## Quality rules

- **The bar: worth an insider's time.** Every section will be read by people who live this: recruiting agency staff, returnee workers, brokers' victims, embassy and NGO caseworkers. They know what's real and can spot a generic, five-minute-research answer at once. Write so they recognise what they know, including what they've never seen written down: the real mechanics (how a visa is actually bought and resold, who takes which cut, what a medical "slip" or a "calling visa" means in practice), the street price next to the official one, the words people actually use, and the tricks that catch people. Specific beats general: names, numbers, places, dates, the exact counter or form. No advice anyone could have guessed. Where we don't know, ask a precise question an insider can answer in one line ("**Need to know:** what does a Saudi house-driver visa sell for in Dhaka in 2026?"), so their review fills the gap.
- **Say how.** Every instruction ("go to", "ask", "check", "apply") says how: where exactly, what to bring, what to type or say, what it costs, and what you get back. "Ask relatives whether their company is hiring" or "go to the agency's office" is useless on its own. "Check the agency is on OEP" is weak too: most agencies are listed, and listed agencies also cheat. If you can't find the how, write a "Need to know", never a bare instruction. Saudi step 1 shows the idea (the relative's-company route, the BMET permission letter, paying by cheque, the complaint route).
- **Prune fluff relentlessly; never cut substance.** Substance is anything that changes what a migrant does, or explains the forces acting on them: who controls the system, the scams and syndicates, real costs, bans, rights. Fluff is everything else: repeated explanations, filler, hedges, research narration, trivia, and statistics or anecdotes with no bearing on a decision. Cut fluff without mercy. Big-picture context goes in Background, once, not scattered through the steps.
- **A guide, not a research log.** Research as hard as you can; write the doc as a clean guide. The doc tells someone what to do, in order, and states each rule once, in its current form, with its citation. Everything behind it (source dates, conflicts between sources, what a search found or didn't, statistics, "source X says") goes in `facts.csv` and `notes.md`, never in the doc. A conflict shows in the doc only as one "Need to know" line, and only if it changes what someone would do. Don't add labels like "unofficial": the `[Nn]` citation already marks a news source.
- **No lazy gaps.** "No source gives X" is not acceptable. Before writing any "Need to know", search official sites, Bangla news, agency guides, NGO reports and embassy pages.
- **What works in practice.** An official line such as "contact the embassy" doesn't show it helps. Look for evidence of what actually happens to workers.
- **Recommend only what has evidence it helps.** There is no public rating of recruiting agencies. Don't name an agency without outside evidence. In Saudi, Bonanza Overseas (RL-0579) is named because of an ILO-backed fair-recruitment pilot; nothing else qualified.
- **Attention to detail.** Do a line-by-line pass before handing anything over: every name explained, every sentence cited, every citation going to a source that says what the sentence says.
- **Read official PDFs in full,** page by page if the text layer garbles the Bangla.
- **Never stop at the first answer.** Research every step more deeply than feels necessary.

## Research process

1. **Split the research by topic:** the main work route; every other visa (visit, family, tourist, student, pilgrimage and so on), visa change, asylum and children; the Bangladesh side and corridor numbers; scams and how to check each document is real. Subagents can run these in parallel.
2. **Keep the evidence.** Save every page and PDF you use into `sources/` with `fetch.py`, and register it with `facts.py source`. Log every fact with `facts.py add`: it records the claim and the exact quote, and refuses a quote that isn't in the saved file, so nothing is written from memory. Cite the id it prints in `doc.md`. A page older than 12 months or with no visible date is "possibly outdated" until you find its date or a newer source.
3. **Check every fact against official sites,** and cross-check conflicts between sources. Keep the newer or official one, and record unresolved conflicts as "Need to know".
4. **Practical pass:** Bangla news, government surveys, NGO and research reports, agency guides and worker forums, in five areas: recruitment and real costs; tests and documents; life and problems in the country; leaving and coming home; non-work visas. Keep notes in `notes.md`.
5. **Official documents.** Start with the PDFs in `official-pdfs/`. BMET posts its permission letters for each job order (agency, employer, job, salary, the most the agency may take) at bmet.gov.bd/pages/miscellaneous-infos; search there for your country. Ministry and BMET PDFs hosted on objectstorage.ap-dcc-gazipur-1.oraclecloud15.com download directly; find them by searching "office-bmet" or "office-wewb".
6. **Destination-side sources:** the country's labour and immigration ministries, its visa portal, the medical-check operator, the Bangladesh embassy's labour wing, and other countries' embassy labour pages (in Saudi, the Indian Embassy's were the most complete).
7. **Sites that block automated reading** (several .gov.bd sites, some visa and test portals, some news sites): try Firecrawl. If that fails, list it under "Pages we could not download" in `notes.md` and ask a teammate to download it in a browser. Never skip a source because it's blocked.
8. **Independent check (fact-check).** Before handing over, have verifier agents that haven't seen the research check every sentence against its cited source, then every number (fees, durations, validity, dates, quotas), then coverage against the destination's official visa list. Fix every failure and repeat until none remain.
9. **Audit the finished doc three times.**
   - From the migrant's questions: how long can I stay, what will I earn, what are my rights at work, what gets me jailed, bank account and SIM, pension, can my family come, what can I bring home.
   - Against the original aim: (1) per visa: types, requirements, where to apply, cost, processing time, appeal if refused, scams both ways (done to the migrant and tried by the migrant), can the holder work, claim asylum, have a child, bring a spouse; (2) changing visa type; (3) asylum, written to discourage; (4) corridor information: Bangladesh numbers compared with other countries, bans, growth opportunities.
   - The insider test: list what a journalist covering the corridor, a corridor expert and a returnee worker would expect to find (the big names and companies, scandals and syndicates, crackdowns and bans, typical real costs, common scams), and check each is in the doc. Also review every fact logged in `facts.csv` but not cited in `doc.md`: was it left out for a good reason?

## Tools and building the doc

Needs Python 3 and pandoc (`brew install pandoc` on a Mac). Every script is in `tools/` and runs from inside your country folder, for example `cd countries/<country>` then `python3 ../../tools/build.py`. Each script explains its options at the top of the file.

- `fetch.py <url> <name>`: saves a page or PDF into `sources/` with a text copy, and refuses a URL already saved. `wayback.py <url> <name> official|news` gets an archived copy of a page that won't load.
- `facts.py source` registers a saved source in `sources.csv`; `facts.py add` adds a fact to `facts.csv` and checks its quote; `facts.py cited doc.md` lists the facts behind a stretch of the doc, for checking. Give each person or agent working at the same time its own `--prefix` letter, so fact ids never clash.
- `datepass.py` looks for real dates on undated or old sources.
- `build.py` turns `doc.md` into `README.md` and `<Country>.docx`. It numbers sources in order of first use (official `[n]`, news `[Nn]`), adds the year to sources older than 2025, links each citation to its reference, writes the reference list and the Contents list, and stops if a citation has no fact behind it.

Commit `README.md` and the .docx with `doc.md`. For a Google Doc, upload the .docx to Drive and open it with Google Docs. Edit `doc.md` and rebuild rather than editing the Google Doc, because citations added by hand there won't link.

## Firecrawl (web scraping that gets past many blocks)

In a terminal:

```
claude mcp add --transport http firecrawl https://mcp.firecrawl.dev/v2/mcp-oauth
claude mcp login firecrawl
```

Restart Claude Code after logging in.

## Version control

This folder is a git repository. Commit after each meaningful change (a section researched, a batch of sources added, a rebuild) with a message that says what changed. Commit `doc.md`, `facts.csv`, `sources.csv`, `sources/`, `notes.md`, `README.md` and the .docx together, so they never drift apart. Never commit passwords or personal data about migrants.
