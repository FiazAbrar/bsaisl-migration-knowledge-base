# United Kingdom: research notes

## What this version is built from

10 Prothom Alo articles (May 2024 to October 2026) from the archive chunk xchunk-united-kingdom.jsonl, read in full; all 10 used, 69 facts logged (XK0001 to XK0069), all cited [N] as news. No official source has been fetched yet, and no network research was done for this version.

The reporting covers the May 2024 returns agreement, asylum claims by Bangladeshis, student visas (e-visa, the June 2026 Basic Compliance Assessment, universities restricting Bangladeshi and Sylhet applicants, withdrawn sponsorship after UKVI interviews), Commonwealth Scholarships, the 10-year ban for visa fraud, citizenship deprivation, remittance and postal-vote registration. It says nothing on the Skilled Worker or care-worker visa, visit visas, family visas, costs or work rights; those are "Need to know" items in the doc. The global Illegal routes doc already holds UK material from other articles (a Sylhet returnee's student-visa case, BBC reporting on fabricated gay asylum claims, the October 2026 asylum-fraud penalties) and the Dalal scams doc a Sylhet UK work-permit fraud case; the doc points there rather than repeating it.

## Second pass: 11 articles missed by the earlier filter (lchunk-united-kingdom.jsonl)

11 more Prothom Alo articles (March 2024 to October 2026), read in full; all 11 used, 80 facts logged (XK0070 to XK0149). They add: the care-worker / Skilled Worker visa and the BBC's 2024 investigation into fake certificates of sponsorship sold to foreign students (new H2 "Care-worker and Skilled Worker visa"); GREAT, Women in STEM and Commonwealth PhD scholarships (new H3 "Scholarships" with three H4s); the British Council pre-departure briefing (Step 3); Starmer's June 2024 Rwanda pledge and Labour's clarification (Status, Removal to Bangladesh); the November 2025 Denmark-style asylum plan; the April 2026 BBC investigation into paid-for false asylum stories and the 6 October 2026 Aponjon raids (new H3 "False asylum stories and the advisers who sell them"); frauds the UK has cracked down on (Visa fraud section).

None of the 11 articles answers the Need to know items on the Skilled Worker / care-worker route from Bangladesh (BMET clearance, numbers, how it is sold in Bangladesh), the visit visa, student visa fees or the money to show; those stay open. The care-visa fraud cases are Indian students already in the UK, not Bangladeshis.

Facts logged but not cited from this pass: XK0071 (2024 GREAT round, superseded by the 2025-26 round XK0072), XK0091 (general "lakhs of pounds" line, covered by XK0093), XK0117 (Women in STEM totals so far; no bearing on a decision). Left out: the 2024-25 GREAT university list (superseded), the Tower Hamlets councillor's resignation and political reactions to Starmer's remark, and the July 2024 article's community wish list (the UK Bangla Press Club president's request not to deport undocumented Bangladeshis is an appeal with no outcome).

## Where the official research pass should start

- UK Home Office / UKVI (gov.uk): Student visa (fees, Immigration Health Surcharge, financial requirement, work hours, dependants), Skilled Worker and Health and Care Worker visa (eligible care roles, salary thresholds, sponsor change, the 2025 closure of overseas care-worker recruitment if confirmed), Standard Visitor visa, e-visa and UKVI account guidance, Basic Compliance Assessment guidance for sponsors (June 2026), general grounds for refusal (10-year ban for deception).
- Home Office immigration statistics: study visas, work visas, asylum claims and grant rates, small-boat arrivals and returns, for Bangladesh nationals 2023-2026.
- UK-Bangladesh returns arrangement (May 2024) and Joint Working Group statement; status of the Rwanda scheme.
- British High Commission Dhaka: visa fraud notice of 25 November 2025; VFS Global visa application centres in Dhaka and Sylhet.
- Commonwealth Scholarship Commission: calls for Bangladesh, nominating agencies (University Grants Commission, Ministry of Education).
- Bangladesh High Commission London (and any offices elsewhere in the UK): address, helpline, labour/welfare wing, help for people facing removal.
- BMET: clearance figures for the United Kingdom by year (any care-worker or skilled-worker departures).
- Bangladesh Bank: country-wise remittance, United Kingdom, FY2023-24 to FY2026-27.
- British Nationality Act 1981, section 40 (deprivation of citizenship).

## Official research pass, 2026-11-23/24 (prefix OK)

