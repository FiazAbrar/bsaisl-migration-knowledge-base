# Oman: research notes

Research notes behind `doc.md`: what was searched, conflicts between sources, what happens in practice, facts logged but not used, and pages we could not download. Each section comes from one research topic; fact ids carry that topic's prefix letter. KA to KF are the fact-check pass and KG the final audit.

## How the doc was put together

- Seven topics were researched in parallel (prefixes C, R, E, D, V, P, B), each saving sources with `fetch.py` and logging facts with `facts.py`, then drafting its sections; the lead merged the drafts on the Qatar model.
- **The suspension shapes the doc.** Oman has issued no new ordinary work visas to Bangladeshis since 31 October 2023. The work-visa steps are written for the routes that work today (exempt professions, the 2026 farm-worker quota) and, clearly labelled, for the route as it worked before.
- **Private legal portal.** qanoon.om and decree.om belong to a private company (Decree Tech LLC), not to the Ministry of Justice and Legal Affairs. All facts quoting them were re-marked non-official (status lead); the fact-check then re-sourced most of them to official texts: the Ministry of Labour's Labour Law page and decision PDFs (staff.mol.gov.om, saved through Firecrawl because its file server blocks curl), the Official Gazette PDFs on mjla.gov.om (garbled text layers, read from the page images and logged with --no-quote-check), ROP, gov.om and the Oman News Agency. Facts still on the private portal are listed in `verify/part*-report.md`.
- **Exchange rate.** RO 1 is about Tk 322: Bangladesh Bank's USD rate of 19 October 2026 (archived copy, as for Singapore) and the rial's peg of RO 0.3845 per US dollar from the Ministry of Finance's October 2026 sukuk prospectus; cbo.gov.om blocks automated reading.
- **Junk downloads removed.** Several MoL PDF downloads saved a "Request Rejected" page; they were deleted with their log rows before commit.
- **Pages for a teammate to save in a browser:** the Ministry of Labour's own Labour Law PDF (its web page omits Article 14, paragraphs 2-3), and ROP's PDF of the Foreigners' Residence Law (no text layer; Firecrawl blocked).

## Background and corridor (insider pass) (prefix C)

### Sources and method
- BMET OEP country-clearance JSON pulled with a script (scratchpad oep_pull.py: same request the OEP page makes, `X-Requested-With: XMLHttpRequest`; filters `country_id[]=133` for Oman, `gender_id=2` for women, `all_skills=1` for trade breakdown). Saved as `oep-oman-clearance-YYYY-MM`, `oep-all-clearance-YYYY`, `oep-oman-trades-YYYY`, `oep-oman-women-YYYY`, logged with `fetch.py --log ... manual`.
- BMET annual table 2004-May 2025: copied `bmet-annual-by-country-2025-05-img` (jpg + md) from the Qatar folder; the Oman column was transcribed by hand (crop enlarged 3x) and appended to the oman copy of the .md.
- NCSI Monthly Statistical Bulletin Oct 2026 (official PDF). Layout text garbles table 18; a raw-mode text copy of page 21 was saved as `ncsi-monthly-bulletin-2026-10.p21-raw.txt` and quoted from it.
- Labour Law quotes from decree.om English translation (registered non-official, as other agents did); Omanisation decisions 235/2022 and 501/2024 from qanoon.om Arabic (non-official copy of the Official Gazette). Facts logged as `lead`.
- Copied `bb-visa-fraud-airport-ac` from agencies/ (files, fetchlog row, sources row).
- Scraped with Firecrawl and saved as .md: Oman Observer July 2025 expat drop; Dentons 2020 NOC note.

### Conflicts and oddities
- 2024 clearances: OEP 357 (C0021) vs BMET annual table 358 (C0001). Doc uses OEP for 2024-26, the annual table for 2014-23 (OEP holds only part of 2022: 7,369 vs 179,612).
- 2023: OEP 127,822 vs annual table 127,883.
- NCSI table 18: the "-3.4%" change column does not match Sep 2026 vs the "2025" column (599,070 vs 612,208 = -2.1%); percentage not used.
- Number of Bangladeshis in Oman: 800,000 (Prothom Alo, Nov 2023, of 2 million workers), 700,000+ (embassy via BBC), 703,840 (NCSI July 2023 via TBS), 637,152 (Jun 2024), 621,048 (Jun 2025), 599,070 (Sep 2026 NCSI). ILO 2021: embassy estimate 750,000 vs Omani 546,681 (Oct 2020).
- Count of open categories: Oman's embassy list (C0032) vs "13 categories" quoted by Bangladeshi officials (C0072, C0073); TBS May 2024 said 12. Doc gives the embassy list and the 13.
- Times of Oman H1-2026 violations article: page date logged as 2026-07 (approximate; article gives no date in the saved copy).
- Ali Haider Chowdhury (BAIRA secretary-general, 2023) said 80% go individually; consistent with ILO on migrants as recruiters.

### Facts logged but not used in the draft
- C0003 (2004-13 series), C0007-C0012 (Jan-Jun 2023 months), C0019 used; C0025 (2024 trades), C0036-C0038 (TBS May 2024 reasons/10,000 a month/remittance FY22-23), C0057 (1.06 lakh to Sep 2023), C0060, C0063 (counts superseded by NCSI), C0074 (Bangladeshi businesses in Oman short of staff: could go in "Where it may grow"), C0080 (BOESL MD quote), C0100, C0109 (duplicate of C0108), C0062 used, C0068 (visit visas; partly used). Reason: duplicates or older numbers superseded by NCSI/OEP.

