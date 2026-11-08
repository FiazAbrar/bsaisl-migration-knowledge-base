# United Arab Emirates: research notes

Merged from the per-topic research files in `drafts/` (8 November 2026). Fact ids like [W0012] are rows in facts.csv.

## Corridor, costs and scams (prefix N)

- Searched: English and Bangla news, BSS, WAM, Embassy press releases, OEP data, GLMM, agency blogs.
- Conflicts: counts of cancelled visas grew over time; GMI 0.84m vs govt 1.2m; ministry official "no visas in 2025" vs BMET 13,750; OEP 2022 incomplete (4,247 vs 101,000).
- Facts N0001-N0148 use prefix N, including cost/chain/scam facts logged before the A instruction; A0001-A0004 are the first A facts.
- Agencies with large UAE activity per agencies.csv (Matco Enterprise, AVR Bangladesh, Al-Anas Overseas, Visa International, Al Saad Labour Supply) were not named in the doc; Al Anas is named only via the Dubai Taxi news.
- Sources needing date fixes: news-shomoyeralo-uae-visa-cancel-protest is 2026-07-27, news-toi-uae-visa-cancel-bangladeshis is 2026-09-16 (registered undated).

## Work visa (UAE side) and free zones (prefix W)

**Searched:** u.ae (work permits, job offers, skill levels, preparing to work, contracts, residence visa provisions, health conditions, recruiting mainland/free zones, fraud tips, track visa); MOHRE service pages (blocked to curl and Firecrawl; got Wayback copies of overseas permit, contract issuance, quotas, mission, temporary permit, classification news, inquiry site); ICP (FAQ, residency permit, visa issuance, 2024 services guide PDF); GDRFA visa status form; EHS and Dubai Health medical fitness; Wafid; Jafza guides; Bangladesh Consulate Dubai; Emirates NBD; Gulf News (SIM); The National (Dubai Police scam warning); Fragomen (Tawjeeh, 2018). Bangla searches ("আমিরাত কাজের ভিসা বাংলাদেশি ২০২৬") returned mostly agency/YouTube pages; corridor status left to agent N.

**Text copies rebuilt:** for MOHRE Wayback pages (and EHS, GDRFA form) fetch.py's cleaner removed the `<form>` holding the content, leaving near-empty .txt files. W rebuilt each `.txt` from the saved `.html` (visible text, scripts/styles removed; first line notes this), so quotes are checkable: mohre-new-work-permit-overseas, mohre-news-classification-2022, mohre-mission-work-permit, mohre-home, mohre-employment-contract-issuance, mohre-work-permit-quotas, mohre-temporary-work-permit, ehs-medical-fitness-residency, gdrfa-status-inquiry-form.

**Conflicts:**
- Contract registration deadline: u.ae 14 days after arrival (W0015) vs MOHRE service 60 days after entry (W0073).
- Time to complete residence: u.ae "within one month of entering" (W0021) vs ICP 60 days from entry (W0089, W0095).
- Residence in passport: u.ae recruiting page (27 Oct 2026) says the residence visa is "stamped in the employee's passport" (W0042); Jafza still speaks of "Residence Stamping" (W0115); news (Gulf News, May 2022; Keesing) reports ICP replaced stickers with the Emirates ID from April/May 2022, Dubai excluded at first. Gulf News and Keesing could not be downloaded.
- Free-zone law: u.ae "Working in free zones" (Aug 2026) says free-zone workers are generally not under the Labour Law (W0047) and are sponsored by the authority (W0046); u.ae "Recruiting in free zones" (27 Oct 2026) says free-zone rules apply together with the Labour Law (W0044). Draft uses the newer wording.
- Medical tests: u.ae "Health conditions" (W0029) limits syphilis/hepatitis B to nursery, domestic, food, salon, health-club workers; "Preparing to work" (W0023) lists them for all. Abu Dhabi X-ray vs "Dubai does not" (W0030) while Dubai Health/EHS run X-rays (W0102).
- Tawjeeh: Fragomen 2018 says levels 3-5 must attend, AED 203 (W0122); MOHRE 2026 delivers contracts of levels 6-9 at awareness centres (W0074).
- u.ae says MOHRE has "13 types" of work permits but lists 12 plus the private-teacher permit; the executive regulation lists 12 (a-l).

**Practice:** Dubai Police (Aug 2026) warns of fake job/visa offers via social media and WhatsApp (W0123, W0124). The six-month permit replacement rule (W0069) is the legal basis for a slot "changing name"; no Bangladesh-specific report found. No source found on what Bangladeshi workers pay in the UAE for Tawjeeh, medical or Emirates ID when employers pass costs on.

**Logged but not used:** W0001 (13 types), W0003 (Article 6 basic rule), W0034 (visa cancellation; for agent L "leaving"), W0032 (180 days outside; for L "going home on leave"), W0062 and W0077 (mission permit; for agent V), W0078-W0079 (classification news 2022; superseded by W0067), W0088 (urgent ID AED 150), W0090 (status change AED 500; for "changing employer"), W0043 (entities), W0097/W0099 duplicates, W0122 (old Tawjeeh).

## Bangladesh-side steps (prefix B)

- **Clearances to the UAE (for agent N):** BMET image 2015-2025: 25,271; 8,131; 4,135; 3,235; 3,318; 1,082; 29,202; 101,775; 98,422; 47,166; 2,993 to May 2025 [B0105]. OEP report (live): 2023 98,201; 2024 47,158; 2025 13,750; 2026 to 7 Nov 23,044 [B0107-B0110]. 2026 by month: Jan 1,446 ... Sep 4,442, Oct 951, 1-7 Nov 63 (sharp October drop) [B0111]. Women: 2015-2025 [B0106]; 2025 721, 2026 764 [B0112, B0113]. Conflict: 2023 = 98,201 (OEP) vs 98,422 (BMET image).
- **Conflict (visa status):** Bonik Barta says the UAE stopped issuing visit and employment visas to Bangladeshis after July 2024 [B0102], yet OEP shows 13,750 clearances in 2025 and 23,044 in 2026. Likely individual/attested visas or re-entries; unresolved, for the lead.
- **Conflict (welfare fee):** BMET charter Tk 3,500 [B0017] vs Ministry circular Tk 5,500 from 1 Oct 2026 [B0024]; Embassy Abu Dhabi's AED 200 = Tk 6,500 incl. insurance [B0025] matches the new fee.
- **Conflict (clearance fee):** BMET charter Tk 250 [B0017] vs news of abolition Dec 2024 [B0099].
- **Navira letter** says other benefits apply under Kuwait's law [B0006]: templated letters.
- **Practice:** clearance card issuance reportedly halted for a week in Sept 2026, cards allegedly sold through back channels [B0101]; BBS average recruitment fee Tk 4.17 lakh across corridors incl. UAE.
- Searched BMET misc-infos with 12 UAE terms; Ministry notices/press releases for আমিরাত, দুবাই, ভিসিট, সতর্ক (no UAE-specific notice found; the 12-country Ministry-approval rule of 4 Nov 2026 does not include the UAE: Serbia, Moldova, Belarus, Congo, Russia, Japan, Iraq, Laos, Vietnam, Cambodia...). No official 2017 cost order found online (cap only via news [B0100]).
- Facts logged but not used: B0031 (Dubai consular wing), B0035 (officials detail), B0067 (mission e-passport fee for labourers USD 30/45, useful for renewal in UAE), B0014 details, B0012.

## Rights at work and problems (prefix L)

**Searched:** uaelegislation.gov.ae (labour law 33/2021 consolidated to 29 Jul 2024, Executive Regulations 1/2022, penal code, narcotics law, cybercrime law, via Wayback PDFs because the site returns 403), u.ae private-sector pages (all dated Aug-Oct 2026), MOHRE service pages (via Wayback; mohre.gov.ae times out to curl), MOHRE Resolutions 47/2022 (amended) and 782/2023, iloe.ae, Dubai Health, ISAHD, Bangladesh Embassy Abu Dhabi pages and PDFs, HRW World Report 2026, Amnesty 2025, Gulf News, Bangla searches (unpaid wages, jail, visa fines).

**Conflicts:**
- Claim time limit: law Art 54(9) as amended 2024 says two years from end of job [L0147]; u.ae labour-disputes page still cites Art 10's old one-year rule. Used the law.
- Dispute timing: u.ae and ER Art 31 still say refer to court within 14 days; Resolution 782/2023 makes MOHRE decide claims under AED 50,000 itself [L0141]. Used 782.
- ILOE non-payment fine: u.ae says AED 400 for not paying [L0094]; older rules said AED 200. Used u.ae (Dec 2025).
- Hotlines: user brief gives 80060; official pages give 80084 (labour claims) and 600590000. A UAE government Facebook post mentions 80060 for "Tawafuq" centres; not confirmed on any official page.
- Penal code alcohol and fine amounts in the English translation are garbled ("(500,000) five hundred AED"); doc avoids the amounts.
- Midday-ban fine source is MOHRE's 2023 announcement [L0027]; 2025/2026 WAM pages could not be fetched.

**In practice:** HRW 2026: false absconding charges, wage theft, recruitment fees, passport confiscation, midday ban ineffective [L0248-L0250]; Amnesty: no unions or assembly, Dubai evictions from partitioned flats [L0251]. No Bangladesh-specific outcome data on MOHRE complaints found.

**Logged but not used:** L0099 (no ILOE premium during absconding complaint, unclear wording), L0097 detail duplicated, L0136 (notice during leave), L0216 duplicate of L0215 note, L0253/L0252 history only in one line. Worker protection insurance premium for domestic workers not used (domestic section belongs to another agent).

**Page dates approximate:** HRW 2026 set to 2026-01-01, Amnesty to 2026-04-01, Littler set to 2011-01-01 (article about 2011 rules).

**Free zones:** not researched (JAFZA, DMCC have own employment regulations); flag for the lead.

## Domestic workers (prefix D)

