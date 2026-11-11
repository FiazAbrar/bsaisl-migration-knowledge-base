# Cambodia research brief (shared by every topic agent, 11 November 2026)

You are one of eight research agents writing the Cambodia doc for the BSAISL Migration Pathway Navigator. Today is 11 November 2026. Repo root: `C:\Users\User\Desktop\Github\bsaisl-migration-knowledge-base` (below: ROOT).

## Read first (binding)

1. `ROOT\CLAUDE.md`: the project, format, quality rules and research process. Binding. Read it in full.
2. `ROOT\countries\malaysia\doc.md`: THE STANDARD. Imitate its depth, tone and step pattern. Read the Background (H3 parts with H4 topics), "Work visa: company worker (PLKS)" Step 1, the problem sections, and any section matching your topic. `ROOT\countries\kyrgyzstan\doc.md` and `ROOT\countries\italy\doc.md` are the newest docs (same rules).

## The corridor in brief (what we know so far; verify everything)

BMET (OEP) cleared 1,378 Bangladeshi workers for Cambodia in 2023 (18th destination), 12,263 in 2025 (8th) and 3,700 in 1 Jan-7 Nov 2026 (12th). Saved files: `ROOT\countries\italy\sources\oep-country-clearance-all-countries-2023.txt`, `-2025.txt`, `-2026-ytd.txt` (2024 is not saved). Cambodia is known for online-scam compounds (Sihanoukville, border towns, special economic zones) that hold trafficked foreigners, including South Asians, and for crackdowns and mass deportations in 2025-2026; there was also an armed Thailand-Cambodia border conflict in 2025. Find out what is really happening for Bangladeshis: which jobs are real (garment, construction, casinos, others), who goes, through whom, at what price, how many end up in scam compounds, how they are rescued, and why clearances rose in 2025 and fell in 2026.

## The style (what the user approved)

- No SOP section. Procedures are written in place, in the step where they happen.
- Numbered actions, each starting with a bold verb: `1. **Register on OEP,** BMET's website for job-seekers ...`
- Under an action: `You'll need:` (documents, money, phone, photos), then click-by-click sub-steps as a nested numbered list (exact URL or portal, what to type, button names as on screen), then short bold labels where they apply: `**Check it is real:**`, `**If it fails:**`, `**Scams:**`.
- Ready-to-use wording where a worker must write or say something (sample in quotes with [blanks]).
- Escalation ladders: "If ..., in this order:" then numbered routes, each with phone, link or address.
- Headings: H2 per visa / big section, H3 per step or topic, H4 inside. Max H4; below that a bold lead-in. No dates in headings.
- Cross-references use the exact heading text: "(see If you aren't paid)", "(Step 1, item 4)", "(Work visa: company worker, Step 3)". Never "see above".
- Every sentence ends with fact ids in brackets, e.g. `[W0012, N0003]`. No uncited sentence, and every list item that states a fact is cited too.
- Gaps: a quote block right after the paragraph or step, one precise insider question per bullet:
  ```
  > **Need to know**
  > - What does a Cambodian work visa sell for in Dhaka in 2026?
  ```
- Explain every acronym, organisation, platform and Khmer term the first time you use it (MLVT, the Ministry of Labour and Vocational Training; FWCMS, its online foreign-worker system; the E-class / EB / EG visa; work permit; employment card; GDI, the General Department of Immigration; NSSF; riel (KHR) ...). No tables. English only in the text. "workers", "people", "migrants", never "beneficiaries". No opinions, no advice of our own.
- State the latest status for Bangladeshis wherever it matters, dated: quotas, visa rules, any suspension, crackdown, deportation wave, or 2025-2026 change.
- Specific beats general: names, numbers, places, dates, the exact office, form, fee and phone. Write what an insider (agency staff, a Bangladeshi in Phnom Penh, a returnee) would recognise as real.
- Money: give amounts in the source's currency (USD, KHR riel, Tk). The lead adds Taka conversions (agent G logs the rate).

## Where you work (avoid file races)