### Searched, not found (Need to know kept)
- Deaths of Bangladeshis in Oman by year: palo-migrant-deaths-2026, alap.news deaths article and WEWB annual report 2023-24 give no Oman figure.
- Any pre-2023 Omani ban on Bangladeshis: not found in this session.
- Prices of Oman visas in 2023 and of the 2026 farm visas: only social-media claims (FB post: "Tk 4-5 lakh visa to ticket"), not logged.
- Prosecutions of Omani sponsors/Bangladeshi brokers for visa trading since 2023: none found.
- BBS Cost of Migration Survey 2020 PDF (`bbs-cost-of-migration-survey-2020`, ILO-hosted) is a scan with no text layer and no OCR available; Oman figure Tk 3.08 lakh taken from Daily Star's report (C0103). Ask someone to read the Oman table in the PDF.
- Whether Oman's minimum wage (RO 325 for Omanis) applies to expatriates: Labour Law leaves it to ministerial decision (C0123); the 90-rial figure is the bilateral agreement per ILO 2021. Official text of that agreement not found.

### Pages we could not download
- decree.om MoL Omanisation statement (https://decree.om/2025/mol20259902/) and English MD 235/2022, 501/2024: members-only; files deleted (fetchlog rows remain under names decree-om-mol-statement-omanisation-2025, decree-om-md-235-2022-professions, decree-om-md-501-2024-professions). Snippet says >245,000 establishments employ no Omani but >1.1 million expatriates.
- Oman Observer "11172 expats booked for labour violations" (https://www.omanobserver.om/article/1194240/...) not fetched; Times of Oman version used.

## Work visa: recruitment and getting there (prefix R)

### Status, 9 Nov 2026
- ROP suspended all new visas for Bangladeshis from 31 Oct 2023 (R0024). June 2024 exemptions via Oman Embassy Dhaka: family, GCC-resident visit, physicians, engineers, nurses, teachers, accountants, investors, official, high-income tourists (R0021). No unskilled category.
- Jan 2026: Omani labour minister promised reopening in two months (R0011). Did not happen: Sept 2026 State Minister said access still restricted (R0019).
- Aug 2026: 5,000 farm-worker quota via agricultural associations (Al Dhahirah branch applications 9-20 Aug) (R0006-R0010). Embassy Muscat (12 Aug 2026) said this is not a market opening (R0106-R0109). Sept 2026: Bangladesh says Oman wants 5,000 farm + 5,000 fisheries workers, agreement signed, Omani team due Oct 2026 (R0018). Outcome of that visit not found.
- BMET monthly clearances to Oman pulled by month from OEP's JSON (sources/oep-oman-monthly-clearance-2025-2026.md/.json): 2025 total 671, with a spike of 451 in Nov 2025 and 137 in Dec 2025; 2026: Jan 12, Feb 4, Mar 1, Apr 0, May 16, Jun 3, Jul 49, Aug 96, Sep 27, Oct 219, 1-8 Nov 79. The Oct-Nov 2026 rise may be the farm quota; unconfirmed.

### Sources and conflicts
- Qanoon.om: I registered MD 602/2025 and ROP 157/2025 as official=yes (Arabic gazette text). Another agent registered qanoon.om's Labour Law as official=no, and the site's footer says it is not an official source. Lead should harmonise the flag across the folder.
- Labour Law facts (R0042-R0056) quote decree.om's English translation (registered by another agent as official=no); logged as status "lead". The Arabic text is in qanoon-om-labour-law-rd53-2023-ar if an official-status quote is wanted.
- MD 602/2025 (in force ~26 Jan 2026) replaced MD 340/2016. Fees now RO 301/251/201 by category (company employers), x0.7 if Omanisation met, x2 if not. The brief's "how the permit fee changed in 2023-24": I did not find/fetch the 2023 reduction decision; the 2021 PwC alert (RO 2,001 top tier) is in search results only. Need a teammate to fetch the 2021 and 2023 MoL fee decisions from qanoon.om if the history matters.
- ROP work visa page (rop-visa-types) still says "Ministry of Manpower" and asks for a release letter within two years of last departure: old page (NOC rule abolished 2021 per secondary sources, not verified). I did not cite the release-letter line.
- Resident card: ROP page says RO 6/1 yr, RO 11/2 yrs (old); ROP Decision 157/2025 (OG 1621, 9 Nov 2025) sets RO 5 per year up to 10 years and RO 20 replacement. Draft uses the decision.
- BMET charter's online visa check list (Saudi, Qatar, Bahrain, Singapore, UAE) excludes Oman.
- Bangla quotes from BMET charter, welfare circular, safe-migration leaflet and PKB pages were re-quoted from Singapore facts with --no-quote-check (text layers garbled; Singapore transcribed from page images). Notes on each row name the Singapore id.
- Cost cap Tk 1,00,780 for Oman: Bangladesh Bank 2019 table + Prothom Alo 2018. No newer order found.

### Permission letters
- BMET list search for ওমান/Oman: no results. agencies/activity.csv identifies 4 Oman letters (Aug-Oct 2023): ProSearch RL1027 x2 (Galfar, 250 helpers at RO 100), Ahmed & Company RL0081 x2 (Al Naba 30 dish washers RO 90; Asyad Dry Dock 90 trades RO 186). PDFs saved as bmet-perm-om-*. Bangla pages (maximum fee the agency may take) are scans; pdftoppm not installed so I could not read the images. Need a teammate to read page 2 of each PDF for the Tk cap.
- The Al Naba demand letter shows Embassy Muscat attestation signed by Mohd Rafiul Islam, Counsellor (Labour); block visa numbers use format BEM/04/010/2023-NNN.

### Practice
- Medical rackets: TBS Bangla Sep 2025 (R0079-R0085), Daily Star Jul 2025 (R0086-R0091). Named syndicate figures in Daily Star not used (allegations about private individuals; could go to Background with attribution).
- Free visas: OKUP survey via Inside Business Mar 2026 (R0158-R0160); Bangla Telegraph 2018 (20,000 Bangladeshis detained) (R0156-R0157).

### Logged but not cited
R0005 (Aug/Sep 2026 counts: kept for Background), R0006/R0107 (duplicative), R0012/R0013/R0014 (Background), R0040/R0041 (category upgrade, regularisation fines: belong to changing employer/absconding sections), R0046/R0048 (Art 28, covered by others), R0075/R0077 (dupes), R0079/R0080/R0082/R0091 (medical racket detail, usable in Background), R0101 (dupe), R0103 (dupe), R0111 (CDA contact: for Contacts).

### Gaps (searched, not found)
- Embassy Muscat demand-letter attestation procedure and fee: embassy attestation page renders empty (curl and Firecrawl); consular fee list has "Attestation of Commercial Documents" RO 11.600 and "Visa online registration" RO 7.000, purpose unclear. Need to know.
- No public ROP check for a worker to verify an employment visa by passport number found; eVisa status is sponsor-login only.
- MoL Omanised-occupations list for 2026 not fetched.
- Oman Embassy Dhaka procedure for exempt professions not found.

### Pages we could not download
- https://muscat.mofa.gov.bd/pages/static-pages/6952667135ce18e1c05a91f2 (Attestation page: content loads by script; curl and Firecrawl both empty).
- https://decree.om/2025/mol20250602/ (English MD 602/2025: paywalled; used Arabic qanoon.om instead; files deleted, fetchlog row remains).
- Oman Observer article body did not load by curl (observer-bangladeshi-farm-worker-visas); saved Firecrawl copy as observer-bangladeshi-farm-worker-visas-fc.

## Work visa: rights and life in Oman (prefix E)

### Source status: the Labour Law text (important for the lead)

- decree.om (English) and qanoon.om (Arabic) are both run by **Decree Tech LLC, a private company** (decree.om/about), not by the Ministry of Justice and Legal Affairs. decree.om states Arabic is the only official text. MJLA hosts the Official Gazette PDF (mjla.gov.om/laws/ar/1/show/199) but its text layer is garbled; the FAOLEX copy of OG 1504 was also garbled and was deleted.
- I registered decree.om English as `official no` and logged its facts as `lead` (E0001-E0113 range). Where the official MOL Arabic page "حقوق وواجبات العامل" (mol.gov.om/pages/Employee-Rights-And-Duties) quotes the same article, I logged that too as official (contract, probation, hours, overtime, weekly rest, annual/sick/special leave, Art. 9 disputes) and cited both.
- Other agents registered qanoon.om texts as `official yes` ("MJLA text via Qanoon.om"). I did the same for RD 60/2025 but `no` for MD 729/2024 and the Narcotics Law. **The lead should pick one rule and re-mark consistently.**
- Consolidated text runs to RD 66/2026 (repealed Art. 146 only). English consolidated text, MD 729/2024 English, SPF Decision C/13/2026, the Foreigners' Residence Law, Penal Law and Narcotics Law English are paywalled on decree.om; Arabic versions on qanoon.om were used.
- MOL's English leaflet (mol.gov.om/Content/Arabicpdf/Guidlinepdf/English-pdf.pdf) refers to Law 35/2003: used only for practical lines (80077000, "employer pays licence/ID/residence fees", "tell your boss if card not done in a month"), all possibly-outdated. It says termination complaints within 15 days; current law says 30 (E0021) — used the law.

### Key findings

- No minimum wage for foreigners (US HRR 2023, E0238).
- WPS: MD 729/2024, 3 days; 75% coverage from Sept 2025 wages, 90% from Nov 2025; RO 50/worker fine. TIP 2025: only 25% of firms compliant. No source for 100% phase.
- SPF: sick/other leave insurance for expats from 19 July 2026 (SPF Decision 13/2026, via DLA Piper; SPF page says employer pays and is reimbursed). **Work-injury insurance for expats postponed to July 2028** (RD 60/2025: 5 years from July 2023). Provident savings scheme replacing gratuity by July 2027 at latest (9% per Middle East Briefing).
- Gratuity under new law: 1 month basic per year (Art. 61) until savings scheme.
- Residence card: up to 10 years, RO 5/year, RO 20 replacement, renew within 30 days (ROP Decision 157/2025, Nov 2025). ROP visa page: RO 50/month late renewal fine (undated); first card page: RO 10/month. Six-month absence rule from Foreigners' Residence Law Art. 18.
- NOC abolished from 1 Jan 2021 (ROP 157/2020) for end-of-contract moves; MOL still approves; mid-contract still needs employer, release fees common (TIP 2025, up to US$3,900).
- Desertion reports: filed by employer after 7+ days' absence on MOL service; requires pay statements and employer pays ticket price; worker appeals via "Appeal Against Desertion Report for Individuals". 2025 amnesty (1 Feb-31 Dec 2025) allowed cancelling reports; no confirmed 2026 successor (a Facebook post mentions a one-year grace after "new regulations", unverified).
- Midday ban 1 June-31 Aug, 12:30-3:30; fines RO 500-1,000 (news). MOL Safe Summer guidance in Bengali.
- Health insurance (Dhamani): pilot launched 20 April 2025; could not confirm enforcement of compulsory employer-paid cover for workers (sanadservice.com guide claims it is mandatory; not used, unofficial and unverified).

### Conflicts

- Late residence renewal fine: RO 50/month (rop-visa-types) vs RO 10/month for late first card (rop-resident-card-first-issue); different services, both kept.
- Family threshold: ROP page RO 600 vs ROP official in 2023 RO 150 (P covers this).
- Embassy address: Villa 4207 Way 3052 (letterhead) vs booking portal; B raised it.
- Labour wing contacts from Ministry list dated 1 May 2025 (possibly outdated); Embassy service-cell notice 14 Dec 2025 gives a workers' landline +968 24603514.

### Logged but not used

- Juvenile, union-federation, collective dispute committee details; MD 602/2025 fee exemptions for employers (E0165-E0168, partly used); temporary transfer decision (E0182); Indian embassy helpline used only as a comparison in a Need to know.
- Sonali News 2018 (women stranded in an Embassy safe home, told to pay own fare) and Jagonews 2018 (20,557 Bangladeshis detained in Oman over free visas) read; Jagonews blocked (403), not logged; domestic-worker side belongs to D.

### Pages we could not download

- https://www.jagonews24.com/probash/article/450748 (403)
- https://www.tamimi.com/our-knowledge/publications/eyes-on-2026/articles/omani-social-protection-law-key-timeline-extensions-under-sultani-decree-60-2025/ (307 redirect)
- https://natlex.ilo.org/dyn/natlex2/r/natlex/fe/details?p3_isn=115199 (403)
- MOL English site (cookie language switch fails; pages come back in Arabic)
- decree.om members-only pages (above)

### Small data issue

- `govom-mol-noon-work-permit` registered as undated in sources.csv but the page shows "Updated: August 18, 2026"; facts use 2026-08-18. `mol-om-employee-rights-duties` dated 2026-11-09 from its footer "آخر تحديث", which may be auto-generated.
- One row (first E0011, Art. 10) was dropped by a concurrent write and re-logged as E0021; all 228 cited ids were checked present in facts.csv at hand-back.

## Domestic workers (prefix D)

Facts logged: D0001 to D0218 (218). Cited in draft: 190.

### Key findings
- **Route closed in practice.** OEP (country id 133, gender_id=2): women cleared for Oman 6,636 (2023), 560 of them Nov-Dec 2023 on pre-suspension visas, 56 (2024), 5 (2025), 3 (1 Jan-8 Nov 2026). Domestic workers are not in the June 2024 exempted categories (BSS). OEP 2022 figures are incomplete (13,445 total vs ~179,611 reported by BMET), so pre-2023 women counts come from news citing BMET (New Age 2016, ILO 2021, Prothom Alo 2023).
- **New law: MD 574/2025** (signed 9 Oct 2025, OG 1617, in force 13 Oct 2025, 3 months to comply) replaced MD 189/2004. 12 occupations incl. private driver and farm worker. Min age 21; 12 h/day max with 8 h rest; 1 day off; 30 days sick; 21 days leave; half-month gratuity per year after 2 years; passport only with written consent; no fees from worker; disputes via Labour Law art. 9, no court fees; fines RO 50-500. No minimum wage. No provision on phones. No clear right to change employer without consent.
- **MD 390/2026** (11 Oct 2026, OG 1669) replaces the 2011 recruitment-office regulation from 1 Jan 2027: domestic workers only via licensed offices (RO 100 fine otherwise), written job offer before arrival, 45-day delivery, insurance incl. ticket home, 2-year refund guarantee, 180-day temporary permits (RO 26) with 60%/100% wage allowance, office may claim recruitment costs from a worker who "leaves without legal reason" (art. 33). Fee cap to be set by separate ministerial decision (not yet found).
- **Fees:** MD 602/2025 annex 2: RO 101/worker (1-3 domestic workers), RO 141 from 4th; farm/herder/guard RO 141. ROP visa RO 20 (Gov.om, updated 10 Aug 2025).
- **Bangladesh side:** 2016 Oman housemaid guideline (New Age, BD24Live): effective 16 Oct 2016, age 25-45, min wage Tk 18,000 = RO 90, sponsor income ≥ RO 1,000, free migration, embassy attestation of contract, Tk 300 affidavits. Official text not found. 2025 21-agency zero-cost rule and housekeeping course reused from Singapore folder.
- **Abuse/practice:** HRW 2016 (UAE–Buraimi trafficking, "sold" women, release fees, police returning workers), US TIP 2025 (release fees, passport taken at airport, social-media intermediaries, shelter rules, hotlines with Bengali speakers), ILO 2021 (Embassy ran two safe homes in Muscat, 60 places, ~20 occupants; RO 80 paid to first-timers; no NGO shelters), Daily Star Bangla 2021 (returnee who gave birth in deportation camp).

### Conflicts / decisions
- **qanoon.om status:** brief calls it MJLA's portal; agent E registered qanoon/decree.om as Decree Tech LLC ("no"). I registered qanoon-md574-2025-domestic-workers and qanoon-md390-2026-recruitment-offices as official "yes" (publisher text says "via Qanoon"). Lead should make this consistent. Tried the official gazette PDFs on mjla.gov.om (download.php?file=1190 = issue 1669); text layer has no usable Arabic, deleted.
- Labour Law art. 2 (D0213-D0215) cited from decree-om English translation, registered "no" by agent E, so status lead.
- Labour wing contacts differ: probashi-labour-wings (counselormuscat@probashi.gov.bd, +968 2469 8440) vs embassy officers page (clomanbd@mail.com, logged by R/B). Need to know in draft.
- TIP 2025 still describes MD 189/2004 (reporting period 2024), predates MD 574.
- HRW report: used agent's saved file hrw-i-was-sold-oman-2016; my duplicate fetch (hrw-i-was-sold-oman-2016-report) deleted, fetchlog row remains.
- D0008 originally assigned to Oct 2023 women (492) was dropped by a concurrent write; re-logged as D0071. All 190 cited ids verified present at hand-back.

### Logged but not cited
D0010 (3-month compliance), D0020/D0021/D0031/D0032 (employer duties detail), D0062, D0073-D0074, D0077, D0082, D0088, D0093, D0095, D0097-D0098, D0104, D0115-D0116, D0141-D0143, D0177, D0187 partly, D0206 (Indian embassy comparison: RO 1,000 salary, RO 1,100 guarantee, age 30-50) — detail or comparison not needed in the steps; available for Background.

### Searched without result
- Migrant-Rights.org analysis of MD 574/2025 (none found).
- Official text of the 2016 Bangladesh Oman housemaid guideline; current Embassy housemaid attestation page (muscat.mofa.gov.bd attestation page lists no housemaid item).
- ROP trafficking hotline and MOSD shelter hotline numbers.
- Recruitment-office fee cap in Oman; Bangladesh rules for men as house drivers.
- Bangla news on 2024-2026 women returnees from Oman (results were mostly Saudi).

### Pages we could not download
- https://www.hrw.org/sites/default/files/report_pdf/oman0716web.pdf (404; HTML report used).
- https://thefinancialexpress.com.bd/home/bangladeshi-women-get-lowest-wage-in-oman-study-1611111715 (body not captured; deleted).
- https://decree.om/2025/mol20250574/ (paywall; deleted).

## Visit, business, student, transit and medical visas (prefix V)

Researcher prefix V. Facts V0001 to V0167. Work done 9 to 10 Nov 2026.

### Key finding: what ROP's own system shows on 9 Nov 2026

- ROP's public eligibility wizard (evisa.rop.gov.om/visa-eligibility) was run by posting its form (no login, no CAPTCHA). Answers: nationality BANGLADESH, not a GCC resident. Result: only 33A Property Owner Visa (RO 50). No 26 tourist visit visa, no 36 one-year visa, no 12B truck driver, no 26E-H family-companion forms (Nepal and India get these; Pakistan also gets only 12B and 33A). Saved as `rop-evisa-eligibility-*.md` (V0046, V0050, V0051, V0069). This is the strongest dated official evidence that the Bangladesh restriction is still live in ROP's system.
- Bangladeshi resident in UAE: 28B (free), 29A (RO 5), 29B (RO 5) offered (V0047-V0049). Matches the June 2024 exemption "visit visas for Bangladeshis residing in GCC countries".
- Visa type tables saved by posting the "View Visa Types" form for each class (`rop-evisa-types-*.md`). Some apostrophes are garbled (вҖҷ) in the saved text; quotes avoid those spots.
- The "Track Your Application" page has a CAPTCHA; not automated. Only the field list was saved (V0128).

### Status evidence chain

- 31 Oct 2023 ROP suspension of all new visas for Bangladeshis + end of visit-to-work conversion for all nationalities (Times of Oman, Daily Star, BBC Bangla, Prothom Alo: V0070, V0071, V0097, V0077-V0079, V0094-V0096).
- 12 Jun 2024 Oman Embassy Dhaka note: exempted categories, processed by the Embassy in Dhaka with attested documents, 1-4 weeks (Oman Observer, BSS, Samakal, Deloitte: V0072-V0076, V0098, V0099). Samakal says "8 categories"; the list itself has more items. No official Omani copy of the note was found (searched fm.gov.om, rop.gov.om, gov.om).
- 22 May 2026 fm.gov.om: Oman ambassador met VFS Global on "processing of visa exempt applications for business and tourism categories" (V0109). Suggests exempted business/tourism applications may move to VFS in Dhaka; no VFS Oman page for Bangladesh found.
- Sep 2026 Migrantimes: State Minister Shama Obaed said visa access still restricted (V0100).
- Jan 2026 BSS/Bonik Barta: Omani labour minister promised work visas within two months (logged by other agents, not used by me).

### Conflicts

- GCC resident visa residence validity: e-visa conditions say 6 months remaining on entry (V0054); gov.om says valid residency of no less than 3 months (V0159). Shown as Need to know.
- "Family visa" on gov.om (V0090-V0093, RO 30, employer's request, spouse/children must reside in Oman) is not clearly the same as e-visa type 4 Family Visit Visa (V0014, V0015). Treated as the family visit route; flag for the family-residence agent (P) to check against the family joining visa.
- 14-day visa-free: fm.gov.om (updated 22 Sep 2026) says "more than 100 countries"; ROP's own List 1 + List 2 total 104 (80 + 24). Consistent.

### Logged but not used

- V0003, V0004 (type descriptions, superseded by wizard conditions V0052-V0066); V0011 used; V0021 (quote truncated by my error; replaced by V0023); V0025 used; V0035 (duplicate of V0041); V0042 used; V0050 used; V0082 used; V0106 GCC citizens (not relevant to Bangladeshis); V0108 used; V0113/V0114 used; V0120 used; V0126, V0127 (labour-law recruiting fee ban and passport retention: belong to the work-visa section; offered to the lead); V0148 used; V0163 (quote does not support "request letter"; not cited).
- Facts from Labour Law are from decree.om's English translation (registered unofficial by another agent), so cited as [N]. The Arabic text on qanoon.om (also unofficial site) matches Art. 143(5). The Foreigners' Residence Law is from qanoon.om (consolidated to RD 60/2021), registered official=no; mjla.gov.om has the original decree but I did not fetch it. Lead: replace with mjla.gov.om or ROP's PDF (rop.gov.om/pdfs/roplaws/ROPRULE-7.pdf) for official citations.
- RD 66/2026 repealed Labour Law Art. 146 only; Art. 143 (working without a permit) still stands.

### What happens in practice

- BBC Bangla (2023): Bangladeshis rarely went on tourist visas but many went on "visit visas" (in practice the sponsored visit route sold with a job promise) and found no work; embassy saw 50-100 such people a day.
- BD Digest (Oct 2025, not logged, not Oman-specific): Bangladeshi passport holders face offloading and refusals across Asia/Gulf; Dhaka immigration screens tourist travellers. No Oman-specific offloading evidence found.
- Jagonews (2018, not saved, free-visa scam, 20,557 Bangladeshis detained in Oman): relevant to work-visa scams, not visits; read via Firecrawl but not logged because it's old and outside my scope.

### Searches done

ROP site and e-visa portal (FAQ, types, eligibility wizard for BGD, BGD-UAE, IND, PAK, NPL, IDN; conditions 29A/29B/28B; occupations list; track page); gov.om service pages (visit extension, family visa, student, express, sponsored tourist, GCC resident, multiple entry, one-year, airport transit, e-auth news); fm.gov.om (entry visas, Dhaka embassy, Bangladesh tag, VFS, e-attestation, foreign embassies list); qanoon.om residence law; labour law (other agents' copies); Muscat airport FAQ and transfer pages; universities (MEC, Muscat College, NU, MoHERI private HE page); Bangla searches (ওমান ভিজিট ভিসা, ভিজিট ভিসায় ওমান প্রতারণা); English searches on visitor insurance, fake visa sites, Dhaka offloading.

### Gaps (also in draft as Need to know)

- No official text of the June 2024 embassy note; no Oman Embassy Dhaka visa page with hours/fees.
- Whether ROP accepts sponsored tourist, family visit or express visas for Bangladeshis online now.
- Definition of "high-income tourist".
- Visitor health insurance requirement for visa holders (only visa-free visitors need it per fm.gov.om).
- Refusal reasons, appeal, refunds.
- Patient/emergency visa fees and whether open to Bangladeshis.
- MoHERI's list of institutions approved to host foreign students; whether student visas are issued to Bangladeshis under the suspension.
- Business visa (types 5, 10) fees and durations.

### Pages we could not download

- https://www.jagonews24.com/probash/article/450748 (curl 403; read via Firecrawl, not saved)
- https://www.gutech.edu.om/international-office/ (curl 403; not retried; says international students may not work off campus per search snippet)
- https://uob.edu.om/en/student-affairs/international-students/admission-requirements (renders empty; files deleted)
- https://www.omanair.com/en/on-arrival-info (empty; files deleted)
- evisa.rop.gov.om track page results (CAPTCHA; not attempted)

### Mis-named saved files (ignore)

- `fm-om-dhaka-vfs-visa-exempt-2026` actually holds the 10 May 2026 article (ambassador meets State Minister); the VFS article is `fm-om-dhaka-vfs-2026-05`.
- `fm-om-e-attestation-bangladesh-2026` actually holds the 50-years-of-relations article; the e-attestation article is `fm-om-eattestation-launch-2026-02`.
- `fm-om-tag-bangladesh` and `fm-om-dhaka-vfs-visa-exempt-2026` are unregistered and unused.

### Data-integrity note

One of my facts was dropped by a concurrent write to facts.csv (two adds printed V0090); re-logged as V0093. All 154 ids cited in V-visits.md were checked present in facts.csv on 10 Nov 2026.

## Family visas, investor residence, changing visa type, asylum, children (prefix P)

### Sources and method

- Law texts read in Arabic on qanoon.om (free): Foreigners' Residence Law RD 16/95; ROP amendments to its Executive Regulation (63/96): 204/2017 (fee table), 129/2018, 35/2019 (joining visa and residence, age limits), 157/2020 (no-NOC transfer, family follows), 142/2021 and 234/2021 (conversion of visas; investor fees), 132/2024, 156/2025 (cultural visa), 87/2026 (property owner residence); Civil Status Law RD 66/99 and amendments 78/2025 and 157/2025 (resident card fees); Basic Statute RD 6/2021; Penal Code RD 7/2018 (Art. 259, 315); MoL Decision 602/2025. The consolidated Executive Regulation is paywalled on decree.om and qanoon.om only has the 1996 PDF, so the current text was rebuilt from amendments.
- ROP's visa pages (English and Arabic) are stale: they still say Ministry of Manpower, RO 600 and RO 20/30 fees that conflict. Gov.om service pages (ROP, updated 2025-2026) were used for current fees.

### Conflicts

- **Family salary threshold.** ROP English and Arabic "family visa" pages: RO 600 + senior job + housing (P0007). Press: RO 600 -> RO 300 or RO 350 (2017; Oman Observer says 300, Migrant-Rights says 350) -> RO 150 (Feb 2023, ROP official, Times of Oman P0019). Migrant-Rights (June 2023) found no official statement (P0022). Gov.om page (May 2026) gives no threshold (P0004). No ROP decision found on qanoon.om changing it. Kept as Need to know.
- **Family visa fee.** Gov.om RO 30 (P0002) = Decision 204/2017 table (P0029); ROP Arabic joining page says 20. Used 30.
- **Resident card fee.** ROP page RO 6/RO 11 (stale, P0063); Decision 78/2025 RO 5/10/15 for 1-3 years (P0079); Decision 157/2025 RO 5 per year, up to 10 years (P0067, in force from 10 Nov 2025). Used 157/2025.
- **Golden Residency minimum.** Deloitte/UGlobal: RO 500,000 (10 y) and RO 250,000 (5 y). Operator Migrate World (omangoldenvisa.com): RO 200,000 combined for 10 years across seven options (P0164). Need to know.
- **Conversion visit->work.** Regulation (234/2021) allows conversion of any Art. 10 visa; ROP suspended tourist/visit conversion from 31 Oct 2023 (P0112). Fragomen says suspension covered "dependent" visitor visas too (P0114); unclear whether joining residence -> work inside Oman is possible.
- **Under-6 passport photo.** Muscat Embassy: white background (P0087); epassport.gov.bd (Qatar S0129): grey background. Used Embassy's.
- P0151 mislabelled the 15-year rule (it is the naturalisation requirement); replaced by P0152. Do not cite P0151.

### What happens in practice

- Family visas for Bangladeshis reopened June 2024 (Oman Embassy Dhaka note) and are reported open in July 2026 (VisaBangla).
- Facebook/TikTok creators in Oman (Musa Emon, probashichannel1) allege broker rings using fake kabinnama to bring women as "wives" who then work as domestic workers, and warn Oman may close family visas to Bangladeshis. Could not be saved (Facebook not scrapable); kept as Need to know. TikTok claims government fee RO 30 plus typing charge.
- Migrant-Rights 2020: babies' documents held until hospital debt paid / marriage certificate shown; domestic workers hide pregnancies.

### Logged but not used

- P0006 (2-year validity on stale ROP page; validity now set by card rules), P0008, P0023, P0030, P0044 (cruise/emergency extension), P0049 (Art. 14 visit sponsors), P0053-P0055, P0059, P0062, P0078 (birth certificate signature), P0082, P0151 (wrong), P0171, P0173 (employer fine; belongs in work section), P0156 partly.
- National Records Law regulation 84/2026: not about births; registered, not used.
- ARIJ "Born without documents" (Jordan, 2025): Bangladesh Embassy in Amman says it cannot document children without a marriage/birth record. Jordan-specific; registered, not used.
- Decision 157/2026: good-conduct certificate for foreigners RO 20 (useful to other sections; not logged by P).

### Searched, not found

- Official Muscat Embassy birth-registration document list (process page 404).
- Newborn residence deadline and fine in Oman; who sponsors a domestic worker's baby.
- Oman Embassy Dhaka attestation fee for nikahnama.
- Whether ROP accepts Bangladeshi e-Apostille.
- UNHCR office arrangements for Oman.
- Domestic worker -> company job rules.

### Pages we could not download

- https://muscat.mofa.gov.bd/pages/static-pages/695266b335ce18e1c05aada2 (Embassy birth-registration process/FAQ: 404, also via Firecrawl)
- https://www.facebook.com/probashichannel1/posts/1619615032939816/ (family-visa fake kabinnama allegation; Firecrawl unsupported)
- https://portal.omanresidence.gov.om (Golden Residency portal; JS app error)
- decree.om/1996/rop19960063, decree.om/2026/rop20260087, decree.om/2025/rop20250156 (paywalled; Arabic texts used from qanoon.om)

## Money, going home, coming home, contacts (prefix B)

Facts logged under prefix B: B0001-B0266 (266; 206 official, 60 news/guide). All 253 ids cited in drafts/B-bangladesh-side.md exist in facts.csv (checked 2026-11-10).

### Copied from Singapore (re-quoted)

126 Bangladesh-side facts re-quoted from countries/singapore (WEWB, Ministry charter, BMET, PKB, JBC leaflet, NRCTA circular, WEDB, Probash pension, baggage rules, HSIA customs, BB drawing arrangements, BB FE circular, budget speech, MTB guide, Prothom Alo death and insurance stories, TBS loan story, BRAC pages). Sources copied with fetchlog and sources.csv rows. Mapping kept in the scratchpad idmap.csv; Singapore id is in each row's note ("Re-quoted from singapore Bxxxx"). Also copied: Nagad (B0229) and BB cost Table 1 (B0230).

### What I searched

- Bangladesh Embassy Muscat: muscat.mofa.gov.bd (JS-rendered; curl gives only the shell plus the live service-cell box, so pages saved via Firecrawl as *-fc), amardutabashmuscat.org (booking portal), its four Google Drive notices (fee list, scheduling, bank payment, service cell). The three scanned notices have no text layer; hand transcriptions saved as *-transcription.md.
- Oman: gov.om (Pay Fines Upon Departure, Record Labor Complaint), ROP exit penalty service, qanoon.om (Foreigners' Residence Law, MD 602/2025, Banking Law RD 2/2025), CBO money exchange list, Oman Customs traveller page, OHRC complaint page, MoL call centre (from mol-om-employee-rights-duties, fetched by another agent), Oman MFA page for the Dhaka embassy (fetched by another agent).
- Other embassies in Muscat: India (death cases, costs) and US (repatriation of remains).
- News: Oman Observer, Times of Oman (2025 grace period), BSS (Jan 2026), AkashJatra (2020 outpass notice), Amader Shomoy (2025 Salalah tour), Jago Bangla (2026 misattributed story), Daily Star Bangla (deaths), Times of Oman (Aug 2026 hawala arrest), Lockton (work injury), KPMG (WPS), Sanad Office guide (lead only, not cited; used to find official sources).
- Bangladesh Bank: country-wise annual and monthly remittance tables; remittance cost PDF (page image read to fix the text layer's row shift: Oman up to USD 200 = 6.06/6.77, not 1.36/1.57).

### Conflicts and oddities

- Embassy address: letterhead and the mofa site say Villa/Building 4207, Way 3052, Shatti Al Qurum; the booking portal says Villa 3126 A-B, Way 3040, Shati Al Qurum (B0127 vs B0150, B0162). Kept as Need to know.
- Embassy hours: website banner and portal say Sun-Thu 8:00-4:00; the service-cell notice gives landline hours 8:30-4:30.
- Counsellor (Labour) email is printed as clomanbd@mail.com (not gmail) on the officers list (B0158). Head of Chancery phone printed with an extra digit (+968 246980843); not used.
- No Travel Permit fee in either Embassy fee list (Mar 2026 PDF, Jun 2026 page). In 2020 the Embassy said outpasses were free (B0193). Need to know.
- bKash lists "Oman International Exchange" and "Gulf Exchange Oman" as partners; neither is on CBO's list of 17 exchange companies (CBO page undated; could be outdated or names differ).
- ROP's work-visa page reportedly gives an RO 50/month renewal-delay fine, against gov.om's RO 20/day residence overstay fee (via Sanad guide; not verified by me; Need to know).
- Foreigners' Residence Law on qanoon.om was registered as non-official by another agent, so those facts are status lead (B0216-B0228), though the text is the consolidated official law.
- Labour Law English text (decree.om) registered non-official by another agent: B0212-B0215 are lead. Arabic qanoon text exists (qanoon-om-labour-law-rd53-2023-ar) if the lead wants to re-quote.

### What happens in practice

- The 2025 Ministry of Labour grace period (1 Feb-31 Jul 2025, extended to 31 Dec 2025 as "final") was worth over RO 60m in waivers; it was mainly an employer-side clean-up of labour-card fines, absconding reports and repatriation tickets. No official evidence of any window open in November 2026. BSS (Jan 2026) quotes Oman's labour minister that the 2023 visa suspension was to prioritise regularising irregular expatriates.
- A Jago Bangla story (16 Sep 2026) headlined as an Oman amnesty (deadline 1 Oct) is a copy of a Jordan/ASEZA (Aqaba) notice; this kind of misattributed "amnesty" news circulates on Bangla Facebook pages. Logged B0194-B0195 and used in the draft as a warning.
- Undocumented Bangladeshis get help mainly through the Embassy's WhatsApp service cell (since Dec 2025); no published evidence on how fast outpasses are issued.
- Death costs in Muscat (Indian Embassy list): embalming RO 100-123, cargo handling ~RO 77, casket RO 180-200; airfreight not given.
- Oman sent 1,893 of 17,871 bodies returned July 2016-June 2022 (third after Saudi and UAE).
- Remittances from Oman: USD 1,634.7m (FY25) -> 2,048.1m (FY26), +25.3%; Jul-Sep 2026 -5.1% y/y. Cost of small transfers from Oman is the highest of BB's ten corridors (6.77% Apr-Jun 2026).

### Logged but not cited (and why)

- B0034 (e-passport USD 30/45 at missions): replaced by the Muscat fee in RO (B0167).
- B0073 (4,745 bodies FY2023-24): superseded by 2024 and 2026 figures.
- B0130, B0131, B0134, B0136, B0139, B0161: duplicates of fee/contact facts cited elsewhere.
- B0153 (passport NOC RO 3.900 via Oman Post): not on my topic; useful to the passport/NOC writer.
- B0176 (MD 602 fee refund if worker dies within 90 days): employer-side detail.
- B0185 (10-year inactive cards cancelled), B0188 (2020 window dates), B0226 (sponsor fine RO 500 for not producing worker): kept for the absconding section if the lead wants them.

### Gaps (Need to know in the draft)

Travel Permit fee/documents/time; any 2026 grace period; deportation centres and Embassy access; ban after paying fine and leaving voluntarily; overstay fine cap; ticket for undocumented with no employer; Embassy death-NOC documents and time; air freight cost of a body to Dhaka/Sylhet; empanelled lawyers; whether SPF work-injury cover for expats started July 2026; Oman bank accounts for low-wage workers; Nagad partners in Oman; WEDB sellers in Oman; hundi rate and "apps"; ROP non-emergency number; Oman visa centre in Dhaka and embassy hours; deaths of Bangladeshis in Oman by year 2023-26.

### Pages we could not download

- https://sanadservice.com/en/guides/overstay-oman/ (403 for curl; read via Firecrawl only, not saved; used as a pointer to official sources).
- https://www.muscatdaily.com/2025/07/28/mol-pushes-labour-amnesty-deadline-to-dec-31/ (403).
- Muscat Embassy "Repatriation of Dead Body" and "NVR" menu links point back to the same page (no content on the site).
- decree.om CBO Money Services Regulation (CB-58/4/2024) and Banking Law English text: paywalled; used qanoon.om Arabic instead.
- Nagad partner table: paginated, Oman rows not rendered.
- WEWB annual report 2023-24: Muscat labour-wing allocations for body repatriation are in the garbled Bangla text layer; not extracted (Singapore's equivalent fact was B0285). Worth reading p. by p. for Oman figures.

## Fact-check and audit (10 November 2026)

- Six independent verifiers (prefixes KA to KF) checked every sentence and number in `doc.md` against its cited source; change lists are in `verify/part1-report.md` to `verify/part6-report.md`. Main errors fixed: the work-injury insurance start for expats (postponed to about July 2028, not July 2026), the start of Decision 602/2025 fees (15 February 2026), the free-visa penalty (the doubling falls on the employer), out-of-date body counts, wrong citations, dropped conditions, and allegations about the suspension without attribution.
- A final auditor (KG) ran the three CLAUDE.md audits and filled gaps (SIM card, visa refusal, comparison with India, Pakistan and Nepal); checklist in `verify/audit-report.md`.
- Facts: 1667 logged, 958 from official sources.
- Unsettled conflicts kept as Need to know: the family-visa salary threshold (ROP's English page RO 600, Arabic page and gov.om none, 2023 press RO 150); the resident-card fee (ROP page RO 6 and RO 11 against Decision 157/2025's RO 5 a year); overstay fees (gov.om RO 20 a day, ROP RO 50 a month); the number of exempt categories (8, 10 or 13 in different reports).
