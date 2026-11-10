# Singapore: research notes

Research notes behind `doc.md`: what was searched, conflicts between sources, what happens in practice, facts logged but not used, and pages we could not download. Each section comes from one research topic; fact ids carry that topic's prefix letter (L is the lead editor's own; KA to KF are the fact-check pass).

## How the doc was put together

- Seven topics were researched in parallel (prefixes C, R, E, D, P, V, B), each saving sources with `fetch.py` and logging facts with `facts.py`, then drafting its sections. The lead merged the drafts on the Qatar model: Bangladesh-side steps (B) were slotted into the Work Permit steps, R's step numbers shifted to make room for Step 2 (passport), and R's "what workers really pay" list moved into Background, part 3.
- `tools/fetch.py` used to delete `<form>` elements, and mom.gov.sg wraps whole pages in one, so early MOM text copies came out empty; they were rebuilt from the saved HTML, and fetch.py now unwraps forms.
- Concurrent `facts.py add` runs dropped a few rows from facts.csv during the research; every cited id was re-checked against facts.csv afterwards and none is missing.
- Exchange rate: Bangladesh Bank's live page returned a CAPTCHA, so the 19 October 2026 rate comes from the archived copy the Qatar research saved (L0001).
- Personal data: the Bangladesh High Commission's "sample" domestic-worker contract PDF is a real attested case. The PDF was not kept; `sources/bdhc-sg-mdw-contract-sample.md` is a redacted transcript (names, numbers, birth date and home district removed).

## Background and corridor (insider pass) (prefix C)

Prefix C. Draft text: drafts/C-background.md (the whole "## Background", six H3 parts). Facts C0001 to C0200.

### Notes for the lead to slot into the steps (step-specific, with fact ids)

**Skills test / training centre step (Work Permit, construction)**
- BCA's five approved OTCs in Bangladesh (list of 25 Sep 2025) with addresses: C0042, C0044; trades per centre: C0045 (bca-otc-trades-bangladesh); OTCs may also run training courses: C0043.
- SEC(K) fee capped at S$925 before GST, paid by the employer to the OTC's Singapore office: C0038 (dup C0039). Bangladesh guidelines bar extra collection: C0098. A worker charged for the test is being overcharged.
- Results come from the OTC; pass both written and practical: C0041. Only CRS-registered firms can register workers, within their quota: C0040.
- From Jan 2028 no pre-entry test; must pass in Singapore within a year for renewal; R2 levy for 6 months: C0036, C0037; BDHC framing: C0136.
- Private training centres: admission Tk 38-40k (2021), passport kept, extra Tk 1.5-2 lakh demanded after test, no receipts, deliberate failing when no visa, placed with supply companies: C0109, C0110, C0111; Facebook ads "Tk 1 lakh salary": C0114; one centre's site Tk 12,000 per one-month course: C0194. BMET's 60 TTCs nominal fee: C0113.
- Untested route (train/test in Singapore) costs more, failures sent back: C0028, C0029. Uncertified worker levied S$900: C0141.

**Choosing the agency / checking the job offer step**
- Only SOs attached to an OTC can send; SO-RA exclusivity; RA can get IPA only for its SO's candidates: C0096, C0099, C0100, C0107. Example enlistment memo (Dec 2025, S. Nabiha Overseas RL-2638 via Progressive Dhaka Technology, RA Hundred Miles Human Resources): C0106. SO must hold valid licence and current NOC: C0108.
- 2018 guideline: no BMET smart card unless the IPA is enlisted on bshrs.com.bd with an IPA reference number: C0101, C0102. bshrs.com.bd did not resolve on 9 Nov 2026 (curl returned no connection). Need to know whether it is still used.
- SO deposit Tk 30 lakh at BMET: C0025, C0049. Dropped SO (Oasis) still took 3,037 clearances: C0049.
- Government cap Tk 2,62,270 (27 Jul 2017): C0122 (also C0117 Prothom Alo 2020).
- Singapore EA fee cap 1 month per year, max 2 months; shown on IPA: C0195.
- IPA: courts enforce IPA salary; ~10% never get IPA; employers declare lower salary to MOM: C0190, C0191, C0192. Two in three cannot read IPA salary: C0070. No written contract common: C0071.
- MOM survey 2024 fee ranges by sector (first-timers): C0073.

**Kickbacks / if you aren't paid step**
- Report kickbacks: MOM 6438 5122, MWC 6536 2692 (MOM PR Jul 2025): C0144. Penalties: C0197 (official), C0075 (TWC2 archive of MOM reply). MOM facilitates change of employer for reporters: C0076.
- MOM tells workers it can do nothing when fees were paid in Bangladesh or in cash: C0083.
- Security bond payouts cover unpaid salary only up to ~S$5,000: C0084; bond S$5,000 employer-paid: C0149.
- 2026 unpaid-salary cases (Process Maintenance Solutions, Jurong Technical and Construction): MOM onboarding centre, job fair 6 Nov, MWC help to change employer: C0016-C0020, C0022. BDHC July 2026 bankruptcies, ~250 re-employed: C0134.

**Changing employer step**
- Construction transfer: current employer consents within 7 days; no consent needed when permit 40-21 days from expiry: C0153, C0154; current employer priority to renew: C0155.
- Shipyard: no in-country move to another sector; Seatrium endorsement of contractors' WP applications: C0187, C0188.

**Leaving / cancellation / forced repatriation step**
- Employer cancels within 1 week of last day of notice, buys one-way ticket within 14 days, Special Pass, worker cannot work meanwhile: C0146, C0156, C0157. Employer bears repatriation regardless: C0158.
- Forced repatriation by "repatriation agents"; walk out at the airport checkpoint/tell police; MOM stepped in 23 times in 2013: C0159, C0160, C0161 (2014 source; flag as old).

**What can get you jailed / overstaying**
- Overstay: up to 6 months' jail + min 3 strokes of the cane, or fine up to S$6,000; deport and ban: C0182. Case of Bangladeshi Pabel (1 month + 3 strokes) and employer Jahangir (12 months): C0181. ICA raids on cleaners: C0183. Visitors cannot work: C0184.
- Extremist posts on social media: permits cancelled and repatriated, then detained at Dhaka airport (Jul 2026): C0198, C0199. ISA 2015-16 (27 arrested): C0180.

**Injury / death**
- WSH 2025: 36 deaths, construction 13; causes; 28,895 injury claims: C0172, C0173, C0174. Lorry deaths 2021, 2016: C0175, C0176. All-country bodies returned 2025: 5,038 (C0200) - no Singapore figure found.

**Sending money home**
- Remittance by year and rank: C0127, C0129, C0130, C0131, C0166.

### Insider test (journalist, corridor expert, returnee)

