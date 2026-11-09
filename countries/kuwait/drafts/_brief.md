# Kuwait research brief (shared by every topic agent, 9 November 2026)

You are one of nine research agents writing the Kuwait doc for the BSAISL Migration Pathway Navigator. Today is 9 November 2026. Repo root: `C:\Users\User\Desktop\Github\bsaisl-migration-knowledge-base` (below: ROOT).

## Read first (binding)

1. `ROOT\CLAUDE.md`: the project, format, quality rules and research process. Binding. Read it in full.
2. The finished docs to imitate in depth, tone and step pattern (read only the parts relevant to your topic, not whole files):
   - `ROOT\countries\malaysia\doc.md`: THE TEMPLATE. Look at the Background (H3 parts with H4 topics), "Work visa: company worker (PLKS)" Step 1 and the problem sections, plus any section matching your topic.
   - `ROOT\countries\maldives\doc.md` and `ROOT\countries\united-arab-emirates\doc.md`: the newest docs. `ROOT\countries\saudi-arabia\doc.md` and `ROOT\countries\qatar\doc.md` are the closest Gulf corridors (kafala, domestic workers, GAMCA/Wafid medical, absconding reports): reuse their structure for the same problems.

## The style (what the user approved)

- No SOP section. Procedures are written in place, in the step where they happen.
- Numbered actions, each starting with a bold verb: `1. **Register on OEP,** BMET's website for job-seekers ...`
- Under an action: `You'll need:` (documents, money, phone, photos), then the click-by-click sub-steps as a nested numbered list (exact URL or app, what to type, button names as on screen), then short bold labels where they apply: `**Check it is real:**`, `**If it fails:**`, `**Scams:**`.
- Ready-to-use wording where a worker must write or say something (sample in quotes with [blanks]).
- Escalation ladders: "If ..., in this order:" then numbered routes, each with phone, link or address.
- Headings: H2 per visa / big section, H3 per step or topic, H4 for topics inside. Max H4; below that a bold lead-in. No dates in headings.
- Cross-references use the exact heading text: "(see If you aren't paid)", "(Step 1, item 4)", "(Work visa: private-sector worker, Step 3)". Never "see above".
- Every sentence ends with fact ids in brackets, e.g. `[W0012, N0003]`. No uncited sentence, ever.
- Gaps: a quote block right after the paragraph or step, one precise insider question per bullet:
  ```
  > **Need to know**
  > - What does a Kuwait Article 18 cleaning-company visa sell for in Dhaka in 2026?
  ```
- Explain every acronym, organisation and platform the first time you use it. No tables. English only. "workers", "people", "migrants", never "beneficiaries". No opinions, no advice of our own.
- State the latest visa refusal, suspension, quota freeze or cancellation status for Bangladeshis wherever it matters (dated). Kuwait has repeatedly frozen or restricted visas for Bangladeshis (e.g. after the 2020-21 MP Papul visa-trafficking case); find the status on 9 November 2026 for each visa type.
- Specific beats general: names, numbers, places, dates, the exact counter, form, fee and phone. Write what an insider (agency staff, returnee, caseworker at the Bangladesh Embassy in Kuwait) would recognise as real.
- Money: give amounts in KWD (Kuwaiti dinar) or USD as the source does. The lead adds Taka conversions (agent G logs the rate).

## Where you work (important: avoid file races)

