# Kyrgyzstan: research notes

Research on 10 November 2026 by seven topic agents (prefixes below), merged with work/merge.py. Kyrgyz official texts are mostly Russian; quotes are kept in Russian with English claims in facts.csv.

## Corridor, chain and money in practice (prefix N)

**Searched.** OEP country-clearance JSON (country_id 94; curl with XHR header): yearly 2022-2026 all/men/women, monthly Jan 2023-9 Nov 2026, by job 2023-2026; all-countries 2024 ranking (my own pull, `oep-country-clearance-all-countries-2024-n`); 2023/2025 rankings copied from Italy. Web (English, Russian, Bangla): "Kyrgyzstan Bangladeshi workers 2025 visa suspended", "граждане Бангладеш Кыргызстан трудовые мигранты 2025", "Кыргызстан приостановил выдачу виз гражданам Бангладеш", "МИД Кыргызстана приостановлена выдача рабочих виз гражданам Бангладеш 2025", "квота 100 тысяч иностранная рабочая сила 2026", "Граждане Бангладеш заявили о трудовом рабстве", "кিরগিজস্তান বাংলাদেশি শ্রমিক", "কিরগিজস্তান ভিসা বন্ধ", "কিরগিজস্তান লাখ টাকা দালাল", "কিরগিজস্তান হয়ে ইউরোপ দালাল", "কিরগিজস্তান অভিবাসন ব্যয় নির্ধারণ", "কিরগিজস্তান বিএমইটি ছাড়পত্র বন্ধ", timesca.com, 24.kg, Azattyk, Kaktus, K-News, Fergana, Vesti.kg, TBS, Daily Star, Prothom Alo, Kalbela, Jugantor, Samakal, Ajker Patrika. IOM Kyrgyzstan MTM report Jul-Dec 2025 (Firecrawl; saved sections III, 1, 3 verbatim as excerpt). US TIP 2026 Kyrgyzstan. Agencies dataset (`agencies/activity.csv`, `agencies.csv`): no Kyrgyzstan permission letters; two agencies flagged from 2022 news.

**Key finding: the 2025-26 stop.** OEP shows clearances collapse in August 2025 (1,410 July → 57 Aug → 1 Sep → 0 Oct) and 11 in all of 2026. No official order found on either side. Evidence pointing to the Kyrgyz side: students report Bangladeshi visa applications unapproved since July 2025 (Prothom Alo, Apr 2026); Legprom in Jan 2026 asked parliament to extend Bangladeshi work visas (implies refusals); Ministry data show Bangladeshi permits fell in 2026 while Chinese/Pakistani rose; Bangladesh is no longer named among the top quota-requesting countries (K-News, May 2026); the Dec 2024 deputy-minister quote that Bangladeshis "break the law most". Bangladesh side: Kyrgyzstan not on the Oct 2026 12-country prior-approval list. The Foreign Secretary's 14 Oct 2026 Bishkek talks discussed jobs and an MoU. A Facebook video titled "কিরগিজস্তান ভিসা আপডেট | ভিসা কবে খুলবে? ২০২৬ নাকি ২০২৭?" (19 Oct 2026) also treats visas as closed (not saved).

**Conflicts / gaps.**
- OEP 2024 clearances 12,747 vs Kyrgyz permits to Bangladeshis 2024 2,758 (N0003 vs N0035); 2026: 11 clearances vs 3,872 permits (N0005 vs N0035). Unexplained; written as Need to know.
- Dec 2025 permit count: IOM 24% of 47,686 (≈11,400) vs ministry 11,677 for 2025 (consistent); Times of Central Asia says 11,700.
- 2025 quota: 25,000 → 42,000 (Aug 2025, IOM/Economist.kg) and "then 52,000" (24.kg Feb 2026 says 52,000 is the 2026 figure). Kept: 2025 42,000; 2026 52,000 → 100,000.
- 2022 sewing-shop case: workers' account (Azattyk/Daily Star/TBS) vs police statement that the 14 said they worked voluntarily (N0135, N0169) and agency denial (N0130). Doc attributes each.
- Infographic numbers (N0035-N0037) are my hand transcription of a 24.kg image (saved as PNG + TXT, logged manual).

