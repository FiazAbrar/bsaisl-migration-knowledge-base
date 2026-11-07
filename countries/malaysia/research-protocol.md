# Malaysia research protocol (binding for every researcher)

Read `../../CLAUDE.md` in full first. Then read this. Today is **6 November 2026**.

## Source rule (Malaysia addendum, revised 6 Nov 2026)

- **Official sources first:** Malaysian government (immigration, home affairs, human resources, labour, social security, the medical operator), Bangladesh government (MOFA, BMET, Expatriates' Welfare Ministry, Welfare Board, Police, Passport Dept), the Bangladesh High Commission in Kuala Lumpur, and visa operators officially named by them. International bodies count as official only for what they are the authority on (UNHCR for its own registration, World Bank for remittance prices).
- **Only after an official search has failed**, news, NGO, research, agency-guide or worker-forum sources may be used. They appear as `[N]` citations under "Needs an official source", as in the Saudi doc. Ledger status `lead`.
- **Never cite news where an official source exists.** If official and news conflict, show both and mark the official one as the rule (status `conflict` on both rows).
- **Exact facts** (fees, eligibility, documents, processing times, legal rules) with no official source: write "**Need to know:**" and say what was reported, labelled "unofficial, not verified". Ledger status `unofficial`.
- **Dates:** a page dated before 6 Nov 2025, or with no visible date, is `possibly-outdated`. Before keeping that flag, look for the page's date (page metadata, Last-Modified header, publication date). A `[N]` source older than 2025 shows its year.
- **Ledger columns:** id | claim | quote | url | access_date | raw_file | page_date | source_type (official/news) | status (verified / possibly-outdated / conflict / lead / unofficial) | note. Register a source before adding rows; source_type is taken from it.

## Fetching (in this order)

1. `python3 ../../tools/fetch.py <url> <name>`. It uses curl, saves `raw/<name>.html` + a cleaned `raw/<name>.md`, or `raw/<name>.pdf` + `raw/<name>.txt`, and logs it in `raw/_fetchlog.csv`. It refuses a URL already fetched and tells you the existing file: **never fetch the same URL twice**; check with `python3 ../../tools/fetch.py --find <part-of-url>`. Names: lowercase, e.g. `imi-plks-overview`, `bdhckl-labour-wing-services`, `bmet-malaysia-permission-2026-03`.
2. If curl fails, returns an empty shell (JavaScript-only page) or an error page: use **Firecrawl single-URL scrape only** (`mcp__firecrawl__firecrawl_scrape`, `formats: ["markdown"]`, `onlyMainContent: true`; for PDFs add `parsers: ["pdf"]`). **Never** use Firecrawl crawl, map, search, extract, agent, interact or monitor. Write the returned markdown to `raw/<name>.md` (first line: `SOURCE: <url> | scraped by Firecrawl <date> | page date: <date or undated>`), then `python3 ../../tools/fetch.py --log <url> <name> firecrawl`. (Load the tool with ToolSearch `select:mcp__firecrawl__firecrawl_scrape` if needed.)
3. If both fail: do **not** skip it. Add it to `blocked-parts/<PART>.md` as `- <exact URL> -> manual/<suggested-file-name>.<pdf|html> : what we need from it`, and carry on with other work. The lead will hand these to the user in one batch.
- To *find* URLs, use WebSearch (load with ToolSearch `select:WebSearch`), official site menus, sitemaps you fetch with curl, and links inside pages you saved. Searching is fine; Firecrawl search is not.
- Read official PDFs in full. If the text layer garbles Bangla, read the PDF page by page with the Read tool (`pages` parameter) and use `--no-quote-check --note "garbled text layer, p.N; quote transcribed from page image"`.
- Local files in `../../official-pdfs/`: copy one into raw first (`cp ../../official-pdfs/x.pdf raw/<name>.pdf && pdftotext -layout raw/<name>.pdf raw/<name>.txt`) then `python3 ../../tools/fetch.py --log <its official URL from countries/saudi-arabia/saudi-ref-list.md> <name> manual`.

## Evidence

- Every fact gets a ledger row: `python3 ../../tools/ledger.py add --part <P> --raw <name> --claim "..." --quote "..." --page-date ... --status ...` (see `python3 ../../tools/ledger.py` for help). The quote must be copied from the saved text file; the tool checks it is there and refuses otherwise. Keep quotes to the sentence(s) that actually prove the claim.
- Register each source once: `python3 ../../tools/ledger.py source --raw <name> --publisher "..." --title "..." --official yes|no --page-date ...`.
- For official facts a chatbot could query (fee, validity, eligibility, documents, processing time, where to apply, can work, can bring family, etc.) add `--visa "<visa/pass name>" --field <field> --value "<value>"` so it lands in facts.csv.
- Only touch **your own** part files: `ledger-parts/<P>.csv`, `ledger-parts/<P>.facts.csv`, `findings-parts/<P>.md`, `blocked-parts/<P>.md`. Never edit other parts, the doc, CLAUDE.md or the Saudi folder.

## What to look for (the "how")

The doc is a step-by-step guide for an aspirant migrant from Bangladesh. Match `countries/saudi-arabia/Saudi Arabia.md` (read at least its work-visa section first). For every instruction, find **where exactly, what to bring, what to type or say, what it costs, how long, what you get back**, and **how to check the document/visa/pass is real** (official status-check pages, what they show). Also find what goes wrong in practice and the official route to fix it. Research every step more deeply than feels necessary; never stop at the first answer; "no source gives X" is only acceptable after searching official sites in English, Malay (Bahasa Malaysia: e.g. *syarat, yuran, permohonan, semakan status, pekerja asing, majikan*) and Bangla.

## Findings notes

Write `findings-parts/<P>.md` as you go, like `countries/saudi-arabia/findings.md` but organised by the doc section/step it feeds. Each note cites ledger ids, e.g. `- PLKS max 10 years in total [W0012]`. End with:
- **Draft steps**: for each step in your sections, the numbered actions with the "how", citing ledger ids (this is what the doc will be written from).
- **Need to know**: each open gap, at the step it belongs to, with what you searched.
- **Conflicts**: pairs of ledger ids.
- **Blocked**: as in blocked-parts.

## Final report (your last message)

Keep it under ~1,200 words: counts (sources fetched, ledger rows by status), the 10-20 most important verified facts with ledger ids, every open Need to know, conflicts, and blocked URLs with suggested manual/ file names. The detail stays in your findings part.