Work ONLY inside your own staging folder: `ROOT\countries\kuwait\work\<YOUR LETTER>\` (it has an empty `sources/` folder). Run every tool from your folder with `python` (not python3), using the path `../../../../tools/`:

```
cd "/c/Users/User/Desktop/Github/bsaisl-migration-knowledge-base/countries/kuwait/work/<X>"
python ../../../../tools/fetch.py <url> <name>                 # saves sources/<name>.html|.pdf + text copy
python ../../../../tools/wayback.py <url> <name> official|news # archived copy of a page that won't load
python ../../../../tools/facts.py source --name <name> --publisher "..." --title "..." --official yes|no|archived|news-archived --page-date YYYY-MM-DD|undated
python ../../../../tools/facts.py add --prefix <X> --name <name> --claim "..." --quote "exact words from the saved text copy" --page-date YYYY-MM-DD|undated --status verified|possibly-outdated|conflict|unofficial|lead [--visa .. --field .. --value ..] [--note ".."]
```

- facts.py refuses a quote not found in the saved text copy: copy quotes exactly from `sources/<name>.md` or `.txt`. Keep quotes short (one sentence) and precise. The quote must actually prove the claim, including every number in the claim.
- Status: official + dated within 12 months = verified; official older or undated = possibly-outdated; news/NGO/guide = unofficial (practice) or lead; conflicting sources = conflict, with a note naming the other id.
- Source names: lowercase, hyphens, start with the publisher (e.g. `moi-kw-visit-visa`, `pam-kw-work-permit-fees`, `news-arabtimes-kuwait-residency-law-2025-01`, `news-prothomalo-kuwait-visa-2026-03`). Prefix names with your letter if you worry about clashes: `<x>-...` is NOT needed; just make names specific.
- Never write to `countries/kuwait/facts.csv`, `sources.csv` or `sources/` directly, or to any other country's folder. Never commit. The lead merges your folder.
- Bangladesh-side pages already saved for other countries (OEP, BMET, PKB, WEWB, Ministry pages) may be copied from `ROOT\countries\maldives\sources\`, `...\united-arab-emirates\sources\`, `...\qatar\sources\` or `...\malaysia\sources\` into your `sources/` (all files for that name: .html/.md/.txt/.pdf), then logged with `python ../../../../tools/fetch.py --log <original url> <name> manual`. Prefer a fresh fetch when the page loads (fees and rules change). Every fact must be logged again in your own facts.csv.
- Official PDFs in `ROOT\official-pdfs\`: read in full; to cite one, fetch its online original or copy it into your `sources/` and log it.
- Kuwait's official sites are often in Arabic only. Arabic pages are fine as sources: quote the Arabic exactly and put the English meaning in the claim. Kuwait Al-Youm (the official gazette) and KUNA (Kuwait News Agency, state-run: count it as official) are good for decrees and cabinet decisions.

## Blocked pages

Many Kuwaiti government sites (moi.gov.kw, manpower.gov.kw, e.gov.kw, paci.gov.kw) block automated reading or are geo-restricted. Respect those blocks: the user downloads blocked pages by hand. If fetch.py fails (403, timeout, empty text), try in this order: (1) Firecrawl, `mcp__firecrawl__firecrawl_scrape` (load it with ToolSearch "select:mcp__firecrawl__firecrawl_scrape" if needed; formats ["markdown"]; use the default settings only: do NOT use stealth/enhanced proxies, location spoofing or any other bot-check circumvention; `mcp__firecrawl__firecrawl_search` is useful for searching too), then save the markdown with the Write tool to `sources/<name>.md` and log it with `fetch.py --log <url> <name> firecrawl`; (2) `wayback.py`. If all fail, list the page under "c. Blocked pages" (exact URL, suggested file name, what it should prove). The user will download blocked pages by hand, so list every one that matters. Facebook / X posts of the Bangladesh Embassy in Kuwait, PAM or the Ministry of Interior count as official; if one can't be saved, list it under blocked pages too. Search the web with WebSearch (load via ToolSearch "select:WebSearch") or Firecrawl search.

## Key official sites (start here)

- Kuwait: Ministry of Interior (moi.gov.kw; residency affairs; the e-visa portal kuwaitvisa.moi.gov.kw; the Sahel app for absconding reports and residence services); Public Authority for Manpower (PAM, manpower.gov.kw: work permits, labour complaints, domestic workers department, Ashal portal for employers); Public Authority for Civil Information (PACI, paci.gov.kw: Civil ID); Ministry of Health (medical exams for residency; Wafid / GAMCA pre-departure medical); Ministry of Foreign Affairs (mofa.gov.kw); Kuwait Al-Youm gazette; KUNA (kuna.net.kw); laws: Private Sector Labour Law 6/2010, Domestic Workers Law 68/2015, the 2024 foreigners' residence law (Decree-Law 114/2024) and its executive regulations (2025); Central Bank of Kuwait (cbk.gov.kw); Kuwait Customs; Kuwait Society of Engineers; Al-Durra (state domestic-worker recruitment company); Kuwait Society for Human Rights.
- Bangladesh: Embassy of Bangladesh in Kuwait (kuwait.mofa.gov.bd; labour wing), BMET (bmet.gov.bd, incl. pages/miscellaneous-infos permission letters), OEP (oep.gov.bd, incl. the country-clearance reports), Ministry of Expatriates' Welfare (probashi.gov.bd), WEWB (wewb.gov.bd), PKB (pkb.gov.bd), Bangladesh Bank (bb.org.bd), BOESL (boesl.gov.bd).
- `ROOT\agencies\activity.csv` and `agencies.csv`: BMET permission letters by country (about 48 Kuwait letters 2024-2026, e.g. Rowshon Habib Overseas RL2011 cleaners, Fly Far Overseas RL2345 heavy drivers, Delight Overseas RL2287, Masud Jamil Overseas RL1400 female cleaners) and agency data with cited red flags. `ROOT\data\oep-agency-list-2026-10-28.csv`: BMET's licence list.
- Other countries' embassies in Kuwait (India: indembkwt.gov.in, very complete worker guides and its Shelter/Labour Welfare pages; Philippines DMW/POLO Kuwait; Sri Lanka, Nepal) often publish the most complete worker guides.
- News: Kuwaiti English (Arab Times arabtimesonline.com, Kuwait Times kuwaittimes.com, Times Kuwait, KUNA English) and Arabic (Al-Qabas, Al-Rai, Al-Anba, Al-Jarida, Al-Seyassah); Bangladeshi (Prothom Alo, Daily Star, TBS, Jago News, Bonik Barta, Samakal, Dhaka Post, Kaler Kantho, banglanews24, BSS, Manab Zamin) in English and Bangla (কুয়েত ভিসা, কুয়েত প্রবাসী, কুয়েতে বাংলাদেশি শ্রমিক, কুয়েতের ভিসা বন্ধ, কুয়েত ফ্যামিলি ভিসা ...). HRW, Amnesty, Migrant-Rights.org, ILO, US State Dept TIP report (Kuwait chapter), RMMRU, OKUP, BRAC Migration for practice.

## Time limit

About 40 minutes of research, then write your findings file even if some points remain open (list them as Need to know with what you searched). Quality over volume, but cover your whole topic. Don't stop at the first answer.

## Your output

Write `ROOT\countries\kuwait\drafts\<X>-findings.md` with:

- **a. Draft doc text:** your sections, written exactly as they should appear in doc.md (headings per the outline below, steps, lists, Need to know blocks), every sentence cited with your fact ids. Where another agent's topic is needed, write "(see <exact section heading>)" rather than researching it.
- **b. Notes (for notes.md):** what you searched (sites and search terms, English, Bangla and Arabic), conflicts between sources (with ids), what happens in practice, facts logged but not used and why.
- **c. Blocked pages:** exact URL, suggested file name, what it would prove.
- **d. Insider questions:** the open Need to know questions, one line each.

Final message back to the lead: 5-10 lines: number of facts and sources logged (official vs news), sections written, the most important findings, and anything the lead must decide.

## Who does what (letter = fact prefix)

- **N** corridor, chain and money in practice: Background drafts (Is it open now: status for each visa type on 9 Nov 2026, channels, who qualifies, size, what closed it before (2016-2019 restrictions, the 2020-21 Papul case, any 2024-2026 freezes or reopenings); How a job reaches you, and who takes a cut: Article 18 visa trade, "free visa"/"azad visa", visa traders and shell companies in Kuwait, the Bangladeshi brokers, the choke points; What you pay, and what you earn and keep: real costs vs BMET cap, wages in practice, deductions, debt; What goes wrong most, and what people wrongly believe; irregular routes), the private-sector worker Scams section, agencies with evidence (from `agencies/`), insider items (syndicates, crackdowns, the big names). Corridor numbers: BMET/OEP yearly and 2026 clearances for Kuwait, stock of Bangladeshis in Kuwait (PACI data), comparison with India, Egypt, Nepal, Sri Lanka, Philippines.
- **W** Kuwait-side private-sector work route (Article 18): Work visa: private-sector worker Steps 2, 3, 5 and 7 (job offer and contract, the employer's PAM work permit and entry visa via MOI/Ashal, fees, medical in Bangladesh (GAMCA/Wafid), checking the visa is real, arrival: medical at the Ministry of Health, fingerprints, residency stamp, Civil ID from PACI, bank, SIM, Sahel app), How long you can stay (renewals, fees, the age-60 rule for workers without a degree, 6-month absence rule, residency fees under the 2025 rules), Your residence permit; Work visa: professional and skilled (engineers and the Kuwait Society of Engineers, nurses and doctors with the Ministry of Health, drivers' licences, degree attestation, the Article 18 to job-title link).
- **B** Bangladesh side: Step 1 (OEP registration, BMET permission letters for Kuwait, the relative's-visa / single-visa route, visa attestation by the Bangladesh Embassy's labour wing, cost caps, PKB loans, complaints to BMET), Step 4 (passport, police clearance, certificates and attestation), Step 6 (PDO, BMET clearance, smart card, fees, welfare fee, insurance, flights to Kuwait), Coming home (WEWB reintegration, airport help desk), Embassy services in Kuwait (passport renewal, outpass/travel permit, legal help, shelter, labour wing contacts), Bangladesh-side contacts. OEP clearance numbers for Kuwait by year and month 2023-2026 (official; the OEP country-clearance report).
- **L** law and work (private sector): Your rights at work (Labour Law 6/2010 and amendments, hours, overtime, Ramadan hours, summer midday work ban, leave, minimum wage, end-of-service indemnity, keeping the passport, housing, health insurance / Dhaman), What can get you jailed or deported (drugs, alcohol, religion, protests, residency law 114/2024 penalties, administrative deportation, traffic violations), If you aren't paid (PAM labour complaint, Labour Court, step by step), If your employer reports you absent (taghayyub, private sector), Changing employer or leaving (transfer rules and fees, release), Leaving at the end of the job (exit, end-of-service pay), Going home on leave, If a worker dies, is injured or loses the job (compensation, insurance, body repatriation from the Kuwait side).
- **D** domestic workers (Article 20: housemaids, house drivers, cooks, guards, farm workers): Work visa: domestic worker section end to end (Kuwait side: Domestic Workers Law 68/2015, PAM's Domestic Labour department, minimum wage, recruitment cost cap, Al-Durra, contract; Bangladesh side: rules for women going abroad, BMET domestic-worker training, age limits, whether Kuwait currently issues domestic visas to Bangladeshi women and men; problems: abuse, shelters (Kuwait's government shelter, the Embassy's safe home), absconding for domestic workers, transferring from Article 20 to Article 18, unpaid wages, going home). Many Bangladeshi men go on Article 20 as house drivers: cover them.
- **U** irregular status: Undocumented workers (amnesties, especially March-June 2024, and anything since), Going home without valid papers (deportation centre in Talha, detention, fines under the 2024 law, blacklist and fingerprint bans, can you ever return), the 2024 biometric fingerprint deadline and its consequences, crackdowns/raids 2024-2026, residency trafficking cases, how workers become undocumented (absconding reports, employer closures).
- **V** visits and short visas: the 2025 visit visa system (tourist e-visa, family visit, business visit, government visit; who qualifies; is it open to Bangladeshis), transit, medical treatment, student visa (Kuwait University scholarships, private universities), Umrah/Hajj transit if any, Visas not open to Bangladeshis (with why), Changing visa type (can a visitor switch to work? Article 18 transfers from Article 20 or 22).
- **F** family and residence: Family (dependent) visa (Article 22: salary threshold, documents, attestation of marriage and birth certificates in Bangladesh, fees, health insurance), Bringing your family (for a private-sector worker), Family visit visa (with V; you own the dependent route), Spouse of a Kuwaiti, Self-sponsorship / investor residence (Article 24) and property-owner residency, Having a child in Kuwait (birth registration, residency for the newborn, passport from the Embassy), Asylum (written to discourage: Kuwait is not party to the Refugee Convention; UNHCR in Kuwait).
- **G** money: Sending money home (exchange houses, banks, apps, remittance limits, bKash/Nagad routes, the Bangladesh 2.5% incentive, hundi and its risks, remittance cost), Bangladesh Bank remittance-from-Kuwait figures, the KWD->Tk and USD->Tk rates on 9 November 2026 (log the source: Central Bank of Kuwait and Bangladesh Bank), what workers can bring home (customs both sides: baggage rules, gold, mobile phones), bank accounts and salaries paid by bank transfer (Kuwait's wage protection rules), Kuwait's ban on travel for people with debts / travel bans for unpaid bills (with L).

## The doc outline (proposed to the user; follow it)

```
# Kuwait: migration guide
(intro: legend, KWD->Tk rate, BMET, PAM, Ministry of Interior, Sahel, PACI)
## Background
### In one minute
### Is it open now, and who can go?   (#### Status, The channels, Who qualifies, Size, What closed it before)
### How a job reaches you, and who takes a cut   (#### topics)
### What you pay, and what you earn and keep   (#### The cap, What people really pay, How it is paid, How they borrow, What the job pays, What goes unpaid, Money sent home, How long the debt takes)
### What ties you to the employer
### What goes wrong most, and what people wrongly believe
## Visas not open to Bangladeshis
## Work visa: private-sector worker (Article 18)
### Step 1: Find a real job
### Step 2: The job offer and contract
### Step 3: The employer gets your work permit and visa
### Step 4: Passport, police clearance and certificates
### Step 5: Medical check and checking your visa is real
### Step 6: Orientation, BMET clearance and the flight
### Step 7: After arrival
### Scams / Your rights at work / How long you can stay / Your residence permit / What can get you jailed or deported /
### If you aren't paid / If your employer reports you absent / Changing employer or leaving
## Work visa: domestic worker (Article 20)
## Work visa: professional and skilled
## Family visa (dependants)
## Visit visas (tourist, family, business)
## Transit and medical treatment
## Student visa
## Self-sponsorship and investor residence
## Changing visa type
## Asylum
## Having a child in Kuwait
## Sending money home
## Undocumented workers and amnesties
## Going home without valid papers
## If a worker dies, is injured or loses the job
## Coming home
## Contacts
```
