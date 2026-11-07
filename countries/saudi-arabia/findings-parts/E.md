# Findings, part E: other visas, changing visa, asylum, money home, no papers, death/injury, coming home, destination, contacts

Draft written to `drafts/SA5.md` (replaces saudi.src.md lines 263-328). Ledger rows E0001-E0145 in `ledger-parts/E.csv`. All refs.md keys in this chunk were replaced by ledger ids; claims that could not be re-verified were dropped (list below).

## Sources and how they were read

- Ministry of Expatriates' Welfare citizen charter (Aug 2026, objectstorage PDF): Bangla text layer garbled; pages 9-12 read as images. Welfare-1 (unpaid wages, saswelfare@, 02-41030251), Welfare-2 (aswelfare@; families' welfare, women's protection, compensation for deceased, bodies home, bringing men and women home), all free, 7 working days. Escalation: Joint Secretary, Mission and Welfare wing, 02-41030219, 01711427769, adsmission@ [E0001-E0006]. Item 18 refers to the "Policy on transport costs of bodies of irregular, undocumented, destitute and helpless migrant workers, 2022": the ministry pays for bodies of undocumented workers too.
- Welfare Board citizen charter (Sep 2026; copied from official-pdfs/, logged as manual from wewb.gov.bd/pages/office-citizen-charters): all 9 pages read as images [E0007-E0022, E0145]. Grievance route on p.9 [E0022].
- Welfare Board annual report 2023-24: SutonnyMJ (Bijoy) encoded text; quotes kept in that encoding. p.29: the Tk 3 lakh grant is for workers who left with BMET clearance or became Board members through a mission [E0037]. p.39: safe homes, one each in Riyadh, Jeddah and Madinah (7 in total with Oman, Jordan, Lebanon, Libya) [E0038]. The 2026 Board charter also lists safe homes in Riyadh, Jeddah and Madinah [E0019]. This settles the open Saudi-doc question (doc said three from a 2018 source; Netra News said Bangladesh funds two): official sources say three. It belongs to the domestic-worker chunk, not this one; passing it on.
- BMET citizen charter 2026, p.12 (image): airport desk services, Tk 5,000 for women returning within a year after abuse or fraud, Tk 35,000 cheque, re-entry visa attestation [E0039-E0043].
- BMET safe migration leaflet (Dec 2025): Bijoy text; insurance since 12 Mar 2023, Tk 1,000 premium, 5 years, Tk 10 lakh, partial disability 10-90%, Tk 50,000 for job loss within 6 months [E0044-E0047]. The Board charter says 10%-100% for disability [E0012]; both are official, the draft uses "10% to 100% of Tk 10 lakh" citing both. Insurance News BD gives partial disability as Tk 1-5 lakh (not used).
- Embassy pages (Riyadh): SEP page, labour wing, contact page (pandoc md was empty; made raw/bdemb-riyadh-contact.txt from the saved html), online request form (srspub, fetched by another part), passportriyadh.com appointment site. All undated, so possibly-outdated.
- Welfare Board list of labour wings abroad: live page fails (curl 000; Firecrawl TLS error; skipping TLS verification was refused by the permission system). Got the Wayback capture of 11 Mar 2026 (page says last updated 6 Oct 2025); the table is base64-encoded in the page, decoded to raw/wewb-labour-wing-contacts-wb.txt [E0035, E0036].
- SPA (Saudi Press Agency) 27 Apr 2026, Interior Ministry: overstay fine up to SR 50,000, up to 6 months, deportation [E0053]. Pandoc md empty; text extracted from the page's embedded JSON into raw/spa-overstay-penalty.txt.
- PKB reintegration loan page (pkb.gov.bd, updated 23 Sep 2026): curl worked; content base64-decoded into raw/pkb-reintegration-loan-page.txt [E0113-E0117]. Replaces the eduitbd guide-site source [N255]. Adds the Tk 3-5 lakh co-collateral tier and the full document list.
- Firecrawl scrapes saved as excerpts (navigation removed): ksavisa medical, pr.gov.sa, World Bank RPW, bKash MTO page, Saudia transit visa, two Prothom Alo articles.

## Other visas