Work ONLY inside your own staging folder: `ROOT\countries\cambodia\work\<YOUR LETTER>\` (it has an empty `sources/` folder). Run every tool from your folder with `python` (not python3), using the path `../../../../tools/`:

```
cd "/c/Users/User/Desktop/Github/bsaisl-migration-knowledge-base/countries/cambodia/work/<X>"
python ../../../../tools/fetch.py <url> <name>                 # saves sources/<name>.html|.pdf + text copy
python ../../../../tools/wayback.py <url> <name> official|news # archived copy from the Wayback Machine
python ../../../../tools/facts.py source --name <name> --publisher "..." --title "..." --official yes|no|archived|news-archived --page-date YYYY-MM-DD|undated
python ../../../../tools/facts.py add --prefix <X> --name <name> --claim "..." --quote "exact words from the saved text copy" --page-date YYYY-MM-DD|undated --status verified|possibly-outdated|conflict|unofficial|lead [--visa .. --field .. --value ..] [--note ".."]
```

- facts.py refuses a quote not found in the saved text copy: copy quotes exactly from `sources/<name>.md` or `.txt`. Keep quotes short and precise. The quote must prove the claim, including every number in it. One fact per number or rule.
- Status: official + dated within 12 months = verified; official older or undated = possibly-outdated; news/NGO/guide = unofficial (practice) or lead; conflicting sources = conflict, with a note naming the other id.
- Source names: lowercase, hyphens, start with the publisher (e.g. `mlsp-kg-work-permit-2026`, `evisa-kg-work-visa`, `news-prothomalo-cambodia-2026-05`). Make names specific so they don't clash with other agents.
- If several facts need adding, write a small Python script in your own folder that reads a JSON list and calls facts.py with subprocess (see `ROOT\countries\cambodia\work\addm.py`, run as `python ../addm.py x.json`; shell quoting breaks on apostrophes and Bangla text). Run each JSON batch once only: rerunning it logs duplicate facts. Put new facts in a new JSON file.
- Never write to `countries/cambodia/facts.csv`, `sources.csv` or `sources/` directly, or to any other country's folder. Never commit. The lead merges your folder.
- Bangladesh-side pages already saved for other countries (OEP, BMET, PKB, WEWB, Ministry, passport, police clearance pages) may be copied from `ROOT\countries\italy\sources\` or `...\kuwait\sources\` into your `sources/` (all files for that name), then logged with `python ../../../../tools/fetch.py --log <original url> <name> manual`. Prefer a fresh fetch when the page loads (fees change). Every fact must be logged again in your own facts.csv.
- Cambodian official pages are often in Khmer, sometimes English: quote exactly and put the English meaning in the claim. Official: the Ministry of Labour and Vocational Training (mlvt.gov.kh; the FWCMS foreign-worker portal fwcms.mlvt.gov.kh: quotas, work permits, employment cards, fees), the General Department of Immigration of the Ministry of Interior (immigration.gov.kh: visas, E-class extensions, overstay fines, deportation), the Ministry of Foreign Affairs and International Cooperation (mfaic.gov.kh; the e-visa portal evisa.gov.kh), the National Committee for Counter Trafficking (NCCT), the Cambodian National Police, the National Social Security Fund (nssf.gov.kh), the General Department of Taxation (tax.gov.kh), the National Bank of Cambodia (nbc.gov.kh), the Labour Law (1997) and its prakas (ministerial orders), and Cambodian embassies' sites.

## Blocked pages and web archives

If fetch.py fails (403, timeout, empty text or a page that needs JavaScript), try in this order:
1. Firecrawl `mcp__firecrawl__firecrawl_scrape` with default settings only (load with ToolSearch "select:mcp__firecrawl__firecrawl_scrape"; formats ["markdown"]). Never use stealth or enhanced proxies, location spoofing or any other bot-check circumvention. Save the markdown with the Write tool to `sources/<name>.md` and log it with `fetch.py --log <url> <name> firecrawl`.
2. The Wayback Machine: `wayback.py <url> <name> official|news`. Also use it for pages that have been removed or changed, and to date undated pages.
3. If all fail, list the page under "c. Blocked pages" (exact URL, suggested file name, what it should prove). The user downloads these by hand, so list every one that matters.
Do not use the Chrome browser tools. Facebook posts of the Bangladesh mission accredited to Cambodia, the Cambodian embassy accredited to Bangladesh, MLVT, the GDI, or BMET count as official; list them under blocked pages with the exact post URL if you can't save them. Search with WebSearch (load via ToolSearch "select:WebSearch") or Firecrawl search, in English and Bangla (and Khmer where useful).

## Key sources (start here)

- Cambodia: see the official sites above; also IOM Cambodia, ILO, UNODC (reports on scam centres in Southeast Asia, 2023-2026), OHCHR's 2023 report on online scam operations, UNHCR, the US State Department Trafficking in Persons report (Cambodia chapter), Amnesty International (2025 report on scam compounds), Human Rights Watch, LICADHO and CENTRAL (Cambodian labour rights NGOs), the Arbitration Council, Khmer Times, Phnom Penh Post, CamboJA News, VOD, Radio Free Asia, The Diplomat, Nikkei Asia, Reuters, AP, Al Jazeera, Rest of World.
- Bangladesh: BMET (bmet.gov.bd: permission letters for Cambodia in "miscellaneous-infos"; `ROOT\agencies\agencies.csv` and `ROOT\data\oep-agency-list-2026-10-28.csv`), OEP (oep.gov.bd country-clearance reports; see `ROOT\countries\maldives\notes.md` on getting OEP JSON, and `ROOT\countries\kyrgyzstan\work\B\` for how B did it last time), the Ministry of Expatriates' Welfare (probashi.gov.bd), WEWB, PKB, BOESL, Bangladesh Bank (bb.org.bd, remittance by country), the Bangladesh mission accredited to Cambodia (check mofa.gov.bd), the Cambodian mission accredited to Bangladesh (check mfaic.gov.kh), the CID and RAB (rescue and trafficking cases), BRAC Migration, RMMRU, OKUP, WARBE.
- News: Bangladeshi (Prothom Alo, Daily Star, TBS, Dhaka Tribune, bdnews24, Jago News, Samakal, Kaler Kantho, Bonik Barta, BBC Bangla, Jamuna TV) in English and Bangla (কম্বোডিয়া ভিসা, কম্বোডিয়ায় বাংলাদেশি শ্রমিক, কম্বোডিয়া ওয়ার্ক পারমিট, কম্বোডিয়া দালাল, কম্বোডিয়া সাইবার স্ক্যাম, কম্বোডিয়ায় আটক বাংলাদেশি, কম্বোডিয়া থেকে উদ্ধার ...); Cambodian and regional English press.

## Time limit

About 40 minutes of research, then write your findings file even if some points remain open (list them as Need to know with what you searched). Quality over volume, but cover your whole topic. Don't stop at the first answer.

## Your output

Write `ROOT\countries\cambodia\drafts\<X>-findings.md` with:

- **a. Draft doc text:** your sections, written exactly as they should appear in doc.md (headings per the outline below), every sentence and fact-bearing list item cited with your fact ids. Where another agent's topic is needed, write "(see <exact section heading>)" rather than researching it.
- **b. Notes (for notes.md):** what you searched (sites and search terms, English, Bangla and Khmer), conflicts between sources (with ids), what happens in practice, facts logged but not used and why.
- **c. Blocked pages:** exact URL, suggested file name, what it would prove (say if Wayback was tried).
- **d. Insider questions:** the open Need to know questions, one line each.

Final message back to the lead: 5-10 lines: number of facts and sources logged (official vs news), sections written, the most important findings, and anything the lead must decide.


## Who does what (letter = fact prefix)

- **N** corridor, chain and money in practice: Background drafts (Is it open now: status for Bangladeshis on 11 Nov 2026, the channels and the one most people use, who qualifies, size, what closed or restricted it before, why 2025 rose and 2026 fell; How a job reaches you, and who takes a cut: the employer, Cambodian and Bangladeshi middlemen, Chinese-run companies, the visa trade; What you pay, and what you earn and keep: real costs in Tk lakh vs any BMET cap, wages in practice, debt; What goes wrong most, and what people wrongly believe, including "Cambodia is a door to Thailand, Malaysia or Europe"), the work visa Scams section (ordinary job scams; agent S owns the scam compounds), agencies with evidence (BMET permission letters and news), corridor numbers (OEP clearances by year and month 2023-2026, by job and sex; Cambodian figures for Bangladeshi workers and work permits; comparison with India, Pakistan, Nepal), big names, crackdowns, stranded-worker cases.
- **W** Cambodian-side work route: Work visa Steps 2, 3, 5 and 7 (the job offer and contract; the employer's quota and work permit on FWCMS; the visa: E-class / business visa on arrival or e-visa, then the EB or EG extension; documents, fees, processing times; checking a permit and visa are real; arrival: work permit and employment card, medical check, extensions, SIM, bank account), How long you can stay (extensions, renewals, long-term stay, any residence or citizenship route), Your residence permit; other work routes (self-employed, business owners, highly skilled).
- **B** Bangladesh side: Step 1 (OEP registration, any BMET/BOESL route to Cambodia, any Bangladesh-Cambodia MoU or labour agreement, cost caps in permission letters, PKB loans, complaints to BMET), Step 4 (passport, police clearance, certificates, attestation at MoFA), Step 6 (PDO, BMET clearance, smart card, fees, welfare fee, flights and the usual route to Phnom Penh), Coming home (WEWB, airport help desk), the Bangladesh mission accredited to Cambodia (find which: an embassy in Phnom Penh, or Bangkok, Hanoi or elsewhere) and its services (passport, Travel Permit, NID, power of attorney, death and body repatriation, legal help, rescues from scam compounds), contacts; OEP clearance numbers for Cambodia by year, month, job and sex 2023-2026, and BMET permission letters for Cambodia (agency, employer, job, salary, cost cap).
- **L** law and work: Your rights at work (Cambodian Labour Law: contract, minimum wage (garment sector and others), hours, overtime, leave, seniority and end-of-contract pay, payslips, NSSF social security for foreigners), What can get you jailed or deported (overstay, working without a permit, fake documents, drugs, involvement in online scams and its prosecution, fines, blacklisting, deportation procedure, immigration detention), If you aren't paid (labour inspection, the Arbitration Council, courts, unions, NGOs in Phnom Penh, step by step), Changing employer or leaving, Leaving at the end of the job, Going home on leave, If a worker dies, is injured or loses the job (NSSF work-injury scheme, body repatriation, compensation), pension.
- **V** non-work visas and family: Visit visa (tourist T-class: visa on arrival, e-visa, fees, length, extensions; why a tourist visa is not a work visa), Student visa (if any route exists for Bangladeshis), Visas not open to Bangladeshis (with why), Changing visa type (tourist to business/E-class inside Cambodia: is it allowed, what agents sell), Family (spouse and children, dependent visas), Having a child in Cambodia (birth registration, the child's status, Bangladeshi passport).
- **U** irregular routes, status and asylum: Cambodia as a transit route (onward to Thailand, Malaysia, Vietnam or further; prices, dalal networks, deaths or detentions), undocumented Bangladeshis, raids, immigration detention, deportations and blacklists, Going home without valid papers (Travel Permit from the Bangladesh mission, overstay fines, IOM assisted return), Asylum (Cambodia's refugee sub-decree and UNHCR's role; written to discourage, but accurate), Irregular routes and undocumented workers. Leave the scam compounds to agent S.
- **S** scam compounds and trafficking (the corridor's biggest danger): how Bangladeshis are recruited into online-scam compounds (fake jobs as data entry, customer service, IT, translator, casino work; ads on Facebook, Telegram, WhatsApp; routes via Dubai, Thailand, Malaysia), where the compounds are (Sihanoukville, Bavet, O'Smach, Poipet, special economic zones), what happens inside (passport seizure, debts, quotas, beatings, resale between compounds, forced crime), numbers of Bangladeshis rescued or deported 2023-2026 (Cambodian police and NCCT, the Bangladesh mission, IOM, UNODC, the US Trafficking in Persons report), the 2025-2026 crackdowns and what happens to rescued foreigners (victim screening vs prosecution vs deportation), how to get out (hotlines, the Bangladesh mission, Cambodian police, NGOs and IOM), warning signs, and Bangladeshi brokers or agencies named in these cases. Write a section `## Scam compounds and trafficking` (so a reader recognises the trap and knows exactly who to call) plus Background inserts.
- **G** money: Sending money home (banks, money transfer companies and apps from Cambodia to Bangladesh, costs, the Bangladesh 2.5% incentive, hundi and its risks), Bangladesh Bank remittance-from-Cambodia figures, the USD->Tk and KHR->Tk rates on 11 Nov 2026 (National Bank of Cambodia and Bangladesh Bank; log a fact "1 USD = about Tk X" and "1,000 KHR = about Tk Y"; wages and prices in Cambodia are mostly in US dollars), opening a bank account in Cambodia as a foreigner (ABA, ACLEDA, Wing), taxes for foreign workers (salary tax rates, who withholds it), what workers can bring home (customs both sides: cash declaration limits, phones, gold), and the cost of living in Phnom Penh in practice.