**Searched and saved (40 official sources, 2 news):** GOV.UK guides (printable versions) for the Student, Graduate, Skilled Worker, Health and Care Worker and Standard Visitor visas, the immigration health surcharge, TB tests (and the Bangladesh clinic list), eVisa account and travel, administrative review, visa application centres, claiming asylum, asylum support, asylum helplines, permission to work for asylum seekers, finding an immigration adviser, minimum wage rates; Immigration Rules Appendix Student (work hours table) and Part Suitability (deception refusals and the re-entry ban table); student sponsor guidance Document 3 (Basic Compliance Assessment thresholds, licence revocation); the March 2026 visa brake guidance; the May 2024 returns agreement news story; BHC Dhaka organisation page, its 2021 work-visa scam notice and a 2011 forgery-factory release; Home Office immigration statistics, year ending June 2026 (asylum and work commentary pages, asylum and visas summary tables); Bangladesh High Commission London (home, hours, officers), MOFA mission list (Wayback, 2022), CSC master's page and national nominating agencies, ICO complaint page (Wayback, 2024); bdnews24 (BMET UK figures) and The Business Standard (Bangladesh Bank UK remittance, IOM diaspora figure).

**Tooling note:** `bs4` is not installed here, so fetch.py made no `.txt` copies. A stdlib equivalent wrote `.txt` copies of the saved HTML (needed for tables pandoc drops, such as the student work-hours table). The Home Office `.ods` summary tables were saved as `.ods` and converted to tab-separated `.txt` with a stdlib script; quotes from them are table rows. The two large xlsx datasets (asylum claims, entry-clearance outcomes) were downloaded and dropped as too large; the summary tables carry the Bangladesh rows.

**Found and changed in the doc:**
- Corridor numbers now official: study visas (12,468 applications, 86% granted), work (3,785, 60%), visitor (37,254, 45%), family (2,069, 89%), asylum claims by year 2022-2025, 11% grant rate, prior route of claimants (4,789 of 5,769 held a visa first; 5 small boat), all year to June 2026.
- Care workers (codes 6135, 6136) cannot get a first visa from abroad since 22 July 2025; added "Visas not open to Bangladeshis".
- New sections: Standard Visitor visa, Graduate visa, Bringing family (student and worker), Changing employer, Visa brake, re-entry bans, ICO complaint steps, full Contacts.
- Student steps rewritten with official fees, money rule (28 days, 31 days), English (B2, Ecctis, SELT), TB clinics with addresses and taka fees, administrative review, eVisa account, work hours (20/10).
- Asylum: 30-month protection for claims from 2 March 2026; permission to work only after 12 months and only Immigration Salary List jobs; support £49.18 a week; Migrant Help line; IAA adviser register.
- BMET (via bdnews24, news): 10,383 in 2023, 3,550 in 2024. Bangladesh Bank (via TBS, news): about USD 3.5 billion from the UK in July 2025 to March 2026.

**Need to know:** of the 30 earlier questions, 17 were answered and removed, 13 were kept in sharper form, and 4 new ones were added (17 open). Answered: Skilled Worker/care route and BMET numbers to 2024; visit visa requirements, fees, time and refusal share; student dependants; study visa numbers; student fees, IHS and money; minimum wage; university licence loss; changing employer; English tests; refusal review; UKVI account; Graduate visa length and cost; Commonwealth nominator and pay; overseas care recruitment; asylum numbers and grant rate; asylum seekers' work; adviser register; small-boat numbers; BHC London contacts; ICO process. Several were reworded into sharper open questions.

**Official facts logged but not cited:** OK0021-OK0022 (document list, covered by the steps), OK0051-OK0052 (surcharge exemptions repeated elsewhere), OK0055 (general TB rule; the Bangladesh-specific OK0056 is cited), OK0137 (travel risk during a sponsor investigation, a narrow case). News facts no longer cited after this pass: XK0001-XK0004, XK0006, XK0007, XK0013-XK0015, XK0019, XK0024, XK0026-XK0030, XK0057-XK0059, XK0092, XK0096, XK0125, XK0163 (each replaced by an official fact).

## Pages we could not download

- https://visa.vfsglobal.com/bgd/en/gbr/attend-centre (403; Wayback copy is an empty script shell). Should show the UK visa application centres in Bangladesh, addresses, hours and paid extras. Suggested name: vfs-bgd-gbr-attend-centre.
- https://www.bb.org.bd/econdata/wageremitance.php (redirect stub). Should give Bangladesh Bank's country-wise remittance including the UK. Suggested name: bb-wage-remittance-countrywise.
- BMET statistics (old.bmet.gov.bd/BMET/stattisticalDataAction and bmet.gov.bd/pages/statistical-data returned 404). Should give the country-wise clearance table with the UK for 2023-2026. Suggested name: bmet-countrywise-2026.
- https://mofa.portal.gov.bd/site/page/013ad4d9-5f3b-4b29-b772-6af04c351095 (no connection; 2022 Wayback copy used for the London address and phone). A current copy would confirm them.
- https://ico.org.uk/make-a-complaint/data-protection-complaints/data-protection-complaints/ (403; 2024 Wayback copy used). A current copy would confirm the 14-week figure.
- Firecrawl was not authenticated in this session, and web search hit its usage limit partway; the Rwanda scheme's formal end, the November 2025 asylum reform statement and a gov.uk copy of the 25 November 2025 visa-fraud warning were not found on gov.uk by search.

