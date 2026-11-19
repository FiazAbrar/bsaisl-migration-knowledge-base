# Japan: research notes

Research notes behind `doc.md`, one section per research topic (fact prefix in brackets); KA to KF are the fact-check pass and KG the final audit.

## How the doc was put together

- Six topics researched in parallel, merged (the rights sections became their own H2, "Living and working in Japan", since they apply to both work routes), split into six parts and checked sentence by sentence by independent verifiers (about 205 fixes: rotated and off-by-one citations, the ITEE levels Japan recognises (FE and AP, not IP), VFS charges by visa type, the remitters on the FSA register, the Embassy's emergency numbers, overstated asylum and student-work claims), then audited (35 duplicate headings made unique, repeated procedures given one home, Start here added).
- Exchange rate: Bangladesh Bank's cross rate of 19 October 2026 (archived copy): ¥1,000 is about Tk 782.
- Fact R0066's claim text was corrected by the lead: of the January 2026 fields, only warehousing and resource circulation are "not yet started".
- Firecrawl's credits ran out early; blocked pages came from the Wayback Machine (several Embassy of Japan in Dhaka pages are 2020-21 copies) or are listed under each topic.
- Open issues: the Tk 148,500 cost rests on one quote by a BMET training-centre principal (attributed in the doc); the end of transit visas on 1 July 2026 rests on a VisaVerge report; the baby-passport fee (¥17,000 or ¥18,000) and the Embassy's emergency numbers conflict between Embassy pages; the Ministry's SSW guideline PDF could not be downloaded.

## Background and corridor (insider pass) (prefix C)

### What was searched

- **Japanese official:** ISA end-2025 foreign-resident press release and tables (PDF text layer lost Japanese labels; rows read from page images); e-Stat 在留外国人統計 2025年12月 第1表 (nationality x status, downloaded as xlsx and converted; Bangladesh, Nepal, Sri Lanka, Pakistan, India and total rows saved as `estat-residents-by-nationality-status-2025-12.md`, raw xlsx kept); ISA SSW statistics page and the June 2026 and December 2025 Table 4 xlsx (SSW (i) by nationality and field, converted to .md); ISA "Information on Bangladesh" SSW page, the Bangladesh procedure PDF (no Japanese text layer; transcribed from images into `isa-ssw-bd-procedure.transcription.md`), the 2019 MOC (English) and the 2022 note verbale; MHLW TITP MOC page; OTIT list of approved Bangladeshi sending organisations (Oct 2026) and the list of removed ones (July 2026); ISA ESD outline (July 2026 revision) and the ESD ordinance slides; ISA missing-intern figures 2021-2025 (dated July 2026; transcribed); ISA 2022 intern-fee survey (transcribed); ISA refugee statistics 2025 (press + tables, Bangladesh row transcribed); ISA 2023-amendment page; ISA student-status tightening (April 2026); MHLW FY2026 minimum wages (transcribed from image, all 47 prefectures); Kagawa Prefecture page on the 23 Jan 2026 Cabinet caps; Prometric SSW fee and test-centre pages; JFT-Basic about page; SSW portal FAQ; OTIT 2026 English handbook.
- **Bangladesh official:** BMET annual table image to May 2025 (Japan column transcribed by hand into this folder's `bmet-annual-by-country-2025-05-img.md`); OEP country clearance 2022-2025 and 1 Jan-18 Nov 2026 (copied from south-korea); Bangladesh Bank top-30 remittance PDF (Japan row read from the image; the text layer misaligns rows) and the selected-country monthly page (copied from south-korea).
- **News:** BSS (28 Apr 2026, 18 Jun 2026), Financial Express (Mar 2019, Sep 2025, Apr 2026), Prothom Alo English (Oct 2019, Oct 2025), Dhaka Tribune (Apr 2026), Ittefaq English (Oct 2025), Daily Observer (Jun 2026), bdnews24 Bangla (Aug 2023), Daily Star (Oct 2019; 2017 Reuters Fukushima), TBS (Oct 2019, Oct 2020), Asia News Network (Sendai school).
- Bangla searches: জাপানে কর্মী পাঠানো ২০২৬ খরচ; জাপান অভিবাসন ব্যয় ১ লাখ ৪৮ হাজার ৫০০; জাপানে পাঠানোর কথা বলে প্রতারণা গ্রেপ্তার ২০২৬; জাপান যেতে কত টাকা লাগে ভাষা শিক্ষা কেন্দ্র.
- Firecrawl was out of credits for the whole session; WebSearch and curl were used instead.

### Conflicts between sources

- **Departures by year.** BMET table 2023: 967 vs OEP 965; 2024 both 1,088. OEP 2022 shows only 14 (OEP covers part of 2022); BMET's 508 used. 2025: BMET table stops at May (454); OEP full year 1,564 used.
- **Bangladeshis in Japan.** Ministry sources (Prothom Alo, Oct 2025) said 26,000; ISA says 35,073 at end-2024 and 44,938 at end-2025. ISA used.
- **Number of agencies for Japan.** 10 government-appointed agencies (2019); 27 permitted (Prothom Alo, Oct 2025); 95 "approved by Japan" (BSS, Apr 2026); OTIT list has 103 entries (Oct 2026, TITP only, including BMET and BOESL). The doc uses OTIT. The SSW list on probashi.gov.bd was not read.
- **TTCs teaching Japanese.** 32 (2019), 39 TTCs + 5 IMTs (2023), 53 (2026). Latest used for the current figure.
- **SSW target.** BSS/FE (Apr 2026) still quote 820,000 by March 2029; the Cabinet reset it to 805,700 on 23 Jan 2026 (Kagawa Prefecture page). Official figure used.
- **Students' 28-hour limit.** FE (28 Apr 2026) says students may work "more than 28 hours per week"; ISA says 28 hours with a comprehensive permission. Used as a myth.
- **Cost.** 2019: "zero migration cost" for interns; 2026: Tk 148,500 "government-approved cost" (BKTTC principal, BSS). No official circular found. Kept as Need to know.
- **Bangladesh Bank top-30 PDF text layer misaligns rows.** Reading the image, July-Sept 2026: Japan 32.73, Korea 108.01. The south-korea C draft cites US$16.76 million for Korea (C0101 there), which in the image is Cyprus's row. Worth telling the Korea lead.

### What happens in practice

- The real bottleneck is Japanese plus the field skills test. Only four SSW tests are offered in Bangladesh (JFT-Basic, care, agriculture, construction), which matches where Bangladeshi SSW workers are (agriculture 334, care 326, construction 168 of 1,189 in June 2026). Food service (105) and others presumably sat tests in Japan (students switching status) or elsewhere; not confirmed.
- Most Bangladeshi workers in Japan are former students: 14,983 students and 8,719 gijinkoku holders vs 2,198 interns and 839 SSW at end-2025.
- Bangladeshi interns are few but have a higher missing rate than the average (1.9% in 2024 vs 1.2% overall; 1.3% vs 0.6% in 2025).
- OTIT removed nine Bangladeshi agencies on one day (30 July 2026); the reason is not given on the list.
- TMSS's recruiting arm was fined in 2019 (as TMSS ICT and as "Northern Recruiting Agency", Mirpur) for unauthorised Japan recruitment; in June 2026 TMSS Northern Recruiting Agency held a Japan/Korea job fair at BKTTC with the Tokyo embassy's First Secretary (Labour) as special guest (BSS). Not put in the draft as an allegation because the 2026 status of its Japan permission is unknown; flagged here for the agency doc.
- Refugee claims by Bangladeshis rose from 80 (2021) to 777 (2025). With 821 Bangladeshis on Designated Activities, some are probably claimants; not confirmed.

### Facts logged but not used, and why

- C0003: duplicate of C0007 (total clearances).
- C0017, C0018, C0020, C0024: all-nationality SSW totals; the doc uses the Bangladesh figures and the overall 390,296.
- C0028, C0029, C0030, C0031, C0040, C0045, C0047: detail of the MOC and OTIT lists, kept for the main-route and contacts sections.
- C0044: quote does not support the full claim (use C0048/C0049 instead).
- C0062-C0064: Nepal and Sri Lanka by status; available for comparison.
- C0070 (one extra year to retake SSW test), C0071 (duplicate of C0073), C0097 (Ibaraki wage), C0104 (main nationalities of refugee applicants), C0112 (ISA leaflets), C0115 (Japan Cell), C0120 (500,000-worker aim: an unverified speech figure), C0153 (fee-cap bill), C0159 (passport confiscation ban, covered by E), C0172 (interview through placement firms).

### Cross-references used (check against final headings)

- From E draft: Minimum wage; How you are paid, and what may be deducted; Technical intern trainees: changing training site; SSW: changing employer; The new rules from April 2027; Overstay and unauthorised work; Selling or lending your bank account or phone.
- Within this draft: What ties you to the employer; Beliefs against the facts.
- Asylum: no draft heading yet; the lead should match it.

### Pages we could not download

- https://probashi.portal.gov.bd/sites/default/files/files/probashi.portal.gov.bd/policies/d7925921_9643_4701_85ec_7ca2f5e7020a/Guidline%20SSW.pdf (ministry SSW guideline: connection failed; no Wayback capture). It should hold the official SSW cost rules.
- https://www.mofa.go.jp/mofaj/press/release/press4_007746.html (MOFA press release on the 2019 SSW MOC; 403). The ISA page covers the same facts.
- https://online-d11.thedailystar.net/news/bangladesh/news/japan-considering-more-skills-testing-centres-recruit-bangladeshi-workers and https://online-d11.thedailystar.net/opinion/views/open-dialogue/news/japan-has-opened-its-door-bangladesh-lets-not-ruin-it-4017886 (connection failed).
- https://www.prothomalo.com/business/বিনা-খরচায়-জাপান-যেতে-যা-লাগবে (404).
- https://www.my.emb-japan.go.jp/itpr_en/newinfo_13102020.html (Japanese embassy in Malaysia warning on study-and-work scams; 403).
- probashi.gov.bd list of approved SSW sending organisations for Japan (linked from the ISA page) was not attempted for lack of time.

### Housekeeping

- `isa-residents-end2025-xlsx` was fetched by fetch.py as garbled HTML; I deleted the files and its _fetchlog row (rewriting _fetchlog.csv; other rows preserved at that moment).
- Transcription files added: `bmet-annual-by-country-2025-05-img.md` (Japan column, replaces the copied S. Korea text), `isa-ssw-bd-procedure.transcription.md`, `isa-refugee-2025-tables.transcription.md`, `isa-titp-missing-2024.transcription.md` (the PDF is the July 2026 edition covering 2021-2025), `isa-titp-fees-survey-2022.transcription.md`, `mhlw-minwage-fy2026.transcription.md`, `bb-top30-country-remittance.transcription-japan.md`.
- One fact (palo-expat HSC/height) was dropped by a concurrent write and re-logged as C0137.

### Personal data

- `ds-fukushima-asylum` names a Bangladeshi asylum seeker; another agent's saved copy is marked as redacted in sources.csv. Not named in the draft.
- C0181 names the chairman and MD of Visa Guide Center from a court report; not named in the draft.

## Work routes: SSW, technical interns and ESD (prefix R)

Researcher prefix R. Draft: `drafts/R-work-visas.md`. 297 facts logged (R0001-R0297): 260 from official sources (160 verified, 97 possibly-outdated, 3 conflict), 37 news/research (unofficial).

### What was searched

- ISA (moj.go.jp/isa): SSW materials PDF revised 23 Oct 2026 (930004452.pdf, the backbone: fields, periods, support plan, RSOs, MOC list, flow before work); ESD outline (001452485, July 2026) and ESD ministerial-ordinance summary (001451331, undated); COE procedure page; SSW status page; residence-card page.
- ISA SSW support website (ssw.go.jp/en): exam schedules by country (Nov-Dec 2026), steps, support, required documents, FAQ, call centre, events.
- Japan Foundation JFT-Basic site (about, FAQ, registration flow) and Prometric's SSW site (JFT-Basic page, fee by country, payment, overseas centres, ID rules, Bangladesh notices, test list).
- JLPT overseas host list; JUAAB (JLPT host in Dhaka) site, Dec 2025 circular and new JLPT portal (juaabjlpt-bd.org).
- OTIT: Bangladesh TITP sending-organisation list (6 Oct 2026), ESD sending-organisation/MOC pages, Bangladesh ESD tentative list, trainee handbook 2026 (fetched by another agent), native-language consultation page.
- MHLW: Japan-Bangladesh TITP MOC (Japanese; only first pages have a text layer).
- Embassy of Japan Dhaka visa page; VFS Global one-pager and long-term (COE) checklist.
- Bangladesh Embassy Tokyo: labour wing and community/employment pages (fetched by another agent).
- Bangladesh side: copied from `countries/singapore/sources` (OEP guide, BMET charter, safe migration leaflet, welfare fee circular, WEWB, JBC insurance, PKB, passport, PCC, 2013 Act) and re-quoted as R0001-R0061; the Bangla PDF rows carry `--no-quote-check` with the original transcription note.
- News (English and Bangla): Dhaka Tribune, TBS, BSS, Bonik Barta, Financial Express, bdnews24 (EN/BN), Prothom Alo (EN/BN), Jugantor, Daily Observer, Daily Star, Digi Bangla, Ittefaq; DU Journal of Japanese Studies article (Saidur Rahman, 2026).

### Conflicts and points to know

- **Number of fields.** ISA's Oct 2026 PDF says 19 SSW (i) fields, three added in January 2026 (linen supply, warehousing, resource circulation) that start "once preparations are completed"; the ssw.go.jp steps page and all Bangladeshi news still say 16. Draft lists 19 and flags the three as not yet started.
- **SSW (i) period per grant.** ISA PDF: up to 3 years per grant (current). ssw.go.jp FAQ (undated) says 4 months, 6 months or 1 year; outdated, not used.
- **Number of Bangladeshi agencies approved for Japan.** 96 (Bonik Barta, Jul 2025, citing BMET), 27 (Prothom Alo, Oct 2025, citing ministry sources), 95 (DT/TBS, Apr 2026). OTIT's TITP list of 6 Oct 2026 has 103 OTIT numbers (BGD...), 60 with RL numbers; 21 formerly approved; ESD tentative list 97 entries. Draft gives the news range and points to OTIT's list.
- **JLPT fee:** Tk 3,060 (Dec 2025 circular) vs Tk 4,356 (Dec 2026 portal). Draft uses the current one.
- **PCC fee:** Tk 1,500 (portal) vs Tk 500 (police guidance), inherited from Singapore (R0011/R0014).
- **Welfare fee:** Tk 5,500 from 1 Oct 2026 (circular, R0036) vs Tk 3,500 in BMET's Sep 2026 charter (R0037, status conflict).
- **100,000 workers.** May 2025 MoUs (BMET with KDS and NBCC/JBBRA) were reported as Japan taking 100,000 workers over five years; Japan's MOFA said on 29 Oct 2026 no such agreement exists. Draft uses this as a scam/belief item.
- **The "zero cost" claim.** 2019 ministry statement (employers pay the agency) and IM Japan route (zero cost) vs 2025 adviser ("not very high") and an agency licence cancelled for overcharging. No official figure for what SSW workers may be charged was found.
- **Test organisers.** Prometric runs JFT-Basic and the long-term care, agriculture and construction tests in Dhaka (fees BDT 3,800 / 1,600 / 2,700 / 800). Building cleaning and automobile transportation tests had Bangladesh dates in Nov-Dec 2026 but are not Prometric tests; organiser, venue and fee not found. Food service had no Bangladesh dates in Nov-Dec 2026.
- **Mapping of ssw.go.jp schedule tables to fields** was done from the HTML anchors (headline ids), not the flattened text; checked: For All Fields (JFT), long-term care, building cleaning, construction, automobile transportation (headline-1747188232), agriculture include Bangladesh.

### What happens in practice (from news/research)

- Language is the bottleneck: Dec 2024 JLPT in Bangladesh, N4 511 of 3,091 passed, N5 3,883 of 8,064. Learning takes about six months and many drop out for lack of money (BMET DG). Trainers are mostly returnees without formal training (ILO policy adviser, Bonik Barta).
- Flow is tiny: 3,574 workers to Japan in 2024 vs Nepal 56,707; 5,014 through agencies 2004-Apr 2025; 702 via IM Japan 2017-2024.
- Fake certificates and forged bank statements blamed for Japan visa appointment problems (Chief Adviser's special envoy, Jul 2025).
- Japan Cell set up in the Ministry; Facebook page and email channel; separate website planned. Contacts not found.

### Facts logged but not used, and why

- R0008, R0018, R0047, R0053: passport payment channels, PKB mygov detail, partial-disability shares, re-entry loan docs: detail belongs in the shared Bangladesh-side sections.
- R0042: BMET GRS chain: kept for the lead's contacts section.
- R0082, R0092, R0106, R0110: employer-side criteria (no violations in 5 years, 5-year cap repeated, construction registered corporation, hiring caps) with no action for the worker.
- R0115, R0116, R0128, R0134, R0135, R0137, R0138: ESD details covered by other cited facts or employer-side.
- R0141: weak quote (whitespace in PDF); replaced by R0297.
- R0185, R0207, R0217, R0256, R0263, R0279: duplicates, superseded figures or Background material (R0256/R0263 suit Background, "size of the flow").

### Housekeeping

- I regenerated the .txt of three ISA ESD PDFs (isa-esd-001452485, -001451331, -001460373), mhlw-titp-moc-001417418, otit-bgd-esd-provisional-2026-10, and also otit-bgd-sending-orgs-2026-10 (fetched by another agent) with `pdftotext -enc UTF-8 -layout`, because fetch.py's text copy dropped the Japanese characters. English content is unchanged; another agent's quotes from otit-bgd-sending-orgs-2026-10 should be re-checked.
- One concurrent-write loss seen: R0282 was overwritten once; re-logged as R0288. All 274 cited ids were checked present in facts.csv at handover.

### Pages we could not download

- https://probashi.portal.gov.bd/sites/default/files/files/probashi.portal.gov.bd/policies/d7925921_9643_4701_85ec_7ca2f5e7020a/Guidline%20SSW.pdf (Ministry's SSW guideline; connection fails; no Wayback capture; Firecrawl out of credits). Most important missing source: likely holds the Bangladesh-side SSW procedure and any fee cap.
- https://www.mofa.go.jp/mofaj/ca/fna/ssw/us/overview/ and /introduction/ (403).
- https://www.bd.emb-japan.go.jp/en/visa/visainfohowto1.html and https://www.bd.emb-japan.go.jp/itpr_en/ISA.pdf (403).
- https://www.jpf.go.jp/jft-basic/e/schedule/index.html (403).
- https://www.jagonews24.com/en/national/news/91920 (Japan Cell, Oct 2026) and /97477 (403).
- https://online-d11.thedailystar.net/... "Japan has opened its door for Bangladesh, let's not ruin it" and "Japan considering more skills testing centres"; https://d11.thedailystar.net/nrb/migration/news/japan-emerges-lucrative-labour-market-3360221 (connection failed).
- https://www.bangladeshmonitor.com.bd/lead-news-pdf/chief-adviser-orders-action-to-curb-fake-skill-certificates (404).
- Firecrawl was unavailable all session (credits exhausted).

### Open questions (also in the draft as Need to know)

- Current Bangladesh cap on what an SSW/TITP worker may pay, and real 2026 street costs.
- Official list of agencies approved for Japan SSW; Japan Cell contacts.
- Building cleaning and automobile transportation test organisers in Dhaka; food-service test status.
- COE validity period for the visa; whether PCC is required.
- Who pays the air ticket; IM Japan intake in 2026; OTIT Bengali line; Bangladesh ESD MOC text.

## Living and working in Japan (prefix E)

Researcher prefix E. Draft: `drafts/E-life-rights.md`. Facts E0001 to E0310 (310 rows). Firecrawl credits ran out after the first scrape (19 Nov 2026), so everything after that was saved with `fetch.py` (curl) or saved by hand from a plain-text file the publisher serves (Kanagawa Police text versions).

### What was searched

- MHLW minimum wage FY2026 (saiteichingin, MHLW national list PDF). The PDF's text layer is garbled; a Firecrawl markdown copy was saved as `mhlw-minwage-fy2026.md` next to the PDF.
- OTIT: home, English trainee page, native-language consultation page, consultation leaflet, OTIT-to-ESDO renaming notice (19 Nov 2026), transfer page, and the full **2026 Technical Intern Trainee Handbook (English)**, which was the richest single source (labour law, wages, deductions, insurance, tax, lump sum, rōsai, crime warnings, all hotlines). Read sections 1 to 23 and the rōsai/employment insurance annex.
- ISA: SSW system overview (Oct 2026), SSW status page, ESD outline (Jul 2026) and ministerial-ordinance summary, notification of contracting organisation, address change, re-entry permit, extension (new fees from 1 Oct 2026), revocation of status and 2024 revocation statistics, deportation Q&A (landing-denial periods).
- Japanese Law Translation: MOJ Order No. 5 of 2019 (SSW contract and support plan criteria) and the Technical Intern Training Act (Articles 46 to 49, 108 to 111).
- Japan Pension Service: English lump-sum page, Japanese 脱退一時金 page (updated 1 Apr 2026, FY2026 amounts), claim form PDF (English, March 2026).
- JOHAS wage advance payment page; MHLW harassment page (Nov 2026); Kanagawa and Hiroshima police pages on bank-account sales; FSA bank-account guide for foreigners (Sept 2024, saved by another agent).
- Bangladesh Embassy Tokyo pages (saved by another agent): labour wing (Oct 2026), phones and emails (June 2026), contact (Dec 2025), address/hours.
- NGOs: POSSE foreign-worker consultation page; CLAIR list of prefectural multilingual centres.
- Searches (English, Japanese, Bangla) for Bangladeshi trainees in Japan: unpaid wages, runaways, broker debt. Found nothing Bangladesh-specific for Japan in 2025-2026; coverage is overwhelmingly about Vietnamese and Myanmar trainees.

### Conflicts between sources

- **Embassy emergency numbers:** Contact page (updated 15 Dec 2025) lists 080-7004-1971, 070-1260-1984, 080-4065-6601 and Labour Wing Counsellor at ext. 201, email zakir2kbd@gmail.com. Phones page (8 June 2026) lists only 090-3558-1968; emails page (8 June 2026) lists the labour wing as First Secretary (Labor), fslabor@mofa.gov.bd and zoynalabedin10@yahoo.com. Draft uses the June 2026 pages and puts the conflict in a Need to know (E0123 logged as conflict).
- **Bank-account sale penalty:** Hiroshima Police page still says 1 year / 1 million yen. Kanagawa Police (page dated 17 Sept 2026) says the amendment was promulgated 10 June 2026 and partly in force 10 July 2026, and its text flyer says the penalty "will become" 3 years / 5 million yen. It is not clear which part took effect on 10 July. Draft states the new penalty "under an amendment promulgated on 10 June 2026". Worth a Need to know if the lead wants the in-force date.
- **OTIT hotline days:** the OTIT leaflet and the handbook give English as Tuesday/Thursday 11:00-19:00 and Saturday 9:00-17:00; consistent. Other languages differ between older third-party leaflets (MAFF, Hiroshima Pref.) and OTIT's own; we use OTIT's.
- **MHLW foreign-worker phone line days:** the handbook's table is garbled for which weekdays each language runs. English is 0570-001701, 10:00-15:00 (noon-13:00 break). Draft omits the days.
- **E0281** was logged with page date 2026-07 but `sources.csv` (registered by another agent) dates `kanagawa-police-account-sale` 2026-09-17. Status (verified) is the same either way; lead may correct the page_date.

### What happens in practice (evidence found)

- 2024 status revocations: 1,184, of which 710 technical intern trainees and 761 under the "3 months without activity" ground (ISA press release, 14 Mar 2025). This is the realistic risk for a runaway or someone who quits an SSW job and doesn't find another.
- JOHAS paid about 11 billion yen to 30,591 people in FY2024 under the unpaid-wage advance scheme.
- Hiroshima Police report trainees selling bank accounts or withdrawing scam money "like a part-time job".
- The lump-sum refund trap: a worker who does 3 years TITP and then 5 years SSW without leaving Japan is paid for only 60 months and loses the rest; the JPS form itself uses this TITP-then-SSW example.
- Renewal fees jumped from 6,000 yen to 25,000-64,000 yen on 1 Oct 2026; who pays in practice is unknown.

### Facts logged but not used, and why

Most are second quotes for a sentence that already cites a stronger row, or background for other sections (Background, arrival steps):

- E0043: OTIT examples: passport, residence card or bankbook taken; mobile phone banned
- E0093: Employment insurance basic allowance: notice of separation to Hello Work
- E0129: Accepting org must provide support in a language the worker understands
- E0140: Accepting org must notify ISA of changes, termination or new SSW contracts
- E0141: Annual notification includes number of missing employees and remuneration payment status
- E0142: After entry: register as resident at municipality, open salary bank account, secure housing
- E0165: Extension can be applied from 3 months before expiry
- E0168: Reduced fee 10,000 yen for some people
- E0212: Voluntary resignation: no basic allowance for 2 months after 7-day waiting
- E0215: Also disqualifying: assault/threat/confinement, withholding pay, restricting going out
- E0216: Disqualifying: unfairly restricting going out
- E0225: Support: airport pick-up and drop-off
- E0230: Revocable if not doing permitted activity and doing other activity
- E0243: SSW gets social insurance and pension
- E0252: FSA counselling 0570-016811 weekdays 10-17
- E0288: Can report implementing or supervising organisations that violate the law
- E0289: Native languages offered: Vietnamese, Chinese, Indonesian, Tagalog, English, Thai, Cambodian, Myanmar (no Bengali)

### Pages we could not download

- https://www.moj.go.jp/isa/content/001468647.pdf (SSW operating guidelines, Aug 2026): text layer garbled; deleted. Needed for the passport-custody wording for SSW and the job-change procedure.
- https://www.moj.go.jp/isa/content/001442736.pdf and https://www.moj.go.jp/isa/content/001417869.pdf (ISA SSW warnings and procedure guide): image PDFs, no text; deleted.
- https://www.moj.go.jp/isa/content/001386304.pdf (SSW notification Q&A): garbled; deleted.
- https://www.moj.go.jp/isa/content/001425159.pdf (missing trainees by nationality 2020-2024): numbers extract but labels don't; deleted. Would give Bangladesh's runaway count.
- https://www.nenkin.go.jp/international/japanese-system/withdrawalpayment/payment.files/E.pdf and the matching A.pdf: 404 (the working copy is under /shinsei/jukyu/sonota-kyufu/20150406.files/A.pdf, saved as `jps-lumpsum-claim-en`).
- https://www.nenkin.go.jp/service/jukyu/sonota-kyufu/dattai-ichiji/20150406.html: 404 (moved to /service/jukyu/seido/..., saved).
- https://migrants.jp/ (Solidarity Network with Migrants Japan): renders empty with curl; Wayback copy was from 2019, so discarded. Firecrawl needed.
- http://zwu.or.jp/ (Zentoitsu Workers Union): site last updated ~2020, no contact details; discarded.
- https://jsite.mhlw.go.jp/fukui-roudoukyoku/content/contents/001661011.pdf (wage advance leaflet): 404.

### Open gaps (also in the draft as Need to know)

- Who files an SSW change-of-status application on changing employer, how long it takes, and whether work may start before approval (official source not saved; third-party sites say approval first, 2-3 months).
- Bangladeshi runaway ("shissō") numbers for TITP/SSW.
- Labour wing's real track record and current extension; any Bengali-speaking NGO or union in Japan.
- Real housing deductions, support-organisation fees, broker fees for transfer jobs, and lump-sum claim agents' fees.
- Wage-claim time limit (3-year transitional rule) and how an LSIO handles a foreign worker's report in practice.

## Visit, business, student, transit and medical visas (prefix V)

Researcher prefix V. Facts V0001 to V0203 in facts.csv. Draft: drafts/V-visits-students.md.

### What was searched

- Embassy of Japan in Bangladesh (bd.emb-japan.go.jp): live visa page (via Firecrawl before credits ran out), "Additional Documents Required" (Wayback, 17 Nov 2025), "How to obtain Japanese Visa" (Wayback, Apr 2026), "Attention" scam notice (2014). curl gets 403 on the site.
- VFS Global Bangladesh one-pager (fees, service charges, processing), short-term, long-term (COE) and multiple-entry checklists.
- MOFA (mofa.go.jp, 403 to curl, all via Wayback): visa index (June 2026), visa exemption list (Sept 2025), working holiday (Nov 2026), visa FAQ (2023), visa fees (June 2026), medical stay page (2019) and guarantor list (Nov 2026).
- ISA (moj.go.jp/isa, curl works): Temporary Visitor and Student status pages, permission for activity outside status (general, Student, job-hunting), job-hunting Designated Activities, COE page, COE document list for unrated language schools, April 2026 "Student" tightening PDF, language-school reporting duties page.
- e-Gov law API for the Immigration Control and Refugee Recognition Act full text (shore pass, transit landing, penalties, cancellation, landing bans, Art. 20(3) on changing from Temporary Visitor).
- Bangladesh Bank FEPD-1 consolidated circular No. 40 (30 Sep 2026) on study remittances.
- JASSO Study in Japan academic fees; JASSO Student Guide 2019-2020 (airport procedures).
- Bangladesh Embassy Tokyo pages (saved by another agent; I logged my own facts from them).
- News: Ajker Patrika (Mymensingh Japan visa fraud, Sept 2026), BSS (ambassador on student numbers and loans, Apr 2026; July 2025 Osaka seminar), Asia News Network/Yomiuri (Sendai school penalty pledges, 2023), VisaVerge (end of transit visas, 2026).
- Searched Bangla news for Japan student-agent fraud, "study and earn", fake guarantors and visit-visa job scams: found only the Mymensingh case. The TBS Tk 15.5 crore study-consultancy scam (Just Thought Education Consultant) was not Japan-specific, so it was dropped.

### Key findings

1. Since 3 Nov 2024 all Japanese visas in Bangladesh go through VFS (Delta Life Tower, Gulshan-2). Visa is free for Bangladeshis; VFS charges BDT 2,090 (short-term) or BDT 1,900 (study/work/transit sections still show this older figure), cash only.
2. Japan stopped issuing transit visas on 1 July 2026 and raised visa fees to ~15,000/30,000 yen, but the Dhaka embassy page (live, Nov 2026) still says "Free for Bangladeshi nationals".
3. ISA's April 2026 "Student" tightening: schools check each student's part-time work every 3 months and report illegal work, including employers forcing more than 28 hours; ISA uses employment notifications to catch multiple jobs. From July 2026, A1 Japanese must be proven by a test certificate or school interview, not 150 study hours. From April 2027, a new "confirmation of ability to pay" form for language-school entrants.
4. Language schools on the MOJ notified list must get MEXT certification by 31 March 2029.
5. Bangladesh Bank (Sept 2026) allows remittance for any language course, paid to the institution, one year at a time, from one branch with a student file.

### Conflicts between sources

- Visit visa documents: the embassy's archived list asks for a two-way air booking and hotel booking; VFS's checklist says reservations and payments are not required. Left as Need to know.
- Photo size: the embassy's student list says 2 x 2 inch white background; VFS says 2 x 1.4 inch. Used VFS (current channel) in the visit section; embassy list cited for language-school list as given.
- Student visa documents at VFS: VFS's long-term checklist lists only 5 items for COE holders; the embassy's archived list for language-school students has 14 items (sponsor bank statements, 3 years of tax papers, textbook). Need to know.
- Processing: embassy says minimum 7 working days; VFS says usually 5 working days; MOFA says about one week. Doc gives the embassy's figure and VFS's.
- VFS service charge: BDT 2,090 on short-term sections vs BDT 1,900 on study/work/transit sections of the same page. Doc gives both.
- Job-hunting visa part-time work: university pages say part-time work is generally not allowed; ISA's own page says comprehensive permission up to 28 hours/week is available. Used ISA.
- Transit: end of transit visas comes from VisaVerge (lead) citing San Francisco, Seattle, Houston and Montreal consulates; the SF consulate PDF (sf.us.emb-japan.go.jp/files/101048791.pdf) returned 403 and has no Wayback capture. The Dhaka embassy's archived list still has a transit section.

### What happens in practice

- Embassy notes heavy student-application seasons (mid-March to early June, mid-Sept to late Oct) with appointment waits of over a month.
- Bangladesh Embassy Tokyo openly says most language-school students come to work; the ambassador has lobbied schools to take more Bangladeshis (July 2025) and cites 25,000 students (Apr 2026). The embassy community page says 40,045 Bangladeshis in Japan in June 2025.
- No Japan-specific report found of Dhaka agents selling "study and earn" packages, of fake Japanese guarantors, or of Bangladeshi students prosecuted for overwork. These remain Need to know questions.

### Facts logged but not used, and why

- V0005 (VFS fee "will be charged"): superseded by the specific BDT figures.
- V0029, V0030: university and short-training document lists; not in my scope beyond the language-school route.
- V0047, V0058, V0135: residence rule; V0058 and V0135 used, V0047 duplicate.
- V0103 (COE return envelope): school files the COE, not the student.
- V0119 (schools tracing missing students): kept for the Background/scams lead if wanted.
- V0142 (40,045 Bangladeshis): corridor-number material for Background.
- V0159 (embassy and Bangladesh Bank simplified tuition payment): covered by the circular facts.
- V0168 (approved-agency handling fee): VFS figures used instead.
- V0109/V0110 both used; V0026 used.

### Pages we could not download

- https://www.bd.emb-japan.go.jp/en/visa/visareqdoc.html and visainfohowto.html: 403; Wayback copies were from 2022 and 2018, too old, deleted.
- https://www.bd.emb-japan.go.jp/itpr_en/ISA.pdf (embassy notice on Japanese tests accepted for Student status): 403, no Wayback capture.
- https://visa.vfsglobal.com/bgd/en/jpn and its fees page: 403 / JavaScript-only (the vfsglobal.com one-pager was used instead).
- https://www.sf.us.emb-japan.go.jp/files/101048791.pdf (SF consulate notice ending transit visas): 403, no capture.
- https://www.jagonews24.com/en/national/news/91920 and /en/biz-econ/news/83304: 403.
- ISA PDFs 001363332 (annex country list for Student status), 001461504 (application notes), 001463590 (Class I school list): text layer garbled with the default pdftotext; 001461177 and 001463592 were re-extracted with `pdftotext -enc UTF-8`, which works, so these can be redone the same way.
- Firecrawl credits ran out after the first scrape (reset 19 Nov 2026 18:10 UTC).

### Tooling note

fetch.py's PDF text copies of Japanese PDFs come out empty; `pdftotext -enc UTF-8 -layout file.pdf file.txt` fixes it. Two-column PDFs (JASSO guide) interleave columns, so quotes must stay within one line.

## Skilled visas, family, PR, changing visa type, asylum, children (prefix P)

### What was searched

- ISA (moj.go.jp/isa) status pages: Engineer/Specialist (gijinkoku), HSP, J-Skip, Dependent, Spouse of Japanese National, SSW, TITP, Student, Temporary Visitor, job-hunting Designated Activities; the procedure pages for COE, change of status, PR and acquisition of status; PR guidelines (revised 24 Feb 2026); fee pages (new fees from 1 Oct 2026, reduced fees, online fees); e-COE page; refugee procedure page; the 2023 amendment page; 2024 and 2025 refugee statistics press releases; the 2018 asylum work-restriction notices (English leaflets).
- e-Gov API: full text of the Immigration Control Act (326CO0000000319) and the landing-criteria ordinance (402M50000010016), saved as plain text (`egov-immigration-act`, `egov-landing-ordinance`, logged with `fetch.py --log ... manual`).
- MOJ: naturalisation Q&A; Minister's press conference of 27 Mar 2026 (naturalisation tightened from 1 Apr 2026).
- IPA mutual recognition page (Bangladesh ITEE, 1 Sep 2014; AP/FE/IP); JICA 2023 B-JET article; bjet.org; Bdjobs B-JET 16th batch ad.
- Bangladesh Embassy Tokyo: birth registration, newborn FAQ, e-passport fees, contact, labour wing, emails.
- Shinjuku City birth notification page; ISA "Guidebook on Living and Working" chapter 1 PDF.
- News/NGO: Daily Star/Reuters 2017 (Fukushima asylum-seeker brokers), LA Times 2023, JAR comments (2024 statistics; Sept 2026 PR guideline draft), UNB 2025 (JICA scam warning), TBS 2019 (RAB fine, Japan job fraud).
- Searches in Japanese and Bangla for: Bangladeshi asylum numbers, asylum brokers, sham marriage cases involving Bangladeshis, gijinkoku dispatch misuse, fake COE scams. Firecrawl credits ran out mid-session; WebSearch used thereafter.

### Conflicts

- Baby passport fee: embassy newborn FAQ (updated 9 Jul 2026) says 18,000 yen (P0224); embassy e-passport page (updated 12 Nov 2026) lists 17,000 yen for 48 pages/5 years and 21,000 yen/10 years (P0229). Both marked conflict; doc uses the newer page and asks a Need to know.
- Refugee processing time: ISA standard 6 months (P0291) vs JAR's reported average of about 2 years 11 months (P0197). Both in doc, attributed by citation.
- Page dates: ISA HTML pages carry no visible date; the HTTP Last-Modified on all of them is 27 Oct 2026 (site-wide republish). Pages whose content reflects the 1 Oct 2026 fee change were dated 2026-10-27 on that basis. If the lead prefers stricter dating, these could be set to undated/possibly-outdated.

### What happens in practice

- Asylum: Bangladesh is a top-5 applicant nationality (2025) and top-5 for appeals (2024), but ISA's nationality tables are image-text PDFs whose Japanese did not extract, so the Bangladeshi counts are a Need to know. ISA itself publishes "applying does not mean you can work" notices in Bengali, implying Bangladeshi misuse is on its radar.
- Brokers: the 2017 Fukushima case is the only documented Bangladeshi asylum-broker case found. ISA's 2018 data: refused claims were mostly debt or neighbour disputes; ~80% of TITP-status and ~68% of student-status applicants applied after leaving their training/school.
- Gijinkoku misuse via dispatch firms (engineers placed in factory work) is reported in Japanese news (Sakigake, Aug 2025) but the saved page returned "article not found"; ISA's 13 Jul 2026 dispatch rules confirm the issue indirectly.
- PR: a stricter PR guideline draft (higher income, national-interest test, job-hunting and asylum time not counted) was in public comment to 3 Sep 2026; adoption not confirmed.

### Facts logged but not used, and why

- P0011 (Japan certificates under 3 months old), P0030 (TB screening, not Bangladesh), P0069-P0071, P0073 (fee-reduction detail beyond what's needed), P0097, P0099, P0102 partly, P0141, P0176, P0179, P0190, P0194-P0196 (older news; official sources used instead), P0198, P0200, P0211, P0271, P0273, P0275, P0296 and some duplicates: background or duplicative of cited facts.
- P0045 holds the old-PR-fee claim; the 200,000 yen PR fee row was dropped by a concurrent write and re-logged as P0074. P0165 holds the 2025 review-request claim; the 11.6% repeat-applicant fact was re-logged as P0279.

### Sources deleted or restored

- Deleted (garbled Japanese text layers, empty, or not used): isa-gijinkoku-criteria, isa-gijinkoku-clarify-full, isa-it-hsp-pdf, isa-hsp-japanese-list, isa-hsp-leaflet-en (duplicate of points table), isa-refugee-2025 PDF, isa-refugee-2025-pdf2, isa-refugee-2024 PDF, isa-2023-amend-operation, isa-amend-pdf-2025, isa-amend-pdf-b, isa-001464639 (Bangladesh COI translation, garbled), isa-refugee-review-2018-pdf and -sep, isa-2026-07-pdf, isa-gijinkoku-dispatch-pdf, sakigake article, ssw-portal-about, egov public-comment page, isa-refugee-proc2, isa-2023-bill, ds-hunger-strike, isa-hsp-faq, isa-pr-docs-work, isa-pr-hsp, isa-hsp-stats, isa-hsp-procedure, isa-designated, isa-it-hsp. Their rows were removed from `sources/_fetchlog.csv`.
- isa-student-status and isa-titp-status were deleted by mistake and immediately re-fetched (same URL, same day); other agents cite them.
- Personal data: migrants' names redacted in saved copies of ds-fukushima-asylum and jica-bjet-2023.

### Pages we could not download

- https://www.mofa.go.jp/j_info/visit/visa/long/visa1.html (403)
- https://www.bd.emb-japan.go.jp/itpr_en/visa_working.html (403)
- https://www.scmp.com/week-asia/people/article/3349313/japans-deportation-drive-strikes-fear-asylum-seekers-foreign-residents (403)
- https://www.moj.go.jp/isa/content/001459863.pdf (2025 refugee annex tables; downloads but the Japanese text layer is empty; needs a human read for Bangladesh rows)
- https://www.moj.go.jp/isa/content/001466474.pdf (17 Jul 2026 TITP-to-refugee-applicant rule; text layer empty)
- https://www.moj.go.jp/isa/content/001460430.pdf (integrated gijinkoku clarification, incl. simple-labour examples; text garbled)

### Open questions (also in the draft as Need to know)

- Bangladeshi refugee applicants/recognitions in 2024 and 2025.
- COE validity period (widely given as 3 months; no ISA page saved says so).
- VFS service fee for long-term visas; whether gijinkoku workers need BMET clearance.
- B-JET fee and next intake; ITEE dates and fee.
- Whether the Sept 2026 PR guideline draft was adopted.

## Money, going home, coming home, contacts (prefix B)

Facts: B0001-B0280 (267 official or archived, 13 news/third-party). Draft: drafts/B-bangladesh-side.md.

### What was searched

- Bangladesh Embassy Tokyo (tokyo.mofa.gov.bd): Travel Permit, Labour Welfare Wing, phone/email/address/contact pages, consular fees, e-passport, community page, Dead Body Repatriation page (still "Under Construction").
- ISA (moj.go.jp/isa): information centre, deportation index, deportation/departure-order Q&A, surrender, departure order, execution/self-paid departure, detention and visits, supervision measures, overstayer statistics (1 July 2025).
- e-Gov law API: Banking Act arts. 4 and 61 (unlicensed banking: 3 years / 3 million yen); Immigration Control Act arts. 70 and 73-2 (overstay; facilitating illegal work).
- FSA: register of funds transfer providers (PDF, 31 Oct 2026, 86 providers), "How to open a bank account and send money" guide (English, Sept 2024), living-in-Japan page.
- Police: Osaka and Kanagawa prefectural police pages on account selling (penalties raised 10 July 2026); Akita Sakigake news (NPA: accounts sold for avg 35,000 yen in 2024).
- Japan Pension Service: lump-sum page and the English claim form/notes (Sept 2026) with amounts, tax, currencies, mailing address.
- Hello Work basic allowance page (employment insurance).
- Japan Embassy Dhaka (blocks curl, 403): visa page saved by another agent (emb-dhaka-visa); contact and office hours via Wayback (2025 captures of pages dated 2020/2021).
- JICA Bangladesh office page; BOESL office address page and Japan caregiver TI notice; IM Japan FAQ; BSS (JETRO ~350 Japanese firms in Bangladesh).
- Repatriation of remains: Osaka Prefecture one-stop desk monthly report (Feb 2026: family pays full cost; consulate certification needed); Ask Explorer guide (cremation ~500,000 yen, embalming ~1.5 million yen, three company names). Bangla news search found only cases of burial in Japan, no cost figures.
- Bangladesh side copied from countries/qatar/sources (WEWB pages, JBC leaflet, BMET/Ministry/PKB charters, NRCTA circular, WEDB, upension, baggage rules, customs, budget speech, BRAC) and countries/cambodia (bKash page with Japan row) and countries/italy (BB monthly remittance report Aug 2026). Facts re-quoted under prefix B (reused quotes from Qatar; Bangla-PDF transcriptions marked no-quote-check as in Qatar).
- Remittance by year: Japan column of Annex-III of BB's Aug 2026 monthly report transcribed with PyMuPDF word positions into `bb-remittance-monthly-report-2026-08-italy.japan-transcription.md` (checked against BB monthly table: FY2021-22 = 69.29).

### Conflicts

- Travel Permit documents: English list (birth + nationality certificates attested by MOFA Dhaka, 4 photos, form, old passport copy) vs Bangla list (form, passport copy, ticket copy, 3 photos, fee receipt; police report for handwritten passports). Processing: English says 3 working days regular / same day urgent; Bangla says 3-5 working days. Both in doc as Need to know / both cited.
- Embassy emergency hotline: Phone Numbers page (June 2026) 090-3558-1968 vs Contact page (Dec 2025) 080-7004-1971, 070-1260-1984, 080-4065-6601. Need to know.
- Labour wing contacts: Emails page (June 2026) First Secretary (Labor) fslabor@mofa.gov.bd; Contact page (Dec 2025) Counsellor zakir2kbd@gmail.com, ext. 201. Both given.
- WEWB treatment aid: WEWB page Tk 2 lakh vs Embassy labour wing page Tk 1.5 lakh (B0015). Need to know.
- Customs currency: BB circular USD 10,000 vs Bangladesh Customs page USD 5,000 (inherited from Qatar). Need to know.
- bKash lists Queen Bee and MoneyGram for Japan; neither name is on the FSA register (they may operate through a registered partner). Need to know.

### Overlap with Agent E (E-life-rights.md)

E has "The lump-sum pension refund (dattai ichijikin)", "Selling or lending your bank account or phone" and "Bans on coming back". My brief asked for the lump-sum steps in Coming home, so I wrote a full step-by-step ("The lump-sum pension refund"); the lead should keep one and link the other. My version adds: US-dollar payment for Bangladesh, Japan Post Bank not accepted, JPS Foreign Business Group phone (+81-3-6700-1165, Japanese only), keep Basic Pension Number, incomplete claims returned, relatives can receive only if claim was filed before death, National Pension 6-11 months = 53,760 yen. Account selling and bans: I gave short versions and cross-referenced E's headings. Unemployment/job-change: I link to E's "If your job ends: the 14-day report and the 3-month rule" and "Technical intern trainees: changing training site"; injury: E's "If you are injured at work"; unpaid wages: "If you aren't paid".

### What happens in practice

- Repatriation of a body from Japan is paid entirely by the family unless an employer/insurer pays (Osaka desk). Bangla news cases (Daily Star Bangla) show Bangladeshis who died in Japan buried there. WEWB/Ministry say they bring bodies home free (incl. undocumented), but no Japan-specific evidence of who pays the airfare.
- Departure order takes about 2 weeks from surrender to leaving; airport surrender doesn't allow same-day departure.
- ISA information centre has no Bengali; OTIT native-language hotline has no Bengali line (English Tue/Thu/Sat).
- IM Japan runs a Bangladesh mental-health programme "Vai-bon" (B0262, not used: belongs to TITP section if wanted).

### Facts logged but not used

- B0009, B0025 (Bangladeshi population in Japan 40,045 June 2025; ~2,500 TIs): Background material for the lead / Agent R.
- B0140 (IC-chip ID check for account opening from 1 Apr 2027): belongs in a bank-account section.
- B0142 (old penalty 1 yr/1m yen): history only.
- B0182, B0193, B0208, B0224, B0235, B0258: duplicates or detail not needed (call-centre name, extra disability rows, old charter desk numbers, 7-day customs declaration conflict, family legal help, BOESL PABX).
- B0262 (IM Japan Vai-bon): TITP section.

### Pages we could not download

- https://www.bd.emb-japan.go.jp/itpr_en/index.html (403; used Wayback for contact.html and 00_000821.html, dated 2020/2021 pages captured 2025).
- https://www.boesl.gov.bd/ (connection failed with www; boesl.gov.bd pages without www worked).
- https://remittanceprices.worldbank.org/corridor/Japan/Bangladesh (403; Firecrawl out of credits). World Bank may not cover JP-BD anyway.
- https://www.bb.org.bd/en/index.php/econdata/wageremitance (bot challenge). Note: the copy `bb-wage-remittance.md` in countries/qatar/sources is a CAPTCHA page; I copied it, found it, and deleted it from japan (files and rows).
- https://www.japantimes.co.jp/news/2017/12/06/business/corporate-business/paperwork-embalming-tokyo-mortuary-firm-handles-cross-border-death-care/ (403).
- bKash remittance page (Firecrawl out of credits; used Cambodia's 10 Nov 2026 Firecrawl copy, which keeps the full country table).
- https://www.nenkin.go.jp/international/japanese-system/withdrawalpayment/payment.files/A.pdf (404; the same form at /international/english/japanese-system/benefit/payment.files/A.pdf worked).

### File incidents

- `egov-immigration-act`: another agent fetched it the same minute; my `--log manual` overwrote its `.md`. I moved my extract to `egov-immigration-act-art70.md`, restored `egov-immigration-act.md` as a copy of its `.txt` (same text), and removed my duplicate fetchlog row. The other agent's facts quote the .txt/.md text, which is unchanged in content. Lead: please check E/other facts citing egov-immigration-act still pass.
- `fsa-funds-transfer-list.txt` was replaced with a `pdftotext -enc UTF-8` extraction (fetch.py's default lost the Japanese).

### Open questions (also in the draft as Need to know)

- Hundi among Bangladeshis in Japan: who runs it, where, any arrests? (No Japan case found in English, Japanese or Bangla searches; Japanese arrests found were Chinese/Vietnamese networks.)
- Remittance cost JP-BD per provider; Japan partners for Nagad; whether WEDB is sold in Japan.
- Bangladeshi overstayer count (ISA table PDF garbled; Bangladesh not in top 10 on 1 Jan 2025).
- Embassy NOC papers/fee for a body; airfare cost Tokyo-Dhaka for remains; who pays for TITP/SSW deaths; Muslim burial in Japan.
- Does WEWB membership taken in Japan bring JBC insurance?
- Japan-returnee reintegration schemes; any business start-up grant for returned interns.