## The doc outline (follow it; the lead may add sections)

```
# Cambodia: migration guide
(intro: legend, USD->Tk and KHR->Tk rates, BMET, OEP, MLVT, FWCMS, work permit, employment card, E-class visa, GDI)
## Background
### In one minute
### Is it open now, and who can go?   (#### Status, The channels, Who qualifies, Size, What closed it before)
### How a job reaches you, and who takes a cut   (#### topics)
### What you pay, and what you earn and keep   (#### The cap, What people really pay, How it is paid, How they borrow, What the job pays, What goes unpaid, Money sent home, How long the debt takes)
### What ties you to the employer
### What goes wrong most, and what people wrongly believe
## Visas not open to Bangladeshis
## Work visa: company worker
### Step 1: Find a real job
### Step 2: The job offer and contract
### Step 3: The employer gets your work permit
### Step 4: Passport, police clearance and certificates
### Step 5: The visa, and checking it is real
### Step 6: Orientation, BMET clearance and the flight
### Step 7: After arrival
### Scams / Your rights at work / Your residence permit / What can get you jailed or deported /
### If you aren't paid / Changing employer or leaving / Bringing your family
## Scam compounds and trafficking
## (other work routes if any)
## Student visa
## Visit visa
## Family
## Changing visa type
## Asylum
## Having a child in Cambodia
## Sending money home
## Irregular routes and undocumented workers
## Going home without valid papers
## If a worker dies, is injured or loses the job
## Coming home
## Contacts
```