## Resolved conflicts

- **Bangladeshi asylum claims in 2023 (official pass):** Prothom Alo's "about 11,000 with 95% refused" [XK0003] conflicts with the Home Office's own table: 5,191 people claimed in 2023 [OK0152]. The official figure stands; XK0003 and XK0004 are no longer cited. The 11% grant rate for the year to June 2026 [OK0151] replaces the 95% refusal claim.
- **Basic Compliance Assessment:** Prothom Alo's thresholds [XK0057, XK0058] match the official guidance [OK0128, OK0130]; the official facts are cited instead.
- **Student work hours and Graduate visa:** news "20 hours" [XK0162 kept only for placements] and "up to two years" [XK0163] confirmed and refined by Appendix Student (20 hours degree level, 10 below) [OK0033, OK0034] and the Graduate guide (2 years to 31 December 2026, then 18 months) [OK0032].
- **Channel crossings:** the Bangladesh High Commission's 2024 letter that no Bangladeshi entered by boat [XK0019] is superseded by Home Office data showing 5 Bangladeshi asylum claimants who came by small boat in the year to June 2026 [OK0153]; XK0019 dropped.
- **Asylum support while pending (researchers, XK0013/XK0014)** replaced by the official asylum support page [OK0175, OK0176]; **remittance "more than USD 2 billion" (XK0015)** replaced by Bangladesh Bank's figure via TBS [OK0216].
- **10-year ban:** the High Commissioner's 2025 statement [XK0033] matches the Immigration Rules' re-entry ban for deception [OK0139]; both kept.
- **Visa application centre operator:** GOV.UK links Bangladesh to VFS Global, but the quote check strips link targets, so the operator is not stated in the doc; kept as a Need to know.


- **Bangladeshi asylum claims in 2023:** about 11,000 claims with 95% refused (17 May 2024 news report of the returns agreement, attributed to the UK side) [XK0003] vs 4,258 applicants with about 71% refused (24 May 2024 opinion piece citing the EU Asylum Agency's database, and not explicit that the figure is for Bangladeshis) [XK0010]. The first is closer to the primary source (the UK government's own announcement of the agreement) and the second is a secondhand database figure of unclear scope; the doc uses 11,000/95%. XK0010 left uncited. The official pass should check Home Office asylum statistics.
- **Bangladeshis crossing the Channel:** the researchers wrote that many Bangladeshis who reached Italy "tried" to cross the Channel [XK0009]; the Bangladesh High Commission wrote in 2024 that no Bangladeshi had entered the UK illegally by boat [XK0019]. Not settleable from this set (an attempt is not an arrival, and the High Commission's letter is advocacy); the doc gives both with attribution and asks for Home Office small-boat figures in a Need to know.
- **"Withdrawal" vs "refusal" rate (October 2026 article):** the article calls the 23.5% Bangladeshi figure a "withdrawal rate" (প্রত্যাহারের হার) while the article is about refusal rates and the Home Office's refusal-rate threshold. Likely a translation slip, but it changes what the number means, so the doc keeps the article's figures neutrally ("the rate reported") and has one Need to know.
- **Russell Group description:** "24 leading universities" (June 2026). Not in conflict with anything.
- **Graduate work visa length:** the only source (July 2024, pa-2024-07-04-6ngsgospii) gives up to two years; the doc states it with a "Need to know" asking whether that still holds for 2026-2027 graduates, since no newer source in the archive confirms it.

## Facts logged but not cited

- XK0005 (the minister's statement of purpose; no bearing on what a migrant does), XK0010 (superseded asylum figure, see above), XK0011 (UK does not publish applicant details; research narration), XK0016 (researchers' view that the UK is interested in recruiting legally from Bangladesh; an opinion, not a route), XK0047 (duplicate of the June 2026 compliance rules), XK0052 (most international students leave within five years; no bearing on a decision).

## Held for other docs (see ledger)

- 2023 irregular arrivals in Europe (40,000+, 15,000+ in Italy) and the 2017 EU-Bangladesh return SOP: global Illegal routes.
- Postal voting for 1.5 to 2 crore expatriates, first time: global FAQ.
- Second pass: nothing held; every usable fact in the 11 articles was UK-specific.
