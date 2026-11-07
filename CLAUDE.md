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

Saudi Arabia is finished as the worked example (`countries/saudi-arabia/`). Match its format, depth and citation style. Each country gets its own folder under `countries/`.

## What's in this repo

- `countries/saudi-arabia/Saudi Arabia.docx`: the finished Saudi doc. Read it in full before writing anything.
- `countries/saudi-arabia/`: also its markdown source (`saudi.src.md`), reference lists (`saudi-ref-list.md`, `refs_extra.py`), build scripts (`build.py`, `fixbullets.py`), the readable copy of the doc (`README.md`, which GitHub shows when you open the folder) and the research notes (`findings.md`).
- `official-pdfs/`: official Bangladesh-side documents. Most apply to every country: the Ministry of Expatriates' Welfare citizen charter, the Wage Earners' Welfare Board citizen charter and annual report, the Probashi Kallyan Bank (PKB) loan page and charter, and BMET's safe migration leaflet. The rest are Saudi-specific BMET notices (skill test, permission letter, Takamol warning), useful as examples of what to look for.
- `data/oep-agency-list-2026-10-28.csv`: BMET's full recruiting-agency licence list (licence, name, address, phone, status, expiry), pulled 28 Oct 2026.

## Format (settled: fix quality inside it, don't redesign it)

- One self-contained doc per country. Call it a "doc", not a "page". The Bangladesh-side steps (OEP, training at Technical Training Centres, police clearance, pre-departure orientation, BMET clearance, PKB loans, Welfare Board, insurance, coming home) sit where they happen in the journey. There is no separate "Leaving Bangladesh" doc.
- Every visa open to Bangladeshis, the most-used first.
- H2 per visa. Under it, H3 "Step 1", "Step 2"... in the order a worker acts, written as numbered actions. Then procedures for problems: if you aren't paid, changing employer, being reported absent (or the country's equivalent), leaving at the end of the job, going home on leave, bringing family, scams.
- After the visas: changing visa type; asylum; sending money home; going home without valid papers; if a worker dies, is injured or loses the job; coming home; the country as a destination (corridor information); contacts.
- Sections a migrant needs even though no source frames them that way: rights at work, how long you can stay, what can get you jailed.
- Short dense paragraphs under bold labels. Few bullets, and never one-fact-per-bullet lists.
- Explain every term, acronym, organisation and platform inline the first time it appears. No glossary.
- Every sentence is cited. `[n]` is an official source. `[Nn]` is news, an NGO, a guide or another third party, listed under "Needs an official source". A source older than 2025 shows its year, like `[N3 (2022)]`. Prefer official sources; don't cite news where an official source exists.
- No conclusions, opinions or advice of our own.
- Gaps go inline as "**Need to know:** ...", at the step they belong to.
- Output: an editable .docx with a clickable Contents list and citations that link to their reference.
- English only. Write "people", "workers" or "migrants", never "beneficiaries".

## Quality rules

- **Say how.** Every instruction ("go to", "ask", "check", "apply") says how: where exactly, what to bring, what to type or say, what it costs, and what you get back. "Ask relatives whether their company is hiring" or "go to the agency's office" is useless on its own. "Check the agency is on OEP" is weak too: most agencies are listed, and listed agencies also cheat. If you can't find the how, write a "Need to know", never a bare instruction. See Saudi step 1 for the standard (the relative's-company route, the BMET permission letter, paying by cheque, the complaint route).
- **Actionable, not a dump.** Keep only what a migrant needs to act, or to understand how the system works. Cut statistics, anecdotes, studies, history and "source X says" lines unless they change what someone would do. Finding something is no reason to include it. The exception is the destination section, which carries the corridor numbers.
- **A guide, not cited facts.** The doc tells someone what to do, in order. A list of facts with citations misses the point.
- **No lazy gaps.** "No source gives X" is not acceptable. Before writing any "Need to know", search official sites, Bangla news, agency guides, NGO reports and embassy pages.
- **What works in practice.** An official line such as "contact the embassy" doesn't show it helps. Look for evidence of what actually happens to workers.
- **Recommend only what has evidence it helps.** There is no public rating of recruiting agencies. Don't name an agency without outside evidence. In Saudi, Bonanza Overseas (RL-0579) is named because of an ILO-backed fair-recruitment pilot; nothing else qualified.
- **Attention to detail.** Do a line-by-line pass before handing anything over: every name explained, every sentence cited, every citation going to a source that says what the sentence says.
- **Read official PDFs in full,** page by page if the text layer garbles the Bangla.
- **Never stop at the first answer.** Research every step more deeply than feels necessary.

