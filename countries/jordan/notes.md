# Jordan: research notes

Merged from the six research parts (A Background, G and H factory work visa, D domestic and other work, V other visas, R money, return and contacts). Fact ids carry the part's letter.

## Part A

### Jordan: research notes (agent A, Background and intro)

Research date 9 Nov 2026. Fact ids like [A0012] point to rows in this folder's facts.csv. The draft states each fact once; conflicts, research narration and facts left out are recorded here.

#### What was searched

- **BMET / OEP numbers.** OEP's country-clearance page (oep.gov.bd/reports/country-clearance) returns only the query form to a plain fetch (the pre-saved `oep-country-clearance-2025` is that form, registered as [A0013]). The data comes from the page's own JSON request: same URL with `draw=1&start=0&length=-1&approval_date_from=...&approval_date_to=...`, sent with the session cookie and `X-Requested-With: XMLHttpRequest`. Adding `&gender_id=2` gives women only. Saved for 2022-2025 and 2026 to 8 Nov, all and women (`oep-cc-json-*`). Jordan's country_id is 88.
- OEP holds only 74 Jordan clearances for 2022 (64,912 total that year), so OEP is incomplete before 2023 [A0012]; years 2015-2024 in the draft come from BMET's annual table image (Jordan column transcribed by me into the copied `bmet-annual-by-country-2025-05-img.md`) and the women's table image (Jordan column added to `bmet-female-employment-by-country-annual-img.transcription.md`). Both crops were read at 2x-2.5x.
- BMET and OEP disagree slightly for overlapping years: 2023 BMET 8,626 vs OEP 8,618 (women 7,838 vs 7,809); 2024 BMET 15,413 vs OEP 15,410 (women 13,772 vs 13,760). The draft uses BMET for 2015-2024 and OEP for 2025-2026, as Qatar does.
- Derived shares (not in any source, computed from cited facts): women 92.4% of 2026 clearances (12,784/13,829), 89.1% in 2025 (11,913/13,375); Jordan's share of women cleared 19.1% in 2025 (11,913/62,355) and 23.6% in 2026 to 8 Nov (12,784/54,221). Men 2026: 1,045; 2025: 1,462.
- **BMET permission letters.** BMET's miscellaneous-information search for "Jordan" and "জর্ডান" (current and archived) returns "কোনো তথ্য পাওয়া যায়নি" [A0162, A0163]: letters are titled by RL number. The agencies list (agencies/activity.csv, built from the full download) counts 28 Jordan letters 2023-2025: BOESL RL0147 27 letters / 15,584 workers, Al-Sourav Overseas RL1028 1 letter / 100. I saved and cited two: BOESL's 20 Jul 2025 letter for Jerash Garments [A0100-A0102] and Al-Sourav's 2023 letter (Ministry page transcribed by agent G) [A0084-A0086]. The draft does not state the 27/28 count because it rests on the agencies dataset, not a saved source quote; the assembler may link to the Recruiting agencies doc, Jordan section.
- **Agencies named.** BOESL (state-owned; agencies.csv flags: ACC's Jul 2026 57-agency records request, an inquiry not a charge; ILO 2018 broker allegations). Al-Sourav Overseas named only as the holder of the cited 2023 permission (no flags in agencies.csv). Surah Travels and Traders (no licence) named from CID's arrest [A0156, A0160]. Bangladesh Export Corporation and Just Way Aviation appear only as the sources of Recruitment Advisor reviews [A0096, A0099]; the draft does not name them, because the reviews are mixed and unverified.
- **BOESL.** Notices via agent G's saved copies (Tusker, Nov 2026; 5,000-women notice, Mar 2026); Prothom Alo report of the Jul 2026 Tusker notice; BSS interview with BOESL's MD (Feb 2026); Daily Star on BOESL's 2023-24 annual report; FE 2022 (cost revision) and 2023 (departures halved). BOESL's own notices site search (boesl.gov.bd/pages/notices) for Jordan/জর্ডান returns nothing; Jordan notices sit under pages/reports.
- **Jordan side.** mol.gov.jo, cbj.gov.jo and petra.gov.jo do not respond from here (curl 000 / 522). MoL's Comprehensive Guide (3 Jul 2025 edition) and Regulation 90 came from agent D's Wayback copies. The 9 Jun 2026 edition of the guide has no Wayback capture. Jordan Times blocks direct fetch (403); some articles came via Wayback.
- **Searches with nothing usable for Bangladeshis:** Jordan-Israel border crossings (only Sri Lankans and unnamed migrants reported); Jordan work permits by nationality 2025-26 (open data portal only 2019-2020); Bangladesh Embassy Amman labour-wing complaint figures; WEWB Jordan data; HRW/Amnesty/Solidarity Center 2024-26 Jordan reports specific to Bangladeshis; "free visa" sales for Jordan in Bangla news (only the Surah Travels case).

#### Conflicts between sources

- **Garment minimum wage history.** IFPRI (2023) says the garment minimum was JD 220 with about JD 125 left after in-kind deductions [A0093]; BWJ says the 2023 CBA's JD 220 was kept until the 2025 CBA raised it to JD 230 (JD 130 cash + JD 100 in kind) [A0023]. Not a conflict once dated; the draft gives the 2025 figures only.
- **Salary currency in BMET/BOESL papers.** BOESL's March 2026 notice says JD 130 basic [A0018]; the Nov 2026 Tusker notice says USD 183.35 [A0072]; the Jul 2025 BMET letter says 183.61 with no currency (USD by size) [A0100]; Prothom Alo reports the Tusker basic as Tk 22,500 [A0083, not cited]. JD 130 at the dinar's fixed rate is about USD 183. The draft gives the JD and USD figures as each notice states them.
- **Returnees.** The Nov 2026 Tusker notice says workers who have been abroad are not taken [A0076]; Prothom Alo's report of the July 2026 Tusker notice says only former Tusker workers could re-apply. Different notices; the draft cites the official one only. Owner of the step (G) should check.
- **Regularisation deadline.** Earlier MoL statements (R's sources) gave 30 Sep 2026 with the deportation flag from 1 Oct; the later ones give 1 Dec 2026 with the flag from 1 Jan 2027 [A0134-A0136]. The draft uses the later dates; R owns the procedure.
- **Dinar peg.** The 0.709 JD per USD figure is widely quoted but no saved source states it (CBJ site unreachable; UPI 1995 and Arab News 2005 blocked). Kept as Need to know; money line uses BOESL's JD 1 = Tk 170 [A0018].
- **Source dates I registered wrongly (sources.csv cannot be edited by tool):** `jt-min-wage-290-wb` registered 2024-12-23, published 2024-12-16; `mamlaka-dec1-call` registered 2026-10-01, page says 03-11-2026; `mamlaka-month-left-dec1` registered 2026-11-01, page says 28-10-2026; `mamlaka-212702-500jd` registered undated, page says 14-10-2026; `ds-boesl-two-countries` registered 2025-01-01 (following agent G), real date not visible. The fact rows carry the correct dates. Assembler: fix in the merged sources.csv.

#### What happens in practice

- BOESL's route is the main one and on paper near-free (Tk 400 refunded), but workers still report spending Tk 40,000-60,000 (passport, medical, urine/pregnancy test, Dhaka trips) [A0089], and brokers sell "help" with the sewing test [A0104, A0087]. BWJ shows pregnancy testing of recruits still found in 18% of factories in 2024 [A0029, not cited in draft; G may use it].
- Men are a small share (about 1,000-1,500 a year by OEP), mostly factory jobs through private agencies at a permitted cost (Tk 1,74,300 in Al-Sourav's 2023 letter) far above BOESL's women's route.
- Domestic work: Bangladeshi women were the largest group in 2014-2017 (about 30,000-50,000) and the largest group leaving employers [A0147, A0150, A0149]; current numbers unknown. Bangladesh's 2025 rule bars agencies from charging women domestic workers [A0106], but reviews show Tk 20,000-1,20,000 paid [A0096].
- Jordan's June 2026 recruitment stop exempts exactly the two jobs Bangladeshis go for (garments in zones, domestic work), which is consistent with 2026 clearances already above 2025.
- BWJ, the only regular inspector publishing factory-level compliance, paused on 22 Jun 2025 [A0048].

#### Facts logged but left out of the draft, and why

- A0002 (2026 all-country total), A0010 (OEP 2023 total), A0012 (OEP 2022 incomplete), A0013 (OEP form page): background to the numbers; noted above.
- A0020's "84,100" kept; A0021 kept; A0028 (zero-fee policy since 2019), A0029/A0030 (pregnancy tests, J-GATE request): belong to the garment visa steps and scams (G).
- A0042 (5% quid-pro-quo harassment): A0043 covers the reporting fear; kept one.
- A0050-A0052 (TBS 2021: Jordanian buyers come weekly; Classic, Aseel, Rainbow test at TTCs; Classic has most Bangladeshi women): useful for G's Step 1; 2021, so left out of Background.
- A0056 (BOESL 94,787 by mid-2023), A0064 (BOESL started 2010): superseded by A0061 and A0065.
- A0063 (employer-pays model): duplicated by BOESL's own notice [A0071].
- A0068/A0069 (BOESL 2022 cost revision; garment charges unchanged): older than the 2026 notices.
- A0077, A0079 (test dates/places): G's steps.
- A0083 (Tk 22,500 basic, Prothom Alo): official JD/USD figures used instead.
- A0086 (agency must report each group's arrival to the embassy): G's steps.
- A0093 (IFPRI JD 125 in hand at the old JD 220 minimum): superseded by the 2025 CBA.
- A0098 (Tk 60,000, promised salary not paid): one review; kept the range.
- A0105 (why women choose Jordan: network, low fees): could go in In one minute; cut for length.
- A0107 (Tk 15 lakh agency deposit for women domestic workers): D's section.
- A0131-A0133 (May 2025 stop): A0131/A0132 cited; A0133 (inspections for "ghost" workers) left for D/H.
- A0137 used; A0141/A0142 used.
- A0144 used; A0145 used; A0152 replaced by A0174 (exact quote for "pardon").
- A0157 used.
- A0158 used.

#### Open questions (kept in the draft as Need to know)

- CBJ's official dinar-dollar rate.
- Whether MoL reopened recruitment after 1 Jun 2026; Iran-war effect on BOESL flights and issued visas.
- BOESL vs private-agency share of 2025-26 women; how many men go and to which jobs.
- BMET age limits for Jordan garment jobs (women) and any Jordan job (men).
- Bangladeshis with valid Jordanian permits by sector; MoL nationality data 2025-26.
- Any Bangladesh-Jordan labour MoU.
- Broker prices for BOESL test places in 2026; Dhaka agencies supplying Jordanian domestic-worker offices and what offices pay them.
- "Free visa" sales for Jordan and price; who issues free work permits in 2026.
- BMET's current maximum migration cost for Jordan through private agencies.
- Typical 2026 take-home with overtime; getting social security back on leaving; dormitory crowding and food.
- QIZ worker leaving early: ticket and re-entry ban.
- Embassy labour-wing complaint data 2025-26; who inspects factories since BWJ paused.
- Attempts to cross into Israel or move to Europe; treatment of deportees on arrival in Dhaka.

#### Pages we could not download

- https://jordantimes.com/news/local/govt-suspends-recruitment-of-non-jordanians-across-most-sectors (403; no Wayback capture; covered by Al Mamlaka and Al Jazeera)
- https://jordantimes.com/news/local/jordan-boost-private-sector-minimum-wage-jd290-2025 (403; saved via Wayback as jt-min-wage-290-wb)
- https://jordantimes.com/node/354975 (403; no capture; 2021 domestic-worker nationality numbers: 7,009 Bangladeshi of 52,221 documented women domestic workers, per search snippet only)
- https://jordantimes.com/news/local/labour-ministry-reports-rising-complaints-experts-urge-urgent-reforms (403; no capture)
- https://jordantimes.com/news/local/organisation-reports-abuse-workers-qiz-garment-factories (403; no capture)
- https://jordantimes.com/news/business/labour-ministry-launches-worker-status-regularisation-drive-through-sep-30 (403; no capture)
- https://jordantimes.com/node/384189 (403)
- https://www.petra.gov.jo/en/news/labour-ministry-freezes-foreign-worker-recruitment-to-prioritize-local-employment (522)
- https://mol.gov.jo/EBV4.0/Root_Storage/EN/EB_Info_Page/Comprehensive_Guide_for_issuing_work_permits_9-6-2026.pdf (no connection; no Wayback capture)
- https://www.cbj.gov.jo/ (no connection; needed for the official peg)
- https://en.phenixcenter.net/the-jordan-labor-watch-welcomes-the-decision-to-raise-the-minimum-wage-to-290-jordanian-dinars/ (no connection)
- https://www.jagonews24.com/en/biz-econ/news/78346 ("BOESL's workforce market stuck in Jordan", 403)
- https://www.business-humanrights.org/en/latest-news/ms-and-next-demand-answers-from-under-armour-and-columbia-over-factory-abuse (403; Apr 2024 suicide of Bangladeshi worker Tureza Akter at Fine Apparel/Needle Craft, per search snippets; MoL report reportedly found suicide due to supervisor mistreatment; BWJ's "tragic suicides" [A0035] is the cited stand-in)
- https://www.business-humanrights.org/fr/dernières-actualités/jordan-migrant-garment-workers-will-bear-the-brunt-of-the-us-tariffs-unionist-says-wpftc/ (403; 2025 US tariff threat to garment jobs)
- https://www.newarab.com/features/migrant-workers-reveal-exploitation-jordans-textile-industry (empty page; Wayback download failed; reportedly says Bangladeshis ranked first in Jordan's labour market in 2024 at 12.8%)
- https://mail.thefinancialexpress.com.bd/trade/living-wage-remains-elusive-for-bds-female-apparel-workers-in-jordan-1572237274 (no connection)
- https://www.arabnews.pk/node/1957936 (403; 2021, garment pay USD 260-360)
- https://www.arabnews.com/node/275041 and https://www.upi.com/Archives/1995/11/23/Jordan-pegs-dinar-to-US-dollar/7677817102800/ (403; peg figures)
- https://thewire.in/labour/despite-labour-laws-south-asian-workers-suffer-in-jordans-billion-dollar-industries (saved but empty shell; not cited)

## Part G

### Jordan: research notes, part G (Work visa: garment and factory worker, first half)

Researcher G, 9 Nov 2026. Fact ids G0001-G0219 in `facts.csv` (this folder). Sections drafted in `draft.md`: the H2 lead, Who pays what, Steps 1-6, Scams. Bangladesh-side procedures (OEP, TTC, passport, PCC, PDO, BMET clearance and fees, insurance, PKB loan, flight, WEWB membership from abroad) are written here in full; other parts should link to them.

#### Sources and how they were read

- **BOESL notices (boesl.gov.bd), the core official source.** The "Jordan employment notice" page (published 9 Nov 2026) links five PDFs dated 8-9 Nov 2026: Sana Garments, United Creation, Mas Al Safi, Prestige Apparel, Tusker Apparel. All are scans with garbled or no text layer; I rendered each page with PyMuPDF and transcribed Sana, United, Prestige and Tusker in full into `sources/<name>.transcription.md` (quotes are checked against these). Mas Al Safi was read from the image (100 women machine operators, flatlock/overlock/feed-off-the-arm, JD 130, age 20-35) but not transcribed or cited. The March 2026 "5,000 women at no cost" notice is a JPEG; fetch.py saved it as `.html` (binary) with junk text copies, which I deleted; the image is copied to `boesl-jo-2026-03-urgent-img.jpg` and transcribed. The Jan 2026 "Classic garments" JPEG (`boesl-jo-2026-01-classic-img.jpg`) was saved but not read or cited.
- **BOESL online portal.** `boesl-brms-flowchart-pdf` (26 Nov 2024) gives the 7 steps for brms.boesl.gov.bd (transcribed). A BOESL notice of 11 Oct 2026 says the portal is closed for all applications because of a technical fault. Prothom Alo and BSS (Jul 2026) report a Tk 100 online application fee for the Tusker notice.
- **BMET permission letters.** BMET's miscellaneous-information list (all 7 pages saved, `bmet-misc-infos-p1..7-of7`) titles letters by memo and RL only, so a search for জর্ডান or Jordan returns nothing (saved as `bmet-misc-search-jordan[-bn]`, empty). The shared agency list (`agencies/activity.csv`, built by extracting every letter) shows 28 Jordan letters 2023-2025: 27 BOESL (RL0147, 15,584 workers) and 1 Al-Sourav Overseas (RL1028, 100 male machine operators, Friends Apparels, Aqaba). I saved and read three: BOESL/Jerash (20 Jul 2025), BOESL/Needle Craft (21 Apr 2025), Al-Sourav (7 Nov 2023). BOESL's letters are one typed BMET page only (no Ministry page, no cost cap). Al-Sourav's includes the Ministry's scanned permission (31 Oct 2023), transcribed: JD 125, 3 years, free food, housing, medical and airfare both ways, and a cost cap of Tk 1,74,300. The 27-letter count is not cited in the draft because it comes from the shared agency extraction, not a source saved here; the assembler can cite it from `agencies/` if the doc's background needs it.
- **Jordan MOL.** mol.gov.jo did not connect from here (timeout). The "Comprehensive Guide of Principles for Issuing Work Permits for Non-Jordanian Workers" (3 Jul 2025 version, amended to May 2025) came from the Wayback Machine (`mol-comprehensive-guide-2025-07`, 7,264 lines). Read: garment sector clauses (VIII), recruitment from abroad (X, XI), fee regulation No. 142/2019 as amended 2025 (XXVII), general recruitment instructions 2012 (XXVIII), QIZ instructions 2007 (XXIX). The newer 9 Jun 2026 guide (mol.gov.jo/.../Comprehensive_Guide_for_issuing_work_permits_9-6-2026.pdf) could not be saved (no Wayback capture).
- **Jordan MOI visas.** MFA Jordan's 2023 notice (Wayback) says all e-visas are issued through eservices.moi.gov.jo; Deloitte (Jul 2023) lists work visa and work residency among the MOI e-services. No official page on how a worker checks a work visa.
- **Better Work Jordan Annual Report 2025** (ILO/IFC; covers Jan 2024-Jan 2025; dated by its statement that BWJ paused on 22 June 2025). Logged as non-official.
- **ILO 2018**, "Recruitment experiences of South Asian migrant workers in Jordan's garment industry" (fieldwork 2015), read in full for the Bangladesh section; two-column PDF, so quotes are single-line fragments. **IFPRI 2023** discussion paper (phone interviews with 26 women returnees) read for recruitment, costs, wages.
- **Bangladesh-side sources** were copied from `countries/qatar/sources/` (BMET charter, safe migration leaflet, Ministry charter and welfare-fee circular, OEP, PKB, police PCC, e-passport, WEWB, the 2013 Act and 2023 amendment). Facts reused from Qatar's ledger keep the same quote. For Bangla PDFs with garbled text layers the Qatar/Malaysia researchers had transcribed quotes from page images and logged them with `--no-quote-check`; I did the same, noting the Qatar id. I re-checked the two fee sources visually: BMET charter p.2 (welfare + insurance Tk 3,500 + 1,000, smart certificate Tk 250, source tax Tk 400/250) and the Ministry circular of 20 Sep 2026 (welfare fee Tk 3,500 to Tk 5,500 from 1 Oct 2026). Both match.

#### Conflicts between sources

- **Welfare fee:** BMET charter (30 Sep 2026) still shows Tk 3,500; the Ministry circular raises it to Tk 5,500 from 1 Oct 2026. The draft uses Tk 5,500 (newer, Ministry). For BOESL recruits the employer pays it anyway.
- **Worker-paid items on BOESL notices differ by notice:** fingerprint Tk 220 (Sana) or Tk 200 (United, Prestige, Tusker); PDO Tk 305 (Sana, United, Prestige) or Tk 200 (Tusker); undertaking stamp Tk 500 on Sana and United only. United says the employer repays these in Jordan; Tusker says before departure. BSS and Prothom Alo (Jul 2026) say "Tk 1,000 medical and Tk 220 PDO and fingerprint", a garble of the notice.
- **PDO fee:** BMET charter says the institute sets it; BOESL notices print Tk 305 or Tk 200.
- **Age band:** 20-35 (Prestige, Tusker, March 2026 call) vs 21-39 (Sana, United).
- **Returnees:** Prestige and Tusker (Nov 2026) say "returnees not taken", while Tusker's July 2026 notice (per Prothom Alo/BSS) was only for its former workers, and both Nov notices also give priority to returnees from war-torn countries. The draft states the difference; insiders may know the logic (factory preference).
- **PCC fee:** Tk 1,500 (portal) vs Tk 500 (police guidance), carried over from Qatar; kept as Need to know.
- **Wage promised vs paid:** IFPRI (2023) JD 125-150 promised vs JD 99-130 paid; the 2025 sector agreement sets JD 130 cash minimum for migrants. BMET letters show 130.0 and 183.61 (USD, matching notices of USD 183.35-183.43, i.e. JD 130 converted).

#### What happens in practice

- Most women learn of Jordan through relatives and ex-colleagues; many still go through brokers who charge for a free route (IFPRI 2023; ILO 2018). ILO 2018: dalal fees Tk 65,000-130,000; alleged bribery of BOESL interviewers with a nail-polish signal; workers told by the dalal to deny paying.
- Total spend for BOESL recruits 2022-23: Tk 40,000-60,000, some Tk 80,000 (passport, medical, urine test, fingerprints, shopping); a "bank draft" deposit (Tk 10,000 in 2015) was refunded after 1-3 months in Jordan. The 2026 notices no longer mention a bank-draft deposit.
- Touts work the crowds at the Mirpur/Shyamoli TTCs; Oct 2026 raid (20 detained, Tk 5-10 lakh taken). June 2026 CID case: Surah Travels forged Jerash Garments' name; the factory complained through the Embassy.
- Pregnancy testing of recruits: J-GATE (Jordan Garment, Accessories & Textiles Exporters' Association) asked the Bangladesh Embassy and BOESL to stop; 18% of factories still cited in 2024.
- Age falsification is a known practice (ILO 2018; BWJ 2024 child-labour cases with falsified passport birth dates).
- Contract in English, not read to the worker; 11-12 hour days; deductions; dorm problems (66% of factories non-compliant on accommodation in 2024).
- Better Work Jordan paused on 22 June 2025 (funding cut). A Petra report (Sep 2026) of a new 18-month ILO-Jordan garment initiative turned up in search but the page returned 522 and could not be saved.

#### Facts logged but left out, and why

201 of 219 facts are cited. Not cited:

- G0039 (Needle Craft letter: 100 machine operators at 130, 15 quality supervisors at 400): supervisor pay; useful for Background part 3.
- G0043, G0051 (Ministry permission text for Al-Sourav; fees not to fall on the worker): duplicate cited conditions.
- G0066 (QIZ garment is a closed sector, transfers only between garment employers): belongs to part H (changing employer).
- G0070 (Bangladesh Embassy on MOL's embassy list): trivia.
- G0078 (2024: eight factories cited for fees, mostly subcontractors; Indian workers most likely to pay): background.
- G0094 (a neighbour advised the broker route): colour; the broker scam is covered.
- G0098, G0199, G0216 (2015 BOESL fees Tk 14,000-25,000 with a refundable "bank draft" deposit; BOESL's Jordan rates unchanged in its 2022 revision): history, superseded by the 2026 notices; useful for Background part 3.
- G0101, G0103, G0104 (2022: 300 a week; extra cost for some high-skill posts; Tk 28,000-30,000 with overtime): background, part A.
- G0128 (penalty on an agency appointing an unregistered sub-agent): the worker-facing penalty G0127 is enough.
- G0156 (brokers are often friends and family, TBS 2024): general, Background.
- G0169, G0170 (clearance for a self-found visa and its Tk 250 smart card fee): Jordan garment visas come through BOESL or an agency; kept for part D/V if a self-found Jordan visa route is written.
- G0196 (complaint against an agency that sent a worker without permission): kept for part H/R.

#### Open questions (kept in the draft as Need to know)

- OEP registration fee; PDO booking click path (carried from Qatar).
- Who pays the JD 50 surcharge on the work permit.
- Current government ceiling for Jordan for private agencies.
- TTC sewing courses and whether BOESL accepts the TTC certificate in place of its test.
- Whether walk-ins need an application while brms is closed.
- F/H/M/A/O meaning on BMET letters; where BMET posts Jordan letters now.
- Whether Jordan/BOESL require a PCC for garment workers.
- How a worker checks a Jordan work visa on eservices.moi.gov.jo; whether Bangladesh is a "restricted nationality".
- Embassy Amman attestation of demand letters (papers, fee, time); whether a worker can verify a demand there.
- Whether BMET's visa check covers Jordan.
- Bangladesh medical centres for Jordan and what they test; whether pregnancy tests continue in 2026.
- What the fingerprints are for.
- The worker's undertaking text.
- Whether JBC job-loss cover excludes BOESL workers.
- Arrival at Queen Alia: who meets BOESL groups, what to show.
- Jordan medical: tests, cost, who pays, unfit outcome.
- Wages by cash/bank/e-wallet; SIM card.
- Arrival orientation since BWJ paused; whether the Al-Hassan Workers' Center is open.

#### Cross-links assumed (for the assembler)

- "Your rights at work", "Your work and residence permits", "If something goes wrong" (part H); "If a worker dies, is injured or loses the job" (part R). Steps 1-5 here are the Bangladesh-side procedures other parts (domestic worker, other work permits) should link to: OEP Step 1 item 1; TTC Step 1 item 2; agency licence and permission letter Step 1 item 6; passport and PCC Step 2; PDO, clearance, fees, insurance Step 4; PKB loan and flight Step 5; WEWB membership from Jordan Step 6 item 8.
- Embassy address/phone is repeated in Step 6 for convenience; the full contact block is part R's.

#### Pages we could not download

- https://mol.gov.jo/EBV4.0/Root_Storage/EN/EB_Info_Page/Comprehensive_Guide_for_issuing_work_permits_9-6-2026.pdf (mol.gov.jo times out from here; no Wayback capture). The July 2025 version was used instead.
- https://www.risingbd.com/national/news/426554 (403): "পোশাক শ্রমিক রপ্তানিতে আপত্তি মালিকদের" (Bangladeshi RMG owners object to sending garment workers abroad, 2026).
- https://www.business-humanrights.org/en/latest-news/jordan-south-asian-migrant-workers-face-overcrowded-dormitories-surveillance-and-strict-employer-control-in-garment-factories/ (403).
- https://www.jagonews24.com/national/news/1128040 (403): Jordan job lure, fake company names.
- https://jordantimes.com/news/local/report-calls-promoting-decent-work-digitising-wages (403): 2021 survey of garment wage payment by cash, bank and e-wallet.
- https://www.petra.gov.jo/en/news/jordan-ilo-launch-18-month-initiative-to-strengthen-labor-standards-in-garment-sector-2 (522).
- https://help.unhcr.org/jordan/... work permit FAQ (not attempted after search; gives a JD 85 medical figure for Syrians at migrant-worker health centres, not applicable to QIZ workers without confirmation).

## Part H

### Jordan, agent H: research notes (second half of Work visa: garment and factory worker)

Research date 9 November 2026. Fact ids [H0001]-[H0255] are in `facts.csv`; sources in `sources.csv` and `sources/`. The draft covers: Your rights at work; Your work and residence permits; What can get you jailed or deported; If something goes wrong; Changing employer or leaving.

#### What was searched

- **Labour Law text.** MOL's English PDF (`labor_law_En.pdf`) times out from here; saved from the Wayback Machine (`mol-labour-law-en`). It is an old translation (pre-2019: e.g. Art. 12 fines of JD 100-150 a month, no Art. 29 harassment clause, Art. 53 fine JD 25-100), so it is cited only for articles unchanged since. The current consolidated Arabic text was taken from Jordan-Lawyer (`jordan-lawyer-labour-law-ar`, "with all amendments including 2026"), a private legal site; facts from it are logged as `lead`. No official consolidated Arabic text could be downloaded: mol.gov.jo refuses connections (ECONNREFUSED / timeout), moin.gov.jo's PDF timed out, the Legislation and Opinion Bureau (lob.gov.jo) is a JavaScript app. Same for the Passports Law, Penal Code, Cybercrime Law 2023, Narcotics Law and Social Security Law (all from Jordan-Lawyer, `lead`).
- **MOL official pages** via Wayback: hotline page (`mol-hotline`, gives the Hemayah link complaint.hemayeh.jo), FAQ (`mol-faq`), the 2025 garment CBA news (`mol-cba-2025`), Hemayah minimum-wage complaints news (`mol-hemayah-2025`), Wage Authority 2024 news (`mol-wage-authority-2024`), heat-wave notice (`mol-heat`), Better Work continuation (`mol-bw-continuation`). The MOL footer "last modified" date is site-wide, not the article date; page dates were set from the article content.
- **MOL comprehensive work-permit guide** (`mol-permit-guide-2025`, updated 22 May 2025, 148 pages). Its Arabic text layer is unreadable (fonts without Unicode mapping), so pages were rendered to images and read: contents, pp. 55-56 (garment sector), 88-91 (transfer between sectors, renewals), 94-97 (clearance, absconding report, permit cancellation, SSC no-objection), 111-113 (Work Permit Fees Regulation 142/2019 as amended), 114-123 (Instructions on employing non-Jordanians 2012, selected articles), 127-134 (QIZ Instructions 2007). Facts from it are logged with `--no-quote-check` and the page and Arabic wording in the note. Pages 4-54, 57-87, 98-110, 135-148 (definitions, occupation lists, Syrian/Egyptian/Gaza rules, special skills) were not read in full because they do not concern garment workers; a reader with time should check pp. 82-87 (recruitment from abroad and replacement workers) for G.
- **Garment sector:** Better Work Jordan Annual Report 2025 (read in full); BW statement on the June 2025 pause; the Unified Work Contract for Migrant Workers (2023 version, from a Jerash Holdings SEC filing; SEC blocks the default user agent, saved with curl and logged `manual`); Jadaliyya dormitory study (March 2025); BHRRC/iNews on Fine Apparel and Tureza Akter (April 2024); Fibre2Fashion on Achilles Apparel (Feb 2024); Jordan Times on the 2025 minimum wage, the JD 230 CBA, Tamkeen's 2024 complaints and the 2018 Al Hassan complaint.
- **Residence, deportation, regularisation:** Jordan News (2025-2026) on the Residence and Foreigners Affairs Law amendment (JD 1.5 to JD 3 a day), PSD's fine statement, the November 2025 deportation statement and the 2026 regularisation exemptions; Jordan News on SSC's June 2026 online "Permanent Departure" claim.
- **Bangladesh side:** WEWB list of labour wings (Wayback) for the Amman labour wing contacts.
- Searches in English, Bangla (জর্ডানে পোশাক শ্রমিক) and Arabic (منصة حماية، العمالة الوافدة، براءة ذمة، تبليغ فرار).

#### Conflicts between sources

- **Garment minimum wage in-kind part:** BWJ says the 2025 CBA fixes JD 100 in kind and at least JD 130 cash [H0019]; Jadaliyya says of the January 2025 JD 10 rise only JD 5 went to cash [H0024] and quotes a Bangladeshi worker with JD 95 deducted [H0025]. Kept BWJ's rule and Jadaliyya's practice; the 2026 figure is a Need to know.
- **SSC lump sum for departing foreigners:** MOL's FAQ says a non-Jordanian can "recover the contributions deducted" [H0099]; the SSC Law Art. 70(b) formula (10% of total insured wages per year for 120 contributions or fewer) applies to anyone leaving coverage under the regulations [H0100]. Whether final departure counts as such a case under the SSC regulation was not confirmed: Need to know in the draft.
- **Strike fine:** an older report says JD 2 a day; the current Labour Law Art. 136 says at least JD 50 the first day and JD 5 a day after [H0166]. The law was used.
- **Hemayah languages:** an Intaj (developer) page says 9 languages; Jordan Times (Dec 2022) says 10 were planned. Neither saved; whether Bengali is offered is a Need to know.
- **Better Work Jordan status:** BW says operations paused on 22 June 2025 with no staff in Jordan [H0113]; MOL's undated statement says it "will continue" [H0116]; a Petra report (August 2026, from search results only, not saved) says the Cabinet raised government funding to JD 5 million for three years. Need to know in the draft.
- **Transfer rules:** the 2012 Instructions' six-month rule [H0143] is general; the garment sector is a "closed sector" allowing moves only within it [H0141]. Whether the six-month rule applies to QIZ workers was not confirmed.

#### What happens in practice (beyond the doc)

- Better Work Jordan 2024 findings (in the doc): overtime cap broken in 54% of factories, migrants 59 h/week, accommodation non-compliance 66%, passport confiscation in three factories, forced resignations and repatriation despite valid contracts, termination papers not in the worker's language. BWJ also notes Indian workers were most likely to have paid recruitment fees (not used; recruitment is G's part).
- Jadaliyya (2025): employer-appointed "camp leaders" report on workers; women "sent home" for curfew breaches, relationships, theft accusations; kidney problems rumoured to end contracts ("having to travel"). In the doc.
- Fine Apparel (Needle Craft), Tureza Akter's suicide (Nov 2023), strike by workers, supervisor and two managers sacked; brands investigated. In the doc. BWJ (2024) mentions "tragic suicides" and a late-2023 case of "illegal retention of workers" without naming factories.
- Achilles Apparel (2022-2024): embassy labour wing negotiated 18 months; 454 Bangladeshi workers got wages and SSC pay in Feb 2024; Fibre2Fashion says MOL to cover airfares (not logged). In the doc.
- Al Hassan (2018): factories let permits lapse for months or years; workers trapped by overstay fines. In the doc as an older example.
- No report was found of a 2023-24 strike by Bangladeshi garment workers ending in deportation; the 2011 Maintrend case (413 Bangladeshi women sent home after a strike, Financial Express) was found in search results only and not saved, so not used.

#### Facts logged but left out, and why

- H0018 (factory clinics), H0159 (late-renewal exemption): duplicates of facts cited.
- H0080 (most line workers are young Bangladeshi women), H0119 (84,100 workers, half of migrants Bangladeshi), H0118 (51% of assessments by labour inspectors alone): corridor background, for A.
- H0104 (SSC online claim tied to the June-September 2026 regularisation window): used as a Need to know question instead.
- H0129 (QIZ employers must file a certificate that the worker paid no recruitment fee beyond legal ones): recruitment, for G's Step on costs/scams.
- H0145 (renewal only when an SSC block is on the employer): minor.
- H0195, H0196: superseded by the exact-number facts H0251-H0253.
- H0198 (106 minimum-wage complaints on Hemayah in early 2025), H0229 (ILO recommendation on Hemayah): statistics/opinion with no bearing on what a worker does.
- H0244 (employer notifies the embassy within 24 hours and pays repatriation of a dead worker's body): belongs to R's "If a worker dies, is injured or loses the job".

#### Cross-links assumed (for the assembler)

- "the steps for this visa" (G) for costs paid in Bangladesh and recruitment.
- Work visa: domestic worker (D) for excluded domestic workers.
- Family residence (V).
- If a worker dies, is injured or loses the job; Going home without valid papers; Coming home; Contacts (R). Contacts should carry the Ministry in Dhaka (Welfare-1) and the Welfare Board legal-help route, which H points to rather than repeats.

#### Pages we could not download

- https://mol.gov.jo/EBV4.0/Root_Storage/EN/EB_HomePage/labor_law_En.pdf (direct; saved via Wayback instead)
- https://www.moin.gov.jo/ebv4.0/root_storage/ar/eb_list_page/قانون_العمل_رقم_8_لسنة_1996_وتعديلاته.pdf (timeout)
- https://www.mol.gov.jo/ and https://complaint.hemayeh.jo/ (connection refused from here; MOL pages taken from Wayback)
- https://jordantimes.com/news/local/minimum-wage-textile-sector-raised-jd230-under-new-labour-contract, .../jordan-boost-private-sector-minimum-wage-jd290-2025, .../ssc-enforce-minimum-wage-compliance-across-kingdom-details-exemptions (403; saved via Wayback)
- https://business-humanrights.org/en/latest-news/jordan-over-400-bangladeshi-garment-workers-receive-owed-wages-social-security-pay (403, no Wayback capture; Fibre2Fashion used instead)
- https://www.business-humanrights.org/en/latest-news/jordan-south-asian-migrant-workers-face-overcrowded-dormitories-surveillance-and-strict-employer-control-in-garment-factories/ (403, no capture; the Jadaliyya original was saved)
- https://petra.gov.jo/GetSimple/index.php/en/news/cabinet-quadruples-better-work-funding-to-jod-5m-in-major-push-for-garment-sector (522, no capture)
- https://wewb.portal.gov.bd/pages/static-pages/6922dd2c933eb65569e13cc0 (timeout; saved via Wayback)
- https://businesspostbd.com/national/454-bangladeshis-in-jordan-receive-due-wages (returned a hosting-company page, not the article; the saved file is not used)

#### Open questions (all in the draft as Need to know)

Take-home pay in 2026; electronic wage payment rule; public holiday list; heat and dorm standards; health insurance; SSC contribution check and lump-sum formula; union field offices; BWJ restart; permit and residence online check and residence fee; home leave and re-entry; lost passport procedure; Hemayah in Bengali; Tamkeen contacts; anti-trafficking hotline; Workers' Centre status; deportation during a pending case; checking and contesting an absconding report; six-month transfer rule for QIZ; real transfer frequency; SSC online claim after the 2026 window; debts and travel bans.

## Part D

### Jordan, part D (domestic worker; other work permits): research notes

Research date 9 Nov 2026, agent D. Fact ids like [D0012] point to rows in `facts.csv` in this folder. The draft states each rule once; conflicts, research narration and facts left out are recorded here.

#### What was searched

- Jordan Ministry of Labour (mol.gov.jo): the site does not answer from this machine (TCP timeouts on port 443 on every try). Everything official from MOL was taken from the Wayback Machine with `wayback.py`, after listing MOL's English and Arabic upload folders through the Wayback CDX index. Found and saved:
  - Comprehensive Guide for issuing work permits, English, last edition 3 Jul 2025 (`mol-guide-2025-07`), read in full for the sections used (definitions, closed and restricted professions, sector table, recruitment from abroad, replacement, transfers between sectors, renewal, clearance, desertion notice, cancellation, guarantee, Syrian permits, fee regulation, 2012 recruitment instructions, Syrian instructions, specialised skills, day-labourers' free permit).
  - The same guide in Arabic, last updated 20 Aug 2026 (`mol-guide-ar-2026-08`, Wayback capture 26 Sep 2026). pdftotext gives no Arabic; a PyMuPDF dump with reversed word order is saved as `sources/mol-guide-ar-2026-08.mupdf.txt` and used for quotes. Checked pages 1-3 (contents), 7-8 (closed and restricted professions), 82 (recruitment from abroad), 88-89 (transfers), 95 (desertion), 111-112 (fees), 147-148 (free permit). These confirm that the 2025 English rules are still current in Aug 2026, with two additions: a JD 700 permit fee for building services workers (fee regulation No. 90 of 2025) [D0112], and a Feb 2026 note on Gaza residents in cleaning and loading jobs (not used).
  - Regulation No. 90 of 2009 on domestic workers and its amendments, English (`mol-reg90-domestic`), read in full.
  - Regulation No. 63 of 2020 on domestic-worker recruitment offices, English (`mol-reg63-offices`), read in full.
  - MOL's Arabic guidance leaflet on the domestic workers sector (`mol-dw-sector-ar`, 11 pages, Wayback capture Nov 2025, file uploaded Apr 2025). Text layer unusable; read page by page from rendered images and hand-transcribed into `sources/mol-dw-sector-ar.transcription.md` (Arabic with English gloss). This is the source of the per-nationality recruitment cost (Bangladesh JD 2,200 / JD 1,700 fee-exempt) [D0005, D0006].
  - MOL service card "replacing a domestic worker" (1 Aug 2024) (`mol-dw-replacement`); Arabic text reversed, dump saved as `sources/mol-dw-replacement.mupdf.txt`; three facts logged with --no-quote-check and the Arabic in the note [D0069, D0070, D0071].
  - Labour Law No. 8 of 1996 (English), copied from agent H's folder with its fetchlog row (`mol-labour-law-en`).
- Bangladesh side: reused from Qatar the housekeeping training policy, the 1 Sep 2025 approval of 21 agencies for women domestic workers, WEWB safe house page, BMET and Ministry citizen charters, PKB women's loan, BMET safe-migration leaflet, OEP agency list. Quotes are the Qatar ones; garbled-PDF facts keep --no-quote-check with the Qatar note.
- Bangladesh Embassy Amman (amman.mofa.gov.bd): home, address, contact and visa pages. No labour-wing page, no housemaid attestation page, no safe-home page. Consular PDF (2023 hours notice) saved but text is garbled and not used.
- News and NGOs: Jordan Times (blocked by 403; all via Wayback), Jordan News, Roya, Al Mamlaka, Arabi21, Zawya (Jordan Times copy), Daily Star, Dhaka Tribune, Prothom Alo, TBS, BSS, The New Nation, ARIJ, ILO, ILO Recruitment Advisor, US TIP report 2025 (ecoi.net copy), UNHCR Jordan help page (Wayback), Tamkeen contact page.
- Searches in English, Bangla (জর্ডান গৃহকর্মী, জর্ডান ফ্রি ভিসা) and Arabic (كلفة استقدام عاملة بنغالية، تصريح العمل المرن، إيقاف الاستقدام، نظام العاملين في المنازل).

#### The big findings

- **Recruitment freeze from 1 June 2026.** MOL suspended recruitment of foreign workers in all sectors, exempting only domestic workers, garments in development zones/QIZ/free zones, and specialised-skill professions; earlier approvals still processed [D0091-D0095]. The official MOL decision text was not found (MOL site unreachable; Petra page returned 522 and has no Wayback capture). Cited from the Jordan Times (via Zawya) and Arabi21. Even before it, the Aug 2026 guide allowed recruitment from abroad only for zone garments, domestic workers, specialised skills, JPMC-contracted agri firms and replacement of departing workers [D0096, D0097]. So for Bangladeshi men there is effectively no legal new route into construction, agriculture, cleaning, bakeries etc. This matters for agent A (Background "Is it open now") and G (garments are exempt).
- **The day-labourers' free permit is only for workers already in Jordan** (Aug 2026 guide, p.147) [D0118]; JD 800 + JD 50 [D0121]. It cannot be a migration route from Bangladesh, which is the key fact against the "free visa" sale.
- **2026 regularisation** (Cabinet decision, ends 1 Dec 2026): 50% waiver of past permit fees, full waiver of fines, JD 500 lump sum for those who entered as visitors, deportation flag from 1 Jan 2027, and new transfer rules for absent domestic workers [D0175-D0183]. Only news (Al Mamlaka) found; the Cabinet decision PDF on aci.org.jo would not download. Agent R (Going home without valid papers) should use this; I cite it only where it touches domestic workers and other permits.

#### Conflicts and uncertainties

- **Recruitment cost for a Bangladeshi housemaid:** MOL leaflet JD 2,200 (JD 1,700 fee-exempt) [D0005, D0006], undated (uploaded about Apr 2025); Roya 2018 gave JD 2,050 (not cited in draft, logged in source roya-dw-cost only as context). Doc uses MOL's.
- **Regulation 63, Art. 15(B) (guarantee period):** the English translation is ambiguous on whether the refund/replacement applies to all refusals or only to the listed exceptions. Logged as D0064 but not cited; the draft uses MOL's leaflet instead (refund within 14 days if ill, pregnant or runaway within 90 days; replacement for refusal, unfitness, runaway) [D0233, D0016].
- **Bank guarantee per worker:** the 2012 instructions (Art. 5) require JD 300 per worker of a "restricted nationality" for any recruiting employer [D0138]; section XXII of the same 2025 guide says the guarantee applies to establishments with more than 30 non-Jordanian workers. Unresolved; doc cites the instructions. Whether Bangladesh is a "restricted nationality" under the Residence Law is a Need to know.
- **Work-permit fee for domestic workers:** the fee regulation says JD 350 for all sectors except garments, free permits and building services [D0113]; I found no separate domestic-worker fee in 2025-26 texts, so the draft gives the household cost only through MOL's per-nationality total. Older press quoted JD 500 for domestic workers (not saved).
- **Free-permit fee history:** JD 1,500/2,000 cut to JD 700/900 during the 2019 grace period [D0230]; now JD 800 for all four types [D0121]. Doc gives the current figure only.
- **July 2024 domestic-worker transfer mechanism:** known only from the 2025 TIP report [D0167, D0168]; the regulation text itself was not found. The MOL leaflet (Apr 2025) still says domestic workers cannot change sector [D0018]; the June 2026 Cabinet decision allows it after two years without a permit [D0177]. Doc states both in date order.
- **Bangladeshi housemaid numbers:** Tamkeen 2021: 7,009 documented Bangladeshi women domestic workers [D0150]; 2020 Daily Star: 75,000 women and 25,000 men (all sectors) [D0188]. Not comparable; most Bangladeshi women in Jordan are in garments.

#### What happens in practice (sources)

- Nazma Begum case (Daily Star, Oct 2020): broker chain from Moheshpur to Faridpur, Tk 50,000, sold in Amman, embassy rescue after ASK letter; the Paltan agency owner named Zahidul declined to name his agency; broker claimed to use "JSK Recruiting Agency, Fakirapool" (not named in the doc: allegation without outside evidence).
- 15-year-old girl sent in 2017 via MH International with passport age 27 (Dhaka Tribune 2018); doc names the agency because the source reports it as a registered agency used, attributed and dated.
- Tamkeen: 730+ complaints 2020-22; 291 women's complaints in 2022 (114 passport); about 30,000 undocumented domestic workers.
- TIP 2025: Dar Karama capacity 35 (20 women); 133 served in 2024; hotline lacks Asian-language interpreters; victims pressured to drop complaints; only 4 domestic workers changed employer without consent; MOL inspected 63 recruitment offices, suspended 9, closed none [D0170, not cited].
- Permit trade (Egyptians): JD 900 to JD 3,100 paid to brokers, passports held by brokers; farm permits sold JD 300-500 (ARIJ 2018) or JD 500-1,000 (2010 Labour Observatory study, in ARIJ).
- Egyptian day labourers at Sweileh: JD 20-30 a day.

#### Facts logged but left out of the draft, and why

- D0064 Reg. 63 Art. 15(B): ambiguous translation (see conflicts).
- D0068 Reg. 63 public office list: duplicate of MOL leaflet D0014.
- D0095 Arabi21 exemptions: duplicate of D0092.
- D0098, D0099 replacement of a departing worker: whether it survives the June 2026 suspension is unknown; kept as a Need to know.
- D0153 Tamkeen 2021-22 document complaints: duplicate of D0155.
- D0157 MOL platform 2024 complaint numbers, D0170 office inspections, D0174 500,000 undocumented, D0165 detention: statistics with no bearing on a step; D0165 duplicates D0166.
- D0169 MoU comparison (Philippines MoU guarantees a base wage, most others do not): relevant to the Bangladesh wage gap; left for the Background writer (A).
- D0172 Egyptians pressured to pay recruitment fees: Egyptian-specific.
- D0173 social security withdrawal needs employer consent: belongs to R (money and leaving).
- D0191, D0192 detail of the 2017 child case (uncle took wages; BRAC safe home): trimmed as detail.
- D0194 BOMSA 2019 complaints: small, old statistic.
- D0206 2016 plan for a MOL domestic-worker shelter: no evidence it opened.
- D0209 211,000 women 2004-Apr 2025 (all sectors): for Background (A).
- D0213 OKUP "free visa" survey (Gulf, not Jordan).
- D0224 ILO RA: violations most common in agriculture and domestic work: generic.
- D0228 placeholder lead for Egyptian permit share: the JT 2023 article does not carry the 124,974 figure in the saved text; not used.
- D0230 2019 free-permit fees: history.

#### Cross-links the assembler must fix

- I pointed to "Work visa: garment and factory worker" by step name, not number: "the OEP registration step", "the agency step", "the BMET clearance step", "the loan step". Replace with G's step numbers.
- Domestic-worker "Leaving Jordan" mentions the MOL clearance certificate (2019 rule) [D0207]; R's "Going home without valid papers" and H's "Changing employer or leaving" should be consistent with it.
- The 2026 regularisation facts (D0175-D0183) overlap R's section; keep one full statement there and link.

#### Open questions (Need to know in the draft: 19 bullets in 14 blocks)

All are in `draft.md`. The most important for an insider: whether BMET currently clears women to Jordan as housemaids and through which agencies; the agreed wage for Bangladeshi housemaids; whether the Embassy attests housemaid contracts; whether the Amman safe house operates; which body takes free-permit applications in 2026; whether Bangladesh is a "restricted nationality"; and what Bangladeshi men actually pay.

#### Pages we could not download

- https://mol.gov.jo/EBV4.0/Root_Storage/EN/EB_Info_Page/Comprehensive_Guide_for_issuing_work_permits_9-6-2026.pdf (MOL unreachable; no Wayback capture; the Arabic 20 Aug 2026 guide was used instead)
- https://mol.gov.jo/ebv4.0/root_storage/ar/eb_list_page/إصدار_تصريح_العمل_لأول_مرة_للعاملين_في_المنازل_(استخدام_من_داخل_المملكة).pdf (Wayback download failed)
- http://mol.gov.jo/EBV4.0/Root_Storage/AR/EB_Info_Page/تعليمات_العمل_المرن.pdf (Wayback download failed)
- https://mol.gov.jo/ebv4.0/root_storage/en/eb_list_page/instructions_for_the_year_2021_insurance_policy_instructions_for_non-jordanian_domestic_workers_for_the_year_2021.pdf (no capture)
- https://mol.gov.jo/ebv4.0/root_storage/en/eb_list_page/instructions_for_offices_working_in_the_recruitment_of_non-jordanian_domestic_workers_2004.pdf (no capture)
- https://www.mol.gov.jo/EBV4.0/Root_Storage/EN/EB_List_Page/Regulation_No_(19)_of_2021_Regulation_of_Agricultural_Workers_Issued_pursuant_to_Paragraph_(B)_of_Article_(3)_of_the_Labor_Law_No_(8)_1996.pdf (no capture)
- https://www.petra.gov.jo/en/news/labour-ministry-freezes-foreign-worker-recruitment-to-prioritize-local-employment (522; no capture)
- https://jordantimes.com/news/local/govt-suspends-recruitment-of-non-jordanians-across-most-sectors (403; no capture; Zawya copy used)
- https://jordantimes.com/news/local/new-labour-policies-boost-local-employment-end-foreign-hiring-municipalities-sanitation (403; no capture)
- https://jordantimes.com/news/local/tamkeen-calls-restoring-domestic-workers’-right-resign (Wayback download failed)
- https://jordantimes.com/news/local/stakeholders-discuss-recruitment-domestic-helpers (Wayback download failed)
- https://jordantimes.com/news/local/labour-ministry-launches-worker-status-regularisation-drive-through-sep-30 (no capture)
- https://aci.org.jo/UploadFiles/قرار قوننة وتوفيق اوضاع العمالة الوافدة.pdf (2026 Cabinet regularisation decision; connection failed)
- https://www.albawaba.com/news/jordans-runaway-domestic-workers-are-stranded-legal-limbo-1053560 (403)
- https://daleel-madani.org/node/165197 ("For a fee", Coventry study on recruiting Bangladeshi women for Jordan and Lebanon; 403)
- https://help.unhcr.org/jordan/?p=2074 (403; English page saved from Wayback instead)
- https://www.agbi.com/employment/2026/06/jordan-halts-expatriate-hiring-to-boost-local-employment/ (405)

## Part V

### Jordan, part V (non-work visas, visa change, asylum, children): research notes

Research date 9 November 2026. Fact ids like [V0012] point to rows in `facts.csv` in this folder. Sections written: Visas not open to Bangladeshis; Visit visa; Entry without prior approval (Gulf residents, Schengen/US visa holders); Tourist visa (with religious visits); Family residence (with marrying in Jordan); Family visit; Business visit; Transit; Student visa and study residence; Medical treatment visa; Investor and residence by investment; Exit and return visa; Changing visa type; Asylum; Having a child in Jordan.

#### How the sources were got

- **moi.gov.jo refuses connections from here** (ECONNREFUSED / timeout from both curl and WebFetch). Every MOI page was taken from the Wayback Machine: the HTML pages with `wayback.py`; the MOI "service cards" (.docx and Arabic .pdf files under `/ebv4.0/root_storage/.../eb_list_page/`) by downloading the archived original bytes (`web.archive.org/web/<ts>id_/<url>`) and logging them with `fetch.py --log <original-url> <name> manual`, then registering them as `--official archived`. The archive URL and timestamp of each manual download are below.
- **The Arabic MOI PDFs have no usable text layer** (pdftotext gives empty or scrambled Arabic). I read them as page images and logged their facts with `--no-quote-check`, quoting the Arabic as transcribed from the page and naming the page in the note. These are V0110-V0115 (family residence), V0125-V0127 (study residence), V0148-V0151 (investment residence). A teammate should re-check those quotes against the PDF.
- Bangladesh-side e-passport pages (`epassport-fees-fc`, `epassport-instructions-fc`) were copied from `countries/qatar/sources/` with their fetch-log rows, as the brief allows for Bangladesh-side pages.
- My mistake, fixed: my first manual download attempt saved Wayback error pages as `.docx`/`.pdf` and logged six names in `sources/_fetchlog.csv` (moi-guide-tourist-visa, -transit-visa, -treatment-visa, -joining-family, -bank-deposit-residence, moi-ar-study-residence). I deleted those files and removed those six rows from my own `_fetchlog.csv` with a script before re-downloading them correctly. No other log row was touched.

Manual Wayback downloads (name, archive URL):
- moi-guide-visit-visa: https://web.archive.org/web/20240603033741/https://moi.gov.jo/ebv4.0/root_storage/en/eb_list_page/service_card.docx
- moi-guide-tourist-visa: https://web.archive.org/web/20240603033853/ (…/eb_list_page/تاشيرة_السياحةtourist_visa.docx)
- moi-guide-transit-visa: https://web.archive.org/web/20240603033745/ (…/transit_visa_تأشيرة_المرور.docx)
- moi-guide-treatment-visa: https://web.archive.org/web/20240603033815/ (…/treatment_visa_تأشيرة_العلاج.docx)
- moi-guide-joining-family: https://web.archive.org/web/20240603033740/ (…/التحاق_بعائل_joining_family.docx)
- moi-guide-bank-deposit-residence: https://web.archive.org/web/20240603033728/ (…/اقامة_سنوية_بموجب_وديعة_بنكية_annual_residence_visa_with_bank_deposit.docx)
- moi-guide-exit-return: https://web.archive.org/web/20240603033716/ (…/exit_and_return_visa_تأشيرة_الخروج_والعودة.docx)
- moi-guide-addition-request, moi-guide-marriage-contract, moi-guide-temp-extension: 20240603 captures of the same folder
- moi-english-guide (english_guide_final.pdf, 20240917): the archived copy is truncated at 1 MB and unreadable; not registered, not used
- moi-ar-family-residence (20241023), moi-ar-study-residence (20241023), moi-ar-investment-residence (20241023), moi-ar-work-residence (20241023), moi-ar-residence-profession (20241023), moi-ar-eservices-guide (20241023, 45 pages; could not be rendered as images here, text layer garbled; not used), moi-visa-regulation-1997 (20241110, .docx with a clean Arabic text layer)

#### What was searched

- MOI (English and Arabic): restricted-nationalities list, visa and residence e-application pages, service guide and every service card in it, FAQ, e-visa page with fees, news items (2026 joint statement on registering residence; one-year multiple-entry visa), Visa Regulation No. 3 of 1997.
- MFA Jordan: Jordan Pass PDF (Washington embassy), embassy pages for New Delhi and Islamabad. No mfa.gov.jo page says which Jordanian embassy covers Bangladesh; Jordan has no embassy in Dhaka (Bangladesh has asked it to open one: TBS, Daily Star, Prothom Alo, Financial Express, 2020; not saved).
- Jordan Tourism / Jordan Pass (restricted list), Ministry of Tourism visa page (blocked), jordan.gov.jo PSD "foreign arrivals" page (blocked).
- CSPD (cspd.gov.jo): service guide pages via Wayback. The English birth-registration service page could not be found in the archive (45/1 not archived; 45/2 is death registration). Birth-registration rules therefore come from the UK Home Office knowledge profile (2026) and an IRB Canada response (2016) quoting Civil Status Law 2001, Article 13.
- Ministry of Higher Education: expatriate admission policy (via Wayback), Jordan News reports on studyinjordan.jo; University of Jordan visa page.
- UNHCR Jordan help site (registration page via Wayback); NRC 2019 report on non-Syrian refugees (hosted on data.unhcr.org); Middle East Eye 2022; HRW 2015; RLI blog 2025.
- Amnesty International 2019 report on women's detention; Raseef22; Pressenza 2026 (returnee from Jordan); Tamkeen contact page.
- Bangladesh Embassy Amman: home, birth registration, birth certificate attestation, address.
- Bangla searches (জর্ডান ভিজিট ভিসা প্রতারণা) found no Jordan visit-visa scam story; English searches found the June 2026 CID arrest at Surah Travels (UNB) and older Daily Star pieces naming Jordan on a Bangladesh-UAE-Jordan-Libya-Europe smuggling route (could not be saved; see below).
- Arabic searches for a salary threshold for a foreign worker to sponsor family (شروط إقامة زوجة وأبناء العامل الوافد) found nothing official or reliable.

#### Conflicts and points to watch

- **The brief mentions "the 2019 deportation of non-Syrian asylum seekers".** The sources show two separate events: the December 2015 deportation of about 800 Sudanese asylum seekers [V0179, V0180, V0181], and the government's 23 January 2019 decision suspending UNHCR registration of new asylum seekers [V0170], which in practice bars anyone who entered for treatment, tourism, study or work [V0175]. The doc states both accurately.
- **UNHCR's own page** says registration of asylum seekers is suspended without naming the entry-purpose criteria [V0170]; the "medical, tourism, study or work" wording comes from Middle East Eye (2022) [V0175]. Kept both.
- **Family residence: whether the family member must be inside Jordan.** The Arabic MOI card says the service is for foreigners already inside Jordan [V0110]; the English card lists "a copy of the stamp of the last entry" [V0104], which fits. The doc therefore says the family enters first on a visit visa. No source states the step for a family member still in Bangladesh.
- **Bank-deposit residence card title.** The English card is titled "Annual residency in a profession (without a bank deposit)" but its terms require a JD 20,000 deposit (or JD 10,000 plus a flat) and its file name is "annual_residence_visa_with_bank_deposit" [V0152]. The doc uses the terms, not the title.
- **Visa fees for restricted nationals.** The JD 40/60/120/200/350 schedule is on MOI's e-visa page, which serves only nationalities that need no prior approval [V0004, V0006]. The visit/tourist/treatment service cards list only the JD 2 service charge. Left as a Need to know.
- **Tourism-office guarantee of JD 50,000** is from a 2016 Jo24 report of a ministerial meeting [V0082]; no current official figure found.
- **Investor routes**: the 5-year property residence (JOD 200,000, keep 5 years) and USD 1 million citizenship deposit come from a law-firm guide (Dec 2024) [V0158-V0160, V0155]; the Jordan Times 2018 report gave a 10-year hold for permanent residency at JD 200,000 [V0157]. No Ministry of Investment page was saved.
- **Schengen/US visa rule (2025)**: Jordan Times says Schengen or US visa holders may enter regardless of prior use and eligible travellers get a five-year visa at the border [V0018, V0019]; it is unclear whether restricted nationals (Bangladeshis) are covered. Kept as Need to know.

#### What happens in practice

- Bangladeshis in Jordan are almost all workers (garment and domestic). The non-work routes that matter in practice are: relatives' visit visas, the 2025 Gulf-resident route (relevant to the large Bangladeshi workforce in Saudi Arabia and the Gulf) [V0016, V0017], and the birth of children to migrant women.
- The June 2026 amnesty let people who entered on tourist visas apply for work permits (Bangladesh Embassy statement reported by New Age) [V0233]; it ended 30 September 2026 with no extension [V0236, V0237]. Official MoL text of the Cabinet decision not saved (Petra page blocked). Part R owns the amnesty; I cite it only under Changing visa type.
- Amnesty (2019) documents a Bangladeshi domestic worker ("Pia") detained 4.5 months in Juweideh for zina, giving birth in detention and having her son taken away [V0195, V0196]. Tamkeen counted 20 home births by unmarried domestic workers in two years, none registered [V0200]. A 2026 Pressenza piece documents a Bangladeshi returnee from Jordan whose daughter is still unregistered at eight [V0204, V0205].
- Students: the Ministry of Higher Education says the unified portal was set up partly to stop brokers selling often-fake admissions [V0144]. In 2026 the top applicant nationalities were Malaysian, Arab-Israeli, Saudi, Syrian and Iraqi [V0145]; no figure for Bangladeshis.

#### Facts logged but left out of the draft, and why

- V0003 (other restricted Asian nationalities): trivia once Bangladesh's status is stated.
- V0011 (Jordan Pass heading): duplicate of V0010.
- V0045 (account opened from abroad is activated by link): the visit-visa host is in Jordan; kept for the assembler in case a visitor applies himself.
- V0055 (children under 16 without passports go in the companion field), V0056 (Iraqis with GCC residence): minor or not about Bangladeshis.
- V0060, V0063 (lists of MOI e-services; five-year residence e-service): covered by the specific service cards.
- V0069 (Minister may waive visa fees on humanitarian grounds): no evidence it is used for Bangladeshis.
- V0135 (universities' three nationality types): duplicate of the restricted-country explanation.
- V0145 (top student nationalities): no bearing on what a Bangladeshi does.
- V0153, V0157 (investment heading; 2018 investor scheme): duplicate or superseded.
- V0178 (Interior Minister on medical-visa asylum claims): the Sudanese deportation and the registration bar make the point.
- V0202, V0203 (Juweideh kindergarten only for "legal babies"; hospitals not obliged to report unmarried pregnancy): detail; could be added under "If the parents are not married".
- V0222 (Embassy consular tours to Irbid, Aqaba, Al Dulayl): belongs in Contacts (part R).
- V0232 (Tamkeen's focus): Tamkeen is explained inline.
- V0234, V0235, V0239 (amnesty detail, "beware of fraud", inspections): part R's amnesty section.
- V0244 (55 passports seized in the Surah Travels raid), V0245 (2020 families included in exit amnesty): detail.

#### Pages we could not download

- https://moi.gov.jo/ (all pages, live): connection refused; used Wayback copies instead.
- https://help.unhcr.org/jordan/en/ , https://help.unhcr.org/jordan/en/applying-for-asylum/ (404), https://help.unhcr.org/jordan/en/contact-unhcr/ : 403 (registration page saved via Wayback).
- https://ammanpe.dfa.gov.ph/95-labor-office/public-advisories/127-visa-fees-for-entry-into-jordan (Philippine labour office, visa fees for restricted nationals): 403.
- https://jordanembassyjapan.com/wp-content/uploads/2022/07/Visa-Information-Updates-July-13-2022.pdf (restricted nationals apply via MOI e-visa, at least 2 weeks): 530.
- https://images.thedailystar.net/node/1745212 ("Illegal Voyage to Europe: They call it 'game'", names a Bangladesh-UAE-Jordan-Libya route): connection failed.
- https://amman.mofa.gov.bd/pages/static-pages/ই-পাসপোর্ট-আবেদন-প্রক্রিয়া-ddzte4-69e0b83c91a6f56f1fa96a69 (Embassy e-passport process): 404 when requested by script.
- https://cspd.gov.jo/EN/ListDetails/Services__Guide/45/39 and the CSPD birth-registration service page: no connection; not in the archive.
- https://portal.jordan.gov.jo/wps/portal/... "procedures for the movement of foreign arrivals" (PSD): no connection.
- https://www.mota.gov.jo/Ar/Pages/معلومات_التأشيرة (Ministry of Tourism visa info): no connection.
- https://www.petra.gov.jo/ar/index.php/en/news/labor-ministry-launches-worker-status-regularization-drive-through-september-30 : 522.
- https://jordantimes.com/... (direct): 403; the three Jordan Times pages used were saved via Wayback.

#### Open questions (also in the draft as Need to know)

The biggest gaps: which Jordanian embassy serves Bangladesh; whether the JD 40-120 visa fee is charged on top of the JD 2 approval charge; stay length and extension of a visit visa; the salary or job rule for a worker to sponsor family; where the family residence card is issued; how the baby's residence works for parents who can't sponsor family; and whether the Embassy registers babies of unmarried mothers.

## Part R

### Jordan: research notes, part R (sending money home; going home without valid papers; death, injury and job loss; coming home; contacts)

Agent R, 9 November 2026. Fact ids R0001-R0259. Facts R0001-R0123 are Bangladesh-side facts reused from `countries/qatar/` (sources copied with their fetch-log rows and re-registered; each row's note says "reused from Qatar <id>"). The mapping Qatar id -> R id is in `reuse-map.txt`; `factmap.txt` maps my working tags to ids.

#### Sending money home

##### Searched
- CBJ list of licensed exchange companies (cbj.gov.jo times out from here; no list found by search). Only third-party sites name houses (Musharbash, Zamzam, Jordan UAE Exchange, Alawneh, Al Alami); none confirmed as sending to Bangladesh, so none is named in the doc.
- bKash partner list for Jordan: no Jordan partner found (bKash remittance pages list corridors, not Jordan). Padma Bank signed with Alawneh Exchange (Jordan) in May 2019 (Financial Express); not saved or used, as it is 7 years old and not proof the channel works now.
- World Bank Remittance Prices: no Jordan-Bangladesh corridor found. Bangladesh Bank's quarterly cost table (R0092) has no Jordan row; only the all-country averages are used.
- Hundi law: Jordan's Money Exchange Business Law No. 44 of 2015 (AMLU English translation, archived) gives the licence requirement and penalty (R0130-R0133). Bangladesh: Money Laundering Prevention Act 2012 on bdlaws (act 1088) gives the definition of money smuggling, the currency-smuggling predicate offence and the 4-12 year penalty (R0134-R0136). No statute names hundi itself; the doc states what each law says and does not claim a hundi sender has been prosecuted under it. Bangladesh Bank's warning that sending outside the banking channel is punishable (R0137) comes from bdnews24, 17 Nov 2022 (the saved file name says 2026-09 by mistake; the page date is 2022-11-17).
- Practice: the Better Than Cash Alliance / Better Work / GIZ report (Oct 2021) is the only source on how garment workers in Jordan pay and remit: two-thirds paid in cash, remittances after cash-out, Western Union via eFAWATEERcom, exchange-house reps in dormitories (R0140-R0144, R0255, R0256).

##### Conflicts
- Probash contribution list: Tk 1,000 option in the Bangla page but not the English brief (R0019 vs R0020), as in Qatar.

##### Left out
- R0122 (PKB migration loan fees): reused by mistake while copying Qatar's contact block; not needed in these sections.

#### Going home without valid papers

##### The overstay fine
- No official text of the 2025 amendment to Residence and Foreigners Affairs Law No. 24 of 1973 could be saved: Refworld (403, no Wayback capture), lob.gov.jo and psd.gov.jo time out. The fine is cited from the PSD statement as reported by Petra/Jordan News, 8 May 2025 (JD 90 a month or JD 3 a day, R0145-R0146), the GDP/Tamkeen CEDAW submission, Sept 2026 (Article 34(A), approved February 2025, doubled from JD 1.5, R0147), and the US State Department travel page (fine collected at departure, R0246).
- Not saved, read only: Jordan News (19 Feb 2025) reported the House approving the JD 1.5 to JD 3 increase and a 90-day rectification period after publication in the Official Gazette.
- The JD 200 fine for not registering an address (Art. 11/14/36) is from the MOI's own news item (archived July 2026, R0148-R0149).

##### The 2026 regularisation decision
- No mol.gov.jo or Official Gazette text could be saved (mol.gov.jo times out; the ACI copy of the Cabinet decision PDF fails to download). All terms come from Al-Mamlaka TV reports quoting the Minister and MOL spokesman Mohammad Al-Zyoud (14 June to 3 Nov 2026), status "lead".
- Timeline: decision announced 14 June 2026, period 15 June-30 Sept; MOL repeated "no extension" in August and September; the Cabinet then extended it to 1 December 2026, with the deportation flag from 1 January 2027 (R0175-R0176). The September articles say the flag starts 1 October 2026; superseded.
- The QIZ garment sector and specialised-skills permit holders are excluded (R0153). This matters most for Bangladeshis, since most work in QIZ garment factories. Unclear whether the exclusion also covers the exit-without-return waiver: kept as a Need to know.
- Five-year ban for those who leave under the decision: stated by the spokesman (R0165) and for the deportation flag (R0173).
- Uptake: 64,000 permits issued or renewed and about 2,400 final departures by 20 Aug 2026; about 49,000 workers in breach registered (R0166, R0169, R0170). No figure for Bangladeshis found.
- Bangladesh side: the Embassy called the early-June amnesty reports a rumour (Bangla Tribune, 2 June 2026) and after the decision posted on Facebook urging caution against fraud (New Age, 18 June 2026). No Bangla news found on how many Bangladeshis used it.

##### Travel permit
- The Amman Embassy website has no travel-permit page (its "Passport" and e-passport process links are empty or 404). No fee in JD found. Kept as a Need to know; only the general e-passport fee at missions is cited (R0029).

##### Detention
- GDP/Tamkeen submission (Sept 2026) for the legal frame (Art. 37, no time limit, no specialised centres). TBS July 2020 for Juweideh numbers. No source found on who pays the ticket for a detained Bangladeshi; the 2025 TIP report says the government often lacks money for flights for trafficking victims (R0252, logged but left out because it is about trafficking victims, not detainees).

##### Travel bans
- No official page found on how to check for a travel ban or deportation flag before the airport (MOI e-services pages are reachable only via Wayback and V owns them). Need to know.

#### If a worker dies, is injured or loses the job

##### SSC work injury
- The SSC law PDF on ssc.gov.jo (Law No. 1 of 2014 as amended to 16 April 2023) is a 45 MB scan with no text layer; not used. Benefit rates come from the US SSA's Social Security Programs Throughout the World 2018 (archived; possibly outdated) and the ILO's 2021 FAQ for QIZ garment workers (procedure after an accident, reporting, receipts, CBA 2019 medical costs, SSC lump sum rules).
- Not found: whether the SSC pays disability or survivor pensions to people living in Bangladesh. Need to know.

##### Body repatriation
- No Embassy Amman page on death procedures, NOC papers or costs. No Jordanian rule found on who pays to send a body home (domestic-worker regulation No. 90 of 2009 not checked in full; D owns it). Practice: Jordan Times 2016 and 2018 cases (archived). No 2025-2026 Bangla news found on bodies returned from Jordan (searches in Bangla and English; Prothom Alo's all-country death figures have no Jordan row in the saved copy).

##### Job loss
- SSC "Permanent Departure from the Country with No Return" online withdrawal (Jordan News, 22 June 2026). Achilles Apparel case (Fibre2Fashion, Feb 2024): 454 workers paid after 18 months of Embassy negotiation. Business & Human Rights Resource Centre and Business Post copies could not be saved (403/blocked).

#### Coming home
- Jordan's cash declaration threshold is JD 10,000 on arrival and departure (Jordan News, Sept 2021, citing AML Law No. 20 of 2021; Jordan Customs page archived). AMLU's 2011 instructions set JD 15,000 for entry; superseded.
- Bangladesh customs and returnee support reused from Qatar unchanged.

#### Contacts
- Embassy contact page (updated 20 Sept 2026) and the WEWB list of labour wings (updated 6 Oct 2025) agree on the main number +962 6 5529192. The labour wing's mobile +962-7896-06415 comes only from the WEWB list. Consular hours are from an April 2023 notice (PDF image, transcribed); no newer hours found.
- No WhatsApp hotline found for the Embassy.
- MOL hotline numbers from UNHCR's Help site (archived May 2026); not on an MOL page we could save.
- Jordan has no embassy in Dhaka (Bangladesh asked in 2020; R0254). The Jordanian Embassy in New Delhi page (saved by V) does not say it covers Bangladesh. Need to know.
- BOESL contacts are from a 2019 archived page (7-digit landlines, likely outdated). BRAC Migration Programme page has no phone number.

#### Facts logged but left out
- R0151 (harbouring a runaway domestic worker = trafficking charge), R0164 (no sector move for workers who entered after 25 Feb 2025), R0167 (employer penalties from JD 800), R0171 (permit renewal online), R0190 (Labour Law Art. 12 deportation), R0192 (12% of permit holders Bangladeshi): belong to H, D or A's sections; offered for their use.
- R0251, R0252 (Dar Karama capacity; no funds for flights): detail not needed for a contact entry.
- R0122: see above.

#### Cross-links assumed
- "Work visa: garment and factory worker, Changing employer or leaving" (H) for changing employer.
- The doc assumes H covers absconding reports and what can get you jailed; this part covers only fines, detention and bans on the way out.

#### Pages we could not download
- https://jordantimes.com/news/business/labour-ministry-launches-worker-status-regularisation-drive-through-sep-30 (403, no Wayback capture)
- https://www.jordantimes.com/news/local/psd-urges-residents-visitors-regularise-residency-status-avoid-fines (403, no Wayback capture)
- https://www.refworld.org/legal/legislation/natlegbod/2025/14194?lang=ar (Residence law as amended 2025; 403, no Wayback capture)
- https://aci.org.jo/UploadFiles/قرار قوننة وتوفيق اوضاع العمالة الوافدة.pdf (Cabinet decision text; connection fails)
- https://www.ssc.gov.jo/wp-content/uploads/2024/01/قانون-الضمان-الاجتماعي-رقم-١-لسنة-٢٠١٤-وفقاً-لآخر-التعديلات-حتى-تاريخ-١٦_٤_٢٠٢٣_compressed.pdf (downloads, but a scan with no text; needs OCR)
- https://www.ssc.gov.jo/wp-content/uploads/2026/03/الجهات-الطبية-المعتمدة-لعلاج-إصابات-العمل-.pdf (SSC-approved work-injury medical providers; 404 via script)
- https://en.ammonnews.net/print.php?id=86903 and https://en.ammonnews.net/article/81049 (connection fails)
- https://customs.gov.jo/en/CMS_NewsDetails.aspx?Key=11875 (live page times out; Wayback copy used)
- https://www.mol.gov.jo/ (all pages time out from here)
- https://jordan.gov.jo/EN/Pages/BKhedmetcom (important numbers; 522, no Wayback capture)
- https://business-humanrights.org/en/latest-news/jordan-over-400-bangladeshi-garment-workers-receive-owed-wages-social-security-pay (403, no Wayback capture)
- https://www.ssa.gov/policy/docs/progdesc/ssptw/2024-2025/asia/jordan.html (403, no Wayback capture; 2018 edition used)
- https://help.unhcr.org/jordan/en/helpful-services-unhcr/working-in-jordan/ (403; Wayback copy used)
- http://www.boesl.org.bd/ContactUs.aspx (live page fails; 2019 Wayback copy used)
- https://amman.mofa.gov.bd/pages/static-pages/ই-পাসপোর্ট-আবেদন-প্রক্রিয়া-ddzte4-69e0b83c91a6f56f1fa96a69 (404)

## Final audit (10 Nov 2026)

- SIM card rules for foreigners: TRC's point-of-sale instructions (2017 amendment, Official Gazette, archived from ammanchamber.org.jo/Uplaoded/3453.pdf) only cap lines; they do not list the papers a non-Jordanian shows. Zawya's 2013 report on prepaid SIM rules (https://www.zawya.com/en/business/new-regulations-on-sale-of-prepaid-sim-cards-go-into-effect-yfulqluc) returned HTTP 400; it reportedly allowed a visa, residence or work permit copy instead of a passport. Logged only the 2019 Al Mamlaka line cap (KG0001).
- Bangladesh-Jordan MoU: only a 2012 MoU found (Recruitment Advisor citing ILO, KG0005); no text, no domestic-worker annex found.
- Social security share: IFPRI's 6.25% (G0100) conflicts with MOL's 7.5% worker share (H0042); doc uses 7.5%.
- Clearance window to change employer: MOL guide Aug 2026 says 60 days (KC0108); the July 2025 English guide said 90 (D0142, H0142). Doc uses 60.
- Full audit checklist: _verify/audit.md.

#### Pages we could not download
- https://www.zawya.com/en/business/new-regulations-on-sale-of-prepaid-sim-cards-go-into-effect-yfulqluc (HTTP 400)
