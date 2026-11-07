# Notes: recruiting agencies

## Compiled list (agencies.csv, doc.md, facts A)

- `agencies.csv` has 178 agencies, keyed by RL number (normalised to RL plus four digits). Selection: the 60 with the most workers and the 40 with the most letters in `activity.csv`; the top 5 by workers in every country with at least 5 letters; every agency on a published list (Malaysia's 2026 FWCMS principals, the 2016-18 G2G Plus ten, the 2022-24 round as reported, the CID figures); every agency with a press flag or an official flag other than OEP status and the 45 administrative cancellations of 30 Oct 2025. The 312 Malaysia associates are not all included; for those included, `listed_in` names their principal.
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
