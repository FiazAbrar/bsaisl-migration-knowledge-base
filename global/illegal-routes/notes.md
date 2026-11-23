# Illegal routes: research notes

This doc was part of the cross-country doc "Going abroad from Bangladesh" until 23 Nov 2026, when it was split into four global modules (faq, dalal-scams, departure, illegal-routes). Its fact ids keep their original prefixes.

## How the cross-country doc was put together

Research notes behind `doc.md`, one section per part. Each part was researched separately (its own facts and sources), fact-checked by an independent verifier, then merged here; the fact ids keep each part's prefix.

## How the doc was put together

- Four parts, researched in parallel in separate work folders so their facts files never clashed, then merged: facts.csv and sources.csv combined (no id or name clashes); where two parts had saved different captures of the same page under one name, both captures are kept in the text copy so every quote still matches.
- Bangladesh's trafficking law: the Prevention and Suppression of Human Trafficking Act 2012 was repealed by the Prevention and Suppression of Human Trafficking and Migrant Smuggling Act 2026 (Act 55 of 2026). The fact-check rewrote every legal reference from the official text on bdlaws; press summaries had it wrong in places.
- Lower-confidence facts: about 98 quotes were typed from scanned Bangla PDFs (BMET and Ministry charters, the safe migration leaflet, WEWB's annual report) and can't be matched to a text layer; most were first transcribed for the country docs.
- Open conflicts kept as Need to know: the 12 countries in the Ministry's order of 4 November 2026 (press lists differ; no official copy found); BMET's Cambodia and Russia clearance counts; the Gulf medical fee; the migration-cost caps date from 2016 to 2025 and new ones are promised.
- A problem found in another doc: the Saudi Arabia doc cites fact B0132 for "no bank, money transfer or SIM", which its source does not say.

## This part

## What this part covers
Libya-Italy boats; Balkans and Eastern Europe; visit/tourist visas sold as jobs (UAE, Saudi, Oman, Kuwait, Qatar, Malaysia, Maldives); free/azad visas and visa trading; Malaysia via Cambodia-Thailand and the old boat route; scam compounds in Cambodia, Myanmar, Laos; Kyrgyzstan and Central Asia; Russia war recruitment; student visas; forged documents; Bangladesh law; help contacts.

## Sources
- About 260 facts were imported from the country folders (italy, cambodia, kyrgyzstan, malaysia, kuwait, oman, qatar, jordan, maldives, saudi-arabia, united-arab-emirates, singapore) with source files, fetchlog rows and sources.csv rows copied. Each imported fact's note says "from <country> <id>". Statuses were recomputed for this folder (official dated within 12 months = verified, else possibly-outdated; news = unofficial).
- New sources fetched for this part: Al Jazeera, RFE/RL (x2), Fortify Rights (Russia war); Dhaka Tribune (Bosnia; Libya longform; "lose millions"; Myanmar 18; home minister on new law); TBS (Europe surge; Mizdah 2020; CID Libya mafia); TBS Bangla (flawed vetting/warfront); IJ4EU (Romania); Daily Star Bangla (Eastern Europe work permits, 2021); ANN (13 embassies warning; 18 dead Greece via Libya); Prothom Alo English (Al Khums capsize); BSS (ordinance approval; 2026 Act); Daily Observer (2026 Act workshop); Freedom Collaborative (new law replaces 2012 Act); Polish Border Guard (forged visa, 2022); Bangladesh Police CID unit page; Bangladesh Monitor (Biman officer; Bangkok embassy Myawaddy).

## Key findings and conflicts
- The Prevention and Suppression of Human Trafficking Act 2012 has been replaced. Ordinance approved by the Council of Advisers 27 Nov 2025 (BSS); Act adopted 9 April 2026 (UNODC). Names vary across sources: "Prevention and Suppression of Human Trafficking and Migrant Smuggling Act, 2026", "Human Trafficking and Migrant Smuggling Prevention and Suppression Act, 2026", "Prevention and Suppression of Trafficking in Persons and Smuggling of Migrants Act, 2026". The official gazette text was not found on bdlaws; section numbers and exact penalties come from BSS/Observer press summaries of the Home Ministry briefing. A Dec 2025 Chandpur case was still filed under the 2012 Act (I0365 source).
- Russia deaths: police/SRB say 20 of 30 May 2026 recruits dead (17 on day one); Minister told Parliament on 9 July 2026 that 4 had died (earlier count); Fortify Rights counts at least 34 killed of 104 recruited (to Feb 2026). Agencies: three licences cancelled (Kaler Kantho, Jun 2026) vs suspended (Minister, Jul 2026).
- Russia clearances: 7,449 (RFE/RL, 1 Jan 2025-27 Oct 2026) vs 7,752 in "21 months" (bdnews24 via cambodia doc). Different windows.
- 12-country list in the 4 Nov 2026 Ministry letter differs between Prothom Alo, Bangla Tribune and bdnews24 (Cambodia vs Croatia; Kosovo, Bosnia).
- Libya route totals: 92,427 (2009-2024) and 105,719 sea crossings (Dhaka Tribune longform) vs ~110,000 to June 2026 (Frontex via Dhaka Tribune Nov 2026). Used the latter.
- ANN pages (13-embassy warning; 18 dead Greece-via-Libya) show no date in the saved HTML; search snippets suggest April/March 2026. Logged as undated.
- Daily Star Bangla Eastern Europe work-permit piece is from 2021 (cited with year).
- Polish Border Guard PDF text lost Polish diacritics; fact I0316 logged with --no-quote-check and a note.

## Pages we could not download / gaps
- Bangladesh Embassy Tripoli and Moscow contact pages: new mofa.gov.bd portal renders contact pages via JS; Firecrawl returned empty content. Needs a browser.
- IOM Bangladesh contact page returns 404.
- CID THB Unit public phone/email not found on police.portal.gov.bd.
- business-humanrights.org Romania page (403); asianews.it 23 drowned 2025 (403).
- No 2025-26 source found on Bangladeshis on the Belarus-Poland route, or on 2026 street prices for Serbia/Croatia/Romania permits.
- Official text of the 2026 Act (bdlaws) not located.

## Fact-check report

Checked 19 November 2026 against facts.csv quotes and the saved sources. All changes are in doc.md; new facts VI0001-VI0033 are in facts.csv; build.py runs without citation errors.

### Changes

### 1. Maldives had no citation; added I0206

- Before: a Gulf or Maldives street with no permit, a Thai or Malaysian immigration depot, or an airport counter where a fake visa is found and you are sent home [I0021, I0346, I0088, I0311, I0265, I0185, I0148, I0146, I0040]
- After: a Gulf or Maldives street with no permit, a Thai or Malaysian immigration depot, or an airport counter where a fake visa is found and you are sent home [I0021, I0346, I0088, I0311, I0265, I0185, I0206, I0148, I0146, I0040]

### 2. 'almost always' is our own generalisation, unsupported

- Before: The giveaway is almost always the same: a tourist or visit visa instead of a work visa
- After: Common signs: a tourist or visit visa instead of a work visa

### 3. removed own conclusion; explained BMET at first use

- Before: Many victims left with real BMET clearance and a licensed agency, so clearance alone does not make a job real [I0068, I0073].
- After: Many victims left with real emigration clearance from BMET (the Bureau of Manpower, Employment and Training) and still ended up in scam compounds [I0068, I0073].

### 4. source says 'often', not 'most'

- Before: Most of the Italy-bound boats are the last stage of an attempt at legal migration that failed [I0019, I0282].
- After: Taking the boat to Italy is often the last stage of an attempt at legal migration that failed [I0019, I0282].

### 5. replaced press summary with official Act text (ss.15, 16, 54); s.16 is 1-3 years, so 'long' dropped; s.54 is narrower than 'breaking the law'

- Before: selling a fake job, trading visas, forging papers and smuggling people are crimes with long prison terms, and a person trafficked into breaking the law abroad is to be treated as a victim, not an accused [I0197, I0189, I0320, I0324].
- After: selling a fake job, trading visas, forging papers for smuggling and smuggling people are crimes with prison terms, and a trafficking victim cannot be charged for illegal entry or a false travel document that resulted from the trafficking [I0197, I0189, VI0007, VI0006, VI0019].

### 6. Ministry claim uncited (added I0222); CID and IOM explained at first use

- Before: Families can complain to the CID, local police, BMET and the Ministry, and BRAC and IOM help with returns (see Where victims and families get help) [I0361, I0356, I0224, I0027, I0228].
- After: Families can complain to the CID (the police's Criminal Investigation Department), local police, BMET and the Ministry of Expatriates' Welfare, and BRAC and IOM (the International Organization for Migration, the UN migration agency) help with returns (see Where victims and families get help) [I0361, I0356, I0224, I0222, I0027, I0228].

### 7. one case stated as general; source is about two men

- Before: Men unpaid in Dubai have been offered Libya by facilitators there [I0283]. One ring in 2025 promised jobs in Greece for Tk 15 lakh each and flew the men to Libya instead [I0362].
- After: A man left unpaid in Dubai was offered Libya by a facilitator there [I0283]. In 2025 two men promised jobs in Greece for Tk 15 lakh each were flown to Libya instead [I0362].

### 8. ransom amounts dated; Bhairab figure is 'reportedly' in source

- Before: In 2026 families were asked Tk 25 lakh per person, for six men from Manoharganj, Cumilla, and for more than 300 from Bhairab, Kishoreganj [I0021, I0024, I0348].
- After: In July 2026 families of six men from Manoharganj, Cumilla, were asked Tk 25 lakh per person, and in November 2026 the same sum was reportedly being demanded for each of more than 300 men from Bhairab, Kishoreganj [I0021, I0024, I0348].

### 9. clarity: the sums were ransom

- Before: - **Paying does not free you.** In a 2025 case the families paid Tk 21.8 lakh and Tk 16 lakh, and the men were then handed to Libyan police and held 45 days [I0363, I0364].
- After: - **Paying does not free you.** In a 2025 case the families paid Tk 21.8 lakh and Tk 16 lakh in ransom, and the men were then handed to Libyan police and held 45 days [I0363, I0364].

### 10. allegation attributed (source: Libya's GNA)

- Before: - **Death.** In May 2020 a trafficker's family killed 26 Bangladeshis and four Africans in Mizda, Libya [I0332].
- After: - **Death.** In May 2020, according to Libya's then government, a trafficker's family killed 26 Bangladeshis and four Africans in Mizda, Libya [I0332].

### 11. source was logged undated; found dateline 30 March 2026 and departure 21 March from Tobruk (VI0024); minister's claim attributed as allegation as in source

- Before: In 2026 at least 18 Bangladeshis died on a boat from Libya to Greece that carried 38 Bangladeshis among 43 people [I0333, I0334]. The State Minister for Expatriates' Welfare said smugglers abandon
- After: In March 2026 at least 18 Bangladeshis died on a boat that left Tobruk, Libya, for Greece, carrying 38 Bangladeshis among 43 people [I0333, VI0024, I0334]. The State Minister for Expatriates' Welfare alleged that smugglers abandon

### 12. count runs to 3 Nov 2025; 'two of whom' referred to the 4 returned on 31 Oct, not the 120

- Before: Italy returned over 120 Bangladeshis in 2025, two of whom had arrived from Libya without a visa a month before [I0035, I0066].
- After: Italy returned over 120 Bangladeshis in 2025 up to early November, including four on 31 October, two of whom had arrived from Libya without a visa a month before [I0035, I0066].

### 13. cited official Act text (ss.2(20), 4, 14-15) instead of press summary

- Before: - **Bangladesh:** organising this journey is migrant smuggling, and holding people for ransom is trafficking, under the 2026 Act (see The law in Bangladesh) [I0331, I0321].
- After: - **Bangladesh:** under the 2026 Act, organising this journey is migrant smuggling, holding people for ransom is a form of exploitation under the trafficking offence, and the Act also covers offences committed abroad against Bangladeshis (see The law in Bangladesh) [VI0006, VI0003, VI0020].

### 14. conversion cited the USD rate (I0067); EUR rate now logged (VI0031, Tk 139.61)

- Before: fined EUR 5,000 to 10,000 (about Tk 6.98 to 13.96 lakh) [I0049, I0067]
- After: fined EUR 5,000 to 10,000 (about Tk 6.98 to 13.96 lakh) [I0049, VI0031]

### 15. unconvicted person: stated as accused

- Before: which led the CID to arrest the man who ran the ransom calls (see Where victims and families get help) [I0365, I0356].
- After: which led the CID to arrest a man accused of coordinating the ransom demands (see Where victims and families get help) [I0365, I0356].

### 16. source logged undated; dateline 9 April 2026 found (VI0025)

- Before: Thirteen Western embassies, including Italy, Hungary and Germany, have jointly warned Bangladeshis
- After: In April 2026 thirteen countries' missions, including Italy, Hungary and Germany, jointly warned Bangladeshis

### 17. date support

- Before: none of them works with any agent [I0309, I0310].
- After: none of them works with any agent [I0309, VI0025, I0310].

### 18. EUR conversion needs EUR rate (11,000 x 139.61 = Tk 15.36 lakh)

- Before: A Romanian job sold for EUR 11,000 (about Tk 15.4 lakh) turned out to be undeclared building work, 12 hours a day, 7 days a week [I0043, I0044, I0067].
- After: A Romanian job sold for EUR 11,000 (about Tk 15.4 lakh) turned out to be undeclared building work, 12 hours a day, 7 days a week [I0043, I0044, VI0031].

### 19. source context: Decreto Flussi

- Before: Thousands of Bangladeshis have paid up to EUR 20,000 for Italian work permits that never came [I0300].
- After: Thousands of Bangladeshis have paid up to EUR 20,000 for Italian work permits under Italy's quota scheme (Decreto Flussi) that never came [I0300].

### 20. wage claim is what workers told rights groups; attributed

- Before: rights groups reported possible trafficking [I0295]. Many had borrowed up to USD 10,000, had passports taken on arrival, were paid below
- After: rights groups reported possible trafficking [I0295]. Many had borrowed up to USD 10,000 and had passports taken on arrival; workers said they were paid below

### 21. Russia is not on bdnews24's list; added Daily Star's fourth version (VI0026) and stated only what all lists share

- Before: - **Bangladesh:** on 4 November 2026 the Ministry of Expatriates' Welfare told BMET to give no clearance without its permission for 12 countries, including Serbia, Moldova, Belarus and Russia [I0114]. Published lists of the 12 differ, some naming Croatia, Kosovo and Bosnia [I0115, I0116].
- After: - **Bangladesh:** on 4 November 2026 the Ministry of Expatriates' Welfare told BMET to give no emigration clearance for 12 countries without the Ministry's recruitment permission or approval [I0114]. Every published list names Serbia, Moldova, Belarus, Japan, Iraq, Laos, Vietnam, Ukraine and Libya; most also name Russia and Cambodia; the rest differ between reports (Congo, Kosovo, Croatia or Bosnia) [I0114, I0115, I0116, VI0026].

### 22. 'usually' unsupported; Saudi case is reported as allegations (2024)

- Before: The person is usually told he has a work visa: to Saudi Arabia, a three-month tourist visa sold with a promised 15-month iqama (residence permit); to Cambodia,
- After: Brokers tell people they have a work visa: to Saudi Arabia, allegedly, a three-month tourist visa sold with a promised 15-month iqama (residence permit); to Cambodia,

### 23. 'main' supported only for Libya

- Before: Dubai remains the main transit to Libya, Kyrgyzstan and Russia [I0290, I0120, I0269].
- After: Dubai is the usual transit point to Libya and has also been used for Kyrgyzstan and Russia [I0290, I0120, I0269].

### 24. source: anonymous official, 'sometimes'

- Before: Traffickers also use Umrah (pilgrimage) visas to get people out before sending them elsewhere [I0355].
- After: An immigration official said traffickers sometimes use a valid visa for one country, such as a tourist or Umrah (pilgrimage) visa, before sending people elsewhere [I0355].

### 25. acronym

- Before: Only some visit visas can be converted, for KD 150 [I0166].
- After: Only some visit visas can be converted, for KD 150 (Kuwaiti dinars) [I0166].

### 26. unconvicted person: allegation stated as accusation; Sepang: employers misused passes

- Before: - **Malaysia:** in October 2026 the CID arrested a Paltan travel agency owner who took two people to Malaysia on visit visas promising work permits, held them and demanded Tk 5 lakh from their families [I0153]. In September 2026 Malaysian immigration detained 147 Bangladeshis on Sepang building sites where social visit passes were misused [I0159].
- After: - **Malaysia:** in October 2026 the CID arrested a Paltan travel agency owner accused of taking two people to Malaysia on visit visas with a promise of work permits, holding them and demanding Tk 5 lakh from their families [I0153]. In September 2026 Malaysian immigration detained 147 Bangladeshis on Sepang building sites where employers had misused social visit passes [I0159].

### 27. allegation dated

- Before: - **Airport collusion:** brokers allegedly pay airport staff Tk 30,000 to 50,000 per passenger, called a "body contract", to pass immigration with incomplete papers [I0354].
- After: - **Airport collusion:** allegations reported in November 2026 say brokers pay some airport staff Tk 30,000 to 50,000 per passenger, called a "body contract", to pass immigration with incomplete papers [I0354].

### 28. I0194 (no conversion) and I0247 (prohibited immigrants) don't say working is illegal; UAE/Saudi/Oman uncited; 'see the path above' is not an allowed link

- Before: - **Destinations:** working on a visit visa is illegal in every Gulf country covered, in Malaysia and in the Maldives (see the path above) [I0165, I0194, I0247, I0207].
- After: - **Destinations:** Kuwait bars every visit visa holder from working, and in the Maldives trying to work on a tourist visa can mean jail and a fine (see The path, country by country) [I0165, I0207].

### 29. advice of our own with no source (I0219 is only the call centre)

- Before: Before travelling, check the visa type with the destination's own visa portal or the Bangladesh embassy; after it goes wrong, call the Probash-Bondhu call centre (see Where victims and families get help) [I0219].
- After: The Probash-Bondhu call centre answers workers and families 24 hours (see Where victims and families get help) [I0219].

### 30. source says 'recruiting agencies', not 'licensed'; ring quote is in I0162

- Before: Of those who knowingly bought one, 54% went through illegal broker networks, 31% through distant relatives and 7% through licensed agencies [I0182]. In Kuwait an organised ring sells visas for lakhs of taka under the "free visa" name [I0161].
- After: Of those who knowingly bought one, 54% went through illegal broker networks, 31% through distant relatives, 8% through family and 7% directly through recruiting agencies [I0182]. In Kuwait an organised ring sells visas for lakhs of taka under the "free visa" name [I0161, I0162].

### 31. source is Qatar, 'sometimes'

- Before: Sponsors demand regular payments to keep sponsoring [I0186].
- After: In Qatar, sponsors sometimes demand regular payments to keep sponsoring [I0186].

### 32. two sources merged into a claim neither makes

- Before: - **Absconding cases:** sponsors file false "absconding" (runaway) reports to free up quotas for resale, which makes the worker illegal [I0163, I0171].
- After: - **Absconding cases:** brokers in Kuwait file false "absconding" (runaway) reports to free up visa quotas for resale, and some sponsors in Oman report free-visa workers as absconding so they are not punished if the worker is caught elsewhere [I0163, I0171].

### 33. Qatar-only sources stated as general

- Before: - **No rights:** a free-visa worker has no legal help if unpaid [I0178]. Free-visa workers hunt for illegal day labour and many face harassment, arrest or deportation [I0185].
- After: - **No rights:** in Qatar a free-visa worker has no legal help if unpaid [I0178]. Free-visa workers there hunt for illegal day labour and many face harassment, arrest or deportation [I0185].

### 34. fine is a maximum

- Before: - **Qatar:** visa trading, and working on a free visa, carry up to 3 years in prison and a QR 50,000 fine [I0176, I0178].
- After: - **Qatar:** visa trading, and working on a free visa, carry up to 3 years in prison and a fine of up to QR 50,000 (Qatari riyals) [I0176, I0178].

### 35. I0224 is the complaint route, not visa checking; I0191 (BMET leaflet) supports checking

- Before: Before paying, ask BMET whether a visa is real; after it goes wrong, complain about the broker under the 2013 Act (see Where victims and families get help) [I0224, I0196].
- After: BMET asks anyone handed such a visa to have it and the other papers checked at BMET in Dhaka or the District Employment and Manpower Office; after it goes wrong, anyone cheated can complain to the government under the 2013 Act (see Where victims and families get help) [I0191, I0196].

### 36. 'fill the gap' is our conclusion; figures are 'believed'/'estimated'; gang name derives from a person's name, dropped

- Before: Smuggling rings fill the gap: one Bangladeshi ring, the "Karim Gang", charged up to RM15,000 (Malaysian ringgit) per person and made about RM3.2 million in 2026 [I0144].
- After: A Bangladeshi smuggling ring broken up in Malaysia in July 2026 is believed to have charged up to RM15,000 (Malaysian ringgit) per person and made about RM3.2 million since January 2026 [I0144].

### 37. no source gives Tk 4.8 lakh for Cambodia; cited sources give 5.3, 5.5, 5.6 and 6 lakh

- Before: for about Tk 4.8 to 5.5 lakh [I0073, I0076, I0090, I0069].
- After: for about Tk 5.3 to 6 lakh [I0073, I0076, VI0028, VI0029].

### 38. the study's 66% via middlemen contradicted 'through licensed agencies'

- Before: Many go through licensed agencies with BMET clearance: a BRAC study found 66% were recruited through middlemen and 98% never got the promised job [I0068, I0081].
- After: Many went with BMET clearance [I0068, I0073]. A BRAC study found 66% of cyber-scam victims were recruited through middlemen and 98% never got the promised job [I0081].

### 39. I0087 (The Star) says 583 'by June' including 109; TBS says 583 in June plus 109 on 1 July; Myawaddy figure dated

- Before: - **Returns:** 583 Bangladeshis came home from Cambodia in June 2026, 109 of them rescued from compounds; 221 returned in four days that month [I0087, I0075]. About 50 rescued from Myawaddy, Myanmar, have been repatriated through the Embassy in Bangkok [I0342].
- After: - **Returns:** 583 trafficking victims came home from Cambodia in June 2026, including 221 in four days, and another 109 on 1 July [VI0027, I0075]. By April 2026 about 50 people rescued from Myawaddy, Myanmar, had been repatriated through the Embassy in Bangkok [I0342, VI0030].

### 40. undated window

- Before: - **Laos:** 7,532 Bangladeshis went to Laos in 21 months [I0079].
- After: - **Laos:** 7,532 Bangladeshis went to Laos in the 21 months before October 2026 [I0079].

### 41. official text (s.2(20)); 'victims, not offenders' goes beyond s.54, which covers only entry, stay and travel documents

- Before: - **Bangladesh:** the 2026 Act treats forced criminality in scam compounds as trafficking, so those held there are victims, not offenders [I0329].
- After: - **Bangladesh:** the 2026 Act counts forcing a person into crimes such as online scamming as exploitation under the trafficking offence [VI0003, I0329].

### 42. Bangla Tribune's list omits Cambodia

- Before: Cambodia is one of the 12 countries needing Ministry approval (see The Balkans and Eastern Europe) [I0114].
- After: Most published lists of the 12 countries needing Ministry approval since 4 November 2026 include Cambodia (see The Balkans and Eastern Europe) [I0114, I0116, VI0026].

### 43. no source says Saudi Arabia; I0132 does not mention routing

- Before: 1. **Dhaka to Dubai, then Moscow** [I0269]. Some groups were routed through Saudi Arabia and the UAE [I0132].
- After: 1. **Dhaka to Dubai, then Moscow**, or through other third countries [I0269, I0268].

### 44. death counts dated and attributed; '20 of the 30' not in source (20 Bangladeshis confirmed dead); earlier official count added

- Before: - **Death:** of 30 men who landed in Moscow on 7 May 2026, 17 were killed on their first day of deployment after minimal training, and 20 were confirmed dead [I0265, I0273]. Police said the Bangladeshis were used as bait to locate enemy positions [I0266]. Fortify Rights and Truth Hounds, two rights groups, documented at least 104 Bangladeshis recruited and at least 34 killed [I0275].
- After: - **Death:** 30 men flew out on 7 May 2026 [I0273]. In October 2026 the commander of the police's Special Response Battalion said 17 who arrived that May were killed on their first day of deployment after minimal training, 20 Bangladeshis were confirmed dead, and they had been used as bait to locate enemy positions [I0265, I0266]. On 9 July 2026 the Minister had told Parliament that four of the 30 had died [I0314]. A joint investigation by Fortify Rights and Truth Hounds, two rights groups, counted at least 104 Bangladeshis recruited and at least 34 killed [I0275].

### 45. allegation against agencies dated and attributed; bdnews24's list omits Russia

- Before: - **Bangladesh:** the government cancelled the licences of three agencies and forfeited their deposits over the 30 men, and police arrested two men accused of the trafficking in October 2026 [I0158, I0263]. The Expatriates' Welfare Minister told Parliament on 9 July 2026 that three agencies' licences had been suspended [I0314]. Russia is one of the 12 countries needing Ministry approval before clearance [I0114].
- After: - **Bangladesh:** in June 2026 the government cancelled the licences of three agencies accused of sending the 30 men, and forfeited their deposits [I0158]; on 9 July 2026 the Expatriates' Welfare Minister told Parliament the three licences had been suspended [I0314]. In October 2026 police arrested two men accused of the trafficking [I0263]. Most published lists of the 12 countries needing Ministry approval since 4 November 2026 include Russia [I0114, I0115, VI0026].

### 46. dated

- Before: - **Fake visas:** two men agreed Tk 30 lakh each for Italy, paid Tk 20 lakh up front, and were given fake Schengen visas [I0359, I0038].
- After: - **Fake visas:** in May 2026 two men agreed Tk 30 lakh each for Italy, paid Tk 20 lakh up front, and were given fake Schengen visas [I0359, I0038].

### 47. allegation attributed and dated

- Before: A ring sent another woman to Italy on a woman's visa; CID seized 56 passports and 153 seals [I0042].
- After: In July 2026 the CID arrested members of a ring accused of sending a woman to Italy on another woman's visa, and seized 56 passports and 153 seals [I0042].

### 48. unconvicted: stated as accusation, dated

- Before: A Biman ground officer who helped them board was arrested [I0039].
- After: In June 2026 a Biman ground officer was arrested, accused of helping them board [I0039].

### 49. I0253 is a 2019 rule, not a report of cases

- Before: applicants caught with fake papers have been banned and reported to the police [I0252, I0253].
- After: the visa centre's rules say applicants caught with fake papers are banned from applying and reported to the police [I0252, I0253].

### 50. replaced press summary with official text (ss.16, 54)

- Before: - **Bangladesh:** passport or visa forgery for smuggling is a serious offence under the 2026 Act [I0320]. A person trafficked into carrying a forged passport is not to be treated as accused [I0324].
- After: - **Bangladesh:** making, obtaining, supplying or holding a document to help migrant smuggling carries 1 to 3 years' rigorous imprisonment and a fine of at least Tk 50,000 under the 2026 Act [VI0007]. A trafficking victim cannot be charged for getting or holding a false travel document as a direct result of the trafficking [VI0019].

### 51. section rested on BSS/Observer press summaries; rewritten from the official text on bdlaws (Act No. 55 of 2026). Corrections: '3 to 7 years for fake online job ads or fraud in the name of migration' is officially s.20, advertising for migrant smuggling; victim protection (s.54) is limited to illegal entry/stay and false travel documents; added minimum penalties, s.27, s.28 complaint route, s.4 extraterritorial reach; UNODC 9 April date kept as 'April 2026' since bdlaws dates the Act 10 April

- Before: The Prevention and Suppression of Human Trafficking and Migrant Smuggling Act, 2026, adopted on 9 April 2026, replaced the Prevention and Suppression of Human Trafficking Act 2012 [I0105, I0375]. It was first approved as an ordinance by the interim government's Council of Advisers on 27 November 2025 [I0326]. For the first time it separates trafficking and smuggling as two crimes [I0331].

- **Who is covered:** trafficking, migrant smuggling, online fraud, scamming and ransom collection [I0317, I0321].
- **Penalties:** life imprisonment or death remain the maximum for trafficking [I0318]. Fake online job ads or fraud in the name of migration carry 3 to 7 years [I0322].
- **Powers:** courts can freeze bank accounts, seize property, restrict foreign travel and try the accused in their absence [I0319, I0327].
- **Victims:** a victim made to carry a forged passport or enter a country illegally is not to be treated as accused [I0324]. Threatening a victim or witness carries 3 to 7 years, and pressuring a victim to settle 2 to 5 years [I0323].
- **Courts:** Human Trafficking Tribunals can try related assault, drug or sexual-violence charges in the same case [I0325]. Justice and Care, an NGO, was supporting about 400 cases in 18 tribunals [I0330].
- After: The Human Trafficking and Migrant Smuggling Prevention and Suppression Act, 2026 (Act No. 55 of 2026), passed in April 2026, repealed the Prevention and Suppression of Human Trafficking Act 2012 and took effect at once [I0105, VI0001, VI0002, VI0032]. It replaced an ordinance of the same name, first approved by the interim government's Council of Advisers on 27 November 2025 [I0326, VI0022]. For the first time it separates trafficking and smuggling as two crimes [I0331]. It applies to anyone who commits one of its offences against a Bangladeshi abroad [VI0020].

- **Trafficking:** at least 5 years' rigorous imprisonment, up to life, and a fine of at least Tk 50,000; by an organised gang, death or life imprisonment, or at least 7 years, and a fine of at least Tk 5 lakh [VI0004, VI0005].
- **What counts as exploitation:** among other things, forced labour, debt bondage, forcing someone into crimes such as online scamming, and holding someone to demand ransom [VI0033, VI0003].
- **Migrant smuggling** (getting someone into another country illegally for gain): 3 to 10 years' rigorous imprisonment and a fine of at least Tk 1 lakh; if the migrant is gravely hurt, dies, is put in danger or treated cruelly, 5 years to life [VI0006, VI0008].
- **Documents and ads:** making, obtaining, supplying or holding a document to help smuggling, 1 to 3 years; advertising for smuggling online, on social media or in print, 3 to 7 years and a fine of at least Tk 1 lakh [VI0007, VI0009, VI0010].
- **Victims:** a trafficking victim cannot be charged for illegal entry or stay abroad, or for getting or holding a false travel or identity document, if it was a direct result of the trafficking [VI0019]. Threatening a victim, the family or a witness carries 3 to 7 years, and pressuring a victim or family to settle 2 to 5 years [VI0011, VI0012].
- **Filing a case:** anyone can complain at a police station or to the tribunal; the police must protect the complainant and keep their identity confidential [VI0014]. All offences are cognisable, non-bailable and can't be settled privately [VI0013].
- **Powers:** on the investigator's application the tribunal can freeze bank accounts, block the sale of property, and bar an accused from leaving the country for up to 60 days; an accused who absconds can be tried in absence [VI0015, VI0023, VI0016, VI0017].
- **Courts:** the government can set up a Human Trafficking and Migrant Smuggling Suppression Tribunal in each district, and it can try a connected offence in the same case [VI0021, VI0018]. In 2026 Justice and Care, an NGO, was supporting about 400 cases in 18 tribunals [I0330].

### 52. added the official filing route and protection from the Act (s.28)

- Before: 2. **File a criminal case with the local police.** CID asks returnees to file cases with their local police so the brokers and agencies can be prosecuted [I0356].
- After: 2. **File a criminal case with the local police.** CID asks returnees to file cases with their local police so the brokers and agencies can be prosecuted [I0356]. Under the 2026 Act a case can be filed at a police station or directly with the tribunal, and the police must protect the complainant and keep their identity confidential [VI0014].

### 53. acronym

- Before: OEP hotline: 09614445271 [I0225].
- After: Hotline of OEP (the Overseas Employment Platform, BMET's online system): 09614445271 [I0225].

### 54. acronym

- Before: apply to the Welfare Board directly or through the DC office's expatriate welfare branch or the DEMO (District Employment and Manpower Office)
- After: apply to the Welfare Board directly or through the expatriate welfare branch of the Deputy Commissioner's (district administration) office or the DEMO (District Employment and Manpower Office)

### 55. law says 'breaking the purpose of entry'; currency explained

- Before: - **Fines and deportation:** working on a tourist visa is fined 10,000 som in Kyrgyzstan, and in September 2025, 180 Bangladeshis were sent back [I0138, I0137].
- After: - **Fines and deportation:** breaking the purpose of entry, such as working on a tourist visa, is fined 10,000 som (Kyrgyz currency) in Kyrgyzstan, and in September 2025, 180 Bangladeshis were sent back [I0138, I0137].

### 56. acronym; fine is per student

- Before: the employer is fined at least JD 800 [I0257, I0258].
- After: the employer is fined at least JD 800 (Jordanian dinars) per student [I0257, I0258].

### New sources and facts

- **bdlaws-trafficking-smuggling-act-2026-full** (official, Legislative and Parliamentary Affairs Division, http://bdlaws.minlaw.gov.bd/act-details-1684.html): full official text of the Human Trafficking and Migrant Smuggling Prevention and Suppression Act, 2026, Act No. 55 of 2026, dated 10 April 2026. Facts VI0001-VI0023, VI0032, VI0033. (A table-of-contents copy, bdlaws-trafficking-smuggling-act-2026, was also fetched but is not registered or cited.)
- VI0024 (ANN/Daily Star 18 dead, dated 30 March 2026), VI0025 (13-country warning, dated 9 April 2026), VI0026 (Daily Star's 12-country list with Kosovo), VI0027 (TBS: 583 in June plus 109 on 1 July), VI0028-VI0029 (Cambodia prices Tk 5.6 and 6 lakh), VI0030 (Myawaddy report dated 28 April 2026), VI0031 (Bangladesh Bank EUR rate Tk 139.61, 10 Nov 2026).

### Issues not fixed

- **12-country list (4 Nov 2026):** no official copy found on probashi.gov.bd or bmet.gov.bd (searched; BAIRA reportedly circulated the letter). Four press versions: Prothom Alo (Congo, Russia, Cambodia), Bangla Tribune (Croatia instead of Cambodia), bdnews24 (Kosovo and Bosnia instead of Congo and Russia), Daily Star (Kosovo instead of Congo). Need to know line kept.
- **Cambodia clearance counts conflict:** 15,921 in 18 months (TBS, Jul 2026), 15,963 in 21 months (bdnews24, Oct 2026), 15,235 Jan 2025-30 Oct 2026 (Daily Star, Nov 2026). Doc keeps the TBS figure; not resolvable without BMET data. Russia: 7,449 (RFE/RL) vs 7,752 (bdnews24) vs 5,776 (Daily Star).
- **Act date:** UNODC says adopted 9 April 2026; bdlaws dates Act No. 55 to 10 April 2026. Doc now says 'April 2026'. The Act is in Bangla only; s.66 says an English translation will be published. English title is our translation.
- **I0087 vs VI0027:** The Star says 583 by June including 109 rescued; TBS says 583 in June plus 109 on 1 July. Doc follows TBS. I0087 now uncited.
- Facts I0320, I0322, I0323, I0324, I0317, I0318, I0319, I0321, I0325, I0327, I0375, I0067 (for EUR), I0090, I0069, I0132 (routing) are no longer cited where they were; the press summary I0322 ('fake online job ads or fraud in the name of migration, 3-7 years') does not match the official text (s.20 is advertising for migrant smuggling).
- I0333-I0335, I0309-I0310 and I0342 rows still show page_date 'undated'; dates are now carried by VI0024, VI0025 and VI0030.
- Fortify Rights/Truth Hounds figures (104 recruited, 34 killed) come from RFE/RL (Nov 2026); the saved Fortify Rights March 2026 page doesn't contain them.
- Embassy contacts for Tripoli and Moscow and the CID THB Unit's public number remain Need to know items (not re-searched).
- Not every source behind every sentence was opened in full; numbers and allegations were all checked against saved text, other sentences against the quotes.

## Prothom Alo chunk illegal-routes-1 (prefix GI, Nov 2026)

29 articles read; 16 used (facts GI0001 to GI0056). The March 2026 Middle East war articles (flights cancelled, ministry hotline and control room, remittances) and a column on bodies sent home were held for the departure, services, money and FAQ docs (see the ledger gledger-illegal-routes-1.json).

### Resolved conflicts

- **Bangladeshis crossing the Mediterranean since 2009.** Three figures: 84,000 for 2009 to 2024 (Prothom Alo editorial, 6 Feb 2025) [LB0139], 106,598 for 2009 to May 2024 (Prothom Alo editorial, 31 Aug 2024) [GI0023], and about 110,000 for 2009 to June 2026 (Frontex) [I0351]. Settled for Frontex: it is the EU border agency that counts the crossings, while both editorials name no source and disagree with each other by over 20,000 for almost the same period. The doc keeps Frontex's figure and the yearly arrival counts; the two editorial totals are no longer cited (the 6 Feb 2025 editorial is still cited, attributed, for its deaths-per-year statement). No Need to know.
- **Trafficking cases in 2023.** BNWLA's Safayet Bin Kamal said 137 trafficking cases were recorded nationwide in 2023 [GI0038]; the Home Ministry counted 683 new cases in January to September 2023 alone [AA0005]. These are probably different counts (BNWLA's own record versus police cases), and the Home Ministry figure is the primary one, so it stays the national figure under "What happens to trafficking cases"; the BNWLA figure is kept only in the Malaysia numbers, attributed, for its 44% Cox's Bazar share. No "Need to know": it changes nothing a migrant would do.

## Prothom Alo chunk illegal-routes-3 (prefix GI, Nov 2026)

5 articles read; 4 used (facts GI0096 to GI0117), plus one Prothom Alo article already saved in the Malaysia doc (16 July 2026, UNHCR/IOM joint statement, jz7zam0xfl) saved here to settle the Andaman question. The parliamentary committee article of 8 October 2026 (airport harassment, workers sent 18 Feb to 30 Sep 2026, 186 brought back from Iran) was held for the departure, FAQ and services docs (see gledger-illegal-routes-3.json). The 2008 essay on slavery is used only for its unsourced India and Pakistan figures, dated to its first publication (4 January 2008); its history of slavery is not relevant.

### Resolved conflicts

- **Andaman Sea trawler "with more than 280 people from the Teknaf coast" (GI0075) vs the April 2026 sinking with about 250 missing (CQ0159).** Not the same boat. The April sinking was reported by Prothom Alo itself from Teknaf on 17 and 19 April (UNHCR: about 250 missing; Prothom Alo: at least 250 aboard; nine survivors handed to Teknaf police), so Teknaf journalists did know of it. The staff reporter's remark on 26 July 2026 (more than 280 aboard, foreign agencies reported it first) matches the UNHCR/IOM joint statement of 16 July 2026, ten days earlier: a boat carrying about 280 people believed sunk near Myanmar's Irrawaddy coast on 8 July 2026 (GI0113). The figure, the timing and "foreign agencies first" all fit; the only mismatch is the departure point (UNHCR/IOM say the two late-June boats left Rakhine State; the reporter says the Teknaf coast). The UN statement is the primary account; the reporter's remark is a later, unsourced aside. GI0075 now sits, attributed, under the new July 2026 case; the Need to know bullet is removed. Not raised as a new Need to know: where the boat left from changes nothing a migrant would do.
- The UNHCR/IOM statement also mentions a second late-June boat of about 250 with which contact was lost. This is a different event from the April boat of about 250 (different months and departure points); both are kept as separate cases.

- **2008 essay on trafficking to India and Pakistan (GI0111, GI0112):** logged but not cited. The figures are from January 2008 and give no source; newer, sourced numbers are in the doc, and these change nothing a reader would do.

## Prothom Alo chunk illegal-routes-x (prefix GI, Nov 2026)

64 articles read (mostly Libya ransom cases and returns, Russia's war recruitment, the 2025 and 2026 Iran evacuations); facts GI0118 to GI0309. New: "Kidnapped after years of work", "Where the ransom is paid" and "The kidnappers speak Bangla" under Ransom and resale; December 2024 Zawiya sinking; charter returns 2024 to 2026; ten more broker cases; Kalkini and Narail rings; new sections Waiting in Iran, Through West Africa and the Sahara to Morocco (a 2005 case) and Legal jobs in Russia; Russia additions (brokers inside Russia, the April 2025 first-hand account, Suruj Kazi, the Jamalpur two, Sagar, Ali Hasan Sohel, captured men). Iran war evacuation logistics and hotlines, the Turkey BOESL notice and the Albania offer were held (see gledger-illegal-routes-x.json).

### Resolved conflicts

- **March 2026 Libya to Greece boat: how many Bangladeshis died.** The State Minister confirmed at least 18 [I0333]; Prothom Alo's local report of 5 April 2026 gives 22 dead, 18 of them Bangladeshi, 13 from Sunamganj with an upazila breakdown [GI0251, GI0252]; Md Touhid Hossain's column of 27 April 2026 relays "20 of the 22 dead or missing reported Bangladeshi" [LB0207]. The official figure and the specific local count agree on 18; the column is a later secondhand restatement. The doc now states 22 dead, 18 Bangladeshi, and no longer cites the column for the 20; the "Need to know" bullet is removed. The passenger count (43 per a survivor, 48 per the column) is left as reported; it changes nothing a reader would do.
- **Sunamganj dead: 12 or 13.** 12 was the early count (Prothom Alo 29 to 31 March, the 1 April editorial, the Dirai case filed over 12 deaths); 13 is the 5 April count with each upazila named. The specific, later count wins; RU0055 (12) is no longer cited, and the editorial is cited without its number. The Dirai case is still described as filed over 12 deaths, as reported.
- **Training for the group of 30: 21 days or 5.** Prothom Alo and the SRB report 21 days for the group [RU0084]; Ali Hasan Sohel says his group of 16 was sent after five days [GI0297]. Both are attributed in the doc; not raised as a Need to know because it changes nothing a reader would do.
- **Two flights of 174 from Libya** (1 September and 27 October 2026) are separate flights with separate details (Tajoura detention centre; 36 from Tajoura, 41 ill), not a duplicate.
- **Bosnia, September 2026:** 36 Bangladeshis of 96 [I0280] and 23 in the first group of 63 [GI0280] are consistent (the second group of 33 also held Bangladeshis); both kept.
- **Old statistics:** the 2005 Western Sahara case is cited, dated, because it documents a route and its outcome; no figures from it are used as current numbers.

## Held items from other ledgers (prefix GI, 23 Nov 2026)

53 held items from other docs' Prothom Alo ledgers placed (facts GI0310 to GI0389, 24 articles saved). New: "From eastern Libya to Greece" (price, split payments, broker network, pointer to the Greece doc's "Irregular entry: Libya to Crete by boat"), "Tajoura detention centre", BRAC's February 2024 study of 557 Libya returnees, the PBI court route that brought a hostage home, the September 2026 Gavdos sinking, Rohingya on Bangladeshi passports, two India cases, Abdur Rahim's death in Russia.

### Resolved conflicts

- **March 2026 Libya to Greece boat: how many rescued.** Prothom Alo of 31 March 2026 (pa-2026-03-31-iky2lx7qxw) says the Greek coast guard rescued 22 alive; Md Touhid Hossain (LB0207) and the Greece doc (Frontex ship, 26 rescued: 21 Bangladeshis, 4 South Sudanese, 1 Chadian) give 26. Kept 26: two independent accounts agree and the Greece doc's figure is the more specific; the 22 is most likely the death toll repeated. The doc's figures (at least 22 dead, 18 Bangladeshi, 13 from Sunamganj) match the Greece doc.
- **Russia: who the ten families applied to.** A Prothom Alo column of 29 November 2025 (GI0346) says at least 10 families applied to the Bangladesh government; the column cites BRAC's report, and BRAC's own statement (RU0018) says the 10 families asked BRAC. Kept RU0018; GI0346 logged, not cited.
- **Sunamganj cases: one case against four, or two against nine.** The video headline (GI0249) names the Dirai case against four; the 31 March report (GI0320) gives two cases, five accused at Jagannathpur and four at Dirai, matching the Greece doc (XG0064). The doc now gives the two cases.
- **Libya returns: 4,200.** The ambassador's "4,200 sent home last year" (GI0339, February 2025) and LB0138's "4,200 freed in the previous year and a half" are the same count; LB0138 kept for the number.

## Prothom Alo chunk lchunk-illegal-routes (prefix GI, 23 Nov 2026)

12 articles read (missed by an earlier filter); 6 used (facts GI0390 to GI0432). New: the Russia-Belarus-Poland route (Liton Chowdhury, 2024) under The Balkans and Eastern Europe; IOM's January 2026 Mediterranean sinkings; Russia additions (Akram Hossain of Ashuganj recruited inside Russia and killed April 2025; Arman Ali's June 2026 video from the group of 30; Rimel Mia captured by Ukraine; Al Mamun of Nandail). Six video teasers were duplicates of facts already in the doc (see lledger-illegal-routes.json).

### Resolved conflicts

- **Training for the group of 30: 21 days, 5 days or 3 to 4 days.** Prothom Alo and the SRB report 21 days [RU0084]; Ali Hasan Sohel says five days [GI0297]; Arman Ali, in a video reported on 21 June 2026, says three to four days [GI0419]. All three are first-hand or attributed and may describe different sub-groups; all are kept, attributed. Changes nothing a reader would do, so no Need to know.
- **Arman Ali alive in June, listed dead in October.** Arman said on 21 June 2026 that he was wounded and alive [GI0421]; the families' October 2026 list of the dead includes a Md Arman Ali [RU0197]. Not a conflict: the dates differ. The doc states both, dated, without asserting they are the same man.

## Held items, round 2 (prefix GI, 23 Nov 2026)

8 items (heldout2-illegal-routes.json): 7 added (GI0433 to GI0450), 1 duplicate (Shayek Ahmad's route via Saudi Arabia and Kuwait, already GI0364). The UNHCR worldwide asylum figure for 2023 (75,867) and Reuters' Europe-only figure (40,332) cover different areas, so both stand.

## Held items, round 4 (prefix GI, 23 Nov 2026)

Five held items (held4-illegal-routes.json). Added: foreign scam-centre rings raided in Chattogram and Cox's Bazar (GI0451 to GI0454, "Cambodia, Myanmar and Laos: scam compounds", What happens); Bangladesh embassy and Tunisian navy details for the February 2024 boat fire (GI0455 to GI0457); the embassy's survivor account of the August 2026 Tobruk boat (GI0458 to GI0462), which replaces the editorial's secondhand summary GI0349 (no longer cited).

### Resolved conflicts

- Shahriar Ahmed Emon (Cyprus): this doc said he left for the job and disappeared on 12 June 2026 (OB0001 to OB0003, Prothom Alo 22 June, a report built on Cyprus police and CID statements); the Other destinations doc says 11 June (Prothom Alo 23 June, the family's account). Settled on 11 June. The family account is first-hand and internally consistent: he spoke to his mother on the afternoon of 11 June, sent his roommate his location at 9 pm local time, a ransom message came from his WhatsApp at about 10 pm, and the roommate reported him missing to police the next morning, 12 June (GI0463 to GI0465). The body was found on Sunday 21 June, which the 23 June report calls ten days after he left (11 June); the 22 June report's "nine days" of search fits a police case opened on 12 June, which is the likely origin of its date. OB0001 is now cited only for his enrolment; OB0002 and OB0003 are no longer cited. Both docs now say 11 June.

- **March 2026 Tobruk boat, how many aboard (resolved 23 Nov 2026):** a survivor's early count (43 aboard, 38 Bangladeshi; I0334) is lower than the later totals: 22 dead (Prothom Alo, 5 April; Greek coast guard via the Greece doc) and 26 rescued by Frontex, 21 of them Bangladeshi (Greece doc, XG facts), which make at least 48 aboard and at least 39 Bangladeshi. The doc keeps the survivor's count only as attributed and early, and points to the Greece doc for the later figures.
