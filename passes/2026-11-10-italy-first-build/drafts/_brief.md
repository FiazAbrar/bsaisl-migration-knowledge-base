# Italy research brief (shared by every topic agent, 10 November 2026)

You are one of ten research agents writing the Italy doc for the BSAISL Migration Pathway Navigator. Today is 10 November 2026. Repo root: `C:\Users\User\Desktop\Github\bsaisl-migration-knowledge-base` (below: ROOT).

## Read first (binding)

1. `ROOT\CLAUDE.md`: the project, format, quality rules and research process. Binding. Read it in full.
2. `ROOT\countries\malaysia\doc.md`: THE STANDARD. Imitate its depth, tone and step pattern. Read the Background (H3 parts with H4 topics), "Work visa: company worker (PLKS)" Step 1, the problem sections, and any section matching your topic. `ROOT\countries\kuwait\doc.md` is the newest doc (same rules) if you need a second example.

## The style (what the user approved)

- No SOP section. Procedures are written in place, in the step where they happen.
- Numbered actions, each starting with a bold verb: `1. **Register on OEP,** BMET's website for job-seekers ...`
- Under an action: `You'll need:` (documents, money, phone, photos), then click-by-click sub-steps as a nested numbered list (exact URL or portal, what to type, button names as on screen), then short bold labels where they apply: `**Check it is real:**`, `**If it fails:**`, `**Scams:**`.
- Ready-to-use wording where a worker must write or say something (sample in quotes with [blanks]).
- Escalation ladders: "If ..., in this order:" then numbered routes, each with phone, link or address.
- Headings: H2 per visa / big section, H3 per step or topic, H4 inside. Max H4; below that a bold lead-in. No dates in headings.
- Cross-references use the exact heading text: "(see If you aren't paid)", "(Step 1, item 4)", "(Work visa: Decreto Flussi worker, Step 3)". Never "see above".
- Every sentence ends with fact ids in brackets, e.g. `[W0012, N0003]`. No uncited sentence, and every list item that states a fact is cited too.
- Gaps: a quote block right after the paragraph or step, one precise insider question per bullet:
  ```
  > **Need to know**
  > - What does a fake Italian nulla osta sell for in Dhaka in 2026?
  ```
- Explain every acronym, organisation, platform and Italian term the first time you use it (nulla osta, permesso di soggiorno, Questura, Prefettura, SUI, codice fiscale, CCNL, INPS, patronato, caporalato ...). No tables. English only in the text. "workers", "people", "migrants", never "beneficiaries". No opinions, no advice of our own.
- State the latest status for Bangladeshis wherever it matters, dated: quotas, visa backlogs or suspensions at the Italian Embassy in Dhaka, fraud crackdowns on nulla osta, Bangladesh as a "safe country of origin" for asylum, any 2025-2026 change.
- Specific beats general: names, numbers, places, dates, the exact office, form, fee and phone. Write what an insider (agency staff, a Bangladeshi in Rome or Milan, a patronato caseworker, a returnee) would recognise as real.
- Money: give amounts in EUR as the source does. The lead adds Taka conversions (agent G logs the rate).

## Where you work (avoid file races)

