# Notes: recruiting agencies

## Compiled list (agencies.csv, doc.md, facts A)

- `agencies.csv` had 178 agencies in the first compile (188 after the ownership rows, 293 after v2; see Compile v2), keyed by RL number (normalised to RL plus four digits). Selection: the 60 with the most workers and the 40 with the most letters in `activity.csv`; the top 5 by workers in every country with at least 5 letters; every agency on a published list (Malaysia's 2026 FWCMS principals, the 2016-18 G2G Plus ten, the 2022-24 round as reported, the CID figures); every agency with a press flag or an official flag other than OEP status and the 45 administrative cancellations of 30 Oct 2025. The 312 Malaysia associates are not all included; for those included, `listed_in` names their principal.
- Columns: `licence_status` is the live OEP page of 7 Nov 2026 (`oep-agencies-c`); "Active (28 Oct list)" would mean it came only from `data/oep-agency-list-2026-10-28.csv`. `countries` and `activity` are tallies of `activity.csv` (permission rows, reposts excluded, `new_workers`). `listed_in` comes from `activity-other.csv`; `people_linked` and `flags` are short forms of the rows in `flags.csv` and `flags-press.csv`; `fact_ids` lists every fact behind the row.
- Facts A0001-A0108 quote each selected agency's row on the OEP page, so licence status can be cited where no C fact existed. A0109 is the OEP list header, A0110-A0111 the newest BMET entries, A0112 the Bonanza Saudi permission letter (garbled Bangla, logged with --no-quote-check: column "অভিবাসন ব্যয়" shows Tk 58,610), A0113 the ACC charge sheet line from the Financial Express (Sep 2025).
- Per-agency letter and worker counts in the doc cite P0001 (the BMET list). They are our tally of the PDFs, not a figure any source prints; the PDFs sit in /tmp/bmetwork/pdf/ and each `activity.csv` row links its PDF.
- Name matches made in compiling: the press agent left four gazette names without an RL; the official-flags agent had matched them, and the doc follows: Hridoy Trade International = Haidory Trade International RL0240, Jaharat International = Zahrat Associate RL0285, Aparajita Overseas = Oparajita Overseas RL1318, New Age International (gazette) = New Edge International RL0703 (the writ was filed by "নিউ এজ ইন্টারন্যাশনাল", C0007). "New Age International" in Prothom Alo's 2024 syndicate ranking (N0032, Q0021) is kept separate, as is "Jaharat Associates" in the Sep 2025 ACC case (N0053); either may be the same agency. BOESL's name-only rows were merged into RL0147.
- Open: whether Imperial Overseas (Prothom Alo 2024) is Imperial Overaseas Company RL0428 (Cancelled) or Imperial Resources RL1874; whether Apurbo Recruiting Agency (N0053) is Anonno Apurbo RL2101 (as the press agent matched).
- The doc lists each country with at least 4 letters. Bahrain, Italy and Kyrgyzstan have no letters, so they have no section; Kyrgyzstan appears under red flags.

## Activity from BMET permission letters (activity.csv, facts P)

### What was collected

- Source list: BMET "miscellaneous-infos" page, https://bmet.gov.bd/pages/miscellaneous-infos. It held 3,151 entries on 7 Nov 2026 [P0001]. The site accepts `?page=N&page_size=500`, so the whole list came down in 7 pages, saved with fetch.py as `sources/bmet-misc-infos-p1-of7` to `p7-of7` (.html), all registered in `sources.csv`. fetch.py's own .md copies came out truncated (bs4 missing), so I added a clean table text copy per page (`sources/bmet-misc-infos-pN-of7.txt`: no. | title | publish date | file links | view page). Quotes for facts come from these.
- Newest entry is dated 8 Feb 2026 (a ToT list); the newest permission letter is dated 10 Dec 2025; the oldest entry is dated 22 May 2023. Nothing posted after Feb 2026 is on the list, so this is not a live feed.
- Most titles do not say much. Only 124 titles name the agency, country and worker numbers in full (mainly Jul to Dec 2025). The rest are "SL1408 RL40 (memo no.)", "নিয়োগানুমতি DN25-dn-489 RL2345 (memo no.)" or "Admin_Job_Report_SA-RL0579-...", which give the RL number only. So I opened the PDFs.
- PDFs: all 4,367 linked files were downloaded from objectstorage.ap-dcc-gazipur-1.oraclecloud15.com, which had no blocking, and run through pdftotext. Most letters include BMET's English system printout ("Recruitment Permission Details/Letter", or the 2025 "Recruitment Permission Check List"). Each printout gives the permission ID (country code-RL-year-serial), permission date, country, employer, agent ID and name, and a job table with the number of posts and the salary. 335 image-only files were OCR'd in English with tesseract, which picks up scanned English printouts.
- The PDFs were not all saved into `sources/`: that would be about 1 GB. They sit in a working cache at `/tmp/bmetwork/pdf/` (temporary, along with the text and OCR copies). Each row's `url` points to the official PDF. Two example PDFs were saved and registered: `bmet-permission-kr-rl0147-2024-0011365` [P0003] and `bmet-permission-rl0040-dn25-469` [P0004, P0005].

### activity.csv

3,162 rows: 3,138 permission rows plus 24 notice rows (`entry_type` = notice, for example "Provide Demand Letter to IT Cell" or "not entered in the database for lack of documents"; these are not permissions). 35 entries that are not about permissions (JLPT lists, PDO question banks, monthly statistics, SVP notices) were left out.

Columns: `date` (BMET posting date; for 90% of rows it is within 2 days of the permission date), `rl`, `agency` (name from the OEP list, falling back to the PDF, then the title), `country`, `workers`, `jobs` (post name with the number of posts), `url` (the first PDF), and then:
- `new_workers`: workers on permission IDs not already counted in an earlier entry. BMET sometimes reposts the same permission. 64 entries are full reposts (`dup_of_entry` gives the earlier list number). Use `new_workers` for totals.
- `permission_date`, `permission_ids`, `part`: one BMET entry can cover several countries or agencies. These are mostly BOESL bulk posts, the "boesl (date)" entries, and get one row per agency and country pair (`part` = "1 of 5").
- `licence_status` and `licence_valid_until`: from `data/oep-agency-list-2026-10-28.csv`. Every RL in the data is on that list.
- `title`, `bmet_list_no`, `list_page`, `all_files`, `extracted_from` (pdf | pdf+ocr | title | pdf-text-fallback+title | none).

Coverage: of the 3,069 rows that are not reposts, 2,967 have a country and 2,945 have a worker count. Rows still missing data are mostly 2023 Bangla scans that English OCR can't read. Where the title RL and the PDF agent ID disagree (22 cases, typos in titles such as "RL13226" or "RL03510"), the PDF's agent ID is used. Job names are rebuilt from wrapped table columns and are approximate. The counts are reliable.

What the numbers mean: a permission letter is BMET's approval for an agency to process emigration clearance for N workers for a named employer. It shows demand an agency obtained and BMET approved. It does not show departures, and it does not show quality or fair fees. The list is also only what BMET chose to post (3,138 letters over about 2.5 years), not every permission BMET issued.

### Summary (rows that are not reposts, 22 May 2023 to 10 Dec 2025)

Totals: 618 agencies, about 259,000 workers approved. By year, letters were 928 in 2023, 1,269 in 2024 and 872 in 2025 (some rows lack a date split by country). Licence status today, per the 28 Oct 2026 OEP list: 540 of the 618 agencies are Active, 52 Cancelled, 15 Expired, 9 Suspended and 2 Server Locked. Agencies now Cancelled account for about 58,000 of the workers. For Malaysia it is about 50,000 of 102,000, almost half.

By country (letters, workers): Saudi Arabia 1,148 / 70,145; Malaysia 1,092 / 102,451 (541 letters in 2023, 476 in 2024, 75 in 2025, the last on 21 Sep 2025); Japan 304 / 1,321; UAE 95 / 31,081; Russia 84 / 8,084; Kuwait 48 / 6,910; Cambodia 39 / 2,359; Jordan 28 / 15,684; Brunei 28 / 2,279; South Korea 23 / 10,867; Libya 20 / 1,209; Singapore 15 / 170; Qatar 8 / 2,261; Maldives 5 / 440; Mongolia 5 / 339; Oman 4 / 370; Romania 4 / 1,080; others 1 to 3 letters each. Bahrain, Italy and Kyrgyzstan don't appear.

Overall, by letters: BOESL RL0147 (state-owned Bangladesh Overseas Employment and Services Ltd) 68; Greenland Overseas RL0040 68; Global Recruiting Agency RL1324 43 (all Japan, 139 workers); AVR Bangladesh RL1135 31; United Gulf Services RL1036 29; Amco Enterprise RL1537 29; A.J. International RL1304 26; Western Business Alliance RL0173 25; Al-Bhokhari International RL0301 25; Career Overseas Consultants RL0403 24; ProSearch RL1027 23; Bonanza Overseas RL0579 23.

Overall, by workers: BOESL 30,149 (Jordan garments, the Korea EPS order of 10,000 [P0003], Brunei, Japan); Greenland Overseas 8,709; Matco Enterprise RL0250 5,112; AVR Bangladesh 4,013; Career Overseas Consultants 3,757; Catharsis International RL0549 3,617 (Cancelled); Navira RL0712 2,796; Al-Anas Overseas RL2735 2,765; A.J. International 2,755; Stanford Employment RL1352 2,744 (Cancelled); Banna Bijoy Overseas RL1314 2,540 (Server Locked).

Per country, top by letters, then top by workers:
- Saudi Arabia. Letters: Greenland 44, Amco 28, A.J. International 26, Career Overseas 24, United Gulf 23, Bonanza 21 [P0002], AVR 18, ASMACS RL1059 15. Workers: Greenland 7,421, Career Overseas 3,757, A.J. International 2,755, Bashundhara Employment RL1064 2,090, Amco 1,933, United Gulf 1,850, Bonanza 1,642, Azam Overseas RL0535 1,221. All are Active today.
- Malaysia. Letters: Al-Bhokhari 24, Greenland 21, SOS International RL1530 19, JG Alfalah RL1861 19 (Cancelled), Amial RL1326 18, Al Rabeta RL0354 17, Okistar RL0393 17, Comfort Overseas RL1739 16. Workers: Stanford 2,585 (Cancelled), Trans Asia RL1472 2,097 (Cancelled), Al Farah RL1485 2,030 (Cancelled), Future International RL1196 1,849, Jannat Overseas RL1419 1,719 (Cancelled), Deshari RL0945 1,706, Win International RL0721 1,686 (Expired), Catharsis 1,661 (Cancelled). 155 agencies.
- Japan: many small letters. Global Recruiting Agency 43 letters / 139 workers, Western Business Alliance 24 / 130, Nagar Overseas RL1286 20 / 87, Sadiatec RL1148 19 / 99, EWB International RL2656 18 / 65, Caplan RL1697 17 / 85, The Human Resource Bangladesh RL1080 15 / 114, ProSearch 14 / 90.
- UAE: Matco 10 / 4,940, AVR 10 / 3,171, Al-Anas 6 / 2,765, Visa International RL0963 4 / 1,965, Al Saad Labour Supply RL0939 2 / 1,645, Meum RL0528 3 / 1,532, Navira 4 / 1,491.
- Russia: Banna Bijoy 16 / 2,540 (Server Locked), Noakhali Overseas RL1602 11 / 344, Runway RL1341 4 / 790, PY and Tomoni RL2681 1 / 700, Munshi Enterprise RL0986 2 / 700 (Suspended), BOESL 1 / 675.
- Kuwait: Delight Overseas RL2287 6 / 1,226, Prestige International RL0232 5 / 685, Heaven Overseas RL0600 2 / 615, Masud Jamil RL1400 2 / 539, Loyal Manpower RL2065 3 / 445.
- Cambodia: Puspita Overseas RL2648 10 / 932, Al Grand Sultan RL1582 4 / 379, Mondol Trade RL2626 5 / 214 (Expired), Fahim RL2594 3 / 163 (Suspended), Sams Company RL0696 4 / 74 (Suspended).
- Jordan: BOESL 27 letters / 15,584 workers; one other letter (Al Sourav, 100).
- Brunei: BOESL only, 28 / 2,279.
- South Korea: BOESL 2 / 10,300 (EPS). Private agencies have small letters: Nazifa RL1859 3 / 160, RRC RL1307 3 / 43, Global Star RL1718 3 / 25, Ahmed & Company RL0081 2 / 95.
- Libya: Godhuli RL1092 1 / 385, Arabian Overseas RL2435 3 / 370, Rabbi International RL0258 2 / 165 (Cancelled), Sonar Bangla Krishi Khamar RL0089 3 / 130.
- Singapore: BRAC Probashbandhu RL1199 is the only agency, 15 / 170.
- Qatar: Barcelona Overseas RL1380 1 / 1,000, T.M. Overseas RL0498 1 / 700 (women), Bonanza 2 / 247.

### Cross-reference with other agents' facts (allegations as reported, not as fact)

Several high-volume agencies appear in reports already logged in `facts.csv` by other agents:
- Catharsis International (RL0549): the Anti-Corruption Commission (ACC) case reportedly alleges it took an extra Tk 130.43 crore from 7,787 workers [N0007]. Its licence is listed as Cancelled.
- Greenland Overseas (RL0040): named among the 13 agencies in the ACC's Sept 2025 cases [N0053]. Prothom Alo reports it was in the Malaysia syndicate [N0026].
- United Gulf Services (RL1036): Prothom Alo reports it is owned by the wife of Greenland's owner [N0026].
- Navira (RL0712) and Jannat Overseas (RL1419) are also among the 13 agencies in the ACC Sept 2025 cases [N0053].
- Career Overseas Consultants (RL0403) is named by Bloomberg among the 2016-18 Malaysia agencies that agents allege charged a syndicate fee; it denied this [N0019].

High volume is not evidence that an agency treats workers well. Some of the busiest agencies are the ones under investigation.

### Use for the country docs

The per-country tables can list who holds approved demand in each corridor. Under the KB rules, an agency is named as recommended only with outside evidence of fair practice (Bonanza in Saudi Arabia). Volume alone shows activity, not trustworthiness. BOESL is effectively the only channel for Jordan, Brunei and Korea EPS in this data.

### Pages we could not download

None. 8 linked files are JPEGs or blank, and 4 of those gave no text even with OCR.

## Activity from lists and reports (activity-other.csv, facts Q)

Output: `activity-other.csv` (rl, agency, oep_name, country, evidence, date, url), 380 rows. `agency` is the spelling in the press list; `oep_name` is the name on `data/oep-agency-list-2026-10-28.csv` for the same RL (for example RL1537 Amko = AMCO ENTERPRISE LIMITED, RL0393 Akister = Okistar, RL1697 Kaplan = CAPLAN, RL1314 Bonna Bijoy = BANNA BIJOY); look names up by `oep_name` or RL. Every row's evidence cites the Q fact ids in `facts.csv` (Q0001 to Q0046) behind it. Every source is saved in `sources/` and registered in `sources.csv`.

### What the rows are

- **Malaysia 2026, principal agencies (25 rows).** The 25 "processing or service" agencies on Malaysia's FWCMS (Foreign Workers Centralised Management System) list, published Friday 21 Aug 2026. Names as printed by New Age [Q0001], same list in the Observer [Q0002]. BSS, the state news agency, reporting the Ministry's 15 Oct 2026 announcement: Malaysia agreed to list BOESL, 25 private processing or service agencies and 312 recruiting agencies (338 in all); BOESL and the 25 handle calling-visa and e-visa work, then the recruiting agency does BMET clearance [Q0008]. Prothom Alo's analysis of BMET data says 17 of the 25 had never sent a worker to Malaysia [Q0003], with per-agency figures for Bhaluka Overseas, The Anchor Care and Bangladesh One Overseas [Q0004, Q0005]. Being on this list shows selection, not a record of sending workers.
- **Malaysia 2026, associate agencies (312 rows).** 250 associates grouped 10 under each principal, plus 62 under BOESL, as printed by Aviation Express on 28 Aug 2026 [Q0009]. Ittefaq printed the same list in Bangla the same day (saved as `ittefaq-malaysia-338-list-2026`, used to check spellings). Ministry sources told ANN/Daily Star that associates can send workers only on approval of a principal or BOESL [Q0011]. **BRAC Probashbandhu Limited is listed as an associate under Motherland Overseas Limited** [Q0010].
- **BOESL (7 rows, no RL: BOESL is state-owned and has no recruiting licence number).** Malaysia: registered as processing agency [Q0007, Q0008]. BOESL's own home page (official) carries current notices for zero-cost Malaysia recruitment, Jordan garments, Singapore construction, Brunei, Japan (women caregiver technical interns), South Korea (EPS (Employment Permit System) language test for the 2027 roster) and Hong Kong (women domestic helpers) [Q0012 to Q0018]. The page is undated, so these are "possibly outdated".
- **Malaysia G2G Plus, 2016-18 (10 rows).** The 10 agencies Malaysia approved, from a Feb 2017 report (The Independent, reposted by Covey SB) [Q0019]. A news repost, not the original; I could not find the original Independent page.
- **Malaysia 2022-24 round (14 rows).** No published list of the roughly 100 agencies was found (see gaps). Rows come from Prothom Alo's May 2024 report, which cites a list "availed from concerned sources" and BMET records: 5M International (8,592 clearances), Oichi International (2nd), New Age International (3rd), Snigdha Overseas (4th, about 8,000), Ahmed International (5th, 7,849), Orbitals Enterprise and Orbitals International (9,861 together), Catharsis International (7,102 per BMET records), BM Travels (7,225 clearances), Imperial Overseas (over 7,000), Anonno Apurba (2,600), and BNS Overseas, PR Overseas and Sadia International named as having joined [Q0020 to Q0032]. Membership of the "syndicate" is Prothom Alo's report of allegations, not a finding. The evidence column says so.
- **CID figures (4 rows).** Samakal (21 Aug 2025), citing the CID (Criminal Investigation Department): Five M International sent 9,370 workers to Malaysia since 2017; Catharsis International sent 45,287 to Malaysia after 2015, 1,098 to Saudi Arabia and 49 to the UAE. CID is investigating 100 agencies and is first completing investigations into five [Q0033 to Q0036]. These are allegations under investigation, not findings.
- **BMET and Ministry job orders (8 rows).** Official permission letters naming the agency and RL: Malaysia, Green Land Overseas RL0040 (Oct 2023), Haidory Trade RL0240 (Dec 2024), Amin Tours RL0981 (Dec 2024), Roseland RL2676 (Dec 2024), J.Er Employment RL1274 (Feb 2025), Al Islam Overseas RL0106 (160 workers, Sep 2025); Saudi Arabia, Bonanza Overseas RL0579 and ASMACS RL1059 (Sep 2025) [Q0039 to Q0046]. These are only the letters the Malaysia and Saudi researchers had already found. The BMET archive holds about 3,151 of them (bmet.gov.bd/pages/miscellaneous-infos). Reading them all is the only official per-agency, per-country job-order record, and the site blocks automated access.

### RL matching

The CSV's RL numbers come from `data/oep-agency-list-2026-10-28.csv`. 348 of 380 rows have an RL. Exact name matches were automatic. Spelling variants (for example Yanbu/YAMBU, Karnaphuli/Karnafully, Kader/QUADER, Mrs. K.S/M/S K S) were matched by hand, and those rows add "RL matched by name to OEP list entry '...'" to the evidence. A Bangla-to-English transliteration can point to the wrong agency, so check these before naming any of them in a doc.

Left blank because there was no confident match (25 names): Al-Marzuk Overseas, Zahara International, Tajba International, Messrs Sarak Overseas, Al Rayyan International (closest is Al-Rayhan RL0444, cancelled), Makkah Overseas, South Bridge Corporation (closest is South Breeze RL1255), Messrs Al Madina International, Amin & Sons International, FNM Limited, Khaja Poribohon Songstha, Zihan Overseas, Messrs Sam International, Messrs Shihab Overseas, Messrs Raihan Overseas, Nawreen International, Akida Overseas, Aziad Limited, Avi Trade International, Notun Somoy Overseas, Mangrove Career Link (a principal; OEP has only Mangrove International RL1756), Career Overseas Resources, Shanjari Travels and Tours (OEP has Shanjari International RL0742), New Age International, and Imperial Overseas. For Imperial Overseas, OEP's "Imperial Overaseas Company" is RL0428, too old for the March 2021 licence Prothom Alo gives.

Licence status on the 28 Oct 2026 OEP list: 318 of the matched rows are Active. Every 2022-24 "syndicate" agency in the CSV is Cancelled (5M, Snigdha, Ahmed, Orbitals x2, Catharsis, BNS, PR Overseas, Sadia, BM Travels, Anonno Apurba), as are 5 of the 10 G2G Plus agencies. Some 2026 associates are not Active: T S Overseas RL1755 and RS International RL1428 are Cancelled, Munshi Enterprise RL0986 and Triple A Overseas RL2630 Suspended, Al-Mamun RL0629 and Nazrul International Service RL1465 Expired, and Bonna Bijoy RL1314 and Alam Overseas RL1647 Server Locked. Amin Tours RL0981 holds a Dec 2024 Malaysia job order but is now Cancelled.

### What was searched and not found

- **Official FWCMS list.** I didn't scrape the FWCMS site itself (fwcms.com.my). All 25 and 338 names come from Bangladeshi news printing the list. Next step: save the FWCMS page or ask a teammate to save it.
- **2022-24 list of about 100 agencies.** I searched in English and Bangla ("১০১টি এজেন্সি", "১০০ এজেন্সির তালিকা"). Many reports give the count (25, then 100 or 101 in three phases) but none of the pages I found prints the names. One YouTube video claims to show the list (not used). The ACC case files against agencies are covered by another agent's sources (`ds-acc-sue-12-agencies` and others), so I didn't repeat them here.
- **BMET or Ministry agency awards and rankings.** No "best recruiting agency" award or ranking turned up (Bangla and English searches). CIP (Commercially Important Person) honours go to expatriates who send remittances, not to agencies. A grading system exists on paper: the Recruiting Agent Classification Rules, 2020 (gazette 5 Mar 2020, saved as `baira-agent-classification-2020`) set up a grading committee and a 100-point score. But The Daily Star reports that the government "has yet to introduce an effective grading system", and the state minister said he could not confidently recommend an agency [Q0037, Q0038]. So there is no official grade list to use.
- **BAIRA lists.** BAIRA's member directory (baira.org.bd/dir/all-member-list) lists members with RL numbers. Membership shows no activity, so it is not used.
- **Agency-wise departure data.** OEP's public reports are only by country (`/reports/country-clearance`, `/reports/geo-clearance-count`), with no per-agency report. The only per-agency counts found are those quoted by journalists from BMET records (Prothom Alo) or the CID (Samakal).
- **Pages that failed:** boesl.gov.bd with "www." (connection failed; the bare domain worked).

### Caveats for anyone using this file

- On the 2026 lists: being listed is selection by Malaysia, not proof of a sending record or of fair practice. The selection process is disputed (BAIRA members and BRAC's Shariful Hasan call it a syndicate in New Age), and that is reported as allegation.
- Under CLAUDE.md, no row here is a recommendation. Naming an agency in a country doc still needs outside evidence that it helps workers. None of these lists is that evidence.
- The CSV has a `country` column, so a country doc can filter its own rows. Most rows are Malaysia, because Malaysia is the corridor where agency lists are published.

## Official red flags (flags.csv, facts C)

Output: `flags.csv` (564 rows, 412 distinct RL numbers plus Ifty Overseas and Dream Home Travels, which have no RL). Columns: rl, agency, flag_type, date, summary, source_url, fact_id. Facts are prefix C (C0001-C0477). The rows were generated by a script that parses the saved sources and calls `facts.py add`, so every row's quote was checked against the saved copy.

### What is in the file

| flag_type | rows | source |
|---|---|---|
| oep-status-cancelled | 235 | OEP agency list (official, undated live page, fetched 7 Nov 2026) |
| oep-status-suspended | 151 | OEP agency list |
| oep-status-server-locked | 9 | OEP agency list. OEP does not say what "Server Locked" means. |
| licence-cancelled | 98 | 49 (Ministry gazette, 19 Jul 2026, Malaysia syndicate case), 45 (Ministry office order, 30 Oct 2025, for not sending 100 workers), 3 (Russia war case, 1 Jun 2026), 1 Dream Home Travels (travel-agency registration, Civil Aviation Ministry) |
| court-order | 50 | High Court stay and Appellate Division chamber stay on the 49-licence withdrawal |
| acc-case | 12 | Anti-Corruption Commission cases approved Mar 2025 (Malaysia overcharging) |
| deposit-forfeited | 3 | Russia war case, 1 Jun 2026 |
| mobile-court-fine-sealed | 1 | Triple A Overseas (RL2630), BMET mobile court, 10 Sep 2026 |
| interpol-request | 1 | Catharsis International (owner Ruhul Amin Swapan), Interpol NCB Dhaka to Malaysia NCB, 24 Oct 2024 |
| cid-case-asset-attachment | 1 | Catharsis International, CID asset attachment on court order, Aug 2025 |
| embassy-attestation-refused | 1 | Jabal-E-Noor (RL2505), Bangladesh Embassy Moscow labour wing, May 2026 |
| trafficking-case-reported | 1 | Bonna Bijoy Overseas (RL1314), Prothom Alo, Oct 2026 |
| foreign-sanction | 1 | Dream Home Travels and Tours, UK sanctions, May 2026 |

An agency can have several rows (for example Catharsis International: OEP cancelled, gazette cancellation, court order, ACC case, Interpol request, CID attachment).

### Evidence level

- Only the OEP agency list is an official source saved here. Every other row rests on news reports of official actions (gazette, office order, court, ACC, CID, BMET mobile court), so those facts are `unofficial`. Summaries attribute each one ("New Age reports...", "Prothom Alo reports...").
- ACC cases, the Interpol request, CID attachment and the trafficking case are allegations or investigations, not verdicts. The summaries say so.
- The OEP list gives status and validity date only. It does not give the reason or the date of a cancellation or suspension. The date column for those rows is "as of 2026-11-07".

### Cross-checks

- **49-agency gazette (19 Jul 2026):** New Age lists 48 names in English (C0002-C0004). Orbitals International comes from Kaler Kantho's Bangla list (C0005). RL numbers were matched by name to the OEP list. All 49 show **Cancelled** on OEP on 7 Nov 2026, which supports the reports. Two ambiguous matches: "Binimoy International" has two OEP entries (RL0351 Cancelled, RL0816 Suspended); I used RL0351 because it is Cancelled, but the gazette's RL is not in any saved text. "Rabbi International" (RL0258) is distinct from Gulam Rabbi International (RL1078, Active).
- **Court challenge:** New Edge International and others won High Court stays (15 Sep 2026; a second writ by 11 agencies). The Appellate Division chamber judge stayed the first on 30 Sep and the second on 4 Oct 2026, so the withdrawal stands (Prothom Alo, bdnews24, Attorney General's account; C0006, C0007). The final hearing outcome is not known.
- **45 licences cancelled on 30 Oct 2025 (Bonik Barta; reason C0012, one fact per agency C0428-C0472):** The reason was administrative: the agencies had not sent 100 workers since licensing (s.12(1) of the 2013 Act). This is not a fraud finding. **14 of the 45 now show Active on OEP** (RL1339, RL1577, RL1637, RL1386, RL1541, RL1587, RL1724, RL1545, RL1458, RL1648, RL1447, RL1430, RL1173, RL1227). Two show Expired (RL0480, RL1129). Desh Rupantor reported agencies demanding the cancellations be reversed (search result only, page not saved). Need to know: were these 14 reinstated, or is OEP out of date? Each row's summary states the OEP status.
- **Russia war case (1 Jun 2026):** RS International RL1428, Jabal-E-Noor RL2505 and TS Overseas RL1755 all show Cancelled on OEP. Prothom Alo adds that the embassy refused Jabal-E-Noor's attestation and that workers were sent under TS Overseas' name (C0476, C0477).
- **Triple A Overseas (RL2630):** shows Suspended on OEP, which fits the September 2026 raid.
- **Bonna Bijoy Overseas:** I matched it to OEP "M/S. BANNA BIJOY OVERSEAS LTD" (RL1314, Server Locked) by name. Prothom Alo gives no RL. The trafficking case is reported with no case number, court or date.
- **Ifty Overseas** (ACC case) is not in the OEP list under that name.

### Counts without names (logged, no rows)

- A minister said 52 agencies' licences were cancelled over visa fraud and some offices sealed (DesheBideshe, 13 Oct 2026; C0473). These are probably the 49 plus the 3 Russia agencies, but the article does not say.
- 204 licences were suspended in 2020 and 163 in 2019 (TBS, 2020; C0474). No names given.
- CID said six cases had been filed over trafficking to Russia (Daily Star, Nov 2025; C0475). Agencies not named.

### Searched, nothing usable

- Saudi-side bans: Saudi HRSD's suspensions (66 offices suspended and 1 licence revoked, Nov 2026; 21 revoked, Mar 2024) cover Saudi recruitment offices, not Bangladeshi agencies. I found no Saudi list naming Bangladeshi RLs. No rows.
- Malaysia-side bans of specific Bangladeshi agencies: none found. Malaysia's role is the FWCMS approved list, which is a different agent's topic.
- Interpol red notices for agency owners: only the 2024 NCB request to Malaysia (Catharsis) was found. Nothing showed a red notice was actually issued.
- BMET deposit forfeitures other than the Russia case: none found with names.
- Official gazette PDFs: not found on probashi.gov.bd or bmet.gov.bd. Kaler Kantho embeds the 49-agency gazette PDF (651fcff0-...pdf), but its URL is not in the scrape. The Ministry page "রিক্রুটিং এজেন্সি সংক্রান্ত" (`mowe-recruiting-agency-page-c`, saved) lists 2017-2019 notices by RL with no type column (grants, renewals and others mixed together). Without opening each PDF I could not tell which ones are sanctions, so I did not use it.

### Pages we could not download

- jagonews24.com/law-courts/news/1164465 (403; bdnews24 and Prothom Alo cover the same court order)
- daily-sun.com 887599 and 897057 (403; other outlets cover the same events)
- business-humanrights.org Russia item (403; Kaler Kantho and Prothom Alo cover it)
- Firecrawl credits ran low during this run, so blocked pages were not retried.

### Overlap with other agents

The press agent (prefix N, `flags-press.csv`) also logged the ACC 12-agency case and the 49 licences from Prothom Alo English. My ACC rows use the same saved Daily Star source (`ds-acc-sue-12-agencies`) with my own C facts. The Dream Home Travels rows use that agent's saved sources (`jago-dreamhome-licence-revoked`, `fe-uk-sanction-dreamhome-fc`) with my own C facts. I did not edit their files.

### For the country docs (answer to the user's question)

A shared agency list works for lookup (the chatbot checks any RL against it), and country docs should name agencies per corridor. Most flags here are corridor-specific: 49 Malaysia, 3 Russia, 1 Triple A (Malaysia passports). Each country doc can cite the rows for its corridor. The shared CSV keeps one copy of the evidence.

## Press and civil-society flags (flags-press.csv, facts N)

Output: `flags-press.csv` (118 rows, 76 distinct agencies). Facts N0001 to N0054 in `facts.csv`; every row's fact_id quotes the saved source. Several rows share one fact when one sentence names many agencies (N0013, N0015, N0016, N0019, N0026, N0027, N0032, N0033, N0040, N0053).

### How to read the CSV

- flag_type:
  - **allegation**: a report, the ACC (Anti-Corruption Commission) or police allege wrongdoing. Nothing is proven.
  - **ownership-link**: the reported owner is a minister, MP, councillor, party leader or BAIRA (Bangladesh Association of International Recruiting Agencies) office-holder, or their family.
  - **complaint**: worker complaints, stranded workers, or an official action reported in the press, such as a licence revocation or an arrest.
  - **positive-evidence**: outside evidence of fair treatment.
- The summary always names the report or authority behind the claim. None of the rows is a finding of guilt.
- Dates are the article's page date. "2026" means the Bloomberg feature, whose exact date is unknown (its URL year is 2026).
- rl: matched by name against `data/oep-agency-list-2026-10-28.csv`. When the spelling differs or two licences share a name, the summary says "RL inferred". It is left blank when no match was found: Hridoy Trade International, Jaharat International/Associates, New Age International, Aparajita Overseas, Ifty Overseas, Global Dhaka, Adib Air Travels & Tours, Imperial Overseas, Dream Home Travels (a travel agency, not BMET-licensed) and Uttara International Career Council (unlicensed).
- Uncertain matches to check by hand:
  - Binimoy International: RL0351 is cancelled, RL0816 is suspended.
  - "Manpower Corporation" was matched to Manispower Corporation (RL0973).
  - "R Ving / Arving Enterprise" was matched to Irving Enterprise (RL0215).
  - "Adity International" was matched to Odity International (RL0983).
  - United Manpower Consultancy (RL1216, expired).
  - "Imperial Overseas" (Prothom Alo 2024) may be Imperial Resources Ltd (RL1874), which faces its own ACC case.

### What the evidence covers

- **Malaysia syndicate (most rows).**
  - Agencies tied to MPs and ministers, with ACC overcharging figures (Daily Star, Mar 2025): Orbitals Enterprise, Orbitals International, Snigdha, 5M, Ahmed International, BM Travels, BNS, Unique Eastern and others.
  - Later ACC cases: 13 agencies (FE, Sep 2025), 6 agencies (Prothom Alo, Nov 2025) and 4 agencies (BSS, Nov 2025). A December 2025 case against 60 agencies (N0052) gave no agency names.
  - The 49-licence revocation (Prothom Alo, Jul 2026). The "-c" agent's sources (pabn-49-upheld-fc-c, bdn24-49-hc-stayed-c) cover the court challenge: the Appellate Division chamber judge kept the revocation in force.
  - Catharsis International / Ruhul Amin (Bloomberg; BHRRC, the Business and Human Rights Resource Centre; Prothom Alo).
  - The 2016-18 "group of 10" (Bloomberg: Prantik and Career Overseas, both of which deny it).
  - The 2026 list of 25: United Gulf Services, linked to Greenland Overseas; Goodness Service, General Trading and Rifa International, which are among 57 agencies the ACC asked BMET about in a case on trafficking women with forged documents.
- **Case status matters.** CID filed a final report (15 Jul 2025) clearing the accused in the separate Paltan trafficking case (103 accused). The plaintiff challenged it (TBS, N0016). The ACC cases are separate and were still under investigation when reported. Denials are noted where the report carries them: Catharsis, Prantik, Career Overseas, Snigdha, BNS/PR Overseas and Ruhul Amin.
- **Other corridors:**
  - Kyrgyzstan: Makkah Madina Trade Int RL0810 and Al-Jabeen RL0884 (2022 reports; Al-Jabeen's MD disputes the claims).
  - Algeria: Virtual World Vision RL2100.
  - Hungary: Global Dhaka.
  - Russia's war: Dream Home Travels, whose registration was cancelled and which the UK sanctioned. The "-c" agent's sources cover the other Russia agencies (RS International etc.), so they are not duplicated here.
- **Positive evidence:** Bonanza Overseas RL0579 is the only agency found. It comes from the 2018-21 pilot run by the ILO (International Labour Organization) and Qatar's Ministry of Labour (UN Network on Migration; ILO brief). The evidence covers one channel only: Qatar construction work for STS/QDVC. After the pilot, workers still paid about USD 300 on average, mostly for passports and local travel (N0025; the PDF text shows "$3007", where the final 7 is a footnote marker). Nothing else qualified.

### Searched, nothing usable for rows

- **Recruitment Advisor** (run by the ITUC, the International Trade Union Confederation): it lists 1,444 Bangladeshi agencies, almost all with 0 to 2 reviews. That is too thin to count as evidence. The ITUC's 2023 report (835 reviews) gives totals only and names no agency.
- **IOM:** IRIS (IOM's ethical-recruitment certification) and IOM's fair-recruitment PDF name no certified Bangladeshi agency. The IRIS certified-list page returned 404.
- **Netra News, Oct 2026** (Saudi women domestic workers): names no agencies.
- **Saudi women:**
  - Prothom Alo (2019): 15 licences suspended over deaths, and 167 suspended by Dec 2019, with no names in the article.
  - Daily Star (2023): the Saudi visa-trade arrests name an agency owner (Mohammed Nasser Uddin Noor) but not the agency.
- **Prothom Alo 2024-25:** "hapless workers" and "revamp syndicate" were saved but add no new agency-level flags. The revamp article carries Ruhul Amin's denial ("a rumour created by a vested quarter").
- **TBS (3 Sep 2024):** the filing of the 103-accused case. It was saved but is covered by N0016.
- **OKUP and RMMRU:** quoted on how complaints are handled (N0054: proven BMET complaints are often settled for Tk 30-60k). No agency names. No WARBE report naming agencies was found.

### Pages we could not download

- **Not saved at all:**
  - Daily Sun 887599 (49 licences): 403. The Prothom Alo version was used instead.
  - netra.news 2022 "Safeguarding": 403, and Firecrawl credits had run out.
  - UCA News 109970 ("dodgy recruiters"): 403.
  - BHRRC "ACC files 13 cases": 403. The FE print version was used instead.
- **Saved by Firecrawl after curl was blocked:** Jagonews24, UN Network on Migration, Bloomberg feature, BHRRC Catharsis and the ITUC PDF. For Bloomberg and BHRRC only the relevant paragraphs were saved, copied verbatim from the scrape.
- `fe-uk-sanction-agency-russia` (curl) has an empty text copy. The Firecrawl copy `fe-uk-sanction-dreamhome-fc` is the one cited.
- Firecrawl credits ran out mid-task, so later searches used WebSearch plus curl.

### Open questions

- For the 49 revoked licences, confirm in OEP whether the current status is cancelled. Most already show as Cancelled in the 28 Oct list.
- Several agencies under ACC cases still show "Active" in OEP: Celebrity, Odity, Merit Trade, RRC, Winner, Navira, South Point, Goodness, General Trading, Rifa, United Gulf, Greenland, Oichi, Prantik and Career Overseas.
- Outcome of the plaintiff's no-confidence petition against the CID final report (hearing set for 4 Sep 2025).
- Names of the 57 agencies in the ACC women-trafficking inquiry and of the 60 agencies in the Dec 2025 case.

### On per-country docs vs a shared list

Most flags here are Malaysia-specific. The Kyrgyzstan, Algeria, Hungary and Russia rows are single-corridor. Bonanza's evidence is Qatar-only and should not be generalised to Saudi Arabia or other corridors. A country doc can filter this CSV by corridor and cite the same fact ids.

## Fixes after the independent check (facts K)

- "Letters" in the doc and `agencies.csv` are permission rows in `activity.csv`: one agency's approval for one country within one BMET posting. Where one posting covers several agencies it counts once per agency. So Saudi Arabia's 1,148 letters are 1,147 distinct BMET entries (entry 454 covers RL1565 and RL1345) and Russia's 84 are 83 (entry 1005, a 22-part BOESL post, has three Russia parts). Worker totals and per-agency counts are unaffected. The doc's opening paragraph states this definition.
- K0001: Azure Bengal Limited (RL0928) is Expired (valid until 31 Dec 2025) on the live OEP page and the 28 Oct list; added to the doc and `agencies.csv`.
- K0002-K0003: Prothom Alo (May 2024): the Tk 152,000-165,000 per-worker payment to syndicate agencies is a general statement, now in the Malaysia syndicate intro, not under Snigdha. Snigdha's own denial (executive director Shahela Parveen) is K0003.
- K0004: the TBS Paltan article names people (Nizam Uddin Hazari, Masud Uddin Chowdhury, Benjir Ahmed, Kashmiri and Nafisa Kamal) and "at least 100 recruiting agency owners", not agencies. The doc now says each owner was among the accused.
- K0005: BSS (11 Nov 2025) names the accused in the four ACC cases. BSS spells the agencies "Adity International" and "R Ving Enterprise". Irving Enterprise (RL0215) is backed by the 19 Jul 2026 gazette. Odity International (RL0983, Active) is a name match only; no "Adity" is on the OEP list, but the doc marks the match as unconfirmed.
- Anonno Apurbo (RL2101): the doc no longer states the Sep 2025 ACC case as fact; it says the Financial Express names an "Apurbo Recruiting Agency", which may be the same agency.
- Uttara International Career Council: Ajker Patrika calls it a "so-called travel agency" (কথিত ট্রাভেল এজেন্সি); it is not on the OEP list (checked the 7 Nov page and the 28 Oct list), so the doc cites the OEP list (A0109) for that.
- A0112: the Bonanza letter is dated 17 Sep 2025 (the agency applied on 15 Sep); the Tk 58,610 is the most the agency may collect from the worker (সর্বোচ্চ), by cheque, bank draft or pay order. sources.csv date corrected.
- Quotes extended to the supporting sentences: N0033, N0038, N0047, N0049-N0051, Q0001, Q0003, C0002, A0112. N0039 and N0042-N0045 keep their figure quotes; the names, the filing date and the denials are cited from K0003 and K0005.

## Compile v2 (8 Nov 2026, facts AG)

- `doc.md` rewritten from the five research notes below plus the earlier work. New sections: "How to use this list" (who is who, six checks before paying, how to read activity versus flags, where to complain and what really happens), "Who is behind the agencies" (licence rules, renting, shared offices, political owners), corridor red flags for Saudi Arabia and the Gulf (women domestic workers; men in Saudi Arabia, UAE, Kuwait, Singapore, Jordan), worker reviews, and a fuller fair-recruitment section that states the search behind "nothing beyond Bonanza". "How the numbers were counted" now covers `activity-other.csv` (ACC counts, press counts from BMET clearance data, OTIT, the 45 low-volume cancellations) and the undercount.
- Our own computation, cited to P0001 plus the ACC facts: for the 21 ACC-case agencies with an RL, ACC counts 113,477 workers; posted BMET letters for the same agencies in Malaysia total 20,663 (18.2%). Japan: of 38 private agencies with Japan letters, 32 are on OTIT's current list and 6 (RL0021, RL0215, RL0384, RL0680, RL0981, RL1101) on its past list; 69 of the 101 approved agencies with an RL have no posted Japan letter. Rechecked by script against `activity.csv` and `activity-other.csv`.
- AG0001-AG0020: complaint-route and pre-payment facts copied from `countries/saudi-arabia/facts.csv` (A0016, A0018, A0023, A0024, A0025, A0036, A0037, A0038, A0039, A0046, A0047, A0048, A0056, A0107, A0108, A0110, A0128, B0171, D0059, SG0005; each row's note names the original id), with their 12 sources copied into `sources/` and registered. AG0021-AG0028: OEP live-page rows for agencies newly named in the doc (RL0275, RL0469, RL0569, RL0776, RL0984, RL1166, RL1175, RL1372).
- `agencies.csv`: 104 rows added (now 293), every RL in `flags-press.csv` with a new-research flag that was not yet listed, except agencies whose only new flag is a Recruitment Advisor review (RL0525, RL0562, RL1073, RL1223). For new rows, `licence_status` is the 7 Nov OEP page, `countries`/`activity` are tallied from `activity.csv`, `flags` are the `flags-press.csv` summaries, and `owners` names the person a source names (else "Need to know"; BAIRA directory pages were not fetched for these). Existing rows got new flags appended from the AB/AC/AE rows, `listed_in` entries for OTIT approval or removal, ACC worker counts, Prothom Alo's no-record finding and the 30 Oct 2025 low-volume cancellation, and `countries`/`activity` filled for the 10 ownership-only rows. The `owners` and `ownership_flags` columns (from the ownership research) sit beside the older `people_linked`.
- Left out of the doc on purpose: Recruitment Advisor reviews of agencies with one or two reviews (too thin), the full 22-agency ACC count table (in `activity-other.csv`), the 2009 and 2011 BMET hearing anecdotes except as evidence of skipped hearings, Bonanza's self-description and bdjobs ad (self-claims), the Meranti Binamas suit (no Bangladeshi agency named), and weak shared-phone links (096 hunting lines; multi-tenant buildings; Bashundhara pair).

## How many workers each agency actually sends (facts AB)

Task: find better evidence of agency volume than BMET's posted permission letters (which stop in Dec 2025 and are only what BMET chose to post). Output: 209 new rows appended to `activity-other.csv` (rows 381 to 589), facts AB0001-AB0049 in `facts.csv`, 11 new sources. Nothing else edited.

### The short answer

No source publishes an agency-by-agency count of workers sent. BMET's statistics, OEP's public reports and the Ministry's pages are by country, district and skill only. The per-agency numbers that exist come from three places, and all three cover Malaysia almost entirely:

- **ACC (Anti-Corruption Commission) cases**, which give the number of workers each accused agency allegedly overcharged in the 2022-24 Malaysia round. These are in effect ACC's count of workers sent through each agency. 22 agencies, 2,845 to 8,592 workers each.
- **Journalists quoting BMET clearance data**: Prothom Alo (May 2024 and Sep 2026), Kaler Kantho (Jun 2024), Samakal citing the CID (Aug 2025).
- **Low-volume findings**: the Ministry's 30 Oct 2025 order cancelling 45 licences because the agency had not sent 100 workers since licensing.

The best new official source is Japan's, not Bangladesh's: OTIT (Organization for Technical Intern Training, the Japanese body that runs the technical intern programme, TITP) publishes the full list of Bangladeshi sending organisations it accepts, with approval and deletion dates. It shows selection, not volume, but it is official, current (6 Oct 2026) and agency-specific.

### What the rows are (activity-other.csv, rows 381-589)

- **Japan, current OTIT list (102 rows).** Every entry on OTIT's "List of Approved Sending Organizations (Bangladesh)" of 6 Oct 2026 except BMET itself (BGD000001), which is listed as a sending body but is not an agency [AB0026]. BOESL (BGD000002) has no RL, as in the other BOESL rows. Each row gives the OTIT number, the date in the row (the approval date, "date of receipt") and the agency's Japan worker total in `activity.csv`. RL numbers are as OTIT prints them; six were in wrapped PDF cells and were read by hand and checked against the OEP name. Two OTIT errors: J K International is printed "RL 2840", the same as J. Alam Trade International; the OEP list gives J K International RL2861, which the row uses. Silvee and Sinthee Travel Agency is printed "RL-149", but RL0149 on the OEP list is Patwary and Brothers Limited; the row keeps RL0149 and says it is unconfirmed.
- **Japan, OTIT past-approved list (21 rows).** Each with approval and deletion dates, one fact each (AB0028-AB0048).
- **Malaysia, Prothom Alo's 17 (17 rows).** The 2026 principals that Prothom Alo, analysing BMET data from Jan 2004 to 23 Aug 2026, found had never sent a worker to Malaysia [AB0001, AB0002]. Mangrove has no RL (the list prints "Mangrove Career Link"; OEP has only Mangrove International RL1756). "অন্বেষা এয়ার" is matched to the principal Annesa Air International RL1786 by name.
- **Malaysia, ACC worker counts (22 rows).** Reused facts N0001-N0012 and N0042-N0051 (already in facts.csv, checked against their saved sources). RLs are the ones in `flags-press.csv`. Every row says it is an allegation of overcharging.
- **Malaysia, Ahmad International (1 row).** Kaler Kantho, citing BMET: 7,869 workers by 24 Apr 2024, against 387 abroad in the seven years before it joined the syndicate [AB0012]. Kaler Kantho prints RL-1146 itself, which confirms the match.
- **Saudi Arabia, Universal Overseas (1 row).** The owner's own claim of 1,400 women in three years (Prothom Alo, Dec 2019), and the agency's suspension on 31 Oct 2019 over women's deaths [AB0024, AB0049]. RL1077 is a name match only.
- **All countries, the 45 low-volume cancellations (45 rows).** Reused C0012 and C0428-C0472. `country` is "All".

### What the new evidence shows

**1. The posted permission letters capture under a fifth of real Malaysia volume.** For the 21 ACC-case agencies with an RL, ACC counts 113,477 workers; our tally of BMET's posted letters for the same agencies in Malaysia is 20,663, about 18%. The gap has two causes: BMET's list starts on 22 May 2023, so the first nine months of the round (Aug 2022 onward) are missing, and BMET did not post every letter. So `activity.csv` ranks agencies roughly right within a corridor but understates every one of them several times over. Don't present letter totals as "workers sent".

**2. The name on the clearance is often not the agency that did the work.** This is the main thing an insider would want written down, and it is now sourced:
- In the 2022-24 round, MPs', a councillor's and party leaders' agencies said publicly they sent no workers; other agencies sent workers in their names [AB0007]. Manpower traders told Kaler Kantho some MPs' agencies sold their demand (চাহিদাপত্র, demand letter) to other agencies at Tk 35,000 per worker [AB0011].
- Agencies outside the syndicate that had their own Malaysian employers sent workers through a syndicate agency and paid it a "chokro fee" (চক্র ফি, syndicate fee) of Tk 152,000 per worker [AB0004]. Riazul Islam, until recently BAIRA's senior vice-president, says at least 817 agencies sent workers that way [AB0005]. In 2016-18 the equivalent was Tk 1.8 lakh per worker from sub-agents to the syndicate members, per a broker quoted by the Daily Star [AB0018].
- Bhaluka Overseas, now a 2026 principal with no Malaysia record of its own, says it previously sent over 1,000 workers to Malaysia, and others to Saudi Arabia, under other agencies' names [AB0003].
- So for Malaysia, BMET clearance figures measure whose licence the visa was processed under, not who recruited the worker. A worker's own agency, the one in the village chain, may not appear anywhere in the data.

**3. Kaler Kantho's BMET reading suggests a quota per agency.** It reports that apart from the first 25 agencies, every agency in the 2022-24 round sent about the same number, 7,000 to 8,000 [AB0011]. That fits the ACC counts (most between 3,000 and 8,600) and points to demand being allocated through FWCMS (Malaysia's Foreign Workers Centralised Management System) rather than won by each agency. Need to know (below) asks how the allocation worked.

**4. The counts disagree with each other, by agency.**
- Ahmed International RL1146: 8,592 (ACC, Mar 2025, N0008); 7,849 (Prothom Alo, May 2024, Q0023); 7,869 by 24 Apr 2024 (Kaler Kantho, AB0012).
- Five M International RL1327: 7,124 (ACC, N0005); 8,592 clearances (Prothom Alo, May 2024, Q0020); 9,370 since 2017 (Samakal citing CID, Q0033). Note that Prothom Alo's 8,592 for 5M is the same figure ACC gives Ahmed International; one of the two papers may have swapped them.
- Catharsis International RL0549: 7,787 (ACC, N0007); 7,102 (Prothom Alo citing BMET, Q0025); 45,287 to Malaysia since 2015 (Samakal citing CID, Q0034, which spans both rounds).
- The differences are partly dates (Apr 2024 vs the round's end in May 2024) and partly what is counted (clearances vs workers overcharged). For the doc, give the ACC figure and cite it as an allegation, since it is the latest and comes with a named authority.

**5. Japan: the OTIT list and BMET's letters agree.** Of 39 agencies with Japan permission letters in `activity.csv`, 32 are on OTIT's current list, BOESL is on it without an RL, and the other 6 are all on OTIT's past list: Al Khamis (45 workers), Amin Tours (19), Mitul Trading (14), Akash Bhraman (5), Unique Eastern (5), Irving Enterprise (4). 69 of the 101 approved agencies with an RL have no Japan letter at all, so approval is not activity.

**6. OTIT delisted the Malaysia-case agencies 11 days after Bangladesh cancelled their licences.** Nine agencies were removed on 30 Jul 2026 (Unique Eastern, Orbitals Enterprise, Irving, Binimoy, Akash Bhraman, Sadia, Catharsis, Al Khamis, Amin Tours) [AB0039-AB0047]. The 49-licence gazette was 19 Jul 2026 (C0002). This is an official Japanese record that matches the press reports of the cancellations. It also settles an open RL question: OTIT prints Binimoy International as RL-351, so RL0351 (not RL0816) is the right match, as `flags.csv` assumed. Thanex RL1779 and Irving RL0215 are confirmed the same way.

**7. Low-volume cancellations vs letters.** Of the 45 agencies cancelled on 30 Oct 2025 for sending under 100 workers, four have posted letters: Japan Bangla Bridge RL1587 (23 workers), Zirabo Overseas RL1458 (40), Mitul Trading RL1101 (14), Al-Sardar RL1722 (5). All are under 100, which fits. Japan Bangla Bridge is still on OTIT's approved list and shows Active on OEP; Mitul Trading was removed by OTIT on 24 Dec 2025.

**8. The 17 with no Malaysia record also have almost no record anywhere.** Our letter tally gives them 0 to 151 workers in total over May 2023-Dec 2025 (Tania Trade 151, Satkhira 112, Jewel Rinku 75, the rest 0 to 40). Prothom Alo gives Bangladesh One Overseas 795 clearances and Bhaluka 235 over their whole history (Q0004, Q0005).

**9. Malaysia's own volume test.** Malaysia's conditions for the 2026 list (sent 27 Oct 2025) included a record of recruiting at least 3,000 foreign workers in the past five years [AB0015]. About 1,000 agencies applied and the Ministry shortlisted about 500 [AB0016]; Prothom Alo says only 163 qualified before conditions were relaxed and 423 were sent [AB0009]. Yet 17 of the 25 picked had no Malaysia record. The 3,000-worker test was not applied to the principals, or was met through workers sent in other agencies' names.

**10. Saudi women: volume is the business model.** Prothom Alo (2019): the Saudi recruitment office deposits at least USD 2,000 in the Bangladeshi agency's account for each woman who arrives, against about USD 1,000 total cost (same source); agencies pay the broker (dalal, দালাল) Tk 40,000-50,000 per woman [AB0022, AB0023]. About 650 agencies were approved to send women, almost all recruiting through brokers [AB0021]; the Ministry secretary told agencies "not one woman knows the agency's name" [AB0025]. BAIRA's secretary general disputed the margin, saying an agency earns no more than USD 200 per worker (in the saved source, not logged as a fact). So for women in Saudi, the agency in BMET's record may be one the worker never dealt with. The figures are from 2019; whether the reverse fee still runs is a Need to know.

### Words people use (for the doc)

চক্র ফি / সিন্ডিকেট ফি (chokro fee / syndicate fee: what an agency outside the syndicate pays a listed agency per worker to process under its licence); চাহিদাপত্র (demand letter, which is what is bought and sold when people say "visa"); ভিসা কেনা (buying a visa: paying the Malaysian or Saudi side for a demand letter, RM 6,000 minimum in 2022-24 per Kaler Kantho [AB0014], RM 8,000-9,000 expected in 2026 per BAIRA members [AB0008]); নামে পাঠানো (sending in another agency's name); ছাড়পত্র (BMET clearance); সহযোগী এজেন্সি (associate agency, the 2026 term for the 312).

### Searched, nothing usable

- **BMET agency-wise statistics.** BMET's statistics pages and annual data are by country, district, skill and gender. No agency-wise table was found on bmet.gov.bd, probashi.gov.bd or OEP (`/reports/country-clearance` and `/reports/geo-clearance-count` are country and district only). One Ministry PDF that came up (office-probashi 99d69219...) has a garbled text layer and could not be read.
- **Parliament answers.** Bangla and English searches for ministers' answers giving agency names with worker numbers found none. Kaler Kantho and Prothom Alo appear to have got BMET's clearance data directly.
- **Awards and rankings.** No Ministry, BMET or BAIRA award for top sending agencies. Agency websites claim "No. 1" (for example a Japan sending organisation calling itself first nationally for intakes), which is self-promotion, not evidence. Notes.md already covers the 2020 grading rules that were never implemented.
- **BAIRA data.** BAIRA publishes a member directory with RLs (other agents saved some `baira-member-rl*` pages) but no volume data.
- **Malaysia FWCMS quotas per agency.** Nothing published. No Malaysian parliamentary answer or press report giving quota by Bangladeshi agency was found.
- **Saudi side.** Musaned (Saudi Arabia's domestic-worker recruitment platform) lists Saudi offices, not Bangladeshi agencies; no per-agency figures found.

### Need to know (one line each, for insiders)

- **Need to know:** in the 2022-24 Malaysia round, how was demand split among the 101 agencies: did FWCMS allot each a fixed number of workers, and who decided it?
- **Need to know:** when agency A sends a worker under agency B's licence, whose name appears on the worker's BMET smart card and on the PDO (pre-departure orientation) certificate, and does the worker get told?
- **Need to know:** is the 2026 chokro fee per worker being charged by the 25 principals to associates, and how much?
- **Need to know:** does a Saudi recruitment office still pay the Bangladeshi agency a per-woman fee (USD 2,000 in 2019), and what is it in 2026?
- **Need to know:** how many workers has each OTIT-approved agency actually sent to Japan? (OTIT's statistics are by country only.)
- **Need to know:** were the 14 agencies cancelled on 30 Oct 2025 that show Active on OEP reinstated (repeats an open item in notes.md; Japan Bangla Bridge RL1587 is one, and it is still on OTIT's list)?

### Sources added (all in sources.csv)

pabn-malaysia-25-new-tactics-ab (Prothom Alo Bangla, 2 Sep 2026; Firecrawl, verbatim body); kk-malaysia-syndicate-2024-ab (Kaler Kantho, 1 Jun 2024; Firecrawl after curl 403, relevant sections verbatim); andyhall-kk-translation-2024-ab (machine-translated repost of the same Kaler Kantho article, kept only because it led to the original; not cited); ds-strict-conditions-3000-ab (Daily Star, 19 Nov 2025); ds-monopoly-kl-2018-ab (Daily Star, 31 Oct 2018); ds-agencies-picked-kl-2024-ab (Daily Star, 2 Jun 2024); ds-syndicate-wins-2024-ab (Daily Star, 8 Jun 2024); ds-ed-must-history-repeat-2024-ab (Daily Star editorial, 31 May 2024; saved but no fact used); pabn-saudi-women-agency-profit-2019-ab (Prothom Alo, 17 Dec 2019; Firecrawl); otit-bgd-sending-orgs-2026-10-ab and otit-bgd-sending-orgs-former-ab (OTIT PDFs, official, curl).

### Pages we could not download

- prothomalo.com Bangla pages refuse curl (connection fails); both were saved with Firecrawl. Not fetched at all: prothomalo.com/bangladesh/o5yotbhsmv ("চূড়ান্ত ছাড়পত্র নিয়েও মালয়েশিয়া যেতে পারলেন না ১৭ হাজার", May 2024), which may give per-agency counts of stranded workers. A teammate could save it in a browser.
- kalerkantho.com returns 403 to curl; saved with Firecrawl.

## Who is behind the agencies (facts AD)

Task: owners and directors, links to politicians and officials, front companies and licence renting (লাইসেন্স ভাড়া, licence bhara). Output: two new columns in `agencies.csv` (`owners`, `ownership_flags`, with fact ids inline in brackets), 10 appended rows, facts AD0001-AD0220, 182 sources registered. No existing cell in `agencies.csv` was changed (checked by script against a copy taken just before the write). `doc.md` not touched.

### What the columns hold

- **owners**: the BAIRA (Bangladesh Association of International Recruiting Agencies) member directory's "Contact Person" and "Designation" for the RL number (baira.org.bd/dir/agency-information/<RL digits>), one AD fact each (AD0001-AD0166), then any press-reported owner, always attributed ("per BSS (Aug 2026)"). BAIRA's field is a contact person with a title (Proprietor, Managing Partner, Managing Director, Chairman), not a shareholder list. For a proprietorship it is usually the licence holder; for a limited company it is one officer. The directory is undated and BAIRA has been under a government administrator since 2024-26 [jugantor-baira-administrator-2026], so entries may be old: it still lists "Md. Shafiqur Rahman Kiron, M.P." and "Benjir Ahmed, Ex. M.P.".
- **ownership_flags**: only links with a source: same office phone or address on BMET's OEP (Overseas Employment Platform) list or in BAIRA, family links reported by the press, ACC (Anti-Corruption Commission) asset probes, and BAIRA members' allegations about a new syndicate. Every allegation names who made it and when.
- Seven RLs have no BAIRA page (the site returns HTTP 500): RL0147 BOESL (state-owned, written as such), RL1400, RL1199, RL1216, RL1428, RL1755, RL2505. Their owners cell says "Need to know".

### The law on ownership (official, OCR of the gazette)

The PDF text layers of SRO 316-Law/2025 and SRO 02-Law/2026 are legacy-font garbage; pages 1-8 of SRO 316 and both pages of SRO 02 were read with Bangla OCR and saved as `.ocr.txt` next to the PDFs. SRO 316 (8 Jul 2025, gazette 14 Jul 2025) replaced SRO 23-Law/2025 of Jan 2025 (`rules-licence-subagent-2025`, kept for comparison: its rule 7 had the same one-licence ban).

- Rule 8(1): no person or agency may hold more than one licence, or a part or share in more than one [AD0167]. The proviso lets a family member (পরিবার: spouse, parents, dependent children, full siblings [AD0169]) get a separate licence only if financially independent, with an office in a separate holding (পৃথক হোল্ডিং, a different building), own income, own trade licence and own staff [AD0168].
- Rule 8(2): a licence cannot be transferred; a proprietorship or partnership converting to a company must keep 51% with the original owner [AD0170, AD0171]. 8(3): no share transfer without government approval [AD0172]. 8(4): no change of chairman, MD or director without prior approval [AD0173]. 8(9): non-resident or foreign shareholders need a mission certificate or NOC [AD0174].
- SRO 02-Law/2026 (5 Jan 2026) created the "associate recruiter" (এসোসিয়েট রিক্রুটার): a licensed agent working through another licensed agent under a written agreement, with workers contracted to the associate and liability shared [AD0175, AD0176]. In effect this legalises what was earlier done informally by renting or "processing under" another licence. The Malaysia 2026 principal/associate structure (Q0008, Q0011) is the same idea.

So the paper rule closes sale and renting; the 2026 amendment opens a lawful way for one agency to work under another's name.

### How licence renting works (press and officials)

- A BMET licence-branch officer told Naya Diganta (Aug 2025) that some owners did not send workers on their own licence but made another person a "partner" by a deal on stamp paper (স্ট্যাম্পে চুক্তি) [AD0177]. The renter used the licence to get on a country syndicate list, for visa processing or for visa trading (ভিসা ট্রেডিং) [AD0178]; some allegedly took migrants' money in the licence's name and vanished [AD0179]. Two Kakrail owners said they had two licences each; one said BMET server-locked one after complaints and he now trades on the other [AD0180]. BMET says it now checks digitally for two licences under one name [AD0181].
- BMET issued a "strict directive" against licence renting in Aug 2023: no one enters the BMET office without showing the licence (Bhorer Kagoj) [AD0182]. The directive itself was not found.
- Amar Sangbad (Sep 2023) quotes Kamal Hossain, who "has long worked by renting various licences"; he alleged BMET officials run the clearance syndicates. The same report has an RV Overseas official saying a last-minute clearance cost an extra Tk 25,000 per passenger [AD0183, AD0184].
- Channel 24 (Dec 2025, Saudi Arabia): the visa of a worker who paid a broker Tk 5.5 lakh was processed by Al-Ihsan; its owner said the worker "bought the visa from Saiful of Maulana Overseas, we only processed it" [AD0185, AD0186]. This is the usual shape: the licence holder files the BMET paperwork, someone else sold the visa and took the money.
- The Abiron death probe (2020) recommended cancelling Airway International's licence, among other allegations for renting it out [AD0187]. RL1016 is a name match only.
- In the 2022-24 Malaysia round, MPs' agencies sold their demand at Tk 35,000 per worker and non-syndicate agencies paid a Tk 152,000 "chokro fee" to send under a syndicate licence (already in facts AB0004, AB0011, AB0007).

Need to know: what does it cost per month or per worker to rent (ভাড়া) a licence today, and is it paid as a flat fee or per visa processed?
Need to know: does BMET check, at clearance, that the worker's contract is with the agency on the file, or only that the RL is active?

### Political and official links found

- **Matco Enterprise RL0250 and Al Saad Labour Supply RL0939.** BAIRA lists Matco's proprietor as "Md. Shafiqur Rahman Kiron, M.P." [AD0013]. BSS (Aug 2026) calls Matco the business of Shariatpur-2 MP Kiron (BNP) and names Farhana Kadir Rahman as its chairman [AD0193, AD0194]; Asian TV (Jan 2026) says she is Kiron's wife [AD0196]. BAIRA lists her as proprietor of Al Saad [AD0065]. OEP gives both agencies the same phone (01711891957) and the same holding, DAG-7014 Islambagh, ground and first floor [A0008, A0039]; BAIRA gives both the identical address [AD0201, AD0202]. Rule 8(1)'s separate-holding condition applies to new family licences; both licences are older (RL0250, RL0939), so whether it binds them is a Need to know. Desh Rupantor (11 Aug 2026) reports BAIRA members' allegation that Matco is among agencies of five BNP MPs and one leader in an attempted new 25-agency Malaysia syndicate, with up to MYR 5 million (about Tk 17 crore) demanded per seat; Kiron denies it [AD0188, AD0189, AD0191]. Matco is not among the 25 principals on FWCMS (Q0001); `listed_in` already shows it as an associate. Kiron told BSS he is sending 216 constituents abroad at his own cost [AD0195].
- **Other agencies named by Desh Rupantor** (BAIRA members' allegation, name match on OEP only): Airway International RL1016 (Jahangir Biswas), Alam Sons RL0165 (Sheikh Farid Ahmed Manik, Suspended on OEP), Surma International RL0299 (BNP leader Gafur Bhuiyan). Not matched: "Rupsha Enterprise" (Ali Asgar Lobi) and "Khandaker Overseas" (Khandaker Abu Ashfaq); OEP has no agency by either name. Rows were appended for the three matched.
- **Abul Bashar family (BH Plaza, Jagannathpur).** Jagonews24 says the late three-time BAIRA president and Jubo League acting president owned "Sarkar Recruiting Agency" [AD0197]; BAIRA lists Sarkar Recruiting Agency RL0226 with chairman Mohammed Abul Basher at BH Plaza, Ka-50/2, phones 55050595-9 [AD0010, AD0198]. OEP puts BNS Overseas RL1450 (son, per Prothom Alo, N0033) on the 7th floor of the same building with phone 55050596, Sarkar on the 8th with 55050597, and PR Overseas RL1928 (son-in-law) at the same address [AD0207, C0367, C0402]. BNS and PR are Cancelled; Sarkar shows Expired (31 Dec 2025).
- **Ex-MPs' agencies (Awami League).** Already in the list (N0013, flags-press). Added: the Financial Express (Aug 2024) report of the ACC allegations that Snigdha got its licence in Dec 2018 and sent only 100 workers in three and a half years, and that Ahmed International had sent 238 before the syndicate, while Benazir Ahmed was BAIRA president [AD0214, AD0215]; plus "many other Awami League leaders, city corporation councillors and new companies" [AD0216].
- **Officials.** No agency owned by a serving official was found. The Ministry's senior secretary told Bonik Barta (Jan 2026) that granting licences is "mainly a political decision" [AD0217]; the white paper says agencies grew powerful through political collusion [AD0218]; Tasneem Siddiqui says the committee recommended removing licences of people holding four or five [AD0219].
- **Benami assets.** The ACC served an asset-statement notice on Prantik Travels MD Golam Mostafa (NTV, Jul 2026), alleging assets beyond known income in his own and others' names [AD0220].

### Front companies and successor offices (OEP and BAIRA data, no allegation)

These are matches in official contact data, written as facts about the data, not as findings of fronting. All pairs found by matching normalised phone numbers across the 2,859 OEP rows and BAIRA addresses for every RL in `agencies.csv`.

- 5M International RL1327 (ex-MP Masud Uddin Chowdhury, Cancelled) and 1 Plus Overseas RL1857 (Active to Mar 2027, BAIRA MD Tasnia Masud [AD0140]): same OEP phone, same BAIRA address down to the floor (Sikder Plaza, House 79, Level 8) [C0350, AD0205, AD0199, AD0200]. Need to know: is Tasnia Masud related to Masud Uddin Chowdhury, and who holds 1 Plus's shares?
- Amin Tours RL0981 (Cancelled; owner Ruhul Amin named by the ACC) and Malaysia Bangladesh Holdings RL1675 (Active, BAIRA MD Shiuley Begum [AD0127]): same address, 95 Road 7 Uttara, and same phone [C0297, AD0206]. RL1675 has 9 posted BMET letters in `activity.csv`.
- Rabbi International RL0258 (Cancelled) shares phone 09612331144 with Al-Baraka RL0603 and Link Up RL0331 (both Active, all in Jagannathpur). 096 numbers are often shared hunting lines, so this is weak.
- Provati International RL0932 (Cancelled) shares a phone with East West Human Resource Center RL0980 (Active).
- Bashundhara Employment Services RL1064 and Bashundhara Overseas RL1252: same OEP address and phone, different BAIRA proprietors. No link to the Bashundhara business group was found; the name alone proves nothing.
- Ahmed International RL1146 and 4 Site International RL0345: same building (Islam Empire Estate, 55/1 Purana Paltan); weak, it is a multi-tenant building.
- New rows for RL1857, RL1675, RL0226, RL1016, RL0165, RL0299, RL0980, RL0603, RL0331, RL1252 have empty `countries` and `activity`: they were added for ownership, not counted. `tools/agency_counts.py` can fill them.

### What was not possible

- **RJSC (Registrar of Joint Stock Companies) records.** Not fetched. Director and shareholder lists for limited-company agencies need a paid certified copy from RJSC; the public name search shows only the company name and number. Need to know: can a member of the public get Schedule X / Form XII (shareholders, directors) for an agency company online at roc.gov.bd, and at what fee?
- **OEP owner fields.** The public OEP agency list has no owner field (name, address, phone, status, validity only). BMET's licence form asks for every partner and director (SRO 316 Form-1), but that is not published.
- **The BAIRA notice PDFs** `baira-notice-member-list-a/b` are scans with no text; not used.
- Fetch failures (HTTP 500): BAIRA pages for RL0147, RL1400, RL1199, RL1216, RL1428, RL1755, RL2505. HTTP 403 then Firecrawl: Jagonews24 (saved as `jago-abul-bashar-dies-2026.md`), Channel 24 (curl got only the title; Firecrawl copy saved as `ch24-licence-rent-searchlight-fc.md`). Dainik Amader Shomoy (Kiron's wife) saved with no article text; Asian TV used instead.
- `trw-manpower-licence-2026` (a law firm's guide) was fetched only to find the official gazette links; nothing is cited from it.
- `deshkal-kiron-sworn-mp` has no readable date or body; not used. Kiron's MP status rests on BSS [AD0195].

### Need to know (for insiders)

- What is the going rate to rent a licence (লাইসেন্স ভাড়া) in 2026, and how is the "partner" stamp-paper deal written?
- Since SRO 02-2026, are informal licence rentals being re-papered as "associate recruiter" agreements?
- Has BMET or the Ministry acted on any agency under rule 8(1) for a second licence held through a family member?
- Who are the shareholders of 1 Plus Overseas RL1857 and Malaysia Bangladesh Holdings RL1675?
- Which agencies do Ali Asgar Lobi ("Rupsha Enterprise") and Khandaker Abu Ashfaq ("Khandaker Overseas") own, by RL?
- Is RL1016 M/S Airway International the same Airway International named in the 2020 Abiron probe?

## Red flags on Gulf and other big-corridor agencies (facts AC)

Scope: Saudi Arabia, UAE, Qatar, Oman, Kuwait, Jordan, Singapore. 133 rows appended to `flags-press.csv` (after row 153), facts AC0001-AC0065. Every row attributes the claim to who made it and when; RLs were matched against `data/oep-agency-list-2026-10-28.csv`, and each summary ends with the agency's status on that list. No rows in `flags.csv` were touched.

### What was added, by source

- **Saudi women domestic workers, 2019 (Prothom Alo, 17 Dec 2019; AC0001-AC0016).** Four lists from one article: 15 licences suspended on 31 Oct 2019 over 16 women who died by suicide or were killed in Saudi Arabia; 2 suspended over Sumi Akter (returned abused); the Bangladesh embassy in Riyadh's 21 Nov 2019 letter naming 6 agencies that raised a woman's age, 7 that lowered it below the 25-45 band, 18 that sent women without training or a medical test, and 12 without proper training. 13 of the 14 age-fraud agencies were then suspended pending inquiry; the article doesn't say which one was spared, so the age rows don't claim a suspension for any single agency. All matched by name (all 2019 names found at 0.88 or better except "Winter Overseas", left without an RL). These are 2019 suspensions; nearly all of these agencies show Active today. That matters: several are now big Malaysia or Qatar senders (Tania Trade RL0436, Vely Trade RL1268, Rifa RL0693 and Neighbour Associates RL0746 are 2026 Malaysia principals; Barcelona Overseas RL1380 has the largest Qatar letter in `activity.csv`).
- **ACC case of 3 Jul 2025 (Daily Star; AC0019-AC0021).** HA International RL0469, Tasnim RL0569, Makka (Mokka) RL1175, S.M. Manpower RL1372 and "KH Overseas" (not matched; Gazipur Kontho lists "KS Overseas" RL1422, which may be the same agency), with four BMET officials. The trick the ACC alleges: a first-time woman is passed off as a returnee (ফেরত কর্মী) by putting someone else's passport number into the BMET system, which skips the checks a first-timer faces. The same ACC case also covers clearance for four women under 25.
- **The 57-agency ACC inquiry (Gazipur Kontho, 27 Jul 2026, citing Asia Post; AC0022-AC0032).** The source prints RL numbers, so the match is by RL. Two RLs don't fit the printed name: RL1968 ("Ajaj Business International"; OEP says Al Gassim Overseas) and RL1901 ("Future Palace"; OEP says F.R Trade International). Both rows carry that warning. BOESL RL0147, the state agency, is on the list. Goodness Service RL2068, General Trading RL0320 and Rifa RL0693 already had a Prothom Alo row for the same list, so they weren't added again. This is an inquiry (অনুসন্ধান), not a charge sheet.
- **UAE smart-card fraud (Samakal, 7 Oct 2022; AC0033-AC0041).** The Ministry inquiry found 6,938 BMET smart cards (emigration clearance cards, স্মার্ট কার্ড) issued on permissions for 2,960 workers. Six agencies are named with licence numbers. The Trade Fair International RL0431 says cards were printed in its name without its knowledge; its row is worded that way. How it worked: extra cards were made on an existing permission by editing the immigration software, then sold to brokers (আদম ব্যাপারী, দালাল) who sent people on UAE visit visas with no job, at Tk 3-4.5 lakh each.
- **Deaths and arrests.** Nodi Akter (Daily Star, Oct 2020): the paper gives "Dhaka Export (RL-275)", but OEP's RL0275 is Punam International and no "Dhaka Export" appears; Dacca Exports is RL0265. Left without an RL and flagged as a mismatch. Umme Kulsum / M H Trade International RL1166 and Star Line Associate RL0776 were already in `flags-press.csv` (another agent's rows), so they weren't duplicated; AC0045-AC0048 hold extra detail (RAB said it would use the trafficking act; the agency owners' group protested the arrest).
- **Kuwait (Daily Star, Aug 2020; AC0049-AC0051).** Job Bank International RL1183, owned by MP Papul's brother: per CID and court sources, people were sent through it to Papul's Marafie Kuwaitia at Tk 5-7 lakh each.
- **Singapore (Ittefaq, Nov 2022 and Mar 2023; AC0052-AC0056).** The Gazipur Air International RL0891, Al Jannat Overseas RL0926, RX Care RL1240 and Welltech Employments Services RL1254 (Ittefaq: "Weltec") allegedly kept sending through a test centre whose Singapore BCA approval had been cancelled. Ittefaq says the inquiry proved it and nothing was done. RL0891 is also on the 2019 Saudi suspension and no-medical lists, which makes it the most repeated name in this set. "Oasis Overseas Services" (show-caused for 3,037 clearances after it was dropped from the list) has no sure OEP match.
- **Jordan, unlicensed (New Age, 16 Jun 2026; AC0063-AC0065).** Surah Travels and Traders, North Badda: CID found 55 passports (Jordan and Saudi), used Jerash Garments' name and seal, Tk 2 lakh each, no licence. It shows the most common Jordan trick: a travel agency (not an RL holder) sells a "garments visa" (গার্মেন্টস ভিসা) in a real factory's name.

### Context facts with no agency attached (for doc.md, if the editor wants them)

- AC0057-AC0059 (Prothom Alo, Mar 2023): a Saudi citizen can get a visa to hire one worker by depositing SR 2,000, with no capacity check, and sell it on. Appointment letters are checked by the Ministry only when more than 25 come at once. BMET's DG said more than half of Saudi visas come singly (the "single visa" or "free visa" trade, ফ্রি ভিসা / আজাদ ভিসা) and only the visa's authenticity is checked.
- AC0060-AC0061 (Bonik Barta, 2026): one Oman spouse-visa approval letter was used for five women on different passports. The state minister said BMET can verify visas for only four or five countries.
- AC0062 (Janobani, Jun 2026): sources allege Qatar-bound workers pay Tk 4-6 lakh and get BMET clearance on unattested visas (no Qatar embassy attestation). No agency is named, so there's no row.
- AC0013-AC0014 (2019 agency economics): an agency pays a broker Tk 40-50k per woman and the Saudi agency pays it at least USD 2,000 on arrival. That is why women "go free" while brokers still collect from them.

### Searched, nothing usable

- BMET mobile courts (ভ্রাম্যমাণ আদালত) against a Gulf-route agency: the only 2025-26 case found is Triple A Overseas RL2630 (Malaysia), already listed. Need to know: has BMET's vigilance team run a mobile court on any Saudi, Qatar or Oman sender since 2024, and where are the results posted?
- Netra News (Oct 2026) on women in Saudi Arabia names no agency.
- Jugantor (Sep 2026) on Saied Romania Overseas: a five-year sentence under the 2013 Act, but no destination given and outside this scope.
- Not fetched: the Prothom Alo 2019 follow-up on the 166-agency shutdown (VOA reports 166 agencies closed after Saudi abuse claims). Need to know: was the full list of the 166 agencies suspended in Nov-Dec 2019 ever published, and by whom?

### Need to know (for insiders)

- Which agency was the 14th in the 2019 age-fraud list, the one BMET did not suspend?
- What came of the 2019 Saudi suspensions: lifted after a hearing, fined, or deposits forfeited? Nearly all show Active today.
- Did the ACC's 57-agency inquiry become a case, and against which agencies?
- Is "Dhaka Export (RL-275)" in Nodi Akter's case Dacca Exports RL0265, or an agency whose licence has since been reissued?

## Worker-side evidence by agency (flags-press.csv rows, facts AE)

Task: add evidence that comes from workers' side, not from the ACC (Anti-Corruption Commission) or licence actions: BMET (Bureau of Manpower, Employment and Training) complaint and arbitration outcomes that name an agency, mobile courts, Recruitment Advisor reviews, NGO case files, and court cases brought by workers. 34 rows appended to `flags-press.csv` (now 152 rows). Facts AE0001-AE0061 in `facts.csv`. All 36 new sources are saved in `sources/` and registered in `sources.csv`.

Every row is a report of what someone said or did (a worker, RAB, police, BMET, a newspaper). None is a finding of guilt unless the summary says a court or BMET decided it.

### New flag types in flags-press.csv

The earlier rows use allegation, ownership-link, complaint and positive-evidence. This batch adds types that say where the evidence comes from:

- **worker-complaint**: a named worker's complaint to BMET, as reported, with no outcome or an unpaid one.
- **bmet-arbitration-award**: BMET decided and money was actually recovered.
- **worker-review**: Recruitment Advisor reviews (the ITUC's, the International Trade Union Confederation's, review site).
- **arrest**: RAB, APBn, CID or police arrested the owner on workers' complaints. An arrest is not a conviction.
- **court-case**: a writ or case in a Bangladeshi court naming the agency.
- **mobile-court-fine-sealed** and **mobile-court-conviction**: an executive magistrate's on-the-spot sentence.
- **fabricated-case**: the agency is the reported victim of a staged case.

### How the BMET complaint actually works

What the sources show, step by step:

1. **Filing.** A worker, or more often a relative at home, files a written complaint (অভিযোগ) at BMET's Kakrail office, or through the online form. Migration Concern lists what to attach: work permit, visa or NOC, appointment letter, money receipts, and video or audio up to 10 MB [AE0053]. BMET's DG said in 2024 that the 64 district employment offices (DEMO) would investigate complaints and that officers were being trained for it [bb-bmet-complaint-61pc]. In 2025 a Monitoring and Enforcement wing was set up to take complaints filed directly at BMET (RMMRU's Tasneem Siddiqui) [AE0010].
2. **Hearing (শুনানি).** BMET writes to the agency and calls both sides. Registered complaints are heard with the agency's representative present; BMET checks the work permit and, for Saudi Arabia, asks the agency to contact the employer [AE0009]. In one 2023 hearing over a Saudi job switch, BMET gave two weeks and told the agency to bring the worker's iqama next time [AE0021]. Agencies often skip hearings or ignore BMET's letter: Soul Associate never answered BMET's letter in 2023 [AE0006]; Al-Selim attended three of five hearings in 2009 [AE0048]; BD Associates skipped the first two in 2011 [AE0049].
3. **Settlement (আপস, সালিশ).** BMET calls it arbitration; workers call it salish. In practice it is a negotiated compromise. Officers and agency staff press the worker to accept a small sum: Tk 15,000 offered against Tk 4.5 lakh spent (2011) [AE0049]; women's awards of Tk 5,000-20,000 in 54% of 38 resolved cases OKUP followed (2019), with only 31% of 123 complaints resolved by Dec 2019 and 48 of the 85 unresolved never called to a hearing [AE0057, AE0058, AE0001]; OKUP's chair says proven cases settle for Tk 30-40k for women and Tk 50-60k for men [N0054]. BMET counts the unpaid salary as the compensation; the migration cost and the harm are not counted [AE0058]. A representative told a woman, in front of the BMET officer, to come to the agency's office to settle or get nothing [AE0059].
4. **Enforcement.** If the agency refuses to pay, BMET refers the case to the Ministry, which can order payment; in 2009 the worker still had not been paid months after the Ministry's order [AE0048]. A BMET director said in Jan 2024 that many agencies' "servers were locked" (সার্ভার লক) over serious complaints [AE0050]. Our reading (not stated in any source): "server lock" blocks the agency's access to BMET's online clearance system, so it cannot process new workers, and the OEP list status "Server Locked" (9 agencies on 28 Oct 2026, including Banna Bijoy RL1314 and Alam Overseas RL1647) is the same lock. The licence-deposit (জামানত) route exists too: in 2017 the High Court ordered one agency's licence cancelled and its deposit paid to nine workers who had paid Tk 24 lakh, and by 2021 they had still not received it [AE0015].

Scale (BMET figures as reported, complaints / settled / recovered): 2019: 732 / 375 / Tk 2.57 crore; 2020: 905 / 424 (Bonik Barta) or 481 (Daily Star op-ed) / Tk 2.40 crore; 2021: 528 / 240 / Tk 1.82 crore; 2022: 1,240 / 339 / Tk 1.60 crore; 2023: 2,380 / 865 / Tk 4.88 crore; 2024: 6,755 / 1,755 / Tk 6.32 crore; 2025: 4,900 / 2,054 / Tk 9.92 crore [AE0004, AE0008, AE0014, AE0019]. Over 2019-2023, 61% of complainants got no remedy [AE0004]. Over 90% of 2025 complaints were about Saudi Arabia (no iqama, no work, late pay) [AE0047]. The 2020 figures conflict (424 vs 481 settled); both papers cite BMET.

The receipts problem is the core of it. Agencies take Tk 4-5 lakh against an official Tk 1.2-1.5 lakh and give no written receipt, so the worker cannot prove what was paid and BMET will not award it (Tasneem Siddiqui, RMMRU) [AE0007]. A worker who has only the BMET permission-letter figure (for example Tk 58,610 on Bonanza's Saudi letter, A0112) can claim only that.

Agencies' side: BAIRA's president said in 2023 that 80% of complaints are false and that "a circle" around BMET with some NGOs pushes migrants to file them; BMET's DG answered that more than half are genuine [AE0020]. BAIRA's Tipu Sultan says the Saudi employer, not the agency, is to blame when there is no iqama, and the embassy should act [inqilab-bmet-complaint-pile]. There is at least one reported staged case: RAB says a worker's wife filed a fake kidnapping and trafficking case against Creative International and withdrew it after the agency paid Tk 10 lakh, then a second woman filed a near-copy in 2025 [AE0018]. So complaints are leverage both ways.

### Criminal cases and courts

- Since late 2021, police may not arrest a licensed agent directly on a trafficking victim's case; the case goes first to BMET for negotiation, and prosecution starts only if that fails (decision at a home ministry meeting, reported by the Daily Star with audio) [AE0025]. BMET's then DG on tape: "Why would they catch those who have valid licences and drag them to court?" BRAC Migration's Shariful Hasan: trafficking "cannot be dealt by negotiation and arbitration". Need to know: is this 2021 BMET-first rule still applied by police in 2026?
- Conviction rates: 538 trafficking cases in 2020, 14 disposed, one conviction [AE0027]. OKUP followed three OEMA (Overseas Employment and Migrants Act 2013) cases by returnee women in Narsingdi and Faridpur: none decided by July 2020; accused agents pressed two complainants to withdraw with a lump sum and attacked one [AE0061]. A Narsingdi tribunal (case 22/19) dismissed a trafficking case, holding that recruitment by a licensed agent with government approval "must not be labeled" trafficking [AE0060].
- Arrests on workers' complaints, named agencies: MH Trade International RL1166 (owner arrested Sep 2020 after 14-year-old Umme Kulsum died in Saudi Arabia; the agency had her passport show age 25) [AE0023, AE0024]; Star Line Associate RL0776 (owner detained May 2023, domestic worker sent without training or BMET smart card) [AE0022]; Concord Apex RL0984 (owner jailed pending bail Aug 2022; RAB claims 2,500 women trafficked, lured with a free Hajj) [AE0016, AE0017]. All three still show **Active** on OEP. No outcome of any of these cases was found.
- Writs: the Oct 2018 High Court rule on the G2G Plus ten was brought by ten rival agencies, not workers [AE0011, AE0012]. The 2024 writ on the 17,777 workers who held BMET clearance but missed Malaysia's 31 May 2024 deadline was a public-interest writ (Advocate Tanvir Ahmed); the government told the court agencies must refund by 18 July 2024 and that charges above the Tk 78,990 ceiling would be settled; in Apr 2025 the Ministry's committee report put the blame on the agencies, and the court asked what action and refunds had happened [AE0028, AE0029, AE0030]. No list of the agencies or refund amounts was published that I could find. A TBS feature ("After losing lakhs to 'syndicate'...", seen in search results, not saved) quotes workers who got half or nothing back; save it before citing.
- Abroad: 33 Bangladeshi workers sued Malaysian firm Meranti Binamas Sdn Bhd and the Malaysian government at the Shah Alam High Court (filed Mar 2025) over RM25,000 each paid for jobs that did not exist [AE0054]. The suit as reported names no Bangladeshi agency.

### Mobile courts

The only BMET mobile court naming a licensed agency in 2025-26 is Triple A Overseas RL2630 (10 Sep 2026, China Tower, Naya Paltan; sealed, Tk 50,000 fine, three boxes of passports seized from Malaysia-bound workers before any official call) [AE0002, AE0003]. Already in `flags.csv` as C-fact; added here with the press sources. Other mobile courts hit unlicensed brokers: 12 brokers sentenced near BKTTC Mirpur in Oct 2026 for taking Tk 40,000 to Tk 10 lakh promising jobs and exam passes, on complaints from BKTTC and BOESL [AE0056]. The trick: brokers stand outside the government training centre and sell "guaranteed" places on routes (Korea EPS, Jordan via BOESL) that the government runs free or at a fixed low fee.

### Recruitment Advisor

The earlier note ("1,444 agencies, 0 to 2 reviews") holds for most, but a handful have real numbers: Bangladesh Export Corporation RL0803 58 reviews, TM Overseas RL0498 29, Just Way Aviation RL0726 11, Modhu Overseas RL1223 7, Elegants RL0544 4, Biplob Overseas 4, Odity RL0983 3 (found by a site search; there may be others). Almost all were posted Nov 2022 to Feb 2023 in the same English phrasing ("reliable but expensive. I paid X BDT ..."), so they look like a survey team entering interviews, probably the ITUC/partner survey of 835 workers already noted (N-agent). They are still the only per-agency, per-worker price data found.

What they say about prices, which matches what insiders report: women domestic workers paid Tk 20,000-120,000 for Saudi Arabia, Jordan, Lebanon and UAE, although women's domestic work in Saudi Arabia is meant to be free to the worker; men paid Tk 100,000-600,000 for Saudi Arabia, Tk 250,000-380,000 for Malaysia, Tk 300,000-400,000 for UAE, Oman and Kuwait, Tk 350,000-450,000 for Bahrain, Qatar and Lebanon, and Tk 950,000 for Singapore [AE0033-AE0045]. Reviews are mixed for every agency: the same agency gets "free, got the job" and "fake contract, re-entry ban". Niloy International's only review lists the agency's own phone and website, so agencies do post reviews of themselves [AE0046].

### Agencies in agencies.csv touched by this batch

Odity International RL0983 (already flagged for ACC; 3 mixed reviews), T.M. Overseas RL0498 (29 reviews), and the G2G Plus ten (court rule). Agencies not in agencies.csv that a compiler may want to add: Bangladesh Export Corporation RL0803, Star Line Associate RL0776, MH Trade International RL1166, Concorde Apex RL0984, Arabian Services Company RL0783, New Hope International Overseas RL2424, Soul Associate RL1037, Path Finder International RL1298. I did not edit agencies.csv.

### RL matching

By name against `data/oep-agency-list-2026-10-28.csv`, checked by address where the source gives one. Confident: Triple A RL2630 (RL in source), MH Trade RL1166 (RL in source), Arabian Services RL0783 (RL 783 in source), Star Line Associate RL0776 (Naya Paltan in both), Concorde Apex RL0984 (Naya Paltan), Bangladesh Export Corporation RL0803, T.M. Overseas RL0498 and Just Way Aviation RL0726 (addresses match), Shanjari International RL0742 (exact name). By name only: Soul Associate RL1037, Path Finder RL1298, Modhu Overseas RL1223, Elegants RL0544, Al Karim RL1073, Jahan RL0562, Niloy RL0525, Al Salim Overseas Agency RL0487 for "Al-Selim Overseas" (2009). New Hope International Overseas RL2424: Inqilab says Naya Paltan, OEP says Shantinagar; may be the same agency after a move, or not. No match: Creative International, BD Associates, Biplob Overseas, SM Enterprise (unlicensed by CID's account).

### Need to know (for insiders)

- **Need to know:** does BMET publish or give out its arbitration decisions (সালিশ নিষ্পত্তির আদেশ) by agency, and can a worker get a copy of the order naming the agency and amount?
- **Need to know:** what does "Server Locked" on the OEP list mean in practice: is it BMET's lock for unpaid complaints, and does paying the award unlock it?
- **Need to know:** at a BMET hearing in 2026, what does a worker without a receipt get: only the permission-letter cost, or nothing?
- **Need to know:** was any of the 2020-2023 arrests (MH Trade, Concord Apex, Star Line) followed by a charge sheet or conviction?
- **Need to know:** which agencies refunded the 17,777 Malaysia workers, and how much, per the Ministry's reports to the High Court?
- **Need to know:** is the 2021 rule that police send cases against licensed agents to BMET first still in force?

### Searched, nothing usable

- BMET's own website: no list of arbitration decisions or agency-wise complaint counts. The notice I opened (`bmet-notice-6922e974`, saved) turned out to be a 2021 list of 15 new licences, not used.
- WARBE, BRAC Migration Programme and OKUP case files naming agencies: none public. OKUP's 2021 report and the 2025 study (114 cases) give patterns, not names; the 2025 study itself was not found online, only the Daily Star editorial [AE0031, AE0032]. BRAC's public material gives returnee totals, not agency names.
- Labour or civil courts awarding a worker money against a named agency: none found.
- Facebook groups and YouTube: not searchable with the tools I have; a web search returned a YouTube video on the 49 cancelled licences (not used). A teammate with Facebook access could search groups like "সৌদি প্রবাসী" for named-agency complaints.
- Prothom Alo 31 Aug 2026 (CID arrest of Salman Hossain, Saudi torture case): names no agency, not used.

### Pages we could not download

- jagonews24.com/national/news/956207 (Malaysia refunds): 403, not retried.
- kalbela.com/national/326993 (Malaysia fraud, agency fined): 403 by curl; probably Triple A again, not retried with Firecrawl.
- kalbela.com/capital/300032 and dailyinqilab.com/national/article/635350: 403 by curl, saved by Firecrawl (article text copied verbatim into `.md`).

## Evidence of fair recruitment (positive evidence)

Research notes for the "Agencies with evidence of fair recruitment" section of doc.md. Facts are AF0001-AF0054 in facts.csv (all quotes checked against saved copies, except AF0011, read from the scanned letter's page image). doc.md and agencies.csv were not edited.

### Bottom line

Bonanza Overseas (RL0579, Active on OEP until 31 Dec 2028) is still the only Bangladeshi private agency with outside, independent evidence of fair recruitment. No second agency qualifies. The search below covered certification lists, ILO/IOM pilots, employer-pays programmes, worker-review data and Bangla news. What did turn up is evidence on *channels* (state-run BOESL and G2G schemes), not on private agencies, and a body of expert opinion on why no private agency has a fair-recruitment record.

### Bonanza: what the evidence actually shows (strengthens the existing entry)

The pilot was not Bonanza acting alone. The Qatari side moved first: STS, the service company that places workers on QDVC construction sites, adopted a no-fee policy in January 2018 before the ILO pilot began [AF0003]. Bonanza was STS's long-time agency in Bangladesh and agreed to join [AF0002]. The mechanics that made it work: the STS-Bonanza service agreement was rewritten to bar any fee or cost to the worker, with an itemised list of what the employer pays [AF0004]; Bonanza advertised in local media and recruited directly in villages to cut out the fee-taking sub-agent (দালাল, dalal) [N0024]; it set up grievance forms and a call-centre before departure [AF0005]. Workers' average cost went from USD 3,408 to about USD 300 [N0025]; what they still paid was mostly the passport and their own travel and lodging during recruitment [AF0006]. STS fired 21% of pre-pilot recruits in their first 18 months and none of the post-pilot ones [AF0007].

A second, independent source exists: the ILO says Tufts University ran the impact assessment [AF0008], and Tufts researchers published a peer-reviewed evaluation of a 2017-2020 Bangladesh-Qatar construction recruitment intervention with 598 workers: lower fees, less felt obligation to migrate [AF0009]. One finding cuts the other way and is worth keeping: job satisfaction and trust in the employer were higher among conventionally recruited workers; the authors read this as people who paid a lot convincing themselves it was worth it [AF0010]. The abstract does not name Bonanza; link it to the pilot only through the ILO's Tufts statement.

Does it carry on after the pilot? Partly yes, on paper. A Ministry permission (নিয়োগানুমতি) dated 28 Nov 2024 lets Bonanza send 210 workers to Urban Hospitality Services, Doha (cleaners, cooks, waiters, technicians, drivers, QAR 1,000-2,000), with air ticket, visa, food, housing and insurance paid by the company and the most the agency may take from each worker (সর্বোচ্চ অভিবাসন ব্যয়) set at Tk 19,560 [AF0011]; a May 2025 BMET permission covers more posts for the same employer [AF0012]. Compare Bonanza's Saudi letter of Sep 2025, which lets it take up to Tk 58,610 [A0112]. So the low-cost Qatar line continues with a different employer (hospitality, not STS/QDVC construction), but it is a ceiling, not a record of what workers paid. Bonanza advertises jobs openly on bdjobs (a 4 Jun 2025 ad for 20 Saudi loading workers) [AF0053] and calls itself "100% Ethical Recruitment" on its own site [AF0052]; that is a self-claim, not evidence.

Suggested wording for doc.md (owner's call): keep the Qatar-only caveat; add that the employer (STS) adopted no-fee first, that an independent Tufts evaluation confirms lower fees [AF0009], and that its 2024 Qatar hospitality permission caps the worker's cost at Tk 19,560 against Tk 58,610 on its 2025 Saudi permission [AF0011, A0112].

- **Need to know:** what Bonanza's Urban Hospitality recruits actually paid in 2024-25, including any sub-agent's cut. A returnee from that batch could answer.
- **Need to know:** whether Bonanza's Saudi recruits pay the Tk 58,610 ceiling, less, or more.

### Certification: nobody from Bangladesh

- **IRIS** (IOM's ethical recruitment certification): the public list of recruiters that have applied, updated Aug 2026, has five names, from Singapore, Poland, Nepal, Kenya and Mexico; none from Bangladesh [AF0013]. IOM announced IRIS's launch in Bangladesh in Feb 2019 and set up a technical working group with BAIRA (Bangladesh Association of International Recruiting Agencies) [AF0014]; at that launch the government and BAIRA said an employer-pays model was the answer [AF0015]. Seven years on, no Bangladeshi agency has applied.
- **Other schemes** (On The Level, Clearview, the Responsible Business Alliance's programme): no Bangladeshi agency found. Andy Hall (Jan 2024) reports IRIS audits cost over USD 1,000 and On The Level about USD 8,000 per agency [AF0001], and that the two Myanmar agencies first certified under On The Level got less business afterwards, not more [AF0018].
- **Government "CIP" status:** the Ministry gives top agencies "Commercially Important" certificates, which IOM describes as recognising performance and quality [AF0047]. Need to know: the criteria. If it is remittance or worker volume, it is not fair-recruitment evidence and should not be cited as such.
- Training is not certification: the MPI (Migration Policy Institute, 2023) found about 600 agencies listed as IRIS-trained against two applicants [AF0016].

### Zero-cost and low-cost channels that held up (state-run, not private agencies)

These are the only channels with outside evidence that workers paid close to the official cost. None is a private agency.

- **Malaysia G2G, 2012-15 (plantations):** BMET's own breakdown put the cost at Tk 32,100, 69% of it airfare [AF0019]; the ILO adds Tk 8,000-10,000 for passport and trips to Dhaka, so about Tk 40,000 [AF0021], against Tk 2.5-3 lakh through private agencies at the time [AF0020]. A randomised evaluation found G2G raised migrants' three-year net earnings by 87% [AF0026]. The catch: only 7,616 went by June 2015 [AF0022], 0.52% of the 1.45 million people registered [AF0023]. It was then replaced by "G2G Plus" and agency syndicates (see red flags).
- **Korea EPS via BOESL:** about USD 900 against over USD 4,000 privately [AF0024]; the 2018 MoU fixes each fee (language test, passport, visa, medical, airfare) [AF0050]. Volume is small: 16,721 in 2008-17 [AF0025].
- **Jordan garments via BOESL (women):** workers interviewed by the ILO in 2018 paid Tk 14,000-25,000 including BOESL's fee, passport, medical and fingerprints; a Tk 10,000 deposit some paid to BOESL was refunded after arrival [AF0028]. It still leaked: one woman paid a dalal Tk 65,000 (first asked Tk 1.3 lakh) and believed she would not have passed BOESL's sewing test without him [AF0029], and a worker alleged dalals bribe BOESL interviewers and mark their candidates, for example with a nail-polish colour on a set finger [AF0030]. That is an allegation by one worker reported by the ILO, not a finding.
- **Women domestic workers to the Gulf:** in the ITUC's Recruitment Advisor survey, the only respondents who paid nothing (103 of 835) were women domestic workers [AF0033]. Other agents' worker-review rows show women domestic workers still paying from Tk 20,000 up to Tk 70,000-120,000 at some agencies (AE0033, AE0038), so "free" here is the norm on paper, not a guarantee.
- **IOM's summary:** G2G deals through BOESL with Korea, Jordan, Hong Kong and Seychelles have "significantly lowered" costs [AF0048].

### "Zero cost" offers that have not been tested yet, or were run by flagged agencies

- **Malaysia 2026:** the 8 Apr 2026 joint statement says the Malaysian employer pays everything under the ILO employer-pays principle [AF0039]; the minister said 10,000 workers would go first at zero cost, with priority through BOESL [AF0037]. BOESL's first concrete notice is 112 jobs at DHL Supply Chain (Malaysia), RM 1,700 basic, chosen by software lottery (300 shortlisted) and then the company's own tests, with a warning not to pay anyone [AF0038]. Too new to judge. Need to know: what the first DHL and other zero-cost batches actually paid, once they have flown.
- **The 2023 "Zero Cost Migration" batch:** a TBS-published press release (20 Jun 2023) said 20 workers flew to Malaysia "at zero cost", run by Ruhul Amin Shawpon of Catharsis International (RL-0549), with the job allocated to Imperial Resources (RL-1874) through JG Alfalah Management (RL-1861) [AF0035, AF0036]. All three licences show Cancelled on OEP [C0194, C0400, C0399], and Catharsis and Ruhul Amin are named in the syndicate allegations under red flags (they deny them). This is a press release, not evidence; do not list any of the three as positive. It shows how "বিনা খরচে" (free of cost) is used as marketing.
- **Saudi Arabia:** the Saudi ambassador said in May 2023 that Saudi employers pay every recruitment fee, including ticket, medical, police report and biometrics, that no worker should pay anything, and that "ফ্রি ভিসা" (free visa) no longer exists [AF0031]. Yet BMET's own 2025 permission lets an agency take up to Tk 58,610 from a Saudi construction worker [A0112]. Insiders should check this gap. Need to know: what the Tk 58,610 is for (BMET clearance, welfare fund, training, agency service charge) when the employer pays the ticket and visa.
- **Malaysian glove makers:** MARGMA members adopted zero fees from April 2019 and, after US import bans, repaid MYR 350-400 million in fees [AF0044]; Top Glove alone says it repaid over MYR 150 million to more than 13,000 workers [AF0046]. Workers were repaid in Malaysia after the fact. That is evidence that the employers paid, not that any Bangladeshi agency stopped charging. No source names a Bangladeshi agency that got through the glove makers' agency vetting. Need to know: which Bangladeshi agencies the glove makers kept on their approved lists after 2021.

### Why there is nothing else: what the sources say

- **The sub-agent sits outside the agency's control.** 78% of returnees in the ITUC survey found their job through a sub-agent or broker [AF0032]. The World Bank (2023) noted that dalals fell outside the Migrants Act 2013 [AF0027]; the sub-agent rules came later, so this needs checking against the current law.
- **The money is too big and too normal.** Mean cost Tk 417,000 (BBS 2020 survey, via the ILO) [AF0045]; about USD 5,000 for Malaysia (Verité 2024) [AF0049]; 2022-24 Malaysia workers up to Tk 5-6 lakh against an official Tk 79,000 [AF0040]. Even workers who called their fee "affordable" paid about Tk 150,000 (men) [AF0034].
- **Fair agencies get undercut.** MPI: ethical standards raise an agency's costs, and rivals who ignore them can undercut it [AF0017]; Andy Hall: certified agencies got no business gain [AF0018].
- **Expert view on employer-pays in Bangladesh.** Prof. C R Abrar (RMMRU): employer-pays "has never been implemented"; dalals inflated costs at each step [AF0041]. Researcher Harun-or-Rashid: under ILO rules the worker should pay only for the passport [AF0043], and Malaysia's new agency conditions (5 years' experience, 3,000 workers in 3 years, a 10,000 sq ft office, own training centre) will push costs up [AF0042]. The ITUC calls employer-pays "the best way" to fair recruitment [AF0054]. In Qatar more widely, Impactt found 90% of the World Cup supply-chain workers it sampled in 2023 still paid fees, averaging USD 530 [AF0051]. Fair recruitment held where one employer insisted and paid, as in Bonanza's case, not across the market.

### Searched, nothing usable

- IRIS list (Aug 2026), On The Level, Clearview, RBA: no Bangladeshi agency.
- IOM/Colombo Process fair-recruitment report: describes RAIMS (BMET's online agency registry), the women-recruitment licence (60 agencies as of 2023) and CIP status; names no agency.
- Impactt's ethical-recruitment report for trade unions: mentions Bangladesh once, no agency.
- Recruitment Advisor (ITUC): the 2023 survey names no agency; per-agency reviews are thin (covered by AE facts).
- Searches for Bangladeshi agencies in employer-pays programmes of hotels, electronics or palm-oil companies: none named in any public source found.
- IOM Bangladesh posts on IRIS training of agencies (Facebook, LinkedIn 2025): could not be opened (Facebook post not fetched; LinkedIn unsupported by Firecrawl). Need to know: which Bangladeshi agencies took IOM's IRIS training in 2025, and whether any applied for certification.
- IOM mapping study of recruitment practices in Bangladesh (bangladesh.iom.int): download failed earlier; worth an upload.

### Sources added this round

Registered: iom-colombo-fair-recruitment-2024-fc (excerpt only, directQuote scrape), iom-iris-bangladesh-launch-fc, ituc-ra-bangladesh-monitoring-fc (excerpt only), ilo-global-fees-study-2024, ilo-g2g-malaysia-plantation-review, wb-bd-low-skilled-migration-case-study, bt-saudi-employer-pays-no-free-visa, verite-bd-my-costs-page, ds-zero-cost-malaysia-10k-2026, chakricircular-bonanza-ad-2025. Fetched but not used: impactt-ethical-recruitment-tu-report.

## Insider-review revision (8 Nov 2026, facts AG0029-AG0105)

Revised doc.md against a 30-point insider review. What changed and why, and what was moved out of the doc.

### Changes
- Coverage stated: letters approve about 259,332 posts (agency_counts.py, 3,045 letters, 618 RLs) against BMET departures of 1,303,453 (2023), 1,011,969 (2024) and about 11.17 lakh (2025) [AG0072, AG0073]. Country ratios use BMET 2025 figures from BSS and Bangladesh Monitor. The reviewer's 271,636 total and 620 RLs could not be reproduced; agency_counts.py gives 259,332 and 618 (2,863-licence OEP page of 7 Nov: 2,204 Active, 542 of them on a posted letter; top 50 agencies hold 51.0% of posted workers).
- Conflict: Kuwait 2025 departures 72,717 (BSS, AG0075) vs 42,716 (Bangladesh Monitor, AG0077). Both given in the doc.
- Kaler Kantho AB0011 re-read: 'প্রথম ২৫টি এজেন্সি বাদে অন্য সব এজেন্সি সমপরিমাণ কর্মী পাঠিয়েছে। এ সংখ্যা সাত হাজার থেকে আট হাজার।' Read per agency it is impossible (76 x 7,000-8,000 > 476,672 total, AB0020); read as a total it contradicts the ACC's per-agency counts. Dropped from the doc; the Tk 35,000 demand-letter resale price from the same fact is now in the doc. ACC per-agency range 2,995 (C0015) to 8,592 (C0021) used instead.
- SR 2,000 (AC0057): Prothom Alo calls it a deposit; the reviewer says it is the Saudi work-visa issuance fee. Only non-official guides (hijri-calendars, remotepass) support 'SR 2,000 issuance fee'; no MHRSD or Qiwa fee schedule found and Firecrawl credits ran out. Doc now says 'for SR 2,000' and asks the question as a Need to know.
- Server Locked: no source beyond AE0050 (BMET director, Jan 2024) explains it; searched English and Bangla. Doc states what AE0050 says and asks a narrower question.
- CIP (foreign employment): 2021 policy (Bangla Tribune, AG0079-AG0082): 20 a year, volume test of 2,000 workers, BAIRA president and SG ex officio, gazette. No CIP list for 2022-26 found in English or Bangla searches. Moved out of the fair-recruitment section.
- Name-only matches: RL numbers removed from the 2019 suspension list (AC0001, AC0002) and the 2019 embassy letter (AC0005-AC0011), which print names only; Odity/'Adity', Path Finder, Soul Associate, Airway International (Abiron) and 'Apurbo' moved to an 'Unconfirmed name matches' list with no RL. agencies.csv has a new column `name_only_facts` on the 56 affected rows telling the chatbot not to cite those facts against the RL.
- Libya: rewritten around the Italy route (AG0090-AG0100). The 2020 Mizda arrests (AG0098) name Sheikh Mahbubur Rahman as chairman of 'a recruiting agency'; the agency's name and RL are not given, so it is not tied to a licence. Agenzia Nova's '18 networks' report (403) and ReliefWeb's Mar 2026 report (202 bot check) could not be saved.
- BAIRA: under administrator Badrul Haque from 28 Apr 2026 for four months (AG0069); whether extended or an election held after Aug 2026 not found.
- Medical centres, air tickets, Saudi embassy gatekeeping, Bestinet added (AG0042-AG0068, AG0083-AG0085). Takamol test fixing: no source found in this pass; left as a Need to know pointing to the Saudi doc.
- BPL disclosure added in the intro (AG0101). Abrar to decide the wording.
- Language: the project CLAUDE.md says English only and no 'dalal'; the KB CLAUDE.md bar asks for the words people use. The doc keeps Bangla-script terms in brackets but dropped the romanised forms (dalal, licence bhara, salish). Abrar to decide.

### Pages we could not download (this pass)
- https://focusmalaysia.my/bestinet-were-an-it-company-not-involved-in-recruiting-migrant-workers/ (403); Bestinet's IT-company position taken from The Edge and FMT instead.
- https://www.agenzianova.com/en/news/Bangladesh-uncovers-18-migrant-trafficking-networks-en-route-from-Libya-to-Italy/ (403)
- https://reliefweb.int/report/bangladesh/navigating-new-corridors-evolving-route-bangladeshi-migration-italy-through-libya-march-2026 (202 bot check)
- Firecrawl credits ran out during this pass, so none of these were retried through Firecrawl.

### Moved out of doc.md

**57-agency ACC inquiry, full list as printed**

- **ACC inquiry into 57 agencies, Jul 2026.** As that case was investigated, the ACC wrote to BMET on 23 Jul 2026 for the ownership, licence and activity records of 57 more agencies and is checking their owners for illegal wealth (Gazipur Kontho, citing Asia Post); this is an inquiry, not a case [AC0022, AC0023]. Names as printed, with the RL given: T-Twenty Overseas (RL1415), Shimul Air Overseas (RL1803), Mahi Business (RL0802), Bangladesh Trade Corporation (RL1207), Zia International (RL0023), Proceed Overseas (RL1204), Goodness Service (RL2068), Central Overseas (RL0112), Easy Way (RL1649), Al-Fatih (RL1213), The Ifti Overseas (RL0894), Amial (RL1326), Labour Asia (RL1730), General Trading (RL0320), Amir Aviation (RL0840), "Ajaj Business" (RL1968, which OEP lists as Al Gassim Overseas), Safeway Employment (RL1483), Aljabeen (RL0884), Ifti Trade (RL1212), Salman Overseas (RL0765), Versatile (RL1585), ABS (RL1771), Protik Travels (RL0506), Vely Trade (RL1268), Al-Zuhur (RL1311), B.A. Associates (RL0567), Biplob (RL0332), Falcon (RL0617), Shun (RL0759), Remal (RL0745), Hemel Air (RL0674), The Winner (RL1149), TPS 360 (RL0995), T S Overseas (RL1755), Just Way (RL0726), "Future Palace" (RL1901, which OEP lists as F.R Trade International), Gulf International (RL1221), Sadman (RL0943), City Air (RL0576), Al Mahmud Overseas (RL1412), Fast Air (RL1383), Nusaiba Trade (RL1612), Al Mobarak (RL0542), Tasnim (RL0569), Makka (RL1175), Al-Minar (RL1235), Bangladesh Export Corporation (RL0803), K S Overseas (RL1422), S.M. Manpower (RL1372), Ratul Trading (RL0777), Citizen Air (RL1089), Al Haramine (RL1116), BOESL (RL0147), Al-Imran (RL0780), HA International (RL0469) and, per Prothom Alo, Rifa International (RL0693) [N0027, AC0024, AC0025, AC0026, AC0027, AC0028, AC0029, AC0030, AC0031, AC0032]. **Need to know:** did the inquiry become a case, and against which agencies?

**Also revoked in the 19 Jul 2026 gazette with no other flag**

Also revoked in the 19 Jul 2026 gazette, with no other flag found: Haidory Trade International (RL0240), Zahrat Associate (RL0285), 4 Site International Limited (RL0345), Q.K. Quick Express Ltd. (RL0441), United Export Ltd (RL0486), GMG Trading (Pvt.) Ltd (RL0490), The Super Eastern Ltd. (RL0501), Elegants Overseas Ltd (RL0544), Madina Overseas (RL0639), Al Khamis International (RL0680), New Edge International (RL0703), Dahmashi Corporation Ltd. (RL0727), Galaxy Corporation (RL0795), Sultan Overseas (RL0906), Provati International (RL0932), Manispower Corporation (RL0973), ISMT Human Resource Development Ltd (RL1194), Darbar Global Overseas (RL1295), Natasha Overseas (RL1315), Oparajita Overseas (RL1318), Stanford Employment Pvt Ltd (RL1352), Trans Asia Integrate Services Limited (RL1472), Al Farah Human Resources & Consultancy (RL1485), Brothers International (RL1571), JG Alfalah Management (RL1861), M.E.F Global Bangladesh Ltd. (RL1963) [C0003, C0004].

**Recruitment Advisor reviews**

Recruitment Advisor, the ITUC's review site, carries workers' own reports of what they paid each agency [AE0033]. A handful of agencies have many reviews, mostly posted between Nov 2022 and Feb 2023 [AE0033, AE0036]. Reviews of the same agency range from "went free and got the job" to "fake contract, no job, banned from re-entry" [AE0035, AE0034]. Prices reported: women domestic workers Tk 20,000-120,000 for Saudi Arabia, Jordan and Lebanon at Bangladesh Export Corporation (RL0803, 58 reviews, also in the ACC's 57-agency inquiry), and Tk 30,000-70,000 for Jordan, UAE and Oman at Just Way Aviation (RL0726, 11 reviews, also in the inquiry); men Tk 100,000-600,000 for Saudi Arabia at Bangladesh Export Corporation, and up to Tk 950,000 for Singapore and Tk 350,000 for a Bahrain job on a false contract at T.M. Overseas (RL0498, 29 reviews) [AE0033, AE0038, AE0036, AE0037, AC0032, AC0031]. One agency's only review gives the agency's own phone and website, so some reviews are self-posted [AE0046].

**IRIS, Myanmar, Malaysian glove makers, CIP (old fair-recruitment text)**

**No other private agency qualifies, and the search was wide.** IOM's IRIS (its ethical-recruitment certification) list of applicants, updated Aug 2026, has five recruiters from Singapore, Poland, Nepal, Kenya and Mexico and none from Bangladesh, though IOM announced IRIS for Bangladesh in 2019 with a working group including BAIRA, and about 600 agencies were listed as IRIS-trained [AF0013, AF0014, AF0016]. Certification is costly and unrewarded: an IRIS audit costs over USD 1,000, and the first Myanmar agencies certified under another scheme got less business afterwards [AF0001, AF0018]. IOM describes the Ministry's "Commercially Important" certificates for top agents as recognising performance and quality [AF0047]. **Need to know:** what are the criteria for those certificates? Malaysian glove makers adopted zero recruitment fees in 2019 and repaid MYR 350-400 million in fees after US import bans, which shows employers paying, not a Bangladeshi agency charging less [AF0044, AF0046]. **Need to know:** which Bangladeshi agencies stayed on the glove makers' approved lists after 2021?

**Old Japan section**

## Japan

304 letters for 1,321 workers, from 39 agencies [P0001].

Japan's OTIT (Organization for Technical Intern Training, which runs the technical intern programme) publishes the Bangladeshi sending organisations it approves; its 6 Oct 2026 list has 103 entries, including BMET and BOESL [AB0026]. Check that an agency offering a Japan intern place is on that list [AB0026]. Of the 38 private agencies with Japan letters, 32 are on it and the other six were removed; nine agencies in the Malaysia case were removed on 30 Jul 2026, eleven days after Bangladesh revoked their licences [P0001, AB0027, AB0039, AB0040, AB0041, AB0042, AB0043, AB0044, AB0045, AB0046, AB0047, C0001]. **Need to know:** how many interns has each approved agency actually sent to Japan?

- **Global Recruiting Agency (RL1324)**: 43 letters, 139 workers [P0001].
- **Western Business Alliance Ltd. (RL0173)**: 24 letters, 130 workers [P0001].
- **Nagar Overseas (RL1286)**: 20 letters, 87 workers [P0001].
- **Sadiatec Ltd. (RL1148)**: 19 letters, 99 workers [P0001].
- **EWB International Ltd (RL2656)**: 18 letters, 65 workers [P0001].
- **Caplan International (RL1697)**: 17 letters, 85 workers [P0001].
- **Aviate International (RL0282)**: 16 letters, 41 workers [P0001].
- **The Human Resource Bangladesh (RL1080)**: 15 letters, 114 workers [P0001].


**Old small-corridor lists (Kuwait, Cambodia, Brunei, Korea, Libya, Singapore, Qatar, Maldives, Mongolia, Oman, Romania)**

## Kuwait

48 letters for 6,910 workers, from 29 agencies [P0001].

- **Delight Overseas (RL2287)**: 6 letters, 1,226 workers [P0001].
- **Prestige International Ltd (RL0232)**: 5 letters, 685 workers [P0001].
- **Heaven Overseas Ltd. (RL0600)**: 2 letters, 615 workers [P0001].
- **Masud Jamil Overseas (RL1400)**: 2 letters, 539 workers [P0001].
- **Loyal Manpower Service Ltd (RL2065)**: 3 letters, 445 workers [P0001].

## Cambodia

39 letters for 2,359 workers, from 14 agencies [P0001].

- **Puspita Overseas (RL2648)**: 10 letters, 932 workers [P0001].
- **Al Grand Sultan Overseas (RL1582)**: 4 letters, 379 workers [P0001].
- **Mondol Trade International Limited (RL2626)**: 5 letters, 214 workers [P0001]; Expired on OEP [A0102].
- **Fahim Recruiting Agency (RL2594)**: 3 letters, 163 workers [P0001]; Suspended on OEP [C0423].
- **Mongol Global Services Limited (RL2527)**: 1 letter, 144 workers [P0001]; Suspended on OEP [C0421].

## Jordan

28 letters for 15,684 workers, from 2 agencies [P0001].

BOESL's site carries a current notice for Jordan garment jobs [Q0013]. Women recruited through BOESL for Jordan's garment factories told the ILO (International Labour Organization) in 2018 they paid Tk 14,000-25,000 in all, covering BOESL's fee, passport, medical and fingerprints [AF0028]. The trick on this route is a "garments visa" sold in a real factory's name by someone with no licence; see red flags [AC0064].

- **BOESL (RL0147)**: 27 letters, 15,584 workers [P0001].
- **Al Sourav Overseas (RL1028)**: 1 letter, 100 workers [P0001].

## Brunei

28 letters for 2,279 workers, from 1 agency [P0001].

BOESL's site carries a current notice for Brunei [Q0015].

- **BOESL (RL0147)**: 28 letters, 2,279 workers [P0001].

## South Korea

23 letters for 10,867 workers, from 14 agencies [P0001].

South Korea hires through EPS (Employment Permit System), a government-to-government scheme run on the Bangladesh side by BOESL; one letter covers 10,000 workers [P0003, Q0017]. EPS workers pay about USD 900, against over USD 4,000 for the same destination through private agencies [AF0024]. Brokers sell "guaranteed" places on it; see How to use this list, step 6 [AE0056].

- **BOESL (RL0147)**: 2 letters, 10,300 workers [P0001].
- **The Nazifa Recruitment Services (RL1859)**: 3 letters, 160 workers [P0001].
- **Ahmed & Company Pte Ltd (RL0081)**: 2 letters, 95 workers [P0001].
- **Western Business Alliance Ltd. (RL0173)**: 1 letter, 53 workers [P0001].
- **The Gazipur Air International (RL0891)**: 1 letter, 50 workers [P0001]; see red flags.
- **RRC Human Resource Services Ltd (RL1307)**: 3 letters, 43 workers [P0001]; see red flags.
- **Global Star Ltd (RL1718)**: 3 letters, 25 workers [P0001].

## Libya

20 letters for 1,209 workers, from 13 agencies [P0001].

- **Godhuli Overseas (RL1092)**: 1 letter, 385 workers [P0001].
- **Arabian Overseas (RL2435)**: 3 letters, 370 workers [P0001].
- **Rabbi International (RL0258)**: 2 letters, 165 workers [P0001]; Cancelled on OEP [C0101]; see red flags.
- **Sonar Bangla Krishi Khamar (RL0089)**: 3 letters, 130 workers [P0001].
- **Moktar International Ltd. (RL1115)**: 1 letter, 35 workers [P0001].
- **Azure Bengal Limited (RL0928)**: 3 letters, 19 workers [P0001]; Expired on OEP [K0001].

## Singapore

15 letters for 170 workers, from 1 agency [P0001].

BOESL's site also carries a notice for Singapore construction jobs [Q0014]. Recruitment Advisor, the ITUC's review site, has a worker who paid Tk 950,000 for Singapore [AE0036]. Singapore jobs depend on a skills test at a centre approved by Singapore's BCA (Building and Construction Authority); see red flags for agencies alleged to have kept sending through a centre whose approval was cancelled [AC0052].

- **BRAC Probashbandhu Ltd (RL1199)**: 15 letters, 170 workers [P0001].

## Qatar

8 letters for 2,261 workers, from 7 agencies [P0001].

Sources told Janobani in Jun 2026 that Qatar-bound workers were being charged Tk 4-6 lakh and cleared by BMET on visas the Qatar embassy had not attested [AC0062]. **Need to know:** which agencies processed the unattested Qatar visas, and has BMET stopped clearing them?

- **Barcelona Overseas (Pvt) Ltd. (RL1380)**: 1 letter, 1,000 workers [P0001]; see red flags.
- **T.M. Overseas (RL0498)**: 1 letter, 700 workers [P0001]; see red flags.
- **Bonanza Overseas (RL0579)**: 2 letters, 247 workers [P0001]; see evidence of fair recruitment (Qatar only).
- **BTS Overseas Limited (RL2434)**: 1 letter, 100 workers [P0001].
- **Ar-Rafi Overseas (RL1790)**: 1 letter, 90 workers [P0001].

## Maldives

5 letters for 440 workers, from 5 agencies [P0001].

- **The Ifthi Overseas (RL0894)**: 1 letter, 134 workers [P0001]; see red flags.
- **Siam Recruiting Agency (RL1531)**: 1 letter, 100 workers [P0001].
- **ZM Tours And Travels Limited (RL1287)**: 1 letter, 100 workers [P0001].
- **BOESL (RL0147)**: 1 letter, 76 workers [P0001].
- **North East Overseas Ltd. (RL2199)**: 1 letter, 30 workers [P0001].

## Mongolia

5 letters for 339 workers, from 2 agencies [P0001].

- **Starling International Ltd (RL2400)**: 4 letters, 339 workers [P0001].

## Oman

4 letters for 370 workers, from 2 agencies [P0001].

Oman has a suspension on general worker visas and women domestic workers; the Oman visa used for five women was a spouse visa [AC0060].

- **ProSearch Recruitment Consultants (RL1027)**: 2 letters, 250 workers [P0001].
- **Ahmed & Company Pte Ltd (RL0081)**: 2 letters, 120 workers [P0001].

## Romania

4 letters for 1,080 workers, from 1 agency [P0001].

- **Infinity HCM Ltd (RL1981)**: 4 letters, 1,080 workers [P0001].


**Old Saudi top list**

## Saudi Arabia

1,148 letters for 70,145 workers, from 370 agencies [P0001]. More than half of Saudi visas come one at a time, and a single visa can be bought from a Saudi citizen and sold on; see How to use this list, step 3 [AC0059, AC0057].

- **Greenland Overseas (RL0040)**: 44 letters, 7,421 workers [P0001]; see red flags.
- **Career Overseas Consultants Ltd (RL0403)**: 24 letters, 3,757 workers [P0001]; see red flags.
- **A.J. International (RL1304)**: 26 letters, 2,755 workers [P0001].
- **Bashundhara Employment Services (RL1064)**: 12 letters, 2,090 workers [P0001].
- **Amco Enterprise Limited (RL1537)**: 28 letters, 1,933 workers [P0001].
- **United Gulf Services (RL1036)**: 23 letters, 1,850 workers [P0001]; see red flags.
- **Bonanza Overseas (RL0579)**: 21 letters, 1,642 workers [P0001]; see evidence of fair recruitment (Qatar only).
- **Azam Overseas (RL0535)**: 10 letters, 1,221 workers [P0001].


**Conflicting counts for Ahmed International**

Ahmed International has 8,592 (ACC), 7,849 (Prothom Alo) and 7,869 by Apr 2024 (Kaler Kantho) [N0008, Q0023, AB0012].

**Creative International staged case (cut from complaints paragraph)**

RAB says a worker's wife filed a staged trafficking case against Creative International and withdrew it once the agency paid Tk 10 lakh [AE0018].

**Tufts evaluation (cut)**

An independent evaluation by Tufts University researchers of a 2017-20 Bangladesh-Qatar construction intervention with 598 workers found lower fees, though conventionally recruited workers reported more trust in their employer [AF0008, AF0009, AF0010].
