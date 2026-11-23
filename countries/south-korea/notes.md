# South Korea: research notes

Research notes behind `doc.md`: what was searched, conflicts between sources, what happens in practice, facts logged but not used, and pages we could not download. One section per research topic (fact prefix in brackets); KA to KF are the fact-check pass and KG the final audit.

## How the doc was put together

- Six topics researched in parallel (C, R, E, V, P, B), merged on the Singapore model, split into six parts and checked sentence by sentence by independent verifiers (about 150 fixes in all: off-by-one citations, dropped insurance conditions, broker cases attributed to the right unit, a confused shipbuilding visa name, wrong EPS Center phone numbers), then audited.
- Exchange rate: the Bank of Korea publishes a won-per-taka rate directly: Tk 1 = KRW 10.86 on 19 October 2026 (KA facts).
- Concurrent writes to facts.csv split two rows; the fragments were removed and every cited id re-checked.
- Firecrawl's credits ran out during the fact-check; pages that needed it are listed under each topic's "Pages we could not download".
- Personal data: three BOESL PDFs that named private people were deleted; one is kept as a redacted transcript.

## Background and corridor (insider pass) (prefix C)

### What was searched

- **Korean official:** MOEL press releases on the 2025 (130,000) and 2026 (80,000) E-9 quotas and the 191,000 non-professional total; MOEL 2025 fatal-accident release (77 foreign deaths); Korea Immigration Service monthly statistics, September 2026 (hwpx and the raw xlsx by nationality and status, converted to text in `sources/`); the 2025 Statistical Yearbook (full PDF, whose Korean text layer is lost, and the statistics-table zip, from which the EPS visa-certificate table by nationality was saved); Work24 pages on workplace change and the foreign-worker insurances; Easy Law "Employment of Foreign Workers"; HRD Korea housing-deduction guide; MOJ E-7-4 releases; Korea.net minimum wage 2026 and 2027.
- **Bangladesh official:** BOESL's 1 July 2026 roster notice (Bangla PDF; text layer garbled, so I rendered the pages to images and read them, and logged quotes with --no-quote-check and page notes); BOESL service-charge table (scanned, no text layer; South Korea row transcribed by hand into `boesl-service-charge-pdf.md`); BMET's annual table image to May 2025 (copied from Singapore; S. Korea column transcribed by hand into this folder's .md); OEP country-clearance reports 2022-2025 (copied from Qatar) and a new pull for 1 Jan to 18 Nov 2026; Bangladesh Bank country-wise remittance (copied from Kuwait and Cambodia).
- **News and NGO:** Bonik Barta (English and Bangla, Sept 2025), Financial Express (2024 quota; E-7 welders 2024), BSS (2022 record; Aug 2026 training and returnee aid), Prothom Alo (2022 cost and salary; 2025 BMET Korean course; Oct 2026 SRB-4 arrests), Dhaka Post and Amar Desh (14 May 2026 roster protest), Dhaka Stream (April 2026, BOESL year-by-year numbers), Asia Post (E-8 Dangjin, July 2026), Chosun Biz (proxy exams), Chosun (greenhouse death ruling), Korea Herald and KBS (E-9 pay surveys), Korea JoongAng Daily (HD HHI), OHCHR CERD summary (April 2025), Business and Human Rights Centre, East Asia Forum, Amnesty "Bitter Harvest" (2014, read in part: summary, accommodation, hours).
- Bangla searches: কোরিয়া ইপিএস বোয়েসেল ২০২৬; কোরিয়া যেতে খরচ; কোরিয়ান ভাষা কোচিং প্রতারণা; দক্ষিণ কোরিয়ায় অবৈধ বাংলাদেশি; মৌসুমি কর্মী E-8; ২০২৬ কোটা.

### Conflicts between sources

- **Departures by year.** BMET table (2023 4,996; 2024 3,038) vs OEP (4,991; 3,022) vs BOESL via Bonik Barta (2023 4,804; 2024 2,779) vs BOESL via Dhaka Stream (2024 2,778; 2025 1,772). 2025: OEP 1,901 vs BOESL 1,772. 2022: BMET 5,910 vs BOESL 5,891. BMET/OEP count every clearance to Korea (EPS plus E-7, E-8 and others); BOESL counts EPS only. The doc uses BMET/OEP for the year list and BOESL for quota-fill figures, and says so implicitly by source. Not a Need to know because it does not change what anyone does.
- **2024 quota.** Financial Express (March 2024) says 11,500; Bonik Barta (BOESL data, 2025) says 11,700; Dhaka Stream says 11,500. The doc quotes Bonik Barta's 11,700 alongside its sent figure (2,779 of 11,700) because both numbers come from the same BOESL table.
- **2023 quota.** FE "a record 10,000"; Bonik Barta 10,200. Used 10,200 (same table as sent figure).
- **Cumulative EPS departures.** BSS 15 Aug 2026: 38,018; BSS 23 Aug 2026: 38,059; Dhaka Stream April 2026: 37,689; FE Jan 2024: 32,000. Used 38,059 (latest).
- **BOESL cost.** Service-charge table says US$240 (and is marked "Need approval by Board", first remark dated 28.10.22), but its Taka items add to Tk 38,584; Prothom Alo 2022 quotes BOESL's deputy GM at Tk 33,524 with a slightly different breakdown (visa Tk 5,100, service charge with VAT Tk 23,184). Welfare fee rose to Tk 5,500 from 1 Oct 2026 (R0038). R's draft carries the same Need to know.
- **E-7 numbers.** FE (Jan 2024): 76 Bangladeshis had gone on E-7 through agencies. KIS (Sept 2026): 6,164 Bangladeshis hold E-7 in Korea. The KIS figure includes E-7-1 professionals (many likely former students who changed status) and E-7-4 conversions; the KIS raw table does not split E-7 sub-types by nationality. Worth a Need to know for the lead if E-7 gets its own section.
- **Korea.net departure-insurance article (2014)** says the insurance is "deducted from their monthly wage"; Work24 (2026) says the employer pays 8.3%. Used Work24; did not use the 2014 article.
- **Korea.net KBiz wage survey** (KRW 3.02 million): page shows no year; article ID suggests late 2024. Logged as undated official.

### What happens in practice

- The bottleneck is employer selection, not the test: about 12,000 from the 2022-23 batches were deleted unused (protest claims, May 2026); BOESL's executive director says Korea controls selection; Korean employers rank Bangladeshis low (World Bank 2011-15; job-hopping reputation). BOESL's responses: deposit (Tk 1 lakh), counselling against job changes, six representatives in Korea, a US$1,200-per-company payment to Korean firms for seasonal workers (MD, April 2026), and the 2026 round giving deleted candidates first registration.
- 2026 round: 10 test seats per rostered place (20,000 for 2,000).
- Brokers operate at the BKTTC exam venue (Technical Mor, Mirpur); SRB-4 arrests 9 Oct 2026 on BOESL's and BKTTC's complaint. A Facebook post by the Ministry/BOESL (not saved: Facebook) reports a joint BOESL-district administration operation against a man in Paba, Rajshahi, who tried to take Tk 16 lakh from a Korea-bound worker.
- Remittances recorded from Korea are tiny (US$16.76 million in Jul-Sep 2026) relative to ~19,000 Bangladeshi workers; hundi is the likely explanation but no source says so. Left as Need to know.

### Facts logged but not used, and why

- C0011 (test result valid 2 years): covered by C0018 and R's steps.
- C0029 (2018 record of 2,355): superseded by the year list.
- C0038 (191,000 non-professional total): E-9 and E-8 figures used instead.
- C0053 (349,660 E-9, 82,845 E-8 holders in Korea): context only.
- C0062 (H-2 free to move): H-2 is for ethnic Koreans; not relevant to Bangladeshis.
- C0085 (2022 worker: min Tk 1.8 lakh): replaced by the 2026 version (C0143).
- C0091 (over one million EPS entrants since 2004): trivia.
- C0096 (E-7-4 quota 5,000 to 35,000, East Asia Forum): replaced by MOJ's official 2026 figure (C0121).
- C0129 (28% of E-9 above KRW 3 million in 2024): replaced by the 2025 figure (C0128).
- C0131 (OEP 2022: 459): OEP covers only part of 2022; BMET figure used.
- C0139 (2008 first round: 20,450 registered, 8,278 passed, 1,595 went): history; available if the lead wants it.

### Cross-references used (check against final headings)

- Work visa: EPS (E-9 non-professional employment); Who pays what; E-8 seasonal agricultural work; Coming back: the sincere worker re-entry and the Special EPS-TOPIK; Done to workers (R draft).
- Housing, and deductions for accommodation and food; How many changes, and for what reasons; Overstaying and losing status; If you aren't paid (E draft).
- Student visas (D-2 degree, D-4 language) (V draft).
- Asylum and Sending money home: no draft heading yet; the lead should make these match.
- R0038 (welfare fee Tk 5,500) is cited from R's facts.

### Pages we could not download

- https://www.jagonews24.com/national/news/1119077 (403; Dhaka Post covered the same protest).
- https://www.daily-sun.com/bangladesh/850246 (403; "Why Bangladesh is losing out in Korea, Japan", Jan 2026).
- https://www.facebook.com/probashi.gov.bd/posts/... (BOESL/district administration operation against Tk 16 lakh fraud on a Korea-bound worker, Paba, Rajshahi) and BOESL Facebook flight notices: Facebook, not fetched.
- KOSIS table "국가별 불법체류 외국인 현황 (2018~2025)" (kosis.kr, orgId 111): needs a browser; it would give undocumented Bangladeshis by year.
- The 2025 Statistical Yearbook PDF (saved as kis-yearbook-2025) has no usable Korean text layer, so country names are missing from its tables; table 6-4 (undocumented by nationality, top 10) needs reading as images.
- https://www.moel.go.kr/common/downloadFile.do?file_seq=20260302753... (2025 fatal accidents investigated; foreign 71 of 605): text layer garbled, deleted; search snippet only.

### Personal data

- No private migrant's document was saved. News articles naming workers (protesters, an injured returnee, an engineer) are public reports; the draft does not name them.

### Gaps (Need to know in the draft)

- Bangladesh's 2026 EPS quota and 2026 job orders and departures (BOESL).
- Registrations, sitters and passers in the September 2026 EPS-TOPIK round.
- Number of undocumented Bangladeshis in Korea.
- Private Korean-language centre fees and promises in 2026; street price of a fake Korea work visa.
- BOESL's 2026 security deposit and refund process.
- Typical all-in spend for an EPS worker in 2026.
- Why recorded remittances from Korea are so low (hundi?).

## Work visa: EPS route, E-8 and E-10 (prefix R)

### Bangladesh-side facts re-quoted from Singapore (Singapore id -> R id)
KB0001 R0001; KB0002 R0002; B0003 R0003; B0005 R0004; B0007 R0005; B0008 R0006; B0009 R0007; B0010 R0008; B0011 R0009; B0012 R0010; KB0004 R0011; B0039 R0012; B0106 R0013; B0050 R0014; B0052 R0015; B0057 R0016; B0058 R0017; B0063 R0018; L0009 R0019; KG0056 R0020; KG0052 R0021; KG0055 R0022; L0010 R0023; KG0054 R0024; KG0053 R0025; L0002 R0026; L0003 R0027; L0006 R0028; L0007 R0029; B0038 R0030; B0001 R0031; B0002 R0032; B0029 R0033; B0030 R0034; B0031 R0035; B0032 R0036; B0033 R0037; B0034 R0038; B0035 R0039; B0036 R0040; B0037 R0041; B0041 R0042; B0042 R0043; B0044 R0044; B0051 R0045; B0053 R0046; B0054 R0047; B0056 R0048; B0059 R0049; B0060 R0050; B0061 R0051; B0062 R0052; B0064 R0053; B0065 R0054; B0066 R0055; B0067 R0056; B0068 R0057; B0069 R0058; B0048 R0059; B0169 R0060; B0043 R0061.
(Bangla PDF quotes re-logged with --no-quote-check carrying the original transcription note.)

Later PCC re-quotes: B0014 R0247 (portal, Tk 1,500); B0015 R0244; B0016 R0245; B0017 R0246; B0018 R0248 (Tk 500 guidance).

### What I searched
- BOESL site (boesl.gov.bd notice board, brms.boesl.gov.bd, eps.boesl.gov.bd), every Korea notice on the board in Nov 2026, and their PDFs (Bangla PDFs have a garbled text layer; read page by page from images rendered with PyMuPDF; quotes logged with --no-quote-check and page notes).
- HRD Korea EPS-TOPIK site (what is, special, punishment, application form, test dates).
- eps.go.kr (EPS history, quotas, permitted industries, insurances, employer and worker procedures), Work24 (re-entry special case, EPS overview with 17 countries, counselling centre 1577-0071).
- Korean Embassy Dhaka / KVAC (VIC checklist, TB centre), Easy Law English PDF, HRD Korea Jeonbuk housing-deduction guide, MOEL 2026 quota, MOJ Seasonal Worker Program, Jung-gu alien registration, Suhyup 2023 report on foreign fishers, Newstapa E-10 series.
- Bangla/English news: Prothom Alo (2022 cost breakdown; Oct 2026 SRB-4 arrests), BSS (Aug 2026 13-day training; Apr 2025 first E-8 group), Bonik Barta (quota fill 37%), Amar Desh (May 2026 ministry siege), Chosun Biz (2025 proxy-exam firms).
- Several sources were saved by other agents in the shared sources folder (boesl-service-charge-pdf, news-palo-korea-salary-cost, news-bss-bn-124-training-2026, news-chosun-proxy-exam-2025, easylaw-foreign-workers-pdf, hrdk-housing-food-deduction, moel-2026-e9-quota-80000, news-bonikbarta-en-quota-37pc-2025, news-amardesh-ministry-siege-2026, oep-country-clearance-2025, bdemb-seoul-*, work24-foreign-worker-counselling-centre, kvac-dhaka-home, vfs-korea-bd-launch-2026). I logged facts from them under R; I registered kvac-dhaka-checklist-vic-general, embassy-bd-tb-test-centre, kvac-dhaka-home and vfs-korea-bd-launch-2026 myself because they were not yet in sources.csv.

### Conflicts between sources
- **Pass mark.** BOESL July 2026 notice: merit list from those scoring more than 120/200 (R0080). eps.go.kr worker-procedure page: 80+ (R0151, older, generic). Prothom Alo 2022: more than 110. Used BOESL's.
- **Cheating ban.** HRD Korea punishment page and Special-UBT oath: 4 years (R0139, R0148). BOESL July 2026 notice: 3 years from UBT (R0090). BOESL Special-UBT schedule and HRDK application-form page: 2 years (R0118). Kept as Need to know.
- **Wage guarantee premium.** eps.go.kr table says KRW 15,000; detail says KRW 16,000 a year (R0187, R0226). Used 16,000 with the table noted in the fact.
- **Return cost insurance group.** Bangladesh not named; "Mongolia and other countries" KRW 500,000 (R0174). Need to know.
- **Qualifier quota.** HRD Korea letter (Apr 2026) raised Bangladesh's annual qualifiers quota from 500 to 2,000 (R0116); BOESL July 2026 notice aims at 2,000 rostered from 20,000 test-takers (R0065). Consistent.
- **Bangladesh quota.** BOESL leaflet (Apr 2026): avg 4,000+, 8,000 in 2026 (R0105). Bonik Barta (Sep 2025, BOESL data): 10,300 in 2025, 11,700 in 2024 (R0228). Different years; not a direct conflict, but the "average 4,000" looks low against the 2023-2025 figures.
- **Total sent.** BOESL leaflet: about 37,800 in 16 years (R0103); BSS Aug 2026: 38,018 (R0194). Used BSS.
- **Labour Wing e-mail.** laborwingseoul@gmail.com (counselling page, 2023) vs labourwingseoul@gmail.com (wing contacts, 2025). Need to know.
- **E-10 and Bangladesh.** Suhyup 2023: E-9 fishing from Indonesia, Timor-Leste, Sri Lanka, Vietnam; E-10 from Indonesia, Vietnam, China, Myanmar (R0209). Work24 (Jan 2026) lists Bangladesh as a specialised E-9 fishing country (R0206), and BOESL's 2026 notice mentions roster deletions in fishing (R0066). So Bangladesh has been added for E-9 fishing since 2023; no evidence for E-10.
- **Police clearance fee.** Tk 1,500 (portal) vs Tk 500 (police guidance), carried from Singapore.
- **VFS as "official".** vfs-korea-bd-launch-2026 is registered as official (VFS is the Embassy's appointed partner); a reviewer may prefer it as non-official.

### What happens in practice
- Roster waits and deletions are the big story: 1,700 rostered 2022 passers expired; protests at the Ministry (May 2026); BOESL warned protests could make HRD Korea reconsider Bangladesh (R0114); HRD Korea refused reinstatement but waived the lottery and raised the qualifier quota (R0115, R0116).
- Bangladesh fills a small share of its quota (37% over five years; 24% in 2024) because few employers send job orders for Bangladeshis (R0227, R0228); a World Bank study ranked Bangladesh seventh in employer preference (R0231).
- Fraud: SRB-4 raid at Technical Mor (near BKTTC/BOESL) in Oct 2026; rings charge Tk 40,000 to Tk 10 lakh for "guaranteed" passes and visas (R0222, R0223). Proxy-test firms advertise on Telegram for KRW 2-2.2 million and claim to bribe local supervisors (R0195-R0197).
- E-8 from Bangladesh is new and small (25 to fisheries in Apr 2025; 20 to Hampyeong farms in 2026) and carries Tk 5 lakh guarantor cheques per guarantor.

### Facts logged but not used (and why)
- R0017 (women's PKB loan), R0020, R0025-R0029 (Act details and OEP agency list: private agencies have no role in EPS), R0030, R0036/R0037/R0039-R0041 (agency/self clearance routes: BOESL does clearance), R0043/R0044/R0061 (BMET grievance: covered via Ministry), R0045/R0047 (insurance claim detail: belongs to the cross-country section), R0050/R0051/R0055 (PKB detail), R0056 (checklist), R0059 (pay agency through bank: BOESL pay order covered).
- R0064 (deletion, duplicated by R0099/R0106), R0069 (US$8 per candidate to BOESL: background), R0102 (consent form), R0103 (37,800 total: superseded), R0108 (leaflet warning, duplicated), R0135, R0142, R0143, R0149, R0150, R0151 (conflicting old pass mark), R0156/R0157 (workplace change: belongs to the "changing employer" section), R0169 (renewal), R0179/R0180/R0181 (history and quotas: Background), R0207, R0229 (roster expiries: Background), R0234 (siege: Background), R0238 (no change to E-9 in Korea: visa-change section).

### Pages we could not download
- https://www.workinkorea.org/ko/34 (re-entry special case, HTTP 400; covered by Work24 instead).
- https://mihu.re.kr/activities/fisherman-story-2/ (E-10 sending-cost caps by country; page rendered empty; deleted and removed from the fetch log).

### Personal data
- Deleted boesl-seasonal-agri-pdf1 (a sample experience certificate naming a private farmer, his parents and village) and removed its fetch-log row.
- Deleted boesl-special-ubt-30-pass-pdf and boesl-special-ubt-30-schedule-pdf2 (lists of named applicants). Saved a redacted transcription of the pass notice's page 1 as sources/boesl-special-ubt-30-pass-notice.md (logged as manual), with the name table omitted.
- The Prothom Alo Oct 2026 article names the convicted ring members; they are not named in the draft.

### Open gaps (also in the draft as Need to know)
- Current BOESL EPS service charge (table row awaiting Board approval); Civil Surgeon medical cost; who books and pays flights; whether BOESL submits visas in bulk; E-9 visa processing time; skills-test tasks and venue; 2026 cut-off score and pass count; typical roster wait; whether EPS workers also do BMET's 3-day PDO; who files alien registration for E-9 workers; return-cost insurance group for Bangladesh; E-8 MoU partners and outcomes; whether any Bangladeshis have gone on E-9 fishing contracts.

## Rights and life on E-9 (prefix E)

Facts logged: E0001-E0206 (206; 194 official, 12 news/NGO). Draft: drafts/E-life-rights.md (194 ids cited, all present in facts.csv at hand-back).

### What was searched

- Official Korean law texts on law.go.kr (Firecrawl scrape; saved as markdown): Labor Standards Act (in force 8 Oct 2026), Immigration Act (2 Oct 2026) and its Enforcement Rule (23 Oct 2026), Act on the Employment of Foreign Workers (with the 9 Jun 2026 amendments) and its Enforcement Rule, Enforcement Decree of that Act (version in force 3 Feb 2023), Serious Accidents Punishment Act, Electronic Financial Transactions Act (2 Oct 2026). Full scrapes saved for LSA, Immigration Act, Immigration Rule and EFT Act; for the EPS Act, its Rule, the Decree and SAPA, the scrape came back inline, so a verbatim excerpt of the articles used was saved (each file says so).
- Ministry of Government Legislation "Easy Law" English PDFs (all drafted 15 Jul 2026): Employment of Foreign Workers, Wage Arrears, Industrial Accident Compensation, Four Major Social Insurances, National Health Insurance, Financial Transactions, Extension of Stay. The HTML pages render empty with curl; the PDF download link (CSP/FileDownload.laf?flType=pdf&csmSeq=...) works with fetch.py. The Korean Easy Law PDF (csmSeq=2042) has a garbled text layer and was deleted.
- MOEL Work24 pages (workplace change, foreign-worker insurance, Foreign Workforce Counselling Centre), the EPS FAQ, HRD Korea Jeonbuk branch page on housing/food deductions, the 2015 EPS mobile app manual, MOEL policy list.
- Reused sources fetched and registered by other agents in this folder: Bangladesh Embassy Seoul wing contacts and labour counselling page, MOJ special voluntary departure release, HiKorea voluntary departure page, Korea Customs hwanchigi notice, Easy Law note on account-lending penalties, East Asia Forum, BHRRC, OHCHR CERD summary.
- News: Hankyoreh (Sep 2023) on the support-centre budget cut; Danbi News (Jul 2024) on the half-revived centres. Bangla news search (Prothom Alo, BSS, Daily Star Bangla) gave nothing on rights in Korea beyond what others already saved.

### Conflicts and points to check

- **Labour counsellor's name.** The embassy wing list (2025-01-13) and counselling page (2023-07-14) give Mr. Mikon Tangchanggya (one says Counsellor, the other First Secretary). A Korea Herald search result names "labor counselor Mokima Begum" (date not checked). The counselling page also gives laborwingseoul@gmail.com (no "u") and mission.seoul@mofa.gov.bd; the newer wing list gives labourwingseoul@gmail.com. Draft uses the newer list; flagged as Need to know.
- **EPS Act dormitory article.** Article 22-2 is being replaced from 10 Jun 2027 ("주거시설", with a building-register requirement); Article 22-3 (support to local governments) takes effect 10 Dec 2026. The draft states the current rule and the 2027 change.
- **Workplace change "employer consent".** The law lists reasons only; NGO reporting (BHRRC 2025) says transfers in practice need employer consent and bring retaliation. Draft gives the law and the practice evidence, plus a Need to know.
- **Substitute payment caps.** Easy Law (Jul 2026) gives KRW 7,000,000 for currently employed workers; Work24 insurance page (Jan 2026) gives up to KRW 10,000,000 for the "simplified substitute payment" (for workers who have left). Not a conflict: two schemes. Draft keeps both.
- **Minimum wage source date.** Korea.net article is dated 11 Jul 2025 (possibly outdated) but Easy Law (Jul 2026) confirms KRW 10,320 for 2026. A search result says the 2027 rate is KRW 10,700 (Acclime, Arirang); not logged (no official source fetched). The lead should add it if the doc will be read after 1 Jan 2027.
- **Decree version.** The Enforcement Decree on law.go.kr shows the 3 Feb 2023 version as current; logged as possibly-outdated by date rule though it is the law in force.
- **SAPA date for small workplaces.** The law says 3 years after promulgation (26 Jan 2021) for workplaces under 50; the draft says "since January 2024" (27 Jan 2024 by computation).

### What happens in practice

- Workplace changes: workers are often refused, retaliated against, or made to prove abuse first (BHRRC 2025). A Bangladeshi worker injured in Pocheon (2024) was told not to report the accident.
- Support centres: the 2024 budget cut closed the MOEL-funded network; 6 of 9 hub centres reopened via local-government funding with half the staff; interpreters for a given language may not be there on a given day (Danbi 2024). Current Bengali-language availability unknown.
- Deaths and injuries: migrant fatality rate 1.7x Koreans (NHRCK 2024 via CERD); 13% of workplace deaths (EAF citing Korea Times); Aricell fire, 18 migrant workers dead (Jun 2024).

### Facts logged but not used, and why

- E0015 (departure insurance claim after 1 year) and E0056, E0097, E0098, E0099, E0105: duplicates of facts cited in another form.
- E0128 (Immigration Act re-entry permit article): superseded by the rule exemption E0172.
- E0171 (MOEL annual inspections): no evidence of what inspections achieve; left out.
- E0175 (embassy says file at Korea Legal Aid Corporation): kept the KLAC line from Easy Law instead; could be added to the embassy contact line.
- E0188, E0192: background on centres and MOEL programmes, covered by other facts.

### Gaps (Need to know questions in the draft)

Real take-home pay; which LSA protections are lost below 5 workers in practice; farm/fishing hours and premiums; actual housing deductions; passport-holding practice; leave for trips home; voluntary departure scheme for 2026-27 and entry-ban length; drug and assault outcomes; hundi prosecutions of customers; SIM (대포폰) penalty; current support centres with Bengali staff; whether the labour counsellor and hotline are current; petition processing time; injury reporting when the employer refuses; sexual-harassment route (Equal Employment Act, NHRCK 1331) not sourced; whether any employer signature is needed for a change filing; broker fees for referrals and for buying bank accounts; "voluntary resignation" pressure.

### Pages we could not download / did not use

- easylaw.go.kr English HTML pages (render empty with curl; used the PDF versions instead).
- Korean Easy Law PDF csmSeq=2042 (text layer garbled; deleted).
- MOEL Bucheon branch housing/food guideline PDF (https://www.moel.go.kr/local/bucheon/common/downloadFile.do?file_seq=20231102496&bbs_seq=20231101681&bbs_id=LOCAL1): text layer garbled; deleted. Would give KRW amounts for the 15%/8% caps at the 2023 minimum wage.
- MOEL housing/food deduction guideline (moel.go.kr dataroom bbs_seq=20200200797) is an .hwp attachment; not fetched. HRD Korea's page summarising it was used.
- ILO-hosted "Introduction to EPS" (HRD Korea, 2012): fetched, too old, deleted.
- Firecrawl credits ran low during this session (Firecrawl reported the daily credit refresh about 11 hours away).

## Visit, business, student, transit and medical visas (prefix V)

Researcher prefix V. Facts V0001 to V0187. Draft: drafts/V-visits-students.md.

### What was searched

- Korean Embassy Dhaka (mofa.go.kr/bd-en): consular notice board m_23305 (seq 1 to 37 probed) and visa issuance board m_23302 (seq 1 to 25 probed); all visa-relevant notices saved.
- KVAC Dhaka (visaforkorea-bd.com, VFS Global): every page and all checklist PDFs linked from visa-type.html.
- Korea Immigration Service: Visa Navigator PDF (Ver 2023.05), E-Visa Center page, K-ETA eligibility page.
- Study in Korea (NIIED): visa and stay, residence/part-time/D-10, expenses, IEQAS-certified universities.
- Other Korean missions: Canada (B-2 transit, Dec 2025), LA (B-2, 2023), Israel (K-ETA).
- Working Holiday Info Center 2026 guide; Medical Korea (KHIDI) medical visa page; Korea.net (voluntary departure).
- Immigration Act (law-immigration-act-ko, saved and registered by another agent) for Art. 94 penalties.
- News: Korea Herald (Oct 2026 student overstay data; Feb 2026 immigration raids), Korea Times (2024 forged invitations), Bonik Barta and Daily Observer (SinGyeongju University, July 2026), Channel 24 (Nov 2026 proposed student-visa reforms). Bangla searches on Korea visit-visa and student-visa scams found mostly agency ads and EPS (work) scams, nothing Korea-visit-specific.

### Conflicts and points to watch

- **KVAC hours:** the Embassy announcement and KVAC site say 09:00-16:00 Sunday to Thursday (V0004, V0047); the VFS press release says 9am to 2pm business hours. Used the Embassy/KVAC figure.
- **Old embassy document pages:** the Embassy's C-3-9, C-3-1, C-3-4 and D-2/D-4 document pages are dated 2021-2024 (possibly-outdated), but the KVAC checklists of Sept 2026 repeat the same lists; facts from both are logged, and the doc cites the KVAC checklist where its text layer was readable. KVAC PDFs lost the "ti" ligature in the text layer ("Applica on"), so quotes avoid those words.
- **D-2/D-4 duration:** Visa Navigator gives "2 years (Extendable)" for D-2 and D-4 at issue; Study in Korea says "up to 2 years per issuance". Consistent.
- **Part-time hours:** the Study in Korea table (undated) shows 2025-style hours (TOPIK 3 for 25 hours, unlimited weekends). Some university pages still show the older 20-hour cap; used the official table. Channel 24 (Nov 2026) reports proposed changes (TOPIK 3 for part-time work, TOPIK 4 to waive proof of funds, 1-3 years' post-study stay) that are not yet in force.
- **Jeju:** no official page found that lists Bangladesh by name for Jeju; the Canada mission says the Incheon transit-tour exclusion covers "23 countries that are not granted visa free entry to Jeju", and the same page lists Bangladesh among 23 excluded transit nationalities. The doc combines V0107 and V0109.

### What happens in practice

- The SinGyeongju case (2026) shows the real sequence: offer letter, fees due within about a week, bank transfer to the university, then the university files with immigration (VIC). If the university fails, the student has paid without any visa application existing. The Embassy (V0095) will not intervene.
- D-4 language visas are the main route into illegal stay (29.2% illegal in Aug 2026, mostly Vietnamese, then Uzbek, Mongolian, Chinese, Nepali); no Bangladesh-specific overstay figure found.
- Raids: frequent (every 1-2 months in Hwaseong per one Bangladeshi), ~140,000 enforcement actions in 2024.
- Forged-invitation rings for C-3-4 visas exist (Pakistani ring, 2024, USD 10,000-13,000 per head); no Bangladesh-specific case found.

### Facts logged but not used, and why

13 of 187 logged facts are not cited in the draft:
- V0004 and V0042: duplicates of V0047 (hours) and V0045 (courier).
- V0013: notarization and police clearance stay with the Embassy; useful for the lead's contacts section.
- V0022: applies to foreign nationals applying from Bangladesh, not Bangladeshis.
- V0029, V0117, V0128: covered by more specific facts (V0154, V0157, V0127).
- V0048: VFS role; V0011 says the same from the Embassy.
- V0104: fake K-ETA websites; K-ETA is not open to Bangladeshis, so the scam is marginal.
- V0111: older (2023) version of the transit rule; V0106-V0108 (Dec 2025) used.
- V0168: an agency's claim of a 90-day refund rule; not an official rule.
- V0172: total student overstay count; V0173 (rates) used instead.
- V0186: proposed study-expense deposit, only a proposal.

### Pages we could not download

- https://www.asiae.co.kr/en/article/2020060914560042180 (Bangladeshi student who used fake China language-trainee papers to bring 12 Bangladeshis into Korea, 2020): curl failed (status 000); Firecrawl credits low, not retried.
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?menuSn=923&dataSetId=107&vcontsId=218324 (KTO medical tourism visa): 503.
- https://elaw.klri.re.kr/eng_service/lawView.do?hseq=33079&lang=ENG (English Immigration Act): frame page with no text; used the Korean act instead.
- https://easylaw.go.kr/CSM/SubCnpclsCmd.laf?csmSeq=2492 (extension and overstay penalties, English): JavaScript-loaded, empty.
- https://www.studyinkorea.go.kr/public/new/file/guideBook_en.pdf (Study in Korea guidebook): 43 MB image PDF with no text layer; deleted.

### Open gaps (also in the draft as Need to know)

- Bank balance the Embassy expects for C-3 tourists and for D-2/D-4 students from Bangladesh; whether Bangladesh is on the MoJ "high-overstay" list for students (Visa Navigator mentions such a list).
- Refusal rates, written reasons and any appeal route.
- Street prices: "visit visa with job", fake Korean company invitations, D-4 "language course plus job" packages.
- Airside transit at Incheon without a visa for Bangladeshis.
- Whether SinGyeongju students were refunded.

## Skilled visas, family, PR, changing visa type, asylum, children (prefix P)

Researcher prefix P. Facts P0001-P0265 (265 logged: 234 from official sources, 31 news/NGO/UNHCR). Draft: `drafts/P-skilled-family.md`.

### What was searched

- MOJ / Korea Immigration Service press releases and notice boards (immigration.go.kr, moj.go.kr): E-7-4 quota (Feb 2026), E-7-4 farm cap and forced-job-change rule (Jun 2026, with full points table annex), E-7-4 reform plan (Oct 2026), 2026 E-7 wage notice (2025-406), F-2-R notice 2026-248, regional visa small-business rule (May 2026), regional visa TF (Mar 2026), refugee living-cost card (Jun 2026), fake refugee broker case (2023), children's education status scheme (2025-2028), parents' stay to age 24 (Mar 2026).
- MOJ statistics monthly, September 2026 (.hwpx, text extracted locally because the PDF text layer is garbled): refugee totals, recognition rates, applications by nationality incl. Bangladesh, G-1 definition, naturalisation numbers.
- MOEL Busan Bukbu branch: 2026 E-7-4 recommendation notice (documents, timeline, 2,000 manufacturing quota).
- law.go.kr: Immigration Act (Korean, saved by another agent; Art. 18, 23, 24, 26, 46, 95), Enforcement Rule (Art. 9: C-3 no change of status), Refugee Act and its Enforcement Decree (English, KLRI translation).
- Easy Law (easylaw.go.kr, Ministry of Government Legislation, dated 15 Oct 2026): marriage-migrant pages on F-6, income threshold, language rule, F-5, naturalisation, renunciation, marriage registration, child birth registration.
- MOJ Visa Navigator (English, May 2023; saved by another agent): F-3, E-9 family rule, D-10, ladder to F-5.
- Bangladesh Embassy Seoul: fee chart Oct-Dec 2026 (saved by another agent), birth registration correction page, e-passport documents page. e-Passport instructions (saved by another agent).
- News/NGO: Weekly Kyunghyang (Feb 2026) on E-7-3 brokers; Financial Express (Jan 2024) on Bangladeshi E-7 welders via RRC; Money Today (Apr 2025) on refugee brokers; Korea Times (Jul 2026) Vietnamese fake-asylum case; Law Times (Aug 2026) Constitutional Court ruling; Newsis (Jan 2025) undocumented children; Korea JoongAng Daily (2011) sham marriages; UNHCR fact sheet (Apr 2024).
- Searches that found nothing usable: Bangla news on Korea welding-visa fraud (Prothom Alo, Daily Star, Jugantor, bdnews24 hits were all Gulf-related); Bangladeshi refugee-broker cases in Korea; Bangladeshi sham marriages with Koreans; official per-nationality recognition figures for Bangladesh; Korean status granted to newborns of E-9 parents.

### Conflicts between sources

- E-9 years needed for E-7-4: MOJ Visa Navigator (May 2023) says 5 years on E-9/E-10 in the last 10 [P0170]; MOJ June 2026 annex and MOEL 2026 notice say 4 years on E-9/E-10/H-2 [P0034, ...]. Draft uses 4 years (newer, official).
- E-7-4 Korean minimum: points table gives 50 points for TOPIK 2/KIIP 2/pre-test 41-60 [P0042]; the overview says KIIP pre-test placement at level 3 [P0030]. Both used where they apply.
- E-7-4 income: KRW 26 million (overview and wage notice) vs income table starting at KRW 25 million and farm/fishing KRW 24 million (income) / 25 million (contract). Draft gives each as stated.
- E-7 stay per grant: MSS-hosted guideline says up to 3 years [P0205]; E-7-4 granted up to 2 years at a time [P0032]. Both stated.
- Refugee recognitions: index.go.kr says cumulative 1,679 at end-2025 [P0154]; monthly stats say 1,785 at end-Sep 2026 [P0110] (consistent: +106 in 2026).
- Two other agents also saved the same Sept 2026 monthly statistics (`kis-stats-monthly-2026-09`) and the same Financial Express article (`news-fe-e7-24-workers`); I logged my facts against my own copies (`moj-stat-monthly-2026-09`, `fe-e7-welders-2024-01`). The lead may want to merge.

### What happens in practice

- E-7-3 shipyard recruitment is private (KOSHIPA tests abroad), and broker fees of KRW 10-20 million are common; workers sign no-leave pledges backed by family guarantors; E-7-3 pay has fallen to minimum-wage level and below E-9 in a 2025 survey. Political pressure in 2026 to stop E-7-3 expansion; regional shipbuilding visa under review.
- E-7-4 uptake is driven by Korean-language difficulty; employers mostly convert their own E-9 workers (89.2%).
- Refugee route: average 4+ years with unlimited re-applications; brokers charge KRW 0.6-10 million; repeated MOJ crackdowns. Bangladeshi claims steady (394 in 2024, 468 in Jan-Sep 2026).
- Undocumented children scheme: only about 1,000 of an estimated 10,000-20,000 children got status in 4 years; parents' fines are the main barrier (up to KRW 30 million per parent reported in a search snippet; not saved, not used).

### Facts logged but not used, and why

- P0012 (same content as P0011), P0016 (duplicate of P0015), P0021 (survey detail, covered by P0004/P0020), P0024 (duplicate of P0023), P0028 (E-7-2 not in scope), P0048 (E-7-4R covered via P0188), P0061/P0064 (regional visa detail beyond need), P0079 (BOESL E-9 numbers belong to the E-9 section), P0099 (covered by P0209/P0082), P0107/P0108 (registration rules belong to the general stay section), P0115 (same as P0134), P0117/P0118 (definitions duplicated by Refugee Act facts), P0119 (Bangladeshi workforce number, for Background), P0150 (anecdote), P0153/P0154 (UNHCR fact used instead; P0154 useful for Background), P0182 (merged into P0181).
- P0170 used only for the F-2 step; its "5 years on E-9" statement is superseded (see Conflicts).

### Source quality notes

- `moj-e74-farm-50pct-2026-06-fc.md`: Firecrawl extraction of the June 2026 PDF; the points-table annex was garbled, so I re-laid it out from the extracted cells. The age-band boundaries (19-26 / 27-33 / 34-40 / 41+) and bonus-point labels are my reading of the garbled row; flagged in the draft as a Need to know and noted on P0043/P0044.
- `moj-stat-monthly-2026-09.md`: text extracted from the official .hwpx (paragraph text joined, table cells one per line). The by-nationality refugee table is interleaved row by row; P0121-P0123 notes explain the reading.
- Several MOJ PDFs have no usable text layer (fonts without Unicode maps); I used Firecrawl's PDF parser and saved trimmed but verbatim markdown (`*-fc.md`).
- `mss-e7-guideline-extract-fc.md`: pages 1-4 of a 73-page MSS-hosted copy of the MOJ E-7 guideline; undated, so possibly-outdated.
- Refugee Act English translation is the 2016 version (Act No. 14408); no later amendment found in the English database.

### Pages we could not download

- https://www.moj.go.kr/bbs/moj/182/495359/download.do and other moj.go.kr download links: HTTP 307 to curl; got the same files via immigration.go.kr or Firecrawl instead.
- https://www.visaforkorea-mn.com/upload/비자 내비게이터(Visa Navigator) 전자책(국문).pdf: downloaded but 2022 edition with garbled text; deleted.
- https://easylaw.go.kr/CSP/FileDownload.laf?flType=pdf&onhunqnaYn=N&csmSeq=47 (Easy Law marriage-migrant PDF, 75 pp.): text layer garbled; used the HTML section pages instead; PDF deleted.
- https://www.mss.go.kr/common/board/Download.do?bcIdx=1060330&cbIdx=256&streFileNm=5dd67758-8653-4dd3-882e-3ecd7d8d6693.pdf: garbled text; only pp. 1-4 taken via Firecrawl.
- https://futurechosun.com/archives/119778 (undocumented children myths, Korean NGO-media): curl failed (000); not retried.
- https://www.unhcr.org/sites/default/files/2024-04/UNHCR_Korea_Fact%20Sheet_ENG_202404.pdf: 403 to curl; saved via Firecrawl.

### Open questions (also in the draft as Need to know)

- E-7-3 from Bangladesh: which agencies hold BMET permission in 2025-2026, the BMET fee cap, where KOSHIPA tests are held, real taka cost, fake training centres.
- E-7-1 process from Bangladesh: who files the visa issuance confirmation, fee, time; apostille vs attestation; BMET clearance channel.
- E-7-4: HiKorea fee and time; whether the birth-year rotation still applies; whether recommendations are sold.
- F-6: Korean Embassy Dhaka/KVAC fee and time; nikahnama attestation chain; Bangladeshi marriage-visa broker activity.
- F-3: whether Bangladesh is on MOJ's high-overstay list; income needed for E-7-4 holders to invite family.
- Children: status granted to a newborn of two E-9 parents, documents and fee; Embassy Seoul new birth-registration document list and time; whether a foreign-child birth registration law has passed after the August 2026 ruling.
- Asylum: number of Bangladeshis recognised or given humanitarian stay; any broker cases targeting Bangladeshi E-9 workers.
- PR/citizenship: number of Bangladeshi F-5 holders and naturalisations; general F-5 income threshold.

## Money, going home, coming home, contacts (prefix B)

Agent B, 19 November 2026. Draft: `drafts/B-bangladesh-side.md`. Facts B0001-B0274 in `facts.csv` (247 cited in the draft).

### How the work was done

- **Bangladesh-side facts ported from Singapore.** B0001-B0124 were re-logged from `countries/singapore` facts (same quote, date and status, source files and log rows copied with a helper script). Mapping, Singapore id -> Korea id: SG B0003->B0001, B0005->B0002, B0013->B0003, B0039->B0004, B0040->B0005, B0041->B0006, B0042->B0007, B0044->B0008, B0050-B0055->B0009-B0014, B0064->B0015, B0065->B0016, B0070-B0073->B0017-B0020, B0075-B0100->B0021-B0046, B0102->B0047, B0101->B0124, B0103 onward->(SG id minus 55) up to B0171->B0114, B0174->B0115, B0284->B0116, B0286->B0117, B0314-B0318->B0118-B0122, C0200->B0123.
- **Concurrent writes dropped rows twice** (SG B0101 and one Korean Embassy fact). Both were re-logged (B0124, B0254). A final check found every B id cited in the draft present in `facts.csv`, with no duplicate ids.
- **Transcriptions made by reading images** (text layer empty or garbled): `bdemb-seoul-consular-fees.txt` (April-June 2025 chart), `bdemb-seoul-fees-2026-q4-img.txt` (October-December 2026 chart; the .jpg was saved by fetch.py as .html/.md/.txt and renamed), `kcs-hwanchigi-notice.txt` (Korea Customs notice), `boesl-eps-leaflet-2026-transcription.txt` (BOESL 12 April 2026 leaflet, contact block and agency roles only; logged with a `#transcription` URL fragment because R had already saved the PDF).
- **Sources shared with Agent R** (registered by R, quoted by me): `easylaw-foreign-workers-pdf`, `easylaw-four-insurance-pdf`, `easylaw-financial-transactions-pdf`, `easylaw-industrial-accident-pdf`, `eps-system-tab06`, `news-bss-bn-boesl-returnee-aid-2026`, `embassy-bd-counterfeit-documents`, `asianews-korea-immigration-dragnet`, `whic-working-holiday-guide-2026`, `bb-remittance-top30-countries`, `bb-remittance-selected-country-monthly`, `wewb-annual-report-2023-24`. I registered `eps-faq` (it was fetched by R but not in `sources.csv`).

### What was searched

- Bangladesh Embassy Seoul site (contact, officers, wing contacts, labour counselling, dead body, office and consular hours, bank details, Travel Permit, fee charts).
- MOJ press releases (2024 extension, 2025-26 special programme, June 2026 policy review), MOJ enforcement page, Hi Korea advance-report page, Korea.net 2020 article; searches in Korean for a 2026-27 programme (none found as of 19 Nov 2026).
- NPS lump-sum refund page (English, dated 15 June 2026).
- FSS FINE registry of small-sum remittance firms (4 pages), bKash partner list, Hanpass registration page, Nagad (no Korea partner list).
- Korea Customs hwanchigi notice; Easy Law notice on daepo tongjang penalties.
- Bangladesh Bank remittance data (country table to April 2024; top-30 PDF for July-September 2026).
- EPS insurance page (eps.go.kr tab 06), Daily Star 2022 unclaimed insurance, ICSF reprint of a 2024 Korean Embassy release, UNB 2019 seminar, BSS 2026 BOESL aid, Korea Times 2026 K-COMWEL interview.
- Bangla searches on deaths and body repatriation from Korea (nothing specific found).

### What happens in practice

- **Unclaimed insurance is a real, recurring loss.** HRD Korea's EPS Center in Dhaka hunted for 300+ returnees in 2022 (Tk 30,000-3 lakh each) and about 400 more around 2024 who left Departure Guarantee and Return Cost money behind (B0246, B0269). The draft therefore puts the claims as numbered steps in Coming home.
- **Crackdowns are frequent.** A Bangladeshi in Hwaseong (Korea Herald, Feb 2026) describes raids every 1-2 months, now in subways and markets; MOJ counts ~140,000 deported, fined or ordered out in 2024 (B0261-B0265).
- **Repatriation of bodies is not covered** by Korea's industrial accident insurance; families often abandon remains (K-COMWEL head, Korea Times, May 2026; B0237-B0239). Casualty Insurance (up to 30 million won) covers only non-work deaths.
- **BOESL holds a refundable security deposit** from EPS workers to make them return on time (BSS, Aug 2026; B0243). The amount and the refund procedure were not found.

### Conflicts between sources

- **Labour wing email:** officers page and wing list give labourwingseoul@gmail.com (B0130, B0131); the counselling page gives laborwingseoul@gmail.com (B0133, not cited); WEWB's 2023-24 report gives fsseoul@probashi.gov.bd (B0273). The draft gives the first and the WEWB one.
- **Labour wing title:** "Counsellor (Labour)" (officers page), "Counsellor (Labour Welfare)" (wing list, Jan 2025), "First Secretary (Labour)" (counselling page, 2023). Same person; the draft uses Counsellor (Labour).
- **Travel Permit fee:** 30,000/15,000 won in April-June 2025; 45,000/30,000 won in October-December 2026. The draft uses the current chart.
- **Insight (Nov 2025) article** shows today's date in its header and was found by search as a "June 2026" item; its publish date is 29 Nov 2025 and it describes the same 2025-26 programme. Deleted, not used.
- **Customs currency limit** (USD 10,000 vs USD 5,000) and **jewellery allowance** conflicts carried over from Singapore (B0090, B0091, B0085, B0093).

### Facts logged but not used, and why

- B0003 (USD e-passport fee at missions): Seoul charges in won (B0143), and passports are R's topic.
- B0057, B0058, B0070 (JBC partial-disability rows, exclusions): kept short; the full schedule is in the Singapore doc model.
- B0091, B0092, B0098 (customs conflicts and details): only the main rules kept.
- B0100, B0103 (PKB loan document list, returnee complaint), B0104, B0105 (RAISE ended June 2026), B0108 (scholarship start year), B0112 (agency complaints): belong to other sections or are history.
- B0120 (Prothom Alo on WEWB body policy): official WEWB facts cover it.
- B0133 (misspelled email), B0143 (e-passport fee), B0151, B0154 (rider crackdown), B0167, B0169, B0184, B0185, B0195, B0202 (Sentbe, not a bKash partner) and duplicates of cited facts.

### Pages we could not download

- MOJ press release PDF for the 2025-26 programme, https://www.moj.go.kr/bbs/moj/182/487751/download.do (HTTP 307; the article page and MOJ blog were saved instead).
- Bangladesh Embassy "Other Consular Services" box, https://seoul.mofa.gov.bd/en/site/view/dynamic_boxs?service_box_category_id=8612f936-451b-48bc-b16a-55e866bf3082 (404).
- Korean Embassy Dhaka contact page, https://overseas.mofa.go.kr/bd-en/wpge/m_2128/contents.do (redirect loop; Firecrawl returned a different page).
- HRD Korea English EPS page, https://www.hrdkorea.or.kr/ENG/4/1 (empty).
- Immigration Act English text at elaw.klri.re.kr (body loads by script; only the table of contents came down). Needed for entry-ban periods and detention rules.
- Businesspost article on the returnee community launch (saved page had no article text; deleted).

### Open questions (also in the draft as Need to know)

- Overstay fine schedule (Immigration Act Enforcement Rule, Table 7) and entry-ban lengths by overstay length and by voluntary vs forced departure.
- Whether a 2026-27 special voluntary departure period is announced; whether 2025-26 leavers can return on E-9.
- Detention: where Bangladeshis are held (Hwaseong, Cheongju), how long, who pays the ticket, whether the labour wing visits.
- Travel Permit processing time; police report for lost passports.
- Death statistics of Bangladeshis in Korea; cost of body repatriation and who pays for EPS workers.
- Nagad partners in Korea; fees of E9pay, GME, Gmoney Trans, Hanpass.
- EPS Center Dhaka phone/email/hours; current returnee job-matching with Korean companies in Bangladesh.
- BOESL's security deposit amount and refund steps; how a returnee in Bangladesh claims insurance left in Korea.
- Bangla-speaking migrant worker centres (Ansan, Gimhae, Hwaseong, Pocheon).

## Fact-check reports

Each part's full change list is in `verify/part1-report.md` to `verify/part6-report.md` (kept in the working folder, not committed). Main open issues they left:
- BOESL's EPS cost table is out of date and contradicts itself (a US$240 total against items adding to Tk 38,584); the real 2026 total is unknown.
- The ban for cheating in the EPS-TOPIK is given as 2, 3 or 4 years by different sources.
- The Bangladesh Embassy in Seoul's labour-wing contact is given three ways on its own pages.
- Bangladesh's own 2026 EPS quota was not found.
- When the Return Cost Insurance is paid conflicts: before departure (EPS) or after departure is confirmed (the Enforcement Decree).

## Prothom Alo archive pass, chunk 1 (prefix PR)

14 Prothom Alo (and Bondhushava) articles from 2024 to November 2026 read in full; 13 saved with save_pa.py and 57 facts logged (PR0001-PR0057). PR0010 is logged but not cited (conflict below).

### Resolved conflicts

- Part-time hours for master's students: a November 2025 student-written piece (PR0010) says up to 40 hours a week. The Ministry of Justice rules already cited (V0135: 15 hours without the language level, 30 weekday hours with it, 35 at a certified university, no weekend limit) are primary and official; kept V0135, PR0010 not cited.
- BOESL's address and phones: an August 2024 article gives BOESL's EPS branch at Probashi Kallyan Bhaban, 4th floor, and phones 48319125, 48317515, 58311838. The doc's Contacts (B0250, from BOESL itself) give the 5th floor and 58313838. BOESL's own page is primary and newer; 58311838 looks like a misprint of 58313838. Not logged; the 4th-floor EPS branch may be a separate desk, but the 2025-26 notices send candidates to Room 701 (7th floor) for EPS applications anyway.
- Bangladeshis in Korea: a March 2025 piece says "more than about 30,000"; Korea's own count of 44,721 on 30 September 2026 (C0044) is official and later. Not logged.
- Departures since 1994 (53,678 to 2023, North South University researchers, PR0015) against BMET's 39,702 from 2004 to May 2025 (C0055): different start years (the 1994 figure includes the pre-EPS years), so both kept with their periods.
- Education consultancy cost article (PR0011, PR0054): its own figures differ slightly between paragraphs (public tuition Tk 3.93 lakh vs 3.98 lakh; living Tk 8.24-11 lakh vs 8.40-11.20 lakh). The doc cites only the totals the writer uses for the budget.

### Not used, and why

- Ranking listicle (f1aa1ff7, 2024): unnamed ranking, no usable fact.
- NSU column (9c22e166): 2022 sector shortage figures and the 2022 69,000 E-9 quota are stale against the 2026 quota (C0037); the "16 EPS countries" figure is superseded by 17 (C0004); annual departures 2019-2022 duplicate C0054; 2021-22 remittance duplicates C0102.
- EPS worker opinion (77c0b798): his prediction that EPS in Bangladesh would close without a circular in one to two months is superseded by BOESL's July 2026 circular (C0001); his Vietnam comparisons are opinion.
- Silver-economy column (5ac4bc98): only the Korea KDI figures are Korea-specific; the NSDA caregiving training line is held for the global modules.