Work ONLY inside your own staging folder: `ROOT\countries\italy\work\<YOUR LETTER>\` (it has an empty `sources/` folder). Run every tool from your folder with `python` (not python3), using the path `../../../../tools/`:

```
cd "/c/Users/User/Desktop/Github/bsaisl-migration-knowledge-base/countries/italy/work/<X>"
python ../../../../tools/fetch.py <url> <name>                 # saves sources/<name>.html|.pdf + text copy
python ../../../../tools/wayback.py <url> <name> official|news # archived copy from the Wayback Machine
python ../../../../tools/facts.py source --name <name> --publisher "..." --title "..." --official yes|no|archived|news-archived --page-date YYYY-MM-DD|undated
python ../../../../tools/facts.py add --prefix <X> --name <name> --claim "..." --quote "exact words from the saved text copy" --page-date YYYY-MM-DD|undated --status verified|possibly-outdated|conflict|unofficial|lead [--visa .. --field .. --value ..] [--note ".."]
```

- facts.py refuses a quote not found in the saved text copy: copy quotes exactly from `sources/<name>.md` or `.txt`. Keep quotes short and precise. The quote must prove the claim, including every number in it. One fact per number or rule.
- Status: official + dated within 12 months = verified; official older or undated = possibly-outdated; news/NGO/guide = unofficial (practice) or lead; conflicting sources = conflict, with a note naming the other id.
- Source names: lowercase, hyphens, start with the publisher (e.g. `interno-it-decreto-flussi-2026`, `esteri-vistoperitalia-lavoro`, `news-prothomalo-italy-visa-2026-05`). Make names specific so they don't clash with other agents.
- If several facts need adding, write a small Python script in your own folder that calls facts.py with subprocess and a list of arguments (shell quoting breaks on apostrophes and Bangla text).
- Never write to `countries/italy/facts.csv`, `sources.csv` or `sources/` directly, or to any other country's folder. Never commit. The lead merges your folder.
- Bangladesh-side pages already saved for other countries (OEP, BMET, PKB, WEWB, Ministry, passport, police clearance pages) may be copied from `ROOT\countries\kuwait\sources\` or `...\maldives\sources\` into your `sources/` (all files for that name), then logged with `python ../../../../tools/fetch.py --log <original url> <name> manual`. Prefer a fresh fetch when the page loads (fees change). Every fact must be logged again in your own facts.csv.
- Official PDFs in `ROOT\official-pdfs\`: read in full; to cite one, fetch its online original or copy it into your `sources/` and log it.
- Italian official pages are often in Italian only: quote the Italian exactly and put the English meaning in the claim. The Gazzetta Ufficiale (gazzettaufficiale.it) and Normattiva (normattiva.it) carry laws and decrees; the Ministry of the Interior (interno.gov.it), Ministry of Labour (lavoro.gov.it, integrazionemigranti.gov.it), Ministry of Foreign Affairs (esteri.it, vistoperitalia.esteri.it, ambdhaka.esteri.it), Polizia di Stato (poliziadistato.it, permesso di soggiorno), INPS, INAIL and ISTAT are official.

## Blocked pages and web archives

If fetch.py fails (403, timeout, empty text or a page that needs JavaScript), try in this order:
1. Firecrawl `mcp__firecrawl__firecrawl_scrape` with default settings only (load with ToolSearch "select:mcp__firecrawl__firecrawl_scrape"; formats ["markdown"]). Never use stealth or enhanced proxies, location spoofing or any other bot-check circumvention. Save the markdown with the Write tool to `sources/<name>.md` and log it with `fetch.py --log <url> <name> firecrawl`.
2. The Wayback Machine: `wayback.py <url> <name> official|news`. Also use it for pages that have been removed or changed, and to date undated pages.
3. If all fail, list the page under "c. Blocked pages" (exact URL, suggested file name, what it should prove). The lead will open these in a browser and the user downloads the rest by hand, so list every one that matters.
Do not use the Chrome browser tools; the lead uses the browser after you finish. Facebook posts of the Bangladesh Embassy in Rome, the Consulate General in Milan, the Italian Embassy in Dhaka or BMET count as official; list them under blocked pages with the exact post URL if you can't save them. Search with WebSearch (load via ToolSearch "select:WebSearch") or Firecrawl search, in English, Italian and Bangla.

## Key official sites (start here)

- Italy: Ministry of the Interior (interno.gov.it: Decreto Flussi, click day, nulla osta, asylum, CPR detention, statistics "cruscotto statistico giornaliero" for sea arrivals by nationality); the ALI portal (nullaostalavoro.dlci.interno.it) and the Sportello Unico per l'Immigrazione (SUI) at each Prefettura; Ministry of Labour (lavoro.gov.it; integrazionemigranti.gov.it, the official migrant guide portal, in several languages); vistoperitalia.esteri.it (visa finder by nationality and purpose); Italian Embassy in Dhaka (ambdhaka.esteri.it) and its visa service provider (VFS Global Italy in Bangladesh); Polizia di Stato / portaleimmigrazione.it (permesso di soggiorno kit at post offices); Agenzia delle Entrate (codice fiscale); INPS (pensions, contributions), INAIL (work accidents), Ispettorato Nazionale del Lavoro (labour inspections, caporalato); Commissione Nazionale per il Diritto di Asilo; Gazzetta Ufficiale and Normattiva (Testo Unico Immigrazione, D.Lgs. 286/1998; DPCM flussi 2023-2025 and 2026-2028; Decree-Law 145/2024 and 2025 decrees on flussi; safe-countries list).
- Bangladesh: Embassy of Bangladesh in Rome (rome.mofa.gov.bd) and Consulate General in Milan (milan.mofa.gov.bd), BMET (bmet.gov.bd, miscellaneous-infos), OEP (oep.gov.bd, country-clearance reports), Ministry of Expatriates' Welfare (probashi.gov.bd), WEWB, PKB, Bangladesh Bank (bb.org.bd, remittance by country), BOESL.
- Other sources: IOM Italy and IOM Bangladesh, UNHCR Italy (sea arrivals portal data.unhcr.org), Frontex, ISMU, Caritas/Migrantes "Rapporto Immigrazione", Fondazione Leone Moressa, Openpolis, ASGI (asgi.it), Melting Pot Europa (meltingpot.org, practical guides), Pakistani/Indian/Sri Lankan embassy pages in Italy, RMMRU, BRAC Migration, OKUP.
- News: Bangladeshi (Prothom Alo, Daily Star, TBS, Dhaka Tribune, bdnews24, Jago News, Samakal, Kaler Kantho, Bonik Barta, BBC Bangla) in English and Bangla (ইতালি ভিসা, ইতালির নুলাওস্তা, ইতালি দূতাবাস ঢাকা, ইতালি মৌসুমি ভিসা, ইতালিতে বাংলাদেশি, লিবিয়া হয়ে ইতালি ...); Italian (ANSA, Il Sole 24 Ore, Corriere, Repubblica, Avvenire, Redattore Sociale, InfoMigrants) in English and Italian.

## Time limit

About 40 minutes of research, then write your findings file even if some points remain open (list them as Need to know with what you searched). Quality over volume, but cover your whole topic. Don't stop at the first answer.

## Your output

Write `ROOT\countries\italy\drafts\<X>-findings.md` with:

- **a. Draft doc text:** your sections, written exactly as they should appear in doc.md (headings per the outline below), every sentence and fact-bearing list item cited with your fact ids. Where another agent's topic is needed, write "(see <exact section heading>)" rather than researching it.
- **b. Notes (for notes.md):** what you searched (sites and search terms, English, Italian and Bangla), conflicts between sources (with ids), what happens in practice, facts logged but not used and why.
- **c. Blocked pages:** exact URL, suggested file name, what it would prove (say if Wayback was tried).
- **d. Insider questions:** the open Need to know questions, one line each.

Final message back to the lead: 5-10 lines: number of facts and sources logged (official vs news), sections written, the most important findings, and anything the lead must decide.

## Who does what (letter = fact prefix)

- **N** corridor, chain and money in practice: Background drafts (Is it open now: status of each route for Bangladeshis on 10 Nov 2026, the channels and the one most people use, who qualifies, size, what closed or restricted it before (e.g. the 2023-24 nulla osta fraud scandal and Italy's response, Embassy backlogs, any suspension for Bangladesh); How a job reaches you, and who takes a cut: the quota, the employer and the click day, how a nulla osta is bought and sold, Italian middlemen and Bangladeshi brokers, the Dhaka visa queue; What you pay, and what you earn and keep: real costs (Tk lakh) vs any BMET cap, wages in practice, debt; What goes wrong most, and what people wrongly believe), the Decreto Flussi Scams section, agencies with evidence, corridor numbers (OEP/BMET clearances to Italy by year 2023-2026, Bangladeshis resident in Italy by ISTAT, visas issued, comparison with India, Pakistan, Sri Lanka, Egypt), the big names, scandals and crackdowns.
- **W** Italy-side work route (Decreto Flussi, non-seasonal and the general route): Work visa: Decreto Flussi worker Steps 2, 3, 5 and 7 (the job offer and contract; how the employer applies on the ALI portal on click day, pre-filling, the 2026-2028 quotas and click-day dates, labour-market check at the Centro per l'Impiego, nulla osta from the SUI; the visa application at the Italian Embassy in Dhaka / VFS, documents, fees, waiting times; checking a nulla osta and visa are real; arrival: contratto di soggiorno at the SUI within 8 days, permesso di soggiorno kit at the post office, Questura fingerprints, codice fiscale, residence registration, health service (SSN) enrolment, bank account, SIM), How long you can stay (permit length, renewal, converting seasonal to non-seasonal, long-term EU permit, citizenship after 10 years), Your residence permit; Work visa: highly skilled (EU Blue Card) and out-of-quota routes (Article 27 TUI: nurses, researchers, etc.), and self-employment visa.
- **B** Bangladesh side: Step 1 (OEP registration, whether BMET/BOESL has any G2G or agency route to Italy, Italy-Bangladesh migration MoU or agreement, cost caps if any, PKB loans, complaints to BMET), Step 4 (passport, police clearance, certificates, legalisation at MoFA and the Italian Embassy, dichiarazione di valore for degrees), Step 6 (PDO, BMET clearance for Italy, smart card, fees, welfare fee, flights), Coming home (WEWB, airport help desk), Bangladesh Embassy Rome and Consulate Milan services (passport, NID, power of attorney, death and body repatriation, legal help), contacts. OEP clearance numbers for Italy by year and month 2023-2026 (see countries\maldives\notes.md on getting OEP JSON).
- **L** law and work: Your rights at work (CCNL national contracts and their minimum pay for agriculture, construction, hotels and restaurants, cleaning, logistics; hours, overtime, leave, TFR severance, busta paga payslip, sick pay; INPS contributions; INAIL accident cover), What can get you jailed or deported (expulsion, CPR detention, overstaying, drugs, fake documents, working without a permit), If you aren't paid (Ispettorato del Lavoro, unions CGIL/CISL/UIL, patronati, labour court, step by step), Changing employer or leaving, Leaving at the end of the job, Going home on leave (re-entry rules, permit in renewal), If a worker dies, is injured or loses the job (INAIL, NASpI unemployment benefit, body repatriation), pension (INPS for a returning Bangladeshi: no social security agreement? refunds?).
- **D** seasonal and domestic/care work: Work visa: seasonal worker (agriculture and tourism quotas, 9-month limit, multi-year seasonal permits, conversion to non-seasonal) and Work visa: domestic and care worker (colf and badanti quotas, CCNL lavoro domestico, minimum pay, live-in rules); caporalato (illegal gangmaster labour) in agriculture, Law 199/2016, the Latina/Agro Pontino cases, special permit for victims of exploitation (Article 18/22 TUI), how Bangladeshis end up in these jobs, the Bangladeshi employers in Italy who sponsor workers.
- **U** irregular routes and status: the Libya/central Mediterranean route (Bangladeshis among the top nationalities arriving by sea 2023-2026, deaths, Libyan detention and ransom, the dalal networks and prices), Lampedusa and hotspots, CPR detention and repatriation, Bangladesh-Italy returns and readmission cooperation, IOM assisted voluntary return, past regularisations (the 2020 emersione and its outcome for Bangladeshis), Undocumented workers, Going home without valid papers, the Albania centres.
- **A** asylum (written to discourage, but accurate): how asylum works in Italy (Questura, Territorial Commission, interview, appeal), Bangladesh on Italy's list of safe countries of origin (date, decree, effect: accelerated and border procedures), recognition rates for Bangladeshis (Ministry/Eurostat), special protection (protezione speciale) and its 2023 restriction, the 2026 EU Pact on Migration and Asylum (in force June 2026: border procedure, return), reception centres and the right to work after 60 days, what happens after rejection, the European Court ruling on safe countries (August 2025).
- **V** visits and study: Schengen visit visa (tourist, business, family visit, medical) from Bangladesh through VFS Dhaka, documents, fees, appointment backlogs, refusal rates for Bangladeshis (EU Schengen visa statistics), transit; Student visa (Universitaly pre-enrolment, dichiarazione di valore/CIMEA, DSU regional scholarships, part-time work 20 hours a week, converting a study permit to a work permit after graduation), Visas not open to Bangladeshis (with why), Changing visa type (can a visitor or student switch to work?).
- **F** family and residence: Family reunification (ricongiungimento familiare: nulla osta at the SUI, income threshold based on the assegno sociale, housing suitability certificate, legalisation of nikahnama and birth certificates, the family visa at the Embassy in Dhaka, permits for family), Bringing your family, spouse of an Italian or EU citizen, Having a child in Italy (birth registration, the child's permit, Bangladeshi passport from the Embassy, citizenship rules), Citizenship (10 years' residence, language B1, the 2025 referendum outcome and 2025 citizenship-by-descent changes only if relevant).
- **G** money: Sending money home (MTOs, banks, Poste Italiane, apps, bKash/Nagad partners in Italy, costs, the Bangladesh 2.5% incentive, hundi and its risks, Italy's 1.5% tax on remittances outside the EU if in force), Bangladesh Bank remittance-from-Italy figures, the EUR->Tk and USD->Tk rates on 10 Nov 2026 (ECB/Banca d'Italia and Bangladesh Bank), opening a bank account in Italy (conto di base), taxes for workers (codice fiscale, IRPEF withheld, 730 return), what workers can bring home (customs both sides: baggage, gold, phones, cash declaration over EUR 10,000).

## The doc outline (proposed to the user; follow it)

```
# Italy: migration guide
(intro: legend, EUR->Tk rate, BMET, Decreto Flussi, nulla osta, SUI, permesso di soggiorno, Questura)
## Background
### In one minute
### Is it open now, and who can go?   (#### Status, The channels, Who qualifies, Size, What closed it before)
### How a job reaches you, and who takes a cut   (#### topics)
### What you pay, and what you earn and keep   (#### The cap, What people really pay, How it is paid, How they borrow, What the job pays, What goes unpaid, Money sent home, How long the debt takes)
### What ties you to the employer
### What goes wrong most, and what people wrongly believe
## Visas not open to Bangladeshis
## Work visa: Decreto Flussi worker (non-seasonal)
### Step 1: Find a real job
### Step 2: The job offer and contract
### Step 3: The employer gets your nulla osta
### Step 4: Passport, police clearance and certificates
### Step 5: The visa at the Italian Embassy in Dhaka, and checking it is real
### Step 6: Orientation, BMET clearance and the flight
### Step 7: After arrival
### Scams / Your rights at work / How long you can stay / Your residence permit / What can get you jailed or deported /
### If you aren't paid / Changing employer or leaving / Bringing your family
## Work visa: seasonal worker
## Work visa: domestic and care worker
## Work visa: highly skilled and out-of-quota (EU Blue Card, Article 27)
## Self-employment visa
## Student visa
## Visit visa (Schengen)
## Family reunification
## Changing visa type
## Asylum
## Having a child in Italy
## Sending money home
## Irregular routes and undocumented workers
## Going home without valid papers
## If a worker dies, is injured or loses the job
## Coming home
## Contacts
```