- Temporary work visa: only Wego (Jun 2026) [E0065, E0066]. Official Qiwa page not found by search. Employer chooses nationality per visa group on Qiwa (Wego), so not barred to Bangladeshis; open question is the Bangladesh side (BMET clearance for a 90-day visa).
- Hajj seasonal visa: Saudipedia (2023) [E0067]. Wego says the seasonal visa was renamed "temporary work visa for Hajj and Umrah services" for specific nationalities, not listed.
- Stopover visa: Saudia page (official airline, with MOFA) [E0141, E0142]; fee figures (SR 39.50, insurance from SR 13) and Bangladesh eligibility only from KSA Expats 2024 [E0068]. visitsaudi.com stopover URL returned 404.
- Medical visa: KSA Visa page, fee USD 80 + 10.5 + 10.5 + insurance [E0069]. Draft's "USD 101 plus insurance" matches the sum.
- Premium Residency: product list only [E0071]; eligibility thresholds not researched (not a route for the doc's readers).

## Changing visa type

- Visit to iqama: Gulf News 2022 quoting Jawazat [E0054, E0055]; Umrah not for work: Gulf News 2024 quoting the Ministry of Hajj and Umrah [E0056]. No newer official statement found; still cited as news.
- Dependants: KSA Expats 2024 citing Okaz [E0060, E0061]. Search found a 2025 DLA Piper note that the minister was given authority to regulate dependants' work permits, and a Middle East Briefing 2026 summary claiming dependants can now get separate permits; neither gives sectors or procedure. Kept "Need to know".
- Domestic worker between households: Gulf News 2023 [E0062, E0063, E0144].
- Domestic worker to company: Saudi Gazette, 9 Mar 2022 [E0132-E0134] answers the old "Need to know" (possible, within the first year only). News only; no current official page found.
- Job title change: MHRSD service page [E0048-E0050]; Jan 2026 suspension of some titles: Deloitte [E0064]. The draft now says the employer pays any fee [E0137].

## Asylum

- US State Department 2024 report (published 2025), replacing the 2023 report on ecoi.net (also saved) [E0072-E0075]. Same substance; adds "authorities sometimes indefinitely detained individuals who lacked travel documents".

## Sending money home

- World Bank RPW, Q3 2025 data (page date Sep 2025, so possibly-outdated) [E0080]. The draft's "STC Pay has been cheapest and banks dearest" now has the actual figures.
- bKash partner list for Saudi Arabia now includes Saudi Awwal Bank, tiqmo and barq, besides STC Pay, URpay, Mobily Pay, WU, MoneyGram [E0082]. Limit Tk 2.5 lakh per transfer; cash out Tk 7 per thousand at ATMs [E0083, E0084].
- 2.5% incentive: kept in FY2026-27 budget (TBS 11 Jun 2026) [E0076]; no-documents rule from a May 2022 Bangladesh Bank circular reported by TBS [E0081]; no later reversal found. Bangladesh Bank circular itself not fetched.
- Hundi: why workers use it (TBS Dec 2024) [E0077]; account freezes (Prothom Alo 2023) [E0078]; Saudi arrests (Gulf News 2021) [E0079]. BMET leaflet is the official line [E0046].
- Not found: whether STC Pay or other apps need a valid iqama (likely, but no source); this matters for workers without papers.

## Going home without valid papers

- SEP covers only companies under the labour offices of Riyadh, Al Qassim, Hail, Al Jouf, Northern Borders and the Eastern Province [E0027]. The western region (Makkah, Jeddah, Madinah, etc.) falls under the Jeddah consulate; no Jeddah SEP page was found (consulate site bdcgjeddah.org did not resolve). "Need to know" kept.
- SEP excludes women domestic workers, people with cases or "matlub", and people who did not leave on an earlier exit visa [E0028]. The draft's "can take months" is from a 2023 embassy notice reported by Prothom Alo [E0096]; no newer figure found.
- Online links: sepsrv.html (rules + application button), /sep/ and /seppub/ (status search) are linked from the embassy home page. The old draft link sepNew was not found on the current site.
- Outpass: no Saudi-specific list of documents or fee found (searched English and Bangla; found Dubai and Delhi equivalents only: police report, passport copy, photos, ticket). UNB 2026: embassy officials visit detention centres and issue travel permits [E0088]. The embassy's own deportation.html page only lists counts of travel permits issued. "Need to know" kept.
- Grace periods: replaced "Watch Absher for amnesties" (Saudi embassy e-services page did not support that) with the March 2026 example announced by the Bangladesh Embassy (Daily Star Bangla) [E0087].
- Bans: Wego (Jul 2026) [E0057-E0059]; ban clock starts on leaving; huroob bans usually lifted only by the sponsor. Wego also describes checking a ban: Absher (needs an iqama), or a Saudi contact via Muqeem, or the Saudi embassy; not put in the doc (unverified procedure).
- Dropped: "employer pays the deportation ticket, or the Saudi government" (Philippine DFA, 2013); too old and not re-verified. MHRSD says a worker leaving without a legitimate reason pays his own return [E0136].

## Death, injury, job loss

- Reality checks: bodies of undocumented workers take much longer (BRAC via Prothom Alo, 6 Oct 2026) [E0090]; families visit the Board repeatedly; irregular returnees get nothing [E0092]; cause of death written abroad, mostly "natural", not checked by Bangladesh [E0093]; insurance claims rejected for suicide and pre-existing or serious illness; middlemen take commissions [E0097, E0098]. About 2,000 Bangladeshi workers died in Saudi Arabia Jan-Sep 2026 [E0094] (not used in the doc; statistic).
- Example of the system working: two brothers died 16 Jul 2026, bodies home 28 Jul, Board paid Tk 35,000 each [E0095] (not used).
- Insurance claims are settled by Jiban Bima Corporation; the Board collects the premium [E0099] (not used).
- GOSI: official FAQ says occupational hazards insurance covers all workers regardless of nationality, employer pays 2% [E0100, E0101]. Dropped the draft's "3 years' wages, up to SR 56,000" (Indian Embassy GOSI page returned HTTP 500 and was not re-verified). Saudi Gazette 2020 (via search, not fetched) gives total disability for non-Saudis as 84 months of benefit, up to SR 330,000. "Need to know" kept on death benefit amount and claim time.
- Employer pays body preparation and transport unless relatives agree to local burial; exempt if GOSI pays (MHRSD) [E0135].
- Would outside bodies take individual cases? Searched: BRAC helps families apply to the Board (Prothom Alo case) [E0143] and runs airport help [E0111]. No evidence found that ILO or IOM take individual Saudi cases; not mentioned in the doc.

## Coming home

- Customs (HSIA page, citing SRO 261 of 2 Jun 2025): 2 used + 1 new phone once a year [E0103]. Conflict with the draft's Financial Express 2025 line ("one new phone, or two with a BMET card and 6 months abroad"): FE page could not be read (pandoc output empty); the official HSIA page is used. Gold: 117 g / one 10-tola bar per year at Tk 5,000 per 11.664 g [E0104]; declare within 7 days at the custom house if missed [E0106].
- BRAC: brac.net migration page has no address or phone. BRAC Centre address and hours come from the UK Home Office returns page (for UK returnees) [E0112]. Old draft phone 02-222281265 dropped (unverified). Search also found a 2020 BRAC-IOM hotline +08000102030 / 09610102030; these are now the Welfare Board's call-centre numbers [E0021]. "Need to know" kept for a BRAC line.
- Probash-Bondhu (16135): now confirmed as the Board's Probashi call centre in its own charter [E0021], replacing the 2022 Dhaka Tribune source.

## Destination

- 2026 context not in the old draft: Saudi visa cancellations over fake demand (TBS Bangla, 7 Mar 2026) [E0127]; Jan-17 Oct 2026 departures to Saudi down 45% (TBS Bangla, 25 Oct 2026, BMET data) [E0129]; flight disruption from the Iran war and Houthi attacks [E0130]; 90% of BMET complaints in 2025 about Saudi Arabia [E0128]. Same article: remittances from Saudi in Jul-Sep 2026 were USD 1.65 billion, 19.2% of the total (not used).
- Al Jazeera list now includes Sudan (1 million) [E0121]. Arab News "3.5 million Bangladeshis" alternative estimate dropped (one number is enough); TBS Bangla says over 3 million unofficially.
- No official BMET statistics page fetched (bmet.gov.bd is on the blocked list; not tried with Firecrawl for lack of a known stats URL). Numbers are BMET figures reported by news.

## Contacts

- 19911 languages: conflict. MHRSD news (May 2024) says Arabic and English [E0051]; the Indian Embassy page (updated 15 Mar 2026, Wayback copy) says multiple languages including Bengali [E0138]. Kept as "Need to know".
- Jeddah labour wing numbers from the Welfare Board list (Oct 2025) [E0036]; not confirmed by the consulate (site unreachable).
- Hajj helpline 16136 and +880 9602666707 from hajj.gov.bd [E0139]; Musaned 920002866 from MHRSD service page [E0140].
- Dhaka airport desk officer phone in BMET charter is printed as "07152-28307" [E0043], which looks like a typo; the Board's charter number +88 02 8901040 is used instead [E0008].

## Need to know (open, with what was searched)

1. Other visas: whether BMET gives clearance for a 90-day temporary work visa and whether agencies process them. Searched Qiwa/MHRSD (no official page found), BMET charter, news.
2. Changing visa type: whether dependants can work outside health and education. Searched Ajeer, MHRSD, Saudi Gazette, DLA Piper, Middle East Briefing.
3. Going home without papers: SEP-equivalent procedure for the western region (Jeddah consulate). Searched embassy site, consulate site (down), Bangla news.
4. Going home without papers: documents and fee for a travel permit (outpass) in Saudi Arabia. Searched embassy site (deportation.html, notice.html), Bangla and English news, other missions' pages.
5. Death: how much GOSI pays a family for a work death and how long claims take. Searched GOSI FAQ pages; amounts only in third-party sources.
6. Coming home: a BRAC phone line for returnees from Saudi Arabia. Searched brac.net, news, UK Home Office page.
7. Contacts: whether 19911 answers in Bangla (official vs Indian Embassy conflict).

The old draft's "Need to know: whether a domestic worker can move to a company job" is now answered (yes, within the first year) [E0132-E0134].

## Dropped from the old draft (could not re-verify, or replaced)

- GOSI "3 years' wages, up to SR 56,000" [N143]; deportation ticket rule [N221]; outpass via passport wing as stated in [N211] (replaced with UNB detention-centre line and embassy booking site); "Watch Absher for amnesties" [36, N172]; BRAC phone 02-222281265 [114]; mobile phone allowance per [N293]; Arab News 3.5 million estimate; "It takes much longer if the worker had no valid papers" now cited to the 2026 Prothom Alo article.

## Blocked

None outstanding. wewb.portal.gov.bd labour wing page was recovered from the Wayback Machine. Financial Express baggage-rules page downloaded but its text could not be extracted (not needed; official HSIA page used).

## Fix round after the independent check (7 Nov 2026)

New ledger rows E0146-E0181; new sources registered: UNHCR KSA contact page (Firecrawl; curl 403), Social Insurance Law (Royal Decree M/273, 1445H, MISA PDF), GOSI Occupational Hazard services page, MHRSD Directory of Services for Expatriates (August 2024 edition, has the Ajeer contact block the November edition lacks), Jeddah consulate officers page (table extracted from html to raw/bdcg-jeddah-officers.txt), embassies.info (Jeddah address, lead), IOM-BRAC PROTTASHA leaflet (Firecrawl; curl 403), Bangladesh Bank CIPC page (Firecrawl; curl copy is a captcha page, ignore raw/bb-cipc-procedure.*), embassy Notice page (text extracted to raw/bdemb-riyadh-notice.txt), Welfare Board district centre list.

- Ajeer dependants: the official MHRSD directory (Nov 2024, "Accompanying Ajeer") replaces the KSA Expats blog as the main source: establishment issues the contract (Contracts, Issue Contract, Contracting Service Between Workforce, Ajeer Accompanying Service), no fees, low green band or higher, education or human health and social work, both iqamas valid, dependant 18+, spouse or mahram [E0148-E0152]. Who "approves" (the "beneficiary") is ambiguous in the directory, so the draft says only "once the contract is approved". Ajeer: ajeer.qiwa.sa, 920011040 [E0147]. The 2025 DLA Piper note on the minister regulating dependants' permits is not cited and was removed from the doc.
- Musaned household-to-household transfer: the official directory says the CURRENT employer starts it on Musaned after the worker's approval, the new employer accepts or rejects, completed through Absher; no fees; worker needs an Absher account [E0153, E0154]. This corrects the old line ("the new employer starts the transfer"), which came from Gulf News 2023. Musaned regulation: employer bears transfer fees [E0180]. Complaint route: domestic workers' dispute committees, free, e-services Individuals Portal [E0155]. The site is musaned.gov.sa (not musaned.com.sa).
- GOSI death benefit: Social Insurance Law art. 39(3): non-Saudi dying from a work injury, family gets a lump sum of 84 x the permanent total disability benefit, which (art. 35(1)) is 100% of the average monthly contributory wage [E0157, E0158]. Art. 40: GOSI pays body preparation and transport home [E0159]. Art. 6: domestic workers (and temporary/seasonal visa workers of up to 60 days) are covered only by board decision [E0160]. GOSI service page: non-Saudi lump sum for death, delivered "At Office" [E0161]. Not found: papers GOSI needs from heirs abroad, time to pay, whether a board decision now covers domestic workers. The 2020 Saudi Gazette figure (84 months, up to SR 330,000) is consistent but was not fetched.
- UNHCR Riyadh: toll-free 009668001000281 (Sun, Tue, Thu), visits Mon and Wed 9-3 by appointment only (Diplomatic Quarter), applications by email saprstaf@unhcr.org with listed details [E0163-E0165]. The un.org page gives +966 55 710 7542 (not used).
- BRAC phone: IOM-BRAC PROTTASHA leaflet lists the BRAC Information Center opposite Dhaka airport, 01700797182/3, and BRAC Reintegration Service Centers in 11 districts [E0170]. The leaflet's project is for returnees from the EU [E0171], so the doc keeps a Need to know on whether it serves Saudi returnees. amiprobashi.com/brac-service (gives helpline 16768) could not be read: DNS failure for curl and Firecrawl. The gov.uk BRAC Centre address [E0112] was dropped from the doc (head office, not a service point).
- Jeddah consulate: the consulate's own officers page (undated, current officers) gives labour counsellor +966501365198 and first secretary +966126335082, newer than the Welfare Board list of Oct 2025 [E0036] (+966 12 689 6276 ext 131, +966 12 680 2048 ext 138); doc now uses the consulate's page [E0166-E0168]. The consulate's "Address and Phone Number" page is not_found; its Facebook page (bcgjksa) can't be scraped; address from embassies.info (lead, edited May 2026) [E0169]: Old Makkah Road, Kilo-3, Bab Al Khalil, Al-Nazlah Al-Sharqiyah, Jeddah 22335; phones +966 12 687 8465 / 689 4712 / 688 1752 (not used: unverified).
- bKash complaint route: Bangladesh Bank CIPC 16236, bb.cipc@bb.org.bd, online form; steps: provider branch, provider complaint cell, then CIPC with the provider's final reply letter; third parties need written authorisation [E0172-E0174].
- Grace periods: the Daily Star Bangla report says the embassy announced the March 2026 window in a notice (bijnapti) [E0176]; the embassy website's Notice page carries such notices (e.g. deadlines to leave on issued exit visas; also unpaid-wage claims for workers of closed companies Saudi Oger, Mohammad Al-Mojil Group, Saad Trading: worth passing to the unpaid-wages chunk) [E0175].
- District probashi kallyan centres: listed on wewb.gov.bd (officers page filtered to "District Probashi Kallyan Centre list") with officer, address, office phone, mobile and email [E0177].
- Medical visa: Tasheer Dhaka centre address from Limpid Travels 2023 (lead) [E0178]; booking at vc.tasheer.com [B0040]. Not found: whether Tasheer Dhaka takes medical visa applications; medical visa document list.
- 19911 language: MHRSD (May 2024) says Arabic and English [E0051]; India's embassy says multiple languages including Bengali [E0138]. The doc states MHRSD's own line and points to the embassy labour wing for Bangla, which works whichever is right.
- Remittance: World Bank RPW raw table names "Saudi British Bank"; the doc writes "Saudi British Bank, now Saudi Awwal Bank" (the bank renamed in 2023; rename not separately sourced). Removed the "why workers use hundi" line [E0077] (no action). Saudi arrests now worded as "have arrested expatriates" (Gulf News 2021, lead). Added B0112 (no iqama, no formal remittance). The "open two bank accounts before leaving" line was removed from this chunk: the before-you-go section (src line 94) already states it [B0104].
- Stopover visa: cut to one paragraph, Saudia only (flynas route dropped); the KSA Expats fee figures (SR 39.50, SR 13) removed. my.gov.sa transit visa page and visitsaudi stopover page could not be scraped; no source found on whether work is allowed.
- Hajj seasonal visa: "the employer pays" changed to "a SR 1,000 entry fee is required" (Saudipedia doesn't say who pays). The old SR 2,000 guarantee and end-of-Muharram exit deadline have no source in the ledger; dropped.
- Temporary work visa to iqama: E0066 says only "not linked to an iqama", so conversion is now a Need to know; only the seasonal visa is cited as non-convertible [E0067].
- Premium Residency: pr.gov.sa saved pages hold no fees or thresholds; cut to one line plus Need to know.
- From-Bangladesh application template removed (our own text).
- Insurance: limited to workers who left from 12 March 2023 [E0044]; "usually" changed to "often" [E0097].
- Death step 4: removed the "bodies come home fairly quickly" line [E0090]; kept the cause-of-death line with a Need to know on challenging it.
