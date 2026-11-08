# Maldives research brief (shared by every topic agent, 8 November 2026)

You are one of eight research agents writing the Maldives doc for the BSAISL Migration Pathway Navigator. Today is 8 November 2026. Repo root: `C:\Users\User\Desktop\Github\bsaisl-migration-knowledge-base` (below: ROOT).

## Read first (binding)

1. `ROOT\CLAUDE.md`: the project, format, quality rules and research process. Binding. Read it in full.
2. The finished docs to imitate in depth, tone and step pattern (read only the parts relevant to your topic, not whole):
   - `ROOT\countries\malaysia\doc.md`: THE TEMPLATE. Look at the Background (H3 parts with H4 topics), "Work visa: company worker (PLKS)" Step 1 and the problem sections, plus any section matching your topic.
   - `ROOT\countries\united-arab-emirates\doc.md`: newest Gulf doc; good for Steps 2-7 and the problem sections.

## The style (what the user approved)

- No SOP section. Procedures are written in place, in the step where they happen.
- Numbered actions, each starting with a bold verb: `1. **Register on OEP,** BMET's website for job-seekers ...`
- Under an action: `You'll need:` (documents, money, phone, photos), then the click-by-click sub-steps as a nested numbered list (exact URL, what to type, button names as on screen), then short bold labels where they apply: `**Check it is real:**`, `**If it fails:**`, `**Scams:**`.
- Ready-to-use wording where a worker must write or say something (sample in quotes with [blanks]).
- Escalation ladders: "If ..., in this order:" then numbered routes, each with phone, link or address.
- Headings: H2 per visa / big section, H3 per step or topic, H4 for topics inside (as in Malaysia). Max H4; below that a bold lead-in. No dates in headings.
- Cross-references use the exact heading text: "(see If you aren't paid)", "(Step 1, item 4)", "(Work visa: company worker, Step 3)". Never "see above".
- Every sentence ends with fact ids in brackets, e.g. `[W0012, N0003]`. No uncited sentence, ever.
- Gaps: a quote block right after the paragraph or step, one precise insider question per bullet:
  ```
  > **Need to know**
  > - What does a Maldives construction-labourer work visa sell for in Dhaka in 2026?
  ```
- Explain every acronym, organisation and platform the first time you use it. No tables. English only. "workers", "people", "migrants", never "beneficiaries". No opinions, no advice of our own.
- State the latest visa refusal, suspension, quota freeze or cancellation status for Bangladeshis wherever it matters (date it).
- Specific beats general: names, numbers, places, dates, the exact counter, form, fee and phone. Write what an insider (agency staff, returnee, caseworker at the Bangladesh High Commission in Malé) would recognise as real.
- Money: give amounts in MVR (Maldivian rufiyaa) or USD as the source does. The lead adds Taka conversions (agent G logs the rate).

## Where you work (important: avoid file races)

