# Brunei: research notes

Research notes behind `doc.md`, one section per research topic (fact prefix in brackets); KA to KD are the fact-check pass and KG the final audit.

## How the doc was put together

- Four topics researched in parallel (a smaller corridor), merged on the Singapore model, split into four parts and checked sentence by sentence by independent verifiers (about 140 fixes: about 20 allegations attributed and dated, three unconvicted people's names removed, the harbouring penalty, remittance rankings, and BOESL's own 29 September 2026 circular found and transcribed, which settled the wage as BND 20-22 a day and confirmed its charges), then audited.
- Exchange rate: the Brunei dollar is at par with the Singapore dollar (BDCB's monetary policy page); with Bangladesh Bank's SGD cross rate of 19 October 2026, BND 1 is about Tk 97. A Bangla Tribune report converted BND at the US dollar rate (about Tk 123); no figure from that conversion is used.
- Brunei publishes little officially, and its labour department site (now the Department of Manpower and Employment), the Employment Order gazette and BOESL's website would not download; Firecrawl's credits ran out during the research. Several rules rest on older or unofficial pages and are flagged as Need to know (for example the BND 1,500 family-pass threshold, from a 2005 page).
- Lead's metadata fixes: B0212 (emergency numbers, page dated 13 April 2026) set to verified; the 2005 source behind the family-pass threshold dated 2005 in sources.csv and its facts.
- Personal data: saved news articles may name migrants who appear in published reports; the doc names only the convicted trafficker.

## Background and corridor (insider pass) (prefix C)

Facts C0001 to C0210 in facts.csv (C0157 duplicates C0156; cite C0156). 164 ids cited in drafts/C-background.md, all checked present in facts.csv on 2026-11-19.

### What was searched

- Firecrawl search: out of credits from the start of this run (daily allowance), so all searching was done with WebSearch and all saving with fetch.py / wayback.py.
- English: Brunei Bangladeshi visa trading, suspension/freeze/moratorium 2026, stranded/jobless/unpaid, Borneo Bulletin crackdowns, overstay and whipping, transfer of employer / release letter, exit fine, minimum wage, salaries in BND, deaths and bodies, women/domestic workers, trafficking convictions 2025, remittance by country.
- Bangla: ব্রুনাইয়ে বাংলাদেশি শ্রমিক ভিসা; ব্রুনাই ভিসা বাণিজ্য; ব্রুনাই শ্রমবাজার ২০২৬ বোয়েসেল; ব্রুনাই প্রবাসী মৃত্যু লাশ; ব্রুনাই ফ্রি ভিসা দালাল প্রতারণা; ব্রুনাই যেতে খরচ; ব্রুনাই অভিবাসন ব্যয় নির্ধারণ; ব্রুনাই প্রবাসী বেতন; ব্রুনাই পাঠানোর নামে প্রতারণা গ্রেপ্তার.
- Official: BMET annual table image (Brunei column transcribed by hand from the 2025-05 image, cropped and enlarged), OEP clearance reports 2023-2026 (copied from countries/singapore/sources), BusinessBN (MOFE) Foreign Worker Licence page, INRD enforcement and work-pass slides (Thai MFA-hosted, fetched by another agent), Bangladesh High Commission BSB checklists and BOESL-BEA MoC (fetched by another agent), DEPS Labour Force Survey 2025, Bangladesh Bank remittance publication August 2026.

### Status on 19 November 2026 (answer to "is there a suspension?")

- No current Brunei suspension of Bangladeshi workers found. Brunei instead restricted the channel: from 1 Feb 2024 Bangladeshis only through BOESL (Labour Department announcement relayed by the High Commission's labour secretary), plus High Commission attestation of every demand letter and visa with detailed employer vetting (Oct 2026 checklist: wage receipts of existing Bangladeshi workers, staff house, projects).
- In 2019-2020 Brunei "wanted to stop recruitment of workers from Bangladesh" over visa trading but did not after the High Commission asked (FE, Jan 2020, C0191). ANN (Oct 2025) lists Brunei among markets that "closed their doors at various times" (C0087, logged, not cited because vague).
- Active 2026 signals: BOESL notice Oct 2026 (148 men, Unity Land Sdn Bhd); ministerial talks 29 July and 3 Nov 2026; OEP 1,726 clearances to 7 Nov 2026.
- The PM's 18 Nov 2026 statement about countries suspending recruitment because of syndicates does not name Brunei (C0199).

### Conflicts

1. BMET yearly table vs OEP clearance report: 2023 = 1,081 (table) vs 5,959 (OEP); 2024 = 205 vs 3,058. Draft uses the table for 2014-24 and OEP for 2025-26 (no table figures yet), with a Need to know. TBS (2024) quotes BMET: only 3,473 from Jan 2020 to Jan 2024 (C0027), which fits the table (530+12+1,850+1,081 = 3,473 exactly), not OEP. So the yearly table is probably the "real departures" series; the OEP report may count clearances that never travelled, or a different category. Worth a lead decision: possibly swap the 2023-24 list values to the table and mention OEP in the Need to know instead.
2. BMET cumulative: 75,435 (1992-Aug 2022, DS Bangla), 77,958 (1992-Jan 2024, TBS), 64,974 (2004-May 2025, table). Consistent if 1992-2003 adds ~11-13k.
3. Number of Bangladeshis in Brunei: 30,000 (2019, FE), 25,000 (2019 High Commission via Reuters; 2024 unofficial), 15,000 (High Commission 2021), 13,000 (FE 2021), 20,000 (mission 2022; FE 2024). Draft gives the range.
4. BOESL Unity Land wage: Bangla Tribune says "ঘণ্টাপ্রতি" (per hour) BND 20/22. Implausible (≈BND 4,000/month); likely per day. Need to know in draft. The BOESL notice itself (brms.boesl.gov.bd) was not saved; another agent may have it.
5. Name of Brunei's labour authority: Borneo Bulletin Sept and Nov 2026 use "Department of Manpower and Employment" (also "Department of Labour and Manpower") and "Employment Act, Chapter 278"; earlier sources say Labour Department and Employment Order 2009. Possibly a 2026 restructuring/merger with JobCentre Brunei and a re-numbered law. Need to know in draft.
6. "Exit fine BND 600" (TIP 2026, C0011) vs INRD slides: BND 600 is the compound sum for many Immigration Act/Regulation offences (s.58), including leaving other than at an authorised point (s.5(2)) and Reg 15 breaches. TIP frames it as employer approval needed to leave. Kept TIP wording, attributed via [N].
7. LPA timing: MOFE page says 7 working days / 18 for construction; a 2018 bizbrunei piece (not saved) said 7/14. Used MOFE.

### What happens in practice (from the reading)

- The "free visa" in Brunei = a visa from a paper company (often Bangladeshi-run with a Bruneian nominee partner) with no project; on arrival brokers take the passport and the man must "freelance" and pay the broker a monthly cut; when caught he is jailed/caned for working outside his pass or overstaying. Repeated in 2015, 2017, 2019, 2020, 2021 cases and in the Nov 2025 conviction of Mahedi Hasan.
- "Body contract" at Dhaka airport was the exit route for unattested visas (FE 2020, 2021; BIBD 2021).
- The 2022 High Commission SOP explicitly banned using existing Bangladeshi workers as brokers/visa traders (C0125) — i.e. the classic chain was worker-to-village.
- Deaths: undocumented workers' bodies stuck in RIPAS morgue over hospital bills; Ministry paid Tk 4.5 lakh to repatriate one (2024).

### Facts logged but not used, and why

- C0012 (TIP list of trafficking methods), C0015 ("runaway workers" term), C0017 (two convictions), C0018 (online complaint mechanism; another agent likely covers complaint routes), C0019 (MOUs with two governments), C0024 (Jan 2024 briefing), C0035 (Unity Land post breakdown; the visa researcher may want it), C0045 (excess charges, over-recruitment 2022), C0058 (HC cancelled attestation), C0061 (30,000 in 2019), C0069/C0148 partly used, C0070-C0073 (2024 raids; replaced by 2026 cases), C0075/C0076 (s.39(1) and hotline; for the If you aren't paid section), C0079 (25 hired by Sept 2024: used only in a Need to know wording without citation; could be cited there), C0082 (150,000 foreign workers, conflicts with LFS 64,100), C0083, C0087, C0103-C0107 partly, C0110, C0114-C0116 partly, C0119 (BND 15 attestation fee, belongs in steps), C0126, C0129 (INRD hotline, for contacts), C0134, C0138, C0141, C0149-C0152 (LPA renewal and training sessions), C0157 (duplicate), C0159/C0165/C0170/C0171 (penalty duplicates), C0162, C0169, C0175 (DME phone 2381848 / 7298989 — for contacts), C0177, C0178, C0180 (nlms.gov.bn complaint portal — for If you aren't paid), C0184, C0189 partly, C0194 used, C0196 (mandatory labour-rights brief on signing).

### Links for the lead

- The draft refers to "Sending money home" and "What ties you to the employer". Two spots that should link to the visa steps (High Commission attestation checklist; BOESL interview process) had their bare references removed; the lead should add exact step links once the visa section exists.

### Pages we could not download

- https://borneobulletin.com.bn/still-many-glaring-labour-law-violations (403 live; Wayback capture download failed) — 2022 High Commissioner speech on labour violations.
- https://borneobulletin.com.bn/application-process-for-new-renewal-of-foreign-worker-licence-updated (403; not tried on Wayback).
- https://www.risingbd.com/amp/news/327186 "ব্রুনাই প্রবাসীদের আহাজারি" (403).
- https://www.jugantor.com/exile/1101639 (403).
- Bangladesh Bank's Annex III country-wise yearly remittance (FY2016-17 to FY2026-27) in bb-remittance-pub-2026-08.pdf: table text is garbled in both layout and raw extraction; only the Table 4 Brunei row (Jul-Aug 2026) was recoverable (saved as bb-remittance-pub-2026-08.raw.txt). Yearly Brunei totals for 2024-25 and 2025-26 need reading from the PDF by eye.
- OEP country-clearance JSON for 2026 to 18 Nov and for 2020-2022: live fetch with a session cookie was refused by the sandbox; used the 8 Nov copies from countries/singapore.

### Personal data

No private migrant documents saved. News articles name some workers (as published); none of their names are used in the draft except Shipon Howlader (deceased, named in national press, needed for the body-repatriation case) — the lead may prefer to anonymise.

## Work visa: foreign worker, rights and life (prefix R)

Researcher prefix R. Draft: `drafts/R-work-visa.md`. Facts R0001-R0238 in `facts.csv`.

### What was searched

- Brunei official: business.mofe.gov.bn (Employing workers page), immigration.gov.bn (Pas Kerja page, enforcement page, news), moh.gov.bn (Foreign Worker Health Screening, approved overseas facilities list), labour.gov.bn (blocked, see below).
- Brunei government slide decks presented to Thai workers and hosted on image.mfa.go.th (folder 670218 = 18 Feb 2567 BE = 18 Feb 2024): Department of Labour "Guidelines on employees' rights under Employment Order 2009", Immigration "Enforcement Section" and "Work Pass Section". These are the best official statements of the Employment Order and Immigration Act penalties found; dated 2024-02-18, so possibly-outdated.
- Bangladesh High Commission, Bandar Seri Begawan (bandarseribegawan.mofa.gov.bd): BOESL-BEA MoC, process flow and sample demand letter (PDF, updated 26 Jan 2024); demand letter checklist (Oct 2026); BOESL visa attestation checklist (2026 revised); Labour Wing visa attestation checklist (B$15 fee); guidelines for workers (Bangla image); counselling and dispute settlement; immigration visit; jail visit statistics; interpreter services; blacklisted companies; officers list.
- BOESL BRMS portal (brms.boesl.gov.bd).
- News: The Business Standard, Bangladesh Monitor, Bangla Tribune (Aug and Oct 2026 BOESL Brunei circulars), Financial Express (2020, 2021, 2022, 2024), The Star / Borneo Bulletin (2025-2026 overstay, labour raids, wage cases, trafficking conviction, minimum wage phase 2), US TIP Report 2026.
- Bangla searches: ব্রুনাই ভিসা প্রতারণা, ব্রুনাই বোয়েসেল মেডিক্যাল টেস্ট ভিসা ফি.
- Bangladesh-side steps copied from `countries/singapore/sources` (BMET charter 2026, safe migration leaflet, welfare-fee circular, WEWB membership and Tk 3 lakh grant, JBC insurance leaflet, PKB pages and charter, Ministry charter, OEM Act 2013, OEP guide, DEMO Sylhet notice, e-passport, PCC pages, Bangladesh Bank 2019 survey with the 2017 country cost ceilings) and re-quoted as R0001-R0062, R0236-R0237, R0214-R0215.

### Key findings

1. Since 1 Feb 2024 the only legal route from Bangladesh is BOESL (G2G under the 16 Oct 2022 MoU); private BD agencies are out. Brunei side: only Department of Labour-licensed Brunei Employment Agencies (BEAs) that sign a MoC with BOESL.
2. The MoC puts nearly all costs on the employer (LPA, agency fee, visa, pass, attestation, Brunei medical, insurance, round-trip ticket, food, housing, repatriation). Worker pays BOESL Tk 56,350 (skilled) / Tk 44,850 (semi/unskilled) plus Brunei visa fee and Dhaka medical (Oct 2026 circular via Bangla Tribune). Ministry 2017 ceiling for Brunei: Tk 1,20,780.
3. Brunei MOH approves only three Dhaka medical centres for Brunei (Fairways, International Health Centre, Modern Diagnostic Centre Unit 3). The validity dates printed next to the Bangladesh entries are old (2014-2020), though the list is "updated 22 June 2026".
4. Overstay over 90 days = 3 months to 2 years' jail plus at least 3 strokes (Immigration Act s15). Courts are caning Bangladeshis for overstay throughout 2026.
5. No minimum wage for construction/most Bangladeshi jobs; BOESL circulars pay BND 20-21 a day or BND 600-1,000 a month.
6. The High Commission publishes a blacklist of 29 Brunei companies (Oct 2026), and checks staff houses, wage receipts and worker lists before attesting demand letters and visas.

### Conflicts between sources

- **LPA processing time:** BusinessBN portal says 7 working days (18 for construction) [R0066]; the 2024 BHC process flow says 14-28 working days depending on security vetting [R0085]. Used the process-flow figure in the doc (it is specific to the BOESL route).
- **Visa processing:** BusinessBN 3-5 working days [R0068]; process flow 5 working days [R0087]. Used 5.
- **October 2026 Unity Land wage unit:** Bangla Tribune says ঘণ্টাপ্রতি (per hour) BND 20/22, but its taka equivalent and the August 2026 BOESL circular (দৈনিক, per day BND 20-21) suggest per day. R0175 logged with a note; left as Need to know in the doc and not cited.
- **Start date of the BOESL-only route:** Bangladesh Monitor (Jan 2024) says 1 Feb 2024; TBS (Apr 2024) quotes BOESL saying the process began 1 March 2024. Doc uses 1 Feb 2024 (the Department of Labour announcement) and cites TBS for the March start of BOESL's processing cost.
- **Exit:** TIP 2026 says workers need employer approval to leave or pay a BND 600 exit fine [R0162]. The Immigration slides show overstay can be compounded for up to BND 600 [R0139]. These may be the same mechanism (compounding an overstay/pass offence at departure). Need to know left in the doc.
- **Deposit:** only figure found is a 2022 minister's statement (US$1,600 for Bangladeshis vs US$500 for Malaysians). No official schedule.
- **PCC fee (Bangladesh):** R0017 and R0021 carried over as "conflict" from Singapore (Tk 1,500 portal vs Tk 500 police guidance). Not used in the Brunei draft because no Brunei source asks for a PCC.
- **Name of the labour body:** 2026 Borneo Bulletin pieces call it the "Department of Manpower and Employment" or "Department of Labour and Manpower" and the law the "Employment Act, Chapter 278"; the Nov 2026 piece still says "Employment Order, 2009". Doc keeps "Department of Labour" and notes the new name once.

### What happens in practice

- Pre-2024 "free visa" / company-visa trade: BND 5,000 a visa, ~22,000 visas in H2 2019 vs 3,300 attested by the mission; airport "body contact"; workers paid Tk 3.8-5 lakh and found no jobs (FE 2020, 2021; TBS/Reuters 2019).
- Ringleader Mahedi Hasan (named Mahedi Hassan Bijon in FE 2020) was deported earlier and in 2025 jailed 5 years, fined BND 50,000 and caned 6 strokes in Brunei for 2018-19 trafficking (Star/Borneo Bulletin 2025-11-06). Possibly the same person; not asserted in the doc.
- Labour raids in 2026 routinely find unpaid overtime, unlawful deductions, no rest days, no written contracts, workers doing jobs outside their licensed occupation. Usual outcome is a compound fine of up to BND 1,000 per offence; one 2025 court case fined owners BND 1,200 each and the workers were still owed BND 1,000 each.
- Passport retention by employers/agents is widespread (TIP 2026; FE 2021). No Brunei statute found that makes it an offence.
- The High Commission's jail statistics: 19 Bangladeshis detained in prison in 2025, 30 in 2026 to 22 October.
- 2024 remittance fraud: 116 workers lost BND 0.72 million via a Western Union sub-agent (Remittance @ Seconds).

### Facts logged but not used, and why

- R0014 (e-passport fees at missions), R0017-R0022 (police clearance): no Brunei source requires a PCC; kept for the lead in case the corridor researcher finds that BOESL asks for one.
- R0031 (individual-visa clearance), R0035 (BMET GRS chain), R0053 (PKB grievance), R0045 (women's loan), R0048 (re-entry loan): general Bangladesh-side detail; the lead may place them in Contacts or a returning-worker section.
- R0039 (disability percentages), R0059 (airport desk statistics), R0062 (notices list check): background.
- R0066, R0068, R0069: superseded by the BOESL process-flow figures (see Conflicts).
- R0104 (checklist signed by First Secretary Labour): supports the officer's name only.
- R0126 (maternity leave): the Brunei BOESL route is men-only in 2026; useful if women's jobs open.
- R0137 (list of laws the Department of Labour enforces), R0143 and R0148 (penalties on employers of illegal workers): employer-side; could go in Background.
- R0164, R0187, R0193, R0195: partly used in Scams; R0195 (HC quote) is colour only.
- R0167 (online complaint mechanism, TIP): duplicated by the more specific R0212 (nlms.gov.bn).
- R0175, R0177, R0178: wage-unit uncertainty and duplicates of R0218.
- R0197 (bodies left in the RIPAS morgue, 2022): belongs in the death/repatriation section (another researcher).

### Pages we could not download

- https://www.labour.gov.bn/ and http://www.labour.gov.bn/Download/BORANG%20LPA_LD.pdf (connection refused / 401). Wayback only had a 2013 copy (deleted). Firecrawl was out of credits for the whole run.
- https://www.agc.gov.bn/AGC%20Images/LAWS/Gazette_PDF/2009/EN/s037.pdf (Employment Order 2009 gazette; 404). The Employment Act Chapter 278 and Immigration Act Chapter 17 texts were not obtained; the doc relies on the government slide decks.
- https://www.boesl.gov.bd/ (connection failed); BOESL's own Brunei circulars could not be fetched, so costs rest on Bangla Tribune.
- https://www.jugantor.com/job-seek/1163478 (403; BOESL Unity Land circular).
- https://www.prothomalo.com/bangladesh/ব্রুনেইয়ে-কর্মী-পাঠানো-হঠাৎ-কমে-গেছে (404).
- https://www.businessinsiderbd.com/economy/news/7877/bangladeshi-migrants-exploitation-abuse-in-brunei (522).
- https://asean.org/brunei-darussalam-policy-repository-on-migrant-workers-legislation-and-practices-of-asean-member-states (307 redirect).
- https://www.moh.gov.bn/SitePages/Foreign%20Workers%20Health%20Screening%20Programme.aspx (403; the new moh.gov.bn page was saved instead).

### Housekeeping

- Image sources saved with fetch.py came out as .html; renamed to .jpg/.png and transcribed into .md (bhc-demand-letter-checklist-img, bhc-visa-checklist-boesl-img, bhc-visa-checklist-labourwing-img, bhc-guidelines-workers-img); `_fetchlog.csv` rows updated. The guidelines image is Bangla; the transcription summarises each line in English and quotes one line in Bangla.
- Deleted unrelated BHC file pages I had fetched (birth registration, MRP, visa forms, document attestation) and a junk Business Post page; removed their log rows.
- No personal data about private migrants saved beyond names already published in court reports.

## Other visas, family, PR, asylum, children (prefix V)

Researcher prefix V. Facts V0001 to V0207 (103 verified, 76 possibly-outdated, 26 unofficial, 2 lead). Firecrawl was out of credits for the whole run (daily allowance exhausted), so blocked pages went to Wayback or were listed below.

### What was searched

- **Brunei Immigration (immigration.gov.bn).** The site is WordPress; the page list came from `/wp-json/wp/v2/pages` (with real modified dates, used as page dates) and news from `/wp-json/wp/v2/posts`. Saved: Visa Lawatan & Diplomatik, Pas Kerja, Permit Masuk, Long Term Pass, Kelahiran, Warganegara, the visit/business/professional/student document PDFs (Dec 2025), the PR guidelines PDF (effective 31 Dec 2024), the birth registration PDF (Mar 2026), the 2023 E-Arrival Card guide, and the 46th citizenship ceremony post (16 Nov 2026). Forms 8, 10, 25 and the visa form are scans without a text layer; Forms 8 and 25 were transcribed from rendered images (`jimn-form8-transcription.md`, `jimn-dependant-form25-transcription.md`).
- **Brunei MFA (mfa.gov.bn).** Visa category pages: Bangladesh ordinary passport = Category B (visa through a mission), diplomatic/official = D3 (14 days visa-free). Types of Visa page (transit visa list). BDGS scholarship page (2026/2027 round).
- **Brunei High Commission in Dhaka** (mfa.gov.bn/bangladesh-dhaka). Consular Services page is the single most useful source: visit, employment, business/professional, dependant/student visa checklists, Tk 2,100 fee, Tk 300,000 six-month balance rule, insurance rules, the VOA statement. The page is undated; Wayback captures show the Tk 300,000 rule, Tk 2,100 fee and VOA statement already present on 9 Nov 2025, and the "Brunei-based insurer" wording added between Nov 2025 and 13 Mar 2026. Page date set to 2026-03 on that basis.
- **Bangladesh High Commission, Bandar Seri Begawan** (bandarseribegawan.mofa.gov.bd): birth certificate requirements PDF (Bangla garbled; transcribed from the image), e-passport checklist (updated 15 Jul 2026), office hours page.
- **Universities:** UTB visa/student pass page and fee tables; UBD site was "under maintenance" on 19 Nov 2026, so UBD fees, ISU and FAQ pages came from Wayback.
- **UN:** OHCHR UPR compilation A/HRC/WG.6/47/BRN/2 (22 Aug 2024) via documents.un.org; SEAP joint UPR33 submission (2019) on the Nationality Act.
- **News:** Borneo Bulletin insurance policy (Wayback), The Star/Borneo Bulletin immigration prosecutions, The Vibes/Bernama on the E-Arrival Card (2023).
- Searches in Bangla ("ব্রুনাই ভিজিট ভিসা", "ব্রুনাই নারী গৃহকর্মী") found only work-visa fraud stories (Daily Star, Financial Express, already saved by other researchers) and nothing on women domestic workers to Brunei.

### Conflicts and judgement calls

- **VOA for students vs the High Commission.** UTB says students show Immigration's approval letter at Brunei airport to get a BND 20 single-entry visa (V0103); UBD's ISU lists "Visa on Arrival (VOA)" among its services (V0114). The High Commission in Dhaka says Bangladesh immigration does not accept a Brunei VOA and the visa must be endorsed before departure (V0006), and it has a separate student visa checklist (V0052, V0054). The draft tells Bangladeshis to get the visa in Dhaka and raises the airport question as a Need to know.
- **Dependant salary threshold.** The only figure found (BND 1,500 a month, professionals/technical/managerial with own accommodation) is from bruneiresources.com, undated (V0084, lead). ExpatFocus gives the same BND 1,500 but blocked download (403). No official figure found on immigration.gov.bn or MFA; Form 25 only asks for "arrangements for provision of security". Kept as a lead with a Need to know.
- **Dependant visa definition** says "whose husband is working in Brunei" (V0034): i.e. written for male workers. Whether a female worker can sponsor a husband is unknown.
- **Stay length on a visit visa.** The High Commission says the visa is "valid for up to three months" (validity of the visa, not length of stay). Third-party sites say 14, 30 or 90 days; none official. Left as Need to know.
- **E-Arrival Card timing.** The High Commission's wording is "prior to arrival ... within three (3) days upon arrival" (V0028): ambiguous. Drafted as "within the three days before you arrive".
- **Housekeeping course for Brunei.** The 2023 policy and the BMET charter (as cited in Qatar's doc) make it compulsory for women going to the Middle East and Hong Kong; Brunei is not named. Drafted the course rules and asked whether they apply to Brunei.
- **V0193** (Employment Order coverage) was logged with page-date "undated"; the source (labour-dept-eo2009-rights-slides, registered by another researcher) is dated 2024-02-18 in sources.csv. Status possibly-outdated is right either way.

### What happens in practice

- Overstayers are prosecuted under section 15(1) of the Immigration Act; Bangladeshis convicted 2024 to 2026 got 5 to 6 months' jail and 3 strokes of the cane (V0178, V0180, V0181). Immigration publishes "Operasi Kakas" raid notices almost weekly on its site (as images); working outside the endorsed job (Regulation 15(3)) is a common charge (V0177).
- The High Commission's Tk 300,000 rule explicitly targets "borrowed" balances: it rejects recent large deposits and same/next-day withdrawals even if repeated monthly (V0015). This reads as a response to the dalal practice of renting a bank balance for a visa file.
- Women domestic workers: BMET counts are tiny (152 in 21 years) but jumped to 50 in Jan to May 2025 (V0168). Nothing found on who sent them or through which channel.

### Facts logged but not used, and why

- V0031, V0033, V0073 (transit visa conditions): Bangladeshis are not eligible, so the conditions are irrelevant.
- V0070 (re-entry visa fees BND 20 to 50, from 2023 slides): belongs to the work-visa section; quote also only shows the label.
- V0078, V0082 (insurance Phase Two; local or international insurer): superseded for Dhaka applicants by the High Commission's Brunei-insurer rule.
- V0085 (spouses and children under 18 need dependant passes): duplicate of V0034.
- V0088, V0124, V0132, V0135, V0182: duplicates or not needed (Form 10 label; PR section role; born-in-Brunei naturalisation, not relevant to Bangladeshi children born to foreigners who are not PRs; child of Bruneian father).
- V0114 (UBD ISU handles VOA): used only in notes for the conflict.
- V0162 (birth certificate needed for passport etc.): general.
- V0196 (BMET female counts 2017-2019): V0168/V0169 suffice.

### Personal data

- `star-bd-immigration-offence-2026-01` and `star-visit-pass-work-detained-2026-09` named convicted Bangladeshi migrants; the names were replaced with "[name redacted]" in the saved .html, .md and .txt. Other researchers' saved Star articles (star-2026-04-bangladeshis-caned-overstay, star-employers-fined-2025) still contain names; not my files, flagged for the lead.

### Pages we could not download

- https://www.expatfocus.com/brunei/articles/how-to-apply-for-a-visa-in-brunei-5993 (403; no Wayback tried as bruneiresources gave the same figure)
- https://bruneipe.dfa.gov.ph/newsroom/advisories/540-overseas-employment-certificate-oec-for-overseas-filipino-workers-ofws (403, no Wayback capture): Philippine Embassy advisory said to give Brunei domestic worker minimum pay of US$400 / B$520 (Philippine requirement, not Brunei law)
- https://www.unhcr.org/my/media/states-parties-including-reservations-and-declarations-1951-refugee-convention (403)
- https://digitallibrary.un.org/record/4061200/files/A_HRC_WG.6_47_BRN_2-EN.pdf (202; same document saved from documents.un.org instead)
- https://webarchive.archive.unhcr.org/... UNHCR UPR submission 2013 (bot-check page; deleted)
- https://www.education.gov.in/.../Public_Notice_Brunei_Darussalam_Scholarship_2026_27.pdf (404) and https://www.education.go.ke/sites/default/files/2026-02/Brunei%20Final.pdf (timeout): other governments' BDGS notices
- ubd.edu.bn pages live (site under maintenance 19 Nov 2026); Wayback copies used
- https://www.mfa.gov.bn/Pages/directoryofmissionsabroad_Bangladesh.aspx (404)
- immigration.gov.bn "Panduan bagi pendaftaran E-Arrival Card" (2 May 2026) is images only; deleted, the 2023 PDF guide used instead

### Open questions (also in the draft as Need to know)

- Visit visa: days of stay granted; extension counter and fee inside Brunei; refusal reasons and re-application wait; whether a tourist with no sponsor is accepted.
- Dependant pass: current salary threshold, deposit, whether female workers can sponsor husbands, whether dependants can work.
- Visit-to-work switch inside Brunei.
- Domestic workers: whether BMET applies the housekeeping course and 25 to 45 rule to Brunei; whether BOESL handles domestic demands; salary floor in demand letters; insurance minimum for domestic work passes.
- Students: whether Dhaka airport lets students board on Immigration's approval letter alone; UBD current international tuition; next BDGS round and Bangladeshi numbers.
- Births: newborn registration at the Bangladesh High Commission (its PDF is written for adults who lack a digital birth certificate); how long a newborn may stay before getting a dependant pass.
- Long-term business/professional pass criteria.

## Money, going home, coming home, contacts (prefix B)

### What was searched
- Bangladesh High Commission site bandarseribegawan.mofa.gov.bd (all Labour & Welfare and consular pages). Many pages are empty shells (Address & Contact, Office Hour content, Dead Body Repatriation, Labour Compensation): the CMS shows only the title. Rendered in the browser to confirm: they really are empty. Attachments (TP rules PDF, TP form, complaint sheet, consular-tour notice) were downloaded from objectstorage and transcribed (TP rules PDF uses a legacy Bangla font; TP form has no text layer).
- BDCB: List of Licensees filtered to Money Remitters (17), Money Services licensing criteria, Alert List, Financial Consumer Complaints, Cap 174 Act PDF, cash-at-border page.
- Bangladesh Bank July 2026 monthly remittance report, Annex-III (country-wise FY2016-17 to 2026-27): Brunei column transcribed from the page image (text layer misaligned) into bb-remittance-monthly-report-2026-07-brunei-transcription.md.
- bKash partner list (copied from cambodia folder), Nagad partner list (rendered in browser; only page 1 of the table, which includes Brunei).
- INRD "Kesalahan di bawah Akta Imigresen Penggal 17" PDF (Dec 2025 upload) for overstay penalties; the azurewebsites URL returns 403, but the same file on www.immigration.gov.bn/wp-content/... downloads.
- Workmen's Compensation Act Cap 74, 1984 revised edition (AIPA copy, aipalync.org/document/view/1978 serves the PDF).
- Brunei MFA site for Brunei High Commission Dhaka; MOH Brunei footer for emergency numbers.
- News: FE 2024 (116 workers, Remittance @ Seconds), The Star Oct 2024 (BDCB order to Remittance@Seconds), TBS 2024 and Dhaka Tribune 2022 (body held 2.5 years), The Star April 2026 (two Bangladeshis jailed and caned).
- Searches for amnesty / pengampunan (English, Malay): only enforcement operations found. Searches for hundi in Brunei (Bangla and English) and for court cases under Cap 174: nothing Brunei-specific.
- Bangladesh-side facts (WEWB, JBC insurance, PKB, NRCTA, WEDB, Probash pension, baggage rules, airport desks, Ministry charter, BMET charter) were re-quoted from the Qatar folder's verified rows under prefix B (note column says "re-quoted from qatar Xnnnn"); sources copied with their fetchlog and sources.csv rows. Rows Qatar logged with --no-quote-check (Bangla transcriptions from page images) were re-logged the same way with Qatar's note appended.

### Conflicts and oddities
- Remittance @ Seconds: BDCB ordered it on 4 Oct 2024 to stop taking money from the public (B0187), yet it is still on BDCB's licensee list fetched 19 Nov 2026 (B0155). Left as a Need to know.
- bKash lists "KHRS Brunei"; BDCB lists "K & H Remittance Services" (Sengkurong). Almost certainly the same (K&H R S), but not stated anywhere; Need to know.
- Nagad spells its partner "MAGNAJAY MONEY REMITTANCE"; BDCB lists "Magnajaya Money Remittance".
- High Commission phone: official pages give 2342420 / fax 2342421 (officers list, consular-tour notice). Third-party directories give +673 2 238 420 and an address Simpang 83-20, Jalan Sungai Akar, BE3915 (or Lot 2469, Simpang 1028, Kg Tanah Jambu, Jalan Muara); no official page gives the address, so the address is a Need to know. WEWB's labour-wing list (Oct 2025) gives First Secretary +6732342460, fsbrunei@probashi.gov.bd; the HC officers list (Nov 2026) shows an Administrative Officer (Labour) and no First Secretary (Labour) on page 1 (11 entries, page 2 not read).
- Cap 74 amounts (BND 28,000 death cap, BND 36,000 total incapacity) are from the 1984 edition; may have been amended since. Old SSA profiles give different caps (BND 9,600 / 7,200). Flagged as Need to know.
- Jimn enforcement slides (2024, R's source) and INRD Dec 2025 offences list agree on overstay penalties; doc cites the 2025 INRD list.
- B0215 was logged with a weak quote (doesn't show the BND 600 compound); superseded by B0219. Do not cite B0215.
- moh-hotlines (B0212) was logged possibly-outdated but the page's dateModified is 2026-04-13, so it should be verified.
- TP form's address box says "Address in the United States" (copied template), B0142.

### What happens in practice
- 2024 Remittance @ Seconds fraud: 116 workers, BND 0.72m, fake receipts from a licensed WU agent; no refund assurance by Sept 2024. Lesson used in the doc: keep receipt until family confirms.
- Undocumented worker death 2022: employer did not pay Tk 16 lakh hospital bill; body held 2.5 years at RIPAS; Ministry paid ~Tk 4.5 lakh to repatriate after ASK appeal. Family's WEWB application got no follow-up for months.
- HC statistics: 54 complaints Jan-early Sep 2026; 30 Bangladeshis in prison in 2026 to Oct; hospital visits 25 in 2025.
- Death compensation at HC requires power of attorney from heirs; HC says no compensation for illegal or uninsured workers.

### Facts logged but not used, and why
- B0009, B0010 (bank guide on incentive exclusions), B0012 (Probash Tk 1,000 conflict), B0014, B0036, B0037, B0048, B0061, B0062, B0067, B0072, B0075, B0081, B0082, B0117: Bangladesh-side detail already covered in Qatar shape; kept for the lead if the doc wants the full Qatar-level detail.
- B0128-B0130 used; B0135 (2023 prison stats) not needed.
- B0163 (remitter licence fee BND 3,000 + BND 55,000 guarantee): trivia for workers.
- B0174, B0175, B0177-B0180 (2024 slide penalties): superseded by the Dec 2025 INRD list.
- B0184 (WU popular; ~20,000 Bangladeshis in Brunei 2024): for Background.
- B0186 (Cap 174 definition): not needed.
- B0193 used; B0194/B0195 used.

### Pages we could not download
- https://www.bb.org.bd/en/index.php/investfacility/drawing?cou=Brunei&bnk= (Bangladesh Bank drawing arrangements for Brunei): "Request Rejected" by curl and in the browser.
- https://www.labour.gov.bn (Labour Department): connection refused/blocked (also logged FAILED by another agent).
- https://rcrc-resilience-southeastasia.org:443/wp-content/uploads/2017/12/2014_edtn_immigration_act.pdf (Immigration Act 2014 edition): 403.
- https://www.police.gov.bn, https://www.fire.gov.bn: no connection.
- Firecrawl was out of credits for the whole run; the HC site was read with curl and the in-app browser.
- Brunei MFA list of foreign missions in Brunei (to confirm the Bangladesh HC address): not found.

### Open gaps (also in the draft as Need to know)
- Bangladesh HC street address and general office hours.
- Amnesty history/current; Special Pass rules; TP validity; who pays deportation ticket; post-deportation ban length.
- Remittance cost from Brunei (Bangladesh Bank survey excludes Brunei); hundi rate and operators.
- Annual deaths of Bangladeshis in Brunei; who pays body repatriation for documented workers under EO2009; RIPAS mortuary procedure.
- Current Cap 74 amounts.