- Searched: uaelegislation.gov.ae (law, regulations; via Wayback, site 403), u.ae domestic workers page (updated 06 Oct 2026), u.ae trafficking, health, worker insurance, ILOE pages; MOHRE (site unreachable from here: curl, Firecrawl and WebFetch all failed; used Wayback copies of the domestic workers page and a 2023 news item); Ministerial Resolutions 674/675/676 (Wayback of u.ae media); OEP clearance reports (women by year; categories by year, from another agent's saved JSON); BMET charter 2026 (page images checked); Ministry housekeeping policy and women DW agency order (image PDFs, transcribed); Embassy/Consulate pages; HRW 2014; US TIP 2026; Gulf News 2022 and 2026; Arabian Business and BBC Bangla on the 2018 MoU; Bangla searches for UAE housemaid abuse and salary (mostly Saudi results).
- Conflicts: (1) appeal against MOHRE's decision: uaelegislation consolidated text (archived Oct 2026) says court of first instance, decided in 30 working days [D0050]; MOHRE's translation of the 2023 amendment says Court of Appeal, 15 working days [D0061]. Draft uses only "court within 15 working days". (2) Sick leave second 15 days: law says half pay [D0024], MOHRE page says unpaid [D0124]; draft follows the law. (3) Gratuity: MOHRE page (May 2024) says 14 days/year [D0122], but the 2022 law leaves the system to the Cabinet [D0048].
- Practice: route has collapsed from 24,307 women (2015) to under 1,000 a year; very few clearances are labelled housemaid. TIP 2026: fees paid at home, passports kept, shelters need formal victim status. No Bangladeshi safe home in UAE.
- Logged but not used: D0012, D0013, D0034, D0036, D0044, D0047, D0049, D0052, D0056, D0057, D0059, D0067, D0076, D0089, D0105, D0108, D0109, D0115, D0128-D0132 (Tadbeer package details; useful for Background), D0141-D0142 (BBC: 2018 reopening, Tadbeer legal adviser), D0144, D0151-D0152, D0163, D0165-D0166, D0193 (2018 Tadbeer prices: Bangladeshi recruitment ceiling Dh7,000; agency guide, old), D0194 (agency salary ranges, no Bangladesh rate). D0193/D0194 are weak; keep for Background only if nothing better.
- Not found: current Bangladesh minimum wage for UAE housemaids; whether UAE visas for Bangladeshi domestic workers are issued in Nov 2026; real cost; phone rights; Embassy shelter practice.

## Visit and short visas (prefix V)

**Searched:** u.ae visa pages (tourist, transit, medical, jobseeker, explore investment, visa on arrival, track visa, fees and fines, fraud tips); ICP service cards (Issuance of a Visa, job exploration 60/90, business exploration 90, 5-year tourist and family, 14-day visa, extension, cancellation, refund, FAQ, Sept 2025 news); GDRFA service cards (visit visa list, tourist single/multiple, relative/friend, job seeker, business, medical, study, 5-year, GCC residents, June 2026 scam news); MOFA (visa on arrival June 2026; UAE Embassy Dhaka page, whose visa page returns 404); Emirates, Air Arabia, Dubai Airports; Decree-Law 29/2021 and Cabinet Resolution 65/2022; MOHRE mission permit; Bangla and English news (Daily Star, TBS, Dhaka Tribune, Bonik Barta, Jugantor, Samakal, Prothom Alo, Shomoyer Alo, Gulf News, Dhaka Post, KPMG); Bangladesh Embassy Abu Dhabi press release 22 Sep 2025 (read from page image).

**Status: what the sources say, by date.**
- 19-20 July 2024 protests, 57 jailed 22 July 2024 (Prothom Alo 24 Jul 2024, logged by others). Foreign Minister then said the UAE had not stopped visas (news-prothomalo-uae-no-visa-ban, not used).
- Start of the stop: July 2024 (Daily Star 30 Mar 2026, V0001; Bonik Barta, N0071), "after 5 August 2024" (TBS), "since September 2024" (Dhaka Tribune 20 Sep 2025, V0014). Conflict logged; the doc says July 2024.
- 4 May 2025: UAE ambassador said 30-50 visit visas a day from the Dhaka embassy, skilled-employment online system reopened, 500 security-guard visas issued (V0015-V0017). 2025 total: ministry official says none issued (V0002). Conflict logged both ways; doc states both.
- Sept 2025: fake "ban from January 2026" claim from uaevisaonline.com; denied by Bangladesh Embassy (V0205-V0206) and ambassador Tareq Ahmed (TBS, Dhaka Tribune). The Facebook copies still circulating ("UAE announced suspension from January 2026") come from this.
- Oct 2025: ATAB/TOAB say tourist and transit visas almost zero (V0003-V0004).
- Jan 2026: only skill and high-profile visas (Dhaka Tribune, V0011).
- 30 Mar 2026: no visit/work visas in 2025 (Daily Star, V0002).
- No official UAE notice reopening or closing Bangladeshi visit visas found in 2026; no UAE official source at all states a Bangladesh restriction. Family-sponsored visits: no source shows exemptions for families, transit or golden-visa relatives. A Reddit post (blocked) snippet: a resident told by GDRFA that no new entry permits for his Bangladeshi parents had been accepted for two years; not logged (not saved).
- Visa on arrival / US-UK-EU holders: Bangladesh not on any list (V0019-V0021). The June 2026 MOFA expansion added six countries, not Bangladesh.
- 5-year tourist visa: officially "all nationalities" (V0090); Shomoyer Alo (16 Jul 2026) says Bangladeshis are eligible (V0104). No evidence of approvals in practice.

**Conflicts (official vs official):**
- Relative/friend visit total stay: ICP Issuance card 120 days (V0034) vs ICP Extension card 180 days (V0054); KPMG/Gulf News July 2026 says 120 days a year (V0211). Doc shows one Need to know.
- 5-year visa: ICP card says both "90 days + extension, max 180 days a year" (V0095) and "must not exceed 90 days within a single year" (V0106); u.ae, GDRFA and the Executive Regulation say 180. Need to know.
- Emirates' resident-sponsor salary table (AED 4,000 parents/wife/children; 5,500 siblings; 7,000 in-laws; 10,000 friends) differs from ICP's Sept 2025 thresholds (4,000/8,000/15,000). Not logged as a fact (table text); doc uses ICP.
- GDRFA single relative/friend page lists only single-entry fees; KPMG (July 2026) adds multiple-entry AED 300/500/700. Both in doc.

**Page dates.** ICP service cards carry WordPress meta 2024-12-11 (site template) but content includes the Sept 2025 rules, so they are logged possibly-outdated with a note. GDRFA service pages show only a site-wide "last updated" date. sources.csv page_date for uaelegislation-residence-law-29-2021 is 2021-09-27 but the law text says 16 Sep 2021 (facts use 2021-09-16); for uaelegislation-residence-exec-regulation-2022 I entered 2022-05-01 as a placeholder: the true date was not found in the text copy; facts use "undated". Please correct both in sources.csv. Emirates and Air Arabia registered as official=yes (airlines are the visa sponsors for their own service); lead may change to news if preferred.

**Concurrency:** uae-portal-explore-investment-visa registration was lost once (another agent wrote sources.csv at the same time); re-registered. Other agents may want to re-check their registrations.

**What happens in practice:** visit visas were the main irregular work route for Bangladeshis (go on a 3-month visit visa, find work, convert) [V0202, V0013]; agencies sold Tk 1.2-1.5 lakh packages including an "airport contract" to pass Bangladeshi immigration [V0199, V0200] (Dhaka Post, 2021; no newer source found). This route is what the UAE closed.

**Logged but not used:** V0047 (ICP call centre, duplicate of V0190), V0052 (FAQ ranges), V0059 and V0061 (pre-arrival extension fee; 60-day visa non-extendable: only relevant to nationalities not open to Bangladeshis), V0081-V0082 (Emirates AED 1,000 deposit for sponsors without proof), V0105, V0123, V0132, V0163, V0164 partly (Executive Regulation duplicates of service cards), V0196-V0197 (UAE Embassy Dhaka address and phone: House 191, Road 69, Gulshan North Avenue, Gulshan-2; +8802222284295; dhakaemb@mofa.gov.ae; 9 am-4 pm, closed Fri-Sat: for Contacts), V0178 (company fine AED 50,000), V0207 (UAE among frequent refusers: Background), V0007 used in Visas not open.

## Residence, family, study, asylum (prefix F)

**Searched:** u.ae residence pages (family, student, retired, virtual work, green, golden, having a baby); ICP service cards (Issuing Residency Permit, Issuance of Visa); GDRFA service pages (family entry permit, family residence, retired, virtual, green x3, humanitarian); uaelegislation (Law 29/2021, Exec Reg Cabinet Res. 65/2022 with golden annex, Births and Deaths Law 10/2022, Penal Code 31/2021) via Wayback; MOHRE work-permit service pages via Wayback; UAE MOFA attestation; VFS Bangladesh; Bangladesh MoFA charter; Dubai Consulate and Abu Dhabi Embassy birth registration and e-passport; universities (MDX, AUD, CUD); CAA list; UNHCR RIMAP; US State Dept HRR; Bangla and English news on status (Jugantor, Dhaka Tribune, NTV, itvbd, Desh Rupantor), WAM denial, Fragomen.

**Conflicts:**
- Newborn deadline: u.ae says 120 days and AED 100/day (F0124); Exec Reg Art. 6 says 4 months (F0125); guides quote AED 50/day. Kept u.ae (newest, 4 Nov 2026).
- Exec Reg Art. 52 says retiree income AED 240,000 (F0114 Dubai), u.ae says AED 180,000 federal / AED 240,000 Dubai; ICP card says AED 240,000. Kept u.ae split; worth an insider check.
- Green investor share: GDRFA and ICP both AED 1 million (F0090, F0091); older guides cite less.
- GDRFA family residence page's "Terms and Conditions" text is wrongly copied from the entrepreneur service (Dubai Future Foundation nomination); not used.
- Tenancy contract for spouse/children in Dubai: official pages silent (ICP asks a utility bill; GDRFA asks attested tenancy only for humanitarian/parents); guides conflict (some say Ejari no longer required). Left as Need to know.
- Exec Reg PDF is the 2022 text; the legislation page lists 6 amendments (last update 3 Jun 2026). Golden-visa thresholds may have been amended.

**Practice:** Minister Ariful Haque Chowdhury (18 Aug 2026) is the most authoritative dated statement of the family/student/employment/transfer stall (F0030). A LinkedIn post by Legal Talks with Aminul (Dubai consultant) says partner-visa and transfer routes for Bangladeshis are "temporarily restricted" (blocked, not logged). Bangla Facebook/TikTok agents widely sell "partner visas" and "Sharjah partner visa" packages (Satwa Road shops) — no price evidence saved.

**Facts logged but not used:** F0121 used; F0016 also covers female sponsors; F0042 widow route used briefly. All others used.

**Scratchpad incident:** I accidentally overwrote another agent's `addfacts.py` in the shared scratchpad with my driver (my own copy is `F-addfacts.py`). Whoever used `addfacts.py` with `facts1-5.json` should check it.

**Dates:** ICP service cards dated 2024-12-11 from page meta (template date; content is live) -> possibly-outdated. GDRFA pages undated -> possibly-outdated, following other agents.

## Money home, going home, contacts (prefix G)

**Searched:** bb.org.bd (exchange rate, remittance pages: captcha on curl, Firecrawl worked; PDFs fetch directly), centralbank.ae (rates, licensing register), icp.gov.ae (service pages, media centre), gdrfad.gov.ae, dubaipolice.gov.ae (JS: Firecrawl), u.ae (several moved pages 404), bcgdubai.gov.bd (the Dubai Consulate's real site; dubai.mofa.gov.bd is not used), abudhabi.mofa.gov.bd, wewb.gov.bd, mygov.bd, nationalsavings.gov.bd, NBR SRO 261 baggage rules, budget speech FY2026-27, Bangla news (Prothom Alo, Dhaka Times), Daily Star, TBS, Arab News.

**Method notes:**
- 54 Bangladesh-side facts (G0005-G0059) were re-logged from Malaysia's facts (WEWB, myGov, ministry charter, BMET leaflet, NBR baggage, HSIA customs) after re-fetching each page into the UAE folder; each note says "(re-logged from Malaysia Bxxxx)". The WEWB insurance image was re-fetched and the Malaysia hand transcription checked against the image.
- Bangladesh Bank PDFs: pdftotext -layout misaligns tables (UAE row picks up Malaysia's numbers). I added `.raw.txt` copies (pdftotext -raw) for bb-remittance-top30-countries, bb-remittance-monthly-report-2026-08 and bb-remittance-cost; quotes come from them. Remittance cost table checked visually.
- Firecrawl-saved files (excerpts, noted at foot of each): bb-exchange-rate-usd-2026-11-08, cbuae-exchange-rates-2026-11-06, dubaipolice-circulars-travel-bans-fc, dubaipolice-report-lost-item, cbuae-licensing-exchange-houses (from Firecrawl search result text; curl copy lacks the JS table), bkash-remittance-mts (UAE row only).
- ICP service pages show a site stamp "Last updated on 08/11/2026" (template meta 2024-12-11); content contains the 2025 grace-period tiers, so logged as verified 2026-11-08 with a note.
- The failed curl copy `bb-exchange-rate-2026-11-08` (captcha page) is in the fetch log; not used.
- Cited other agents' facts N0033, N0035 (WAM sentencing/pardon 2024) in "If you are detained". Agent V logged the official uaelegislation text of Decree-Law 29/2021 (V0173-V0177); I logged the GDRFA English translation (G0105-G0110). The lead may prefer V's ids.

**Conflicts:**
- Treatment aid: WEWB Tk 2 lakh (G0014, G0016) vs Dubai Consulate page Tk 1 lakh (G0131). Keep WEWB.
- Tk 3 lakh grant eligibility: WEWB "clearance or membership" (G0005) vs Consulate "workers who went legally" (G0131).
- Insurance start date: WEWB 1 January 2023 (G0018) vs BMET leaflet 12 March 2023 (G0042) (carried from Malaysia).
- 2024 amnesty dates: official 1 Sept-31 Oct 2024, extended to 31 Dec (G0092, G0093, G0138); Prothom Alo quotes the foreign ministry as "1 July-31 Dec" (G0096).
- Travel-permit Friday submission "9 am-11 pm" on the Consulate page (typo; service hours end 11:30 am) (G0111, G0080).
- WEWB membership fee: Tk 6,500 equivalent (G0133) = AED 200 at the Consulate (G0130); consistent at AED1 = Tk 34. Agent B has the Embassy's Sept 2026 fee notice (bdemb-abudhabi-wewb-fee-notice-2026-09: AED 200).

**Practice:**
- Dubai Consulate monthly numbers (June 2026: 861 travel permits, 35 bodies; Jan-Jun 2026: 2,915 travel permits, 213 bodies, 5,028 welfare cards) show the scale (G0082).
- 2024 amnesty: about 50,000 Bangladeshis regularised; 5,500+ left on travel permits with no ban; Dubai Consulate issued 4,840 travel permits, the Embassy 817 (G0094). UAE announced arrests and AED 50/day fines after it ended (G0095).
- 2026 regional war: Iranian strikes from 28 Feb 2026 closed airspace; ICP waived overstay fines (G0070, G0071, G0072); a Bangladeshi delivery driver was killed in the UAE (G0135).
- Remittance cost from the UAE is the highest of the main corridors (G0100).
- The budget (G0102) promises "Bangladesh Support Centres" at embassies for imprisoned and deceived workers and says reopening of the UAE labour market has begun: useful for Background.

**Logged but not used:** G0003 (CBUAE buy/sell peg band, redundant with G0002); G0042 (only in a Need to know); G0026's 20-day total; G0092 detail on the 2024 Amer AED 24 fee and 14-day exit permit (historic); G0093; G0102 (for Background); G0120 note on Al Ansari Digital Pay; G0123/G0124 partly. bb-invest-nrb.pdf fetched but text is garbled legacy font and outdated (bond rate from 2000): not logged. GDRFA "lifting the ban on a file" pages (gdrfad-ban-services, gdrfad-lift-ban-individuals) concern establishment/sponsor file blocks, not worker entry bans: not logged.


# Pages we could not download

Received from the user on 8 Nov 2026 and logged (method manual): mohre-new-work-permit-overseas-live (confirms the work-permit fees, M0003), mohre-resolution-340-2026-wps (turned out to be a Polaris Legal Library summary of u.ae, not MOHRE's own PDF; it showed the doc's late-wage list missed day 11 and the day-21 rule for firms of 50+, now fixed from u.ae, M0001-M0002), mohre-know-your-rights-bengali, iloe-flyer-bengali (registered; not cited). MOHRE's own Resolution 340 PDF is still wanted.

Second batch received from the user on 8 Nov 2026 (all logged, method manual; integrated by agents MA, MB, MC; proposals in verify/m-*.md, checked in verify/m-check.md):
- probashi-migration-cost-16-countries-2017: actually the Bangladesh Annual Migration Report 2017 (Ministry and IOM, June 2019); Table 6 gives the official 2017 UAE cap, Tk 1,07,780 (now official, replaces news N0138).
- bbs-ilo-cost-of-migration-survey-2020: scanned; OCR copy saved as .ocr.txt; no UAE-only figures (UAE inside "Other countries").
- wam-icp-grace-period-2026-06 (replaces EY lead G0072), adjd-estafser.png, news-kalerkantho-uae-embassy-visa-cancel-2026-07 (no Embassy email given).
- mohre-admin-resolution-5-2024-recruitment-manual, mohre-service-new-work-permit-domestic, wam-uae-bangladesh-domestic-mou-2018, dip-epassport-fees.
- mohre-inquiry-job-offer-form.png, icp-file-validity-form.png (transcribed), ehs-medical-fitness-live (fee corrected: AED 250, not 260), flydubai-ok-to-board (Bangladesh not on its OK-to-Board list).
Still wanted: gdrfa-relative-friend-visit-visa-2025 (the saved page holds only the title; save it after the page fully loads, or a screenshot of the conditions and fees); MOHRE's own Resolution 340 PDF; the Embassy's Facebook notice of 1 Aug 2026; ICP File Validity result screen and the visa/passport search fields; Abu Dhabi Embassy travel-permit fee.

Each line: the URL, the file name to save it as in `sources/`, and why it matters.

## Corridor, costs and scams (prefix N)

- ILO/BBS Cost of Migration Survey 2020: https://www.ilo.org/sites/default/files/wcmsp5/groups/public/@asia/@ro-bangkok/@ilo-dhaka/documents/publication/wcms_766198.pdf -> sources/bbs-ilo-cost-of-migration-survey-2020.pdf (UAE-specific cost and income).
- Kaler Kantho embassy statement 28 Jul 2026: https://www.kalerkantho.com/online/national/2026/07/28/1717449 -> sources/news-kalerkantho-uae-embassy-visa-cancel-2026-07.html
- Facebook: Bangladesh Embassy Abu Dhabi notice of 1 Aug 2026 (cases by email), and any later notice on reinstatements.

## Work visa (UAE side) and free zones (prefix W)

- https://www.mohre.gov.ae/en/services/recruiting-a-worker-from-overseas-2022 (curl and Firecrawl time out; Wayback copy of Jan 2026 used) -> sources/mohre-new-work-permit-overseas-live.html: confirms current fees.
- https://inquiry.mohre.gov.ae/ (English view, and the "Job offer inquiry" form) -> sources/mohre-inquiry-job-offer-form.html (screenshot): exact fields to type.
- https://smartservices.icp.gov.ae/echannels/web/client/default.html (Public services > File validity form) -> sources/icp-file-validity-form.png (screenshot): fields and result.
- https://www.ehs.gov.ae/EN/services/services-directory/examination-of-medical-fitness-for-residency-visa (live) -> sources/ehs-medical-fitness-live.html: current fee (Wayback Jan 2026 used).
- https://gulfnews.com/uae/government/now-emirates-id-replaces-residence-visa-sticker-in-passport-of-uae-residents-except-in-dubai-1.87920236 -> sources/news-gulfnews-emirates-id-replaces-sticker-2022.html: sticker question.
- https://www.doh.gov.ae (visa screening fees, Abu Dhabi) -> sources/doh-visa-screening.html.
- Facebook screenshots wanted: MOHRE UAE (facebook.com/MOHREUAE) posts on overseas work permit steps 2026; Bangladesh Embassy Abu Dhabi labour wing posts on demand attestation and on UAE work visas for Bangladeshis 2026; Bangladesh Consulate Dubai posts on "visa open/closed" notices.

## Bangladesh-side steps (prefix B)

- Ministry office order (2017) fixing migration costs for 16 countries (UAE Tk 1,07,780): not on probashi.gov.bd office-orders; suggest `sources/probashi-migration-cost-16-countries-2017.pdf`; needed to cite the cap officially.
- https://www.jagonews24.com/national/news/404005 (2017 cost order report) failed (000); `sources/news-jagonews-migration-cost-16-countries-2017.html`.
- Facebook: Bangladesh Embassy Abu Dhabi (facebook.com/BangladeshEmbassyAbuDhabi) and Consulate Dubai posts on demand/visa attestation fees and 2026 visa notices; screenshots would help.
- UAE Embassy Dhaka attestation fee page (mofa.gov.ae missions/dhaka services, attestation tab, shows no fee); suggest a browser screenshot `sources/uae-embassy-dhaka-attestation-fees.png`.

## Rights at work and problems (prefix L)

- https://www.mohre.gov.ae/assets/download/9e530b2e/Ministerial%20Resolution%20No.%200340%20of%202026.pdf.aspx -> `sources/mohre-resolution-340-2026-wps.pdf`: the 2026 WPS resolution (curl times out; u.ae summary used).
- https://www.mohre.gov.ae/assets/download/b578cbaa/e3ref7qooqek-bingali.aspx -> `sources/mohre-know-your-rights-bengali.pdf`: MOHRE's Bengali rights guide.
- https://www.iloe.ae/pdf/ILOE-Flyer-Bengali.pdf -> `sources/iloe-flyer-bengali.pdf`: ILOE in Bangla.
- https://www.wam.ae/en/article/bk01z89-mohre-implement-midday-break-for-21st-consecutive -> `sources/wam-midday-break-2025.html`: newer midday fine confirmation.
- https://mohre.gov.ae/assets/download/960ffdc1/Ministerial%20Resolution%20No.%20657%20of%202022%20on%20Rules%20and%20Guidelines%20to%20Deal%20with%20Work%20Injuries%20and%20Occupational%20Diseases_638945724651791715.pdf.aspx -> `sources/mohre-resolution-657-2022-work-injuries.pdf`: injury claim procedure.
- https://u.ae/-/media/Mohre-resolutions/Ministerial-Resolution-No318-of-2022-Concerning-Bank-Guarantees-and-Employees-Protection-Insurance-S.pdf (404) -> `sources/mohre-resolution-318-2022.pdf`: how workers claim the protection insurance.
- Facebook: Bangladesh Embassy Abu Dhabi and Consulate Dubai posts (July-Oct 2026) on visa-cancellation email submissions and any reinstatements; MOHRE UAE post on the community reporting service.

## Domestic workers (prefix D)

- MOHRE whole site unreachable (connection refused). Please download in a browser:
  - https://mohre.gov.ae/assets/download/594f4504/Administrative%20Resolution%20No.%205%20of%202024.pdf.aspx -> sources/mohre-admin-resolution-5-2024-recruitment-manual.pdf (operation manual: refunds, replacements, warranty, office duties to workers)
  - https://www.mohre.gov.ae/en/services/approved-services-centers/domestic-workers-services-centers -> sources/mohre-domestic-service-centres.html (list of licensed offices)
  - https://mohre.gov.ae/en/media-center/news/27/7/2026/mohre-issues-135-fines-against-42-domestic-worker-recruitment-offices-during-the-first-half-of-2026 -> sources/mohre-news-135-fines-2026-07.html (official version of D0135-D0137)
  - https://www.mohre.gov.ae/en/media-center/news/25/2/2026/mohre-12-unlicensed-domestic-worker-recruitment-offices-closed-and-referred-to-public-prosecution -> sources/mohre-news-12-unlicensed-offices-2026-02.html
  - https://www.mohre.gov.ae/en/services/issuance-of-a-new-work-permit-domestic-workers-2022 -> sources/mohre-service-new-work-permit-domestic.html (fees, conditions)
  - https://www.mohre.gov.ae/en/faq.aspx -> sources/mohre-faq.html (domestic worker FAQs)
- https://www.wam.ae/en/article/hszr6wlg-uae-bangladesh-sign-mou-domestic-workers -> sources/wam-uae-bangladesh-domestic-mou-2018.html (official WAM text of the 2018 MoU; JS-only)
- https://www.tamm.abudhabi/en/articles/ewaa-shelter-for-women-and-children -> sources/tamm-ewaa-shelter.html (Ewa'a contact numbers; JS-only)
- Facebook screenshots that would help: Bangladesh Embassy Abu Dhabi (facebook.com/BangladeshEmbassyAbuDhabi) and Consulate Dubai posts on housemaid visa attestation requirements and minimum salary; MOHRE UAE post on "domestic worker terminated after probation responsible for return expenses" (facebook.com/MOHREUAE/posts/689126813248976).

## Visit and short visas (prefix V)

- https://www.reddit.com/r/visas/comments/1vsfeq6/has_any_bangladeshi_passport_holder_received_a/ → `sources/forum-reddit-bd-uae-new-visa.html`: worker reports (2026) that GDRFA accepts no new entry permits for Bangladeshi parents; only practice evidence on family visits found.
- https://www.gdrfad.gov.ae/en/services/a01f0970-ba1a-11f0-5210-4cd98f768936 → `sources/gdrfa-relative-friend-visit-visa-2025.html`: GDRFA's new (post-Sept 2025) relative/friend visit card; the saved copy is empty (JS). Would replace KPMG for the Dubai salary thresholds and multiple-entry fees.
- https://www.mofa.gov.ae/en/missions/dhaka/services/Visas → `sources/mofa-uae-embassy-dhaka-visas.html`: returns 404 to scripts; the Dhaka embassy's own visa page.
- https://www.flydubai.com/en/flying-with-us/ok-to-board/ and https://www.flydubai.com/en/flying-with-us/visas-and-passports/dubai-visas → `sources/flydubai-ok-to-board.html`, `sources/flydubai-dubai-visas.html`: flydubai OK-to-board rules for Bangladesh and its visa fees.
- https://www.etihad.com/en-ae/fly-etihad/visas → `sources/etihad-visas.html`: Etihad transit/tourist visa terms.
- https://www.thenationalnews.com/news/uae/2026/08/25/dubai-police-fake-visa-job-offer-warning/ → `sources/news-thenational-dubai-police-visa-scam-2026-08.html`: Dubai Police warning on visa/job scams, 25 Aug 2026.
- Biman Bangladesh Airlines and US-Bangla: any page on OK to Board for UAE (not found online).
- ICP smart services service screens (smartservices.icp.gov.ae, service cards 783, 784, 939, 941, 942, 944-946) are JS-only: a screenshot of the "Issue search for job visa 120 days" card would confirm the 120-day ICP fee and terms.
- Facebook screenshots that would help: UAE Embassy Dhaka page (facebook.com/p/UAE-Embassy-Dhaka-100070103688784) posts on visit visas 2025-2026; Bangladesh Consulate General Dubai and Embassy Abu Dhabi posts on visit visas or family visas for Bangladeshis in 2026.

## Residence, family, study, asylum (prefix F)

- https://www.mohre.gov.ae/en/services/work-permits-for-dependents-sponsored-by-family-members-2022 -> `sources/mohre-work-permit-family-sponsored.html` (live; I used a March 2026 Wayback copy).
- MOHRE freelance permit service page (URL not found; search "Freelance permit" on mohre.gov.ae services directory) -> `sources/mohre-freelance-permit.html`: fee and conditions.
- https://www.epassport.gov.bd/instructions/passport-fees -> `sources/dip-epassport-fees.html` (403): current mission fees for child passports.
- https://bcgdubai.gov.bd/wp-content/uploads/2024/09/Passport-Fee-English.jpg -> `sources/bcgdubai-passport-fee-english.jpg`: Dubai Consulate passport fee table (image).
- https://www.linkedin.com/posts/legaltalkswithaminul_uaevisa-bangladeshtouae-rakez-activity-7453327735722127360-1sU5 -> `sources/guide-legaltalks-rakez-partner-visa-bd.html`: practitioner says partner/transfer routes restricted for Bangladeshis.
- https://www.state.gov/reports/2024-country-reports-on-human-rights-practices/united-arab-emirates/ (403) -> `sources/usstate-hrr-uae-2024.html`: newer asylum text.
- https://www.unhcr.org/us/where-we-work/countries/united-arab-emirates (403) -> `sources/unhcr-uae-country.html`: UNHCR Abu Dhabi contact.
- https://smartservices.icp.gov.ae (golden/green "About" and eligibility pages, JS-only) -> screenshot of category conditions.
- Facebook screenshots that would help: Bangladesh Embassy Abu Dhabi and Dubai Consulate posts on family/student visa status for Bangladeshis (2025-2026); Ministry of Expatriates' Welfare press release of 18 Aug 2026 meeting with the CIP Business Association.

## Money home, going home, contacts (prefix G)

- https://www.wam.ae/en/article/c0scyu2-icp-grants-individuals-affected-exceptional -> `sources/wam-icp-grace-period-2026-06.html`: official text of the June-July 2026 overstay grace period (currently only EY, G0072). The curl copy saved under that name is an empty JS shell.
- https://u.ae/en/information-and-services/passports-and-traveling/preliminary-checks/check-if-you-have-a-travel-ban -> `sources/uae-portal-check-travel-ban.html`: official travel-ban checking guide (404 to scripts; the page may have moved: search u.ae for "travel ban").
- https://www.adjd.gov.ae/sites/eServices/EN/Pages/Estafser.aspx -> `sources/adjd-estafser.html`: Abu Dhabi Judicial Department's Estafser travel-ban/case inquiry (JS-only; curl copy empty). Needed to cite the Abu Dhabi check in Step 2.
- https://gulfnews.com/uae/thousands-use-estafser-to-check-uae-travel-bans-and-legal-cases-in-minutes-1.500130833 -> `sources/news-gulfnews-estafser-travel-ban-2025-05.html` (fetch failed).
- https://en.prothomalo.com/bangladesh/ms35nsib27 -> `sources/news-prothomalo-bodies-return-2026-10.html` (fetch failed; bodies repatriation practice).
- Abu Dhabi Embassy "MRP Against Lost Passport" and travel-permit fee pages: menu items with no working static link found; a screenshot of the Embassy's out-pass fee and documents would close the Step 1 gap.

**Facebook screenshots that would help:** Consulate General Dubai (facebook.com/cgbduae) and Embassy Abu Dhabi (facebook.com/BangladeshEmbassyAbuDhabi) posts on: current travel-permit fees and processing; any 2026 amnesty or fine-waiver announcement; deportation-centre visits; e-passport fee table.

# Verification

- Round 1 (8 Nov 2026): 9 independent line verifiers (every sentence and number against the saved source) and 1 coverage/audit agent; 131 line problems and 47 coverage items; reports in verify/r1-*.md. All line fixes applied; 45 of 47 coverage items applied (skipped: Penal Code Art. 212 on a news-only fact, N0105; humanitarian residence needs a logged fact).
- Round 2: 3 verifiers re-checked every changed line (163 lines); 26 problems, all fixed (verify/r2-*.md).
- Round 3: 1 verifier re-checked the 27 lines changed in round 2; 5 problems, all fixed and self-checked against the saved sources (verify/r3-r3.md).
- Fact rows corrected during verification: V0205, V0206, N0049, N0050 (placeholder quotes; OCR text copy of the Embassy press release added); D0212-D0216 and source mewoe-women-dw-zero-cost-agencies dated 1 Sep 2024 (not 2025); N0031, N0032 dated 27 Jul 2026.
- Not re-checkable by tool (garbled Bangla PDF text, accepted on the researchers' page transcriptions): D0198-D0202, D0212-D0216, D0219-D0222, B0103, G0092 and other --no-quote-check rows.

# Procedure (SOP) pass, 8 Nov 2026 evening

Three agents (SA, SB, SC; proposals in verify/s-S*.md) turned the weak sections into step-by-step procedures in the Malaysia pattern: company-worker Steps 4 and 6, change employer, scams, detained; tourist, job-seeker, family visit, business and medical visits; student, Green, Golden, other residence visas, changing visa type, domestic Step 5 and scams. Three independent checkers verified all 178 changed lines (verify/s-check-*.md): 15 problems, all fixed (two leaked editing instructions repaired by hand). Open: which BMET officer handles written agency complaints (Director (Emigration) 01711-135901 [B0020] vs Director (Employment) 01711111544 [D0222], charter PDF garbled).

- 8 Nov 2026: found the official Embassy notice of 31 July 2026 (attached to the Ministry notice of 1 Sep 2026 on probashi.gov.bd): email mission.abudhabi@mofa.gov.bd, 12 details, subject line, urgent numbers (MD0001-MD0006). Closes the FAQ-test gap on cancelled visas (email and details); reinstatement process still unknown.


# Research notes by topic (from the original research parts)


# Agent B findings: Bangladesh-side steps for UAE-bound workers

Facts B0001-B0113 are in facts.csv (91 official, 7 news/guide; the rest official image/PDF transcriptions). All sources saved in sources/ and registered.

## a. Draft doc text

### Step 1: Find a real job

1. **Register on the Overseas Employment Platform (OEP),** BMET's (Bureau of Manpower, Employment and Training) website for job-seekers. A UAE permission letter requires the agency to choose workers from BMET's database, and BMET clears no worker outside it [B0009].

   You'll need [B0052, B0053]:

   - your NID (national ID card);
   - a phone that can receive codes;
   - Tk 200 for the government fee.

   1. Open [employee.oep.gov.bd/employee/registration](https://employee.oep.gov.bd/employee/registration) [B0053].
   2. Type your name in English, mobile and NID numbers, date of birth, division and district exactly as on the NID, the captcha, tick the terms and press "যাচাই করুন" (Verify) [B0052].
   3. Print 2 copies of the registration slip and give your fingerprints at the district office (DEMO, District Employment and Manpower Office) [B0053]. DEMO addresses are listed on BMET's website [B0054].

   **If it fails:** call the OEP hotline, 09614445271 [B0062].

2. **Learn a trade if you need one.** BMET lists every TTC (Technical Training Centre) and IMT with contacts on its website [B0055].

   **Women going as domestic workers** must do housekeeping training at one of 41 TTCs before going [B0021]. BMET's curriculum for women going to Gulf countries takes women aged 25 to 40 at admission, with at least class 5, able to read and write a sentence in Bangla and English, at least 4 ft 10 in tall and 40-65 kg, and runs for 2 months; women who are pregnant or whose youngest child is under 5 are not admitted [B0103]. For clearance as a domestic worker a woman must prove she is 25 to 45 and bring a no-objection letter from her legal guardian [B0016].

   > **Need to know**
   > - Is the UAE open to new Bangladeshi women domestic workers in 2026, given 764 women were cleared for the UAE from January to 7 November 2026 [B0113]?
   > - Does the UAE require any skill test or certificate from Bangladeshi workers before the visa, as Saudi Arabia does?

3. **Through a recruiting agency: find and check the permission letter.** For a UAE job order BMET issues a permission letter naming the agency, the employer, the Consulate's attestation number, each job and its pay, the conditions and the most the agency may take [B0003, B0004, B0005, B0007]. Example (Navira Ltd, RL-0712, 21 August 2025): Transguard Group LLC, Dubai; 470 men as masons (AED 1,150 a month), shutter carpenters and steel fixers (AED 1,050), electricians (AED 1,400), loaders and warehouse workers (AED 1,080), helpers and cleaners (AED 800); 2-year contract, 9 hours a day, 6 days a week; the company pays housing, transport, return air tickets and the visa, gives a food allowance and takes no recruitment fee; the agency may take at most Tk 71,840 [B0003, B0004, B0005, B0007].

   You'll need: the agency's RL number and the employer's name [B0001].

   1. Open [bmet.gov.bd/pages/miscellaneous-infos](https://bmet.gov.bd/pages/miscellaneous-infos) and search "আমিরাত", "Dubai" and your agency's RL number [B0001, B0002].
   2. Open the PDF and compare the employer, job, pay and maximum fee with what you were told [B0004, B0007].
   3. Check the Consulate attestation number on the letter (it starts "BCG/DUBAI(LWW)") matches your demand letter [B0003, B0014].

   As of 8 November 2026 BMET's list shows only two UAE letters, from August 2023 and August 2025 [B0001, B0002].

   > **Need to know**
   > - Where does BMET publish permission letters for the 23,044 workers cleared for the UAE in 2026 [B0110]?
   > - Do individual (single) UAE visas get a permission letter at all?

4. **Have the demand letter and visa checked.** BMET checks job visas and demand letters free within 3 working days and checks UAE visas online; bring the visa and, if stamped, a copy of the passport page [B0019]. Do this at your DEMO or BMET, 89/2 Kakrail, Dhaka [B0085, B0097]. A UAE demand letter is valid only once the Consulate General in Dubai or the Embassy in Abu Dhabi has attested it [B0027, B0032]. To attest it, the employer gives the Consulate a demand letter attested by the UAE Chamber of Commerce, a power of attorney to the Bangladeshi agency, the recruitment contract, a guarantee letter to the Ministry's Secretary, a specimen work agreement, both companies' licences and the UAE company's quota [B0028, B0029, B0030].

   > **Need to know**
   > - Can a worker ask the Consulate or Embassy labour wing to confirm an attestation number, and how?

5. **Through a relative in the UAE (individual visa).** The Consulate's labour wing attests individual employment, residence and housemaid visas [B0026, B0032]. A worker with a visa they got themselves applies for clearance at BMET's emigration branch in Dhaka or the Chattogram DEMO (Step 6) [B0018]. Source tax on a single visa is Tk 250 if the visa is attested and Tk 400 if not [B0017].

   > **Need to know**
   > - What does the Consulate or Embassy charge to attest an individual employment visa, and what does the sponsor bring?

**Before paying:**

- **Know the cap.** The Ministry fixed the UAE maximum at Tk 1,07,780 in 2017 [B0100]; the 2025 Navira letter set Tk 71,840 [B0007]. The worker pays nothing for the UAE side: the employer bears the levy and airfare [B0008].
- **Pay late, by bank.** The agency may take its money only once the visa, BMET clearance and flight are confirmed, by cheque, bank draft or pay order [B0007]; pay into the agency's bank account and keep receipts [B0084].
- **Get the contract and Bangla translation before clearance** [B0010].
- **Don't go on a visit visa to work:** the Ministry warns that brokers send people to the Middle East on tourist or visit visas with false job promises [B0088].
- **Borrow from PKB** (Probashi Kallyan Bank, the government bank for migrants) once you have a visa: up to Tk 3 lakh at 9% simple interest, repaid monthly over up to 3 years, decided within 7 working days [B0045].

  You'll need [B0043, B0044]:
  - the free bank form, 3 photos, NID copy;
  - passport, visa and BMET card copies;
  - 3 signed MICR cheque leaves from your own account with a statement;
  - a PKB savings account opened with at least Tk 500;
  - two guarantors: one financially solvent person with cheques, statement and proof of income, and one family member.

  You and the guarantors must live in the branch's area and you must be 18 to 60 [B0042]. Fees: 0.5% processing and 0.5% documentation, plus VAT, and Tk 900 per lakh risk cover [B0045]. Women can take PKB's women's migration loan, which needs one guarantor and no processing fee [B0047]. Apply at the branch or on mygov.bd, which sends application and tracking numbers by SMS [B0048]. Helpline 16238, or +880 9677-787878 from abroad [B0046].

**If an agency or broker takes your money:** taking money on a false job promise or holding a migrant's passport is a crime punishable by up to 5 years' jail and a fine of at least Tk 1 lakh [B0098]. Complain to BMET or the Ministry as in the Malaysia procedure; the Consulate in Dubai also forwards complaints to the District Commissioner in Bangladesh on its complaint form [B0041]. Free legal advice: 16699 [B0095].

### Step 4: Passport, police clearance and certificates

1. **E-passport.** Fill the form exactly as on your NID (compulsory over 20); nothing needs attesting; upload technical certificates such as a driving licence [B0068, B0069]. Pay through A-Challan, DGePay or ShurjoPay, or at a bank [B0066]. A 48-page passport costs Tk 4,025 / 6,325 / 8,625 for 5 years and Tk 5,750 / 8,050 / 10,350 for 10 years (regular / express / super express) [B0064], delivered within 15, 7 or 2 working days of enrolment [B0065]. No police verification is needed with an online-verified NID [B0071]. Helpline 16445 (09666716445 from abroad) [B0072]. If lost, file a GD and re-apply with the old passport copy [B0070].
2. **Police clearance only if the employer asks.** Apply at [pcc.police.gov.bd](https://pcc.police.gov.bd/) with a passport valid 3 months and an address that is in the passport [B0073]; pay Tk 1,500 by treasury challan, code 1-7301-0001-2681, or online [B0074]; track by SMS "PCC S <reference>" to 26969 [B0075]. Helpdesk Sunday-Thursday 9-5, 01320001824, 01320001825 [B0076].

   > **Need to know**
   > - Which UAE jobs or emirates ask Bangladeshi workers for a police clearance?

3. **Certificates for a skilled UAE permit.** The chain is: issuing authority and Ministry of Education [B0081], then MoFA Bangladesh, then the UAE Embassy in Dhaka through UAE MOFA's "Attestation through UAE Missions Abroad" service [B0083].
   1. On mygov.bd, register, choose the attestation service for the document, upload it as JPEG/JPG/PNG and pay Tk 200 a page; it takes 5 working days and an SMS tells you when it is ready [B0077, B0078].
   2. The UAE does not accept Bangladesh's e-Apostille [B0079, B0082], so take the Apostille and documents to MoFA's consular counter, 10:00-13:00, for a consular sticker [B0079].
   3. Experience certificates must first be attested by BMET or the Ministry of Expatriates' Welfare and notarised; MoFA then attests them free [B0080].
   4. Apply to UAE MOFA online for the mission attestation; help +97180044444 [B0083].

   > **Need to know**
   > - What does the UAE Embassy in Dhaka charge per certificate, and how long does it take?

### Step 6: Orientation, BMET clearance and the flight

1. **Pre-departure orientation (PDO), 3 days,** compulsory, at one of 70 BMET institutes; pay against a money receipt (Tk 200 at Feni TTC) [B0021, B0056]. Download the certificate at training.oep.gov.bd/pdo-certificate with your passport or NID number [B0057].
2. **Check the contract** at least 2 days before you go: job, employer, workplace, length, pay, leave and airfare [B0058], against the permission letter (Step 1).
3. **BMET clearance (the smart card).** The agency applies with the demand letter, power of attorney, contract and skill certificates; BMET clears within 3 working days of the visa [B0011, B0015]. Your costs:
   - welfare fee Tk 5,500 to the Wage Earners' Welfare Board from 1 October 2026 [B0024];
   - insurance Tk 1,000 once (5 years, Tk 10 lakh cover) [B0086];
   - clearance fee Tk 250 [B0017];
   - source tax Tk 1,200 (skilled) or Tk 800 (unskilled) on a group visa [B0017].

   > **Need to know**
   > - Is the Tk 250 clearance fee still charged, given the Ministry reportedly abolished the smart card fee in December 2024 [B0099]?

   **Individual visa:** apply at BMET's emigration branch, Dhaka, or the Chattogram DEMO with your application, visa copy, any contract, attested OEP card copy, a Tk 300 stamp declaration and the pay order for the welfare fee and insurance [B0018]. Women on a single visa need a guardian's no-objection letter [B0059].

   **Check it is real** at portal.wewb.gov.bd/bmet-wewbm-check with your passport number [B0061]; the airport welfare desks check smart cards [B0022].
4. **The flight.** The employer pays the airfare, and an agency representative must fly with you or meet you at the UAE airport [B0008, B0013].
5. **Before you fly:** keep one set of copies at home and 3 with you, open 2 bank accounts, and never carry a packet you don't know [B0087]. Save the labour wing numbers (Contacts).

## Coming home (Bangladesh side)

- **Airport help.** Welfare desks at Dhaka, Chattogram and Sylhet help with customs and lost luggage, take complaints of abuse or fraud, give women who return within a year after abuse or fraud Tk 5,000, and send sick returnees to hospital by free ambulance [B0089, B0022, B0090]. Dhaka desk +8802 8901040, 01404 413388 [B0090].
- **A place to stay:** Wage Earners' Centre near Shahjalal airport, Tk 100 admission and Tk 200 a night (wec.wewb.gov.bd) [B0091]; Probashi Lounge with free wifi and phone [B0092].
- **Family threatened at home:** apply to the Welfare Board directly, through the DC office or DEMO, or on myGov [B0093, B0104].
- **Business loan:** PKB's rehabilitation loan, up to Tk 50 lakh (Tk 3 lakh without collateral), 9% over up to 10 years, at the branch for the project's area with a trade licence and return papers [B0049, B0050]; fees 0.5% processing (max Tk 15,000) and 0.5% documentation [B0051].
- **BRAC** gives returnees airport help, counselling, money or materials to restart earning, and legal help [B0094].

## Contacts

- **Embassy of Bangladesh, Abu Dhabi:** Villa 46, 48, Sector-19, Zone-W31, Al Jawwalah Street, Al Saadah, P.O. Box 2504; +971 2 446 5100; mission.abudhabi@mofa.gov.bd [B0034]. Labour wing: +971 2 445 8182 (direct), welfare officer ext. 209, labourwingauh@gmail.com [B0036]; Counsellor (Labour) counselorabudhabi@probashi.gov.bd, +971 2 446 2745 [B0037]. Hours: Monday-Thursday 9:00-15:00, Friday 8:30-11:00 [B0038]. Fees: power of attorney AED 38 (AED 75 urgent) [B0033].
- **Consulate General, Dubai:** Villa 36 & 145, 123/3 Street, Abu Hail Road, Al Wuheida, Deira; labour welfare WhatsApp (text only) +971 5081 68253, +971 5081 68363; +971 4 238 8199 [B0039]; First Secretary (Labour Welfare) labour.dubai@mofa.gov.bd [B0040].
- **BMET emigration:** Director (Emigration) +8802222222415, 01711-135901, diremi@bmet.gov.bd [B0020]; OEP hotline 09614445271 [B0062].
- **Probashi call centre (24 hours):** 16135 [B0063].
- **Ministry:** Probashi Kallyan Bhaban, 71-72 Old Elephant Road, Dhaka [B0096].
- **PKB:** 16238, +880 9677-787878 [B0046].
- **Airport desks:** Chattogram 01913631797, Sylhet 01558277904 [B0023].

## b. Notes

- **Clearances to the UAE (for agent N):** BMET image 2015-2025: 25,271; 8,131; 4,135; 3,235; 3,318; 1,082; 29,202; 101,775; 98,422; 47,166; 2,993 to May 2025 [B0105]. OEP report (live): 2023 98,201; 2024 47,158; 2025 13,750; 2026 to 7 Nov 23,044 [B0107-B0110]. 2026 by month: Jan 1,446 ... Sep 4,442, Oct 951, 1-7 Nov 63 (sharp October drop) [B0111]. Women: 2015-2025 [B0106]; 2025 721, 2026 764 [B0112, B0113]. Conflict: 2023 = 98,201 (OEP) vs 98,422 (BMET image).
- **Conflict (visa status):** Bonik Barta says the UAE stopped issuing visit and employment visas to Bangladeshis after July 2024 [B0102], yet OEP shows 13,750 clearances in 2025 and 23,044 in 2026. Likely individual/attested visas or re-entries; unresolved, for the lead.
- **Conflict (welfare fee):** BMET charter Tk 3,500 [B0017] vs Ministry circular Tk 5,500 from 1 Oct 2026 [B0024]; Embassy Abu Dhabi's AED 200 = Tk 6,500 incl. insurance [B0025] matches the new fee.
- **Conflict (clearance fee):** BMET charter Tk 250 [B0017] vs news of abolition Dec 2024 [B0099].
- **Navira letter** says other benefits apply under Kuwait's law [B0006]: templated letters.
- **Practice:** clearance card issuance reportedly halted for a week in Sept 2026, cards allegedly sold through back channels [B0101]; BBS average recruitment fee Tk 4.17 lakh across corridors incl. UAE.
- Searched BMET misc-infos with 12 UAE terms; Ministry notices/press releases for আমিরাত, দুবাই, ভিসিট, সতর্ক (no UAE-specific notice found; the 12-country Ministry-approval rule of 4 Nov 2026 does not include the UAE: Serbia, Moldova, Belarus, Congo, Russia, Japan, Iraq, Laos, Vietnam, Cambodia...). No official 2017 cost order found online (cap only via news [B0100]).
- Facts logged but not used: B0031 (Dubai consular wing), B0035 (officials detail), B0067 (mission e-passport fee for labourers USD 30/45, useful for renewal in UAE), B0014 details, B0012.

## c. Blocked pages

- Ministry office order (2017) fixing migration costs for 16 countries (UAE Tk 1,07,780): not on probashi.gov.bd office-orders; suggest `sources/probashi-migration-cost-16-countries-2017.pdf`; needed to cite the cap officially.
- https://www.jagonews24.com/national/news/404005 (2017 cost order report) failed (000); `sources/news-jagonews-migration-cost-16-countries-2017.html`.
- Facebook: Bangladesh Embassy Abu Dhabi (facebook.com/BangladeshEmbassyAbuDhabi) and Consulate Dubai posts on demand/visa attestation fees and 2026 visa notices; screenshots would help.
- UAE Embassy Dhaka attestation fee page (mofa.gov.ae missions/dhaka services, attestation tab, shows no fee); suggest a browser screenshot `sources/uae-embassy-dhaka-attestation-fees.png`.


# D findings: domestic workers (agent D)

Facts D0001-D0223 in facts.csv. Rate: use "AED1 = about Tk 34 [G0001, G0002]" if needed (not used below).

## a. Draft doc text

## Work visa: domestic worker

Housemaids, cooks, nannies, gardeners, home nurses, family drivers and guards working in a household come under the domestic workers law (Federal Decree-Law No. 9 of 2022, amended by Decree-Law No. 21 of 2023), not the main labour law; it lists 19 such occupations [D0001, D0002, D0003, D0004]. Only offices licensed by MOHRE (the Ministry of Human Resources and Emiratisation) may recruit them, and the worker must be at least 18 [D0006, D0005]. Bangladesh and the UAE signed a domestic worker MoU (memorandum of understanding) on 18 April 2018: recruitment goes only through MOHRE-licensed Tadbeer centres, only licensed Bangladeshi agencies may put forward workers, and the contract must state the job, salary, food, accommodation and transport, with salary paid through the WPS (Wage Protection System, the UAE's electronic salary transfer) [D0138, D0139, D0140]. Since 2022 the Tadbeer centres have been replaced by MOHRE-licensed "domestic worker recruitment offices"; 138 were active in July 2026 [D0133, D0136].

**Is it open now?** The route is open but tiny. Women going to the UAE fell from 24,307 in 2015 to 1,036 in 2024 [D0143, D0195]; BMET cleared 721 women for the UAE in 2025 and 764 from 1 January to 7 November 2026 [D0196, D0197]. Of 23,044 Bangladeshis cleared for the UAE in 2026 to 7 November, 59 were "House Keeper", 30 "House Keeper Female", 9 "Housemaid" and 4 "Baby Sitter"; the 2,591 "Driver" clearances do not separate house drivers from company drivers [D0145, D0146, D0147, D0148, D0149, D0150]. For the general 2026 visa situation for Bangladeshis, see Background ("Is it open now").

> **Need to know**
> - Are UAE recruitment offices getting domestic worker entry permits for Bangladeshi nationals in November 2026, or are they refused at the visa stage?
> - What does a UAE housemaid or house-driver visa cost a Bangladeshi worker in 2026, and who sells it?

### Step 1: Check you qualify

1. **Age.** The UAE minimum is 18 [D0005]. For BMET clearance a woman going as a domestic worker must be 25 to 45 and bring proof of age and a no-objection letter from her legal guardian [D0217].
2. **Health.** The recruiting office has you medically examined no more than 30 days before you enter the UAE [D0010]. The UAE residence medical includes a pregnancy test for domestic workers (maids, nannies, drivers and similar) [D0190]. Bangladesh's housekeeping course does not admit a woman who is pregnant, whose youngest child is under 6, or who has a contagious or incurable disease [D0202].
3. **Skill papers.** For jobs where the UAE requires a certificate, such as nursing and driving, the office must check you hold a certificate of experience [D0062]. The office may also need a police certificate of good conduct from Bangladesh [D0064].

### Step 2: Do the 30-day housekeeping course (women)

Housekeeping training is compulsory for women going to the Middle East as domestic workers and runs at 41 TTCs (Technical Training Centres, BMET's training schools) [D0218]. The course lasts one month (24 working days), is residential, and takes 10 to 40 women a batch [D0198, D0204].

You'll need [D0200, D0201, D0203]:

- age 25 to 45 (returnee women up to 50);
- class 5 pass (can be relaxed);
- your legal guardian's no-objection letter;
- a photocopy of your birth certificate, NID (national ID card) or passport, and the originals at the interview.

1. Watch for BMET's online admission notice, apply online, pay the fee and choose the TTC and the training date [D0199]. Fees are paid online into BMET's bank account; BMET sets them [D0208].
2. Go in person to the TTC for selection; the selection committee checks your originals and whether you can read and write [D0203].
3. Attend at least 90% of sessions [D0205]. You learn the destination's language, its home appliances and how to use them safely, and how to reach the nearest police station and the Bangladesh embassy [D0206].
4. Pass the final test (100 marks, pass mark 70%; language and practical work count 30 marks each) [D0207].
5. Download and print your digitally signed certificate from the online platform [D0209].

The certificate is valid 2 years for a first departure; between 2 and 3 years you need a 3-day refresher, after 3 years the full course again; a returnee with at least a year abroad does the 3-day refresher [D0210]. Ministry training branch: 02-41030254, dstraining@probashi.gov.bd [D0211]. TTC addresses: see Work visa (company worker), Step 1.

> **Need to know**
> - What is the housekeeping course fee in 2026?
> - Does the course include Arabic for the Gulf, and for how many hours?
> - Do men going as house drivers, cooks or gardeners need any specific BMET course?

### Step 3: Get the job through a licensed agency at both ends

1. **Bangladesh side.** Only agencies the ministry has approved may send women domestic workers [D0221, D0212]. Each must lodge a Tk 15 lakh FDR (fixed deposit) security with BMET, employ at least one woman in its office, take **no migration cost** from the woman, and sign an undertaking that its licence can be cancelled if she is abused [D0213, D0215, D0214]. The 1 September 2025 order approved 21 agencies, including Metak Al Madina Overseas (RL-2480), Just Recruiting (RL-2702), Tehjib Overseas (RL-1664), Raj International (RL-1523), Swapnasiri International (RL-2035) and Duranta Air International (RL-1876) [D0216].
2. **UAE side.** Recruiting domestic workers without a MOHRE licence is a crime: up to a year in prison and/or a fine of AED 200,000 to 1,000,000 [D0006, D0055]. A licensed office may deal only with licensed agencies abroad and must follow the MoU with the sending country [D0066, D0091].

   **Check it is real:** ask for the UAE office's trade licence number, then call MOHRE on 80060, choose your language, press 2 (domestic workers) and ask an agent, or search Services, Enquiry services, "Company Information" on mohre.gov.ae [D0134]; MOHRE's list of licensed offices is under Services, Authorised Service Centres [D0127]. For the Bangladesh agency's RL number, see Work visa (company worker), Step 1.

3. **Pay nothing.** A UAE office may not ask for or accept any commission or expense from you, before or after you start, directly or through anyone else [D0009]. It must give a document saying it pays any commission abroad itself without charging you, and MOHRE tells offices to make sure brokers abroad charged the worker nothing [D0065, D0117]. Your employer may not take money from you either [D0032]. An office that collects extra money is fined AED 5,000 per case [D0090].

   **What happens in practice:** many workers still pay fees at home and arrive in debt; MOHRE registered 10,646 complaints about recruitment fees in 2025 [D0153, D0154].

4. **Named ("direct") recruitment.** If a relative finds you a household, the office brings you by name at the employer's request; the office then skips some checks and owes the employer no refund if you leave [D0068, D0072]. If you quit after probation for your own reasons, you pay your own ticket home (the employer pays if you cannot) [D0046].

> **Need to know**
> - Which of the 21 approved agencies actually sent women to the UAE in 2025-26?
> - Does the MoU's list of approved Bangladeshi agencies still apply, and where is it published?

### Step 4: See the job offer and contract before you sign

1. The office must tell you the type of work and the wage before bringing you, let you read the job offer that matches the contract and sign it yourself [D0008, D0063]. MOHRE tells offices that the agency in Bangladesh must explain every term in a language you understand [D0116].
2. Check the contract is on MOHRE's standard form: two years, renewable [D0014, D0016]. It must state the workplace, the type of work, the start date, the total wage and basic wage, how you are paid, your leave, any probation, your rest periods and how it can end [D0015]. It is in Arabic plus a language you understand [D0058]; four copies are signed, one for you [D0118].
3. The Embassy's labour wing in Abu Dhabi and the Consulate's in Dubai attest individual housemaid visas [D0177, D0179]. The Embassy's form states the basic salary in AED per month and makes the employer pay your ticket out and your ticket home [D0183, D0182].
4. Have BMET check the UAE visa online: free, 3 working days; bring the visa and a copy of the passport visa page [D0219]. At BMET clearance a single visa costs Tk 250 tax if attested, Tk 400 if not [D0220]. For the rest of BMET clearance, see Work visa (company worker).

> **Need to know**
> - What minimum monthly salary does the Embassy require before attesting a Bangladeshi housemaid visa in 2026 (it was Dh750 in 2014 [D0164])?
> - What do Bangladeshi housemaids in the UAE actually earn in 2026?

### Step 5: Arrive and get your residence visa

1. Wages are due from the day you enter the UAE [D0038]. Probation can last up to six months [D0017].
2. The employer must buy health insurance before your residence permit is issued or renewed (compulsory in Abu Dhabi and Dubai since 1 January 2025); the basic package is AED 320 a year [D0185, D0186]. The employer's worker insurance covers up to AED 20,000 of unpaid wages (last 120 days), end-of-service pay, ticket home, work-injury costs and body repatriation [D0188, D0189].
3. Until the residence visa is stamped you cannot leave the country, except by cancelling the entry permit in an emergency [D0192].

### Your rights at work

These are minimums; any contract term worse than the law is void [D0060].

- **Rest.** At least 12 hours' rest a day, 8 of them in a row [D0018]. One paid day off a week, agreed with the employer; if you work it you get another day off or a day's wage, and not more than two rest days in two weeks unless you agree [D0019, D0075].
- **Leave.** 30 days' paid annual leave, paid before you go; 2 days a month if you worked 6-12 months [D0020]. A return ticket home every two years, a one-way ticket if the contract ends after the leave, and cash for unused leave when you finish [D0021, D0022, D0023]. Sick leave up to 30 days a year with a medical report: 15 days full pay, 15 days half pay [D0024].
- **Pay.** In dirhams, within 10 days of the due date, proved by a written receipt [D0037, D0038]. Deductions only for damage from your grave mistake, at most a quarter of the cost, with your consent or MOHRE's approval [D0039]. WPS is compulsory only for private tutors, trainers, home care providers, private agricultural engineers and messengers [D0106]; for housemaids it is voluntary [D0107, D0155].
- **Food, room and care.** Suitable accommodation, meals and work clothes; medical treatment or health insurance; protective gloves and shoes [D0025, D0026, D0083]. You may not be lent to other people, except the employer's close relatives with your consent, or moved to another occupation without your consent [D0027, D0082, D0029].
- **Your passport.** You keep your own passport and ID [D0030, D0114]. The fine on an employer who keeps them is only AED 500, and in practice it does not stop employers [D0088, D0156].
- **Abuse.** Sexual harassment, forced labour and discrimination are banned [D0007]. An employer whose household assaults or harasses you is fined AED 20,000 and has its file suspended [D0110, D0086].
- **Travel with the family.** The UAE contract still applies abroad unless that country's law says otherwise [D0035].
- **End-of-service pay.** MOHRE says 14 days' wage per year after a year's service, lost if you stop work illegally [D0122, D0123]; dues are paid within 10 days of the end [D0043]. Domestic workers get no unemployment insurance (ILOE) [D0187].

> **Need to know**
> - Does any UAE rule give a domestic worker the right to keep and use her own mobile phone?
> - Has the Cabinet issued the end-of-service gratuity system for domestic workers promised in the 2022 law [D0048]?

### If you are mistreated or not paid

**First keep proof:** photos of your contract, passport, visa and pay receipts, the employer's name, address and phone [D0015, D0038]. Use the routes below; several at once is fine.

1. **MOHRE complaint.** You or the employer may complain during the contract and up to 3 months after it ends [D0094, D0053]. Call 600590000, the Labour Claims and Advisory Centre on 80084, or use MOHRE's online domestic worker platform (eservices.mohre.gov.ae/Mohre.Domestic.UI) [D0120, D0137, D0112]. A legal researcher hears both sides; if there is no settlement within two weeks MOHRE refers the case to court [D0084, D0113]. MOHRE itself decides claims up to AED 50,000, and its decision can be enforced; either side can go to court within 15 working days [D0051, D0050]. Workers pay no court fees and cases are urgent [D0054]. After referral you must file at the court within 14 days, and within 30 days you can ask for a temporary permit to work for someone else; meanwhile the recruiting office must house and feed you [D0096, D0097, D0098].
2. **If you are assaulted.** You may leave at once if the employer or their representative assaults, humiliates or sexually assaults you; report to the police promptly and notify MOHRE within 3 days [D0078, D0079]. Then go back to your recruiting office, or give MOHRE another address and a phone number [D0080]. If you leave without telling the employer for any reason, lodge a complaint within 48 hours, so you are protected and not treated as absconding [D0095, D0119].
3. **Police and shelters.** Police 999, ambulance 998 [D0121]. Dubai Police: human trafficking hotline 8007283, labour complaints 8005005 [D0171, D0172]; its human rights directorate gives temporary shelter, visas and tickets home [D0173]. DFWAC (Dubai Foundation for Women and Children) runs a free 24/7 helpline, 800111, also on WhatsApp, with shelter, medical, legal, consular and immigration help [D0174, D0168]. In Abu Dhabi, Ewa'a shelters victims of violence and trafficking; Sharjah's women's protection line is 800700 [D0169, D0170]. **In practice:** shelters need formal recognition as a trafficking victim, and police sometimes send women to their embassy instead [D0158, D0157].
4. **The Bangladesh missions.** The Embassy in Abu Dhabi (Villa 46-48, Al Jawwalah Street, Al Saadah; +971-2-4465100; mission.abudhabi@mofa.gov.bd) takes complaints, attends labour courts and gives distressed workers money or a ticket home [D0178, D0175, D0176]. The Consulate in Dubai's labour wing (weekdays 9 am-5 pm; WhatsApp text +971 50 816 8253 or +971 50 816 8363) counsels women workers and forwards complaints to Bangladesh [D0180, D0181, D0179]. Bangladesh runs no safe home for women in the UAE; its three are in Riyadh, Jeddah and Muscat [D0184].
5. **From Bangladesh.** A complaint against the agency goes in writing, with evidence, to BMET's Director General: free, 30 working days; Director (Employment) 01711111544, diremi@bmet.gov.bd [D0222]. A woman who returns within a year after abuse gets Tk 5,000 at the airport welfare desk [D0223].

> **Need to know**
> - Does the Embassy or Consulate shelter a woman who escapes an employer, and where does she stay while her case runs?
> - Which language lines does MOHRE's 600590000 offer (is Bangla available)?

### Leaving or changing employer

1. **Changing employer.** MOHRE approves a transfer when the contract has ended, when a court finds the employer broke the contract, or when the employer agrees in writing [D0092, D0093]. If your wage is cut or the employer breaks the contract, notify MOHRE; after two weeks without a fix you may leave, keep your rights, and transfer or go home [D0077, D0081]. For a named recruit who moves in the first contract, the new employer repays part of the old employer's costs [D0074].
2. **Cancelling your permit yourself.** You can ask MOHRE to cancel your work permit for any reason without the employer's consent; if the employer does not answer within 10 days it is processed [D0099, D0100]. You must then change status or leave the UAE [D0085]. The cancellation goes through MOHRE or the Domestic Work Bundle [D0191].
3. **Absconding ("absence") reports.** The employer must report you within 5 days of an unexcused absence [D0040, D0126]. Ten days in a row, or 15 days in a year, without an excuse ends the contract [D0042]. MOHRE can cancel the report if you were absent under 10 days or lawfully, were at work or on leave, or went back to the recruiting office [D0101, D0102]. A true report bars a new work permit for a year after you leave; so do drunkenness at work, assaulting the family, or posting photos or videos of the home [D0103, D0104]. A false report costs the employer AED 5,000 [D0087].
4. **Why offices push workers back.** If you leave in probation the office must refund the employer in full or replace you; after probation it refunds (cost ÷ contract months) × months left, for example AED 7,000 of AED 12,000 after 10 of 24 months, within two weeks [D0069, D0070, D0071, D0125, D0073]. Late refunds were 106 of 135 fines on offices in the first half of 2026 [D0135]. The office must house and feed workers returned to it [D0011].
5. **Going home.** If the employer ends the contract for a reason that is not your fault, it pays your ticket and all dues [D0045]; dues are due within 10 days [D0043]. Claims die 3 months after the job ends [D0053].

> **Need to know**
> - Can a domestic worker move to a company (labour law) visa without leaving the UAE, and how?

### Scams

- **Unlicensed offices and online "maid" sales.** The UAE shut 230 social media accounts recruiting domestic workers without a licence in 2025; some sponsors and agents advertise "selling" workers online [D0160, D0159].
- **The visit-visa job.** Some workers enter on tourist visas and are kept working illegally, then threatened with their status [D0161]. A real domestic job starts with an entry permit for employment, not a visit visa (see Work visa (company worker), Step 1 on checking a visa).
- **Big salary promises and contract switching.** Fake recruiters promise high pay; some workers find a lower wage on the UAE contract [D0162, D0167].
- **Fees.** Anyone asking a woman domestic worker for migration money breaks Bangladesh's zero-cost rule and the UAE law [D0214, D0009].

## b. Notes (for notes.md)

- Searched: uaelegislation.gov.ae (law, regulations; via Wayback, site 403), u.ae domestic workers page (updated 06 Oct 2026), u.ae trafficking, health, worker insurance, ILOE pages; MOHRE (site unreachable from here: curl, Firecrawl and WebFetch all failed; used Wayback copies of the domestic workers page and a 2023 news item); Ministerial Resolutions 674/675/676 (Wayback of u.ae media); OEP clearance reports (women by year; categories by year, from another agent's saved JSON); BMET charter 2026 (page images checked); Ministry housekeeping policy and women DW agency order (image PDFs, transcribed); Embassy/Consulate pages; HRW 2014; US TIP 2026; Gulf News 2022 and 2026; Arabian Business and BBC Bangla on the 2018 MoU; Bangla searches for UAE housemaid abuse and salary (mostly Saudi results).
- Conflicts: (1) appeal against MOHRE's decision: uaelegislation consolidated text (archived Oct 2026) says court of first instance, decided in 30 working days [D0050]; MOHRE's translation of the 2023 amendment says Court of Appeal, 15 working days [D0061]. Draft uses only "court within 15 working days". (2) Sick leave second 15 days: law says half pay [D0024], MOHRE page says unpaid [D0124]; draft follows the law. (3) Gratuity: MOHRE page (May 2024) says 14 days/year [D0122], but the 2022 law leaves the system to the Cabinet [D0048].
- Practice: route has collapsed from 24,307 women (2015) to under 1,000 a year; very few clearances are labelled housemaid. TIP 2026: fees paid at home, passports kept, shelters need formal victim status. No Bangladeshi safe home in UAE.
- Logged but not used: D0012, D0013, D0034, D0036, D0044, D0047, D0049, D0052, D0056, D0057, D0059, D0067, D0076, D0089, D0105, D0108, D0109, D0115, D0128-D0132 (Tadbeer package details; useful for Background), D0141-D0142 (BBC: 2018 reopening, Tadbeer legal adviser), D0144, D0151-D0152, D0163, D0165-D0166, D0193 (2018 Tadbeer prices: Bangladeshi recruitment ceiling Dh7,000; agency guide, old), D0194 (agency salary ranges, no Bangladesh rate). D0193/D0194 are weak; keep for Background only if nothing better.
- Not found: current Bangladesh minimum wage for UAE housemaids; whether UAE visas for Bangladeshi domestic workers are issued in Nov 2026; real cost; phone rights; Embassy shelter practice.

## c. Blocked pages

- MOHRE whole site unreachable (connection refused). Please download in a browser:
  - https://mohre.gov.ae/assets/download/594f4504/Administrative%20Resolution%20No.%205%20of%202024.pdf.aspx -> sources/mohre-admin-resolution-5-2024-recruitment-manual.pdf (operation manual: refunds, replacements, warranty, office duties to workers)
  - https://www.mohre.gov.ae/en/services/approved-services-centers/domestic-workers-services-centers -> sources/mohre-domestic-service-centres.html (list of licensed offices)
  - https://mohre.gov.ae/en/media-center/news/27/7/2026/mohre-issues-135-fines-against-42-domestic-worker-recruitment-offices-during-the-first-half-of-2026 -> sources/mohre-news-135-fines-2026-07.html (official version of D0135-D0137)
  - https://www.mohre.gov.ae/en/media-center/news/25/2/2026/mohre-12-unlicensed-domestic-worker-recruitment-offices-closed-and-referred-to-public-prosecution -> sources/mohre-news-12-unlicensed-offices-2026-02.html
  - https://www.mohre.gov.ae/en/services/issuance-of-a-new-work-permit-domestic-workers-2022 -> sources/mohre-service-new-work-permit-domestic.html (fees, conditions)
  - https://www.mohre.gov.ae/en/faq.aspx -> sources/mohre-faq.html (domestic worker FAQs)
- https://www.wam.ae/en/article/hszr6wlg-uae-bangladesh-sign-mou-domestic-workers -> sources/wam-uae-bangladesh-domestic-mou-2018.html (official WAM text of the 2018 MoU; JS-only)
- https://www.tamm.abudhabi/en/articles/ewaa-shelter-for-women-and-children -> sources/tamm-ewaa-shelter.html (Ewa'a contact numbers; JS-only)
- Facebook screenshots that would help: Bangladesh Embassy Abu Dhabi (facebook.com/BangladeshEmbassyAbuDhabi) and Consulate Dubai posts on housemaid visa attestation requirements and minimum salary; MOHRE UAE post on "domestic worker terminated after probation responsible for return expenses" (facebook.com/MOHREUAE/posts/689126813248976).


# F findings: long-stay residence other than ordinary employment

Agent F, 8 Nov 2026. Facts F0001-F0147 (147 logged; about 104 from official sources, 43 news/guide/third-party). Cross-referenced other agents' ids where they already cover a point: V0188 (checking visa validity on ICP/GDRFA), W0098 (Emirates ID fee).

---

## A. Draft doc text

## Family residence (spouse, children and parents)

**Status for Bangladeshis (Nov 2026).** The rules below are the law for every nationality, but since July 2024 Bangladeshis have met restrictions and long stalls on new family visas, as on student, tourist and employment visas and company-to-company transfers; Bangladesh's Expatriates' Welfare Minister said so on 18 August 2026 [F0030]. Reporting in January 2026 said only "skill visas" and "high-profile visas" were being issued to Bangladeshis [F0031].

> **Need to know**
> - Are GDRFA and ICP approving new family residence applications by Bangladeshi sponsors in November 2026, and for which salary or job levels?
> - Are renewals of existing Bangladeshi family visas going through normally?

A resident worker (man or woman) can sponsor a spouse, unmarried daughters of any age, sons under 25 and children with special needs [F0001]. The family visa runs for the same period as the sponsor's and can never be longer [F0008]. If the sponsor's visa is cancelled, the family's visas must be cancelled too; the family then has 6 months to get a new residence permit, and a sponsor who neither renews nor cancels can be fined [F0004, F0005]. A residence permit becomes void after more than 180 consecutive days outside the UAE [F0027].

**Who qualifies to sponsor** [F0002, F0006, F0007, F0025]:

- a valid UAE residence permit;
- salary of at least AED 4,000 a month, or AED 3,000 plus housing given by the employer;
- housing big enough for the family, owned or rented;
- proof of the relationship.

Dubai has a separate humanitarian route for a worker earning under AED 4,000 whose family's residence expired or was cancelled inside the UAE; it needs the attested marriage and birth certificates, 3 months' bank statements and an attested tenancy contract, and a committee decides each case [F0035, F0038].

### Step 1: Get the marriage and birth certificates attested

The UAE accepts a Bangladeshi certificate only after three attestations: Bangladesh's Ministry of Foreign Affairs (MoFA), then the UAE Embassy in Bangladesh, then the UAE Ministry of Foreign Affairs (UAE MOFA) [F0043].

1. **Notarise the certificates.** MoFA works from a notarised scan of the nikahnama or marriage documents issued by the nikah registrar, and of the birth certificate issued by the city corporation, municipality or union parishad [F0053, F0054]. A hospital birth certificate must first be attested by the Civil Surgeon or the Health Ministry [F0054].
2. **Apply to MoFA on mygov.bd.** Register, choose the option for the document type (marriage certificate or birth certificate), fill in the form and upload the scan as JPEG, JPG or PNG [F0055]. It is free and takes 5 working days; an SMS tells you when the attested copy is ready to download from your mygov account [F0053, F0056]. Questions: MoFA consular section, 024152830, asconsular2@mofa.gov.bd [F0056].
3. **Apply for the UAE attestations online.** Make a UAE Pass account, log in at mofa.gov.ae and choose Services > Services for Individuals > Document Attestation > UAE Embassy and Consulate abroad > Bangladesh > mission "VFS delivery service" > "Issued from Outside UAE" [F0045]. Pay AED 300 per personal document on the portal (AED 150 Embassy + AED 150 UAE MOFA) plus VFS Global's service fee [F0046]. If the application is rejected only the Embassy fee comes back [F0047].
4. **Hand over the originals.** A VFS courier collects them within 48-72 hours, or you drop them at the VFS UAE Attestation Centre; the Embassy and UAE MOFA attest digitally in 2-3 working days and nothing more is needed inside the UAE [F0044, F0049]. VFS call centre: +8809606 777 919 [F0049].

**Check it is real:** the original is not stamped; download the attested document at verify.mofa.gov.ae with the reference number and issue date [F0048, F0051].

> **Need to know**
> - What is VFS Global's service fee in Taka for one UAE attestation in Dhaka?
> - Where are VFS's UAE Attestation Centres in Bangladesh?
> - Does ICP or GDRFA also ask for an Arabic translation of a Bangladeshi nikahnama?

### Step 2: Prepare the sponsor's papers and housing

You'll need [F0011, F0012, F0016, F0028]:

- the sponsor's passport, residence and Emirates ID (the national identity card for residents);
- the employment contract, or a salary certificate if the employer is government, semi-government or free zone;
- an employment certificate showing monthly income and housing;
- a water or electricity bill;
- the attested marriage certificate and children's birth certificates;
- health insurance for each family member.

In Dubai the sponsor must buy health insurance for resident dependants; in Abu Dhabi the employer or sponsor covers one spouse and 3 children under 18 [F0063, F0064]. A partner sponsoring family in Dubai needs a share of at least AED 48,000 [F0020]. A wife sponsoring needs a no-objection from the father [F0016].

In Dubai, a rental is registered in Ejari (Dubai Land Department's tenancy register) with the unified tenancy contract and the tenant's Emirates ID, for AED 177.75 to AED 220 in total [F0065, F0066].

> **Need to know**
> - Does GDRFA still require an Ejari (Dubai) or Tawtheeq (Abu Dhabi) tenancy contract to sponsor a spouse and children, or only for parents?
> - Is a bed-space or shared-flat tenancy accepted for a family visa?

### Step 3: Apply for the entry permit, then the residence

1. **Apply for the family entry permit** in the sponsor's emirate: Dubai residents with GDRFA (General Directorate of Identity and Foreigners Affairs, Dubai) online with UAE Pass, at a GDRFA Customer Happiness Centre or at an Amer centre (Dubai's licensed typing centres); other emirates with ICP (Federal Authority for Identity, Citizenship, Customs and Port Security) on smartservices.icp.gov.ae or the ICP app, which needs UAE Pass [F0021, F0015].
2. **Pay.** Dubai: AED 200 plus 5% VAT; if the family member is already in the UAE, add AED 10 knowledge fee, AED 10 innovation fee and AED 500 [F0018, F0019]. ICP: AED 100 application, AED 100 per year of residence, AED 100 smart service fee, AED 20 deposit fee, and AED 500 for a change of status inside the UAE [F0013, F0014]. GDRFA quotes 48 hours and ICP 2 days [F0021, F0015].
3. **Enter within the permit's validity and finish within 60 days.** The permit allows 60 days from entry to complete the residence; after that overstay costs AED 50 a day [F0017, F0009, F0010].
4. **Medical and Emirates ID.** Family members aged 18 or over must pass the medical fitness test at an approved centre in the UAE [F0003, F0023]. Then apply for the residence permit and Emirates ID: Dubai charges AED 200 plus AED 10, AED 10, AED 500 if inside the UAE, and AED 20 delivery, rising by AED 100 a year for residence over two years [F0022]. If nothing is missing GDRFA emails the approval [F0024].

**Check it is real:** check an Abu Dhabi or Northern Emirates visa on ICP's File Validity page and a Dubai visa on GDRFA's Status Inquiry page [V0188]. ICP call centre: 600522222 [F0015].

> **Need to know**
> - Is there a separate refundable deposit for a spouse or child's residence in any emirate in 2026?

### Parents

In Dubai, parents (and minor brothers and sisters who depend on the worker, or the spouse's parents and minor children) come under GDRFA's humanitarian-case residence: one year, renewable, decided case by case by a committee [F0032, F0037, F0038]. You'll need the parent's passport copy, a salary certificate or contract showing at least AED 10,000 a month (or partnership papers), an attested tenancy contract big enough for the family, and 3 months' bank statements [F0033, F0034]. On approval GDRFA takes a guarantee of AED 5,000 per person, up to AED 15,000 [F0038]. Fees are AED 200 plus the same extras as above; it takes about 14 days, through the GDRFA app or website, Amer centres or the Humanitarian Cases Section at Festival Centre [F0041, F0040]. The grace period after it ends is 60 days [F0039]. Sons over 25 can be sponsored with certified proof of continuing studies [F0036]. A resident's widow or divorcee inside the UAE can sponsor herself and her children within 6 months of the death or divorce [F0042]. Green visa holders may sponsor first-degree relatives, including parents [F0001, F0094].

> **Need to know**
> - What do ICP (Abu Dhabi and Northern Emirates) require to sponsor a resident's parents: salary threshold and deposit?

### Can a family member work?

Yes, but only with a work permit. A foreigner may not work, paid or unpaid, without one [F0029]. The employer applies to MOHRE (Ministry of Human Resources and Emiratisation) for a "Dependents Sponsored by Family Members" work permit; the family member keeps the family visa [F0057]. Conditions: aged 18 or over, no other active permit, valid residence under the relative; all skill levels; no quota needed; valid 2 years; full-time, part-time, temporary, flexible, remote or job-sharing contracts [F0057, F0059, F0060]. Fees are AED 50 to apply and AED 250 to issue, free online apart from these, with typing-centre commission capped at AED 72; MOHRE takes 2 working days [F0058]. In the DMCC free zone the employer instead applies for a one-year identity card, counted in its visa quota [F0062].

## Student visa

**Status for Bangladeshis (Nov 2026):** new student visas for Bangladeshis are among those stalled since July 2024, the Expatriates' Welfare Minister said on 18 August 2026 [F0030].

> **Need to know**
> - Are UAE universities currently getting student visas approved for applicants from Bangladesh, and which universities?

A student stays either on a resident parent's sponsorship or on the university's [F0067]. A son over 25 can stay on a parent's visa with proof he is in higher education, and a daughter can be sponsored to study at any age until she marries [F0068]. The university is the sponsor for a university visa, and it must be licensed and approved by the Ministry of Education or the emirate's education authority [F0071]. Students' families may stay if they can afford suitable housing [F0070].

### Step 1: Check the university

1. **Check it is licensed** on caa.ae > HE Institutions (the Commission for Academic Accreditation list), filter "Active"; it shows each institution's emirate and status (Active, Inactive, Currently on Probation) [F0080].
2. **Free-zone branch campuses in Dubai** need a letter from KHDA (Dubai's Knowledge and Human Development Authority) for the visa; a training institute only gets a 90-day entry permit, not residence [F0079].

> **Need to know**
> - Where does KHDA publish the list of free-zone universities allowed to sponsor student visas?

### Step 2: Apply through the university

You'll need [F0069, F0073]:

- passport and photo;
- the university's enrolment certificate and acceptance letter stating the programme and its length;
- the education authority's approval certificate (the university gets it);
- valid health insurance.

Fees are set by each university. Examples: Middlesex University Dubai charges AED 5,555.22 if you apply from outside the UAE (AED 7,235.22 inside), covering processing, Emirates ID and medical insurance, plus a refundable AED 2,500 deposit, and wants 25% of the year's tuition paid first [F0074, F0075, F0076]. The American University in Dubai charges AED 2,000 plus a refundable AED 3,000 deposit [F0077]. If the visa is refused the deposit comes back but the government fee may not [F0075]. Leaving without cancelling the visa forfeits the deposit [F0077].

The visa lasts for the programme; ICP lets a student stay 180 days after finishing, but some universities keep it active only 3 months after graduation [F0072, F0078].

### Can a student work?

Only through an employer's MOHRE student training and work permit: for students aged 15 and over already in the UAE, valid 3 months, AED 50 federal fee, with guardian consent if under 18, the institution's no-objection for training, and a medical certificate [F0081, F0082]. University students can also get MOHRE's free 2-year private-tutoring permit [F0083].

> **Need to know**
> - Is there a weekly hours limit for university students working on the student training and work permit?

## Green visa

A green visa is a 5-year renewable residence with no employer sponsor, and the holder can sponsor family, including first-degree relatives [F0086, F0094]. Three routes:

- **Skilled worker:** MOHRE work permit under a valid contract, MOHRE skill level 1, 2 or 3, at least a bachelor's degree, and salary of at least AED 15,000 a month [F0087, F0088]. MOHRE does not count anyone earning under AED 4,000 or without a degree as skilled [F0061].
- **Freelancer or self-employed:** MOHRE freelance permit, a bachelor's degree or specialised diploma, and self-employment income of at least AED 360,000 a year for the past two years, or proof of solvency [F0089, F0084]. Abu Dhabi's Residents Office is not taking nominations for this category [F0095].
- **Investor or partner:** a trade licence and partnership or investment contract with a paid share of at least AED 1 million [F0090, F0091].

The Dubai entry permit costs AED 200 plus VAT (plus AED 520 if you are inside the UAE), and you have 60 days from entry to finish [F0092]. ICP charges AED 100 to apply, AED 100 per year and AED 100 smart service fee [F0093].

> **Need to know**
> - Are green visas being approved for Bangladeshi skilled workers in 2026?

## Golden visa

A golden visa is a 5- or 10-year renewable residence with no sponsor; the holder may stay abroad more than six months and sponsor a spouse, children of any age and parents [F0096, F0102]. It is applied for directly on ICP's platform or by government nomination; anyone eligible but abroad gets a 6-month multiple-entry visa, renewable once [F0106, F0103]. ICP charges AED 100 to apply, AED 100 per year and AED 100 smart service fee [F0107]. Employers hire a golden visa holder on a 2-year golden visa work permit [F0085].

**Categories** [F0097]:

- **Skilled professional (10 years):** MOHRE work permit, skill level 1 or 2, bachelor's degree, salary of at least AED 30,000 a month, and a practice licence where required [F0098]. In Dubai without a government nomination, the AED 30,000 must be basic salary excluding allowances since November 2025, earned for the previous two years too [F0099, F0100].
- **Investor:** AED 2 million in a fund, bank deposit or company, or a company paying AED 250,000 a year in federal tax (10 years); or property worth AED 2 million, wholly owned or with an approved local bank loan (5 years) [F0097, F0101].
- **Entrepreneur (5 years):** an approved innovative project [F0097].
- **Exceptional talent, scientists and specialists (10 years):** by recommendation [F0097].
- **Outstanding students and graduates:** one-time; for example a GPA of 3.5 from an A-ranked UAE university, 3.8 from a B-ranked one, or 3.5 from a top-100 world university, within two years of graduating [F0104].
- **Humanitarian pioneers and frontline heroes (10 years):** including nurses, paramedics and lab and pharmacy technicians accredited to the National Pride Office [F0097, F0105].

**Status for Bangladeshis:** Bangladeshis still receive golden residence, mostly by recognition; journalist Keramat Ullah Biplob got a 10-year golden residence in March 2025, after actor Shakib Khan and cricketers Ashraful and Tamim Iqbal [F0109].

**Scam:** on 7 July 2025 Bangladeshi media reported a cheap "nomination-based" golden visa for Bangladeshis and Indians [F0108]. ICP denied it the next day: golden visas go only through official UAE channels, no consultancy inside or outside the UAE is authorised, and nobody should pay fees or hand over documents to anyone selling one [F0110, F0111]. Check eligibility on icp.gov.ae or call 600522222 [F0111].

## Other residence visas (freelance, partner or investor, remote work, retirement, property owner)

- **Freelance permit:** MOHRE issues it to people working independently, including foreigners on self-sponsored residence, without an employer or contract [F0084]. It is the first requirement for the self-employed green visa [F0089].
- **Partner or investor visa through a trade licence:** a free zone company issues residence visas to its shareholders. In DMCC, a share certificate of at least 50 shares totalling AED 50,000 gives a 3-year investor visa with no immigration deposit [F0117, F0118]. The visa is tied to that free zone and does not allow work on the mainland [F0119], and each company gets only a few visas (a DMCC flexi desk: up to 3) [F0120]. ICP inspects for people brought in under one sponsor who work for others [F0121].
- **Remote work visa:** one year, renewable, no sponsor; needs health insurance, medical fitness, proof of working for a company outside the UAE and a salary of at least USD 3,500 a month [F0112, F0113].
- **Retirement visa:** 5 years, for people who worked at least 15 years and are 55 or older, with property worth AED 1 million plus AED 1 million savings, or income of AED 180,000 a year (AED 240,000 in Dubai) [F0114, F0115].
- **Property-owner visa:** a fully built, wholly owned, habitable property registered with the land authority, plus income of at least AED 10,000 a month or proof of solvency [F0116].

> **Need to know**
> - What do Bangladeshis pay, all in, for a "partner visa" through a free-zone or mainland trade licence in 2026?
> - Which free zones are refusing or holding partner visas for Bangladeshi nationals in 2026?
> - What happens to a partner-visa holder who does not renew the trade licence: is the visa cancelled and is there a fine?

## Changing visa type

- **Visit visa to family or employment residence:** Yes. An entry visa can be converted to residence without leaving the UAE after paying the fee [F0026]; ICP charges AED 500 for the status change and GDRFA adds AED 500 for a person inside the country [F0014, F0019]. For Bangladeshis, new employment visas and company-to-company transfers have been restricted since July 2024 [F0030].
- **Family residence to work:** Yes, without changing visa. The employer gets a MOHRE dependant work permit (see Family residence) [F0057].
- **Employment to family residence:** Yes, if the spouse or parent qualifies to sponsor; the new residence is issued after the old one is cancelled, for AED 500 inside the country [F0014].
- **Expired or cancelled residence to new residence:** Yes, without leaving, after paying the fee [F0026].
- **Employment to green or golden visa:** Yes, if you meet the salary, skill-level and degree thresholds [F0087, F0098].
- **Student to work:** Only with a new employer work permit; a university visa lasts until 180 days after study ends [F0072].

> **Need to know**
> - Is GDRFA or ICP refusing in-country status changes for Bangladeshi passport holders in 2026?

## Asylum

The UAE is not party to the 1951 Refugee Convention or its 1967 Protocol, and its law gives no asylum or refugee status [F0142, F0144]. Anyone without legal residence is treated under immigration law and can be detained; some people seeking protection have been held in a section of the airport while waiting for resettlement elsewhere [F0145, F0144]. People without legal residence, including those on visit or expired visas, generally cannot work legally [F0146]. The refugees UNHCR (the UN refugee agency) recognises in the UAE come mainly from Iraq, Syria and Palestine; it counts 1,377 refugees and 6,257 asylum seekers [F0143, F0142].

> **Need to know**
> - Does UNHCR's office in Abu Dhabi register new asylum claims, and how is it contacted?

## Having a child in the UAE

The baby's residence is a family residence, so the parent must meet the family-sponsorship salary and housing rules [F0001, F0002].

**Unmarried parents.** A man and an adult woman who have a child outside marriage face at least 2 years' jail, but no case is brought if they marry, or one or both acknowledge the child and get the child identity and travel documents from their country [F0130, F0129]. The birth certificate needs a marriage certificate or the parents' acknowledgement of the child legalised by their embassy or a notary [F0126]; if the father is unknown, a court order based on the mother's acknowledgement is needed [F0127].

1. **Get the birth certificate within 30 days** at the hospital or the emirate's health authority (MOHAP, DHA in Dubai, DoH in Abu Dhabi) [F0122]. You'll need the attested marriage certificate translated into Arabic, both parents' passports (originals and copies), the hospital's birth notification and discharge summary [F0123]. Late reporting can be fined up to AED 5,000 [F0128].
2. **Attest it** with MOHAP (a DHA or DoH stamp counts) and the UAE MOFA [F0147, F0052]; the UAE MOFA fee is AED 150 [F0050].
3. **Register the birth with Bangladesh.**
   - Dubai and Northern Emirates: apply online at bdris.gov.bd, then take the printed form, 2 photos, parents' passport copies, the child's UAE birth certificate attested by UAE MOFA, and the marriage certificate attested by MoFA Dhaka to Foshwa Global, 3 Reem Residency, Um Hurair, Karama, Dubai (appointment needed; 8 am-4 pm Mon-Fri; +971 4 288 0190, WhatsApp +971 50 729 2294) [F0131, F0132, F0133, F0134]. Free within 45 days, then AED 10, plus AED 31.50 service charge; certificate in 3 working days [F0134, F0135, F0132].
   - Abu Dhabi: parents' digital birth certificates, the child's photo and original UAE birth certificate and parents' original passports to Room 102 at the Embassy; free within 45 days, then AED 5, cash only, 15 days [F0136, F0137].
4. **Get the child a Bangladeshi passport.** Apply online at epassport.gov.bd, then go to the Consulate or Embassy with the 17-digit online-verifiable birth certificate in English, two 3R lab photos on white, the UAE birth certificate in English and the parents' passports or NIDs; children under 5 need not attend [F0138]. A first passport needs police verification in Bangladesh; otherwise a regular passport takes 4-6 weeks [F0139]. In Abu Dhabi a 48-page, 5-year passport is AED 405 (express AED 610), cash only [F0140].
5. **Get the residence visa within 120 days.** The baby's passport, Emirates ID and residence must be done within 120 days of birth; after that AED 100 a day is charged and the baby cannot leave the UAE [F0124].

In Dubai a newborn is covered under the mother's health insurance for its first 30 days [F0141].

> **Need to know**
> - What does a normal delivery cost at a government hospital for an uninsured or basic-insured Bangladeshi mother in Dubai and Abu Dhabi?
> - What is the Dubai Consulate's current fee for a child's e-passport?

---

## B. Notes (for notes.md)

**Searched:** u.ae residence pages (family, student, retired, virtual work, green, golden, having a baby); ICP service cards (Issuing Residency Permit, Issuance of Visa); GDRFA service pages (family entry permit, family residence, retired, virtual, green x3, humanitarian); uaelegislation (Law 29/2021, Exec Reg Cabinet Res. 65/2022 with golden annex, Births and Deaths Law 10/2022, Penal Code 31/2021) via Wayback; MOHRE work-permit service pages via Wayback; UAE MOFA attestation; VFS Bangladesh; Bangladesh MoFA charter; Dubai Consulate and Abu Dhabi Embassy birth registration and e-passport; universities (MDX, AUD, CUD); CAA list; UNHCR RIMAP; US State Dept HRR; Bangla and English news on status (Jugantor, Dhaka Tribune, NTV, itvbd, Desh Rupantor), WAM denial, Fragomen.

**Conflicts:**
- Newborn deadline: u.ae says 120 days and AED 100/day (F0124); Exec Reg Art. 6 says 4 months (F0125); guides quote AED 50/day. Kept u.ae (newest, 4 Nov 2026).
- Exec Reg Art. 52 says retiree income AED 240,000 (F0114 Dubai), u.ae says AED 180,000 federal / AED 240,000 Dubai; ICP card says AED 240,000. Kept u.ae split; worth an insider check.
- Green investor share: GDRFA and ICP both AED 1 million (F0090, F0091); older guides cite less.
- GDRFA family residence page's "Terms and Conditions" text is wrongly copied from the entrepreneur service (Dubai Future Foundation nomination); not used.
- Tenancy contract for spouse/children in Dubai: official pages silent (ICP asks a utility bill; GDRFA asks attested tenancy only for humanitarian/parents); guides conflict (some say Ejari no longer required). Left as Need to know.
- Exec Reg PDF is the 2022 text; the legislation page lists 6 amendments (last update 3 Jun 2026). Golden-visa thresholds may have been amended.

**Practice:** Minister Ariful Haque Chowdhury (18 Aug 2026) is the most authoritative dated statement of the family/student/employment/transfer stall (F0030). A LinkedIn post by Legal Talks with Aminul (Dubai consultant) says partner-visa and transfer routes for Bangladeshis are "temporarily restricted" (blocked, not logged). Bangla Facebook/TikTok agents widely sell "partner visas" and "Sharjah partner visa" packages (Satwa Road shops) — no price evidence saved.

**Facts logged but not used:** F0121 used; F0016 also covers female sponsors; F0042 widow route used briefly. All others used.

**Scratchpad incident:** I accidentally overwrote another agent's `addfacts.py` in the shared scratchpad with my driver (my own copy is `F-addfacts.py`). Whoever used `addfacts.py` with `facts1-5.json` should check it.

**Dates:** ICP service cards dated 2024-12-11 from page meta (template date; content is live) -> possibly-outdated. GDRFA pages undated -> possibly-outdated, following other agents.

## C. Blocked pages

- https://www.mohre.gov.ae/en/services/work-permits-for-dependents-sponsored-by-family-members-2022 -> `sources/mohre-work-permit-family-sponsored.html` (live; I used a March 2026 Wayback copy).
- MOHRE freelance permit service page (URL not found; search "Freelance permit" on mohre.gov.ae services directory) -> `sources/mohre-freelance-permit.html`: fee and conditions.
- https://www.epassport.gov.bd/instructions/passport-fees -> `sources/dip-epassport-fees.html` (403): current mission fees for child passports.
- https://bcgdubai.gov.bd/wp-content/uploads/2024/09/Passport-Fee-English.jpg -> `sources/bcgdubai-passport-fee-english.jpg`: Dubai Consulate passport fee table (image).
- https://www.linkedin.com/posts/legaltalkswithaminul_uaevisa-bangladeshtouae-rakez-activity-7453327735722127360-1sU5 -> `sources/guide-legaltalks-rakez-partner-visa-bd.html`: practitioner says partner/transfer routes restricted for Bangladeshis.
- https://www.state.gov/reports/2024-country-reports-on-human-rights-practices/united-arab-emirates/ (403) -> `sources/usstate-hrr-uae-2024.html`: newer asylum text.
- https://www.unhcr.org/us/where-we-work/countries/united-arab-emirates (403) -> `sources/unhcr-uae-country.html`: UNHCR Abu Dhabi contact.
- https://smartservices.icp.gov.ae (golden/green "About" and eligibility pages, JS-only) -> screenshot of category conditions.
- Facebook screenshots that would help: Bangladesh Embassy Abu Dhabi and Dubai Consulate posts on family/student visa status for Bangladeshis (2025-2026); Ministry of Expatriates' Welfare press release of 18 Aug 2026 meeting with the CIP Business Association.


RATE FACTS: G0001, G0002 (also G0004); AED1 = about Tk 34 on 8 November 2026 (Bangladesh Bank USD = Tk 124.35 [G0001]; CBUAE USD = AED 3.6725 [G0002]; 124.35 / 3.6725 = Tk 33.86; CBUAE's own Taka rate 0.029486 gives Tk 33.91 [G0004]). Cite as "AED1 = about Tk 34 [G0001, G0002]".

# Agent G draft: money home, going home without papers, death/injury (Bangladesh side), coming home (UAE side), contacts

Tk figures below use AED1 = about Tk 34 [G0001, G0002].

## Sending money home

**Use a bank or a licensed exchange house, never hundi** (sending through an unlicensed agent) [G0051]. Bangladesh's Financial Intelligence Unit (BFIU) froze about 55,000 mobile-money (MFS) accounts linked to digital hundi and online gambling in 2026 and decided in August 2026 to freeze about 14,000 more [G0126]; money in a frozen account can't be cashed out [G0125].

The UAE was Bangladesh's third-largest source of remittances in July-September 2026, USD 777 million, after Saudi Arabia and the UK [G0099]. It sent USD 4,636 million in FY2023-24, USD 4,168 million in FY2024-25 and USD 4,584 million in FY2025-26, out of USD 35,589 million from all countries in FY2025-26 [G0097, G0098]. Sending from the UAE is the most expensive of Bangladesh's ten main corridors: 2.92% of the amount on average in April-June 2026, and 6.49% for transfers up to USD 200 (about AED 735) [G0100, G0002].

You'll need:
- your passport and Emirates ID (the UAE's resident identity card) for the exchange house;
- the receiver's bKash (or Nagad) number and their full name exactly as registered, or their bank account number, bank and branch [G0122].

1. **Check the licence.** Exchange houses must be licensed by the Central Bank of the UAE (CBUAE). Open centralbank.ae/en/licensing, "Search Financial Institutions", choose licence type "Exchange Business" and look for the name on the shop's sign [G0120]. Licensed examples include Al Ansari Exchange, Lulu International Exchange, Al Fardan Exchange, Al Rostamani International Exchange, Sharaf Exchange, Index Exchange, GCC Exchange, Al Ahalia Money Exchange Bureau, Al Dahab Exchange and Unimoni Exchange [G0120]. A shop or person not on the register is not licensed.
2. **Send.** For bKash, bKash lists these UAE partners: Al Ahalia Exchange, Al Ansari, Al Dahab Exchange, Al Fardan Exchange, Al Rostamani, GCC Remit, Index Exchange, Ria, e&money, Wise, Worldwide CE, Western Union, Taptap Send, MoneyGram and Remitly [G0121]. At the counter give the bKash number and registered name and hand over the cash; up to Tk 2.5 lakh per transfer, any number of times [G0122]. Keep the receipt.
3. **The family** gets the government's 2.5% cash incentive on money sent through legal channels, kept in the FY2026-27 budget [G0101], and can cash out bKash remittance at Tk 7 per thousand at BRAC Bank, City Bank and Q-Cash ATMs [G0122].

> **Need to know**
> - What reference number does a UAE exchange-house receipt carry, and how does the family trace a transfer that hasn't arrived?
> - Where does a worker in the UAE complain when a licensed exchange house loses or delays a transfer (CBUAE's consumer complaint channel)?
> - Can a worker whose residence visa has expired or been cancelled still send money legally from a UAE exchange house without a valid Emirates ID?

**Saving at home: the Wage Earner Development Bond.** A 5-year government bond for workers abroad, bought in taka or foreign currency in the worker's own name or a named beneficiary in Bangladesh, at authorised-dealer bank branches in Bangladesh or at Bangladeshi banks' branches and exchange houses abroad [G0123]. Denominations run from Tk 25,000 to Tk 50 lakh, with no upper limit on purchases [G0123]. It pays 12% simple profit at maturity on holdings up to Tk 15 lakh (11% for Tk 15-30 lakh, 10% for Tk 30-50 lakh, 9% above), paid every six months; the money and profit are income-tax free, you can borrow against it, name a nominee, and take the principal back in US dollars [G0124].

> **Need to know**
> - Which UAE exchange houses sell the Wage Earner Development Bond, and what papers does a worker need there?

## Going home without valid papers

If your visa or residence permit has expired or been cancelled, the UAE fines you AED 50 (about Tk 1,700) for every day you stay after the grace period [G0066, G0069]. The grace period after a residence permit expires or is cancelled is 30 days for most workers, 60 days for permits held with a guarantor or host, 90 days for skilled workers at levels 1-3, and 180 days for Golden, Green and Blue residence holders [G0067]. To leave you pay the fines, get an exit (departure) permit, and fly out within 7 days [G0060, G0061]. Not paying the fine can bring up to 3 months' prison or a fine of up to AED 4,000 (about Tk 1.36 lakh), and the court may deport you [G0109].

No amnesty (a period when fines are waived) is open in November 2026. The last general amnesty ran from 1 September to 31 December 2024 [G0092, G0093]; about 50,000 Bangladeshis regularised and more than 5,500 went home on travel permits without a ban [G0094]. In 2026 ICP (the Federal Authority for Identity, Citizenship, Customs and Port Security, the federal immigration authority) waived only fines run up from 28 February 2026 by people stranded by the regional airspace closures, then gave them until 9 July 2026 to leave or regularise [G0070, G0071, G0072].

> **Need to know**
> - Is a new UAE amnesty expected for 2026-2027, as Bangladeshi missions have asked?

### Step 1: Get a passport or outpass

With a valid passport, go to Step 2. If your passport has expired, been lost, damaged or mutilated, or you have lived in the UAE illegally for a long time, get a Travel Permit (an "outpass", a one-way document home) from the Bangladesh mission [G0073]. It is valid 3 months [G0074]. The Dubai Consulate issued 2,915 travel permits from January to June 2026 [G0082].

Only holders of a Bangladeshi machine-readable passport (MRP) or e-passport can get one; the Consulate can't issue it on an old hand-written passport [G0075].

You'll need [G0076]:
- the Travel Permit (Out Pass) application form (download it from bcgdubai.gov.bd, "Download Forms") [G0085];
- a photocopy of your expired MRP;
- if the passport is lost, the police lost report (see "If you lose your passport") and a photocopy of the lost passport;
- two passport-size colour photos;
- your email address and phone number written on the form;
- your Emirates ID, if you have one.

1. Go yourself to the Consulate General of Bangladesh in Dubai, Villa No. 36 & 145, Abdulla Hussain Al Malik Villa, 123/3 Street, Abu Hail Road, Al Wuheida, Deira [G0078]. Hand in the papers at counter No. 19, Monday to Thursday 9 am to 3 pm, Friday from 9 am (the Consulate closes at 11:30 am on Fridays) [G0111, G0080].
2. Pay AED 60 (about Tk 2,040) in cash at counter 19; it is not refunded if refused [G0077].
3. Collect it the same day: Monday to Thursday 3 to 4 pm, Friday 12 to 12:30 pm [G0111].

The Embassy in Abu Dhabi also issues travel permits (address and hours in "Contacts") [G0112].

> **Need to know**
> - What does the Abu Dhabi Embassy charge for a travel permit, and is it also same-day?
> - How does a worker who never had an MRP or e-passport (only a hand-written passport, or no passport at all) prove citizenship to get a travel permit?

**If it fails:** Dubai Consulate labour welfare helplines +971 50 816 8253 and +971 50 816 8363 (WhatsApp text, office hours), consular and passport +971 50 505 5834 [G0079]; Abu Dhabi Embassy labour wing +971 2 445 8182 or labourwingauh@gmail.com [G0089].

### Step 2: Settle fines and status

1. **Check your fines.** In Dubai use GDRFA's free Fines Inquiry Service, gdrfad.gov.ae/en/fines-inquiry-service, with your passport number (GDRFA is the General Directorate of Residency and Foreigners Affairs, Dubai's immigration office) [G0136]. For any emirate, call ICP on 600522222 (+971600522222 from abroad) [G0137].
2. **Check for a travel ban.** A court case or unpaid debt can stop you at the airport even after the fines are paid. Dubai Police's free "Circulars and travel bans" service on the Dubai Police app or website (log in with UAE Pass, the national digital ID), at smart police stations or at police stations shows at once whether a financial-case circular or travel ban exists [G0104].
3. **Check for a labour ban or absconding report.** Call MOHRE (the Ministry of Human Resources and Emiratisation) on 600590000, 8 am to 8 pm [G0128]. A proven "work abandonment" report (the official name for an absconding report) bars a new work permit for a year, counted from the day you leave [G0127, G0128]. An employer who reports that a worker has left work is exempt from the AED 50,000 fine for employing or harbouring violators [G0108].
4. **Pay the fines.** Online on ICP's smart services site or app (UAE Pass login, plus an AED 100 smart-services fee), or at an ICP or GDRFA service centre [G0069]. After paying you must either regularise (get a new visa) or leave [G0069].

> **Need to know**
> - Is the Abu Dhabi Judicial Department's Estafser service (adjd.gov.ae) the way to check an Abu Dhabi travel ban, and does it work without UAE Pass?
> - Can a worker with no UAE Pass (because their Emirates ID has been cancelled) check and pay fines online, or only at a centre?
> - Who pays the fines when the employer let the visa lapse: can a worker claim them from the employer at MOHRE?

### Step 3: Leave

You'll need [G0063, G0114]:
- your passport, or the travel permit from Step 1;
- a personal photo;
- a confirmed air ticket dated within 7 days;
- the fine payment.

1. **Get the exit permit.** Outside Dubai, apply on ICP's smart services (UAE Pass) or at an ICP Customer Happiness Centre; AED 200 plus AED 100 smart-services fee (about Tk 10,200); ready in 2 days [G0063]. In Dubai, go yourself to an Amer centre, GDRFA's Public Services Section in Al Aweer, the Terminal 3 airport service centre or Hatta port; violators also have an eye-print recorded; AED 241 (about Tk 8,200); about 48 hours [G0114].
2. **Fly within 7 days** of the permit's issue. If you miss it, the permit must be cancelled and a new one applied for, and from the 8th day after it expires you are fined AED 50 a day again [G0061, G0064].

> **Need to know**
> - Can a violator pay fines and get the exit permit at the airport on the day of travel, outside Dubai's Terminal 3 centre?

### If you lose your passport

You'll need [G0083, G0113]:
- a copy of the lost passport (keep a photo of the data page on your phone);
- your NID (national ID card) or 17-digit online birth registration certificate [G0083];
- your Emirates ID and UAE visa copy, if you have them [G0083].

1. **Report the loss to the police.** In Dubai, use "Report Lost Item" on the Dubai Police app or website (UAE Pass) or at a police station, 7:30 am to 10 pm [G0113]. The Certificate of Loss costs AED 50 plus AED 20 in fees (about Tk 2,400), AED 100 more at a police station, takes up to 3 working days, is emailed to you and is valid one month [G0113].
2. **If you want to stay and work:** apply for a new e-passport. Fill the form at epassport.gov.bd, book the appointment, then go yourself to the Consulate with the printed form, the police report, a copy of the old passport, your NID or birth certificate and your Emirates ID and visa; pay at counters 1-3 and give fingerprints and iris scan in Room 23 [G0083, G0084]. It takes 4-6 weeks (urgent about 15 days) if no police verification is needed and your data match your NID [G0084].
3. **If you are going home:** get a travel permit instead (Step 1); ICP issues the exit permit on the consulate's travel pass and the police report [G0062].

> **Need to know**
> - What do the Dubai Consulate and Abu Dhabi Embassy charge for a regular and an urgent e-passport in 2026?
> - How does a worker outside Dubai get the police lost report (Abu Dhabi, Sharjah and the northern emirates)?

### If you are detained

The UAE can hold a person under a deportation order for up to 30 days, extendable once [G0106]. The deportee's own money pays for the deportation, or the employer if it broke the law, otherwise the state [G0107]. GDRFA's centre in Al Aweer (Dubai) handles residency violators, including issuing exit permits with an eye-print [G0114].

The Abu Dhabi Embassy's labour wing says it regularly visits jails and the deportation centre to identify Bangladeshis, issues travel permits to them, and gives air tickets or money to workers in distress [G0112]. The Consulate says WEWB members (see "If a worker dies") get help to be freed and brought home [G0131]. After 57 Bangladeshis were sentenced for street protests in July 2024 (three to life), the UAE President pardoned them in September 2024 and ordered them deported [N0033, N0035].

What to do: give the police or centre the Consulate's or Embassy's number and ask them to inform the mission; the family can ask the Welfare Board for legal help abroad (next step) [G0027].

> **Need to know**
> - Where is the deportation centre for Abu Dhabi and the northern emirates, and can family visit?
> - Who buys the ticket home for a detained worker with no money: the employer, the mission or the deportation centre?
> - How long does a Bangladeshi held for overstay usually wait in Al Aweer before the flight?

### If your family in Bangladesh asks for help

A close relative can ask the Ministry of Expatriates' Welfare and Overseas Employment to help bring a worker home; it acts through the mission, the Welfare Board or BMET, free, within 7 working days [G0039].

You'll need [G0039]:
- proof the person is a migrant worker (passport copy, visa, Emirates ID);
- their workplace and home address in the UAE;
- the recruiting agency's name and address;
- the employer's mobile number.

1. Call the Probashi call centre (run by the Wage Earners' Welfare Board, WEWB), 16135 free, or +8809610102030 from abroad, 24 hours [G0036].
2. For legal help abroad (a case, detention, unpaid dues), apply to the Welfare Board on myGov (mygov.bd), at the Board (Probashi Kallyan Bhaban, 71-72 Eskaton Garden, Ramna, Dhaka), or through the expatriate welfare branch of the Deputy Commissioner's office or the DEMO (District Employment and Manpower Office); the Board writes to the labour wing in 1-2 days, which takes about 15 working days; free [G0026, G0027, G0057]. This needs BMET clearance or Board membership [G0026].
3. No reply: the Ministry's grievance officer, Joint Secretary (Admin and Finance), 02-41030224, 01712992086, adsadmin@probashi.gov.bd, has 30 working days [G0040].

### Bans after you leave

A person who has been deported can't return to the UAE without the permission of ICP's chairman [G0105]. Under past amnesties, people who left on an amnesty exit permit had no "entry ban stamp" [G0138], but people who had entered the UAE illegally left with a two-year entry ban [G0139]. A proven work abandonment report bars a new work permit for one year from the day you leave; skilled workers and Golden visa holders are exempt [G0127, G0128]. Forging or using a forged visa or residence permit can bring up to 10 years' prison and deportation [G0110].

To check a labour ban, call MOHRE on 600590000; to contest it, send a grievance with documents through MOHRE's channels [G0128].

> **Need to know**
> - Does a worker who pays overstay fines and leaves on an ordinary exit permit (outside an amnesty) get an entry ban, and for how long?
> - How can a worker in Bangladesh check whether they have a UAE entry ban before paying for a new visa?
> - How does a deportee apply for the ICP chairman's permission to return, and has any Bangladeshi worker succeeded?

## If a worker dies, is injured or loses the job

(Bangladesh-side grants and repatriation only; agent L writes the UAE labour-law side: employer's duties, compensation, gratuity.)

In Bangladesh the Wage Earners' Welfare Board (the Welfare Board; Probashi Kallyan Bhaban, 71-72 Eskaton Garden, Ramna, Dhaka) pays grants and handles the insurance bought at BMET clearance [G0057, G0030]. Most grants need either BMET emigration clearance (the smart card) or Welfare Board membership [G0005, G0014]. Many Bangladeshis in the UAE went on visit visas and never got clearance; they can buy membership in the UAE.

**Get Welfare Board membership if you have no BMET card.** Any Bangladeshi aged 18 to 65 in the UAE without a BMET card can register for membership (the "Probashi Kallyan Card") [G0129]. The Dubai Consulate issued 5,028 cards from January to June 2026 [G0082].

You'll need [G0130]:
- your Bangladeshi passport;
- your UAE visa;
- your Emirates ID;
- one colour passport-size photo;
- your nominee's details.

1. Apply online at portal.wewb.gov.bd and print the form [G0133, G0130].
2. Hand it in with the papers and AED 200 (about Tk 6,800, the equivalent of Tk 6,500, including life insurance) in cash at the Consulate's service centre, Foshwa Global, No. 3 Rim Residency, Umm Hurair, Karama, Dubai (+971 4 570 1648, WhatsApp +971 50 729 2294); keep the receipt [G0130, G0133].
3. Collect the card from the centre after at least 3 working days [G0130]. If you lose it, download it again from wewb.gov.bd with your passport number [G0132].

> **Need to know**
> - How long does Welfare Board membership bought in the UAE last, and how is it renewed?
> - Does the Tk 3 lakh death grant cover a member who went to the UAE on a visit visa, given the Consulate's page says it is for workers who went legally [G0131] while the Board says clearance or membership [G0005]?

### If you are injured or fall ill

1. **Going home injured.** On your or your family's application, with proof of clearance or membership and a passport copy, the Welfare Board asks the mission to bring you home [G0017]. The Board's ambulance at Dhaka and Chattogram airports is free on request (Dhaka desk +8802 8901040, 01404 413388) [G0013].
2. **Treatment money in Bangladesh.** A returnee with clearance or membership who is injured, sick or disabled can get up to Tk 2 lakh; the family applies within 1 year of return through the Board's web portal, the district probashi kallyan (migrant welfare) centre or the Board [G0014, G0016].

   You'll need [G0016]:
   - medical reports and prescriptions;
   - a bank statement;
   - a passport copy and a copy of its arrival stamp;
   - proof of clearance or membership;
   - one 6R (6 by 8 inch) colour photo of the worker.

   A Board committee checks the case by WhatsApp video call; free; up to 60 working days after all papers are in [G0014, G0016].
3. **Insurance.** For workers who left with clearance from 1 January 2023, it pays Tk 10 lakh for total permanent disability and 10% to 90% of that for partial permanent disability [G0018, G0041]; claim through the Board (see "Claiming the insurance").

> **Need to know**
> - Is the treatment grant Tk 2 lakh (Welfare Board [G0014]) or Tk 1 lakh (Dubai Consulate's page [G0131])?

### If a worker dies

These steps are for the family in Bangladesh. The Dubai Consulate handled 213 body repatriations from January to June 2026 [G0082].

1. **Ask the Welfare Board to bring the body home.** Call 16135 (from abroad +8809610102030) [G0036]. Then apply in one of these ways, even if the worker had no clearance or membership:
   - on myGov, service "Application to bring home a migrant worker's body", with a myGov account (register with your mobile number at idp-v2.live.mygov.bd/registration), the worker's passport and any clearance or membership; a tracking number comes by SMS; free; up to 35 working days [G0022, G0023, G0024]; or
   - to the Ministry of Expatriates' Welfare, aswelfare@probashi.gov.bd, which also handles irregular and undocumented workers, describing what happened and the cause of death, with proof the person was a migrant worker (passport, work permit, BMET smart card, Emirates ID) and the death certificate; free; 7 working days [G0038].
2. **Home or burial in the UAE.** The Board passes the family's choice to the mission [G0019, G0020]. For burial in the UAE, apply on myGov, "Application for permission to bury a migrant worker's body in the destination country", with the worker's passport or visa copy, any clearance or membership, the district office's investigation report and a certificate signed by all heirs on the union parishad (rural council) chairman's letterhead; free; 3 working days [G0021]. The Abu Dhabi Embassy needs the family's no-objection certificate sent through the Welfare Board or the foreign ministry [G0091].
3. **The UAE side.** The Consulate issues a free No Objection Certificate (NOC) for the body the same day, Room 14, 9 am to 3 pm Monday to Thursday, 9 to 11:30 am Friday; hotline +971 50 816 8253 (WhatsApp only) [G0081]. The employer, sponsor, a colleague or a relative in the UAE applies with [G0081]:
   - the death certificate and the deceased's passport (originals and copies) and Emirates ID copy;
   - the death notification or medical report;
   - for an accidental death, the police or autopsy report;
   - the passport or Emirates ID copy and phone number of the person accompanying the body;
   - the family's contacts in Bangladesh, and the name and number of the person receiving the body at the airport;
   - proof that all money owed to the worker has been paid to the nominee.

   In Abu Dhabi the Embassy also asks for the cargo booking, the final settlement from the employer by cash or cheque in the Embassy's name (or sent to the heirs with the remittance copy), the NID copy of the airport receiver, and a Welfare Board letter or the heirs' application recommended by the local chairman [G0091]. The Board forwards the family's request within 3-5 working days and the labour wing takes about 30 [G0025].

   4. **At the airport.** The Board's desk gives a Tk 35,000 cheque for transport and burial, collectable within 3 months, and a free ambulance [G0011, G0013]. You'll need [G0012]:
   - the worker's passport copy;
   - a heirship (warish) certificate from the union parishad chairman, mayor or city councillor;
   - the NID of the wife, father or mother;
   - the death certificate;
   - the NOC;
   - the original air waybill;
   - proof of clearance or membership, if any.
5. **The Tk 3 lakh Welfare Board grant,** for the family of a worker with clearance or membership who died in the UAE, the country of the clearance [G0005, G0006]. If the family took the airport cheque, no application is needed; after burial in the UAE, apply within 1 year of the death to the Board's Director General or through the district office [G0007]. It goes to the spouse, children and parents; for an unmarried worker with no living parents, to full siblings [G0008].

   You'll need [G0009]:
   - a family-members certificate on the letterhead of the union parishad chairman, mayor or city councillor, countersigned by the UNO (Upazila Nirbahi Officer) or, in a city corporation, the regional executive officer;
   - an indemnity, undertaking and authorisation on Tk 400 non-judicial stamp paper, countersigned the same way (samples on wewb.gov.bd);
   - the NOC or death certificate copy;
   - a bank certificate or original statement for the receiver's account with the routing number;
   - each family member's colour photo, attested by the chairman and the district welfare centre;
   - the worker's passport copy.

   Paid by bank transfer (BEFTN) with an SMS, within 60 working days of all papers reaching the Board [G0010, G0034].
6. **The insurance:** Tk 10 lakh for a death within 5 years of the smart card date, for workers who left with clearance on or after 1 January 2023 [G0018, G0031].

   > **Need to know**
   > - Are workers who left between 1 January and 11 March 2023 covered, since BMET's leaflet gives the start as 12 March 2023 [G0042]?
   > - Does Welfare Board membership bought in the UAE include the Tk 10 lakh death insurance, or a different sum?

7. **UAE compensation and dues.** When the mission reports that compensation, unpaid wages or end-of-service benefits may be due, the Welfare Board asks the family for a power of attorney and papers (with free help from its legal cell), sends them to the mission and follows the case; it pays the heirs within 60 working days of having the papers and the money [G0028, G0029]. The Abu Dhabi labour wing recovers death compensation from courts, companies and sponsors [G0112]. The family can also write to the Ministry, aswelfare@probashi.gov.bd, which writes to the mission and the Board within 7 working days [G0037].

   > **Need to know**
   > - Is any compensation paid to the families of Bangladeshis killed in the UAE by the 2026 Iranian strikes, such as the water-delivery driver Ahmad Ali [G0135]?

### If you lose the job

**Insurance:** coming home within 6 months of going, after losing the job, pays Tk 50,000 to workers who left with clearance from 1 January 2023 [G0018, G0033]; see "Claiming the insurance".

### Claiming the insurance

1. **Call 16135** (+8809610102030 from abroad); the Welfare Board helps claim from Jiban Bima Corporation, the state life insurer [G0030, G0036].
2. **Apply.** For a death, nothing is needed if the body came through the airport desk; after burial abroad or a death after return, apply at portal.wewb.gov.bd or at the Board [G0031]. For disability or a lost job, apply to the Board's welfare section [G0032, G0033]:
   - disability: Deputy Director, +88 02 48317085, 01321-158354, dd.welfare2@wewb.gov.bd;
   - lost job: Assistant Director, 01712-107301, jahanwewb@gmail.com.
3. **You'll need:** proof of clearance or membership and a passport copy, with departure and arrival stamps for a lost job; for disability, medical papers and a 6R colour photo of the disabled part of the body [G0030, G0032, G0033]. Free; 30 working days [G0031, G0032, G0033].
4. **If it stalls,** complain in this order [G0035]:
   1. the Board's grievance officer, +88 02 55138267, 01684-501891, azizwelfare@gmail.com (30 working days);
   2. the Ministry's Joint Secretary (Administration), +88 02 41030261, jsadmin@probashi.gov.bd (20 working days);
   3. grs.gov.bd, the Cabinet Division's grievance system.

## Coming home

(UAE exit side and baggage; agent B writes the Bangladesh reintegration side.)

- **Cancel the visa properly.** The employer cancels the residence permit through ICP (AED 50 application plus AED 100 smart-services fee); a domestic worker's residence is cancelled through MOHRE or the Domestic Work Bundle [G0068]. Get end-of-service pay before you sign (agent L's sections). The Dubai Consulate has a "Final Settlement" form and a complaint format on bcgdubai.gov.bd, "Download Forms" [G0085]. After cancellation you have the grace period in "Going home without valid papers" to leave [G0067].
- **Check for bans before you buy the ticket:** travel bans (Dubai Police service, Step 2 above) and fines [G0104, G0136].
- **Leaving the UAE with cash.** Declare more than AED 60,000 (about Tk 20.4 lakh) in cash, other currencies, cheques, gold or precious stones to ICP, online at declare.customs.ae or on the Afseh app [G0103].
- **Customs in Bangladesh.**
  - Duty-free: 65 kg of baggage, 2 used phones and 1 new phone a year, and once a year, if declared, 100 g of gold or 200 g of silver jewellery (no more than 12 pieces of one type) [G0043, G0044, G0045].
  - Once a year you may bring a declared gold bar up to 117 g (10 tola; duty Tk 5,000 per tola) or a silver bar up to 234 g; a bigger or hidden bar is confiscated [G0046, G0048].
  - No alcohol on a Bangladeshi passport [G0047].
  - Declare foreign currency over USD 10,000 on the FMJ form [G0049].
  - Customs emergency line: +88 01319-056591 [G0050].
- **Airport help.** The Welfare Board's desks at Dhaka, Chattogram and Sylhet airports give food and water to people returning from jail or on an outpass, money to workers coming back from war, disaster or lay-off, help with customs and lost luggage, and take complaints of abuse or cheating [G0052, G0053]. Women returning within a year after abuse or fraud get Tk 5,000 cash [G0054]. Dhaka desk +8802 8901040, 01404 413388; Chattogram 01913631797; Sylhet 01558277904 [G0013, G0056].
- **A place to stay.** The Wage Earners' Centre (Lonjonipara, Borua, Khilkhet, Dhaka-1229, near Shahjalal airport): Tk 100 admission, Tk 200 a night; book at wec.wewb.gov.bd or in person with proof of clearance or membership, a passport copy and the ticket; 01310 350555, 01754 715720 (24 hours) [G0055]. The Probashi Lounge at Shahjalal airport gives free wifi and phone calls and food at up to 30% off with proof of clearance or membership [G0058].
- **If your family is threatened or its property seized,** apply to the Welfare Board (directly, through the Deputy Commissioner's expatriate welfare branch or the DEMO); it writes to the local administration [G0059].

> **Need to know**
> - Does Dhaka airport immigration treat a returnee on a travel permit (outpass) differently, and do they keep the permit?

## Contacts (UAE side)

- **Bangladesh Embassy, Abu Dhabi:** Villa No. 46, 48, Sector-19, Zone-W31, Al Jawwalah Street, Al Saadah Area, P.O. Box 2504; +971 2 446 5100; mission.abudhabi@mofa.gov.bd; facebook.com/BangladeshEmbassyAbuDhabi [G0087]. Consular and welfare applications Monday to Thursday 9 am to 3 pm (break 1 to 2 pm), Friday 8:30 to 11 am [G0088].
  - Labour wing: Counsellor (Labour) Mohammad Ullah Khan, counselorabudhabi@probashi.gov.bd, +971 2 446 2745; First Secretary (Labour) Mohammad Ismail, fsabudhabi@probashi.gov.bd, +971 2 445 2216 [G0090]; Legal Officer Mohammed Rezaul Alam (ext. 331), Welfare Officer Mollah Osman Goni (ext. 209), labourwingauh@gmail.com, direct line +971 2 445 8182 [G0089].
- **Bangladesh Consulate General, Dubai:** Villa No. 36 & 145, Abdulla Hussain Al Malik Villa, 123/3 Street, Abu Hail Road, Al Wuheida, Deira; P.O. Box 4336; +971 4 238 8199, +971 4 265 1116; mission.dubai@mofa.gov.bd [G0078, G0079]. Monday to Thursday 9 am to 3:30 pm, Friday 9 to 11:30 am [G0080].
  - Helplines (WhatsApp text, office hours): labour welfare +971 50 816 8253, +971 50 816 8363; consular and passport +971 50 505 5834 [G0079].
  - Labour wing: Counsellor and Head of Chancery Md Abdus Salam, labour.dubai@mofa.gov.bd; First Secretary (Labour) Shahanaz Parvin, fslabour.dubai@mofa.gov.bd [G0086]; also counselordubai@probashi.gov.bd and fsdubai@probashi.gov.bd [G0134].
- **Probashi call centre (Welfare Board), 24 hours:** 16135 in Bangladesh, +8809610102030 from abroad [G0036].
- **Ministry of Expatriates' Welfare:** deaths and compensation aswelfare@probashi.gov.bd [G0037]; grievance officer adsadmin@probashi.gov.bd, 02-41030224 [G0040].
- **MOHRE (labour ministry):** 600590000, 8 am to 8 pm, several languages, for labour complaints and to check a labour ban [G0117, G0128].
- **ICP (federal immigration):** 600522222, +971600522222 from abroad; Street 12, near Al Forsan Resort, Abu Dhabi [G0137].
- **GDRFA Dubai (Amer call centre):** 8005111, amer@gdrfad.gov.ae [G0115].
- **Emergency:** police 999, ambulance 998, civil defence 997 [G0116]. Dubai Police non-emergency 901 [G0104].
- **Human trafficking:** EWAA (Abu Dhabi shelter) 800 SAVE (800 7283); National Committee to Combat Human Trafficking 8007283; Dubai Police Control Center of Human Trafficking +971 4 608 2347, htccc@dubaipolice.gov.ae [G0117, G0118]. Dubai Police's human rights directorate gives victims temporary shelter, temporary visas and air tickets home [G0118].
- **Dubai Foundation for Women and Children (shelter for women and children facing abuse or trafficking):** 800111, free, 24 hours [G0119].

---

## Notes (for notes.md)

**Searched:** bb.org.bd (exchange rate, remittance pages: captcha on curl, Firecrawl worked; PDFs fetch directly), centralbank.ae (rates, licensing register), icp.gov.ae (service pages, media centre), gdrfad.gov.ae, dubaipolice.gov.ae (JS: Firecrawl), u.ae (several moved pages 404), bcgdubai.gov.bd (the Dubai Consulate's real site; dubai.mofa.gov.bd is not used), abudhabi.mofa.gov.bd, wewb.gov.bd, mygov.bd, nationalsavings.gov.bd, NBR SRO 261 baggage rules, budget speech FY2026-27, Bangla news (Prothom Alo, Dhaka Times), Daily Star, TBS, Arab News.

**Method notes:**
- 54 Bangladesh-side facts (G0005-G0059) were re-logged from Malaysia's facts (WEWB, myGov, ministry charter, BMET leaflet, NBR baggage, HSIA customs) after re-fetching each page into the UAE folder; each note says "(re-logged from Malaysia Bxxxx)". The WEWB insurance image was re-fetched and the Malaysia hand transcription checked against the image.
- Bangladesh Bank PDFs: pdftotext -layout misaligns tables (UAE row picks up Malaysia's numbers). I added `.raw.txt` copies (pdftotext -raw) for bb-remittance-top30-countries, bb-remittance-monthly-report-2026-08 and bb-remittance-cost; quotes come from them. Remittance cost table checked visually.
- Firecrawl-saved files (excerpts, noted at foot of each): bb-exchange-rate-usd-2026-11-08, cbuae-exchange-rates-2026-11-06, dubaipolice-circulars-travel-bans-fc, dubaipolice-report-lost-item, cbuae-licensing-exchange-houses (from Firecrawl search result text; curl copy lacks the JS table), bkash-remittance-mts (UAE row only).
- ICP service pages show a site stamp "Last updated on 08/11/2026" (template meta 2024-12-11); content contains the 2025 grace-period tiers, so logged as verified 2026-11-08 with a note.
- The failed curl copy `bb-exchange-rate-2026-11-08` (captcha page) is in the fetch log; not used.
- Cited other agents' facts N0033, N0035 (WAM sentencing/pardon 2024) in "If you are detained". Agent V logged the official uaelegislation text of Decree-Law 29/2021 (V0173-V0177); I logged the GDRFA English translation (G0105-G0110). The lead may prefer V's ids.

**Conflicts:**
- Treatment aid: WEWB Tk 2 lakh (G0014, G0016) vs Dubai Consulate page Tk 1 lakh (G0131). Keep WEWB.
- Tk 3 lakh grant eligibility: WEWB "clearance or membership" (G0005) vs Consulate "workers who went legally" (G0131).
- Insurance start date: WEWB 1 January 2023 (G0018) vs BMET leaflet 12 March 2023 (G0042) (carried from Malaysia).
- 2024 amnesty dates: official 1 Sept-31 Oct 2024, extended to 31 Dec (G0092, G0093, G0138); Prothom Alo quotes the foreign ministry as "1 July-31 Dec" (G0096).
- Travel-permit Friday submission "9 am-11 pm" on the Consulate page (typo; service hours end 11:30 am) (G0111, G0080).
- WEWB membership fee: Tk 6,500 equivalent (G0133) = AED 200 at the Consulate (G0130); consistent at AED1 = Tk 34. Agent B has the Embassy's Sept 2026 fee notice (bdemb-abudhabi-wewb-fee-notice-2026-09: AED 200).

**Practice:**
- Dubai Consulate monthly numbers (June 2026: 861 travel permits, 35 bodies; Jan-Jun 2026: 2,915 travel permits, 213 bodies, 5,028 welfare cards) show the scale (G0082).
- 2024 amnesty: about 50,000 Bangladeshis regularised; 5,500+ left on travel permits with no ban; Dubai Consulate issued 4,840 travel permits, the Embassy 817 (G0094). UAE announced arrests and AED 50/day fines after it ended (G0095).
- 2026 regional war: Iranian strikes from 28 Feb 2026 closed airspace; ICP waived overstay fines (G0070, G0071, G0072); a Bangladeshi delivery driver was killed in the UAE (G0135).
- Remittance cost from the UAE is the highest of the main corridors (G0100).
- The budget (G0102) promises "Bangladesh Support Centres" at embassies for imprisoned and deceived workers and says reopening of the UAE labour market has begun: useful for Background.

**Logged but not used:** G0003 (CBUAE buy/sell peg band, redundant with G0002); G0042 (only in a Need to know); G0026's 20-day total; G0092 detail on the 2024 Amer AED 24 fee and 14-day exit permit (historic); G0093; G0102 (for Background); G0120 note on Al Ansari Digital Pay; G0123/G0124 partly. bb-invest-nrb.pdf fetched but text is garbled legacy font and outdated (bond rate from 2000): not logged. GDRFA "lifting the ban on a file" pages (gdrfad-ban-services, gdrfad-lift-ban-individuals) concern establishment/sponsor file blocks, not worker entry bans: not logged.

## Blocked pages (please download in a browser)

- https://www.wam.ae/en/article/c0scyu2-icp-grants-individuals-affected-exceptional -> `sources/wam-icp-grace-period-2026-06.html`: official text of the June-July 2026 overstay grace period (currently only EY, G0072). The curl copy saved under that name is an empty JS shell.
- https://u.ae/en/information-and-services/passports-and-traveling/preliminary-checks/check-if-you-have-a-travel-ban -> `sources/uae-portal-check-travel-ban.html`: official travel-ban checking guide (404 to scripts; the page may have moved: search u.ae for "travel ban").
- https://www.adjd.gov.ae/sites/eServices/EN/Pages/Estafser.aspx -> `sources/adjd-estafser.html`: Abu Dhabi Judicial Department's Estafser travel-ban/case inquiry (JS-only; curl copy empty). Needed to cite the Abu Dhabi check in Step 2.
- https://gulfnews.com/uae/thousands-use-estafser-to-check-uae-travel-bans-and-legal-cases-in-minutes-1.500130833 -> `sources/news-gulfnews-estafser-travel-ban-2025-05.html` (fetch failed).
- https://en.prothomalo.com/bangladesh/ms35nsib27 -> `sources/news-prothomalo-bodies-return-2026-10.html` (fetch failed; bodies repatriation practice).
- Abu Dhabi Embassy "MRP Against Lost Passport" and travel-permit fee pages: menu items with no working static link found; a screenshot of the Embassy's out-pass fee and documents would close the Step 1 gap.

**Facebook screenshots that would help:** Consulate General Dubai (facebook.com/cgbduae) and Embassy Abu Dhabi (facebook.com/BangladeshEmbassyAbuDhabi) posts on: current travel-permit fees and processing; any 2026 amnesty or fine-waiver announcement; deportation-centre visits; e-passport fee table.


# L findings: company worker's life and problems in the UAE

Agent L. Fact prefix L (L0001-L0253). Also cites agent G (G0002, G0060, G0061, G0066, G0067, G0069, G0076, G0081, G0118) and agent N (N00xx) facts where they already cover a point. AED1 = about Tk 34 [G0002].

---

## Work visa: company worker

### Your rights at work

Federal Decree-Law 33 of 2021 (the UAE Labour Law, in force since 2 February 2022, amended 2024) and its Executive Regulations (Cabinet Resolution 1 of 2022) cover private-sector workers; domestic workers have their own law. MOHRE (the Ministry of Human Resources and Emiratisation) enforces them. Free zones such as JAFZA have their own rules for some matters (see Notes).

**Contract.** Contracts are fixed-term and renewable by agreement; there are no open-ended contracts [L0058]. You get one of the two copies [L0056], in Arabic plus a language you understand (Arabic prevails in a dispute) [L0057]. Its terms must match the MOHRE job offer you signed in Bangladesh [L0052]. MOHRE job offer forms carry a barcode serial number you can check on 600590000, the MOHRE website or app [L0054]. MOHRE's "Know Your Rights" guide exists in Bengali [L0053].

**No fees, no passport-keeping.** Recruitment, travel and residence-permit costs are the employer's [L0051]; charging workers recruitment fees is illegal [L0048]. The employer may not keep your passport or other official documents, and you need no employer permission to leave the country [L0049, L0050]. Forced work, threats, sexual harassment, bullying and violence are banned [L0059, L0060].

**Hours and overtime.**
- 8 hours a day or 48 a week; 2 hours less in Ramadan [L0001, L0007].
- After 5 hours in a row, breaks totalling at least 1 hour, unpaid [L0002].
- Overtime at most 2 hours a day and 144 hours in total every 3 weeks [L0003, L0006]; paid at the basic hourly rate plus 25%, or plus 50% between 10 pm and 4 am (not for shift workers) [L0004].
- Work on your rest day or a public holiday: another day off, or the day's pay plus at least 50% of basic [L0005, L0011].

**Summer midday break.** No work in direct sun or open places from 12:30 pm to 3 pm, 15 June to 15 September every year [L0025]. Exempt: asphalt or concrete work that cannot wait, urgent public repairs, and permit-controlled work [L0026]. Employers must give shade, cooling, drinking water and first aid [L0028]. The fine is AED 5,000 per worker, up to AED 50,000 [L0027]. Report a breach on 600590000, the MOHRE app or website ("Add Complaint") [L0029]; anyone can also report heat-rule, overtime, accommodation and safety breaches through MOHRE's community reporting service or 80084 [L0177].

**Rest and holidays.** At least one paid rest day a week [L0008]. Paid public holidays: 1 January; Eid Al Fitr 1-3 Shawwal; Arafah Day; Eid Al Adha 10-12 Dhu al-Hijjah; Hijri New Year; the Prophet's birthday; National Day 2-3 December; Islamic dates follow moon sighting [L0009, L0010].

**Leave.**
- Annual: 30 days a year after one year; 2 days a month between 6 and 12 months [L0012]. The employer sets dates with one month's notice [L0013] and may not stop you taking it for more than two years in a row [L0014]. Unused leave is paid when you leave [L0015].
- Sick: none paid during probation [L0018]; afterwards up to 90 days a year, 15 full pay, 30 half pay, 45 unpaid [L0016, L0017]. Tell the employer within 3 days with a medical report [L0019]. You cannot be dismissed or given notice while on sick leave [L0020].
- Bereavement 5 days (spouse) or 3 days (parent, child, sibling, grandparent, grandchild) [L0021]; parental 5 working days within 6 months of a birth [L0024]; maternity 60 days (45 full, 15 half pay) [L0023]; Hajj up to 30 days unpaid, once per employer [L0022].

**Pay.** There is no minimum wage [L0040]. Wages must go through the Wage Protection System (WPS: MOHRE's electronic record of every salary paid through a bank, exchange house or approved payroll card) [L0032, L0033]. Since Ministerial Resolution 340 of 2026, last month's wage is due on the 1st of each month, and at least 85% of the total due must be paid on time [L0030, L0031]. What happens to a late employer is under If you aren't paid.

**Deductions.** Only in the cases the law lists [L0042]:
- loan repayments, with your written consent and no interest [L0080];
- overpaid wages, up to 20% of the wage [L0043];
- disciplinary fines under a MOHRE-approved list, up to 5% [L0044];
- damage you caused, up to 5 days' wage a month (more only by court order) [L0045];
- court debts, up to a quarter of the wage [L0046].

All deductions together may never pass 50% of the wage [L0047].

**Housing.** The employer must give licensed housing, or pay a housing allowance, or include it in the wage [L0062]; firms with 50 or more workers earning AED 1,500 a month or less must house them [L0061]. Standards:
- at least 3 square metres per person, 8 to 10 people per room at most [L0063, L0064];
- your own bed, side table and 2-metre lockable cupboard; no three-tier bunks [L0066, L0065];
- one toilet and one shower per 8 people [L0067];
- air-conditioning in every room [L0068].

> **Need to know**
> - Is there any limit on what an employer may charge for housing or food when housing is "included in the wage"?

**Health insurance.** The employer must insure you: since 1 January 2025 a policy is required before your residence permit is issued or renewed, in every emirate [L0070, L0071, L0075, L0076]. The cheapest approved package costs AED 320 a year, with no waiting period for chronic illness [L0072]; you pay at most AED 100 per outpatient visit (25% co-pay) and AED 500 per inpatient stay, capped at AED 1,000 a year [L0074, L0073]. In Dubai a worker earning AED 4,000 or less must get at least the Essential Benefits Plan, and the employer may not deduct the premium or cut pay for it [L0078, L0077].

> **Need to know**
> - Where does a worker complain if the employer deducts the health insurance premium outside Dubai?

**Unemployment insurance (ILOE, Involuntary Loss of Employment).** Compulsory for private-sector workers (not domestic workers, temporary-contract workers or under-18s) [L0081, L0082]. You pay it yourself: up to AED 5 a month if your basic salary is AED 16,000 or less [L0083], through iloe.ae, the ILOE app, Tasheel or Tawjeeh centres (MOHRE's typing and service centres), Al Ansari Exchange, bank apps, du or Etisalat SMS or BOTIM [L0096]. Not joining, or not paying, costs a AED 400 fine [L0095, L0094]; after 3 months unpaid the policy is cancelled [L0097]. Check your policy at iloe.ae: choose your sector, enter Emirates ID and mobile, take the OTP, then View Policy Details [L0098]. Claiming is under If a worker dies, is injured or loses the job.

**Worker protection insurance.** When hiring, the employer buys a policy (AED 137.50 for skilled, AED 180 for low-skilled workers) or lodges a AED 3,000 bank guarantee [L0174, L0175]. If the firm goes bankrupt or will not pay, it covers up to AED 20,000 per worker: up to the last 120 days' unpaid wages, gratuity, the ticket home, body repatriation and work-injury medical costs [L0172, L0173]. MOHRE draws on it in a proven collective dispute without the employer's consent [L0161].

> **Need to know**
> - How does an individual worker claim the worker protection insurance: through MOHRE only, or directly with the insurer?

**Gratuity (end-of-service pay).** After at least one year: 21 days' basic wage per year for the first five years, 30 days' per year after that, pro rata for part years, capped at two years' wage [L0106, L0107, L0108, L0109, L0112]. Basic wage only; housing and transport allowances do not count [L0110]. Unpaid absence does not count as service [L0112]; the employer may deduct money you owe [L0113].

### How long you can stay

**Two years at a time.** A work permit for a worker recruited from abroad lasts two years [L0218]; sponsored residence visas run 1, 2 or 3 years [L0217]. Renewal is the employer's job and needs the health insurance above [L0070].

**The 180-day rule.** A residence visa dies automatically after more than 180 days in a row outside the UAE [L0212]. Exceptions include residents sent abroad for treatment with a UAE-approved medical report, students and investors, plus anyone ICP (the Federal Authority for Identity, Citizenship, Customs and Port Security) exempts for a fee [L0213, L0214]; ICP issues a permit to stay outside more than six months for a valid reason [L0219]. If the visa lapsed while you were abroad for work, study or treatment, you can apply from abroad for an entry permit, with a reason, paying AED 100 per 30 days outside, and must enter within 30 days of approval; this is not available to Dubai residents [L0215, L0216].

> **Need to know**
> - Is there an upper age limit for a worker's work permit or residence renewal?

**When the job ends.** After cancellation you have a grace period, 30 days for ordinary workers, to change status or leave [G0067, L0127]; after that overstay costs AED 50 a day [G0066, G0069]. Leaving with unpaid fines needs ICP's departure permit, used within 7 days [G0060, G0061].

**No escape from a lapsed visa.** Since July 2026 many Bangladeshis' visas were cancelled while they were at home on leave (see Going home on leave) [N0001, N0005].

### What can get you jailed

**Papers and work.**
- Working for someone other than your sponsor or using a visa for another purpose: jail or a fine of at least AED 10,000, and deportation [L0225]. Whoever employs or houses you illegally pays AED 50,000, and you are deported [L0223, L0224].
- Forged visas or residence permits: up to 10 years and deportation [L0226]. Entering illegally: jail and deportation [L0227].
- Overstay is fined AED 50 a day [G0069]; not paying can bring up to 3 months' jail or a AED 4,000 fine and deportation [L0228].

**Protests.** Joining a public gathering of 5 or more people that disturbs order and not leaving when told: at least 1 year and AED 100,000; at least 5 years if it disrupts security, traffic or work [L0229, L0230]. Calling for unpermitted demonstrations online: jail and/or AED 200,000 to 1 million [L0242]. In July 2024, 57 Bangladeshis who protested in UAE streets got 10 years to life; they were pardoned and deported in September 2024 [N0033, N0035]. Recording and sharing videos of the gatherings counted against them [N0034]. Joining a strike or non-peaceful protest also cancels any ILOE claim [L0092].

**Social media and insults.**
- False news or rumours online: at least 1 year and AED 100,000 [L0241].
- Insulting someone online: jail and/or AED 250,000 to 500,000 [L0240].
- Photographing people without consent, or posting photos of accident victims: at least 6 months and/or AED 150,000 to 500,000 [L0243].
- Insulting someone by phone or in front of others: up to 6 months or AED 5,000; publicly, up to 1 year or AED 20,000 [L0238, L0239].

**Drugs.** Using drugs: at least 3 months' jail or a AED 20,000 to 100,000 fine for a first offence; a third offence at least 2 years and AED 100,000 [L0244, L0245]. Since December 2025, foreigners convicted of any narcotics offence must be deported after the sentence [L0246].

> **Need to know**
> - Does a positive blood or urine test alone, with drugs taken outside the UAE, count as "use" for prosecution?

**Alcohol.** Legal only where emirate rules allow [L0231]. Drinking in public or unlicensed places, or being drunk and causing trouble in public: up to 6 months and/or a fine [L0232]. Being drunk at work allows dismissal without notice [L0121].

**Relationships.** Consensual sex outside marriage: at least 6 months for both, but only on a complaint by a spouse or guardian [L0234, L0235]. Having a child outside marriage: at least 2 years for both unless they marry or acknowledge the child and get it papers [L0236].

**Other.** Begging: up to 3 months and AED 5,000 [L0233]. Assault causing under 20 days' injury: up to 1 year and AED 10,000 [L0237]. A bounced cheque for lack of funds has been a civil matter since January 2022, but an unpaid cheque debt can bring a travel ban and frozen assets, and a cheque on a closed account or with fraud is still criminal [L0247].

**After arrest.** The Bangladesh labour wing visits jails and deportation centres [L0207]. For a worker with no valid passport the Embassy issues a Travel Permit (out pass): a form giving passport number, sponsor, arrival date, cause of jail and sentence, with two photos [L0210, G0076]. Family can call the Abu Dhabi labour wing (+971 2 445 8182, labourwingauh@gmail.com) or the Dubai consulate's humanitarian line +971 56 847 1066 [L0203, L0202, L0206].

> **Need to know**
> - Does the Embassy or consulate get notified when a Bangladeshi is arrested, and how does a family find which jail holds a worker?

### If you aren't paid

**First collect proof.** Keep photos of your contract, MOHRE job offer, Emirates ID, passport, WPS bank or card statements and any written messages; MOHRE asks for documents supporting the claim, such as a resignation or dismissal letter [L0165]. Complain within 30 days of the breach [L0139].

**What MOHRE does to a late employer** (Resolution 340 of 2026) [L0034, L0035, L0036, L0037, L0038]:
- day 2 after the due date: alerts to the employer;
- day 5: no new work permits for it;
- day 16: labour disputes opened automatically for unpaid workers in firms of 25 or more;
- day 21: an executive (enforceable) order to pay in firms under 50 workers, attachment of assets and a travel ban on the person in charge; prosecution for repeat offenders with 50 or more.

**1. Confidential salary complaint.** "My Salary Complaint" on the MOHRE website or app does not tell the employer who complained; free [L0166]. Use it when pay is late but you want to keep the job.

**2. Formal labour complaint.**

You'll need [L0162, L0165]:
- passport number, name, date of birth, nationality;
- Emirates ID number;
- a mobile number for the OTP;
- any supporting papers.

1. Open "Register Labour Complaints - Private Sector Employees" on mohre.gov.ae or the MOHRE UAE app, or call 600590000 (24 hours; also WhatsApp) or the Labour Claims and Advisory Centre on 80084 (toll free) [L0162, L0055, L0149].
2. Enter your details and the employer's; confirm with the OTP sent by SMS or email [L0162].
3. MOHRE calls both sides to settle; if that fails it sets a meeting and texts you the date, then tries a second time [L0162, L0163].

What you get back: a settlement, or for claims under AED 50,000 a MOHRE decision that is enforceable like a court order [L0141]; either side can go to court within 15 working days, which suspends it [L0142]. Over AED 50,000 without settlement, the case goes to court [L0144]. MOHRE aims to finish within 14 days; the service is free [L0140, L0164]. During the dispute MOHRE may make the employer keep paying wages for up to two months [L0146]. If you are fired for a serious complaint or valid case, the court can award up to 3 months' wage on top of notice pay and gratuity [L0125].

If MOHRE cannot reach the employer within 5 working days (10 if it asks for time), it cancels your permit on your request so you can move, and late-permit fines go on the employer's file [L0154, L0155]. You can also quit without notice, keeping your rights, if you notify MOHRE 14 working days ahead and the employer does not fix the breach [L0123].

**3. Labour court.** Register the case at court within 14 days of MOHRE's referral [L0151]. The court sets a hearing within 3 working days and decides within 30 [L0145]. No court fees on claims under AED 100,000 [L0148]; there are legal-support offices for workers in the courts [L0176]. While the case runs you may get a temporary permit with a new employer, unless you were reported absent [L0152]; if you stopped working, your permit is cancelled 6 months after referral [L0153]. Claims cannot be heard after two years from the end of the job [L0147].

**4. The labour wing.** Abu Dhabi: +971 2 446 5100 or +971 2 445 8182, labourwingauh@gmail.com [L0202, L0203]. Dubai consulate (Al Wuheida, Deira): 04-2388202 or 04-2690764, labourwingdubai@gmail.com [L0204, L0205]. It takes complaints, visits camps and attends labour court [L0207].

**In practice:** Human Rights Watch reports wage theft, recruitment fees and passport confiscation continuing, with Bangladeshi workers among those hit, and false absconding charges filed against workers who leave abuse [L0250, L0248]. Workers cannot form unions or protest [L0251].

> **Need to know**
> - How long do MOHRE complaints by Bangladeshi workers actually take, and how many end in payment?
> - Does the labour wing accompany workers to MOHRE meetings, and does it charge anything?
> - Is 80060 a current MOHRE number? (u.ae and MOHRE pages give 80084 and 600590000.)

### If you want to change employer

**The old bans.** Before 2011 a worker refused a no-objection certificate (NOC) had to leave for six months, and low-skilled workers needed consent in their first two years [L0252, L0253]. Today the law lets you move in the cases below, and the only ban is one year [L0126, L0128].

**When you can move freely** [L0126]:
- the contract expired and was not renewed;
- it was ended lawfully, including by you without notice for the employer's breach, assault or danger [L0123, L0124];
- the employer ended it without fault on your part.

**Quitting with notice.** Either side may end the contract for a legitimate reason with 30 to 90 days' written notice; whoever skips it pays the other the notice-period wage [L0118, L0119]. If the employer gives notice, you may take one unpaid day a week to job-hunt, telling them 3 days ahead [L0120].

**During probation (up to 6 months).** To move to another UAE employer give one month's written notice; the new employer repays the old one's recruitment costs unless agreed otherwise [L0114, L0138]. To leave the UAE give 14 days' notice [L0116]. Breaking these rules means no work permit for a year from departure [L0117].

**How the move happens.** The new employer applies for a transfer work permit with the MOHRE job offer signed by both of you; all skill levels qualify, it takes 2 working days, and it must be applied for within 90 days of the old permit's cancellation [L0169, L0170, L0171]. You must not work for the new firm before the permit [L0137].

**The one-year ban** applies if you quit during probation without the employer breaching, if a work abandonment report is proven, or if your permit at a fake company is cancelled [L0128]. It runs from your departure and lifts by itself [L0132]. Check for one on 600590000 (8 am-8 pm, several languages); contest it with a grievance and documents through MOHRE channels [L0130, L0131].

### If your employer reports you absent (work abandonment)

**What it is.** A "work abandonment" report (the old "absconding" case) can be filed after more than 7 days' absence in a row when the employer cannot locate or contact you [L0156]. Absence over 7 consecutive days, or 20 in a year, also allows dismissal without notice [L0121].

**What follows.** A proven report means no new work permit for a year [L0128], no temporary permit during a court case [L0152], no ILOE payout while it is open [L0088], and removal from WPS [L0039]. Human Rights Watch says false reports are used against workers who leave abuse, risking detention and deportation [L0248].

**Grounds to cancel it** [L0157, L0158, L0159, L0160]:
- 7 days had not passed, or you had a legitimate reason;
- you were at work or on lawful leave;
- the employer agreed you could stop or look for another job;
- the employer agrees to take you back.

**How to cancel it.**
1. Check on 600590000 or the MOHRE app whether a report exists [L0130].
2. On the MOHRE website or app, use "Cancellation of an Absence from Work Complaint (Absconding Report)": enter your work permit or passport number, name, date of birth, nationality, the absence date and the company details; confirm by OTP [L0167].
3. Attach proof: attendance records, leave approval, WhatsApp messages showing the employer knew where you were, and any earlier labour complaint [L0167].

What you get back: an SMS with the result within 14 working days; free [L0168]. If you left over unpaid wages or abuse, file the labour complaint first (If you aren't paid) [L0123].

> **Need to know**
> - Does a worker get an SMS or other notice when an employer files a work abandonment report?
> - Does a report block the worker's exit at the airport, and how is it cleared if the worker wants to go home?

### Leaving at the end of the job

1. **Notice and last pay.** Serve the notice in your contract [L0118]. Within 14 days of the end the employer must pay all wages, unused leave and gratuity [L0111, L0015]. Ask for a free experience certificate [L0134].
2. **Ticket home.** The employer pays unless you joined another employer or the termination was your fault [L0133].
3. **Housing.** Leave employer housing within 30 days unless agreed otherwise [L0069].
4. **Cancellation.** The employer cancels the work permit and residence; you then have 30 days' grace to leave or change status [G0067]. If the employer will not cancel, MOHRE can cancel on your complaint (If you aren't paid) [L0154].
5. **ILOE, if you were let go** (If a worker dies, is injured or loses the job).

Claims under the labour law cannot be heard more than two years after the job ends, and an ILOE payout needs you to be in the UAE [L0147, L0089].

### Going home on leave

**Before you book.** Agree the dates in writing; the employer sets leave dates with a month's notice [L0013]. A worker who does not come back on time without a good reason is unpaid for the absence, and over 7 days can bring dismissal or an abandonment report [L0135, L0121, L0156]. Stay under 180 days or the visa dies [L0212].

**The 2026 cancellations.** Since June-July 2026 the UAE has cancelled residence visas of Bangladeshis who were home on leave, without stated reasons; Bangladesh counted 985 cases by 3 August, the minister spoke of 4,000 in early September and about 4,800 by mid-September [N0022, N0001, N0002, N0003, N0018]. Notices came by email, SMS or through the sponsor; some learned only at check-in or at UAE immigration [N0012, N0020, N0023, N0027]. Some had visas with over a year left [N0032]. Officials gave security reasons; an embassy official listed possible causes such as job title not matching the work, company quota or WPS problems, investor visas used for labour, and social media posts [N0017, N0055]. Pakistanis, Egyptians, Filipinos and Nepalis were also hit [N0007].

**Check before you fly.**
1. Abu Dhabi, Sharjah, Ajman, Umm Al Quwain, Ras Al Khaimah or Fujairah visa: ICP's "File Validity" page (smartservices.icp.gov.ae) or app, with passport number and nationality; ICP 600522222 [L0220, L0222].
2. Dubai visa: GDRFA's status inquiry (smart.gdrfad.gov.ae); from abroad call +9714-313-9999 [L0221].
3. Ask your employer to confirm in writing that the visa is active.

**If it was cancelled.**
1. Send your details to the Bangladesh Embassy's designated email; it forwarded 985 cases to the UAE by diplomatic note, but being listed does not guarantee reinstatement [N0019, N0051, N0053].
2. Ask the employer whether it cancelled or can re-apply; the Embassy was checking with employers [N0010].
3. Do not buy expensive tickets until the visa shows valid; fares rose to Tk 70,000-1 lakh [N0031].
4. For unpaid wages or gratuity, email the labour wing (labourwingauh@gmail.com) [L0202]; an ILOE payout needs you to be in the UAE [L0089].

> **Need to know**
> - Has any cancelled Bangladeshi visa been reinstated, and by what process?
> - Can a worker whose visa was cancelled abroad still claim gratuity and unpaid wages from Bangladesh, and through whom?

---

## If a worker dies, is injured or loses the job (UAE side)

Bangladesh-side grants, insurance and the WEWB (Wage Earners' Welfare Board) steps: see agents B and G.

### If you are injured or fall ill at work

1. **Get treatment** at any government or private facility; the employer pays all of it, including hospital, surgery, tests, medicine, rehabilitation, artificial limbs and transport, until you recover or a disability is confirmed [L0188, L0179, L0181]. Accidents on the usual route to or from work count [L0178].
2. **Make sure it is reported.** The employer must report to MOHRE within 48 hours, via its website, app or service centre [L0185, L0189]. If it does not, report it yourself on 600590000 or 80084 [L0149].
3. **Pay while off.** Full wage up to 6 months, then half wage up to 6 more [L0180].
4. **Compensation**, due within 10 days of the medical report [L0186]:
   - total permanent disability: 24 months' basic wage, AED 18,000 to 200,000 [L0182];
   - partial: the disability percentage in Cabinet Resolution 33 of 2022 times that amount, same limits [L0183].

   Lost if the injury was self-inflicted, under alcohol or drugs, from a deliberate safety breach, or if you refused treatment [L0187].
5. **If the employer will not pay,** file a MOHRE labour complaint (If you aren't paid) and copy the labour wing, which visits workers in hospital and arranges escorts or stretchers for the flight home [L0162, L0211].

### If a worker dies

1. **Police and death certificate.** A death outside hospital goes to the police, who arrange a post-mortem; the body is released with the prosecutor's permission [L0196]. The death certificate is issued on the police registration, the hospital's death notification, passport and Emirates ID [L0195].
2. **Consulate NOC.** The Embassy (Abu Dhabi) or consulate (Dubai) issues the no-objection certificate. It needs [L0198, G0081]:
   - the original passport;
   - police and forensic report (for accidental death);
   - death certificate (English and Arabic) with the death notification;
   - cargo booking for the body;
   - the company's final settlement;
   - NID of the receiver at the Bangladesh airport;
   - a WEWB letter or heirs' application recommended by the local chairman.

   Queries: 02 445 8182 or WhatsApp 050 361 4760 [L0201].
3. **Embalming and flight.** In Dubai, Dubai Health's service needs the death certificate, notification, police letter, embassy letter, airline ticket and passport copy [L0194]; fees: embalming AED 1,020, ambulance AED 220, body-handling company AED 1,840, typing AED 52.50 [L0193]. The employer pays all costs of preparing and sending the body home if the family asks [L0192].
4. **Burial in the UAE** needs the family's no-objection certificate sent through WEWB or MOFA [L0200].
5. **Money owed.** Within 10 days the employer must give the family all wages, dues and gratuity [L0190]; a worker can name a family member in writing to receive them [L0191]. For a work death the family also gets 24 months' basic wage, AED 18,000 to 200,000 [L0184]. The settlement can be paid to the Embassy or straight to the heirs [L0199]; the labour wing recovers death compensation from companies and courts [L0208]. Unpaid amounts up to AED 20,000 can come from the worker protection insurance [L0172, L0173].

> **Need to know**
> - How long does the Embassy take to pay a recovered death settlement to the family, and through which channel?

### If you lose the job: claiming ILOE

You qualify if you subscribed for 12 months in a row, paid every premium, were not resigning or dismissed for discipline, have no open absence report, and are still in the UAE [L0085, L0086, L0087, L0088, L0089].

You'll need [L0102, L0105]:
- Emirates ID and unified or work permit number;
- a UAE mobile number and date of birth;
- contract, termination letter, residence cancellation, bank statement, any labour complaint.

1. Cancel the work permit first, as ILOE advises [L0102].
2. Within 30 days of the job ending (or of the labour dispute ending), go to diniloe.ae/nsure ("Submit your claim" on iloe.ae), the ILOE app, or call 600599555 [L0091, L0098].
3. Log in with Emirates ID and mobile, enter the OTP, click Claim Submission, confirm the date and reason, upload papers [L0103, L0105].
4. Choose bank transfer (IBAN) or an exchange house [L0104].

What you get back: 60% of your average basic salary of the last 6 months, up to AED 10,000 a month, for up to 3 months, paid within two weeks [L0101, L0084, L0090]; stops if you start a new job; at most 12 monthly payments in a working life [L0093, L0100].

> **Need to know**
> - What share of ILOE claims by low-wage workers are paid, and what are the common rejection reasons?

---

## Notes (for notes.md)

**Searched:** uaelegislation.gov.ae (labour law 33/2021 consolidated to 29 Jul 2024, Executive Regulations 1/2022, penal code, narcotics law, cybercrime law, via Wayback PDFs because the site returns 403), u.ae private-sector pages (all dated Aug-Oct 2026), MOHRE service pages (via Wayback; mohre.gov.ae times out to curl), MOHRE Resolutions 47/2022 (amended) and 782/2023, iloe.ae, Dubai Health, ISAHD, Bangladesh Embassy Abu Dhabi pages and PDFs, HRW World Report 2026, Amnesty 2025, Gulf News, Bangla searches (unpaid wages, jail, visa fines).

**Conflicts:**
- Claim time limit: law Art 54(9) as amended 2024 says two years from end of job [L0147]; u.ae labour-disputes page still cites Art 10's old one-year rule. Used the law.
- Dispute timing: u.ae and ER Art 31 still say refer to court within 14 days; Resolution 782/2023 makes MOHRE decide claims under AED 50,000 itself [L0141]. Used 782.
- ILOE non-payment fine: u.ae says AED 400 for not paying [L0094]; older rules said AED 200. Used u.ae (Dec 2025).
- Hotlines: user brief gives 80060; official pages give 80084 (labour claims) and 600590000. A UAE government Facebook post mentions 80060 for "Tawafuq" centres; not confirmed on any official page.
- Penal code alcohol and fine amounts in the English translation are garbled ("(500,000) five hundred AED"); doc avoids the amounts.
- Midday-ban fine source is MOHRE's 2023 announcement [L0027]; 2025/2026 WAM pages could not be fetched.

**In practice:** HRW 2026: false absconding charges, wage theft, recruitment fees, passport confiscation, midday ban ineffective [L0248-L0250]; Amnesty: no unions or assembly, Dubai evictions from partitioned flats [L0251]. No Bangladesh-specific outcome data on MOHRE complaints found.

**Logged but not used:** L0099 (no ILOE premium during absconding complaint, unclear wording), L0097 detail duplicated, L0136 (notice during leave), L0216 duplicate of L0215 note, L0253/L0252 history only in one line. Worker protection insurance premium for domestic workers not used (domestic section belongs to another agent).

**Page dates approximate:** HRW 2026 set to 2026-01-01, Amnesty to 2026-04-01, Littler set to 2011-01-01 (article about 2011 rules).

**Free zones:** not researched (JAFZA, DMCC have own employment regulations); flag for the lead.

## Blocked pages

- https://www.mohre.gov.ae/assets/download/9e530b2e/Ministerial%20Resolution%20No.%200340%20of%202026.pdf.aspx -> `sources/mohre-resolution-340-2026-wps.pdf`: the 2026 WPS resolution (curl times out; u.ae summary used).
- https://www.mohre.gov.ae/assets/download/b578cbaa/e3ref7qooqek-bingali.aspx -> `sources/mohre-know-your-rights-bengali.pdf`: MOHRE's Bengali rights guide.
- https://www.iloe.ae/pdf/ILOE-Flyer-Bengali.pdf -> `sources/iloe-flyer-bengali.pdf`: ILOE in Bangla.
- https://www.wam.ae/en/article/bk01z89-mohre-implement-midday-break-for-21st-consecutive -> `sources/wam-midday-break-2025.html`: newer midday fine confirmation.
- https://mohre.gov.ae/assets/download/960ffdc1/Ministerial%20Resolution%20No.%20657%20of%202022%20on%20Rules%20and%20Guidelines%20to%20Deal%20with%20Work%20Injuries%20and%20Occupational%20Diseases_638945724651791715.pdf.aspx -> `sources/mohre-resolution-657-2022-work-injuries.pdf`: injury claim procedure.
- https://u.ae/-/media/Mohre-resolutions/Ministerial-Resolution-No318-of-2022-Concerning-Bank-Guarantees-and-Employees-Protection-Insurance-S.pdf (404) -> `sources/mohre-resolution-318-2022.pdf`: how workers claim the protection insurance.
- Facebook: Bangladesh Embassy Abu Dhabi and Consulate Dubai posts (July-Oct 2026) on visa-cancellation email submissions and any reinstatements; MOHRE UAE post on the community reporting service.


# N findings: corridor big picture, practical pass, scams (agent N; prefix N, and A for chain/cost/scam facts)

Status: draft for the lead. Facts N0001-N0148 and A0001-A0004 are logged in facts.csv. Remittance figures cite agent G's facts (G0097-G0099) rather than duplicating them. Rates: AED1 = about Tk 34 [G0002].

## a. Draft doc text

### Background

**Is it open now, and who can go?**

Open only a crack, and shaking. New work visas for Bangladeshis have been restricted since July 2024, and since July 2026 the UAE has been cancelling the residence visas of Bangladeshis who went home on leave [N0037, N0001].

- **Status on 8 November 2026:** no published UAE ban exists, but the Expatriates' Welfare Minister says family, student, tourist and employment visas, and transfers of a visa from one company to another, have all been restricted or stalled since July 2024 [N0049, N0098]. Some work visas are issued: BMET (Bureau of Manpower, Employment and Training) cleared 23,044 workers for the UAE from 1 January to 7 November 2026, over 4,000 a month in July to September, then 951 in October and 63 in the first week of November [N0137, N0141, N0142, N0143, N0144, N0145].
- **Visas cancelled while home on leave (July 2026 onward):** notices arrive by email, text message or through the kafil (sponsor), often with no reason; some people learned only at check-in, when the airline system refused them a boarding pass [N0011, N0020, N0027, N0023]. People whose visas still had more than a year to run were hit [N0032].

  The count kept rising:
  - 626 on 30 July 2026 (Foreign Affairs State Minister Shama Obaed, who said Pakistanis, Egyptians, Filipinos and Nepalis were also affected) [N0006, N0007];
  - 985 sent to the UAE by diplomatic note by 3 August, out of about 2,500 emails the embassy received [N0051, N0002];
  - 4,000 on 6 September (State Minister Nurul Haque Nur) [N0003];
  - 4,800 by mid-September [N0013, N0018];
  - 5,000 on 13 October (Law Minister Md Asaduzzaman, who added that many renewals were pending) [N0100];
  - about 6,600, the figure protesters gave outside Probashi Kallyan Bhaban on 7 October [N0021].
- **The reasons given:** the UAE has given no formal explanation [N0057]. The state minister says the UAE cites internal security [N0017]. A senior embassy official listed possible causes: the company hired over its quota, the job on the visa does not match the real work, Wage Protection System (WPS, the UAE's electronic salary-payment system) violations, company licence problems, a labourer working on an investor visa, social media posts against UAE law, and criminal or disciplinary cases [N0055]. Bangladesh's ministers warn workers not to film sensitive events or post them online [N0009, N0099].
- **What Bangladesh has done:** the embassy collects cases by email and forwards them to the UAE; being on its list does not guarantee reinstatement, because only the UAE government can reactivate a visa [N0019, N0052, N0053]. The Ministry asked the UAE to re-examine the cases [N0017].

> **Need to know**
> - Why did BMET clearances for the UAE fall from 4,442 in September 2026 to 951 in October: a new UAE restriction, flight disruption after the 10 October Riyadh airport attack, or a pause in BMET processing?
> - Has the UAE reinstated any of the cancelled residence visas, and through which office (ICP, GDRFA or MOHRE)?

**Visa by visa, November 2026** (details in each visa section):
- **New work visa, low-skilled:** restricted since July 2024; a ministry official said none were issued in 2025, though BMET cleared 13,750 workers that year, mostly as cleaners, drivers, accountants, helpers and managers [N0038, N0136, N0089].
- **New work visa, named employer recruiting in bulk:** moving in 2026. Dubai Taxi Company plans to hire 6,000 Bangladeshi drivers this year, and construction helpers, masons and steel fixers are the largest 2026 clearance categories [N0077, N0090].
- **Skilled work visa:** MOHRE (the UAE Ministry of Human Resources and Emiratisation) reactivated its online system for skilled Bangladeshi workers in May 2025 [N0075].
- **Visit visa:** the UAE Embassy in Dhaka issued 30 to 50 a day in May 2025; by October 2025 travel agents called tourist and transit visas "almost zero" [N0074, N0062].
- **Residence visa of people now in Bangladesh on leave:** at risk of automatic cancellation [N0005, N0029].

**The channels.**
- **A named employer recruiting through a licensed agency:** Dubai Taxi's 2026 drive runs through three agencies, Al Anas Overseas, VIP Global and M Bahar Overseas, with interviews at the Bangladesh-Korea Technical Training Centre (Step 1) [N0078, N0077].
- **A visa found by a relative in the UAE:** the most common route; workers say it is safer than agents [N0117, N0125].
- **Partner or investor visa:** a residence visa tied to a trade licence, sold as a way in when labour visas closed; working for anyone else on it is illegal ("How a job reaches you") [N0107, N0108].

**Who qualifies.** Whoever the employer's MOHRE work permit names: the UAE portal says a genuine job comes with a MOHRE offer letter signed by the employer's authorised manager [N0129]. Dubai Taxi drivers must communicate in English [N0079].

**Size.**
- About 12 lakh Bangladeshis live in the UAE by Bangladesh's estimate, the third-largest foreign community after Indians and Pakistanis [N0014, N0065]. A private estimate puts them at 0.84 million, against 4.36 million Indians, 1.9 million Pakistanis, 0.78 million Filipinos and 0.36 million Nepalis [N0146, N0147, N0148].
- BMET clearances for the UAE: 98,201 in 2023 (4th destination), 47,158 in 2024 (5th), 13,750 in 2025 (6th) and 23,044 in 2026 up to 7 November (6th, behind Saudi Arabia, Singapore, Qatar, the Maldives and Kuwait) [N0084, N0093, N0135, N0094, N0136, N0095, N0137, N0096]. Before the curbs about 5,000 to 6,000 a month went [N0061].
- Remittances from the UAE: USD 4,583.9 million in FY2025-26, of USD 35,589.39 million in total; in July to September 2026 the UAE was the third source after Saudi Arabia and the UK [G0097, G0098, G0099].

**What closed it before.**
- **2012-13 to 2020:** the UAE largely stopped labour visas for Bangladeshis; migration fell until 2021 [N0036, N0073].
- **2021 to mid-2024:** flows rose again on various visas, to 101,000 in 2022 and 98,000 in 2023 [N0073, N0041].
- **19 July 2024:** Bangladeshis marched in UAE streets in support of the quota reform movement. Protests without permission are banned. On 21 July a federal court sentenced 57: three to life, 53 to ten years, one (who had entered illegally) to eleven years, all to be deported afterwards [N0069, N0033]. Recording and sharing videos of the gathering counted against them [N0034]. Visa applications for Bangladeshis were blocked from 22 July 2024 [N0042, N0071].
- **3 September 2024:** the UAE President pardoned them and ordered deportation; 131 more were arrested and 188 freed in all, most flown home in November and December 2024, jobless [N0035, N0102, N0127]. Their fingerprints were kept, and a Foreign Ministry director said they may not get into the UAE or other Gulf states again [N0103].
- **2025:** limited reopening (30 to 50 visit visas a day, skilled visas, 500 security-guard visas granted and 1,000 more approved) after the chief adviser's special envoy lobbied; the envoy was told over 25% of the UAE's visa and residency violators are Bangladeshis [N0074, N0075, N0076, N0064].
- **July 2026 onward:** residence visas of people on leave cancelled (above).

**How a job reaches you, and who takes a cut**

A UAE work visa starts with a UAE company that has a MOHRE work permit for a named person; the law makes that employer pay recruitment costs, so the ambassador says a worker should be able to come free [N0129, N0131, N0115]. In practice the visa is bought and sold through layers of middlemen, and the price rises at each hand [N0115, A0002].

**Who carries the visa.**
- **Relatives:** most workers come through a relative already in the UAE [N0117, N0125].
- **Agencies and their brokers:** a 2019 study found agents and relatives alike paint the job rosier than it is, and the contract signed in Bangladesh often differs from the one the company holds [N0123, N0124].

**Free visa, partner visa, company visa.** Workers sort UAE visas this way:
- **কোম্পানি ভিসা (company visa):** a work permit for a real job with the company that sponsors you; the Dubai Taxi and construction visas of 2026 are this kind [N0077, N0090].
- **ফ্রি ভিসা (free visa):** no such visa exists in UAE law. Brokers sell a work permit in a company's name with no job behind it; the worker must find work himself, working for anyone else is illegal, the company can cancel the visa at any time, and renewal means paying the broker again [N0111, N0113].
- **পার্টনার/ইনভেস্টর ভিসা (partner or investor visa):** residence as a part-owner of a trade licence, usually one licence for two people plus an Emirati partner paid over a lakh taka and a shop or office lease [N0109]. In 2019 brokers charged Tk 6 to 7 lakh, bringing people in on visit visas, though the visa cost less than half that [N0107]. The holder may work only for his own licence: one caught working for an Abu Dhabi company got two months' jail and deportation, and the company was fined AED 50,000 [N0108]. Raids made employers stop hiring partner-visa holders [N0110]. In 2026 the embassy listed "labourer working on an investor visa" among possible reasons for cancellations [N0056].

**What the clearance data shows.** BMET's own clearance titles for the UAE in 2023 were led by "Manager" (23,300) and "Accountant" (8,597), ahead of "Worker" and "Labour"; 2024 had 1,006 cleared as "Partner" [N0085, N0086, N0087, N0088]. In 2026 construction helpers, drivers, cleaners and masons lead, though "Marketing Manager", "Accountant" and "Sales Manager" still number in the hundreds [N0090, N0092]. A visa whose job title does not match the real work is one of the possible reasons the embassy gave for the 2026 cancellations [N0055].

> **Need to know**
> - Who were the 23,300 Bangladeshis cleared as "Manager" for the UAE in 2023: real managers, partner-visa holders, or labourers on visas with skilled titles bought to pass the restriction?
> - What does a UAE company work visa (construction helper, cleaner, driver) sell for in Dhaka in 2026, and what does a "free visa" or partner visa sell for?
> - Who sells UAE visas to Bangladeshi brokers: the UAE sponsor (kafil) himself, Bangladeshi-owned companies in the UAE, or typing-centre agents?

**The choke point.** Two gates: the UAE deciding whether to issue a visa to a Bangladeshi passport at all, and BMET's emigration clearance (the smart card). The second has been sold: a 2022 Ministry inquiry found BMET had issued 6,938 smart cards against UAE permissions for 2,960 workers, sold to manpower traders and brokers for Tk 3 to 4.5 lakh each, and named BMET officials in the ring [A0001, A0002, A0004]. Workers sent on those cards got neither legal status nor jobs, and many slept in parks [A0003]. Each agency's record is in the `agencies` folder.

**What you pay, and what you earn and keep**

**The cap.** The government's maximum for the UAE is Tk 1,07,780, set in 2016-17 [N0138]. Under UAE law the employer pays recruitment costs (Step 1) [N0131].

**What people really pay.** For Dubai Taxi driver jobs, the state minister said in May 2026 that workers pay at least Tk 3.5 lakh; he asked for Tk 1 lakh [N0080]. Middle East jobs in general cost Tk 5 to 7 lakh in 2025 [N0116]. The government survey of 2015-18 migrants found men paid Tk 4.71 lakh on average, with unskilled workers paying more than skilled [N0118, N0119].

**What the job pays.** Dubai Taxi drivers earn a 35% commission per ride, about AED 2,500 to 4,000 a month (about Tk 85,000 to 1.36 lakh) [N0079, G0002]. In a 2019 study 44% of low-skilled workers got less than promised [N0124].

> **Need to know**
> - What do UAE construction helpers, cleaners, security guards and salesmen actually take home in 2026, after food and accommodation deductions?

**How long the debt takes.** On the survey's averages, 17.6 months; unskilled workers need 20.2 months [N0118, N0119].

**What ties you to the employer**

Tied: the visa belongs to the sponsoring company, which can cancel it online without telling you [N0028]. Changing employer has been restricted for Bangladeshis even inside the UAE [N0098, N0126]. Law detail: agent L's section.

**What goes wrong most, and what people wrongly believe**

**The commonest losses.** Losing the visa while on leave (2026); arriving on a visa with no job behind it (free visa, fake smart card); pay lower than promised; and being stuck with an employer you cannot leave [N0005, N0113, A0003, N0124, N0126].

**What people believe, and the facts.**
- **"If I have a job, my visa is safe."** The employer can cancel it online without the worker knowing; check it before you fly (Going home on leave) [N0028, N0025].
- **"A free visa lets me work anywhere."** No such visa exists; working outside the sponsoring company is illegal [N0111, N0113].
- **"Go on a visit visa; the work visa gets done there."** A visit visa gives no right to work, and working on one brings fines [N0130].
- **"The UAE banned Bangladeshis from January 2026."** That claim came from a private visa website; the embassy said the site's Dubai address does not exist and most of its customers say they were cheated [N0044, N0049, N0050].
- **"A partner visa is a work visa."** It allows work only for your own licence [N0108].

**How irregular routes end.**
- **Amnesty:** over 50,000 Bangladeshis took the 2024 amnesty [N0128].
- **Bans:** a Foreign Ministry official says a cancelled residence or a broken law bars re-entry for 5 to 10 years [N0104].
- **Protest:** jail, then deportation (above) [N0033, N0035].

### Scams

**Scams done to you.**

1. **A "free visa" or job that doesn't exist.** The visa is real but has no job behind it; you pay again to renew [N0111, N0113].
   **Check it is real:** ask for the MOHRE offer letter and check it by reference number; check an entry permit on GDRFA Dubai (if issued in Dubai) or ICP (the other emirates) [N0129, N0133].
2. **A fake or oversold smart card.** In 2022 cards were sold beyond the UAE permissions [A0001, A0002].
3. **"Your cancelled visa can be reinstated for a fee."** Only the UAE government can reactivate a visa; the embassy's list is free [N0053, N0019]. False notices using the embassy's logo and email circulated in July 2026 [N0068].
4. **"Visa ban" or "visa open" posts.** The 2025 ban story came from a website that cheated customers [N0050].
5. **Ticket gouging.** During the cancellations, Dhaka-UAE one-way fares of Tk 15,000-20,000 were sold for Tk 70,000 to 1 lakh [N0031].

**Scams done by the migrant.**
- Working on a visit visa or partner visa: fines, jail, deportation [N0130, N0108].
- Fake certificates: the law minister says agencies submitted certificates from institutions that did not exist [N0101].

## b. Notes

- Searched: English and Bangla news, BSS, WAM, Embassy press releases, OEP data, GLMM, agency blogs.
- Conflicts: counts of cancelled visas grew over time; GMI 0.84m vs govt 1.2m; ministry official "no visas in 2025" vs BMET 13,750; OEP 2022 incomplete (4,247 vs 101,000).
- Facts N0001-N0148 use prefix N, including cost/chain/scam facts logged before the A instruction; A0001-A0004 are the first A facts.
- Agencies with large UAE activity per agencies.csv (Matco Enterprise, AVR Bangladesh, Al-Anas Overseas, Visa International, Al Saad Labour Supply) were not named in the doc; Al Anas is named only via the Dubai Taxi news.
- Sources needing date fixes: news-shomoyeralo-uae-visa-cancel-protest is 2026-07-27, news-toi-uae-visa-cancel-bangladeshis is 2026-09-16 (registered undated).

## c. Blocked pages
- ILO/BBS Cost of Migration Survey 2020: https://www.ilo.org/sites/default/files/wcmsp5/groups/public/@asia/@ro-bangkok/@ilo-dhaka/documents/publication/wcms_766198.pdf -> sources/bbs-ilo-cost-of-migration-survey-2020.pdf (UAE-specific cost and income).
- Kaler Kantho embassy statement 28 Jul 2026: https://www.kalerkantho.com/online/national/2026/07/28/1717449 -> sources/news-kalerkantho-uae-embassy-visa-cancel-2026-07.html
- Facebook: Bangladesh Embassy Abu Dhabi notice of 1 Aug 2026 (cases by email), and any later notice on reinstatements.


# V findings: short-stay and visit visas (agent V)

Prefix V. Facts V0001-V0215 in facts.csv. AED1 = about Tk 34 [G0002].

## a. Draft doc text

## Visas not open to Bangladeshis

**Status, November 2026.** The UAE has never announced a ban, but in July 2024, after Bangladeshis in the UAE protested in support of the quota reform movement, it quietly stopped issuing visit and work visas to Bangladeshis [V0001]. The closure showed only as the visa submission system blocking Bangladeshi applications; no letter was sent to Bangladesh [V0009]. A Ministry of Expatriates' Welfare official said no visit or work visas were issued to Bangladeshis in 2025 [V0002]; the UAE ambassador in Dhaka had said in May 2025 that the embassy was issuing 30 to 50 visit visas a day, on a limited scale [V0015]. Only "skill visas" and "high-profile visas" for professionals were reported available in January 2026 [V0011, V0010, V0005], and turning a visit visa into a work visa inside the UAE has been closed to Bangladeshis for years [V0012]. The visit visas were restricted because Bangladeshis increasingly used them to find work [V0013]; UAE immigration officials told Bangladesh's special envoy in June 2025 that over 25% of all visa and residence violators in the UAE are Bangladeshis [V0007]. Each visa below gives its own status line.

> **Need to know**
> - Does ICP's or GDRFA's system still reject an application at submission when the passport nationality is Bangladesh, for every visit visa type, as of November 2026?
> - Has any Bangladeshi-passport visit visa been issued in 2026, and through which channel (embassy courtesy visa, airline, family sponsor)?

- **Visa on arrival or visa-free entry:** not for Bangladeshis; only listed nationalities get it on arrival [V0022, V0021].
- **14-day or 60-day visa for holders of a US, UK, EU or other approved residence or visa (including a US green card):** limited to nationals of India, Indonesia, Kenya, the Philippines, South Africa, Thailand and Vietnam; Bangladeshis are not eligible even with a US, UK or EU visa or residence [V0019, V0020, V0021].
- **Tourist visa applied at a UAE embassy:** UAE embassies, including Dhaka, do not issue tourist visas [V0071]. The embassy can issue courtesy visit visas, with ICP approval, to people it chooses and to diplomatic and UN passport holders [V0198].
- **Converting a visit visa to a work visa inside the UAE:** closed to Bangladeshis for several years [V0012]. A residence visa can only be processed after the person enters on a valid entry permit [V0187].

### Scams

**Done to travellers.** In September 2025 a visa-agency website, uaevisaonline.com, posted that the UAE would ban tourist and work visas for Bangladesh and eight other countries from January 2026; Bangladeshi media repeated it [V0018]. The Bangladesh Embassy in Abu Dhabi said the claim was false, that the UAE had made no such announcement, that the site's contacts were in the UK, US and India, that its Dubai head-office address did not exist, and that most of its customers complained of being cheated [V0205, V0206]. A "ban list" or a "reopening" announced only by an agent or website is not official: check u.ae, icp.gov.ae and gdrfad.gov.ae (see Tourist visa, Step 4).

### Don't work

No visit visa allows work (see Tourist visa, Don't work) [V0179].

## Tourist visa

**Status, November 2026:** tourist visas for Bangladeshis have been effectively stopped since mid-2024 [V0001, V0003]. In October 2025 the Association of Travel Agents of Bangladesh (ATAB) said tourist and transit visas were "almost zero" [V0003], and a director of the Tour Operators Association of Bangladesh (TOAB) who processed over 2,000 UAE tourist visas a year from 2021 to mid-2024 had not managed one in the year since [V0004]. Even a 27-member official delegation to an Abu Dhabi congress got its visas only the night before the flight, after Foreign Ministry intervention [V0008]. The rules below are the official ones, for when applications go through.

A tourist visa lasts 30 or 60 days, single or multiple entry [V0062, V0066]. A visitor cannot apply alone: a UAE tourism establishment (licensed travel agent, hotel or tour operator) or a UAE airline applies as sponsor [V0062, V0064, V0073, V0068]. Airlines do it only for their own passengers [V0069]; travel agents and hotels only if the ticket is bought through them and the hotel booking is kept [V0070].

### Step 1: Choose who applies for you

- **A UAE airline** (Emirates, Etihad, flydubai, Air Arabia) [V0185]. Emirates applies online through "Manage your booking" for passengers holding an issued Emirates ticket into and out of Dubai on one booking reference (PNR), at least four working days before arrival; VFS Global processing fees are added [V0077, V0078, V0079].
- **A licensed UAE travel agent or hotel**, which files with ICP (the Federal Authority for Identity, Citizenship, Customs and Port Security, for Abu Dhabi and the northern emirates) or GDRFA Dubai (the General Directorate of Identity and Foreigners Affairs, for Dubai) [V0068, V0051, V0064].
- **A Bangladeshi travel agency** selling a package with a UAE tour operator; check it is genuine before paying or sending any document copies; the UAE embassy can help verify [V0072].

### Step 2: Prepare the papers

You'll need:

- a passport valid at least 6 months [V0030, V0065];
- a photo and a passport copy [V0062, V0040];
- a confirmed return or onward ticket [V0030, V0065];
- UAE-valid health insurance [V0030, V0065];
- for ICP, a tour programme statement [V0040];
- for Emirates, a confirmed hotel booking for the whole stay (or a tenancy contract in a family member's name) and a return Emirates ticket (number starting 176) whose dates match the hotel booking [V0076, V0075].

### Step 3: Pay

- **GDRFA, single entry:** AED 200 (30 days) or AED 300 (60 days), plus 5% VAT (value added tax); no deposit [V0063].
- **GDRFA, multiple entry:** AED 300 (30 days) or AED 500 (60 days), plus VAT [V0066].
- **Emirates (VAT included):** US$90 for 30 days single entry up to US$231 for 60 days multiple entry; extension US$230 [V0074].
- **Agents' and typing centres' fees** come on top; compare with the Amer price list (amer247.com) for Dubai visas [V0186].

A decision takes about 48 hours (GDRFA, ICP) or 2 to 4 working days (Emirates) [V0067, V0048, V0080]. The visa arrives by email as an electronic copy [V0049]. You must enter within 60 days of issue [V0033, V0074]. If ICP does not complete a service, only the issuance fee is refunded, on request with a bank certificate showing the IBAN; application and smart-service fees are not [V0208, V0209].

> **Need to know**
> - Can a refused UAE visit visa be appealed, or only re-applied for?
> - What do Dhaka travel agencies charge for a UAE tourist visa package in 2026?

### Step 4: Check the visa is real

1. **Find which emirate issued it** (printed on the visa).
2. **Dubai visa:** open the GDRFA Status Inquiry page (smart.gdrfad.gov.ae/Public_Th/StatusInquiry_New.aspx) and enter the visa details [V0189].
3. **Abu Dhabi, Sharjah, Ajman, Umm Al Quwain, Ras Al Khaimah or Fujairah visa:** open ICP's File Validity page (smartservices.icp.gov.ae, "fileValidity") [V0188]; to track an application, enter the application number, which starts with 010, under application tracking [V0050].
4. **Or phone:** ICP 600522222; GDRFA 800 5111 inside the UAE, +971 4 313 9999 from abroad [V0190].

> **Need to know**
> - What do ICP's and GDRFA's validity pages ask for (visa file number, passport number, nationality) and what do they show for a fake visa?

### Step 5: Board the flight

**OK to Board.** Air Arabia requires an "OK to Board" message on the booking of passengers flying from Bangladesh to the UAE who carry a copy of the visa or an e-visa; the sponsor or a representative takes the original visa to an Air Arabia office at least 24 hours before departure and pays AED 15 to 20 [V0086, V0087, V0088, V0089].

> **Need to know**
> - Do Biman, US-Bangla, flydubai and Emirates require OK to Board for Bangladeshi visit-visa passengers, and at what fee?

**At Dhaka or Chattogram airport,** immigration police question visitors to Dubai about their purpose and family and stamp "offload" in the passports of those they doubt [V0201]. In 2021 travel agencies charged Bangladeshis Tk 1.2 to 1.5 lakh for a UAE visit visa package covering the visa, ticket, a promised job and an "airport contract", and separately Tk 30,000 or more, which they said went to immigration police, to get offloaded passengers through [V0199, V0200].

> **Need to know**
> - Does the "airport contract" for UAE visit-visa travellers still operate in 2026, and at what price?

**At the UAE airport,** some visitors must do an eye scan at passport control; GDRFA's visa office in Dubai Terminal 3 arrivals, near Entrance 1, is open 24 hours [V0195, V0194].

> **Need to know**
> - Do UAE immigration officers ask Bangladeshi visitors to show a minimum amount of cash or a hotel booking on arrival?

### Step 6: Extend or leave

A tourist visa may be extended once or more, up to 120 days in total, by applying to ICP or GDRFA with the same documents: AED 100 application plus AED 500 extension [V0053, V0060, V0058]. Leave when it expires [V0170]. Overstaying costs AED 50 a day [V0045]; check fines on GDRFA's fines inquiry service and pay through ICP or GDRFA [V0191].

### 5-year multiple-entry tourist visa

This self-sponsored visa is open to all nationalities, including Bangladeshis: valid 5 years, up to 90 days each visit, extendable by 90 days, no more than 180 days a year [V0090, V0091, V0095, V0104]. The year counts from the first entry, and unused days don't carry over [V0096].

> **Need to know**
> - The ICP card also says the holder must not exceed 90 days a year [V0106]: is the yearly limit 90 or 180 days?
> - Has any Bangladeshi-passport holder been granted the 5-year visa since mid-2024?

You'll need:

- a bank statement showing at least USD 4,000 (about Tk 5 lakh) throughout the 6 months before applying [V0093, V0104];
- UAE-issued health insurance valid 180 days [V0094];
- a return ticket and proof of where you'll stay [V0097];
- passport valid 6 months and a photo [V0097].

1. **Apply yourself** online on ICP's smart services ("Issuance of a Long-Term Multiple-Entry Tourist Visa – 5 Years") or GDRFA's ("Issuing a multi-entry tourist visa (5 years)"), 24 hours a day, or at a GDRFA Customer Happiness Centre or Amer centre (Dubai's licensed government-service centres) [V0092, V0102, V0122]. Families use ICP's family-group version; the head of family must enter with them [V0103].
2. **Pay** AED 100 application, AED 500 issuance, AED 100 smart-service fee and a refundable AED 3,000 guarantee plus AED 20; GDRFA's total is AED 3,713 (about Tk 1.26 lakh) [V0092, V0099].
3. **Enter within 60 days** of issue; after that the visa is multiple-entry [V0098].
4. **Track your days** by requesting a travel report of entries and exits; an overstay is fined at the departure port and the AED 3,000 guarantee is forfeited [V0101, V0100].

### Bangladeshis living in another Gulf country

A Bangladeshi resident of a GCC (Gulf Cooperation Council) country applies online for an entry permit before travelling [V0023]. The residence must be valid at least a year from arrival and the profession must be on the UAE's approved list [V0025, V0026]. The permit is valid 30 days from issue, allows 30 days' stay and can be extended once for 30 days [V0024]. GDRFA charges AED 100 application, AED 100 issuance and AED 52.5 service fee, decided in 48 hours; you upload a photo, passport copy and your residence permit showing your profession [V0027, V0028].

> **Need to know**
> - Which professions are on the approved list for the GCC-resident entry permit?

### Scams

**Done to travellers.** On 19 June 2026 GDRFA Dubai said it had acted against entities selling unauthorised visa and residence services on social media, and told people to use only official channels and to check the source before sharing documents or paying [V0192, V0193]. Fake "ban" and "reopening" news is spread by visa-selling websites (see Visas not open to Bangladeshis, Scams) [V0205, V0206]. "Visit visa with job" packages are sold in Bangladesh: the buyer pays for a visa, ticket, a promised job and an airport contract [V0199]. Only airlines, licensed hotels and licensed travel agencies issue tourist visas [V0185].

**Tried by travellers.** A false statement to get a visa carries up to 6 months' jail and/or a fine of AED 5,000 to 10,000, and possible deportation [V0176]. Forging a visa, or knowingly using a forged one, carries up to 10 years' jail and mandatory deportation [V0177].

If an agent sold you a fake visa or a "job on a visit visa", or holds you in the UAE: use the complaint ladder in Work visa: company worker, Scams.

### Don't work

A visit or tourist visa gives no right to work; working on one brings fines and legal liability [V0179]. The law forbids any work except as UAE legislation allows [V0169]. Anyone who employs or houses a person in breach of the residence law is fined AED 50,000 per person, up to AED 5 million, and jailed on a repeat; the worker is deported [V0171, V0172, V0173]. Using or helping to use a visa for a purpose other than the one it was issued for carries jail or a fine of at least AED 10,000 per person, and deportation [V0174, V0175]. Under the Labour Law, employing a worker without a work permit costs the employer AED 100,000 to 1,000,000 [V0210].

## Job-seeker visit visa

**Status, November 2026:** visit visas for Bangladeshis are restricted (see Visas not open to Bangladeshis) [V0001, V0002]; only skilled and high-profile categories were reported open in January 2026 [V0011].

This visa lets a person enter once to look for work without a UAE sponsor, for 60, 90 or 120 days [V0107, V0117]. It is only for:

- a skilled worker at MOHRE (Ministry of Human Resources and Emiratisation) skill level 1, 2 or 3; or
- a graduate of one of the world's top 500 universities (Ministry of Education ranking) who graduated within the last 2 years;

and in both cases with at least a bachelor's degree [V0108, V0109, V0112, V0123].

> **Need to know**
> - How does a Bangladeshi abroad get MOHRE's certificate of skill level, which ICP lists as a document?

### Step 1: Prepare

You'll need:

- a passport valid 6 months and a colour photo [V0110, V0030];
- the attested bachelor's degree certificate [V0110, V0114];
- MOHRE's certificate confirming your skilled-worker level, or, for a top-500 graduate, the Ministry of Education's certificate of the university's ranking [V0114, V0115];
- UAE-valid health insurance [V0030].

### Step 2: Apply

1. **Online:** ICP smart services or app (log in with UAE Pass, the UAE's digital ID, or a username), service "Issuance of a Job Exploration Visa" (60, 90 or 120 days, single entry); or GDRFA's "Issuing a visit visa to explore job opportunities" [V0111, V0046, V0122].
2. **Or in Dubai at a counter:** at a GDRFA Customer Happiness Centre or an Amer centre: take a queue ticket, hand in the papers, pay [V0122].
3. **Pay:** ICP AED 100 application, AED 100 issuance, AED 100 smart-service fee and a refundable AED 1,000 guarantee [V0113]; GDRFA AED 200 (60 days), AED 300 (90) or AED 400 (120), plus 5% VAT and the AED 1,000 security [V0119, V0120].
4. **Wait about 48 hours** [V0121]. Enter within 60 days of issue [V0116].

### Step 3: Extend, then leave or switch

The visa can be extended once or more up to 180 days in total, for AED 100 plus AED 500 [V0055, V0058]. To claim the AED 1,000 back, leave, have the visa cancelled after departure, and have no violations [V0118]. A job found during the visit needs a MOHRE offer letter and a work permit (see Work visa: company worker) [V0180]; for Bangladeshis the visit-to-work switch inside the UAE has been closed for years [V0012].

### Scams

**Done to job-seekers.** A genuine job comes with a MOHRE offer letter, which you can check by its reference number at inquiry.mohre.gov.ae [V0180]. The employer, not the worker, pays recruitment costs [V0181]. Check the company on the National Economic Register (ner.economy.ae) [V0182]. MOHRE answers recruitment questions on +971 6 802 7666 and ask@mohre.gov.ae [V0183].

> **Need to know**
> - Are Bangladeshi agents selling "job-seeker visas" to people without a degree, and at what price?

**Tried by job-seekers.** A fake degree or false statement to qualify is a crime (see Tourist visa, Scams) [V0176, V0177].

### Don't work

The job-seeker visa is for looking, not working; the penalties in Tourist visa, Don't work apply [V0179, V0171, V0210].

## Family visit visa

**Status, November 2026:** visit visas for Bangladeshis were restricted from July 2024 and a ministry official said none were issued in 2025 [V0001, V0002].

> **Need to know**
> - Are UAE residents (including Golden Visa holders) able to get visit visas for Bangladeshi parents, spouses or children in 2026?

A UAE resident can sponsor a relative's or friend's visit for 30, 60 or 90 days, single or multiple entry [V0034, V0211, V0124]. The sponsor must earn at least [V0031, V0130]:

- AED 4,000 a month for a first-degree relative: father, mother, spouse, son, daughter;
- AED 8,000 for a second- or third-degree relative: sibling, grandparent, grandchild, uncle, aunt, cousin;
- AED 15,000 for a friend [V0032].

In humanitarian cases ICP's Director General of Identity and Foreigners Affairs can waive the income or kinship rule [V0131].

### Step 1: The visitor sends papers to the sponsor

You'll need:

- a passport valid at least 6 months and a recent photo [V0030, V0213];
- the attested marriage, birth or family certificate proving the relationship [V0213, V0041];
- a return ticket and UAE-valid health insurance [V0030].

### Step 2: The sponsor applies in the UAE

You'll need (the sponsor): a valid UAE residence visa and Emirates ID, an active sponsor file, and proof of income (salary certificate from a government or free-zone employer, employment contract for a private company, or partnership contract), plus proof of accommodation [V0212, V0035, V0125, V0213].

1. **Apply** on the ICP smart services site or app with UAE Pass ("Issuance of a Visa", visitor for relatives or friends) for Abu Dhabi and the northern emirates [V0029, V0046]; Dubai residents use GDRFA's smart services, app, an Amer centre or a Customer Happiness Centre [V0215, V0122]. Emirates ticketing offices in the UAE also take residents' visa applications for Emirates passengers [V0085].
2. **Pay:**
   - ICP: AED 100 application, AED 100 per month (single entry) or AED 200 per month (multiple entry), AED 100 smart-service fee, and a refundable guarantee of AED 1,000 (single) or AED 2,000 (multiple) plus AED 20 [V0037, V0038, V0039];
   - GDRFA: AED 200 (30 days), AED 300 (60) or AED 400 (90) single entry, or AED 300, 500 or 700 multiple entry, plus 5% VAT, insurance AED 40 to 90, and a refundable AED 1,000 (single) or AED 2,000 (multiple) deposit [V0126, V0127, V0128, V0214].
3. **Wait about 48 hours**; the visa is emailed [V0048, V0049].
4. **Send the visa to the visitor,** who must enter within 60 days [V0033].

### Step 3: Stay, extend, leave

Extensions are granted once or more, on the same documents, for AED 100 plus AED 500 [V0060, V0058]. The visitor then leaves; the sponsor asks for the guarantee back after the visa is cancelled or the visitor exits, if there was no violation [V0036].

> **Need to know**
> - ICP's two service cards give a different maximum total stay for a relative's visit (120 days [V0034] and 180 days [V0054]): which applies?

### Scams

**Done to families.** Brokers sell "family visas" through social media; GDRFA warned in June 2026 that unauthorised visa services online can exploit people [V0192]. A family visit visa can only be applied for by the resident relative, with their own Emirates ID and salary proof [V0212]: an agent with no relative behind it cannot get one legally.

**Tried by families.** A false relationship certificate or salary paper is a false statement or forgery (see Tourist visa, Scams) [V0176, V0177]; the sponsor faces AED 50,000 per person for harbouring someone who breaks the residence law [V0171].

### Don't work

A visit visa holder may not work (see Tourist visa, Don't work) [V0179]. An overstay costs AED 50 a day, and the sponsor loses the guarantee [V0045, V0036].

## Business visit

**Status, November 2026:** visas for Bangladeshi business people have been slow and uncertain; group visas for business delegations were said to be speeded up in May 2025 [V0017, V0008].

### Explore business or investment

A single-entry visa for 60, 90 or 120 days, with no UAE sponsor, for people who are financially solvent, talented or highly qualified and work in the intended business at home [V0203, V0204]. Since September 2025 the applicant must show financial capability for the activity, run it through a company abroad, or practise the profession [V0135].

You'll need:

- a passport valid 6 months and a photo [V0133, V0030];
- initial approval from the UAE authority for the planned business [V0133];
- a stamped bank statement for at least 6 months [V0133];
- a bachelor's degree certificate (ICP) or proof of investment (GDRFA) [V0133, V0136].

1. **Apply** on ICP smart services ("Issuance of a Visa to Explore Business Establishment Opportunities") or GDRFA's business-exploration service [V0133, V0136].
2. **Pay** ICP AED 300 in fees plus a refundable AED 1,000 guarantee, or GDRFA AED 200 to 400 plus VAT and AED 1,000 [V0134, V0136].
3. **Extend** if needed, up to 180 days in total [V0055].

### Events, conferences and training

Since September 2025 there is an Events Visit Visa for exhibitions, conferences, seminars, festivals and similar; a UAE public or private host applies, with a letter giving the event and its dates [V0137, V0138]. For study or training, a licensed UAE university, institute, research body or a government or private trainer applies with a letter stating the programme and its length; GDRFA grants 30, 60 or 180 days for AED 200 to 400 plus VAT and an AED 1,000 deposit [V0044, V0139, V0140].

> **Need to know**
> - Do UAE exhibitions (for example Gulfood) currently get Events Visit Visas approved for Bangladeshi participants?

### Scams

**Done to business travellers.** Invitations and "exhibition visas" sold by agents without a real host cannot be checked by the traveller except through the issuing authority (see Tourist visa, Step 4) [V0188, V0189].

> **Need to know**
> - What fake "business" or "exhibition" visa schemes target Bangladeshis going to the UAE?

### Don't work

Meetings and exploring are allowed; work is not (see Tourist visa, Don't work) [V0179, V0169].

## Medical visit

**Status, November 2026:** visit visas for Bangladeshis are restricted [V0001]; the UAE ambassador promised flexibility for humanitarian cases raised by Bangladeshi authorities (May 2025) [V0016].

A licensed UAE hospital applies for the patient, single or multiple entry; in Dubai the visa is for 90 or 180 days [V0141, V0142, V0143].

### Step 1: Get the hospital to sponsor you

You'll need:

- a passport copy (valid 6 months) and a photo [V0143, V0030];
- a medical report [V0143, V0043];
- health insurance [V0143].

The hospital writes the letter justifying the visit and pays the deposit [V0143, V0043].

### Step 2: The hospital applies

- **GDRFA (Dubai):** AED 200 (90 days) or AED 500 (180 days) single entry plus VAT; deposit AED 1,000 single, AED 2,000 multiple [V0146, V0148, V0147].
- **ICP (other emirates):** through "Issuance of a Visa", category licensed healthcare facilities [V0029].

### Step 3: Companions and extensions

A companion enters with the patient on the same type of visa, with the hospital's letter and a copy of the patient's visa; ICP also asks for the health authority's approval letter [V0144, V0043]. The patient's visa can be extended up to 180 days in total [V0056]; the companion's is extended only once, on a certified report that treatment must continue, and only if the patient's is [V0145].

> **Need to know**
> - Which UAE hospitals currently sponsor Bangladeshi patients, and how long do they take?

### Scams

> **Need to know**
> - What medical-visa scams (fake hospital letters, "treatment" visas sold as job visas) target Bangladeshis for the UAE?

### Don't work

No work on a medical visa (see Tourist visa, Don't work) [V0179].

## Mission work visa (temporary work)

**Status, November 2026:** work visas for Bangladeshis are restricted except skilled categories (see Work visa: company worker) [V0001, V0011].

A UAE company registered with MOHRE gets a Mission Work Permit to bring a worker from abroad for a temporary job or time-bound project [V0162, V0149]. It lasts three months, renewable once [V0150]. All skill levels and professions can apply, if the worker is 18 or older and has no active work permit [V0151, V0152, V0153]. You cannot apply yourself: the company applies, and ICP then issues the entry visa (work mission category) [V0149, V0029].

### Step 1: The company applies to MOHRE

You'll need (sent to the company):

- a colour photo with white background [V0158];
- a passport copy valid 6 months [V0158];
- MOHRE's job offer form, signed by you and the employer [V0158];
- certificates for your skill level: bachelor's for levels 1 and 2, diploma for 3 and 4, high school for 5, none for 6 to 9 [V0159];
- a professional licence if the job needs one [V0158].

1. The company applies on the MOHRE website, app or a service centre, which needs an electronic quota [V0154, V0155].
2. MOHRE decides in 2 working days; the company pays the AED 50 federal fee (a centre's commission is capped at AED 72) and a bank guarantee or insurance [V0157, V0156, V0155, V0160].
3. **Check it:** the application status is on mohre.gov.ae (Inquiry), the MOHRE app, or 600590000 [V0161].

### Step 2: The entry visa

ICP's work-mission visa needs an employer certificate, a temporary job contract or letter of purpose, a medical fitness certificate for work, a ticket, and an attested good-conduct certificate for some categories [V0042, V0164]. It can be extended once, with MOHRE's approval [V0057].

> **Need to know**
> - Does a mission-visa worker need BMET emigration clearance, like a worker with a full work visa?
> - Are mission visas being issued to Bangladeshis in 2026?

### Scams

**Done to workers.** A "mission visa" sold as a two-year job is a 3-month permit, renewable once [V0150]. Check the MOHRE offer by its number at inquiry.mohre.gov.ae [V0180].

### Don't work

Work only for the company named on the permit; working for others breaks the permit and the residence law (see Tourist visa, Don't work) [V0174, V0210].

## Transit

**Status, November 2026:** transit visas for Bangladeshis were reported restricted and "almost zero" in October 2025 [V0006, V0003].

Leaving the airport during a connection needs a pre-arranged transit visa for anyone not eligible for visa on arrival, which includes Bangladeshis [V0165, V0022]. It is for 48 or 96 hours, single entry, not extendable [V0167]. It needs a passport valid for the UAE and the next country and an onward ticket [V0168].

1. **Apply** through the UAE airline you fly, a travel agency or an airport hotel [V0166]. Emirates issues it for travel on Emirates tickets out of Dubai, online in "Manage your booking" or at the Emirates Commercial Visa office, Dubai airport Terminal 3 [V0083].
2. **Pay** Emirates US$10 (48 hours) or US$49 (96 hours); transit fees are never refunded [V0074, V0084].

> **Need to know**
> - Can a Bangladeshi change planes in Dubai without a visa if they stay airside?

### Scams

> **Need to know**
> - Are transit visas used to send Bangladeshis to the UAE for work, and at what price?

### Don't work

A transit visa allows no work or overstay (see Tourist visa, Don't work) [V0179, V0045].

## b. Notes (for notes.md)

**Searched:** u.ae visa pages (tourist, transit, medical, jobseeker, explore investment, visa on arrival, track visa, fees and fines, fraud tips); ICP service cards (Issuance of a Visa, job exploration 60/90, business exploration 90, 5-year tourist and family, 14-day visa, extension, cancellation, refund, FAQ, Sept 2025 news); GDRFA service cards (visit visa list, tourist single/multiple, relative/friend, job seeker, business, medical, study, 5-year, GCC residents, June 2026 scam news); MOFA (visa on arrival June 2026; UAE Embassy Dhaka page, whose visa page returns 404); Emirates, Air Arabia, Dubai Airports; Decree-Law 29/2021 and Cabinet Resolution 65/2022; MOHRE mission permit; Bangla and English news (Daily Star, TBS, Dhaka Tribune, Bonik Barta, Jugantor, Samakal, Prothom Alo, Shomoyer Alo, Gulf News, Dhaka Post, KPMG); Bangladesh Embassy Abu Dhabi press release 22 Sep 2025 (read from page image).

**Status: what the sources say, by date.**
- 19-20 July 2024 protests, 57 jailed 22 July 2024 (Prothom Alo 24 Jul 2024, logged by others). Foreign Minister then said the UAE had not stopped visas (news-prothomalo-uae-no-visa-ban, not used).
- Start of the stop: July 2024 (Daily Star 30 Mar 2026, V0001; Bonik Barta, N0071), "after 5 August 2024" (TBS), "since September 2024" (Dhaka Tribune 20 Sep 2025, V0014). Conflict logged; the doc says July 2024.
- 4 May 2025: UAE ambassador said 30-50 visit visas a day from the Dhaka embassy, skilled-employment online system reopened, 500 security-guard visas issued (V0015-V0017). 2025 total: ministry official says none issued (V0002). Conflict logged both ways; doc states both.
- Sept 2025: fake "ban from January 2026" claim from uaevisaonline.com; denied by Bangladesh Embassy (V0205-V0206) and ambassador Tareq Ahmed (TBS, Dhaka Tribune). The Facebook copies still circulating ("UAE announced suspension from January 2026") come from this.
- Oct 2025: ATAB/TOAB say tourist and transit visas almost zero (V0003-V0004).
- Jan 2026: only skill and high-profile visas (Dhaka Tribune, V0011).
- 30 Mar 2026: no visit/work visas in 2025 (Daily Star, V0002).
- No official UAE notice reopening or closing Bangladeshi visit visas found in 2026; no UAE official source at all states a Bangladesh restriction. Family-sponsored visits: no source shows exemptions for families, transit or golden-visa relatives. A Reddit post (blocked) snippet: a resident told by GDRFA that no new entry permits for his Bangladeshi parents had been accepted for two years; not logged (not saved).
- Visa on arrival / US-UK-EU holders: Bangladesh not on any list (V0019-V0021). The June 2026 MOFA expansion added six countries, not Bangladesh.
- 5-year tourist visa: officially "all nationalities" (V0090); Shomoyer Alo (16 Jul 2026) says Bangladeshis are eligible (V0104). No evidence of approvals in practice.

**Conflicts (official vs official):**
- Relative/friend visit total stay: ICP Issuance card 120 days (V0034) vs ICP Extension card 180 days (V0054); KPMG/Gulf News July 2026 says 120 days a year (V0211). Doc shows one Need to know.
- 5-year visa: ICP card says both "90 days + extension, max 180 days a year" (V0095) and "must not exceed 90 days within a single year" (V0106); u.ae, GDRFA and the Executive Regulation say 180. Need to know.
- Emirates' resident-sponsor salary table (AED 4,000 parents/wife/children; 5,500 siblings; 7,000 in-laws; 10,000 friends) differs from ICP's Sept 2025 thresholds (4,000/8,000/15,000). Not logged as a fact (table text); doc uses ICP.
- GDRFA single relative/friend page lists only single-entry fees; KPMG (July 2026) adds multiple-entry AED 300/500/700. Both in doc.

**Page dates.** ICP service cards carry WordPress meta 2024-12-11 (site template) but content includes the Sept 2025 rules, so they are logged possibly-outdated with a note. GDRFA service pages show only a site-wide "last updated" date. sources.csv page_date for uaelegislation-residence-law-29-2021 is 2021-09-27 but the law text says 16 Sep 2021 (facts use 2021-09-16); for uaelegislation-residence-exec-regulation-2022 I entered 2022-05-01 as a placeholder: the true date was not found in the text copy; facts use "undated". Please correct both in sources.csv. Emirates and Air Arabia registered as official=yes (airlines are the visa sponsors for their own service); lead may change to news if preferred.

**Concurrency:** uae-portal-explore-investment-visa registration was lost once (another agent wrote sources.csv at the same time); re-registered. Other agents may want to re-check their registrations.

**What happens in practice:** visit visas were the main irregular work route for Bangladeshis (go on a 3-month visit visa, find work, convert) [V0202, V0013]; agencies sold Tk 1.2-1.5 lakh packages including an "airport contract" to pass Bangladeshi immigration [V0199, V0200] (Dhaka Post, 2021; no newer source found). This route is what the UAE closed.

**Logged but not used:** V0047 (ICP call centre, duplicate of V0190), V0052 (FAQ ranges), V0059 and V0061 (pre-arrival extension fee; 60-day visa non-extendable: only relevant to nationalities not open to Bangladeshis), V0081-V0082 (Emirates AED 1,000 deposit for sponsors without proof), V0105, V0123, V0132, V0163, V0164 partly (Executive Regulation duplicates of service cards), V0196-V0197 (UAE Embassy Dhaka address and phone: House 191, Road 69, Gulshan North Avenue, Gulshan-2; +8802222284295; dhakaemb@mofa.gov.ae; 9 am-4 pm, closed Fri-Sat: for Contacts), V0178 (company fine AED 50,000), V0207 (UAE among frequent refusers: Background), V0007 used in Visas not open.

## c. Blocked pages

- https://www.reddit.com/r/visas/comments/1vsfeq6/has_any_bangladeshi_passport_holder_received_a/ → `sources/forum-reddit-bd-uae-new-visa.html`: worker reports (2026) that GDRFA accepts no new entry permits for Bangladeshi parents; only practice evidence on family visits found.
- https://www.gdrfad.gov.ae/en/services/a01f0970-ba1a-11f0-5210-4cd98f768936 → `sources/gdrfa-relative-friend-visit-visa-2025.html`: GDRFA's new (post-Sept 2025) relative/friend visit card; the saved copy is empty (JS). Would replace KPMG for the Dubai salary thresholds and multiple-entry fees.
- https://www.mofa.gov.ae/en/missions/dhaka/services/Visas → `sources/mofa-uae-embassy-dhaka-visas.html`: returns 404 to scripts; the Dhaka embassy's own visa page.
- https://www.flydubai.com/en/flying-with-us/ok-to-board/ and https://www.flydubai.com/en/flying-with-us/visas-and-passports/dubai-visas → `sources/flydubai-ok-to-board.html`, `sources/flydubai-dubai-visas.html`: flydubai OK-to-board rules for Bangladesh and its visa fees.
- https://www.etihad.com/en-ae/fly-etihad/visas → `sources/etihad-visas.html`: Etihad transit/tourist visa terms.
- https://www.thenationalnews.com/news/uae/2026/08/25/dubai-police-fake-visa-job-offer-warning/ → `sources/news-thenational-dubai-police-visa-scam-2026-08.html`: Dubai Police warning on visa/job scams, 25 Aug 2026.
- Biman Bangladesh Airlines and US-Bangla: any page on OK to Board for UAE (not found online).
- ICP smart services service screens (smartservices.icp.gov.ae, service cards 783, 784, 939, 941, 942, 944-946) are JS-only: a screenshot of the "Issue search for job visa 120 days" card would confirm the 120-day ICP fee and terms.
- Facebook screenshots that would help: UAE Embassy Dhaka page (facebook.com/p/UAE-Embassy-Dhaka-100070103688784) posts on visit visas 2025-2026; Bangladesh Consulate General Dubai and Embassy Abu Dhabi posts on visit visas or family visas for Bangladeshis in 2026.


# W findings: main UAE work route (UAE side) and free-zone employees

Agent W, 8 November 2026. Facts W0001-W0124 in `facts.csv`. Cross-references to other agents' ids: N (corridor status), G (exchange rate). Agent B writes Steps 1, 4 and 6; agent L writes rights and problems after arrival; agent V writes the mission visa section.

---

## a. Draft doc text

## Work visa: company worker

The standard work visa is a two-year residence visa, renewable, and only the employer can apply for it [W0057]. It rests on a Ministry of Human Resources and Emiratisation (MOHRE) work permit, which for a worker recruited from abroad is also valid two years, and on a fixed-term contract of at most three years [W0002, W0016]. The employer must be registered with MOHRE and hold an approved quota of work permits [W0065, W0038]. MOHRE sorts jobs into 9 skill levels; most Bangladeshi workers are in levels 6 to 9 (farm, craft and construction workers, machine operators and "simple professions"), which need no certificate [W0018, W0070]. A job counts as skilled only at levels 1 to 5 with a post-secondary certificate, attested, and at least AED 4,000 (about Tk 1.36 lakh) a month [W0019, G0002]. You must be at least 18 [W0004]. The law bars the employer from charging you any recruitment or employment cost, directly or indirectly; the work permit, the AED 3,000 MOHRE bank guarantee, the entry permit and the residence visa are the employer's costs [W0060, W0052, W0035, W0036].

**Is recruitment open now?** See Background ("Is it open now"). In May 2025 MOHRE reopened online work-permit applications for skilled Bangladeshi workers, and BMET cleared 22,030 workers for the UAE in January to September 2026, more than twice the year before [N0075, N0045].

> **Need to know**
> - Is MOHRE issuing new work permits for Bangladeshi workers in skill levels 6 to 9 as of November 2026, or only for skilled levels?
> - Does MOHRE's system currently block or refuse any work-permit applications because the worker is Bangladeshi?

### Step 2: The job offer and contract (MOHRE offer letter)

1. **Get the MOHRE offer letter, not a company letter.** A real UAE job offer is an offer letter issued on MOHRE's system and signed by the company's authorised manager [W0049]. It must be in Arabic, English and a third language you understand, which can be Bengali, and comes with an annex summarising the Labour Law [W0010, W0017]. The employer signs it electronically and sends it to you in Bangladesh, directly or through a recruitment agency [W0011].

   **Check what it says.** The contract built from it must give the employer's name and address, your name, nationality and date of birth, your job, start date, workplace, working hours, rest days, probation, contract length, wage with allowances, annual leave, notice period and how the contract ends [W0121]. After you sign, the employer may not change the offer without your consent [W0009]. An employer who gives MOHRE false information can be fined up to AED 20,000 [W0012].

2. **Sign it.** Workers in skill levels 1 to 3 sign; levels 4 and 5 may give a fingerprint [W0011]. The signed offer goes with the employer's application for the work permit (Step 3) [W0013].

   > **Need to know**
   > - How do workers in skill levels 6 to 9 sign the offer: signature, fingerprint or through the agency?

3. **Check the offer is real before you pay anything.** MOHRE's enquiry site checks a job offer by its reference number [W0050].

   You'll need: the transaction (reference) number printed on the offer [W0050].

   1. Open [inquiry.mohre.gov.ae](https://inquiry.mohre.gov.ae/) [W0050].
   2. Choose "Job offer inquiry" (الاستعلام عن عرض العمل) [W0080].
   3. Enter the number; the result should show the same employer, job and salary as your paper.

   Also check the company exists: search its English and Arabic name on the National Economic Register, [ner.economy.ae](https://ner.economy.ae/) [W0053]. For questions about a contract or recruitment, MOHRE answers on +971 6 802 7666 or ask@mohre.gov.ae [W0054].

   > **Need to know**
   > - Which fields does the MOHRE job-offer enquiry ask for besides the transaction number, and what does it show?

4. **On arrival, sign again; the offer becomes your contract.** You and the employer sign the same offer in the UAE and MOHRE registers it as the binding employment contract; no clause can change unless your rights are not reduced, both of you agree and MOHRE approves [W0014]. Contracts of workers in skill levels 6 to 9 are handed over at a workers' awareness (Tawjeeh) centre [W0074]. You can see your registered contract on MOHRE's enquiry site ("View attested employment contract", عرض عقد العمل الموثق) [W0081].

   > **Need to know**
   > - Must the employer register the contract within 14 days of arrival (u.ae) or within 60 days (MOHRE's service page) [W0015, W0073]?
   > - What does the Tawjeeh session cost in 2026, who pays it, and is it compulsory for levels 6 to 9 [W0122]?

5. **Know the probation rules.** Probation is at most six months; the employer must give 14 days' written notice to end it [W0027]. If you resign in probation to leave the UAE you give 14 days' notice; to move to another UAE employer, one month, and the new employer repays your recruitment cost unless agreed otherwise [W0028].

**Scam:** fraudsters sell "jobs" and "visas" for cash on social media and WhatsApp under unlicensed company names or posing as official bodies [W0124]. A visit or tourist visa never lets you work, and working on one brings fines for worker and employer [W0022].

### Step 3: The employer gets your work permit and entry permit

1. **The employer needs a MOHRE quota.** It opens a MOHRE file and gets an electronic quota of permits; MOHRE sets the number from the company's legal status, premises, projects and needs, after a Taq'eem site evaluation (AED 406) [W0038, W0076].

2. **The employer applies for the work permit.** It uploads your photo, a passport copy valid at least six months, the offer signed by both of you and, for levels 1 to 5 only, your certificates [W0071, W0070]. You must not hold an active UAE work permit with another company [W0039]. MOHRE decides in 2 working days [W0066]. The fees, all the employer's, are [W0067, W0060]:

   - AED 50 application fee;
   - the two-year permit: AED 250 (category 1 company), AED 1,200 (category 2) or AED 3,450 (category 3, companies with violations) [W0006];
   - at most AED 72 to a business (typing) centre for the paperwork [W0068];
   - an AED 3,000 bank guarantee, refunded when your labour card is cancelled [W0035].

   The approval is valid 60 days; if the employer doesn't pay the fees and guarantee in that time it is cancelled automatically [W0037].

   **Why it can be refused.** MOHRE refuses or cancels permits for false documents, a fictitious company or one not doing its licensed business, or one not paying wages through the Wage Protection System [W0005]. Companies accused of human trafficking or with unfit labour housing get no new permits [W0007].

   **The trap.** Within six months of issue the employer may switch the permit to another worker, even of another nationality, up to twice, as long as ICP cancels the first worker's entry permit [W0069]. A permit in your name can therefore be given to someone else.

3. **The entry permit.** With MOHRE's approval the employer gets an electronic employment entry permit from the residency authority: GDRFA (General Directorate of Identity and Foreigners Affairs) for Dubai, ICP (Federal Authority for Identity, Citizenship, Customs and Port Security) for the other six emirates [W0040, W0055]. ICP issues it in 48 hours for AED 300 in fees plus a refundable AED 1,000 guarantee [W0094]. The employer sends it to you electronically [W0051]. You must enter the UAE within 60 days of issue [W0092]. A company that is not really operating is fined AED 20,000 for using entry permits [W0091].

   > **Need to know**
   > - Does the UAE Embassy in Dhaka have any role in employment entry permits for Bangladeshi workers?
   > - Is Bangladesh among the nationalities that must show an attested certificate of good conduct (police clearance) for a work entry permit [W0093]?

4. **Medical before you fly.** The UAE's own fitness test is done after arrival (Step 7) [W0041]. Wafid, the Gulf Health Council's booking system, lists the UAE as a destination for pre-departure medicals in Bangladesh, at $10 for a standard appointment [W0106, W0107].

   > **Need to know**
   > - Do UAE employers or BMET require a Wafid (GAMCA) medical in Bangladesh for UAE work visas in 2026?

5. **How long.** In order:

   1. The employer gets its MOHRE quota (2 working days) [W0076].
   2. The work permit: 2 working days [W0066].
   3. The employer pays within 60 days [W0037].
   4. The entry permit: 48 hours [W0094].
   5. You enter within 60 days [W0092].
   6. Medical, Emirates ID and residence within 60 days of entry (Step 7) [W0089].

   Through the Work Bundle, MOHRE's single platform for permit, residence, medical and Emirates ID, the whole UAE side is meant to take 5 working days and two visits [W0008, W0087].

**What you get back:** an electronic entry permit for employment in your name, and a MOHRE work-permit approval you can check (Step 5) [W0051, W0082].

### Step 5: Check your visa and permit are real

1. **The job offer and work permit:** on [inquiry.mohre.gov.ae](https://inquiry.mohre.gov.ae/), "Job offer inquiry" and "Electronic work permit information" (معلومات تصريح العمل الإلكتروني) [W0050, W0080, W0082]. MOHRE's call centre is 600590000, 24 hours [W0072].
2. **The entry permit:** first see which emirate issued it [W0055].
   - *Dubai:* GDRFA's Visa Status page, [smart.gdrfad.gov.ae/Public_Th/StatusInquiry_New.aspx](https://smart.gdrfad.gov.ae/Public_Th/StatusInquiry_New.aspx) [W0083]. The form is in Arabic. Choose "ملف" (file) and enter the file number, nationality (207 - بنجلاديش, Bangladesh) and date of birth; or choose "طلب" (application) and enter the application number, transaction number, payment date and first name in English [W0084, W0085]. Help: +971 4 313 9999 from abroad, 800 5111 in the UAE [W0058].
   - *Abu Dhabi, Sharjah, Ajman, Umm Al Quwain, Ras Al Khaimah, Fujairah:* ICP's eChannels at [smartservices.icp.gov.ae](https://smartservices.icp.gov.ae/echannels/web/client/default.html#/login) [W0055]. Help: 600522222 [W0059].
3. **The company:** National Economic Register, [ner.economy.ae](https://ner.economy.ae/) (Step 2) [W0053].
4. **After arrival, your Emirates ID application:** at smartservices.icp.gov.ae with the application number starting 010 [W0086].

> **Need to know**
> - What does ICP's eChannels "File validity" check ask for (passport number, expiry date, nationality?) and what does it show for an employment entry permit?
> - Does the GDRFA form accept a search by passport number for an entry permit?

**If a check fails:** stop paying. Report it to MOHRE (+971 6 802 7666, ask@mohre.gov.ae) and, for a Dubai scam, to Dubai Police on 901 or its eCrime platform [W0054, W0123]. The Bangladesh-side complaint routes are in Step 1 ("If an agency or broker takes your money").

### Step 7: After arrival (medical fitness test, Emirates ID, residence, bank account, SIM)

1. **Finish everything within 60 days of entry.** The medical, Emirates ID and residence must be completed within 60 days of arrival or daily fines apply; a residence visa can't be processed while you are outside the UAE [W0089, W0056]. The fine is AED 50 a day [W0033].

   > **Need to know**
   > - Is the deadline 60 days from entry (ICP) or one month (u.ae, "Preparing to work") [W0089, W0021]?

2. **Medical fitness test.** You must be found free of communicable diseases to get residence [W0029]. The tests are HIV, hepatitis B, leprosy, syphilis and tuberculosis (TB), plus pregnancy for domestic workers [W0023]. Residency is refused if HIV or leprosy is positive [W0023]. TB scars or active or drug-resistant TB bring a conditional certificate and a one-year residence while you are treated in the UAE [W0031, W0024]. Abu Dhabi uses a chest X-ray; the Emirates Health Services (EHS) centres in the northern emirates include one [W0030, W0102].

   - *Dubai:* Dubai Health's 25 "Salem" medical fitness centres, including Al Quoz, Al Yalayis Jebel Ali, JAFZA and Al Muhaisnah; premium results in 6 to 24 hours [W0104, W0105].
   - *Sharjah, Ajman, Ras Al Khaimah, Fujairah, Umm Al Quwain:* EHS centres, for example Sahara and Al Khibra (Sharjah), Musheirif (Ajman), Dahan (Ras Al Khaimah), Mena Tower (Fujairah) and Al Madar (Umm Al Quwain); AED 260 plus the centre's fee for workers, result in 24 hours by email and SMS [W0103, W0100, W0101].

   You'll need: a passport photo, your passport and the entry permit copy [W0048].

   > **Need to know**
   > - What happens to a worker found HIV-positive or unfit: who pays the flight home, and is the worker detained first?
   > - What does the Abu Dhabi (Department of Health) visa screening cost?

3. **Emirates ID biometrics.** Your fingerprints and photo are taken for the Emirates ID as part of the same bundle [W0087]. The card costs AED 100 per year of residence, plus AED 100 e-service fee; a typing office adds AED 30 [W0098, W0099].

4. **Residence visa.** ICP issues the work residence for two years: AED 100 application, AED 100 a year and AED 100 e-service fee; it needs the fit result and health insurance [W0096, W0097]. These are employment costs the employer may not pass to you [W0060].

   > **Need to know**
   > - Is the residence still printed in the passport for Dubai-issued visas, or shown only on the Emirates ID [W0042]?

5. **Contract and Tawjeeh.** Workers in skill levels 6 to 9 collect their MOHRE contract at a Tawjeeh (workers' awareness) centre (Step 2, item 4) [W0074]. Check it matches the offer you signed in Bangladesh [W0014].

6. **Keep your passport.** Possession of your own passport is your right [W0026]. If the employer keeps it, see "Your rights at work".

7. **Salary account.** Private-sector wages must be paid through the Wage Protection System (WPS), into a bank, exchange house or other institution licensed by the Central Bank [W0120]. A bank account needs your original Emirates ID and a salary letter, contract or payslip; Emirates NBD, for example, asks for a salary transfer of at least AED 5,000 [W0117, W0116].

   > **Need to know**
   > - Which payroll cards or exchange-house accounts do employers use for workers earning under AED 5,000, and what do they charge?

8. **SIM card.** A normal prepaid or postpaid line needs your Emirates ID under the telecom regulator's (TDRA) rules [W0118]. Until it arrives, buy a visitor or tourist SIM on your passport (e& (Etisalat) visitor line: 90 days) and convert it once you have the Emirates ID [W0118, W0119].

## Work visa: free zone employee

Free zones are business areas with their own authority, such as Jebel Ali Free Zone (Jafza) in Dubai. A free-zone company applies for your work permit and residence visa to the free zone authority, not MOHRE, and the number of visas it can get depends on its package or lease [W0045, W0112]. You are sponsored by the free zone authority, not the company [W0046]. Your job is governed by the free zone's rules together with the federal Labour Law; DIFC and ADGM, the financial free zones, have their own employment law [W0044].

1. **The company applies.** In Jafza, for example, it applies on the Dubai Trade portal with your passport copy and photo, and an attested degree only for managerial or professional jobs [W0114]. The residence is valid up to three years [W0112]. Jafza's normal package costs the company AED 2,378 for one year or AED 2,678 for two [W0114].
2. **After you land,** the company reports your arrival and receives a DHA (Dubai Health Authority) medical form, your employment contract and medical and Emirates ID appointments; once you are fit it uploads your health insurance card and entry permit to finish the residence [W0115].
3. **Work only in the free zone.** A Jafza-sponsored worker may work only inside the zone unless Jafza approves temporary outside work [W0113].
4. **Check it is real** the same way as Step 5: Dubai free-zone entry permits on GDRFA, others on ICP [W0055].

> **Need to know**
> - Which free zones employ most Bangladeshi workers (Jafza, SAIF Zone, Hamriyah, RAKEZ, KEZAD)?
> - Does a free-zone worker file wage complaints with MOHRE or with the free zone authority?

---

## For Step 1 / Step 4 / Step 6 (agent B)

- **Demand letter attestation (Dubai and northern emirates).** Any UAE company recruiting Bangladeshis must have its demand letter attested by the Consulate General of Bangladesh in Dubai [W0108]. It submits: an application to the Consul General, the demand letter on letterhead, a letter of authorization, a copy of the agreement, the contract (offer letter), a guarantee letter, the company licence and the recruiting agency's licence [W0109]. Fee AED 221, cash, non-refundable; the sponsor, partner, HR manager or PRO must attend in person, Room 14, Monday to Thursday 9 am to 3 pm, Friday 9 to 11.30 am [W0110]. Consulate: Villas 36 & 145, Abu Hail Road, Al Wuheida, Deira, Dubai; +971-4-2388199; mission.dubai@mofa.gov.bd [W0111]. Abu Dhabi embassy equivalent not checked by W.
- **UAE-side checks a worker can do in Step 1:** MOHRE job offer enquiry, National Economic Register (Step 2, item 3) [W0050, W0053].
- **Certificates (Step 4):** only levels 1-5 need certificates; certificates from abroad are attested by Bangladesh's Ministry of Foreign Affairs and then the UAE Embassy [W0070, W0025]. Passport must have at least six months' validity [W0020].
- **Police clearance (Step 4):** ICP lists "a certificate of good conduct, duly attested as required, according to the announced categories" for work/mission entry visas [W0093]; whether Bangladesh is covered is open.
- **Medical (Step 4/6):** Wafid lists the UAE as a destination from Bangladesh [W0106]; whether BMET requires it for UAE clearance is for B.
- **UAE recruitment agencies:** recruiting or intermediating without a MOHRE licence is illegal; licensed agencies lodge AED 300,000 (intermediation) or AED 1 million (outsourcing) guarantees and lose their licence for forced labour, trafficking or unpaid wages [W0061, W0063, W0064].

---

## b. Notes (for notes.md)

**Searched:** u.ae (work permits, job offers, skill levels, preparing to work, contracts, residence visa provisions, health conditions, recruiting mainland/free zones, fraud tips, track visa); MOHRE service pages (blocked to curl and Firecrawl; got Wayback copies of overseas permit, contract issuance, quotas, mission, temporary permit, classification news, inquiry site); ICP (FAQ, residency permit, visa issuance, 2024 services guide PDF); GDRFA visa status form; EHS and Dubai Health medical fitness; Wafid; Jafza guides; Bangladesh Consulate Dubai; Emirates NBD; Gulf News (SIM); The National (Dubai Police scam warning); Fragomen (Tawjeeh, 2018). Bangla searches ("আমিরাত কাজের ভিসা বাংলাদেশি ২০২৬") returned mostly agency/YouTube pages; corridor status left to agent N.

**Text copies rebuilt:** for MOHRE Wayback pages (and EHS, GDRFA form) fetch.py's cleaner removed the `<form>` holding the content, leaving near-empty .txt files. W rebuilt each `.txt` from the saved `.html` (visible text, scripts/styles removed; first line notes this), so quotes are checkable: mohre-new-work-permit-overseas, mohre-news-classification-2022, mohre-mission-work-permit, mohre-home, mohre-employment-contract-issuance, mohre-work-permit-quotas, mohre-temporary-work-permit, ehs-medical-fitness-residency, gdrfa-status-inquiry-form.

**Conflicts:**
- Contract registration deadline: u.ae 14 days after arrival (W0015) vs MOHRE service 60 days after entry (W0073).
- Time to complete residence: u.ae "within one month of entering" (W0021) vs ICP 60 days from entry (W0089, W0095).
- Residence in passport: u.ae recruiting page (27 Oct 2026) says the residence visa is "stamped in the employee's passport" (W0042); Jafza still speaks of "Residence Stamping" (W0115); news (Gulf News, May 2022; Keesing) reports ICP replaced stickers with the Emirates ID from April/May 2022, Dubai excluded at first. Gulf News and Keesing could not be downloaded.
- Free-zone law: u.ae "Working in free zones" (Aug 2026) says free-zone workers are generally not under the Labour Law (W0047) and are sponsored by the authority (W0046); u.ae "Recruiting in free zones" (27 Oct 2026) says free-zone rules apply together with the Labour Law (W0044). Draft uses the newer wording.
- Medical tests: u.ae "Health conditions" (W0029) limits syphilis/hepatitis B to nursery, domestic, food, salon, health-club workers; "Preparing to work" (W0023) lists them for all. Abu Dhabi X-ray vs "Dubai does not" (W0030) while Dubai Health/EHS run X-rays (W0102).
- Tawjeeh: Fragomen 2018 says levels 3-5 must attend, AED 203 (W0122); MOHRE 2026 delivers contracts of levels 6-9 at awareness centres (W0074).
- u.ae says MOHRE has "13 types" of work permits but lists 12 plus the private-teacher permit; the executive regulation lists 12 (a-l).

**Practice:** Dubai Police (Aug 2026) warns of fake job/visa offers via social media and WhatsApp (W0123, W0124). The six-month permit replacement rule (W0069) is the legal basis for a slot "changing name"; no Bangladesh-specific report found. No source found on what Bangladeshi workers pay in the UAE for Tawjeeh, medical or Emirates ID when employers pass costs on.

**Logged but not used:** W0001 (13 types), W0003 (Article 6 basic rule), W0034 (visa cancellation; for agent L "leaving"), W0032 (180 days outside; for L "going home on leave"), W0062 and W0077 (mission permit; for agent V), W0078-W0079 (classification news 2022; superseded by W0067), W0088 (urgent ID AED 150), W0090 (status change AED 500; for "changing employer"), W0043 (entities), W0097/W0099 duplicates, W0122 (old Tawjeeh).

## c. Blocked pages

- https://www.mohre.gov.ae/en/services/recruiting-a-worker-from-overseas-2022 (curl and Firecrawl time out; Wayback copy of Jan 2026 used) -> sources/mohre-new-work-permit-overseas-live.html: confirms current fees.
- https://inquiry.mohre.gov.ae/ (English view, and the "Job offer inquiry" form) -> sources/mohre-inquiry-job-offer-form.html (screenshot): exact fields to type.
- https://smartservices.icp.gov.ae/echannels/web/client/default.html (Public services > File validity form) -> sources/icp-file-validity-form.png (screenshot): fields and result.
- https://www.ehs.gov.ae/EN/services/services-directory/examination-of-medical-fitness-for-residency-visa (live) -> sources/ehs-medical-fitness-live.html: current fee (Wayback Jan 2026 used).
- https://gulfnews.com/uae/government/now-emirates-id-replaces-residence-visa-sticker-in-passport-of-uae-residents-except-in-dubai-1.87920236 -> sources/news-gulfnews-emirates-id-replaces-sticker-2022.html: sticker question.
- https://www.doh.gov.ae (visa screening fees, Abu Dhabi) -> sources/doh-visa-screening.html.
- Facebook screenshots wanted: MOHRE UAE (facebook.com/MOHREUAE) posts on overseas work permit steps 2026; Bangladesh Embassy Abu Dhabi labour wing posts on demand attestation and on UAE work visas for Bangladeshis 2026; Bangladesh Consulate Dubai posts on "visa open/closed" notices.


# FAQ test: does the doc answer what Bangladeshis actually ask?


Date: 8 November 2026. Tested file: `doc.md` (1,832 lines). Method: 9 Firecrawl web searches (English and Bangla) to collect the questions that show up as Bangla news headlines, YouTube/Facebook video titles, agency blogs and Quora; then each question was searched in doc.md (Grep/Read) and judged as a chatbot that may answer only from the doc.

- **ANSWERED** = direct, specific, actionable answer in the doc.
- **PARTIAL** = some of it, or only "unknown/restricted" without the practical how.
- **NOT ANSWERED** = nothing usable.

Searches run: "দুবাই ভিসা খোলা ২০২৫ বাংলাদেশ"; "UAE visa Bangladeshi 2025 open ban work visa cost"; "দুবাই ভিসা চেক করার নিয়ম পাসপোর্ট দিয়ে"; "দুবাই কাজের ভিসা খরচ কত টাকা বেতন কত"; "আমিরাত ছুটিতে দেশে এসে ভিসা বাতিল প্রবাসী"; "দুবাই ফ্যামিলি ভিসা বেতন কত লাগে বাংলাদেশি"; "আমিরাত ভিসা ওভারস্টে জরিমানা ক্ষমা সাধারণ ক্ষমা বাংলাদেশি"; "দুবাই ভিজিট ভিসা থেকে কাজের ভিসা করা যায় কি / BMET smart card Dubai"; "দুবাই ভিসা প্রতারণা দালাল ভুয়া ভিসা আমিরাত".

## The 15 questions

### 1. দুবাই ভিসা কি খোলা? কবে খুলবে? (Is the UAE/Dubai visa open for Bangladeshis now?)
- **Evidence:** visanewsbd.com/dubai-visa-update ("দুবাই ভিসা কবে খুলবে ২০২৬"); saudijabo.com/blog/dubai-visa-2026-bangladesh ("দুবাই ভিসা খোলা আছে কি?"); kalbela.com/national/224678 ("বাংলাদেশিদের জন্য সহজেই খুলছে না দুবাইয়ের ভিসা"); YouTube njDpNIhW3JY ("আমিরাতের ভিসা কবে চালু হচ্ছে, জানালেন রাষ্ট্রদূত"); ndtv.com "Did UAE Suspend Tourist, Work Visas For Bangladesh?".
- **Verdict: ANSWERED.**
- **Doc:** lines 11-17 (status on 8 Nov 2026), 32-38 (visa by visa), 126-133 (visas not open).
- **Answer:** partly open; no published ban, but tourist, family, student, most work visas and transfers restricted since July 2024; bulk employer visas (Dubai Taxi, construction) and skilled visas still moving; 23,044 BMET clearances in 2026 to 7 Nov.
- **Missing:** nothing critical (the doc itself flags why October-November clearances fell).

### 2. দুবাই কাজের ভিসায় যেতে কত টাকা লাগে? (How much does a Dubai work visa cost from Bangladesh?)
- **Evidence:** bn.quora.com "দুবাইতে ওয়ার্ক পারমিটে যেতে মোট কত টাকা লাগে?"; obokash.com/dubai-visa-from-bangladesh (BDT 1,45,000 + deposit); dubaivisitsvisa.com "Dubai Work Visa for Bangladeshi Nationals 2026".
- **Verdict: ANSWERED.**
- **Doc:** lines 9, 84-88, 137, 195-196.
- **Answer:** government cap Tk 1,07,780 (a 2025 permission letter set Tk 71,840); the employer must pay all UAE costs; in practice Dubai Taxi drivers pay at least Tk 3.5 lakh and Middle East jobs Tk 5-7 lakh; pay by bank, late.
- **Missing:** the 2026 street price of an ordinary company visa, a "free visa" or a partner visa (doc's own Need to know, line ~95). Nothing on the "security deposit" agencies demand (obokash: AED 3,025).

### 3. পাসপোর্ট নাম্বার দিয়ে দুবাই ভিসা চেক করব কীভাবে? (How do I check my Dubai visa with my passport number?)
- **Evidence:** ezyorbit.com/dubai-visa-check ("পাসপোর্ট নাম্বার দিয়ে দুবাই ভিসা চেক করার নিয়ম ২০২৬"); YouTube 7NWLoX1Ob2k and Facebook videos "দুবাই ভিসা চেক করুন | UAE Visa Status Check 2026"; Facebook "Dubai visa check bd! কিভাবে দুবাই ভিসা চেক করবো!".
- **Verdict: PARTIAL.**
- **Doc:** lines 335-346 (work), 887-895 (tourist), 619-622 (on leave).
- **Answer given:** MOHRE inquiry for the work permit; GDRFA Status Inquiry (Arabic form, by file number or application number, nationality code 207); ICP File Validity, which has a "Passport Information" option.
- **Missing:** the exact thing people ask: a check by passport number. The doc says it does not know whether GDRFA accepts a passport number (line 346) or which fields ICP asks for under "Passport Information" (line 345). It also does not say what a valid, cancelled or fake result looks like. A worker holding only a passport and a PDF visa can't finish the check from the doc.

### 4. দুবাইতে বেতন কত? কোন কাজে বেতন বেশি? (What salary do Bangladeshi workers get in Dubai?)
- **Evidence:** Facebook Emiratessangbad "দুবাই শ্রমিকদের বেতন প্রসঙ্গ" (1,500 dirham salary, food costs); YouTube yRmrnzGfKkI ("দুবাইতে কোন চাকরিতে কত বেতন?"); munnifreelancer.com "দুবাই কোন কাজের চাহিদা বেশি ও বেতন বেশি ২০২৫".
- **Verdict: PARTIAL.**
- **Doc:** lines 90-92, 169 (Transguard 2025 permission letter: mason AED 1,150, helper/cleaner AED 800, electrician AED 1,400), 428 (no minimum wage).
- **Answer given:** taxi drivers AED 2,500-4,000; one employer's basic pay by trade; BBS first-3-month averages Tk 23,629-29,477; 44% got less than promised.
- **Missing:** a 2026 pay range for the common jobs (construction helper, cleaner, security guard, salesman, delivery rider), what is deducted for food and housing, and what a worker can send home each month. The doc flags this itself (line ~93-94, questions.md line 12).

### 5. দুবাই ট্যুরিস্ট/ভিজিট ভিসার খরচ কত, কী কাগজ লাগে? (Tourist/visit visa cost and papers)
- **Evidence:** Facebook group post "UAE employment visa requirements for Bangladeshi citizens" (30-day visit AED 950); bn.y-axis.com/visa/visit/dubai ("দুবাই ট্যুরিস্ট ভিসা – খরচ"); munnifreelancer.com (visit visa "সত্তর হাজার থেকে..."); saudijabo.com ("দুবাই টুরিস্ট ভিসা: বাংলাদেশ থেকে আবেদনের নিয়ম").
- **Verdict: ANSWERED.**
- **Doc:** lines 828 (status), 836-882 (sponsor, papers, fees), 881 (Tk 1-2 lakh packages against about Tk 11,600 official).
- **Answer:** effectively stopped for Bangladeshis since mid-2024; if attempted, an airline, UAE agent or hotel must sponsor; GDRFA AED 200-500 plus VAT, Emirates US$90-231; papers listed.
- **Missing:** whether the Tk 1-2 lakh packages actually deliver visas in 2026 (doc's Need to know).

### 6. ভিজিট ভিসায় গিয়ে কাজের ভিসা করা যায়? (Can a visit visa be converted to a work visa?)
- **Evidence:** saudijabo.com heading "দুবাই ভিজিট ভিসা থেকে ওয়ার্ক ভিসা করা যায় কি?"; Facebook visainformation1 "দুবাই ভিজিট ভিসায় যাওয়ার সহজ উপায়"; munnifreelancer.com.
- **Verdict: ANSWERED.**
- **Doc:** lines 119-120 (myth), 133, 197 (Ministry warning), 1442.
- **Answer:** no; closed to Bangladeshis for several years; working on a visit visa brings fines; brokers use this promise.
- **Missing:** nothing.

### 7. BMET কার্ড কীভাবে পাব? ভিজিট ভিসায় দুবাই যেতে কি BMET কার্ড লাগে? (BMET smart card: how, cost, and needed on a visit visa?)
- **Evidence:** Facebook visainformation1 "বিএমইটি কার্ড কিভাবে পাবেন? ভিজিট ভিসায় দুবাই যেতে লাগবে ম্যানপাওয়ার কার্ড" (also YouTube Us7CcB7lhEo); Facebook "কিভাবে BMET কার্ড দিয়ে দুবাই যাবেন".
- **Verdict: PARTIAL.**
- **Doc:** lines 145-160 (OEP registration), 352-365 (clearance, fees, individual visa, check), 909 (airport offload), 1641.
- **Answer given:** for a work visa the route is complete: OEP registration Tk 200, PDO, clearance within 3 days, welfare fee Tk 5,500, insurance Tk 1,000, individual-visa papers, online check.
- **Missing:** the visit-visa half of the question, which is what the video titles ask. Does a visit-visa traveller need, or can they get, a BMET/manpower card? Does airport immigration demand one? The doc only says visit-visa migrants have no BMET clearance (line 1641) and that immigration offloads doubtful visitors (line 909).

### 8. ছুটিতে দেশে এসে আমিরাতের ভিসা বাতিল হয়ে গেছে, এখন কী করব? (My visa was cancelled while I was home on leave)
- **Evidence:** amadershomoy.com/migrants/article/201230 ("ছুটিতে এসে আমিরাতের ভিসা বাতিল, কর্মস্থলে ফিরতে ৬৬০০ প্রবাসীর..."); bangla.thedailystar.net/news/bangladesh/news-3961601; ekhon.tv (protest); Facebook new.probashbangla "ছুটিতে এসে আরব আমিরাতের ভিসা বাতিল প্রবাসীদের যে বার্তা দিল আবুধাবি দূতাবাস".
- **Verdict: PARTIAL.**
- **Doc:** lines 15-29 (counts, reasons), 613-633 (Going home on leave), 650-652 (reinstatement scam).
- **Answer given:** check the visa before flying (GDRFA/ICP); send details to the Embassy's designated email; ask the employer; reinstatement isn't guaranteed and only the UAE can do it; claim wages through labourwingauh@gmail.com.
- **Missing:** the key contact. The doc does not give the Embassy's designated email address or the details to send (its own Need to know, line ~632). It also has no reinstatement process, no word on whether gratuity can be claimed from Bangladesh, and no word on whether the person can come back on a new visa. This is the most-reported UAE story of 2026, and the bot can't give the one address people need.

### 9. দুবাইতে ফ্যামিলি ভিসা করতে বেতন কত লাগে? (What salary is needed to bring wife/children?)
- **Evidence:** YouTube mjNRzsH3DEY ("দুবাই ফ্যামিলি ভিসা আপডেট | Dubai Spouse Visa"); Facebook hellowdubai2020 ("দুবাইতে কিভাবে কম খরচে ফ্যামিলি ভিসা করবেন? ... কত খরচ হবে আর কি লাগবে"); Instagram DeFEXnRkfH6 ("দুবাইয়ে ফ্যামিলি ভিজিট ভিসায় বেতনের নতুন শর্ত").
- **Verdict: ANSWERED.**
- **Doc:** lines 635-637, 1099-1112 (status and sponsor rules), 1116-1162 (attestation, papers, fees), 1041-1049 (family visit: AED 4,000 / 8,000).
- **Answer:** AED 4,000 a month, or AED 3,000 plus employer housing, plus suitable housing; attest the nikahnama and birth certificates (MoFA, then UAE MOFA, AED 300 each); GDRFA AED 200 plus VAT; restricted and stalled for Bangladeshis since July 2024.
- **Missing:** whether any Bangladeshi applications are being approved now (doc's Need to know); VFS fee in Taka.

### 10. আমিরাতে ভিসার মেয়াদ শেষ হলে জরিমানা কত? সাধারণ ক্ষমা কবে? (Overstay fines and amnesty)
- **Evidence:** kalbela.com/probash/152171 ("আমিরাতে সাধারণ ক্ষমার মেয়াদ শেষ"); prothomalo.com ("সাধারণ ক্ষমা পেয়েছেন ৫০ হাজার বাংলাদেশি"); dhakatimes24.com 2024/08/29 ("আমিরাতে সাধারণ ক্ষমার সুযোগ, যা করতে হবে বাংলাদেশিদের"); Facebook bdprobasiu ("ফাইন মাফ | গ্রেস প্রিয়ড | সাধারণ ক্ষমা").
- **Verdict: ANSWERED.**
- **Doc:** lines 1516-1521, 1523-1573 (outpass, check and pay fines, exit permit), 1628-1636 (bans).
- **Answer:** AED 50 a day after a 30-day grace period (60 or 90 days for some); last amnesty 1 Sep-31 Dec 2024, none announced since; check fines on GDRFA with a passport number; outpass AED 60 same day at Dubai Consulate; exit permit AED 200-241, fly within 7 days.
- **Missing:** whether an ordinary (non-amnesty) leaver gets an entry ban, and how to check a ban from Bangladesh (doc's Need to know).

### 11. দুবাই যেতে কি গ্র্যাজুয়েশন সার্টিফিকেট লাগে? সার্টিফিকেট সত্যায়ন কীভাবে? (Do I need a degree certificate, and how to attest it?)
- **Evidence:** zilhajjgroup.com "বাংলাদেশিদের জন্য দুবাইয়ের ভিসা কি সত্যিই বন্ধ?" ("যাদের হাতে original graduation certificate আছে, তারা এখনও legal way তে দুবাই আসতে পারেন"); saudijabo.com (skilled-profession visas only).
- **Verdict: ANSWERED.**
- **Doc:** lines 137 (levels 6-9 need no certificate; levels 1-5 need an attested post-secondary certificate and AED 4,000), 312-325 (attestation chain: mygov.bd Tk 200/page, MoFA consular sticker, UAE MOFA online; e-Apostille not accepted; verify.mofa.gov.ae), 664, 1033 (fake degree is a crime).
- **Answer:** only skilled jobs need it; attestation steps given.
- **Missing:** UAE Embassy fee and time per certificate (doc's Need to know).

### 12. দুবাই যেতে বয়স কত লাগে? (Age limit for going to Dubai)
- **Evidence:** YouTube fFdXW50ud_4 ("... দুবাই যেতে বয়স কত লাগে? নতুন ..."); age is a stock question in Bangla visa videos.
- **Verdict: PARTIAL.**
- **Doc:** line 137 (at least 18), 163 and 675 (domestic workers: clearance age 25-45, at least 18), 210 (PKB loan 18-60), 472 (upper age: Need to know).
- **Answer given:** minimum 18; women domestic workers 25-45.
- **Missing:** any upper age for men on work visas or for renewal. The doc says it doesn't know (line 472).

### 13. দুবাইয়ের ৫ বছরের মাল্টিপল এন্ট্রি ভিসা কি বাংলাদেশিরা পাবে? (5-year multiple-entry visa)
- **Evidence:** Facebook DPostOnline and YouTube ZfjkvRliTWI ("দুবাই ভিসা কবে খুলবে বাংলাদেশের জন্য? মাল্টিপল-এন্ট্রি ভিসা চালু করলো আমিরাত"); saudijabo.com source list ("৫ বছরের মাল্টিপল এন্ট্রি ভিসা").
- **Verdict: ANSWERED.**
- **Doc:** lines 938-956.
- **Answer:** open to all nationalities; USD 4,000 balance for 6 months, UAE health insurance, self-apply on ICP/GDRFA, AED 3,713 total including a refundable AED 3,000 guarantee; up to 90 days a visit.
- **Missing:** whether any Bangladeshi has actually got one since mid-2024, and whether the yearly limit is 90 or 180 days (both flagged by the doc).

### 14. ট্রান্সফার ভিসা কি চালু? কোম্পানি পরিবর্তন করা যায়? (Is visa transfer / changing company open?)
- **Evidence:** Facebook hellowdubai2020 ("ট্রান্সপার ভিসা কি চালু হয়েছে...? ... কি এক কোম্পানি থেকে ..."); minister's statement that transfers are stalled (cited across news).
- **Verdict: ANSWERED.**
- **Doc:** lines 15 and 104 (transfers restricted for Bangladeshis since July 2024), 549-578 (when you can move, probation, steps, one-year ban, check ban on 600590000).
- **Answer:** legally possible at contract end or lawful termination, through a new MOHRE offer and transfer permit (2 working days, about AED 50); but restricted for Bangladeshis since July 2024.
- **Missing:** whether any Bangladeshi transfers are approved in 2026 and on what terms.

### 15. দুবাই ভিসা দেওয়ার নামে প্রতারণা চিনব কীভাবে? "বাংলাদেশসহ ৯ দেশে ভিসা বন্ধ" খবর কি সত্য? (Spotting visa scams and fake ban news)
- **Evidence:** Facebook MorurGolpo ("দুবাই ভিসা দিচ্ছে বলে মিষ্টি কথা শোনাচ্ছে? সাবধান!"); YouTube 63MoOpcNPxg ("প্রতারকদের নতুন কৌশল! দুবাই ভিসা করতে গেলে সাবধান"); Facebook Ismailvaivlog ("দুবাই ভিসা বন্ধ করে দিল বাংলাদেশসহ ৯টি দেশের"); Facebook vicglobalbd ("কাদের জন্য বন্ধ হলো দুবাই ভিসা?").
- **Verdict: ANSWERED.**
- **Doc:** lines 118 (the January 2026 ban was false), 639-658 (scams: free visa, fake smart card, reinstatement for a fee, ban/open posts, ticket gouging; checks and report lines), 191-200 (before paying), 202 (16135, BMET complaint).
- **Answer:** check the MOHRE offer, entry permit and smart card online; the ban claim came from a private website; report to MOHRE, Dubai Police 901 / eCrime, 16135.
- **Missing:** how the UAE Embassy in Dhaka verifies an agency (doc's Need to know, line ~852).

## Counts

| Verdict | Count | Questions |
|---|---|---|
| ANSWERED | 10 | 1, 2, 5, 6, 9, 10, 11, 13, 14, 15 |
| PARTIAL | 5 | 3, 4, 7, 8, 12 |
| NOT ANSWERED | 0 | none |

## Top 3 gaps worth fixing

1. **Visa cancelled on leave: the Embassy's designated email and what to send (Q8).** This is the biggest UAE story of 2026 (about 5,000-6,600 cases). The doc tells people to email the Embassy but gives no address, no list of details to send and no reinstatement process. Fix: find the Abu Dhabi Embassy / Dubai Consulate notice that gives the address and required fields (passport, UID/file number, Emirates ID, employer), and add it to lines 624-628.
2. **Checking a Dubai visa by passport number (Q3).** This is the most-searched how-to; every Bangla tutorial is titled "পাসপোর্ট নাম্বার দিয়ে". The GDRFA form in the doc needs a file or application number, and the passport search is unconfirmed (line 346). Fix: test the GDRFA and ICP "Passport Information" forms (or the GDRFA app/Amer check), record the fields and what a valid or cancelled result shows, and add the fallback (BMET's free visa check at DEMO, line 189).
3. **Pay and take-home for common jobs, plus BMET card on a visit visa (Q4, Q7).** People ask "বেতন কত" and "ভিজিট ভিসায় BMET কার্ড লাগবে?" The doc has one 2025 permission letter and the taxi figure, but no 2026 range for helper, cleaner, guard or rider net of food and housing. It also says nothing on whether visit-visa travellers need or can get a BMET card at the airport. Fix: add a 2026 pay table from recent BMET permission letters or labour-wing data, and one line on BMET rules for visit-visa travellers.

Smaller: upper age limit for men (Q12, line 472).
