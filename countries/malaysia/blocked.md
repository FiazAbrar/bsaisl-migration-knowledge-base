# Malaysia: pages we could not fetch

Merged from the per-topic notes in `blocked-parts/`. Ledger ids like [W0012] point to rows in ledger.csv.


# W: Work route (PLKS) to arrival, scams, document checks

# Blocked / not found online: part W (main work route, PLKS)

- https://www.fomema.com.my/ -> manual/fomema-home.html : curl failed (no connection); Firecrawl returned a cPanel "default web page" (server misconfigured). Need FOMEMA's own rules for the post-arrival medical: deadline after arrival, fee for men/women, what the worker brings, and how a worker/employer checks the result (reported portal: portal.fomema.my, also needs saving as manual/fomema-portal-result-check.html).
- (no URL found) -> manual/probashi-press-release-2026-10-15-malaysia.pdf : Ministry of Expatriates' Welfare press release of 15 Oct 2026 announcing the restart of recruitment to Malaysia (10,000 workers at zero cost; BOESL + 25 processing agencies + 312 recruiting agencies; process steps; medical centres). Reported by UNB and Prothom Alo (raw/news-unb-malaysia-recruitment-2026-10, raw/news-prothomalo-malaysia-how-recruited-2026) but not posted on probashi.gov.bd notices/news or bmet.gov.bd notices as of 6 Nov 2026. Probably on the Ministry's Facebook page or pressinform.gov.bd (PID handouts).
- (no URL found) -> manual/probashi-press-release-2026-10-31-malaysia-medical-fee.pdf : Ministry press release of 31 Oct 2026 fixing the Malaysia medical fee at Tk 8,000, no fee for MiGRAMS slip, complaint email (reported by TBS/UNB, raw/news-tbs-medical-fee-tk8000). Not on probashi.gov.bd.
- (not public online) -> manual/mou-bangladesh-malaysia-2021-12-19.pdf : text of the Bangladesh-Malaysia MoU on recruitment signed 19 Dec 2021 (cost items, who pays, agency selection, medical centres). Only second-hand descriptions found (BMET office order 23 Dec 2021; news).


# L: Life and problems in Malaysia, getting home

# Blocked URLs, part L (life and problems in Malaysia, getting home)

curl times out on jtksm.mohr.gov.my, mohr.gov.my, ssp.mohr.gov.my, minimumwages.mohr.gov.my, perkeso.gov.my, moha.gov.my, fomema.com.my / fomema.my, kwsp.gov.my (403), jtksabah.gov.my. Firecrawl single-URL scrape failed on every one tried (ERR_TUNNEL_CONNECTION_FAILED or timeout); WebFetch refused (ECONNREFUSED). fomema.com.my returns a cPanel "default web page" (domain misconfigured).

