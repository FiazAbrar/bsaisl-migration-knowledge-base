Official-source research pass on a doc built from news: spec

The doc named in your instructions was built from Prothom Alo reporting only. Your job is the research pass the repository's CLAUDE.md requires: find the official sources, answer the doc's "Need to know" questions, and replace or back news claims with official ones where they exist. Readers include recruiting-agency staff, returnees and caseworkers; the chatbot answers from this doc.

Repository: /Users/rarba/Programming/brac/bits-migration/kb-research (a git worktree). Edit only your doc folder. Run no git commands. No sub-agents.

Read first: CLAUDE.md in full (Format, Quality rules and Research process are binding), then your doc.md, notes.md and questions.md in full.

Steps
1. Make a research list: every "Need to know" bullet in the doc, plus every rule, fee, deadline, office, address or number the doc states from news alone where an official source should exist (visa types and requirements, fees, processing times, work rights, embassy and consulate contacts, BMET clearance numbers for this destination, the destination's own immigration and labour pages).
2. Research each item on the web, official sources first: the destination government's immigration, labour and visa pages; the Bangladesh embassy or high commission there; BMET, the Ministry of Expatriates' Welfare, the Wage Earners' Welfare Board, PKB, Bangladesh Bank, NBR (for Bangladesh-side items); then international bodies (IOM, ILO, UNHCR) and reputable NGOs. For Bangladesh-side numbers, BMET's own statistics and the ministry's releases.
3. Save every page or PDF you use with the tool, from inside your doc folder:
   python3 ../../tools/fetch.py <url> <name>
   (it refuses a URL already saved). If a site blocks it, try python3 ../../tools/wayback.py <url> <name> official|news. If both fail, list the page in notes.md under "Pages we could not download" with the exact URL, what it should prove and a suggested file name; never skip it silently, never invent its content.
   Register each source: python3 ../../tools/facts.py source --name <name> --publisher "<publisher>" --title "<title>" --official yes|no --page-date <YYYY-MM-DD or undated>
4. Log every fact: python3 ../../tools/facts.py add --prefix <your prefix> --name <name> --claim "<self-contained English sentence>" --quote "<exact words from the saved text copy>" --page-date <date> --status verified|possibly-outdated|unofficial (see the tool's help: official and dated within 12 months is verified; official but older or undated is possibly-outdated). Read official PDFs in full.
5. Rewrite the doc where official facts change it: state each rule once, in its current official form, with its citation; where an official source confirms a news claim, cite the official fact (and drop the news citation if it adds nothing); where it contradicts one, the official source stands and the reasoning goes in notes.md under "Resolved conflicts". Answer each "Need to know" you can and remove its bullet; sharpen the ones you can't into a precise question, and only after a real search (no lazy gaps). Follow Format: steps as numbered actions that say how (where, what to bring, cost, time, what you get back), every acronym explained at first use, no advice of our own. Keep the doc's existing Prothom Alo material unless an official source supersedes it.
6. Build (python3 ../../tools/build.py), fix every error, delete any .pdf, then do a line-by-line pass over everything you added or changed.
7. Update questions.md with the sync script: python3 /Users/rarba/Programming/brac/bits-migration/prothom-alo-archive/extract/kb4/sync_questions.py . (it adds new bullets); remove from questions.md any question you answered.
8. notes.md: a section "Official research pass, <date>": what you searched, what you found, the resolved conflicts, the pages you could not download.

Final message, at most 8 lines: official sources added, facts logged, Need-to-know answered vs still open, the main changes to the doc, pages that need a human to download, and anything a human must decide.