Work ONLY inside your own staging folder: `ROOT\countries\maldives\work\<YOUR LETTER>\` (it has a `sources/` folder; some letters already contain pages saved in an earlier attempt today: reuse them, but they are NOT yet registered in sources.csv, so run `facts.py source` for each one you use; if `_fetchlog.csv` is missing an entry, log it with `fetch.py --log <url> <name> manual`). Run every tool from your folder with `python` (not python3), using the path `../../../../tools/`:

```
cd "/c/Users/User/Desktop/Github/bsaisl-migration-knowledge-base/countries/maldives/work/<X>"
python ../../../../tools/fetch.py <url> <name>                 # saves sources/<name>.html|.pdf + text copy
python ../../../../tools/wayback.py <url> <name> official|news # archived copy of a page that won't load
python ../../../../tools/facts.py source --name <name> --publisher "..." --title "..." --official yes|no|archived|news-archived --page-date YYYY-MM-DD|undated
python ../../../../tools/facts.py add --prefix <X> --name <name> --claim "..." --quote "exact words from the saved text copy" --page-date YYYY-MM-DD|undated --status verified|possibly-outdated|conflict|unofficial|lead [--visa .. --field .. --value ..] [--note ".."]
```

- facts.py refuses a quote not found in the saved text copy: copy quotes exactly from `sources/<name>.md` or `.txt`. Keep quotes short (one sentence) and precise.
- Status: official + dated within 12 months = verified; official older or undated = possibly-outdated; news/NGO/guide = unofficial (practice) or lead; conflicting sources = conflict, with a note naming the other id.
- Source names: lowercase, hyphens, start with the publisher (e.g. `immigration-mv-work-visa`, `news-dailystar-maldives-visa-2024-05`).
- Never write to `countries/maldives/facts.csv`, `sources.csv` or `sources/` directly, or to any other country's folder. Never commit. The lead merges your folder.
- Bangladesh-side pages already saved for the UAE or Malaysia (OEP, BMET, PKB, WEWB pages) may be copied from `ROOT\countries\united-arab-emirates\sources\` or `...\malaysia\sources\` into your `sources/` (all files for that name: .html/.md/.txt/.pdf), then logged with `python ../../../../tools/fetch.py --log <original url> <name> manual`. Prefer a fresh fetch when the page loads. Reuse their facts' wording if helpful, but every fact must be logged again in your own facts.csv.
- Official PDFs in `ROOT\official-pdfs\`: read in full; to cite one, fetch its online original or copy it into your `sources/` and log it.

## Blocked pages

If fetch.py fails (403, timeout, empty text), try in this order: (1) Firecrawl, `mcp__firecrawl__firecrawl_scrape` (load it with ToolSearch "select:mcp__firecrawl__firecrawl_scrape" if needed; formats ["markdown"]; `mcp__firecrawl__firecrawl_search` is useful for searching too), then save the markdown with the Write tool to `sources/<name>.md` and log it with `fetch.py --log <url> <name> firecrawl`; (2) `wayback.py`. If all fail, list the page under "c. Blocked pages" (exact URL, suggested file name, what it should prove). Facebook posts of the Bangladesh High Commission in Malé, Maldives Immigration or the Ministry of Homeland Security count as official; if one can't be saved, list it under blocked pages too. Search the web with WebSearch (load via ToolSearch "select:WebSearch") or Firecrawl search.

## Key official sites (start here)

- Maldives Immigration: immigration.gov.mv (visa pages: /visa/work-visa, /visa/tourist-visa, /visa/sponsorship-declaration, /visa/marriage, /visa/dependent, /visa/business, /visa/resident, /visa/meeting; /downloads; /news; /press-announcements; /faqs); IMUGA portal imuga.immigration.gov.mv; Traveller Declaration
- Ministry of Homeland Security and Technology (work permits, Xpat Online xpat.egov.mv, "Kurangi" regularisation); Ministry of Economic Development and Trade (minimum wage); Labour Relations Authority (lra.gov.mv); Employment Tribunal (et.gov.mv); Maldives Police (police.gov.mv); Human Rights Commission of the Maldives (hrcm.org.mv); Maldives Monetary Authority (mma.gov.mv); Maldives Pension Administration Office (pension.gov.mv); Aasandha / NSPA (health insurance); Health Protection Agency; laws (agoffice.gov.mv, mvlaw.gov.mv, gazette.gov.mv); President's Office (presidency.gov.mv press releases, cabinet decisions); Maldives Customs (customs.gov.mv); MIRA (tax)
- Bangladesh: High Commission in Malé (male.mofa.gov.bd), BMET (bmet.gov.bd, incl. pages/miscellaneous-infos permission letters), OEP (oep.gov.bd), Ministry of Expatriates' Welfare (probashi.gov.bd), WEWB (wewb.gov.bd), PKB (pkb.gov.bd), Bangladesh Bank (bb.org.bd), BOESL (boesl.gov.bd)
- `ROOT\agencies\activity.csv` and `agencies.csv`: BMET permission letters by country (5 Maldives letters, 2024: Siam RL1531, The Ifthi Overseas RL0894, North East Overseas RL2199, ZM Tours RL1287, BOESL RL0147 doctors) and agency data
- Other countries' missions in Malé (India, Sri Lanka, Nepal) often publish the most complete worker guides
- News: Maldivian (Sun, Edition.mv, PSM, Avas, Atoll Times, Maldives Independent, The Press, Corporate Maldives, Mihaaru English, Dhauru, Adhadhu), Bangladeshi (Prothom Alo, Daily Star, TBS, Jago News, Bonik Barta, Samakal, Dhaka Post, Kaler Kantho, banglanews24, BSS), in English and Bangla (মালদ্বীপ ভিসা, মালদ্বীপ প্রবাসী, মালদ্বীপে বাংলাদেশি শ্রমিক ...). HRW, Amnesty, Transparency Maldives, ILO, US State Dept TIP report (Maldives chapter) for practice.

## Time limit

About 40 minutes of research, then write your findings file even if some points remain open (list them as Need to know with what you searched). Quality over volume, but cover your whole topic. Don't stop at the first answer.

## Your output

Write `ROOT\countries\maldives\drafts\<X>-findings.md` with:

- **a. Draft doc text:** your sections, written exactly as they should appear in doc.md (headings per the outline, steps, lists, Need to know blocks), every sentence cited with your fact ids. Where another agent's topic is needed, write "(see <exact section heading>)" rather than researching it.
- **b. Notes (for notes.md):** what you searched (sites and search terms, English and Bangla), conflicts between sources (with ids), what happens in practice, facts logged but not used and why.
- **c. Blocked pages:** exact URL, suggested file name, what it would prove.
- **d. Insider questions:** the open Need to know questions, one line each.

Final message back to the lead: 5-10 lines: number of facts and sources logged (official vs news), sections written, the most important findings, and anything the lead must decide.

## Who does what (letter = fact prefix)

- **N** corridor, chain and money in practice: Background drafts (Is it open now: status, channels, who qualifies, size, what closed it before; How a job reaches you, and who takes a cut: work-permit quota, sponsor/"visa" trade, brokers in Malé and Bangladesh; What you pay, and what you earn and keep: real costs vs cap, wages in practice, deductions, debt; What goes wrong most, and what people wrongly believe; irregular routes), the company-worker Scams section, agencies with evidence, insider items (syndicates, crackdowns, the big names). Corridor numbers (BMET yearly flows, stock of Bangladeshis in Maldives, undocumented estimates, comparison with India/Nepal/Sri Lanka).
- **W** Maldives-side work route: Work visa: company worker Steps 2, 3, 5 and 7 (job offer/contract, employer's quota and work permit on Xpat Online, fees, deposit/security, Work Permit Entry Pass, checking the permit/visa is real, arrival: medical, work visa sticker/card, insurance, bank, SIM) and How long you can stay; Work visa: professional (Maldives side: teachers, doctors, nurses, engineers; certificate attestation; MQA (Maldives Qualifications Authority) recognition; professional registration councils).
- **B** Bangladesh side: Step 1 (OEP, permission letters for Maldives, demand-letter attestation at the High Commission's labour wing in Malé, relative's-visa route, cap, PKB loan, complaints), Step 4 (passport, police clearance, certificates), Step 6 (PDO, BMET clearance, smart card, fees, welfare fee, insurance, flights to Malé), Coming home (WEWB reintegration, airport help desk), High Commission services (passport renewal, travel permit), Bangladesh-side contacts. BMET clearance numbers for Maldives by year and month (official).
- **L** law and work: Your rights at work (Employment Act 2/2008 and amendments incl. the 2026 ninth amendment, hours, overtime, leave, minimum wage, passport keeping, housing, Ramadan hours), What can get you jailed (drugs, alcohol, religion, protests, overstay), If you aren't paid (LRA complaint, Employment Tribunal, step by step), If you want to change employer, Leaving at the end of the job, Going home on leave, If a worker dies, is injured or loses the job (compensation, insurance, body repatriation from the Maldives side), pension (does the Maldives pension scheme cover foreigners?).
- **U** irregular status: Undocumented workers: regularisation (Kurangi programme phases, deadlines, fees, how to apply), If your employer reports you absconded, Going home without valid papers (deportation, detention at Hulhumalé/Maafushi, fines, blacklist, bans after you leave), crackdowns/raids 2024-2026.
- **V** visits and short visas: Tourist visa (30 days on arrival, IMUGA Traveller Declaration, hotel booking, money shown, refusals of Bangladeshis at Velana airport), Business visa, Meeting visa, Transit, Medical treatment, Student visa, Visas not open to Bangladeshis (with why), Changing visa type (can a tourist switch to work?).
- **F** family and residence: Dependent visa (family of foreign workers/professionals), Bringing your family (company worker), Marriage visa (spouse of a Maldivian), Resident visa, Having a child in the Maldives, Asylum (written to discourage), Work visa: domestic worker (women; Bangladesh's rules for women going abroad, whether the Maldives takes Bangladeshi housemaids).
- **G** money: Sending money home (MMA rules, USD shortage, limits on foreign currency purchase by expats, banks and money transfer operators in Malé, bKash/Nagad routes, the 2.5% incentive, hundi and its risks, remittance cost), Bangladesh Bank remittance-from-Maldives figures, the MVR->Tk and USD->Tk rates on 8 November 2026 (log the source), what workers can bring home (customs both sides: baggage rules, gold, mobile phones).

## The doc outline (approved by the user)

```
# Maldives: migration guide
(intro: legend, MVR->Tk rate, BMET, Ministry of Homeland Security and Technology, Xpat Online, Immigration)
## Background
### In one minute
### Is it open now, and who can go?   (#### Status, The channels, Who qualifies, Size, What closed it before)
### How a job reaches you, and who takes a cut   (#### topics)
### What you pay, and what you earn and keep   (#### The cap, What people really pay, How it is paid, How they borrow, What the job pays, What goes unpaid, Money sent home, How long the debt takes)
### What ties you to the employer
### What goes wrong most, and what people wrongly believe
## Visas not open to Bangladeshis
## Work visa: company worker (construction, resort, shop)
### Step 1: Find a real job
### Step 2: The job offer and contract
### Step 3: The employer gets your work permit and entry pass
### Step 4: Passport, police clearance and certificates
### Step 5: Check your permit and visa are real
### Step 6: Orientation, BMET clearance and the flight
### Step 7: After arrival
### Your rights at work / How long you can stay / What can get you jailed / If you aren't paid /
### If you want to change employer / If your employer reports you absconded / Leaving at the end of the job /
### Going home on leave / Bringing your family / Scams
## Work visa: professional (teachers, doctors, nurses, engineers)
## Work visa: domestic worker
## Undocumented workers: regularisation
## Tourist visa
## Business visa
## Meeting visa
## Dependent visa
## Marriage visa (spouse of a Maldivian)
## Resident visa
## Student visa
## Transit and medical treatment
## Changing visa type
## Asylum
## Having a child in the Maldives
## Sending money home
## Going home without valid papers
## If a worker dies, is injured or loses the job
## Coming home
## Contacts
```