**Logged but not used:** N0006 (women 2023), N0014/N0015 (zero months early 2024), N0034, N0041, N0046 (legalisation campaign; for U), N0047 (ILO 181; for W/L), N0056, N0060, N0063 (5,000 irregular; for U), N0066 (47% of 2024 applications Bangladeshi; could add to Size), N0074 (exit to Uzbekistan to re-enter on visa; for U), N0079 (Deputy FM's April 2024 Dhaka visit; could go in Status history), N0080, N0088, N0098, N0100 (operation "Nelegal"; for U), N0109, N0144, N0146, N0147, N0153-N0156 partly, N0158, N0171, N0175.

**Sources fetched but not registered (not used):** exclusive.kz interview, akipress 2026 quota (paywalled), akipress 2024 suspension (paywalled; Azattyk covers it), TBS attestation-exemption article (Jul 2026), Dhaka Post student courier ban (Jan 2025, for V), Ekhon TV student visa (2024, for V), Kaktus student visa transfer (Jan 2026, for V), 24.kg June 2025 "visa for 60 days then extended to a year" (for W), Azattyk Indian-community article, Times of Central Asia Oct 2026 quota piece (11,700 Bangladeshi permits), Fergana quota-100k analysis, Kaktus quota piece.

## Kyrgyz work route (prefix W)

**The system on 10 Nov 2026 (W side).**
- 1 Jan 2025: Single/Unified Permit pilot under Resolution No. 721 (2 Dec 2024) replaced the employer quota permit + personal work permit + work visa (W1); applications moved from ework.e-gov.kg (closed 25 Dec 2024) to evisa.e-gov.kg; the interdepartmental quota commission was abolished [W0052, W0053, W0138, W0099].
- 1 Jul 2025: Resolution No. 367 (27 Jun 2025) added the resident card and set the Annex 2 fees (30,000 som + USD 300) [W0057-W0062]. The 7 to 10 day decision time, 3-employer rule, 30 days to leave and 10-day extension rule are from #367 summaries (Caravan-Info, 4 Jul 2025) [W0086-W0089].
- 30 Apr 2026: Resolution No. 312 replaced #721/#367 with one Temporary Regulation (visas + Unified Permit + resident card), MFA in charge, until 31 Dec 2026 [W0001-W0003, W0137]. Amended by No. 506 (23 Jul 2026) [W0069].
- Sept 2026: presidential decree moving Unified Permit, resident card, ВНЖ and registration to the Ministry of Labour (new migration department, services outsourced; Cabinet has two months) [W0127-W0130].
- 4 Sept 2026: new registration procedure, Cabinet Resolution No. 600 [W0111].

**Quota:** 2025: 25,000, then 42,000 (order No. 710, 18 Aug 2025) [W0014]; 2026: 52,000, then 100,000 (30 Apr 2026) [W0011, W0010]. Traveliscope (agency) claims 120,000 for 2027 by an order of 7 Sept 2026 [W0140]; no news or official source confirms it (searched Russian news: квота 2027 трудовая миграция). The 2027 immigration quota (400, order No. 780-т, 13 Oct 2026) is a different quota.

**Bangladeshis in the numbers (for N):** by 30 Apr 2025, 2,573 of 12,232 60-day Single Permits went to Bangladeshis, second after China (2,844) [W0097, W0096]; IOM DTM (via Economist.kg): Bangladeshis 24% of ~48,000 permit holders by Dec 2025, second after China 40%, Pakistan 17%, India 5% [W0103]; 48,439 unified permits issued by 17 Dec 2025 [W0101]. 17,989 foreigners got work permits in 2024 (logged in source, not as a fact).

**Conflicts / uncertainties:**
- Fees under #312: no source gives the standard 2026 rates. The garment-sector "preferential" rates in #506 [W0071, W0072] equal the #367 standard rates [W0057-W0061], which implies the #312 standard rates are higher. A search summary mentioned "61,767 som" for the unified permit after May 2026; no saved source contains it. Not logged.
- Registration deadline: e-Visa portal says 5 working days for visa nationals [W0034]; Resolution No. 600 says "not later than the last day of stay permitted without registration" per the exempt list. Not resolved for Bangladesh.
- Processing time: MFA (2024-25) says 7 working days [W0056]; #367 says 7-10 [W0087]; Traveliscope says 2, 5 or 7 by fee tier [W0139] (lead).
- Medical/HIV: required under the pre-2025 system [W0148] and since July 2026 for SW1/SW2 [W0073]; nothing confirms it for ordinary Unified Permit workers.
- Exit visa fees: 24.kg/Caliber give 17,500 / 192,500 som + USD 1,100 [W0008, W0009]; Traveliscope's e-Visa calculator figures (USD 206 to over USD 13,500) not logged (agency).
- Kabar headline "Kyrgyzstan offers free exit visas to foreigners violating immigration rules" (related link, Dec 2025) not opened; for U/L.

**Searched:** evisa.e-gov.kg (all info pages, forms, the Bangladesh eligibility selector), mfa.gov.kg (blocked, 502; Wayback), cbd.minjust.gov.kg (JavaScript app; search page via Firecrawl returned not-found), base.spinform.ru (full text behind login), zakon.kg (law texts), 24.kg, Kaktus, Akchabar, Economist.kg, Kabar, AKI-TV, Caravan-Info, vb.kg; agency/law-firm guides (Traveliscope, Legis, KG Account, NNRoad, tour.too.kg via Wayback, Terrana); BE&OE Pakistan job listing. Terms: Единое разрешение, резидент-карта, Временное положение 312, квота трудовая миграция 2026/2027, регистрация иностранцев 2026, ПИН иностранца, SIM-карта регистрация; English: Kyrgyzstan Single/Unified Permit, work permit 2026; Bangla: কিরগিজস্তান ওয়ার্ক পারমিট ভিসা (only agency pages came back).

**What happens in practice:** sources describe the employer doing everything online; the worker never visits a Kyrgyz embassy. No source found on what Bangladeshi workers actually receive (printed permit? QR?), on the Kyrgyz mission accredited to Bangladesh's role, or on what agencies charge for the permit.

**Logged but not used in the draft:** W0006 (register of unscrupulous employers; used indirectly), W0108-W0110 (fines on companies; for L), W0144 (Pakistan-Kyrgyzstan labour MoU July 2025, agency claim; for N/B: does Bangladesh have one?), W0149 (old W1 visa), W0040/W0041 (portal payment and corrections, details), W0102.

**Source naming note:** `news-caravaninfo-new-rules-permit-2026` and `news-caravaninfo-resident-card-qr-2026` are dated 4 July 2025 (names misleading; page-date in sources.csv is correct).

## Bangladesh side and the Embassy in Tashkent (prefix B)

**Searched.** OEP country-clearance JSON (curl with `X-Requested-With: XMLHttpRequest`; Kyrgyzstan is country_id 94): totals and women by year 2022-2026, by month Jan 2023 to 9 Nov 2026, by job category 2023-2026 (script `work/B/oep_pull.py`). BMET miscellaneous-infos: live search no longer returns results by curl (JS); `agencies/activity.csv` (all BMET posted permission letters, scanned from all 7 pages) has no Kyrgyzstan letter, and `agencies/notes.md` confirms "Bahrain, Italy and Kyrgyzstan have no letters". tashkent.mofa.gov.bd: home, address, office hours, news, press releases (5 and 13 Aug, 30 Sep 2025: scanned PDFs, read as images; only 30 Sep is relevant), e-passport fee PDF, postal-vote/Kyrgyzstan page. bangladesh.uz (the Embassy's older site): direct fetch and Firecrawl fail (TLS error); Wayback copies of consular-section, accredited-countries and visa-and-passport-information are JS shells with no content. MoFA Apostille list and charter (Kyrgyzstan is 'A' category, no. 50). Bangla: "কিরগিজস্তান বিএমইটি ছাড়পত্র বন্ধ কর্মী", "কিরগিজস্তানে কর্মী পাঠানো বন্ধ মন্ত্রণালয় নিয়োগানুমতি ২০২৫", "কিরগিজস্তান থেকে ১৮০ বাংলাদেশি ফেরত দূতাবাস তাসখন্দ", "কিরগিজস্তান ভিসা সত্যায়ন তাসখন্দ দূতাবাস কর্মী বিএমইটি", "\"কিরগিজস্তান\" বহির্গমন ছাড়পত্র বিএমইটি ২০২৫", "কিরগিজস্তান ওয়ার্ক পারমিট ভিসা বাংলাদেশি কর্মী ২০২৬ খরচ দালাল", "বোয়েসেল কিরগিজস্তান". English: BMET clearance suspended Kyrgyzstan 2025; Bangladeshis Kyrgyzstan fraud return September 2025; BOESL Kyrgyzstan; Bangladesh Kyrgyzstan MoU labour; Dhaka to Bishkek flight; Kyrgyz embassy accredited to Bangladesh; honorary consul of Bangladesh in Bishkek. Russian: "граждане Бангладеш Кыргызстан визы приостановлено 2025", "Кыргызстан Бангладеш рабочие визы приостановили август 2025 Минтруд", "Посольство Кыргызской Республики в Индии по совместительству Бангладеш".

**Main finding: the BMET flow collapsed in August 2025, and nobody has said why.** Clearances ran at 1,100-1,500 a month from April to July 2025, then 57 in August, 1 in September, 0 in October, and 11 in all of 2026 (B0089-B0101). No BMET or Ministry notice, and no news item, explains it. Leads for N and the lead:
- Kyrgyz Labour Ministry suspended quota distribution for Bangladesh, Pakistan and India from April 2024 (AKIpress 774450, VOA); not logged by B, N/W should check whether a second halt came in mid-2025.
- Times of Central Asia (search snippet): about 11,700 Bangladeshis held Kyrgyz work permits by December 2025; time.kg: about 61,000 work visas issued in 2026 including to Bangladeshis. If true, Bangladeshis are still getting Kyrgyz permits while BMET clears almost none: either they go without BMET clearance (tourist visa, or via Dubai as CID described, B0145), or are already inside. This is the key question for N/U.
- AKIpress kg.akipress.org/news:2398018 "Ассоциация «Легпром» просит продлить рабочие визы для мигрантов из Бангладеш" (the garment industry association asks to extend Bangladeshi migrants' work visas): not fetched, date unknown; for N/W.
- The Bangla Tribune / Prothom Alo 4 Nov 2026 Ministry letter does NOT include Kyrgyzstan (B0114, B0115).
- Kyrgyz single-window rule: since 1 Jan 2025 work permits go through evisa.e-gov.kg (B0151); W's topic.

**Size in context.** 2024 (12,747) was the corridor's largest year, not 2025; the brief's figures (1,713 in 2023, 6,652 in 2025) match OEP. Bangladesh Monitor gives 6,650 for 2025 (agencies AG0078). April-June 2024 (10,141 clearances) followed none in February-March 2024, which fits a backlog released after the April 2024 Kyrgyz-Bangladesh talks (B0141) but nothing says so.

**Practice.**
- Kyrgyzstan visas don't appear in BMET's posted permission letters at all; most clearances are titled just "Worker". Either letters were never posted, or visas were cleared as single visas. Asked as Need to know.
- The Prothom Alo item (B0117) says demand letters for up to 7 workers needed no Ministry approval and were misused; plausible route for Kyrgyzstan, unconfirmed.
- No Kyrgyzstan cost cap exists in the Ministry's 2017 table (probashi-migration-cost-16-countries-2017, ported, checked by grep; not logged as a fact since absence can't be quoted).
- Real prices from news: Tk 5 lakh (Jannat Trade, c. 2024, B0152), Tk 2.8-3.25 lakh per visa (2022, B0147). N owns costs.

**Conflicts.**
- 4 Nov 2026 list: Cambodia (Prothom Alo English, B0114) vs Croatia (Bangla Tribune, B0115). Neither includes Kyrgyzstan, so no effect on the doc.
- Welfare fee: BMET charter Tk 3,500 (B0012, B0153) vs Ministry circular Tk 5,500 from 1 Oct 2026 (B0019). Doc uses Tk 5,500; B0153 cited only for the clearance fee and source tax.

**Logged but not used:** B0001 (114 countries accept the Apostille, superseded by B0150), B0012 (fee conflict), B0039, B0041 (folded into B0056/B0058), B0123 (April 2026 consular talks, no practical effect), B0135 (May 2024 consular cooperation), B0113 (2023 jobs), B0116 (signatory of the 4 Nov letter), B0141 (April 2024 Kyrgyz interest in skilled workers; used only in these notes), B0151 (Kyrgyz single-window e-visa rule, for W), B0143 (Jannat Trade had only a travel licence; could go in N's Scams), B0146-B0147 (2022 Al Jabeen case: for N, agencies doc already has it as N0040/N0041).

**Dates.** The Daily Star Jannat Trade article (B0142-B0145, B0152) has no date on the page; article id 3604471 and the story (ad in December, departure 7 April) point to April-May 2024. Tashkent Embassy address page last updated 11 July 2025 (possibly outdated, but the 30 Sep 2025 press-release letterhead gives the same address and phones).

## Law and work (prefix L)

**Searched:** cbd.minjust.gov.kg (Labour Code 3-45, Code of Offences 3-36, Criminal Code 3-38, Law On External Migration 350, Cabinet decrees 721 (2024, repealed) and 312 (2026) with the Single Permit Temporary Regulation); economist.kg, 24.kg, kaktus.media in Russian ("иностранный гражданин без разрешения на работу штраф", "инспекция труда жалоба", "минимальная заработная плата 2026", "граждане Бангладеш зарплата"); ombudsman.kg; English and Bangla searches on unpaid or dead Bangladeshis in Kyrgyzstan (কিরগিজস্তানে বাংলাদেশি শ্রমিক বেতন, লাশ); WEWB pages.

**Practice:**
- Kyrgyz law ties the worker hard to the employer: the Single Permit is not transferable and dies with the job, leaving 30 days to leave [L0107-L0110].
- 2025 returnee stories show unpaid workers ending up undocumented and jailed, not compensated [L0174, L0175].
- No Kyrgyz NGO handling foreign workers' cases was found.
- No report of a Bangladeshi death in Kyrgyzstan was found.

**Conflicts and caveats:**
- The headhunter.kg guide [L0166-L0171] names the "State Labour Inspection"; the October 2026 news [L0165] names the "Service for Control and Supervision of Labour Legislation". I used the latter.
- The decree-312 fee table has no column header; som/USD was inferred from the 87.5 ratio (note on L0102).
- The minimum wage is from news only; the official 2026 budget law was not saved.

**Logged but not used:** none significant.

**Tool problem:** the first batch was logged twice by mistake and the 183 duplicate rows were deleted from work/L/facts.csv. The current L0184-L0189 are a later batch, so the ids are unique. Some claims were narrowed after logging (fixclaims.py) to match their quotes.

## Visits, study, family and children (prefix V)

**Searched:** e-visa portal evisa.e-gov.kg (home, Get information, FAQ); cbd.minjust.gov.kg via Firecrawl (Temporary Regulation 2026, decree 312, stay regulation 541, consular fees 839, citizenship law); Refworld (2017 visa instruction, now suspended); spinform.ru (decree 506 of 23 July 2026, presidential decree 337 of 28 Sept 2026); mfa.kg / mfa.gov.kg (failed, 000 and 502); 24.kg, Kaktus, Economist.kg, bizmedia.kz (visa regime 2019-2026, medical accreditation 2026); Prothom Alo, Financial Express, UNB, Daily Star (May 2024 attacks); BMDC site via Firecrawl (news list and notices); Jago News; bdlaws. Terms: English "Kyrgyzstan visa Bangladesh", "MBBS Kyrgyzstan BMDC", "Bishkek mob attack students"; Russian "визовый режим Бангладеш", "упрощенный визовый режим резидент-карта", "Временное положение ... Единого разрешения", "аккредитация медвузов 2026", "Центр по приему иностранных студентов", "гражданство ребенка родившегося"; Bangla "কিরগিজস্তান ভিসা", "বিদেশ থেকে এমবিবিএস বিএমডিসি".

**Key findings:**
- Regime timeline: 2019 simplified tourist visa for Bangladeshis with Gulf residence (V0099); Sept 2021 tourist visas for BD/IN/PK/NP blocked, self-application replaced by host-organisation invitation (V0094-V0098); 2022 MFA reminder of simplified procedure (V0167); 2023 decree 541 replaced the 2009 simplified-regime list; current Annex 2 (edition 7 Sept 2026) keeps Bangladesh only for Gulf/Brunei resident-card holders (V0155, V0002).
- New Accompanying visa (type A, added 23 July 2026): for Gulf resident-card holders working as staff of Gulf citizens visiting Kyrgyzstan, up to 90 days (V0037, V0038). Relevant to Bangladeshi drivers, maids and staff of Gulf families; I did not put it in the draft as its own H2 (it is narrow). Lead may add one line under Visas or Visit visa.
- Gulf citizens get 180 days visa-free in 360 (V0004): context for the accompanying visa.
- Presidential decree 337 (28 Sept 2026) moves Unified Permit and resident-card issuance from MFA to the Ministry of Labour, Social Security and Migration, to be outsourced (source `spinform-kg-president-decree-337-2026-migration-to-mlsp`, saved, no fact logged; W should cover). Visas stay with MFA.
- Business visa for medical treatment (V0018) is the route for Bangladeshi patients.
- Student numbers: no official count of Bangladeshi students found; 800+ (Prothom Alo 2024) vs 1,000+ (a student via UNB/FE 2024).

**Conflicts:** Transit visa validity: Temporary Regulation says up to 3 days (V0035) vs fee table "up to five days" (V0076). Both marked conflict.

**Facts logged but not used in the draft:** V0004 (Gulf visa-free, context), V0010/V0011 (legal frame, for the lead's intro), V0020/V0077 (visa support validity and fee: used only implicitly), V0024, V0032, V0033 (embassy guarantee letter), V0035-V0038 (transit and accompanying visa), V0079 (legalisation fee), V0092, V0096, V0101 (April 2026 MFA-ambassador meeting: B's contacts section), V0102, V0103, V0141-V0146 (RQE details: lead may add to Student visa if space), V0163 used. Meken visa is V0168.

**BMDC Eligibility Certificate notice (10 Feb 2026):** saved as `bmdc-eligibility-certificate-notice-2026.md` but the PDF's Bangla OCR is garbled; no fact logged. It appears to say students going abroad for MBBS/BDS from a 2024-25 session must get BMDC's Eligibility Certificate, and must later submit the registration certificate of the country of study. Needs a clean copy (see c). The draft cites only V0140 (2018 RQE requirements) for the certificate; the clause on the 10 Feb 2026 notice has no fact yet: drop it or log the notice once a clean text exists.

**Files to delete or ignore:** `news-akipress-foreign-students-3-public-medschools` (paywalled, empty); `news-medicaldialogues-kyrgyz-accreditation-row`, `news-24kg-regulation-stay-foreigners`, `news-economistkg-new-rules-foreign-workers-2025`, `news-bizmedia-simplified-visa-extended-2023`, `news-kaktus-cabinet-extends-simplified-visa`, `news-dailystar` (failed), `news-unb-kyrgyz-bd-students-fm-2024`, `news-economistkg-birth-registration-qa-2024`, `refworld-kg-visa-instruction-2017-155-ru`, `spinform-*`: saved, no facts.

## Irregular routes, status and asylum (prefix U)

**Searched:** English: "Bangladeshi workers Kyrgyzstan stranded", "Bangladeshi Kyrgyzstan route Europe Russia Kazakhstan", "IOM Kyrgyzstan assisted voluntary return Bangladesh", "Bangladeshi Russia army Kyrgyzstan", "2025 TIP Kyrgyzstan", "Kyrgyzstan refugee status determination UNHCR", "Bangladesh Embassy Tashkent Kyrgyzstan travel permit". Russian: "граждане Бангладеш Кыргызстан задержаны граница Казахстан", "граждане Бангладеш депортированы Кыргызстан 2025", "легализация иностранцев 2025 амнистия", "Нелегал-2026", "граждан Бангладеш Бишкек 2026 выдворены", "Кодекс о правонарушениях штраф иностранец выдворение запрет въезда", "указ 2026 добровольный выезд выездная виза", "выездная виза просроченная виза evisa", "статус беженца 2025", "Кыргызстан Бангладеш транзит Европа ГКНБ канал". Bangla: "কিরগিজস্তান হয়ে ইউরোপ বাংলাদেশি আটক", "কিরগিজস্তান বাংলাদেশি শ্রমিক ফেরত ২০২৬", "কিরগিজস্তান দালাল ইউরোপ পাঠানোর কথা বলে প্রতারণা", "কিরগিজস্তানে আটকা বাংলাদেশি কারাগার মুক্তিপণ". Sites: economist.kg, 24.kg, kaktus.media, akchabar, currenttime, timesca, rferl, inform.kz, caravan.kz, Daily Star, TBS (English and Bangla), Dhaka Tribune, Bangla Tribune, Views Bangladesh, New Nation, Bangladesh Pratidin, Prothom Alo, help.unhcr.org, ecoi.net.

**What happens in practice:**
- The undocumented population is mainly people who came legally and lost status, not border-crossers: tourist visas sold as work visas, visas expiring on arrival, "work visa later" promises, employers not renewing [U0040-U0046, U0009, U0074].
- Fixers sell fake legalisation: a Bangladeshi forger (USD 66,500, Feb 2025) and a fake medical certificate (form 086) ring (March 2026) [U0063, U0066].
- Enforcement has hardened every year since 2024: Tashiev's 1,000 Bangladeshi deportations (2024), Decree 164 window then Nelegal-2025, Law No. 80 fines (April 2025), Nelegal-2026 (June, August, October raids), Decree 233 exit window (July 2026), Cabinet resolution 602 and EISUM (September 2026). Uptake of the July 2026 window was low: about 500 exit visas by 13 July against 5,000 expected [U0104].
- The 180 returnees of September 2025 are the biggest single stranded-worker event; the Kyrgyz government organised the flight. I found no IOM-assisted return of Bangladeshis from Kyrgyzstan.
- "Door to Europe": every case found ends in prison, deportation or a self-paid ticket home; none ends in Europe. Kyrgyz press reports (2023-2024) of South Asian smuggling to Kazakhstan concern mostly Pakistanis, Nepalis and Sri Lankans; Bangladeshis appear in the June 2024 Kazakhstan case.

**Conflicts and caveats:**
- Shahidul Islam's arrival date: Views Bangladesh says "June 3 this year" (2025) while TBS Bangla says 3 June 2024 [U0009]. I used TBS Bangla (more specific; seven months unpaid plus three months in jail fits 2024).
- Dhaka Tribune (8 Sept) said the flight would be Tuesday 9 Sept; arrival was early Wednesday 10 Sept [U0004].
- Entry-ban durations come from a 2022 statement by the Deputy Interior Minister [U0112]; not checked against the current Law "On external migration" (cbd.minjust.gov.kg loads only with JavaScript).
- Fine tiers [U0084-U0088] come from Economist.kg's summary of Law No. 80; the official text of the Code of Offences article 431 was not saved. Agent L may have the official text; prefer L's ids if so.
- The exit visa price "almost 100,000 som" [U0103] is the MFA consular director quoted by Kaktus; it seems to include penalty fees. The ordinary exit visa fee is not found.
- Cabinet resolution 602 (refusal of re-entry) is worded for the visa-free regime; Bangladeshis need a visa (agent V/W), so its effect on them is unclear.
- UNHCR sources registered as official "yes" following the Malaysia precedent (unhcr-my-rsd); lead may reclassify.
- Caravan.kz 2004 article [U0059, U0060] is old; used only to show the Europe pitch is long-standing.

**Logged but not used in draft:** U0027-U0030 (Jannat Trade's YouTube ad, Tk 60,000-65,000 pay, Tk 5 lakh price, fake papers caught at Dhaka airport: for the Scams section, agent N), U0042 (most of the 130 not in demand: lack of skills, low pay: for N's What goes wrong), U0071 (GKNB asks employers to arrange voluntary departure), U0073 (tourists and students working), U0075 (nationalities in the June 2026 Issyk-Kul raid), U0095 (the July 2026 window was not a legalisation), U0104 (only about 500 exit visas by 13 July 2026 against 5,000 expected), U0105 (work-visa holders: Chinese about 50%, then Pakistan, India, Bangladesh: for N's Size), U0106 (companies either take foreigners out or extend visas: for W), U0114 (controlled departure presented to the CIS), U0140, U0142 (Ukraine count; UNHCR mandate refugees).

## Money (prefix G)

**What was searched**
- Official Kyrgyz: nbkr.kg (official rates page and home page, daily.xml, register of money transfer systems item=2665, consumer complaint notice); cbd.minjust.gov.kg (Cabinet Decree No. 7 of 2023 via Firecrawl search and scrape); customs.gov.kg (individuals' page, cash page slug "akca-karajattar" returns 404, passenger declaration PDF has a garbled Cyrillic text layer); invest.gov.kg (taxation guide, data as of June 2026); sti.gov.kg (searched, no page on income tax rate for foreigners found).
- Bangladesh: Bangladesh Bank rate sheet 10/11/2026 (fresh fetch); bb.org.bd country-wise remittance page (econdata/wagermidtl.php is "Request Rejected"; en/index.php/econdata/wagermidtl scraped with Firecrawl); BB monthly remittance report August 2026 and top-30 table (Italy folder) grepped for Kyrgyzstan: none. Copied from Kuwait (logged as manual): mof-budget-speech-2026-27, hsia-customs, news-tbs-bfiu-14000-mfs-hundi, tbs-why-hundi-2024, nsd-wage-earner-development-bond.
- Providers: bKash MTS page (curl 403, Firecrawl OK), Western Union KG, Profee, Optima Bank, Bakai Bank non-resident documents PDF, MBANK press release.
- Search terms: English "send money from Kyrgyzstan to Bangladesh bKash", "Western Union Kyrgyzstan Bangladesh", "Kyrgyzstan income tax foreign workers", "open bank account foreigner Kyrgyzstan", "Bishkek cost of living 2026", "Bangladeshi workers Kyrgyzstan salary hundi"; Russian "перевод денег из Кыргызстана в Бангладеш", "бангладешцы Бишкек денежные переводы хавала", "вывоз наличной валюты Кыргызстан 10 000 / 5 тысяч", "временном запрете на вывоз наличной иностранной валюты", "реестр систем денежных переводов НБКР", "аренда Бишкек 2026", "вывоз мерных слитков НБКР"; Bangla "কিরগিজস্তান থেকে টাকা পাঠানো রেমিট্যান্স", "কিরগিজস্তানে বাংলাদেশি শ্রমিক বেতন টাকা পাঠাতে পারছেন না", "কিরগিজস্তান প্রবাসী বেতন সোম বিকাশ হুন্ডি". No Bangladeshi or Kyrgyz news item was found on how Bangladeshis in Kyrgyzstan send money or on hundi rates in Bishkek.

**Rates (logged for the lead)**
- USD 1 = KGS 87.45 (NBKR, 10 Nov 2026; 87.4498 set for 11 Nov) [G0001]; USD 1 = Tk 124.42 (Bangladesh Bank weighted average, 10 Nov 2026) [G0002]; KGS 1 = Tk 1.4228, use "about Tk 1.42" [G0003]. Handy: 1,000 som = Tk 1,423; 10,000 som = Tk 14,228; 30,000 som = Tk 42,700; Tk 1 lakh = 70,280 som = USD 804.

**Conflicts and caveats**
- Cash export: the official decree text (edition 1 Aug 2024, latest on cbd.minjust.gov.kg) still says "до принятия соответствующего решения Кабинета Министров" (until the Cabinet decides); no repeal found. The 2024-09 news confirms enforcement; the 2026-07 Manas case cites the EAEU declaration rules (declare over USD 10,000) rather than the USD 5,000 ban. Status of the ban in 2026 is a Need to know. The Aug 2024 amendment (Decree 446) exempted licensed banks, exchange bureaus and microfinance companies only.
- Income tax: invest.gov.kg (official, June 2026) gives 10% basic rate; one expat site (wheretoemigrate.io) claimed a 20% top rate; ignored as unreliable.
- Social insurance 27.25%/12.25% "including foreign employees" (G0041) may clash with agent L's findings on social insurance for foreigners; L should reconcile.
- The STS patent regime (G0043) is described for "migrant workers from neighboring countries"; not confirmed for Bangladeshis.
- bKash: Kyrgyzstan is absent from the partner-country table (G0013). Western Union and MoneyGram appear for most countries on bKash's list, but not for Kyrgyzstan, so whether a WU/MoneyGram transfer from Kyrgyzstan can be paid to bKash is unknown.
- Profee is not on the NBKR register (checked the whole international list, 20 operators). It may operate as a card-to-wallet service from abroad. Not recommended in the text; only described.
- BB country table (G0020) shows FY2021-22 to April 2024 only; the newer monthly report (Aug 2026) and top-30 (Jul-Sep 2026) also have no Kyrgyzstan row. No official remittance figure from Kyrgyzstan exists.

**Facts logged but not used, and why**
- G0030 (residents' USD 10,000 limit and 10% levy): applies to Kyrgyz residents, not to Bangladeshi workers; kept for context.
- Sources saved without facts: nbkr-daily-rates-2026-11-10 and nbkr-official-rates-page-2026-11-10 (back-up for G0001), alta-kg-cabinet-decree-7-2023-cash-export and news-24kg-cash-export-ban-2023-01 (original 2023 text; superseded by the official edition), customs-kg-for-individuals and customs-kg-cash-rules (curl saved empty/404 pages; the EAEU import allowances, EUR 10,000 and 50 kg by air duty-free, were read via Firecrawl but not saved), customs-kg-passenger-declaration-form (garbled text layer).

**What happens in practice (leads only)**
- No source found on the channel Bangladeshis actually use. Pakistani government job postings for Bishkek garment work (35,000-37,000 som with free housing and food) surfaced in searches but belong to agent N's wage topic.

## Writing and independent check (10-11 November 2026)

- Gap agent K saved official texts from cbd.minjust.gov.kg with Firecrawl (Resolutions 312, 506, 600; Decrees 337 and 362; the 2026 budget law's minimum wage). Still not found: the general Unified Permit and resident card fees (Annex 5 of the Temporary Regulation), the quota orders for 2026 and 2027, the Law "On refugees".
- doc.md was assembled from six parts written in parallel (Malaysia and Italy as the standard), then checked by independent verifiers: round 1 (7 verifiers, whole doc) 79 failures; round 2 6; coverage audit added 22 points and 9 Need to know questions; round 3 11; round 4 1; round 5 1 (two words), round 6 0.
- Lead's fixes: R0001 logged (1 RP = 100 som, Kaktus) so every RP conversion has a source; a coverage edit that put a Need to know mid-paragraph was repaired; the "tourist visa can't be changed" misreading of V0045 (para 24 of the Temporary Regulation) corrected in Visit visa and Changing visa type; three duplicate Need to know questions removed.
- Known weak points: why BMET clearances stopped in August 2025 (no notice found); the standard permit fee; real prices and pay in 2026 (news only); the Embassy in Tashkent's Travel Permit and death-repatriation procedures (its sites are broken).
- The visa and permit rules come from a Temporary Regulation valid to 31 December 2026: recheck in January 2027.

## Pages we could not download

Save every file into `countries/kyrgyzstan/manual/` (NOT `sources/`). Keep the real extension: PDF, "Save page as" HTML, or a dated screenshot (PNG). Skip anything you can't get and tell me which. Kyrgyz laws on cbd.minjust.gov.kg are being fetched by an agent, so they are not on this list.

### Priority 1: Bangladesh Embassy in Tashkent (covers Kyrgyzstan)

1. **Consular services and fees** (Travel Permit, power of attorney, birth registration, death and body repatriation): https://bangladesh.uz/consular-section, https://bangladesh.uz/visa-and-passport-information and https://bangladesh.uz/accredited-countries (the certificate has expired: click through the browser warning) → `bdemb-tashkent-consular-section.html`, `bdemb-tashkent-passport-info.html`, `bdemb-tashkent-accredited.html`
2. **tashkent.mofa.gov.bd**: the pages "Repatriation of Dead Body", "Other Consular Services & Fees" and "Relation with Accredited Countries" (menu links; empty when fetched by script) → `bdemb-tashkent-dead-body.html`, `bdemb-tashkent-consular-fees.html`
3. **The Embassy's Facebook page** (search Facebook for "Embassy of Bangladesh Tashkent"): posts about Kyrgyzstan, especially the e-passport camp in Bishkek (Dec 2025), the 180 workers sent home (Sept 2025), and any warning about Kyrgyzstan jobs or visas → screenshots `bdemb-tashkent-fb-kyrgyzstan-<yyyy-mm-dd>.png`
4. **Bangladesh Honorary Consulate in Bishkek**: http://bangladeshhc.kg/ (if it loads) → `bangladeshhc-kg-home.html`

### Priority 2: Kyrgyz official pages

5. **Kyrgyz Customs, cash rules for travellers**: https://www.customs.gov.kg/site/ru/master/customskg/jeke-adamdar-ucun, open the section "Информация относительно перемещения наличных денежных средств" → `customs-kg-cash-movement-info.html` (is the USD 5,000 cash-export limit for foreigners still in force?)
6. **Ministry of Labour (mlsp.gov.kg)**: the labour inspection's contacts page (address, phone) → `mlsp-kg-labour-inspection-contacts.html`
7. **e-Visa portal, employer account** (only if someone has one): screenshots of the Unified Permit application form and its fee screen at https://www.evisa.e-gov.kg/login.php?lng=en → `evisa-kg-unified-permit-form-<n>.png`

### Priority 3: news and money (turn guesses into facts)

8. **Bangladesh Post, 180 workers back from Kyrgyzstan (Sept 2025)**: https://bangladeshpost.net/posts/180-bangladeshis-return-from-kyrgyzstan-after-falling-victim-to-fraud-160383 → `news-bangladeshpost-kyrgyzstan-180-return-2025-09.html`
9. **Business & Human Rights Resource Centre, sewing-shop case (June 2024)**: https://www.business-humanrights.org/en/latest-news/kyrgyzstan-exploitative-sewing-shop-subjects-south-asian-workers-to-slave-labor-conditions-neglects-proper-standards-and-fails-to-pay-promised-wages/ → `news-bhrrc-kyrgyzstan-sewing-shop-2024.html`
10. **MBANK international transfer tariffs** (mbank.kg, "В другую страну"; does it send to Bangladesh, and the fee?) → `mbank-kg-international-transfers.html` or `.png`
11. **Western Union, Kyrgyzstan to Bangladesh**: the price estimator at westernunion.com with "send from Kyrgyzstan" and "to Bangladesh" (bKash or bank, fee for USD 200) → `westernunion-kg-to-bd-estimate.png`
12. **National Bank of Kyrgyzstan's Facebook video** on its WhatsApp complaints channel: https://www.facebook.com/NBKR.kyrgyzbank/videos/572400441278404/ → `nbkr-fb-whatsapp-consumer-channel.png`
13. **Facebook video "কিরগিজস্তান ভিসা আপডেট | ভিসা কবে খুলবে? ২০২৬ নাকি ২০২৭?"** (page 61569888204436, 19 Oct 2026): screenshot of the post and top comments → `fb-kyrgyzstan-visa-update-2026-10-19.png`

### Not online: ask by phone or email if possible

14. **BMET Emigration branch**: was there any notice or instruction in July-September 2025 that stopped clearances for Kyrgyzstan (57 in Aug 2025, 1 in Sept, 11 in all of 2026)? → a note or photo of any letter, `bmet-notice-kyrgyzstan-2025.pdf`

### Priority 4: visit and study (added after the last agent finished)

15. **e-Visa portal, "Do I need visa?"** at https://evisa.e-gov.kg/get_information.php?lng=en: choose Bangladesh and each purpose (tourist, business, study, private); screenshot each result with the fee → `evisa-kg-do-i-need-visa-bangladesh-<purpose>.png`
16. **Kyrgyz Foreign Ministry visa page**: https://www.mfa.kg/consular-service/obshie-vizovie-trebovaniya_en.html (or mfa.gov.kg visa regime pages; they failed for us) → `mfa-kg-visa-regime.html`
17. **BMDC Eligibility Certificate notice of 10 Feb 2026** (scanned PDF): https://www.bmdc.org.bd/upl/doc/news/iCqLeVnNmDcT.pdf → `bmdc-eligibility-certificate-notice-2026.pdf`
18. **BMDC Act 2020**: https://www.bmdc.org.bd/docs/bmdc_act_2020.pdf → `bmdc-act-2020.pdf`
19. **Kyrgyz Ministry of Health: list of accredited medical universities (2026)** and order No. 912 of 3 Aug 2026 (med.kg or gov.kg) → `moh-kg-medical-accreditation-2026.pdf`