## Research process

1. **Split the research by topic:** the main work route; every other visa (visit, family, tourist, student, pilgrimage and so on), visa change, asylum and children; the Bangladesh side and corridor numbers; scams and how to check each document is real. Subagents can run these in parallel.
2. **Check every fact against official sites,** and cross-check conflicts between sources. Keep the newer or official one, and record unresolved conflicts as "Need to know".
3. **Practical pass:** Bangla news, government surveys, NGO and research reports, agency guides and worker forums, in five areas: recruitment and real costs; tests and documents; life and problems in the country; leaving and coming home; non-work visas. Keep notes in a `findings.md` like Saudi's.
4. **Official documents.** Start with the PDFs in `official-pdfs/`. BMET posts its permission letters for each job order (agency, employer, job, salary, the most the agency may take) at bmet.gov.bd/pages/miscellaneous-infos; search there for your country. Ministry and BMET PDFs hosted on objectstorage.ap-dcc-gazipur-1.oraclecloud15.com download directly; find them by searching "office-bmet" or "office-wewb".
5. **Destination-side sources:** the country's labour and immigration ministries, its visa portal, the medical-check operator, the Bangladesh embassy's labour wing, and other countries' embassy labour pages (in Saudi, the Indian Embassy's were the most complete).
6. **Sites that block automated reading** (several .gov.bd sites, some visa and test portals, some news sites): try Firecrawl. If that fails, ask a teammate to download the page or PDF in a browser. Never skip a source because it's blocked.
7. **Audit the finished doc twice.**
   - From the migrant's questions: how long can I stay, what will I earn, what are my rights at work, what gets me jailed, bank account and SIM, pension, can my family come, what can I bring home.
   - Against the original aim: (1) per visa: types, requirements, where to apply, cost, processing time, appeal if refused, scams both ways (done to the migrant and tried by the migrant), can the holder work, claim asylum, have a child, bring a spouse; (2) changing visa type; (3) asylum, written to discourage; (4) corridor information: Bangladesh numbers compared with other countries, bans, growth opportunities.

## Building the .docx

Needs Python 3 and pandoc (`brew install pandoc` on a Mac). For a new country, copy the scripts from `countries/saudi-arabia/` into `countries/<country>/`. Write `<country>.src.md` with citation keys (`[12]` official, `[N104]` news, several as `[N2, N108, 14]`). Put your own references in a ref-list file with the same structure as `saudi-ref-list.md`: official entries as `12. Publisher. [Title](url)`, then "### Needs an official source" with `- N104. ...` entries. Adapt `build.py`: it reads `saudi-ref-list.md`, loads `refs_extra.py` and has a few Saudi overrides hard-coded, so strip those and point it at your files. Then, inside that folder:

```
python3 build.py                              # <country>.src.md -> pandoc.md and README.md
pandoc pandoc.md -o "<Country>.docx"
python3 fixbullets.py "<Country>.docx"
```

`build.py` renumbers citations in order of first use, adds the year to pre-2025 sources, links each citation to its reference and builds the Contents list. It writes two copies of the text: `pandoc.md`, a build file pandoc turns into the .docx (not committed), and `README.md`, which GitHub displays with working links when you open the country folder. Commit `README.md` with the .docx. It stops if a citation key has no reference. For a Google Doc, upload the .docx to Drive and open it with Google Docs. Edit the source and rebuild rather than editing the Google Doc, because citations added by hand there won't link.

## Firecrawl (web scraping that gets past many blocks)

In a terminal:

```
claude mcp add --transport http firecrawl https://mcp.firecrawl.dev/v2/mcp-oauth
claude mcp login firecrawl
```

Restart Claude Code after logging in.

## Version control

This folder is a git repository. Commit after each meaningful change (a section researched, a batch of sources added, a rebuild) with a message that says what changed. Commit the source, the reference list, findings.md and the rebuilt .docx together, so they never drift apart. Never commit passwords or personal data about migrants.
