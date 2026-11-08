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