What they would expect, and where it is:
- The test centres and their Singapore owners (Fonda Global, Santarli, SEC South Point/BBR, Setsco, Lian Beng; 2018 list adds WellTech, CT, Progressive): Background part 2. Done.
- The SO system, Tk 30 lakh deposits, RA exclusivity, bshrs.com.bd: part 2. Done.
- Syndicate/monopoly claims (13 agencies 2022; 10 agencies 2024; "six companies in Singapore" per State Minister Sep 2026; "OTC-centred syndicate" per Ministry secretary Sep 2026): part 2. Done.
- Weltec fake BCA certificate scandal (Gazipur Air International, Al Jannat, RX Care, Welltech; Oasis 3,037): part 2. Done. Agencies doc already carries these flags (AC0052-AC0056).
- Kickback convictions (Derrick Ho / Lian Cheng; Loo Kim Huat / Weishen with Bangladeshi collectors and a Bangladesh-based agent): part 2. Done.
- Real costs Tk 8-16 lakh; TWC2 S$9-13k; S$15,555 (2015): part 3. Done.
- COVID dormitory outbreak (47% infected), 2021 entry ban: part 1. Done.
- Tangail as top sending district (insiders know Tangail/Munshiganj): part 1. Done.
- Mustafa Centre / Little India Sunday gatherings: part 1 "Where they live". Done (only a BBC Bangla 2020 source; no newer).
- Deaths, lorries: part 5. Done; Singapore-specific annual death count not found (Need to know).
- Remittance size and rank (10th FY26; 8th Jul-Sep 2026): part 3. Done.
- 2028 end of OTC testing: parts 0, 1. Done.
- Seatrium shipyard immobility: part 4. Done.
- ISA cases 2015-16 and July 2026: part 5. Done.
- Not covered: the 2013 Little India riot (not a Bangladeshi story; led to alcohol limits in Little India) - left out as no bearing on a decision. Hundi rates from Singapore - not researched (sending-money agent's topic).

### Method
- OEP country-clearance JSON fetched directly with curl (headers X-Requested-With: XMLHttpRequest and Accept: application/json) for 2023, 2024, 2025 and 2026 to 7 Nov; saved as sources/oep-country-clearance-*.json/.md (scratchpad script oep.py). OEP has no data before late 2022 (2022 shows 1,836), so 2014-2024 come from BMET's annual table image (Singapore column transcribed by hand, cropped and enlarged 3x: sources/bmet-annual-by-country-2025-05-img.md, image copied from countries/qatar/sources).
- OEP Singapore country id is 159 (district report: geo-clearance-count?country_name[]=159).
- MOM pages render empty through pandoc; the text is in the HTML. Extracted with BeautifulSoup into the .md (scratchpad script h2t.py) for mom-foreign-workforce-numbers, mom-pr-2026-dorm-sites, mom-pr-2021-10-vaccination-entry.
- TWC2 2026 report PDF: pdftotext -layout interleaves the two columns, so a plain pdftotext extraction of the same PDF was saved as sources/twc2-price-of-working-report-2026.md for quoting.
- Ittefaq Weltec articles copied from agencies/sources (logged with fetch.py --log ... manual).
- Facts also logged from sources other agents fetched and registered (probashi-otc-guidelines-fc, probashi-so-progressive-technology-pdf, mom-wp-*, mom-pr-kickbacks-2025, mom-factsheet-fw-policies-2026, mom-nts-ol, bdhc-sg-worker-info-2026-10-pdf, bb-top30-country-remittance, bb-wagermidtl-selected-countries, deshrupantor-sg-training-trap, palo-sg-18-months, inqilab-sg-cost-rising, ica-*, twc2-repatriation-agents-2014, hasibstc-courses).
- Money: S$1 is about Tk 95, from TWC2's "ten lakh taka roughly equivalent to $10,500" (Feb 2026, C0177). Replace with Bangladesh Bank's rate if the lead has one logged.

### Searches run (Firecrawl, Bangla and English)
Dormitory numbers; Bangladeshis in Singapore (Bangla); BCA OTC list; সিঙ্গাপুর ট্রেনিং সেন্টার বিসিএ টেস্ট সেন্টার সিন্ডিকেট; MOH COVID dormitory serology; সিঙ্গাপুর ডরমিটরি করোনা; TWC2 recruitment fees; TWC2 survey tag and kickback tag; remittance from Singapore FY25/26 (Bangla); lorry deaths (Bangla); MOM WSH 2025; সিঙ্গাপুর আইপিএ জাল ভিসা প্রতারণা (nothing usable beyond guides); Bangladesh-Singapore labour MoU (none found); "second-largest labour market" (TBS Sep 2026); 2021 border measures; ISA arrests 2016 and 2026; bodies returned by country (no Singapore split found).

### Conflicts
- Number of Bangladeshis in Singapore: BDHC Oct 2026 "about 135,000" by BMET's latest (C0132, official); TBS Sep 2026 "an estimated 200,000" (C0165); Inqilab 2022 quoting FM Momen (early 2021) "about 130,000" (C0125); BDHC Jan 2016 "more than 160,000" via TWC2 2017 (C0033). Draft uses 135,000 and notes 200,000.
- Test centres: TBS Apr 2024 "six" (C0023); BCA list 25 Sep 2025 "five" (C0042); Ministry 2018 list eight (C0104); Ministry Dec 2025 memo names an OTC "Progressive Dhaka Technology Ltd" not on BCA's Sep 2025 list (C0106) - Need to know in draft.
- Agencies controlling the market: 13 (Inqilab 2022, C0123), 10 with training centres (TBS 2024, C0025), "six companies in Singapore" (State Minister, TBS Sep 2026, C0163). Different units (BD agencies vs Singapore companies), different years.
- Weltec: Ittefaq Nov 2022 says the four agencies sent "more than 100,000" (C0047); Ittefaq Mar 2023 says "about 60,000" clearances (C0051). Draft uses the later figure.
- TBS Apr 2024 (Kiron) says the per-Singaporean quota fell from 7 Bangladeshis to 5 in 2024 (C0030); MOM's construction page says 5 Work Permit holders per local employee (C0140), applies to all nationalities; the "7" is not confirmed by MOM. C0030 not used.
- TWC2's kickback article title says "jailed 24 months"; its text says "jailed 24 weeks". Draft uses 24 weeks. Straits Times original (14 Nov 2024) not fetched.
- Recruitment fees: MOM's 2024 survey ranges (construction S$1,000-7,800) far below TWC2 casework (S$9,000-13,000 for first-time Bangladeshis) and Bangla news (Tk 8-10 lakh in 2024; up to Tk 16 lakh in 2026). TWC2 says MOM's figures understate (C0078). Draft shows both.
- BMET table vs OEP for 2023 (53,265 vs 53,031) and 2024 (56,878 vs 56,847). Draft uses BMET's table to 2024 (C0001) and OEP for 2025-26 (C0003, C0004); C0005, C0006 are the OEP figures, unused.
- TBS Apr 2024 says about 5,000 certificate holders a year come out of the training centres (C0193), which is far below yearly departures (50,000+); possibly the TBS figure counts one centre or one channel. Not used.
- C0189: claim says shipyard workers earn about a quarter of PWM recommendations; the quote supports only the ~S$2,000 PWM level. Not used in draft; fix the claim wording if used.

### Facts logged but not used, and why
- C0005, C0006: OEP 2023/2024 figures (BMET table used instead).
- C0012: S Pass total (no Bangladeshi relevance).
- C0015: 71,500 beds pipeline (detail).
- C0021: duplicate of TWC2 salary via bdnews.
- C0023, C0193: TBS 2024 six centres / 5,000 certificates (superseded / doubtful).
- C0030: Kiron's 7-to-5 quota claim (unconfirmed; see conflicts).
- C0032: TBS 2024 Tk 40-60k earnings (superseded by TWC2 2026 salary data).
- C0033, C0125: older community estimates.
- C0034: BAIRA quote (generic).
- C0039: duplicate fee cap.
- C0047: superseded Weltec figure.
- C0058, C0059: COVID ICU/deaths/clearance (detail).
- C0062: all-nationality TWC2 average.
- C0069: Bangladeshi monthly salary S$837 (basic S$820 used).
- C0102, C0105, C0108: guideline detail (in step notes).
- C0115: used. C0117: duplicate cap. C0119: BBS contract finding (conflicts with TWC2's no-written-contract finding; dated 2015-18).
- C0128, C0131: total remittance / Jul-Nov 2025 (detail).
- C0144: MOM/MWC hotline numbers (step material).
- C0185 used; C0189 see conflicts.
- C0200: all-country bodies (no Singapore split).

### Open questions (also as Need to know in the draft)
- Current list of Singapore SOs with their OTC and Singapore RA.
- Whether bshrs.com.bd is still used for IPA enlistment.
- Whether Progressive Dhaka Technology Ltd is BCA-approved.
- How a Tk 10-16 lakh payment is split; IPA street price.
- Payment stages in 2026.
- Annual Bangladeshi deaths in Singapore and causes.
- Bangladesh-Singapore labour MoU (none found).
- Whether the Weltec agencies or Oasis were ever punished.
- Share of clearances by sector.

### Pages we could not download
- http://bshrs.com.bd/ (no connection, 9 Nov 2026).
- https://www.bb.org.bd/en/index.php/econdata/wagermidtl (curl returns a page without the data table; the other agent's Firecrawl copy, data to April 2024, was used).
- Straits Times originals for the Derrick Ho case (14 Nov 2024) and the Process Maintenance Solutions / Jurong Technical cases (29 Oct and 7 Nov 2026) were not fetched; Bangla and TWC2 reports of them were used.

## Work Permit: recruitment and getting there (prefix R)

Prefix R. Draft: `drafts/R-workpermit-recruitment.md`. Facts R0001 to R0295 (one id, R0070, was removed and re-logged as R0087; a stray test row was deleted). Research 8-9 Nov 2026, interrupted by a connection stall.

### Method notes

- **mom.gov.sg pages convert to empty text with `fetch.py`**: MOM wraps the whole page body in an ASP.NET `<form>`, which `fetch.py` strips before pandoc. I regenerated the `.md`/`.txt` text copies from the same saved `.html` with a scratch script that does the same cleaning minus the `form`/`button` removal (`remd.py` in my scratchpad). Applied to my MOM pages and, harmlessly, to `mom-check-pass-status` and `mom-sgworkpass` (fetched by another agent): I re-checked every existing fact quote against those two files afterwards and all still match. **Suggest the lead fixes `tools/fetch.py`** (don't decompose `form` when it wraps the main content), since other agents' MOM pages (`mom-spass-*`, `mom-wp-overview`) are still 72-byte stubs.
- Scanned Ministry/BMET/High Commission PDFs have no or garbled text layers; I used Firecrawl's PDF parser and saved the output as `-fc.md` files: `probashi-otc-guidelines-fc`, `bdhc-sg-ipa-waiver-2025-fc`, `bmet-permission-sg-rl1199-2025-03-fc` (page 1 only, worker names omitted).

### What the research found (for the lead and Background writers)

- **The Bangladesh choke point is the OTC-SO-receiving agent chain.** Ministry guidelines (1 Oct 2018, R0187-R0196): Singapore companies hold BCA approval for OTCs; their Bangladeshi partners hold a Ministry NOC renewed yearly; the partners and agencies tied to them are "Sending Organisations"; each SO is tied to one Singapore receiving agent; BMET clears only IPAs that come through that SO; the Singapore agent may get IPAs only for that SO's candidates. This is a closed chain: whoever controls an OTC NOC controls the job flow. The Dec 2025 SO letter (R0197) shows the system still runs. Earlier SO letters (2015, not saved as sources, read via Firecrawl): Progressive Test Centre with Oasis Services (RL999, GK Manpower) and Jihan Overseas (RL1104, Bevertec Consultants), memo 49.000.00.00.027.2012.158 of 10-08-15; WellTech Test Centre with Al Jannat Overseas (RL926, Hundred Miles Human Resources), memo ...15.184 of 10-09-2015. URLs: objectstorage.../office-probashi/2024/12/1d35b0923b4247ca8d214214a32524c9.pdf and .../9f217620ad2b4417a6057abc92c6d7d8.pdf. These tie in with the Ittefaq 2022-23 Weltec/Oasis scandal already in agencies/ (AC0052-AC0056): Oasis was later dropped from the SO list but took clearance for 3,037 workers; Weltec's BCA approval was cancelled.
- **"Progressive" OTC.** The 2018 copy list names "Progressive Test Centre (Pte.) Ltd., Tongabari, Ashulia" (Singapore partner Progressive Builders). BCA's Sept 2025 OTC list has 5 Bangladesh OTCs and no Progressive; yet the Ministry enlisted an SO for "Progressive Dhaka Technology Ltd" OTC in Dec 2025, with Hundred Miles HR as receiving agent (the same Singapore EA that worked with Al Jannat/WellTech in 2015). Unresolved: written as a Need to know.
- **bshrs.com.bd** (the Ministry-endorsed IPA database required by the 2018 guidelines; no BMET smart card without a bshrs IPA reference number) does not resolve (DNS failure, 9 Nov 2026). Need to know whether BMET still requires it.
- **Test fee:** BCA caps SEC(K) fees at S$925 before GST and says the sponsoring employer pays, to the OTC's Singapore office (R0148-R0149). Ministry rules also ban extra collection (R0188). In practice workers pay training centres a "package". No 2026 street price found in print beyond older reports (Tk 6 lakh package, 2016-21; Tk 7-8 lakh extra demanded).
- **Overseas testing ends Jan 2028 for Bangladesh** (BCA 30 Apr 2026; R0143, R0165, R0289-R0293). This will change the whole OTC/SO chain; no Bangladesh-side response found yet. Big open question for the Background.
- **BCA identity verification/IPA endorsement ended 4 May 2026** (R0150). MOM's "Apply for a Work Permit" page (updated 29 Sep 2026) still tells employers to book a BCA appointment within 4 months of the test (R0085): conflict, kept as one Need to know.
- **IPA attestation by the Bangladesh High Commission was waived from 18 April 2025** (R0274). The High Commission's 2022 "General Information" page (another agent's B0182/D0195) still describes on-the-spot IPA attestation; the 2025 notice is newer and official, so I used it.
- **No pre-departure medical in Bangladesh is required by MOM**: the Work Permit medical is done at the Onboard centre (male CMP) or a Singapore clinic/Anchor Operator (R0123-R0124). A Dhaka agency's post-IPA checklist (R0287) lists no Bangladesh medical. Forum posts mention people doing a private check in Dhaka before going; whether employers demand one is a Need to know.
- **Who pays the inbound air ticket:** no MOM rule found (MOM only requires the employer to pay repatriation, R0065). BRAC Probashbandhu's permission letter has an "Air ticket" line but the scan is garbled. Need to know.
- **Real costs:** TWC2's Aug 2026 survey (R0219-R0228) gives S$3,259 average for Bangladeshis who paid, but this is diluted by mid-career workers; TWC2 says all new Bangladeshi CMP workers pay. Older anchors: S$15,000 first-time construction (TWC2 2016/2017), BBS Tk 5,74,241 (2020 survey of 2015-18 migrants), Tk 6-8 lakh (ex-BAIRA leader, 2022). Facebook/YouTube pages in 2025-26 quote Tk 8-15 lakh packages (not logged: social media only). The agencies/ notes record a Recruitment Advisor review of Tk 950,000 for Singapore (AE0036).
- **BRAC Probashbandhu (RL1199)** is the only agency with posted Singapore permission letters (agencies/ notes: 15 letters, 170 workers). Its March 2025 letter is a "Sandbox Piloting" group: workers take SEC(K) in Singapore at their own cost (R0280), basic S$18/day. The cost cell OCRs as "২৬০,০০০/- থেকে ২,৫৮০০০/-" (Firecrawl) and as garbled glyphs in pdftotext; I could not read it reliably. Since BRAC is the project's owner, the draft names it only as a factual example of a permission letter, not as a recommendation; the lead should decide.
- **IPA salary:** MOM survey 2024: 90.1% got an IPA before starting work, 91.5% were paid the IPA salary (R0229-R0230); TWC2: 2.5% were paid less, employers sometimes declare less than agreed (R0276-R0278). Courts enforce the IPA terms (R0275).
- **Card delivery time conflict:** MOM key facts page (1 Jul 2026) says 4 working days (R0056), apply page (29 Sep 2026) says 5 working days (R0083). Used the newer 5.
- **Age limits changed twice:** 50 (non-Malaysian) until June 2025; 61/63 from 1 Jul 2025 (COS 2025 factsheet, R0283); now 62/64, pegged to retirement age (sector pages Oct 2026, R0003-R0004). Used current 62/64.

### Independent fact-check (9 Nov 2026)

A verifier subagent checked every sentence against the quotes and sources. Fixed: process R1 criteria (R0138's claim wrongly makes a PCF Bronze firm a requirement; it is one of three alternatives with salary S$1,200 or 4 years; corrected by R0296, R0297, R0302, R0303, and R0138 is no longer cited); TWC2 sector averages are for all nationalities, not Bangladeshis; AEP is not PRC/Thailand-only: BCA's AEP page invites employer-led pilot proposals for any source country, India's round closed 30 Oct 2026, and Asia Philanthropy Circle runs a "migrant worker sandbox" AEP pilot (R0298-R0301). BRAC Probashbandhu's "Sandbox Piloting" letter may belong to that sandbox: unconfirmed, kept as Need to know. Also removed advice-like phrases, added "allegedly" for unproven cases, and explained terms at first use.

### Facts logged but not used, and why

- R0138: claim is wrong (see above); superseded by R0296.

- R0010, R0119 (SIP rule restated), R0013 (step order, covered by Step 5), R0034/R0045 (duplicate of R0044/R0035), R0047 (covered by R0020/R0029/R0049), R0055 (covered by R0074/R0107), R0056 (older conflicting card time), R0063 (superseded by R0246-R0247), R0067 (marriage rule: belongs in "what can get you jailed"), R0091, R0092, R0098-R0100 (bond forfeiture/discharge: belongs in absconding/leaving sections), R0140 (duplicate), R0144-R0145 (covered by BCA factsheet facts), R0152 (formwork detail), R0189, R0195 (NOC renewal and bshrs operator: Background detail), R0204, R0205 (BBS: BMET DG quote, contracts; Background), R0227, R0230, R0232 (survey details), R0251 (bank book), R0272-R0273 (CNA duplicates of BCA official facts).

### Searches run (main ones)

- MOM: sector pages, NTS-OL page and FAQ PDF, COS 2025 and 2026 factsheets, key facts, apply, IPA, security bond, medical insurance, medical exam, Onboard centre, SIP, check-status eService, SGWorkPass, EA Directory and FAQs, EFMA page, kickback and phantom-worker press releases, MOM Migrant Worker Survey 2024.
- Singapore law: Employment Agencies Rules 2011 on SSO (fee cap, refund).
- BCA: overseas trade testing page, OTC contact list, Bangladesh trades list, registration dates, e-certificate slip, AEP circular (30 Oct 2026), media factsheet (30 Apr 2026), OTMS portal (employers only; not saved as a source).
- Bangladesh: Ministry SO enlistment letters (2015, Dec 2025), OTC guidelines (2018), BMET permission letter RL1199, High Commission IPA waiver notice.
- News/NGO: TWC2 (2025 survey comments parts 2 and 4; 2026 price-of-working report), CNA (2020 recruitment fees; 2026 BCA change; 2026 fake-agent case), HOME (2026 Shanti case), Straits Times (2026 fake permits), Desh Rupantor (2021 training trap), Prothom Alo (2020 BBS survey), Inqilab (2022 syndicate), a training centre's course page, a Dhaka agency's post-IPA checklist.
- Bangla searches: সিঙ্গাপুর ট্রেনিং সেন্টার খরচ; সিঙ্গাপুর শ্রমবাজার ট্রেনিং সেন্টার দালাল খরচ; "২ লাখ ৬২ হাজার ২৭০" সিঙ্গাপুর; সিঙ্গাপুর সেন্ডিং অর্গানাইজেশন; সিঙ্গাপুর ভুয়া আইপিএ প্রতারণা; সিঙ্গাপুর যাওয়ার আগে মেডিকেল টেস্ট.

### Not found after searching (kept as Need to know)

- 2026 street price of a Singapore construction "package" in Dhaka (only social-media claims of Tk 8-15 lakh).
- Any case of test impersonation (proxy candidates) at Bangladesh OTCs.
- Standard IPA validity period (MOM says only "stated in the letter").
- Whether the 2017 Tk 2,62,270 cap was replaced.
- A worker-facing way to verify a SEC(K) result before travel (OTMS needs CorpPass).

### Pages we could not download

- http://www.bshrs.com.bd/ : DNS does not resolve (curl and Firecrawl), 9 Nov 2026.
- https://www.mom.gov.sg/passes-and-permits/work-permit-for-foreign-worker/sector-specific-rules/marine-shipyard-sector-requirements : 404 (the live URL is .../marine-sector-requirements, saved as `mom-wp-marine`).
- MOM .../work-permit-for-foreign-worker/documents-required, .../get-the-work-permit-issued, .../check-status : 404 (content is on the apply page).
- otms.bca.gov.sg: curl returned an empty shell; read via Firecrawl but not saved (employer login portal only).

## Work Permit: rights and life in Singapore (prefix E)

Research notes for drafts/E-workpermit-life.md (prefix E). 405 E facts logged (356 official, 49 news/NGO), 397 cited in the draft.

### Method

- MOM (mom.gov.sg) pages download fine with curl, but `fetch.py` strips every `<form>` element, and MOM wraps the whole page body in an ASP.NET form, so the .md and .txt copies came out empty (72 bytes). I re-made the text copies from the saved .html with a scratch script that keeps the form content (same bs4 + pandoc conversion as fetch.py, only `form`/`button` not removed, plus header/footer/nav dropped). The .html files are untouched. **For the lead:** other agents' MOM sources may have the same empty-text problem; fetch.py should not decompose `form` on mom.gov.sg.
- Quote check: `facts.py` turns `**bold**` and link brackets into spaces, so a quote ending right before a full stop or comma after bold or linked text fails; quote without the trailing punctuation.
- Facts from other agents cited: V0051, V0052, V0060 (SG Arrival Card, ICA). Sources registered by other agents and cited by me: mom-wp-conditions, mom-faq-passport, mom-faq-marriage-pregnancy, mom-wp-key-facts, mom-wp-construction, mom-wp-security-bond, bdhc-sg-ipa-authorization-pdf. I registered mom-wp-existing-process (fetched by another agent, not registered).

### Searches run

MOM site searches (firecrawl, site:mom.gov.sg) on: transfers and consent; TADM/ECT; heat stress; medical insurance; WICA and Special Pass; FEDA, NDS and the Dormitory Transition Scheme; repatriation; passports; PCP; maximum age and period of employment; ACE Group and mental health; EFMA penalties; replacement cards; missing workers; lorry transport; overseas leave; termination notice; 2026 myMOM eService changes; illegal employment penalties. Other: TADM (tal.sg) filing and mediation guide; judiciary.gov.sg ECT pages and guide; MWC, HealthServe, TWC2, ItsRainingRaincoats; Bangladesh High Commission labour wing; MOH/gov.sg vaping; MHA/SPF liquor control; SPF SIM-card and money-mule offences; Immigration Act s15 (SSO); CNB drug laws; NEA littering; chewing-gum regulations (SSO); BBC on the 2013 riot and 2012 SMRT strike; NAS copy of MOM's 2012 strike statement; Bangla news (Daily Star Bangla, bdnews24) and NTUC on the October 2026 unpaid-wage case.

### Sources and dates

- MOM "A guide for migrant workers" (mom-mw-handy-guide) is undated and from the COVID period (still has AccessCode, Exit Pass and Rostered Routine Testing pages). Used for rights, IPA, KETs, deduction bans, penalties table and contacts, all status possibly-outdated; where a current MOM page says the same thing, the current page is cited. Its phone list is garbled in the text layer (SOS, HealthServe and embassy numbers can't be matched to names reliably), so those numbers were not used.
- Work Permit conditions in law: the PDF MOM links (mom-wp-conditions-legal) is the informal consolidation in force from 1 October 2020. Newer amendments may exist; current MOM web pages (2025-2026) were preferred wherever they cover the same point.
- HealthServe helpline page is from 2021 (modified 2022); the 24-hour number 3129 5000 is repeated by MOM's mental-health advisory (Oct 2024). Clinic hours and fees at the foot of the HealthServe page may be out of date (Need to know in the draft).
- Bangladesh labour wing contacts come from the Ministry of Expatriates' Welfare labour-wing list, last updated 1 May 2025 (possibly-outdated). The address (Jit Poh Building, 19 Keppel Road) is from a 2022 High Commission letter template.
- Annual leave page (2023) and termination-with-notice page (undated) are old but the Employment Act rules they state are long-standing.

### Conflicts

- Maximum age at application: MOM key facts says "below 62 years old when applying" (E0134); the construction sector page says "Maximum: 62 years old" (E0135). Both say work until 64. Left as Need to know.
- Maximum period of employment: MOM's renewal page (April 2026) still lists "the maximum employment period" as something that can shorten a renewal (E0140), while sector pages say holders can work until 64. Left as Need to know.
- PCP co-payment: S$5 clinic / S$2 telemedicine now; S$5 for both from 1 April 2027 (MOM press release 6 Aug 2026). Both stated with dates.
- WICA medical expenses cap: S$45,000 for accidents before 1 Nov 2025, S$53,000 from 1 Nov 2025 (MOM, Oct 2026). Draft gives the current figure.

### What happens in practice (NGOs, news and MOM replies)

- Salary claims: in 2025, 88% of salary claims settled at TADM mediation, 12% went to ECT, over 90% fully recovered (MOM Employment Standards Report, July 2026). TWC2's April 2026 report (17 interviews) found employers typically cancel claimants' work passes "out of pique", TADM generally issues COE (Change of Employer) letters, the process to ECT filing usually takes six months or less, tribunal orders are often unenforceable when employers are insolvent or abscond, and the S$5,000 security bond is often the only route to payment but caps recovery at S$5,000. Workers feel pressure to settle low.
- COE letters (TWC2, Sept 2025, 20 interviews): issuance is "more or less standardised", but extensions vary; workers without contacts pay unlicensed Bangladeshi job fixers; the letter can stigmatise the worker.
- October 2026: ~230 workers (many Bangladeshi, arrived from July 2026, some paid up to S$12,000 to come) of Process Maintenance Solutions and Jurong Technical & Construction unpaid up to two months; MOM investigating; MWC feeding ~90, briefing in Bengali, speeding up change of employer, warning the firms may not pay; one worker's permit valid to July 2027 cancelled without reason; he earned S$600/month and had a S$9,000 bank loan for the agent (NTUC 23 Oct, Daily Star Bangla 29 Oct, bdnews24 8 Nov 2026).
- Kickbacks: TWC2 (Jan 2026) case of a Bangladeshi welder whose new employer cut out the agent and took S$600 directly, then told him to delete the evidence; later short-paid overtime and pressed to sign a contract with a blank salary; three co-workers terminated without warning in five months. MOM (2021) said it investigates ~960 kickback cases a year, taking action against ~102 employers a year, 80% by warning or composition fine.
- Passports: MOM's 2024 survey found over 31% of Work Permit holders do not keep their own passport (PQ, 3 March 2026); MOM says most employers return passports after it intervenes.
- Forced repatriation: MOM's guide and TWC2 (2022) say a worker taken to the airport can go to the ICA counter and be referred to MOM / given a Special Pass; TWC2 says workers find this hard to act on for fear of being treated as overstayers. Repatriation agents escorting workers is documented by TWC2 in 2014; no recent source found.
- Dormitories: 70% of ~1,600 FEDA-licensed dormitories are older ones with 12-16 per room (PQ, 6 May 2026). On 6 Nov 2026 MOM announced a relaxation letting NDS dormitories go to 14 per room and 3.6 sqm per person from 1 Jan 2027 to 31 Jan 2030, to build bed supply.
- Illegal work while on a claim: MOM/TADM's 2026 statement on Mr Ali Md Kawsar (a Bangladeshi worker): Special Pass and COE letter issued, three mediation sessions failed, ECT ruled in his favour and he was paid in full in Sept 2025; he had worked illegally Feb-Jul 2025, was later allowed a 6-month TJS job, and enforcement was taken against him in Feb 2026.

### Facts logged but not used (and why)

- E0129 (MWC listed in MOM's mental-health advisory): the quote does not show "24 hours"; MWC's own page is cited instead.
- E0114 (Settling-In Programme told about passports): Settling-In Programme belongs to the arrival steps (another agent's section).
- E0277 (ECT claim cannot be served outside Singapore): relevant only to employers abroad; left out for length.
- E0287 (about 850 Special Pass holders a year work under the TJS): statistic with no bearing on what a worker does.
- E0313, E0324: duplicated by E0394 and E0326/E0327.
- E0342 (consent to MOM/MWC contacting the worker): minor.
- E0401 (some paid up to S$12,000): belongs in Background part 3 (costs); flag for the lead.

### Open questions (also in the draft as Need to know)

- Seats and seat belts in lorry rear decks; any lorry rule changes since 2024.
- HealthServe clinic hours and fees now.
- Maximum age at application (below 62 or 62); whether any maximum period of employment remains.
- Who pays a lost-card replacement fee (S$109).
- Home-leave ticket: any rule, or contract only; usual home leave for Bangladeshi CMP workers.
- Current fine for spitting.
- How a worker checks for a re-entry ban before paying for a new job.
- COE letter validity and extensions; filing a TADM claim without Singpass in person, counter hours.
- Whether repatriation companies still escort workers to Changi, and what ICA does when a worker refuses to board.
- What the Bangladesh High Commission labour wing actually does in unpaid-wage and forced-repatriation cases; whether its May 2025 contacts are current.
- Transfer-job fixer fees in 2026.

### Pages we could not download

- https://www.bdhc.sg/news/labour-wing-of-bangladesh-high-commission-has-arranged-an-awareness-program-along-with-dormitory-visit/ (curl failed with status 000; Firecrawl failed on an SSL certificate error). Labour wing page of the Bangladesh High Commission; would confirm the labour wing's phone (search snippet: +65 6255 0075, mission.singapore@mofa.gov.bd).
- https://www.nlb.gov.sg/main/article-detail?cmsuuid=1665605a-de43-4e02-a8aa-c3d8f42a1c8c (NLB Infopedia, Little India riot; HTTP 202 bot wall). BBC used instead.
- https://www.nlb.gov.sg/main/article-detail?cmsuuid=d937e20c-d28d-451b-a661-951a056c8c33 (NLB Infopedia, SMRT bus drivers' strike; HTTP 202). NAS copy of MOM's statement and BBC used instead.
- https://www.nlb.gov.sg/main/article-detail?cmsuuid=8d4408cb-eb2d-4604-921e-7fa55f51baf3 (NLB Infopedia, chewing gum ban; HTTP 202). SSO regulations used instead.
- Not tried for lack of time: MWC Facebook post on Help Centre hours (May 2026); the Instagram post with ItsRainingRaincoats' WhatsApp (+65 8101 8187) and admin email; TWC2 "Fog and minefields" and "Not good anywhere" reports (Bangladesh-specific, 2025).

## Domestic workers (prefix D)

Researcher prefix D. Draft: drafts/D-domestic-worker.md. Facts D0001 to D0278 (check facts.csv for the final count).

### Method notes

- MOM pages fetched with curl render empty in fetch.py's text copy because MOM wraps the whole page body in an ASP.NET `<form>`, which fetch.py strips. I re-made the .md and .txt text copies from the saved .html (keeping div#MainContent) with a scratchpad script (momconv.py); the .html is the untouched curl copy. Tables in MOM pages show as [TABLE] in the .md, so quotes from tables come from the .txt copy. "Last Updated" dates are from each page's footer. Suggest the lead patch fetch.py to keep `<form>` content (or keep div#MainContent) for mom.gov.sg.
- The High Commission's "Sample of Employment Contract of Foreign Domestic Worker" PDF is a real attested case with a migrant's name, passport, FIN, NRIC, address and phone numbers. I deleted the PDF from sources/ and kept a redacted Firecrawl OCR transcription (sources/bdhc-sg-mdw-contract-sample.md). Re-download from the URL in the file header if needed; do not commit the unredacted PDF. The doc does not name the worker or employer.
- BMET citizen charter clearance item 6 (women domestic workers: proof of age 25-45 and guardian NOC) logged as D0191 with --no-quote-check, quote transcribed from the page image by the Saudi agent (saudi-arabia D0039); the text layer is garbled and no PDF renderer is installed here.
- The draft cites four B facts (B0029 housekeeping course destinations, B0058 PKB women's loan, B0126 death compensation via the Ministry, B0177 harassment complaint via the Ministry), B0030/B0002 for OEP registration and B0037 for self-obtained visa clearance, rather than re-logging the same garbled Bangla charter pages.

### Searched

- MOM: the whole Work Permit for MDW section (eligibility, employer requirements, security bond, insurance, medical, 6ME, EOP, SIP, frequent changes, levy and concession, apply, renew, cancel, transfer direct and through EA, notify MOM, employer's guide subpages on rest days, contracts and safety agreement, salary, disputes, abuse, employment rules, MDW interview, house visit, sending home, overseas leave, debarment), MOM FAQs (MDW in distress, not paid, passport, marriage and pregnancy), MOM press releases (2021 MDW support measures, 2022 mandatory rest day), MOM press reply 2024 (MDW well-being), Ask Jaya columns (phone, home leave), "Paying your helper's salary on time" (placement loan rule), MOM's educational requirements PDF for first-time MDWs (Bangladesh: SSC or HSC only), EA directory and EA FAQs, check-pass-status eService.
- Law: Employment of Foreign Manpower (Work Passes) Regulations 2012 on SSO (Fourth Schedule, current, with the 1 Jan 2023 rest-day amendments) and MOM's 2020 informal consolidation PDF; Employment Agencies Rules 2011 on SSO (fee cap, overseas costs exclusion, refunds, passport return, no entry before IPA).
- Bangladesh: Housekeeping Training Operation Policy 2023 (sent Aug 2025), Ministry approval of 21 agencies for women domestic workers (1 Sep 2025), BMET citizen charter, OEP clearance reports filtered to Singapore and women for 2024, 2025 and 2026 (to 7 Nov).
- High Commission of Bangladesh, Singapore: welfare general information (maid visa attestation listed), IPA authorization form, address page, IPA attestation waiver notice (18 Apr 2025), October 2026 general information for workers, sample MDW contract (attested 10 Apr 2025).
- NGOs and news: HOME (home page, Annual Report 2025, 2025 phone-restriction article, 2014 "business of making money from maids"), CDE (contact, Rex House), FAST (contact), TWC2 (2012 SIP replaces entry test), Straits Times (Oct 2026 debt traps; May 2026 rest-day enforcement; 2016 bogus FDW permits), CNA (Aug 2025 moonlighting fine; Feb 2026 "sponsor" scheme jail), Financial Express (2010 Singapore opens doors to Bangladeshi maids), SearchMaid and housemaid.com.sg (Bangladeshi maid agencies and an employer fee guide), SIP providers (Absolute Kinetics, Grace Management: Bengali classes).
- Bangla searches: সিঙ্গাপুরে গৃহকর্মী বাংলাদেশি নারী; সিঙ্গাপুরে চাকরির কথা বলে নারী পাচার প্রতারণা ফেসবুক; সিঙ্গাপুরে নারী কর্মী পাঠানো বিএমইটি গৃহকর্মী হাউজকিপিং. Results were Facebook posts and YouTube videos (an explainer on MDW rules, broker posts, an abuse case of a Bangladeshi man convicted for sexually abusing a maid) and no Bangla news report on Bangladeshi women going to Singapore as domestic workers.

### What the evidence says about Bangladeshi MDWs

- Bangladesh has been an approved MDW source for a long time; in 2010 the Singapore agencies' association (AEAS) visited Dhaka to promote Bangladeshi maids, and Bangladesh High Commission officials then said hardly any Bangladeshi maids worked in Singapore (Financial Express, 21 Sep 2010, logged as source only).
- BMET cleared 89 women for Singapore in 2024, 126 in 2025, 145 in 2026 to 7 Nov (all occupations; OEP does not show occupation). Singapore had 316,900 MDWs in 2025.
- The High Commission's October 2026 note lists Bangladeshi workers' sectors without domestic work. HOME's 2025 shelter nationality chart has no Bangladeshi category (D0243, logged, not cited).
- Singapore maid portals list a few Bangladeshi maids and 3 to 4 agencies that place them; one portal's fee guide includes "Bangladesh EC Processing S$200" (employer side) and an agency fee of S$888 for a new Bangladeshi maid (D0268, D0269); the guide's S$30 permit fee is older than MOM's current S$35, so it is outdated.
- The one documented case (attested 10 Apr 2025): direct hire by a household, S$600 salary, 4 rest days a month, levy S$60 (concessionary), S$0 owed to a Singapore EA, contract clauses making the worker pay her own ticket and the visa cost if she left within 2 years and limiting phone use to rest time.

### Conflicts and points to check

- Age: Singapore allows 23 to under 50 at application; Bangladesh's housekeeping course and BMET clearance need 25 to 45. Effective window for a Bangladeshi woman going through BMET: 25 to 45.
- Education: Singapore needs 8 years of formal education, and for Bangladesh MOM accepts only SSC or HSC (June 2026 PDF). The Bangladeshi housekeeping course needs only class 5 (relaxable). So the course alone does not qualify a woman for Singapore.
- Housekeeping course: the 2023 policy covers all women migrating in housekeeping; BMET's 2026 citizen charter says compulsory for Hong Kong and the Middle East (B0029). Unclear for Singapore (Need to know in draft).
- High Commission attestation: the welfare page (2022) lists maid visa attestation; the 18 Apr 2025 notice waived IPA attestation; the only attested maid visa sample is 10 Apr 2025. Unclear whether MDW papers are covered by the waiver (Need to know in draft). The B agent's draft says no IPA attestation is needed any more (B0287, B0288).
- Ticket home: the High Commission's attested April 2025 contract made the worker pay her ticket and the visa cost if she left within 2 years; Work Permit conditions (Fourth Schedule Part I para 23) make the employer bear repatriation cost at any time unless the Controller permits otherwise, and MOM's "full salary" guidance bars deductions for repatriation.
- Medical insurance: the 2020 informal consolidation of the regulations says S$15,000; MOM's page (Sept 2026) says S$60,000 annual claim limit since 1 July 2023. Used MOM.
- Entry test: the brief asked about an "Entry Undertaking (ADLP)" and an English assessment. No current MOM page mentions an entry undertaking, ADLP or language test for MDWs. TWC2 (2012) reports the SIP replaced the English entry test from 1 May 2012 (D0278, lead). MOM's EOP and SIP pages are the current rules.
- Men: MOM's eligibility table says "Sex: Female". No source found on any pass for a male household driver, cook or gardener (Need to know in draft).
- Safety agreement: MOM publishes it in 7 bilingual versions, none Bengali.
- SIP language: MOM says "native language"; Absolute Kinetics offers English classes with a Bengali interpreter (Tue, Thu, Sat, book 2 days ahead); Grace Management offers translated international classes including Bengali.

### What happens in practice (for the Background and caseworkers)

- About 90 employers a year have been penalised since 2023 for denying the mandatory monthly rest day (ST, May 2026, citing the Manpower Minister); 64% of MDWs stay over 6 months.
- HOME 2025: 501 women sheltered, about 1,200 MDW helpline calls, 480 helped at the MDW helpdesk; top issues verbal abuse 331, overwork 236, threats 227, documents confiscated 201, no full rest day 184, food 184; transfers still depend on employer consent, and MOM lets the repatriation destination default to the home country.
- MOM told ST (Oct 2026) that MDWs who borrow from unlicensed moneylenders lose their pass and are barred.
- Enforcement against workers: moonlighting fines (S$13,000, Aug 2025), "sponsor" scheme jail (16 weeks plus S$25,000, Feb 2026), bogus-employer scheme (2016, workers permanently barred), fake qualifications (660 barred a year, MOM 2021).

### Independent fact-check (done 9 Nov 2026)

A verifier agent that had not seen the research checked about 220 sentences against the cited quotes and saved sources and found 25 problems. All were fixed in the draft: salary-change rule (a cut needs written consent and notice to MOM, a raise does not; D0284, D0285), the "bans only on conviction" line narrowed to MOM's referee system (D0206), fee-cap wording, "first-time" for the CDE interviews, the attestation case wording (Counsellor (Local), not the Labour & Welfare Wing address), "barred from working in Singapore", "may" penalties, "two consecutive months", "should not" for 6ME presence and joint accounts, "communication barriers", "uncorrected error", latecomers rule attributed to Absolute Kinetics only, the entry-test sentence, the course-only bars, the transfer steps spelled out (D0286 to D0288), the EC fee guide marked undated, terms explained (POSB, MRT, HealthServe, Special Pass, smart card). New facts with exact quotes were logged where an earlier fact's claim said more than its quote (D0289 to D0297).

Remaining notes for the lead:
- D0217's claim text mentions contract substitution but its quote covers only fees being higher than agreed; the substitution is carried by D0281. The draft cites D0217 only for the higher-fee point. Consider rewording D0217's claim.
- B0029 (another agent's fact): its claim says the housekeeping course is compulsory for Hong Kong and the Middle East, but its quote covers only the 3-day PDO; the Hong Kong / Middle East part is unverified. I removed it from my draft and kept a plain Need to know.
- OEP counts D0025 to D0028: the saved pages show only district tables and totals; the Singapore and female filters are in the fetched URL (fetch log) and the html's selected options, not in the text copy.
- The coordinator later fixed fetch.py to keep MOM page text; my MOM text copies were already rebuilt from the saved .html with momconv.py, so they are complete.
- Every id cited in the draft was checked against facts.csv after the concurrent-write warning: none missing (283 then 297 D rows present).

### Facts logged but not cited, and why

- D0036, D0049 detail duplicates; D0050, D0051 bond forfeiture and pregnancy liability (employer side); D0054 PA payout duplicate of D0052/D0082; D0072 levy start date (employer side); D0079, D0080 6ME letter and 2021 background; D0084 regulation text behind D0146; D0093 MOM rest-day hotline for employers (2022); D0148 penalty for employing without a permit (employer); D0159 High Commission Counsellor (Local) contact on the April 2025 attestation (attestation since waived); D0172 contract page title; D0179 missing worker 7-day duty (covered by D0203); D0180, D0182 levy waiver and cancellation during leave (employer side); D0195, D0197, D0198, D0202 High Commission attestation hours, NETS payment, services and the Labour & Welfare Wing address on the 2022 IPA form (attestation waived in April 2025); D0207 unlicensed moneylender reporting by employers; D0219, D0239 MDW totals from news (used MOM's own figure D0283 instead); D0243 HOME nationality chart; D0253 HOME helpdesk count; D0269 portal's total employer fee.

### Pages we could not download

- https://www.home.org.sg/helpline (404)
- https://objectstorage.ap-dcc-gazipur-1.oraclecloud15.com/n/axvjbnqprylg/b/V2Ministry/o/office-bmet/2024/12/da3db8b31cc6424dbf45fd80986a0907.pdf (BMET "A Guide for Foreign Workers Singapore"): downloaded but image-only, no text layer; not read. Ask a teammate to check whether it has a domestic-worker part.
- Facebook posts on Bangladeshi MDWs (for example facebook.com/100089505173807/posts/1039175762409253, a Bangla post on going to Singapore as an MDW) were not fetched.

## S Pass, Employment Pass, family passes, PR, changing visa type, asylum, children (prefix P)

Facts logged: P0001 to P0393 (393 rows: 364 official, 29 news/NGO). 390 are cited in `drafts/P-skilled-family-pr.md`. Unused, on purpose: P0257 (MOM's 2020 reason for the WP marriage rule: background only), P0377 (2021 MRP-era newborn passport fees, superseded by the Aug 2024 fee page), P0379 (MOM's "register within 14 days", a conflict, see below).

### Tool problems found

- **fetch.py drops `<form>`**: MOM's site (ASP.NET) wraps the whole page body in a `<form>`, so every curl-fetched mom.gov.sg page gets a 72-byte `.md` and a ~100-byte `.txt`. The saved `.html` is complete. Fix used: a scratchpad script that re-makes `sources/<name>.md` and `.txt` from the saved `.html`, unwrapping `<form>` instead of deleting it (and removing script, style, nav, header, footer, button). Quotes then check against the real page text. Suggest the lead patch fetch.py to `unwrap()` forms.
  - Side effect: on 8 Nov one call ran the script over other agents' MOM files that were then still empty (mom-faq-ea-fee-cap, mom-faq-ea-refund-6months, mom-faq-ea-refund-resign, mom-faq-marriage-pregnancy, mom-faq-passport, mom-faq-wica-leave-sg, mom-faq-wica-special-pass, mom-faq-wp-card-hold, mom-faq-wp-index, mom-wp-conditions). Their text copies now hold the full page text. No fact had been logged against them then (checked), so nothing broke.
  - Still empty and not mine, so left alone: `mom-wpe-foreign-students.md` (I cited the same page through `mom-students-work-fc`), `edb-techpass.md` (2 bytes; the `.txt` is complete and was used).
- **Concurrent writes to facts.csv**: in the first logging batch three of my rows were lost (their ids were reused) while other agents wrote at the same time. I rebuilt my label-to-id map from facts.csv after every batch and re-logged the lost facts. All P ids cited in the draft exist in facts.csv (checked with `facts.py cited`, 0 missing). The lead may want to check other agents' ids for the same problem.
- **Quote matching tip**: where a page has `**bold**` or a link right before a comma or full stop, the normaliser leaves a space before the punctuation; quotes either stop before the punctuation or include the space.

### S Pass

- Current rule (MOM S Pass eligibility page, updated 1 Sept 2026): S$3,300 minimum rising with age to S$4,800 at 45+; S$3,600 / S$5,100 for new applications from 1 Jan 2027 and renewals of passes expiring from 1 Jan 2028. Financial services S$3,800 to S$5,650 (S$4,000 to S$5,650 from 2027). Some Bangla guides (probashiapp.net) still give the old S$3,150; not used.
- "Declaring qualifications is optional" on the eligibility page. TWC2 (Nov 2025) says MOM pages from 2015 and 2018 required a degree or diploma (or a technical certificate after at least one year of full-time study) and links the change to S Pass jobs sold to unskilled first-timers: the Joy Engineering case (seven Bangladeshis from Bogura, ten lakh each, hired 2024, firms owned by a Bangladeshi couple, one a PR; one firm later in compulsory liquidation) and Forohi (twelve lakh to a cousin, S$4,008 "Supervisor" IPA, Sept 2025; actually labour supply, then a BCA skills test he failed; settled for about two-thirds of a S$20,000+ claim; went home June 2026). The Joy hiring predates the optional-qualification wording TWC2 saw in Sept 2025, so the doc does not say one caused the other.
- S Pass now also needs the 14-day MyCareersFuture advert (FCF), like the EP. Exemptions: fewer than 10 employees, S$22,500+, 1 month or less, local transferee.
- Levy harmonised at S$650 from 1 Sept 2025; quota 10% services, 15% construction, manufacturing, marine shipyard and process. No security bond. Fees S$105 application, S$100 issue. IPA 60 days.
- MOM's "Check work pass and application status" page shows salary only for Work Permit holders; an S Pass worker can't check the declared salary online, only on the IPA. TWC2 says courts enforce IPA terms as the contract.
- TWC2 practice points not all used in the doc: S Pass salary claimants get 30 days after cancellation and then a Special Pass; COE (change of employer) letters for ex-S Pass claimants are unclear even to TWC2; S Pass claimants lose the Work Permit safety net (bond, housing, food, medical, ticket).
- The BCA/MOM circular of 15 Aug 2023 (cited by TWC2) lets S Pass construction workers be moved to Work Permits without SEC(K) if paid at least S$1,600 (R1 levy); TWC2 suspects some employers plan this downgrade from the start (IPA occupation "Supervisor and general foreman (M&E)" matching the circular's list). I did not fetch the BCA circular itself; it is a lead for the Work Permit agent.
- COMPASS: MOM's EP eligibility page says EP candidates must pass COMPASS; the S Pass eligibility page lists only salary (and the quota page the quota). No MOM sentence says outright "COMPASS does not apply to S Pass"; the doc states it from the two pages.
- Bangladesh High Commission: its labour wing attests "Work Pass & Employment Pass" IPAs on the spot (page last updated Oct 2022). Whether BMET requires this for S Pass holders, and the fee, are left as Need to know (the Bangladesh-side agent covers BMET clearance).
- Searched without success (English and Bangla, news, Facebook, YouTube): what Bangladeshi diploma engineers pay for a genuine S Pass in 2026, which job titles they get, and the street price of a sold S Pass. Facebook recruiter posts (e.g. "site supervisor, Diploma/B.E. Civil, salary $1,300, shipyard, S pass") show sub-minimum "S Pass" offers, which are themselves a scam sign, but were not used as sources. Left as Need to know.

### Employment Pass and other passes

- EP qualifying salary S$5,600 (S$6,200 financial services) rising to S$10,700 (S$11,800) at 45+; from 1 Jan 2027 S$6,000 to S$11,500 (S$6,600 to S$12,700). COMPASS 40 points; C2 now 20 points for top-100 QS and similar, 10 for UK-bachelor-equivalent; a new 20-point list applies from 1 Jan 2027.
- Verification proof: MOM refuses certificates, notarised copies, school letters, HEDD, My eQuals, National Student Clearinghouse and OpenCerts screenshots. Need to know whether any Bangladeshi university has an MOM-acceptable English portal.
- EP issue fee S$225 (S$30 MJV); IPA 6 months; EPSC registration within 2 weeks.
- ONE Pass AI and Tech track opens 28 Jan 2027; EDB/MOM stop Tech.Pass applications from the same date (EDB page updated 6 Nov 2026).
- EntrePass key facts and PEP pages are dated 2024 (possibly outdated); EntrePass eligibility page is Aug 2026.

### Family passes

- DP and LTVP for EP/S Pass holders: S$6,000 (own salary); parents S$12,000; fees S$105 + S$225; 3 weeks; IPA 6 months (EP) or 2 months (S Pass). MOM's DP and LTVP eligibility pages are dated March 2024 (possibly outdated), but the S Pass eligibility page (Sept 2026) and LTVP overview (June 2026) repeat the S$6,000 and S$12,000 figures.
- DP holders lost the Letter of Consent route on 1 May 2021 (MOM PQ answer, 5 Apr 2021); DP-Work Permit is the low-salary option. Spouses of citizens and PRs on ICA LTVP/LTVP+ keep the LOC and PLOC.
- ICA spouse LTVP: S$45 + S$60 (+S$30 MJV); 6 months for a citizen's spouse, 6 weeks with a PMLA Letter of Eligibility; 6 weeks for a PR's spouse. LTVP+ for a citizen's spouse with a citizen child or pregnancy; 3+ years of marriage viewed more favourably.
- Work Permit marriage rule: MOM FAQ (28 Oct 2026) and the Fourth Schedule of the Work Passes Regulations (condition 6). Applies to current and former WP holders, including Training Work Permit; not to those now or last on EP/S Pass; 4-week decision; about 8 in 10 approved in the five years to 2020 (MOM written answer, 2 Mar 2020).
- Marriage of convenience: ICA 2019 release (penalties up to S$10,000 and/or 10 years); 2026 SGDC 158 (May 2026) shows a witness was prosecuted, and cites a case of a sham marriage arranged so a foreigner could find a job.

### PR and citizenship

- ICA PR page (30 Oct 2026): categories are SC/PR spouse, SC/PR child under 21, aged parent of SC, EP or S Pass holder, student with a national exam or IP, GIP investor. No Work Permit category. Fees S$100 + S$20 + S$50 + S$50; 6 months.
- Population in Brief 2026 (Sept 2026): 35,352 PRs and 25,094 citizenships granted in 2025. No nationality or pass breakdown is published; MOM also refuses to publish its foreign workforce by nationality (PQ answer 2021). Need to know: Bangladeshi PR grants.
- National Service: male PRs who got PR as students or through parents must serve; defaulting S$10,000 / 3 years; renouncing PR without NS harms the son's and the family's future applications.

### Changing visa type

- No conversion inside one pass: new applications by employer or ICA. WP transfer rules from MOM's construction transfer page (Sept 2026): consent any time; without consent only 40 to 21 days before expiry; new permit within 14 days of the old one ending; same sector.
- Visit pass: MOM lets employers apply for S Pass/EP while the candidate is overseas or in Singapore, but won't extend the visit pass. For a first-time Bangladeshi Work Permit holder this is the WP agent's area; left as Need to know.
- Domestic worker to a non-domestic WP or S Pass: no MOM page found. The Work Passes Regulations confine a "domestic worker" WP to household duties. Left as Need to know.
- Student to work: MOM student work exemption (16 hours a week in term, full-time in vacation, listed institutions only); ICA IHL graduate LTVP, 1 year, non-renewable, S$45.

### Asylum

- MHA AskGov (two answers, shown as updated about 5 months before 8 Nov 2026, so about June 2026): Singapore not in a position to accept asylum seekers or refugees regardless of ethnicity or origin; helps departure to a third country with UNHCR; respects non-refoulement. Same line at the UN in Nov 2023.
- UNHCR UPR submission (data to July 2020): Singapore not party to the 1951 Convention; UNHCR can register and do RSD remotely; no legal status; irregular entrants may be prosecuted and detained before deportation; one refugee and one asylum-seeker case active. No newer UNHCR figure found. Logged as `lead` (UNHCR is not a Singapore government source).

### Having a child

- **Conflict**: MOM's newborn DP page (June 2025) says register the birth "within 14 calendar days"; ICA's birth registration page (30 Oct 2026) says 42 days, with fines or jail for late registration. The doc gives ICA's 42 days (ICA administers the law and its page is newer). Logged MOM's line as P0379 (conflict). It doesn't change what a parent does if they register promptly, so no Need to know in the doc.
- ICA: LifeSG, S$18, digital certificate download within 90 days, no physical certificates since 29 May 2022, Special Pass 42 days for non-citizen babies, extension form for those without a DP.
- Constitution Art. 121(2)(c): no citizenship by birth if neither parent is a citizen.
- WP pregnancy rule: MOM FAQ (Oct 2026) and Fourth Schedule condition 7 ("during and after the validity period of her work permit"); pregnancy blood testing (Fourth Schedule) and MDW 6-monthly exam. What happens next (permit revoked, repatriation) is left to the WP and MDW agents (E and D).
- Bangladesh High Commission: newborn passport notice is a SutonnyMJ-encoded PDF (Nov 2021, MRP era), logged with `--no-quote-check` and the decoded Bangla in the note. It says the High Commission issues the baby's birth certificate through the online form on www.lgd.gov.bd, and lists the documents (45x35 mm photos then; the e-passport rules now ask for a 3R lab print under age 6). E-passport procedure page Oct 2022; fee page Aug 2024 (S$154 / S$231 for 48 pages, 5 years, general rate). epassport.gov.bd lists a mission rate for labourers and students of USD 30 / 45; whether the High Commission gives a worker's baby that rate is a Need to know.
- Not found: the High Commission's own birth-registration fee and processing time in Singapore (no page on singapore.mofa.gov.bd beyond the passport notice).

### Pages we could not download

- None. (edb-techpass converted to an empty `.md`, but its `.txt` is complete.)

### Still to do (for the lead)

- Independent verifier pass (CLAUDE.md research step 8) on this draft has not been run by a separate agent; I checked every cited id exists, and checked every number in each line against the claim or quote of the facts cited on that line (0 mismatches).

## Visit, business, student, transit and medical visas (prefix V)

Researcher V, 8 to 9 November 2026. Draft: `drafts/V-visits-students.md`. Facts V0002 to V0329 logged by V (V0001 was already logged by the lead): 328 facts, 260 from official sources (166 verified, 94 possibly outdated because undated or older than 12 months) and 68 from news, NGO, agency, airport, hospital and university pages (67 unofficial, 1 lead).

### What was searched

- **Official, Singapore:** ICA (ica.gov.sg) visa guideline for Bangladesh, Visa Guidelines, VFTF, Transit, SG Arrival Card, e-Pass, STVP extension, Visiting Singapore and fake-website advisories, consultants advisory, Student's Pass pages (application, IHL, PEI, formalities, cancellation, sponsorship), graduate LTVP and IHL list, Form 14A and V39A PDFs, SAVE e-Service landing page; about 25 AskGov (ask.gov.sg/ica) answers on visas, appeals, e-Pass and Student's Pass. MOM: student work exemption, Work Holiday Programme, Work and Holiday Visa Programme, Work Pass Exempt Activities and notification. SWDA (swda.gov.sg) private education pages: misconceptions, guide for choosing a PEI, dispute resolution, alerts; TPGateway PEI listing and enforcement actions. MOE Tuition Grant pages. MHA written PQ reply on Student's Passes 2023.
- **Official, Dhaka:** Singapore High Commission (dhaka.mfa.gov.sg) visa application page with the AVA list (updated 6 Oct 2026), visa information, LOI page, FAQ PDF (1 Jan 2025), contact page (renders no details).
- **Practical:** Saimon Global (an AVA) visa page with fees; Changi Airport and Jewel pages on transit; Mount Elizabeth (IHH) and Raffles Hospital international patient pages; NTU Student's Pass page (SOLAR steps); Straits Times (overstayers Dec 2025; TEP misuse June 2025); TWC2 TEP victim story (July 2025); The Hindu (2023, Bangladeshis on Indian passports caught at Changi); ICA press releases (2020 four Bangladeshis arrested for cleaning work; 2026 Jahangir case); TBN24 (Bangla, Sept 2025) on "verification calls".
- **Bangla searches:** সিঙ্গাপুর ভিজিট ভিসা প্রতারণা; সিঙ্গাপুর স্টুডেন্ট ভিসা প্রতারণা বাংলাদেশি শিক্ষার্থী; সিঙ্গাপুর স্টুডেন্ট ভিসায় গিয়ে কাজ পার্ট টাইম দালাল প্রাইভেট কলেজ. Results were mostly agency ads, YouTube and Facebook videos (for example a Bangladeshi consultancy's "Singapore Work-Based Diploma ... earn while you study" video), no news investigation on Singapore visit or student visa scams for Bangladeshis. English searches for fake Singapore visas sold in Dhaka also found nothing specific.

### Key findings

1. **All Dhaka applications go through 23 AVAs** listed on dhaka.mfa.gov.sg, grouped by area (Gulshan 2, Gulshan 1, Banani, Motijheel/Paltan, Banglamotor, Dhanmondi, Mirpur, Uttara). Two are medical: Parkway Hospitals Singapore's Dhaka office and MediConsult Limited. Note: the listing numbers restart in each area and contain numbering slips (for example two "1"s under Motijheel in one search snippet); the saved page lists 23 names.
2. **Real cost through an AVA:** Saimon Global page (modified 15 Oct 2026) gives Tk 2,830 visa cost (its S$30 equivalent) + Tk 1,300 service charge = Tk 4,130. A Facebook post by Bengal Travel & Tours (not saved) advertised Tk 3,780 total. The implied rate (Tk 2,830 / S$30 = about Tk 94.3) is the agent's own; not logged as an exchange rate.
3. **Processing time conflict:** ICA's Bangladesh page says 3 working days (this is ICA's e-Service time for local-contact applications); the High Commission says at least 5 working days for Dhaka applications; Saimon Global says 5 days to over a month. The draft states each for its route.
4. **Appeal routes:** the High Commission FAQ says it gives no reasons and the applicant may appeal for reassessment through the AVA; ICA's AskGov says an appeal can be filed within 1 month through the ICA enquiry form with a letter signed by the local contact, about 14 working days. Both are in the draft as two routes.
5. **Extension of stay:** Bangladesh is on ICA's list of nationalities needing a local sponsor (SC/PR aged 21+ with Singpass) to extend a short-term visit pass; apply only when 14 days or fewer remain; S$40 after 90 days plus S$30 visa fee.
6. **No visa-free transit for Bangladeshis:** VFTF is for CIS, Georgia, India, Turkmenistan, Ukraine and some PRC documents. Airside transit needs no visa or SGAC; leaving the transit area (Jewel, low-cost carriers that need re-check-in) needs a visa.
7. **SWDA replaced the earlier regulators in 2026:** ICA's PEI page now says PEIs are registered with the Skills and Workforce Development Agency (SWDA); TPGateway's enforcement list shows "SWDA" for 2026 and "SSG" (SkillsFuture Singapore) for earlier years. A third-party help page (ApplyBoard, not saved) says SWDA was formed on 1 July 2026 by merging SSG and Workforce Singapore. The brief mentioned the Committee for Private Education (CPE): that name no longer appears on the official pages saved. The doc uses SWDA.
8. **PEI students cannot work at all** (term or vacation) unless the PEI is on MOM's exempt list (DigiPen, ESSEC, INSEAD, SP Jain, TUM Asia, EHL, LASALLE, NAFA, Sorbonne-Assas and a few others). PEI graduates (except LASALLE and NAFA) are not on ICA's IHL list for the 1-year graduate LTVP.
9. **Student's Pass for Bangladeshis:** IHL processing within 2 weeks (visa-required nationals); IPA letter includes a single journey visa (NTU page); S$45 + S$60 + S$30.
10. **Training Employment Pass abuse** (ST, TWC2, 2025): a Bangladeshi paid about S$15,000 to a Bangladeshi fixer for a TEP sold as a route to a Work Permit; insiders say some PEIs act as fronts. Used in the student scams section; the TEP itself belongs to the work-route sections (other agents).

### Conflicts and doubts

- **Passport endorsement:** the High Commission page (6 Oct 2026) still tells visitors to check the "arrival visit pass endorsement" on the passport (V0004). ICA says since 11 March 2022 there is no endorsement and the e-Pass comes by email (V0042). ICA's version used; V0004 left uncited.
- **Single vs multiple journey:** Form 14A offers single, double, triple and multiple journey visas; the HC FAQ says MJV is not guaranteed. The Student's Pass IPA includes a single journey visa (NTU), and the S$30 MJV is paid at formalities (ICA).
- **"Verification calls":** TBN24 (Bangla, 10 Sept 2025) reported mandatory phone or video verification calls for Singapore visa applicants from 2025. No ICA, MOM or High Commission page says this; it reads like a rewrite of an unsourced web article. Logged as "lead" (V0138) and used only in a Need to know.
- **Visit pass length:** no official page gives a standard number of days (30 days is commonly cited by agents). Left as Need to know.
- **Medical visa:** ICA has no separate "medical visa"; the HC FAQ speaks of a medical visa needing an LOI from the medical industry, and the STVP page lists medical treatment as a visit purpose. Treated as the ordinary entry visa with a hospital LOI.

### Facts logged but not used, and why

- V0004 (HC passport endorsement): outdated against ICA (see above).
- V0029 (HC LOI page header), V0034 (apply at the Mission or its AVA), V0101 (AskGov AVA question): duplicates of facts cited.
- V0046 (VFTF cannot be extended): irrelevant, VFTF closed to Bangladeshis.
- V0149 (Saimon passport delivery hours): minor; could be added to Visit visa Step 4.
- V0165 (WPEA entry still assessed at checkpoint): duplicate of visit rule.
- V0190 (digital STP replaced cards from 27 Feb 2023): trivia.
- V0207 (STP holders may work if MOM requirements met): covered by MOM facts.
- V0261 (graduate must obtain LTVP to stay): covered by V0267.
- V0284 (false immigration ads referred to ASAS): low value for migrants.
- V0288 (cancel STP on completion): duplicate of V0280/V0266.
- V0260 (extra attachments in term need a work pass): too detailed for the target reader.

### Pages fetched but not registered or not used

- `ica-stvp` (curl of the short-term visit pass URL redirected to the e-Pass page; duplicate of `ica-epass`).
- `ica-entry-requirements`: interactive checker; no quotable text.
- `sghc-dhaka-home`, `sghc-dhaka-contact`, `sghc-dhaka-updates`: no usable text (contact details load by script). The High Commission's address (Ventura Avenue, 5th floor, CWN(C)-8/B Gulshan Avenue) appears only in third-party pages and an MFA travel advisory reprint; not logged.
- `mom-wpe-foreign-students`, `mom-misc-work-pass` (curl, near-empty); replaced by Firecrawl copies (`mom-students-work-fc`). Miscellaneous Work Pass page not re-fetched.
- `ica-stp-sponsorship`: only says local sponsors are needed for government schools and ITE; not relevant to Bangladeshi university or PEI students.
- `nus-ug-tuition-2026` (NUS fees PDF AY2026/27): the pdftotext layout scrambles the fee table, so fees can't be matched to faculties reliably. Someone should read the PDF visually: international students with the Tuition Grant appear to pay about S$21,000 to S$23,000 a year for most courses, and without it about S$36,000 to S$44,000 (to be checked before use).
- `swda-pe-resources`, `ica-advisory-visiting-singapore` (partly used), `askgov-ica-visa-contact` used.
- `valencia-singapore-visa`: 404.
- `nus-solar-user-guide` (curl): blocked by Incapsula, empty files; the same PDF was saved through Firecrawl as `nus-solar-guide-fc` (NUS user guide, accurate as of 5 Oct 2026) and used for the SOLAR steps.
- `bhrrc-tep-workers-2025` (Business & Human Rights Resource Centre): 403, not retried.

### Pages we could not download

- https://dhaka.mfa.gov.sg/contact-us/ (curl and Firecrawl both return the page without the address, phone and email).
- https://valenciabd.com/singapore-visa (404).
- https://www.business-humanrights.org/en/latest-news/singapore-migrant-workers-from-india-bangladesh-myanmar-on-training-employment-passes-subjected-to-rights-violations-incl-14-hour-workdays-denial-of-leave/ (403).
- https://www.facebook.com/bengaltravelandtour/posts/... (Bengal Travel & Tours Tk 3,780 post; Facebook, not attempted).

### What happens in practice (evidence found)

- AVAs ask for more than the official list: air ticket booking, hotel booking, bank statement and solvency certificate (Saimon Global).
- ICA raids keep finding visitors working on expired social visit passes (ST, Dec 2025) and Bangladeshis doing cleaning work without passes (ICA 2020).
- No source found on refusal rates for Bangladeshi visit visas, entry refusals at Changi, or the price of "visit visa with job" packages in Dhaka: all left as Need to know.

### Open questions (also in the draft as Need to know)

- AVA service charges other than Saimon Global; any cap.
- Bank balance expected for a visit visa and for a Student's Pass.
- Whether the Bangladesh High Commission in Singapore issues LOIs for tourists.
- Days usually granted to Bangladeshi visitors at Changi.
- Whether the High Commission phones or video-calls applicants.
- Number of companions allowed per patient; whether hospitals sponsor extensions.
- Dhaka prices for "work-based diploma" or "study and work" Singapore packages; Bangladeshi Student's Pass numbers by PEI.
- SWDA's complaint channel (the feedback portal link service-portal.swda.gov.sg/s/feedback appears on its site but no text describes it).

## Bangladesh side, money, going home, coming home, contacts (prefix B)

Draft: `drafts/B-bangladesh-side.md`. Facts B0001-B0320 in `facts.csv` (320 rows: 280 official, 40 news/NGO/company).

### Sources copied from the Qatar folder

66 Bangladesh-side sources copied from `countries/qatar/sources/` (OEP guide, BMET and Ministry charters, welfare-fee circular, PCC, e-passport, MOFA apostille directory, HCCH table, WEWB service pages, JBC leaflet transcription, PKB pages and charter, NRCTA circular, WEDB, upension, NBR baggage rules transcription, HSIA customs, Bangladesh Bank remittance cost and top-30, BRAC pages, two news items). Each was logged with `fetch.py --log <original url> <name> manual` and registered with the Qatar metadata. 177 facts re-quoted from those copies (B0001-B0177); each note says "Re-quoted from Qatar <id>". Statuses were recomputed against the 2025-11-08 cutoff.

Bangla quotes from image-only PDFs (BMET charter, BMET leaflet, Ministry charter, PKB pages, welfare-fee circular) were added with `--no-quote-check`, carrying the Qatar row's note that the quote was transcribed from the page image. They were not re-read from the image in this session: the machine has no PDF renderer (no pdftoppm, no PyMuPDF) and the Read tool cannot render PDFs without poppler.

Status fixes after copying: B0034 (welfare-fee circular, Tk 5,500 from 1 Oct 2026) and B0040 (WEWB membership, Tk 6,500 equivalent) set to verified; their Qatar "conflict" was with Doha-specific embassy pages that don't apply to Singapore.

### Biggest findings

1. **IPA attestation abolished.** The Bangladesh High Commission's notice of 18 April 2025 (No. 19.01.6501.103.36.051.25) says the Government waived IPA attestation from 18 April 2025 (Ministry memo 49.00.0000.048.11.017.21.119 of 17 April 2025) (B0287, B0288). The High Commission's 2022 welfare page still describes IPA attestation, its hours and its authorisation-letter format (B0182, B0183, B0185, B0186): those are logged but superseded; the draft cites only the hours/welfare services, not attestation as current.
2. **No police clearance in MOM's Work Permit documents.** MOM's "Apply for a Work Permit" page (Sept 2026) lists passport, immigration document, declaration form, security bond form and educational qualifications "if required" (B0229). I grepped every saved MOM WP and MDW page for police/clearance/criminal record: nothing. The PCC procedure is kept in the draft only for workers who are asked for one. Need to know asks whether agencies still ask.
3. **Apostille works for Singapore.** HCCH: Singapore acceded 18 Jan 2021, in force 16 Sep 2021 (B0220); MOFA Bangladesh lists Singapore (no. 95) among the 114 countries that accepted Bangladesh's accession (B0221, B0222). Whether MOM accepts an e-Apostille on educational certificates is not stated anywhere I found: Need to know.
4. **Government cost cap for Singapore: Tk 2,62,270**, training included, highest of 16 countries (Bangladesh Bank survey report, Jan 2019, Table 5.1: B0273-B0275; Prothom Alo English 2018: B0276). FE (March 2017) shows the Bangladesh mission's Tk 260,000 proposal and its breakdown (B0277, logged, not used in the draft). I did not find the Ministry's own notification (around 2016-2017); a newer Singapore cap was not found. Aug 2026: State Minister Shama Obaed says the target is Tk 3 lakh maximum and real costs are Tk 10-14 lakh (B0278, B0279).
5. **Hundi to Bangladesh is prosecuted in Singapore.** SPF Sept 2024 release names two dormitory hundi operators sending to Bangladesh (B0251, B0252); MOM/SPF April 2026 Norris Road case, S$38.6 million (B0254, B0255). PSA s5(1) penalty S$125,000 / 3 years (B0250). Money mules: caning up to 12 strokes since 30 Dec 2025 (B0258).
6. **POSB Payroll Account rules** (company page, logged as lead): one DBS/POSB account per Work Permit holder, S$7,000 daily limit, frozen after the WP ends and the worker leaves (B0238-B0245). MOM requires bank payment for dormitory residents (B0236).
7. **Deceased workers:** High Commission NOC process (May 2026) with full document list and flowchart (B0192-B0197); employer bears repatriation (B0232, B0233); WEWB pays when no employer (B0284), Singapore wing allocation Tk 1 lakh for bodies and Tk 5 lakh for stranded/detained workers in 2023-24 (B0285).
8. **Overstay:** Immigration Act s15(3) penalties (B0261, B0262); ICA: deported and barred (B0292); a Bangladeshi case (Pabel, 2021: 1 month + 3 strokes, deported, barred; employer 12 months, May 2026) (B0295-B0297); Special Pass holders must report to ICA's repatriation branch (CNA, B0304); No-Boarding Directives from 30 Jan 2026 (B0298).

### Conflicts and readings

- PCC fee: Tk 1,500 on the portal (B0014) vs Tk 500 in Bangladesh Police guidance (B0018). Kept as Need to know.
- Welfare fee: Tk 5,500 (B0034, rule) vs BMET charter Tk 3,500 (B0035, superseded).
- Airport desk numbers: WEWB page (B0131-B0133) vs BMET charter (B0134). Need to know kept.
- Customs: USD 10,000 (B0145/B0155) vs USD 5,000 (B0146); jewellery wording (B0140/B0148/B0149); late declaration 30 days (B0147) vs 7 days (B0152). Need to know kept.
- **Remittance cost, two measures:** Bangladesh Bank's survey (B0218): Singapore up to USD 200 = 2.51% (Jan-Mar 2026) and 1.76% (Apr-Jun 2026). pdftotext shifts BB's Table 2 down one row; the Qatar agent read the page image and took Qatar = 4.55/5.11, so Singapore = the values printed on the "Italy" line. World Bank RPW (Aug 2025, S$260): 6.54% average including exchange-rate margin (B0271, B0272). The two differ in method (WB includes FX margin against a market rate); both shown, no Need to know.
- WB RPW page values are run together by Firecrawl as SGD+USD pairs (e.g. "3.373.37" = 3.37% / 3.37%; "5.003.85" = S$5.00 / USD 3.85). Per-firm numbers in B0272 were parsed from lines ~580-2025 (S$260 tab).
- Workers in Singapore: High Commission (Oct 2026, per BMET) about 135,000 (B0204); State Minister (Aug 2026) about 150,000 (B0280). Not used in my sections; for the Background.

### What happens in practice (evidence found)

- High Commission, Oct 2026 (B0205): workers complained orally about high costs and pay at 3 meetings; asked for written complaints with proof; none filed. Used in the cost paragraph.
- 2026 bankruptcies: about 240-250 workers unpaid; High Commission took it to MOM; about 250 re-employed (B0207, B0208). Other agents have bdnews/Daily Star Bangla items on the same case (bdnews-sg-unpaid-230-2026, dsbangla-sg-unpaid-230-new-jobs-2026).
- Prothom Alo Oct 2026 (B0314-B0317): 4,060 bodies Jan-Sep 2026; 66% "natural"; irregular workers' bodies take much longer; WEWB pays body costs for cleared/registered workers, Ministry budget otherwise.
- Agency practice for Singapore clearance (Jakwan Travels, Oct 2026; B0289-B0291): IPA, passport, BMET registration, district fingerprints, PDO certificate for first-timers or old clearance-stamp page for returnees.

### Facts logged but not used in the draft, and why

- B0043, B0049 (BMET GRS ladder, middlemen warning): generic; the Work Permit section owner may use them.
- B0074 (BB all-country cost averages): replaced by Singapore-specific figures.
- B0173 (WEWB membership through missions, 176,895 cards): covered by B0040.
- B0175-B0177 (Ministry complaint routes for agencies and harassment of women): belong in the scams/complaints sections.
- B0185, B0186 (IPA attestation fees/authorisation letter): superseded by the April 2025 waiver.
- B0204, B0280, B0281, B0219 (worker numbers, remittance volumes): for the Background.
- B0209 (BCA skilled test at Bangladesh OTCs ends January 2028), B0210 (Secretary on the OTC-centred agency syndicate), B0212 (IPA tied to company and occupation): for the Work Permit / costs owner. B0209 is important: the High Commission says it will cut what workers pay brokers.
- B0277 (FE 2017 cost breakdown), B0282 (MOFA Migration Wing): context.
- B0309 (report immigration offenders to ICA): not needed.

### Searches that found nothing usable

- A PKB loan specific to Singapore: none on pkb.gov.bd, mygov, or in news; PKB migration loan (max Tk 3 lakh) applies. A Facebook page claims PKB loans "up to Tk 5 lakh": not on PKB's own page, not used. Agrani Bank's ALOW loan (Tk 50,000-3 lakh, 11.90%) added (B0312, B0313).
- Singapore-specific death statistics for Bangladeshi workers: WEWB annual report 2023-24 gives only all-country totals (4,745 bodies) and mission allocations; Prothom Alo Oct 2026 gives Saudi and Malaysia but not Singapore. Need to know kept.
- Nagad's Singapore partners: Nagad's partner table is paginated by JavaScript (7 pages) and only page 1 rendered. Remitly SG and 6GPay advertise Nagad transfers (search snippets only; not logged). Need to know kept.
- ICA repatriation branch address/hours and what happens on surrender: no ICA page found; CNA case only. Need to know kept.
- Length of re-entry bans for deported overstayers: ICA says "barred" without a period. Need to know kept.

### Pages we could not download

- High Commission PDFs: general information for workers (July 2025): https://objectstorage.ap-dcc-gazipur-1.oraclecloud15.com/n/axvjbnqprylg/b/V2Ministry/o/office-singapore-mofa/2024/12/b2b6d83338f640d897f5c5ad96f10b99.pdf and e-passport fee PDF: .../2024/12/7d99011e0e2542c687bec194f1ad93f0.pdf (both image PDFs; Firecrawl returned ERR_ADDRESS_UNREACHABLE once; saved as PDFs with empty text copies: bdhc-sg-worker-info-general-pdf, bdhc-sg-passport-fee-pdf).
- MOM FAQ "How do I open a bank account for my migrant worker?" https://www.mom.gov.sg/faq/work-permit-for-foreign-worker/how-do-i-open-a-bank-account-for-my-foreign-worker (renders empty with curl; saved as mom-faq-wp-bank-account with no text; not used).
- Nagad partner table pages 2-7 (JavaScript pagination).
- Daily Sun (403 with curl; Firecrawl copy saved as dailysun-cost-3lakh-shama-2026-fc).
- WEWB annual report 2023-24: Bijoy-encoded text layer; quotes B0284 and B0286 decoded/copied by hand with --no-quote-check (notes explain).

### Saved files to tidy (for the lead)

- `sources/mom-pr-2026-unlicensed-remittance` is in `_fetchlog.csv` but its files were deleted (curl copy was empty); the Firecrawl copy is `mom-pr-2026-unlicensed-remittance-fc`.
- `sources/nagad-remittance` likewise: log entry without files; use `nagad-remittance-fc`.
- `sources/bdhc-sg-home.*` was fetched but not registered (index page only).

## Final audit (KG, 10 November 2026)

- JBC insurance leaflet: the 10% row (row 6 of Schedule C), the end of the 15% row and the note on death after partial disability were missing from the saved transcription, though the facts B0112 and B0113 quoted them. Checked against the page image of the scanned leaflet (countries/qatar/sources/wewb-jbc-insurance-leaflet.pdf, PDF page 1, top left): the rows are there as quoted. Added them to sources/wewb-jbc-insurance-leaflet-transcription.md; both quotes now match. The doc's 10% line stands.
- Hundi penalty: E0218 (MOM handy guide, undated: S$100,000, 2 years) conflicts with B0250 (SPF, Sept 2024, Payment Services Act s.5: S$125,000, 3 years). The doc now uses B0250; E0218 kept only for "permit revoked".
- Pages not found: MOM's EntrePass appeal page (two URL guesses 404; no appeal page linked from the EntrePass pages); www.techpass.gov.sg did not load. EDB's Tech.Pass application page saved via Firecrawl (curl copy had an empty text layer).
- Remittance series still unreconciled: Bangladesh Bank's monthly country table gives Singapore US$87.71 million for July-September 2026 (about US$350 million a year), against the US$1.49 billion for FY2025-26 the doc cites (C0127). Someone should confirm which series is right before the doc quotes either as a trend.
- SIM cards: only a 2022 CNA report (IMDA quoted) found for the three-prepaid-card limit and ID scanning; no current IMDA page saved.

## Fact-check and audits (9-10 November 2026)

- Six independent verifiers (fact prefixes KA to KF) checked every sentence and number in `doc.md` against its cited source, in six parts; their change lists are in `verify/part1-report.md` to `verify/part6-report.md`. Main kinds of error fixed: numbers taken from the wrong row or year, conditions dropped ("only for", "unless"), one case stated as a general rule, out-of-date rules (IPA attestation stopped on 18 April 2025; ECT filing steps), wrong or swapped citations, and claims about nationality the source does not make.
- A final auditor (prefix KG) ran the three CLAUDE.md audits (the migrant's questions, the original aim per visa, the insider test), filled steps, scams and help for every pass, and pruned duplication; its checklist is in `verify/audit-report.md`.
- Facts: 2414 logged, 2000 from official sources.
- Lower-confidence facts: several Bangladesh-side figures (JBC insurance tiers, Ministry and BMET charter contacts, WEDB rates, the pension flyer, baggage rules) are quotes transcribed from image-only Bangla PDFs, many first transcribed for Qatar; this machine could not render the PDFs to re-check every one against the page.
- Open conflicts not resolved in the doc: Bangladesh Bank's remittance series (US$1.49 billion for 2025-26 against quarterly figures); MOM pages on the maximum age at application (62 or under 62) and on the no-consent transfer deadline (7 or 14 days); the birth-registration deadline (MOM 14 days, ICA 42 days).