- https://jtksm.mohr.gov.my/ms/soalan-lazim/akta-kerja-1955-pindaan-2022 -> manual/jtksm-faq-akta-kerja-pindaan-2022.html : JTK FAQ on the 2022 amendments (overtime rate, rest day, public holidays, sick leave, termination benefits); page date
- https://jtksm.mohr.gov.my/sites/default/files/2023-11/Akta%20Kerja%201955%20(Akta%20265).pdf -> manual/jtksm-employment-act-1955-act265-2023.pdf : consolidated Employment Act (s.60A overtime 1.5x, s.59 rest day, s.60D holidays, s.24 deductions, s.19 pay within 7 days, s.69 Labour Court, s.60K/60KA, s.90B)
- https://jtksm.mohr.gov.my:443/sites/default/files/2022-12/masalah_di_tempat_kerja.pdf -> manual/jtksm-masalah-di-tempat-kerja.pdf : JTK guide "problems at work": how to file a Labour Court claim (where, documents, statutory declaration, fee, time)
- https://jtksm.mohr.gov.my:443/sites/default/files/2023-03/PROSES%20KERJA%20PTM%20DAN%20PDG.pdf -> manual/jtksm-proses-kerja-ptm-pdg.pdf : JTK work process for change of employer (PTM) for foreign workers
- https://ssp.mohr.gov.my/images/pdf/Borang%20dan%20Senarai%20Semak%20Pertukaran%20Majikan%2007062024%20v1.pdf -> manual/mohr-bppa-change-employer-form-2024.pdf : conditions and checklist for a PLKS worker to change employer (bankrupt/closed employer, 10th-year rule, 3 months PLKS left, JTK support letter)
- https://ssp.mohr.gov.my/images/pdf/DASAR_DAN_AMALAN_DALAM_PENGGAJIAN_PEKERJA_ASING.pdf -> manual/mohr-dasar-amalan-penggajian-pekerja-asing.pdf : MOHR policy on employing foreign workers (FOMEMA within 1 month at employer cost, levy, housing, passport)
- https://minimumwages.mohr.gov.my/images/PUA%20376.pdf -> manual/mohr-minimum-wages-order-2024-pua376.pdf : Minimum Wages Order 2024 (RM1,700 from 1 Feb 2025 / 1 Aug 2025; applies to foreign workers?)
- https://lom.agc.gov.my/ (act-view for P.U. (A) 376/2024, Act 446 Employees' Minimum Standards of Housing, Accommodations and Amenities Act 1990, Act 846 Abolition of Mandatory Death Penalty Act 2023, Passports Act 1966 s.12) -> manual/lom-<act>.pdf : LOM links are token-protected and the listing API is encrypted; please download these four PDFs from the LOM site in a browser
- https://www.mohr.gov.my/images/pdf/JLD4%20(22)Caruman%20Mandatori%20KWSP%20kepada%20Pekerja%20Bukan%20Warganegara%20Malaysia.pdf -> manual/mohr-epf-mandatory-foreign-workers.pdf : EPF 2% + 2% for foreign workers from Oct 2025 wages
- https://www.perkeso.gov.my/images/pekerja_asing/en/20122_-_brosur_Pekerja_Asing_EN.pdf -> manual/perkeso-foreign-worker-brochure-en.pdf : PERKESO Employment Injury Scheme benefits for foreign workers (medical, temporary/permanent disablement, dependants', funeral/repatriation)
- https://perkeso.gov.my/images/pekerja_asing/flyers/24022026_Flyer_English.pdf -> manual/perkeso-foreign-worker-flyer-2026-02.pdf : 2026 flyer (1.25% employer EIS, invalidity 0.5%+0.5%)
- https://www.perkeso.gov.my/images/imej/imej2_sip/FAQ_Foreign_Worker_Protection.pdf -> manual/perkeso-faq-foreign-worker-protection.pdf : how to claim, dependants' benefit, time limits
- https://perkeso.gov.my/en/54-social-security-protection/social-security-protection-schemes.html -> manual/perkeso-schemes-foreign-workers.html : scheme page
- https://www.fomema.com.my/ (or its current domain) -> manual/fomema-fees-and-result-check.html : FOMEMA fee (male/female), who pays, 30-day deadline, how to check result, appeal
- SPIKPA (foreign workers hospitalisation and surgical insurance) official page (likely on mohr.gov.my or the insurers' association site) -> manual/spikpa-scheme.pdf : coverage, premium, who pays
- https://jtksm.mohr.gov.my/ (pages for "Tuntutan di Mahkamah Buruh", "Aduan Buruh Paksa", Industrial Relations Department complaint for dismissal at jpp.mohr.gov.my) -> manual/jtksm-labour-court-claim.html, manual/jpp-unfair-dismissal.html : how, fee, time limit (60 days for dismissal representation?), documents


# B: Bangladesh side, money home, coming home, corridor numbers

# Blocked URLs, part B

- https://www.bb.org.bd/en/index.php/mediaroom/circular -> manual/bb-fepd-remittance-incentive-circular-2026.pdf : the current Bangladesh Bank FE/FEPD circular confirming the 2.5% cash incentive on wage earners' remittance (rate, who gets it, documents, any cap). Curl gets a captcha; Firecrawl loaded the list but found no remittance circular on its first page.
- https://archive.data.gov.my/data/dataset/jumlah-pekerja-asing-plks-aktif-mengikut-jantina-dan-negara-sumber -> manual/datagov-plks-active-by-country.csv : active PLKS (work permit) holders by source country, to compare Bangladesh with Indonesia, Nepal and India. Curl connection failed.
- Dewan Rakyat written reply of 25 Aug 2025 (question by Hassan Karim, Pasir Gudang) on Bangladeshi PLKS holders (news says 803,332 active at 30 Jun 2025, 37% of foreign workers) -> manual/parlimen-written-reply-2025-08-25-bangladesh-plks.pdf : official source for the corridor numbers. Not found on parlimen.gov.my by search.
- Dewan Rakyat written reply, Feb 2025 (Human Resources Minister) on foreign workers by nationality (news: Bangladesh 898,970, Indonesia 582,108, Nepal 370,127; 2,368,422 total) -> manual/parlimen-written-reply-2025-02-foreign-workers-by-nationality.pdf
- https://www.moha.gov.my/index.php/en/terkini/3897-notis-makluman-penyelarasan-proses-berkaitan-penangguhan-sistem-permohonan-pekerja-asing-sppa -> manual/moha-sppa-suspension-notice-2018.pdf : official notice suspending the Bangladesh worker application system (SPPA) in 2018, for the bans history. 404 by curl and Firecrawl (page moved).
- https://www.moha.gov.my/index.php/ms/kenyataan-media-kdn/2608-kemyataanmediamoumalaysiabangladesh -> manual/moha-statement-g2g-plus-mou.pdf : KDN statement on the Malaysia-Bangladesh G2G Plus MoU, for the bans and reopenings history. 404.
- KDN/MOHR statement on the May 2024 stop of new foreign-worker intake (the 31 May 2024 entry deadline) and any 2025-2026 reopening for Bangladesh -> manual/kdn-statement-foreign-worker-freeze-2024.pdf : official source for "Malaysia stopped recruitment from Bangladesh in 2024". Not found on moha.gov.my by search.
- https://www.bnm.gov.my/about-money-services-business (403) -> manual/bnm-about-msb.html : BNM's own explanation of licensed remittance and warnings on illegal remittance (hundi). Partly covered by the BNM FAQ (B0098-B0099).
- https://www.brac.net/contact (not tried) -> manual/brac-migration-contact.html : a phone number or walk-in address for BRAC's Migration Programme / Migration Welfare Centre at Dhaka airport. The programme page has no contact.


# V: Short-stay visas, MDAC, entry, transit, PVP, visas not open

# Part V blocked / incomplete sources (short-stay entry)

- https://imigresen-online.imi.gov.my/mdac/main?registerMain -> manual/mdac-register-form.html : full MDAC registration form. curl copy (raw/mdac-register-form.html) is truncated after "Last Port of Embarkation"; Firecrawl timed out. Need the remaining fields (accommodation/address in Malaysia, state, city, postcode, declaration text, what the confirmation email/PIN looks like). A screenshot of each step and of the confirmation email is ideal.
- https://malaysiavisa.imi.gov.my/evisa/ (logged-in application form) -> manual/myvisa-vtr-application-form-screens.pdf : MyVISA requires an account (email OTP). Need screenshots of the VTR (social visit) application form fields, upload fields, payment page showing the total in RM for a Bangladesh passport, and a sample eVISA Note PDF (to see whether it carries a QR code / sticker number). Public pages give no field list or sample.
- https://kualalumpur.mofa.gov.bd/pages/static-pages/6952669935ce18e1c05aa418 -> manual/bdhckl-sabah-travel-advisory.html : "Travel Advisory for Sabah Visit" (Bangladesh High Commission KL). Body is rendered by JavaScript; curl and Firecrawl return only the menu. Need the advisory text (likely warns against visit-visa job offers in Sabah).
- https://banglanews24.com/english/national/news/bd/47877.details -> manual/news-banglanews24-vln-2025.html : lead only (403 to curl). Alleges the HC Dhaka appointed "Visa Luar Negara (VLN)" which charges Tk 2,500 per visa. Need the article to know what to verify officially.
- List of "Authorised Visa Application Agencies" in Dhaka -> manual/kln-dhaka-authorised-visa-agencies.pdf : the HC Dhaka FAQ says the list is on its website, but the "Agencies" page lists only Tourism Malaysia's office. Ask HC Dhaka (dhaka@imi.gov.my) for the current list, or save it if found on the HC Dhaka Facebook page.


# S: Student pass, changing visa type, asylum, children

# Part S: blocked or not retrievable

- https://lom.agc.gov.my/ (Federal Constitution, current reprint; site uses tokenised processFile.php links, no direct PDF URL found) -> manual/federal-constitution-en.pdf : Second Schedule Part II s.1(a) (citizenship by operation of law for persons born in Malaysia: at least one parent a citizen or permanent resident) and Part III, to confirm that a child of two Bangladeshi parents is not a citizen by birth.
- https://lom.agc.gov.my/ (Immigration Act 1959/63 [Act 155] and Immigration Regulations 1963, current reprints) -> manual/immigration-act-155-en.pdf and manual/immigration-regulations-1963-en.pdf : regulation 39 (breach of pass conditions, e.g. a student or visitor working) and its penalty; s.55B (employing a person without a valid pass); absence of any refugee definition.
- https://www.unhcr.org/where-we-work/countries/malaysia (curl 403; not retried with Firecrawl because the help.unhcr.org pages covered the facts) -> manual/unhcr-malaysia-country-page.html : registered population by nationality (are any Bangladeshis registered or recognised).
- https://master.nst.com.my/amp/news/crime-courts/2024/07/1079877/colleges-universities-must-report-missing-foreign-students (curl 502; news, lead only, low priority) -> manual/news-nst-2024-missing-foreign-students.html : what Immigration requires of colleges when foreign students go missing (then find the official source).


# E: Employment Pass, family passes, MM2H, DE Rantau, long-stay

# Blocked URLs, part E (professional, long-stay and family passes)

- https://www.perkeso.gov.my/pengiklanan-mufuturejjobs-bagi-penggajian-pegawai-dagang.html -> manual/perkeso-myfuturejobs-expat-ads.html : PERKESO rules for the MYFutureJobs job advert an employer must run before a new Employment Pass (how many days the advert must run, exempt positions). curl failed (000); Firecrawl failed (tunnel error).
- https://mtcp.sarawak.gov.my/admin/file_manager/download/?id=2319 -> manual/sarawak-mtcp-smm2h-requirements.pdf : official Sarawak MM2H (S-MM2H) requirements (age, fixed deposit, income, stay, fees, agents). curl failed (000); Firecrawl failed (tunnel error).
- https://mtcp.sarawak.gov.my/web/subpage/news_view/577 -> manual/sarawak-mtcp-smm2h-news.html : Sarawak ministry (MTCP) announcement of the 2025 S-MM2H rules. curl failed (000).
- https://mm2h.sarawak.gov.my/ -> manual/sarawak-mm2h-home.html : if it exists, the official S-MM2H portal. curl failed (000).
- https://drive.google.com/drive/folders/1cnNg9Gkr4nN7ifE-7jxao7ydUtiR92De?usp=drive_link -> manual/imi-permit-masuk-ebook.pdf : IMI's e-book guidelines for Entry Permit (permanent residence) applications, including the "Warga Asing Sepenuhnya" (fully foreign) category. It's linked from imi.gov.my/index.php/perkhidmatan-utama/permit-masuk/ and is a Google Drive folder, so it can't be fetched with curl.
- https://www.imi.gov.my/wp-content/uploads/2026/11/GARIS-PANDUAN-REP.pdf : already saved as raw/imi-permit-masuk-rep-guideline.pdf, but it's image-only (the text layer is empty) and there's no PDF-to-image tool here. Someone needs to read or OCR it -> manual/imi-permit-masuk-rep-guideline-ocr.txt : Returning Expert Programme PR criteria.
- https://www.motac.gov.my/wp-content/uploads/2025/12/Guide-Malaysia-My-Second-Home.pdf : already saved as raw/motac-mm2h-guide.pdf (29 MB), but it's image-only -> manual/motac-mm2h-guide-ocr.txt : MOTAC's MM2H step-by-step guide (application flow, documents, fees).
- https://www.imi.gov.my/index.php/faq_brjim/soalan-lazim-plsxpats/ -> manual/imi-faq-plsxpats.html : the PLS@Xpats FAQ. The page loads, but the FAQ body is empty in the saved HTML (it's probably in a script-loaded accordion). Need: eligibility, the 30-day limit, sectors, fees.
- https://imigresen-online.imi.gov.my/eservices/main -> manual/imi-pvip-guidelines.pdf : the PVIP (Premium Visa Programme) portal. It's behind a login and no public official terms page was found. Need the official PVIP guideline or FAQ (fees, income, fixed deposit, appointed agents) from IMI (pvip@imi.gov.my).
- https://www.theborneopost.com/2022/10/04/immigration-d-g-foreign-professionals-may-enter-malaysia-with-social-visit-pass/ -> manual/news-borneopost-plsxpats-2022.html : lead only (HTTP 403). It's the news report of the IMI DG's PLS@Xpats announcement (30-day work permission).


# A: Practical: recruitment and real costs

# Blocked, part A (recruitment and real costs)

- https://www.manufacturing.net/labor/news/22941712/migrant-factory-workers-in-malaysia-seek-unpaid-wages-from-plastic-parts-supplier -> manual/news-ap-kawaguchi-panasonic-2025-05.html : AP (May 2025) report that Panasonic was "proportionally reimbursing" recruitment fees (~USD 5,000) paid by Bangladeshi workers at supplier Kawaguchi; evidence of buyer-funded fee remediation (curl 403; Firecrawl not tried, low priority)
- https://www.business-humanrights.org/en/latest-news/malaysia-bangladeshi-workers-win-labour-office-claim-against-recruitment-agency-meranti-binamas-for-unpaid-wages-illegal-recruitment-fees-and-contract-breaches/ -> manual/bhrrc-meranti-binamas-2025.html : only if a teammate wants BHRRC's summary; the FMT report is already saved (news-fmt-74-workers-win-2025-06b)
- https://daily-sun.com/printversion/906450 -> manual/news-dailysun-906450.html : Daily Sun piece on Malaysia recruitment costs (curl 403); low priority

## Official sources to obtain (not found online by curl; news cites them)

- Ministry of Expatriates' Welfare press release, 28 Aug 2026 (10,000 workers at zero cost incl. airfare via BOESL; Malaysia chose the 25 agencies; "do not pay, do medical tests or submit passports until official notice") -> manual/probashi-press-release-2026-08-28.pdf : cited by A0033, A0034, A0029
- Ministry urgent notice (Jul-Sep 2026) telling agencies not to sign contracts, collect passports, arrange medicals or take money for Malaysia; complaint contacts 16135 / +880 961-010-2030 and Malaysia focal point Md. Hedayetul Islam Mondal, +880 241-030-241, dsemployment1@probashi.gov.bd -> manual/probashi-malaysia-warning-2026.pdf : cited by A0040-A0042, A0008
- Ministry press release, 10 Sep 2026, on the BMET mobile court sealing Triple A Overseas (RL-2630) and seizing passports -> manual/probashi-press-release-2026-09-10.pdf : A0043
- Bangladesh-Malaysia joint statement, 8 Apr 2026 (employer bears full recruitment cost, ILO Employer Pays) -> manual/joint-statement-bd-my-2026-04-08.pdf : A0097 (probashi.gov.bd, kln.gov.my or mohr.gov.my newsroom). Note: raw/probashi-joint-statement-malaysia-2026-05-img is only a meeting photo.
- BOESL circular of 4 Sep 2025 (Tk 1,62,500 for stranded workers; any breakdown incl. "visa purchase") -> manual/boesl-circular-2025-09-04.pdf : A0056 (W0020 already has the fee)
- Bangladesh High Commission KL notice (c. Aug 2025) on the Sabah recruitment fraud ring -> manual/bdhckl-sabah-fraud-notice-2025.pdf : A0102
- Overseas Employment and Migrants (Amendment) Act 2024 and Recruiting Agents Code of Conduct Rules 2025 (sub-agents/dalals made accountable) -> manual/oema-amendment-2024.pdf : A0093
- BMET complaint/arbitration statistics for 2024-2026 (complaints received, resolved, compensation) -> manual/bmet-complaint-stats.pdf : would replace the 2024 TBS figures (A0074-A0078)


# D: Practical: tests and documents

# Blocked, part D (tests and documents)

- Ministry of Expatriates' Welfare Facebook page, post of 31 Oct 2026 (exact URL unknown; Jugantor says the Tk 8,000 notice was published there, D0004) -> manual/probashi-facebook-medical-fee-2026-10-31.pdf : the notice's own text (fee cap Tk 8,000, MiGRAMS slip free, switching agency, complaint email). Not on probashi.gov.bd notices (searched "মেডিকেল", 6 Nov 2026: only 2022-2023 notices).
- Ministry press release of 28 Oct 2026 signed by PRO Md Shariful Islam (reported by UNB, Dhaka Tribune, bdnews24, Prothom Alo; D0007-D0013) -> manual/probashi-press-release-2026-10-28-malaysia-medical.pdf : official wording on start date 31 Oct, list of approved centres, VDR papers sent to the centre.
- https://www.bernama.com/en/crime_courts/news.php?id=2514139 -> manual/news-bernama-klia-fake-plks-2026-01.html : curl got an empty page; Bangladeshi held at KLIA with a fake PLKS (Jan 2026). Low priority.
- https://thesun.my/local-news/fomema-document-forgery-syndicate-busted-five-bangladeshis-nabbed-BJ12933301 -> manual/news-thesun-fomema-forgery.html : curl got an empty page. Low priority (FMT covers a similar 2026 case, D0035).
- FOMEMA (fomema.com.my) is already on other parts' blocked lists (fee, result check, appeal); still needed for part D: FOMEMA's own fee, who may pay, how a worker sees the result, and whether there is an appeal.


# N: Practical: non-work visas

# Part N blocked / needs a person (non-work visas, practical pass)

- https://www.facebook.com/HCMalaysiaDhaka/ -> manual/hc-malaysia-dhaka-fb-myvisa-2026.pdf : Facebook (login wall). Need screenshots of the High Commission of Malaysia, Dhaka posts (a) announcing MyVISA was unavailable from 10 Feb 2026 and (b) announcing when MyVISA reopened for Bangladeshi applicants, plus the "official e-Visa link" post the High Commissioner mentioned in Dec 2025 (N0054). Also any post naming the current "service provider"/authorised visa agencies in Dhaka and their fee (N0002).
- https://www.facebook.com/bdhckl/ (Bangladesh High Commission, Kuala Lumpur, official page) -> manual/bdhckl-fb-warnings-2025.pdf : the official text of the 31 Jan 2025 warning about women brought on tourist visas with false job promises (N0028) and the 1 Aug 2025 Sabah job-scam notice (N0029). Neither is on bdhckl.gov.bd or kualalumpur.mofa.gov.bd (Sabah advisory page is JS-rendered; already listed in blocked-parts/V.md).
- MHTC current authorised partners in Bangladesh -> manual/mhtc-bangladesh-partners.pdf : no public list on malaysiahealthcare.org; ask MHTC (+603 8776 6168, communications contacts in raw/mhtc-pr-mrem-bd-presence-2026-09.md) or HC Dhaka. Needed to confirm/replace GD Assist (V0078, 2022) vs Irving Aviation (N0042, news only).
- Optional (403 to curl, content duplicated elsewhere, not needed): https://sylhetmirror.com/?p=186600 (Sabah warning; UNB copy used), https://www.jagonews24.com/en/international/news/85087 (graduate pass denial; UNB copy used).


# Z: Fixes after verification

- https://drive.google.com/drive/folders/1cnNg9Gkr4nN7ifE-7jxao7ydUtiR92De?usp=drive_link -> manual/imi-entry-permit-criteria-ebook.pdf : IMI's Entry Permit (permanent residence) criteria e-book, linked from imi-permit-masuk; needed for the "Permanent residence" Need to know (Other passes).
