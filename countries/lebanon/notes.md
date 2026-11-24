# Lebanon: research notes

## What this version is built from

19 Prothom Alo articles (January 2024 to May 2026) from the archive chunk xchunk-lebanon.jsonl, read in full; 17 used, 78 facts logged (XL0001 to XL0078), all cited [N] as news. No official source has been fetched yet and no network research was done for this version.

The reporting covers the 2024 war and evacuation (registration with the embassy, IOM's role, flights, numbers, the exit-pass fine for irregular workers), deaths in the 2024 and 2026 wars and how one body was brought home, the size of the community, and embassy services (service week, public hearing, health camp, remittance awards). It says nothing on how Lebanon jobs are recruited in Bangladesh, costs, wages, the visa or work-permit process, BMET clearance, or rights at work; those are "Need to know" items in the doc.

## Where the official research pass should start

- Lebanon's Ministry of Labour (work permits for foreign domestic and other workers, the standard unified contract for domestic workers, complaint line) and General Directorate of General Security (residence permits, kafala sponsorship, exit and overstay fines, amnesty or fine waivers granted in 2024).
- Bangladesh Embassy in Beirut: address, phone and WhatsApp hotline, labour wing services, its 2024 evacuation notices and registration method, Facebook notices on 2026 deaths.
- BMET: clearance figures for Lebanon by year and by sex (2015 to 2026), any ban or restriction on sending women domestic workers, permission letters for Lebanon.
- Ministry of Foreign Affairs press releases on the 2024 evacuation (October 2024 to January 2025) and on the April and May 2026 deaths.
- Wage Earners' Welfare Board: death compensation and body repatriation rules (Tk 35,000 burial, Tk 3 lakh), and whether they apply to workers without BMET clearance.
- IOM Bangladesh and IOM Lebanon: the 2024-25 return programme and reintegration help for returnees.
- ILO and Lebanese NGOs (KAFA, Anti-Racism Movement) on Bangladeshi domestic workers' wages, passport retention and the kafala system.
- RMMRU: source of its 150,000 estimate.

## Resolved conflicts

- **Size of the community:** 70,000 to 100,000 (Foreign Adviser and embassy press release, October 2024) [XL0017, XL0041]; about 100,000 (Expatriates' Welfare Adviser, October 2024) [XL0026]; about 150,000, over half women (RMMRU, April 2026) [XL0058]. Different sources and dates; not truly in conflict since all are estimates. The doc gives each with its source and date.
- **When Dipali Begum went to Lebanon:** the April 2026 articles say "two years ago" [XL0053]; the May 2026 article says 2011, at 19 [XL0073]. The 2011 figure is specific and consistent with her age of 34; "two years ago" may refer to her latest departure. Not settled from these articles, and it changes nothing a migrant would do, so the doc gives neither date. XL0053 is left uncited.
- **Her name:** Dipali Begum (most articles) vs Dipali Akter (12 April and 5 May articles); father named differently too. Same person (same age, village, date and place of death). The doc uses "Dipali Begum".
- **Flight counts in the 2024 evacuation:** 697 people on 11 flights by 21 November 2024 [XL0045] but 963 on 9 flights by 5 December 2024 [XL0046]; 1,246 on 19 flights by 17 January 2025 [XL0050]. The people counts rise consistently; the flight counts don't. The doc gives people counts, and the flight count only for the final total.
- **First flight:** expected 53 on 20 October (Foreign Adviser, 17 October) [XL0017 article], actually 54 on 21 October [XL0023]. The actual figure is used.
- **Where the 11 May 2026 drone struck:** the embassy-based report of 11 May says a residence in Zebdine [XL0074]; the Satkhira district report of 12 May says a vehicle carrying bread [XL0087]. The earlier report quotes the embassy, so the doc keeps "residence"; it changes nothing a migrant would do. XL0087 is left uncited.
- **Wanting to return:** about 1,000 (initial information, 9 October 2024) [XL0013], then 1,800 registered (17 to 31 October) [XL0017, XL0037]. A rising count, not a conflict; the later figure is used.

## Facts logged but not cited

- XL0007 (many workers attended the embassy event): no bearing on a decision.
- XL0013 (early 1,000 estimate): superseded by the 1,800 registrations.
- XL0053 (departure "two years ago"): see Resolved conflicts.

## Articles not used

- 0fbd40c4 (24 Feb 2024): the embassy's International Mother Language Day event in Beirut; ceremonial, nothing a migrant would act on.
- 653aea8d (12 May 2026): a shorter duplicate of 952f0096 (the two Satkhira workers killed in Nabatieh).

## Official research pass, 24 November 2026

### What was searched
- Lebanon's General Directorate of General Security (general-security.gov.lb, English pages): residence, domestic workers, sponsorship transfer, "leaving the workplace" (absconding) complaints, departure certificates, clearance certificates for violators, regularisation for departure, residence fees, visa types, entry of nationals from labour-supplying countries, hotline 1717. All downloaded directly. Two pages (residence fees, entry of labour-supplying countries) keep their data in HTML tables that pandoc drops; a plain-text copy (`.txt`) was made from the saved HTML so the quotes can be checked (bs4 is not installed, so `fetch.py` did not make one).
- Lebanon's Ministry of Labour (labor.gov.lb): blocked by Cloudflare (403); the FAQ and complaints pages were saved from the Wayback Machine (official, archived).
- Bangladesh Embassy in Beirut (beirut.mofa.gov.bd): home, office hours, officers, press releases, consular fees, regularisation notices (January 2024), dead-body repatriation guide. The notices are scanned PDFs with no text layer: the two English notices were OCR'd with tesseract and checked against the page images (the fee table on page 1 and the contact line on page 2 of the 29 January notice were transcribed from the image); the one-page Bangla guide and the consular fee chart were transcribed by hand from the images. The Bangla version of the regularisation notice (emb-regularization-bn-pdf) was downloaded but not transcribed; the English versions cover the same notice.
- BMET: the country-wise table "Overseas Employment & Remittances (2004 to May 2025)" image; the Lebanon column transcribed by hand (bmet-annual-by-country-2025-05-lebanon.md). No split by sex was found for Lebanon.
- Wage Earners' Welfare Board: Tk 3 lakh grant, Tk 35,000 transport and burial, help bringing bodies home, compensation recovery.
- ILO and NGOs: ILO "For a fee" (2015) on recruiting Bangladeshi women for Lebanon and Jordan; ILO news on the 2020 Standard Unified Contract and the 2015 hotline 1740; Amnesty International and Human Rights Watch on the suspension of the 2020 contract.
- News: Dhaka Tribune on the August 2024 ban and its lifting in March 2025; L'Orient Today on the June 2025 exit-fine waiver (via Wayback).

### What changed in the doc
- New Background facts: Bangladesh on GS's list of countries allowed to send workers; the August 2024 to March 2025 ban and the conditions on reopening (demand letters certified by the embassy, no placement in the south); BMET clearances by year; the recruitment chain and fees from the ILO study; the official list of fees GS says may be paid; kafala and the suspended 2020 contract.
- Work visa: domestic worker now has three steps (employer's papers in Lebanon, in Bangladesh, work and residence permits), plus complaints, changing employer and being reported for leaving the workplace.
- Without valid papers: the 2024 regularisation programme step by step with fees; leaving with expired papers (Ministry of Labour clearance certificate since 1 November 2024, border settlement, travel permit, the June 2025 waiver).
- Family: the embassy's documents for taking a child born in Lebanon home, and passport and birth certificate fees.
- If a worker dies: the embassy's document list; the Tk 35,000 (every body) and Tk 3 lakh (only with BMET clearance or Board membership) rules; compensation papers.
- Contacts: embassy hours, labour officer email and phone, phones from the 2024 notice, GS 1717 and complaints, Welfare Board call centre.

### Need to know: answered and still open
- Answered and removed: which permits a domestic worker gets and who applies (employer: MoL approval, GS visa, work permit, residence permit); whether Bangladesh restricted sending workers after the 2024 war (yes, 13 August 2024 to 4 March 2025); whether a worker can change employer or leave without the kafil (needs the old sponsor's waiver; leaving with expired papers needs a clearance certificate and fines at the border); what happens to a worker who leaves the house (Leaving the Workplace notice); how a worker becomes irregular and the exit-pass route; where to complain; whether a child born in Lebanon can get a passport from the embassy; who covers what when a worker dies (partly: the Welfare Board's rules); embassy phone and hours.
- Sharpened and still open: 22 questions, listed in questions.md. The main ones: women's share of clearances; whether sending was restricted again in 2026; 2026 costs and wages; passport retention; whether a domestic worker can transfer sponsorship (see conflict below); whether the regularisation programme is still open; the cost of the clearance certificate; who pays the flight for a body; the embassy's street address.

### Resolved conflicts
- **Sponsorship transfer for domestic workers.** GS's "Sponsorship Transfer Applications" page says transfer "is not permitted for domestic workers or for workers who have already been recruited more than twice" [OL0018], but the Ministry of Labour's FAQ describes a domestic worker's transfer by notarised waiver [OL0012], the Housing Bank deposit can be withdrawn on "change of sponsor" [OL0011], GS's own "Leaving the Workplace" page treats a transfer to a new employer as normal [OL0021], and GS's departure-regularisation page says transfers are accepted "regardless of the number of previous waivers" until further notice [OL0019]. Not settled; the GS sentence may be a translation error. The doc describes the transfer procedure and asks the question in a Need to know. OL0018 is logged with status "conflict" and left uncited.
- **Job contract attestation fee.** US$40 in the embassy's 2021 fee chart [OL0094] against US$70 in its January 2024 regularisation notice [OL0049]. The newer figure is used; OL0094 is left uncited.
- **GS regularisation service charge.** The January 2024 notice prints "4900,000 (nine million)" LBP [OL0047]: the figure and the words disagree. GS's own fee page gives LBP 4,900,000 as the urgent paid-service fee per residence permit, which matches the figure, but the notice may mean a different charge. The doc quotes the notice as printed and asks in a Need to know.
- **Regularisation fines are in pre-crisis amounts.** The January 2024 notice gives LBP 400,000 (man) and 300,000 (woman) a year without an akama, while GS's current residence permit fees are LBP 18 to 24 million [OL0046, OL0005]. GS says overstay penalties are charged at the rate in force when each falls due [OL0031]. The doc gives the notice's figures as the notice's and asks whether the programme still runs.
- **Exit-fine waivers.** The Foreign Adviser said in October 2024 that the government was arranging a waiver [XL0022]; no GS notice for Bangladeshis in 2024 was found. GS did let all foreigners with expired papers leave free from 13 June 2025 (L'Orient Today) [OL0081]; the 2025 and 2026 waivers found in searches were for Syrians and Palestinians from Syria only, and are not used.

### Facts logged but not cited
- OL0018 (GS: no transfer for domestic workers): see Resolved conflicts.
- OL0027 (work permit or clearance certificate needed to leave with an expired work residence permit): covered by OL0023 and OL0025.
- OL0028 (departure certificates and re-entry ban): an employer-side procedure; kept for a future section on re-entry.
- OL0029 (Category 3 and 4 residence fees): the domestic-worker fees OL0005 say the same for this doc.
- OL0031 (overstay fees charged at the rate when due): used only in Resolved conflicts.
- OL0094 (2021 contract attestation fee): superseded by OL0049.

### Pages we could not download
- https://www.labor.gov.lb/ (and every live page on it): Cloudflare 403. Should prove the current clearance-certificate fee and the domestic-worker complaint route. Saved from Wayback: FAQ and complaints only. Suggested names: mol-clearance-certificate, mol-domestic-worker-complaint.
- https://mofa.portal.gov.bd/site/page/2914cb0c-50ca-4c0d-be0e-f7bf49438ac9 (Ministry of Foreign Affairs list of missions): connection failed. Should give the embassy's street address and phones. Suggested name: mofa-missions-list.
- https://dailynewnation.com/guidelines-for-irregular-workers-in-lebanon: bot wall (Anubis); saved file holds only the challenge page and is not used. It reportedly quotes an embassy statement that irregular workers must get an exit visa from GS after paying service charges and fines.
- BMET statistics by sex for Lebanon (bmet.gov.bd blocks automated reading; Wayback was offline during the pass). Suggested name: bmet-female-by-country-2024.
- Embassy pages linked from its menu with no working target: "Location Map", "Wing-wise Contact", "Travel Advisories", "Consular Service Hour" (the site links them to not_found).
