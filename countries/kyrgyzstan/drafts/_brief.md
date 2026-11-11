# Kyrgyzstan research brief (shared by every topic agent, 10 November 2026)

You are one of seven research agents writing the Kyrgyzstan doc for the BSAISL Migration Pathway Navigator. Today is 10 November 2026. Repo root: `C:\Users\User\Desktop\Github\bsaisl-migration-knowledge-base` (below: ROOT).

## Read first (binding)

1. `ROOT\CLAUDE.md`: the project, format, quality rules and research process. Binding. Read it in full.
2. `ROOT\countries\malaysia\doc.md`: THE STANDARD. Imitate its depth, tone and step pattern. Read the Background (H3 parts with H4 topics), "Work visa: company worker (PLKS)" Step 1, the problem sections, and any section matching your topic. `ROOT\countries\italy\doc.md` and `ROOT\countries\kuwait\doc.md` are the newest docs (same rules) if you need more examples.

## The corridor in brief (what we know so far; verify everything)

BMET (OEP) cleared 1,713 Bangladeshi workers for Kyrgyzstan in 2023 (17th destination) and 6,652 in 2025 (10th), but fewer than 1,146 in 1 Jan-7 Nov 2026 (not in the top 30). Saved files: `ROOT\countries\italy\sources\oep-country-clearance-all-countries-2023.txt`, `-2025.txt`, `-2026-ytd.txt`. News says Kyrgyzstan raised its foreign-worker quota to 100,000 for 2026 (from 25,000 in 2025), that arrivals of Bangladeshis fell in 2026 while Indians and Uzbeks rose, and Facebook groups advertise a "new work visa program" for Bangladeshis. Kyrgyzstan is also suspected to be sold as a stepping stone to Russia, Kazakhstan or the EU. Find out what is really happening: who goes, to what jobs, through whom, at what price, what happens to them, and why the flow fell.

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
  > - What does a Kyrgyz work visa sell for in Dhaka in 2026?
  ```
- Explain every acronym, organisation, platform and Kyrgyz or Russian term the first time you use it (work permit / разрешение на работу, registration, the Ministry of Labour, Social Security and Migration, the Migration Service, Bishkek, som (KGS) ...). No tables. English only in the text. "workers", "people", "migrants", never "beneficiaries". No opinions, no advice of our own.
- State the latest status for Bangladeshis wherever it matters, dated: quotas, visa rules, any suspension, crackdown, deportation wave, or 2025-2026 change.
- Specific beats general: names, numbers, places, dates, the exact office, form, fee and phone. Write what an insider (agency staff, a Bangladeshi in Bishkek, a returnee) would recognise as real.
- Money: give amounts in the source's currency (KGS som, USD, Tk). The lead adds Taka conversions (agent G logs the rate).

## Where you work (avoid file races)

Work ONLY inside your own staging folder: `ROOT\countries\kyrgyzstan\work\<YOUR LETTER>\` (it has an empty `sources/` folder). Run every tool from your folder with `python` (not python3), using the path `../../../../tools/`:

```
cd "/c/Users/User/Desktop/Github/bsaisl-migration-knowledge-base/countries/kyrgyzstan/work/<X>"
python ../../../../tools/fetch.py <url> <name>                 # saves sources/<name>.html|.pdf + text copy
python ../../../../tools/wayback.py <url> <name> official|news # archived copy from the Wayback Machine
python ../../../../tools/facts.py source --name <name> --publisher "..." --title "..." --official yes|no|archived|news-archived --page-date YYYY-MM-DD|undated
python ../../../../tools/facts.py add --prefix <X> --name <name> --claim "..." --quote "exact words from the saved text copy" --page-date YYYY-MM-DD|undated --status verified|possibly-outdated|conflict|unofficial|lead [--visa .. --field .. --value ..] [--note ".."]
```

- facts.py refuses a quote not found in the saved text copy: copy quotes exactly from `sources/<name>.md` or `.txt`. Keep quotes short and precise. The quote must prove the claim, including every number in it. One fact per number or rule.
- Status: official + dated within 12 months = verified; official older or undated = possibly-outdated; news/NGO/guide = unofficial (practice) or lead; conflicting sources = conflict, with a note naming the other id.
- Source names: lowercase, hyphens, start with the publisher (e.g. `mlsp-kg-work-permit-2026`, `evisa-kg-work-visa`, `news-prothomalo-kyrgyzstan-2026-05`). Make names specific so they don't clash with other agents.
- If several facts need adding, write a small Python script in your own folder that reads a JSON list and calls facts.py with subprocess (see `ROOT\countries\kyrgyzstan\work\addm.py`, run as `python ../addm.py x.json`; shell quoting breaks on apostrophes, Bangla and Russian text).
- Never write to `countries/kyrgyzstan/facts.csv`, `sources.csv` or `sources/` directly, or to any other country's folder. Never commit. The lead merges your folder.
- Bangladesh-side pages already saved for other countries (OEP, BMET, PKB, WEWB, Ministry, passport, police clearance pages) may be copied from `ROOT\countries\italy\sources\` or `...\kuwait\sources\` into your `sources/` (all files for that name), then logged with `python ../../../../tools/fetch.py --log <original url> <name> manual`. Prefer a fresh fetch when the page loads (fees change). Every fact must be logged again in your own facts.csv.
- Kyrgyz official pages are often in Russian or Kyrgyz only: quote the Russian exactly and put the English meaning in the claim. Official: the Cabinet of Ministers (gov.kg), the legal database of the Ministry of Justice (cbd.minjust.gov.kg: laws "On external migration" / "О внешней миграции", "On external labour migration" / "О внешней трудовой миграции", the Labour Code, Cabinet decrees on the yearly quota for foreign workers), the Ministry of Labour, Social Security and Migration (mlsp.gov.kg) and its migration service, the Ministry of Foreign Affairs (mfa.gov.kg) and the e-visa portal (evisa.e-gov.kg), the State Tax Service (sti.gov.kg), the National Bank (nbkr.kg), the National Statistical Committee (stat.gov.kg), the State Border Service, the Ministry of Internal Affairs (mvd.gov.kg), and Kyrgyz embassies' sites.

## Blocked pages and web archives

If fetch.py fails (403, timeout, empty text or a page that needs JavaScript), try in this order:
1. Firecrawl `mcp__firecrawl__firecrawl_scrape` with default settings only (load with ToolSearch "select:mcp__firecrawl__firecrawl_scrape"; formats ["markdown"]). Never use stealth or enhanced proxies, location spoofing or any other bot-check circumvention. Save the markdown with the Write tool to `sources/<name>.md` and log it with `fetch.py --log <url> <name> firecrawl`.
2. The Wayback Machine: `wayback.py <url> <name> official|news`. Also use it for pages that have been removed or changed, and to date undated pages.
3. If all fail, list the page under "c. Blocked pages" (exact URL, suggested file name, what it should prove). The user downloads these by hand, so list every one that matters.
Do not use the Chrome browser tools. Facebook posts of the Bangladesh mission accredited to Kyrgyzstan, the Kyrgyz embassy accredited to Bangladesh, or BMET count as official; list them under blocked pages with the exact post URL if you can't save them. Search with WebSearch (load via ToolSearch "select:WebSearch") or Firecrawl search, in English, Russian and Bangla.

## Key sources (start here)

- Kyrgyzstan: see the official sites above; also IOM Kyrgyzstan (kyrgyzstan.iom.int: migration situation reports with foreign workers by nationality), ILO, UNHCR Central Asia, the US State Department Trafficking in Persons report (Kyrgyzstan chapter), Human Rights Watch, Times of Central Asia (timesca.com), 24.kg, AKIpress, Kaktus.media, Kloop, RFE/RL (Radio Azattyk), Eurasianet, The Diplomat.
- Bangladesh: BMET (bmet.gov.bd: permission letters for Kyrgyzstan in "miscellaneous-infos"; the agencies list in `ROOT\agencies\agencies.csv` and `ROOT\data\oep-agency-list-2026-10-28.csv`), OEP (oep.gov.bd country-clearance reports; see `ROOT\countries\maldives\notes.md` on getting OEP JSON), the Ministry of Expatriates' Welfare (probashi.gov.bd), WEWB, PKB, BOESL, Bangladesh Bank (bb.org.bd, remittance by country), the Bangladesh mission accredited to Kyrgyzstan (find which: Tashkent, Moscow, Astana or another; check mofa.gov.bd), the Kyrgyz mission accredited to Bangladesh (probably in New Delhi; check mfa.gov.kg).
- News: Bangladeshi (Prothom Alo, Daily Star, TBS, Dhaka Tribune, bdnews24, Jago News, Samakal, Kaler Kantho, Bonik Barta, BBC Bangla, Jamuna TV) in English and Bangla (কিরগিজস্তান ভিসা, কিরগিজস্তানে বাংলাদেশি শ্রমিক, কিরগিজস্তান ওয়ার্ক পারমিট, কিরগিজস্তান দালাল, কিরগিজস্তান হয়ে ইউরোপ ...); Kyrgyz and Russian (24.kg, AKIpress, Kaktus, Azattyk: "граждане Бангладеш", "бангладешцы Кыргызстан", "трудовые мигранты из Бангладеш", "квота иностранная рабочая сила").

## Time limit

About 40 minutes of research, then write your findings file even if some points remain open (list them as Need to know with what you searched). Quality over volume, but cover your whole topic. Don't stop at the first answer.

## Your output

Write `ROOT\countries\kyrgyzstan\drafts\<X>-findings.md` with:

- **a. Draft doc text:** your sections, written exactly as they should appear in doc.md (headings per the outline below), every sentence and fact-bearing list item cited with your fact ids. Where another agent's topic is needed, write "(see <exact section heading>)" rather than researching it.
- **b. Notes (for notes.md):** what you searched (sites and search terms, English, Russian and Bangla), conflicts between sources (with ids), what happens in practice, facts logged but not used and why.
- **c. Blocked pages:** exact URL, suggested file name, what it would prove (say if Wayback was tried).
- **d. Insider questions:** the open Need to know questions, one line each.

Final message back to the lead: 5-10 lines: number of facts and sources logged (official vs news), sections written, the most important findings, and anything the lead must decide.

## Who does what (letter = fact prefix)

- **N** corridor, chain and money in practice: Background drafts (Is it open now: status for Bangladeshis on 10 Nov 2026, the channels and the one most people use, who qualifies, size, what closed or restricted it before, why 2025 rose and 2026 fell; How a job reaches you, and who takes a cut: the quota, the employer, Kyrgyz and Bangladeshi middlemen, the visa trade; What you pay, and what you earn and keep: real costs in Tk lakh vs any BMET cap, wages in practice, debt; What goes wrong most, and what people wrongly believe, including "Kyrgyzstan is a door to Europe"), the work visa Scams section, agencies with evidence (from BMET permission letters and news), corridor numbers (OEP clearances by year and month 2023-2026, by job and sex; Kyrgyz figures for Bangladeshi workers and permits; comparison with India, Pakistan, Nepal, Uzbekistan), big names, scandals, crackdowns, stranded-worker cases.
- **W** Kyrgyz-side work route: Work visa Steps 2, 3, 5 and 7 (the job offer and contract; the employer's quota and work permit at the Ministry / migration service; the work visa (category, e-visa portal evisa.e-gov.kg, Kyrgyz embassy, invitation), documents, fees, processing times; checking a permit and visa are real; arrival: registration with the migration authority, the work permit card, medical tests, the residence permit, tax number (INN/PIN), SIM, bank account), How long you can stay (permit length, renewal, extension, permanent residence, citizenship), Your residence permit; any other work route (individual work permit, self-employment / patent, business owners, highly skilled).
- **B** Bangladesh side: Step 1 (OEP registration, any BMET/BOESL G2G or agency route to Kyrgyzstan, any Bangladesh-Kyrgyzstan MoU, cost caps in permission letters, PKB loans, complaints to BMET), Step 4 (passport, police clearance, certificates, attestation at MoFA, and any legalisation the Kyrgyz side needs), Step 6 (PDO, BMET clearance, smart card, fees, welfare fee, flights and the usual route to Bishkek), Coming home (WEWB, airport help desk), the Bangladesh mission accredited to Kyrgyzstan and its services (passport, Travel Permit, NID, power of attorney, death and body repatriation, legal help), contacts. OEP clearance numbers for Kyrgyzstan by year, month, job and sex 2023-2026, and the BMET permission letters for Kyrgyzstan (agency, employer, job, salary, cost cap).
- **L** law and work: Your rights at work (Kyrgyz Labour Code: contract, minimum wage, hours, overtime, leave, end-of-contract pay, payslips, sick pay, social insurance for foreigners), What can get you jailed or deported (overstay, working without a permit, wrong employer, fake documents, drugs, fines in som, entry bans, deportation procedure, detention), If you aren't paid (labour inspection, courts, the Ombudsman (Akyikatchy), NGOs and lawyers in Bishkek, step by step), Changing employer or leaving, Leaving at the end of the job, Going home on leave, If a worker dies, is injured or loses the job (work-accident rules, body repatriation, compensation), pension.
- **V** non-work visas and family: Visit visa (tourist and business: e-visa, visa-free or not for Bangladeshis, fees, length of stay, registration), Student visa (Kyrgyz universities and medical colleges that take South Asian students, admission, fees, part-time work rules, the Bangladesh Medical and Dental Council's recognition of Kyrgyz medical degrees), Visas not open to Bangladeshis (with why), Changing visa type (can a visitor or student switch to work inside Kyrgyzstan?), Family (bringing a spouse and children, family visa), Having a child in Kyrgyzstan (birth registration, the child's status, Bangladeshi passport).
- **U** irregular routes, status and asylum: Kyrgyzstan as a transit route (onward to Russia, Kazakhstan, Belarus, the EU; prices, dalal networks, deaths or detentions), workers stranded or deceived in Kyrgyzstan (cases 2023-2026), undocumented Bangladeshis, raids, deportations and entry bans, Going home without valid papers (Travel Permit from the Bangladesh mission, exit fines, IOM assisted return), Asylum (Kyrgyzstan's refugee law and UNHCR's role; written to discourage, but accurate: who is recognised, what happens to Bangladeshi claims), Irregular routes and undocumented workers.
- **G** money: Sending money home (banks, money transfer companies and apps from Kyrgyzstan to Bangladesh, costs, the Bangladesh 2.5% incentive, hundi and its risks), Bangladesh Bank remittance-from-Kyrgyzstan figures, the KGS->Tk and USD->Tk rates on 10 Nov 2026 (National Bank of Kyrgyzstan and Bangladesh Bank; log a fact "1 USD = about Tk X" and "1 KGS = about Tk Y"), opening a bank account in Kyrgyzstan as a foreigner, taxes for foreign workers (income tax rate, who withholds it), what workers can bring home (customs both sides: cash declaration limits, phones, gold), and the cost of living in Bishkek in practice.

## The doc outline (follow it; the lead may add sections)

```
# Kyrgyzstan: migration guide
(intro: legend, KGS->Tk and USD->Tk rates, BMET, OEP, work permit, the Kyrgyz migration authority)
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
### Step 5: The work visa, and checking it is real
### Step 6: Orientation, BMET clearance and the flight
### Step 7: After arrival
### Scams / Your rights at work / How long you can stay / What can get you jailed or deported /
### If you aren't paid / Changing employer or leaving / Bringing your family
## (other work routes if any)
## Student visa
## Visit visa
## Family
## Changing visa type
## Asylum
## Having a child in Kyrgyzstan
## Sending money home
## Irregular routes and undocumented workers
## Going home without valid papers
## If a worker dies, is injured or loses the job
## Coming home
## Contacts
```
