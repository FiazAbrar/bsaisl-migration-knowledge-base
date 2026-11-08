# UAE doc: round-1 coverage and structure audit (8 Nov 2026)

Scope: coverage against u.ae/ICP visa lists, the three CLAUDE.md step-9 audits, uncited facts (168 of 1,366 facts are not cited), and structure (duplicates, contradictions, cross-references, order). Order of sections matches the Malaysia template (Background, Visas not open, visas most-used first, then Changing visa type to Contacts); the free-zone, green, golden and other-residence sections are UAE additions in a sensible place. Anchors in `old:` are exact and unique in doc.md (checked by script). Every proposed sentence cites existing fact ids whose quotes I checked; status of weak facts is noted in `why`.

## A. Contradictions

### 1. CONTRADICTION
- where: Changing visa type, first bullet
- old: `- **Visit visa to family or employment residence:** Yes. An entry visa can be converted to residence without leaving the UAE after paying the fee [F0026]; ICP charges AED 500 for the status change and GDRFA adds AED 500 for a person inside the country [F0014, F0019]. For Bangladeshis, new employment visas and company-to-company transfers have been restricted since July 2024 [F0030].`
- new: `- **Visit visa to family or employment residence:** The law lets an entry visa be converted to residence without leaving the UAE after paying the fee [F0026]; ICP charges AED 500 for the status change and GDRFA adds AED 500 for a person inside the country [F0014, F0019]. For Bangladeshis, turning a visit visa into a work visa has been closed for several years, and new employment visas and company-to-company transfers have been restricted since July 2024 [V0012, F0030].`
- why: Says "Yes" while "Visas not open" and Job-seeker Step 3 say visit-to-work is closed to Bangladeshis [V0012].

### 2. CONTRADICTION
- where: Work visa: company worker, Step 1, item 2 (women domestic workers) vs Work visa: domestic worker, Steps 1-2
- old: `BMET's curriculum for women going to Gulf countries takes women aged 25 to 40 at admission, with at least class 5, able to read and write a sentence in Bangla and English, at least 4 ft 10 in tall and 40-65 kg, and runs for 2 months; women who are pregnant or whose youngest child is under 5 are not admitted [B0103]. For clearance as a domestic worker a woman must prove she is 25 to 45 and bring a no-objection letter from her legal guardian [B0016].`
- new: `The course, its admission rules and the clearance age (25 to 45) are under Work visa: domestic worker, Steps 1 and 2 [D0217, D0198].` Then add to the Need to know block after domestic Step 2: `> - Is the housekeeping course one month for women aged 25 to 45 whose youngest child is at least 6 (2023 policy [D0198, D0200, D0202]), or two months for women aged 25 to 40 whose youngest child is at least 5 (2024 GCC curriculum [B0103])?`
- why: Two sections give different course length (2 months vs 30 days), upper age (40 vs 45) and child age (5 vs 6); also duplicated content.

### 3. CONTRADICTION
- where: Work visa: domestic worker, Step 3, item 2 ("Check it is real") vs "If you aren't paid" Need to know
- old: `then call MOHRE on 80060, choose your language, press 2 (domestic workers) and ask an agent, or search Services, Enquiry services, "Company Information" on mohre.gov.ae [D0134];`
- new: `then search Services, Enquiry services, "Company Information" on mohre.gov.ae [D0134];`
- why: The doc instructs calling 80060 here (from a "lead" news fact) while asking elsewhere whether 80060 is a current MOHRE number; keep the existing Need to know line until confirmed.

### 4. CONTRADICTION
- where: Contacts, MOHRE line (also Step 5 item 1 and "If you aren't paid" say 24 hours)
- old: `- **MOHRE (labour ministry):** 600590000, 8 am to 8 pm, several languages, for labour complaints and to check a labour ban [G0117, G0128].`
- new: `- **MOHRE (labour ministry):** 600590000, 24 hours, also on WhatsApp, for labour complaints [W0072, L0055, G0117]; labour-ban checks on the same number 8 am to 8 pm, several languages [G0128]; Labour Claims and Advisory Centre 80084, toll free [L0149].`
- why: Same number given as "24 hours" [W0072] in Step 5 and complaints, and "8 am to 8 pm" here and in change-employer/going-home sections.

### 5. CONTRADICTION
- where: Work visa: domestic worker, Step 5, item 2
- old: `(compulsory in Abu Dhabi and Dubai since 1 January 2025)`
- new: `(since 1 January 2025, in every emirate) [D0185, L0071]`
- why: "Your rights at work" says the insurance rule applies in every emirate [L0071]; this line limits it to Abu Dhabi and Dubai.

### 6. CONTRADICTION
- where: Having a child, step 3 vs "If a worker dies, is injured or loses the job" (membership)
- old: `to Foshwa Global, 3 Reem Residency, Um Hurair, Karama, Dubai (appointment needed; 8 am-4 pm Mon-Fri; +971 4 288 0190, WhatsApp +971 50 729 2294)`
- new: keep text; add to the Need to know block under Having a child: `> - Is Foshwa Global's (Reem/Rim Residency, Umm Hurair) phone +971 4 288 0190 [F0134] or +971 4 570 1648 [G0130], or does each serve a different desk?` and spell the place the same in both sections ("Umm Hurair").
- why: The same consulate service centre has two phone numbers and two spellings in two sections.

### 7. CONTRADICTION
- where: Contacts, In Bangladesh, Ministry line vs Welfare Board address in "If your family in Bangladesh asks for help" and "If a worker dies"
- old: `- **Ministry:** Probashi Kallyan Bhaban, 71-72 Old Elephant Road, Dhaka [B0096].`
- new: `- **Ministry and Welfare Board:** Probashi Kallyan Bhaban, 71-72 Old Elephant Road, Eskaton Garden, Ramna, Dhaka [B0096, G0057].`
- why: Same building appears as "Old Elephant Road" here and "Eskaton Garden" elsewhere; a reader may think they are two places.

### 8. CONTRADICTION
- where: Work visa: company worker, "Before paying" (cap year) vs Background "The cap"
- old: `- **Know the cap.** The Ministry fixed the UAE maximum at Tk 1,07,780 in 2017 [B0100];`
- new: `- **Know the cap.** The government's UAE maximum is Tk 1,07,780, set in 2016-17 [N0138, B0100];`
- why: Background says 2016-17, the step says 2017; the cap is also stated three times (In one minute, The cap, Before paying): Background "The cap" could point to this step.

## B. Duplicates

### 9. DUPLICATE
- where: Visas not open to Bangladeshis: status paragraph, Need to know, "### Scams" and "### Don't work"
- old: `**Status, November 2026.** The UAE has never announced a ban, but in July 2024, after Bangladeshis in the UAE protested in support of the quota reform movement, it quietly stopped issuing visit and work visas to Bangladeshis [V0001].`
- new: Replace the whole status paragraph and its Need to know with `**Status:** see Background ("Is it open now"); each visa below gives its own status line [V0001, V0009].` Move the sentence on why visit visas were curbed into Background (see entry 24). Move the two Need-to-know bullets under Tourist visa's status line. Move the "### Scams" paragraph (uaevisaonline.com) into Tourist visa, Scams, replacing its pointer "(see Visas not open to Bangladeshis, Scams)". Delete "### Don't work" (it only points to Tourist visa, Don't work). The section then is a plain list, as in Malaysia.
- why: The paragraph repeats Background status lines (2024 stop, no visas in 2025, 30-50 a day, skill visas only, 25% violators); H3 Scams/Don't work under a list of closed visas breaks the template.

### 10. DUPLICATE
- where: Work visa: company worker, Going home on leave, "The 2026 cancellations"
- old: `**The 2026 cancellations.** Since June-July 2026 the UAE has cancelled residence visas of Bangladeshis who were home on leave, without stated reasons; Bangladesh counted 985 cases by 3 August, the minister spoke of 4,000 in early September and about 4,800 by mid-September [N0022, N0001, N0002, N0003, N0018].`
- new: Replace this paragraph (through "...Filipinos and Nepalis were also hit [N0007].") with: `**The 2026 cancellations.** Since July 2026 the UAE has cancelled residence visas of Bangladeshis who were home on leave, about 5,000 by mid-October, with no formal reason given; the counts and possible causes are in Background ("Is it open now") [N0001, N0100, N0057]. Notices came by email, SMS or through the sponsor; some learned only at check-in, and some had visas with over a year left [N0020, N0023, N0027, N0032]. In many cases the person had been away less than six months, so the visa had not lapsed under the 180-day rule but was cancelled through the sponsor [N0026].`
- why: Repeats the Background counts (and starts "June-July" vs "July" there); adds uncited N0026, which tells the worker the 180-day rule is not the cause.

### 11. DUPLICATE
- where: If a worker dies, In the UAE, item 2 (NOC list) vs The family in Bangladesh, item 3 (Dubai and Abu Dhabi NOC lists); item 4 (burial NOC) vs item 2 of the family steps
- old: `2. **Consulate NOC.** The Embassy (Abu Dhabi) or consulate (Dubai) issues the no-objection certificate. It needs [L0198, G0081]:`
- new: Replace item 2 and its seven bullets with `2. **Consulate NOC.** The Embassy (Abu Dhabi) or Consulate (Dubai) issues the no-objection certificate; the papers each asks for are under "The family in Bangladesh", item 3 [G0081, G0091]. Queries: 02 445 8182 or WhatsApp 050 361 4760 [L0201].` Delete item 4 ("Burial in the UAE needs the family's no-objection certificate sent through WEWB or MOFA [L0200].") since family item 2 says the same [G0091].
- why: Abu Dhabi NOC papers and the burial NOC are each listed twice in one section.

### 12. DUPLICATE
- where: Going home without valid papers, Bans after you leave (also stated in Change employer, Absent, and Step 2)
- old: `To check a labour ban, call MOHRE on 600590000; to contest it, send a grievance with documents through MOHRE's channels [G0128].`
- new: `To check or contest a labour ban, see "If you want to change employer".`
- why: The check-and-contest method is given four times (change employer, absent, Step 2, here).

### 13. DUPLICATE
- where: Going home without valid papers, If you are detained
- old: `After 57 Bangladeshis were sentenced for street protests in July 2024 (three to life), the UAE President pardoned them in September 2024 and ordered them deported [N0033, N0035].`
- new: delete
- why: Stated in Background ("What closed it before") and "What can get you jailed"; adds nothing to what a detained worker does.

## C. Cross-references

### 14. XREF
- where: Work visa: company worker, Step 1, "If an agency or broker takes your money"
- old: `Complain to BMET or the Ministry as in the Malaysia procedure;`
- new: `Complain in writing, with evidence, to BMET's Director General: free, decided within 30 working days; Director (Employment) 01711111544, diremi@bmet.gov.bd [D0222];`
- why: Points to another country's doc; the UAE doc must be self-contained.

### 15. XREF
- where: Your rights at work, first paragraph
- old: `Free zones such as JAFZA have their own rules for some matters (see Notes).`
- new: `Free zones such as Jafza have their own rules for some matters (Work visa: free zone employee) [W0044].`
- why: "Notes" is not a section of the doc (notes.md is internal). The paragraph also has no citations at all (for the sentence checkers).

### 16. XREF
- where: Work visa: domestic worker, Scams, "The visit-visa job"
- old: `(see Work visa (company worker), Step 1 on checking a visa)`
- new: `(see Work visa: company worker, Step 5)`
- why: Visa checks are in Step 5, not Step 1.

### 17. XREF
- where: Tourist visa, Scams, last line
- old: `use the complaint ladder in Work visa: company worker, Scams.`
- new: `complain as in Work visa: company worker, Step 1 ("If an agency or broker takes your money") and Step 5 ("If a check fails").`
- why: The company-worker Scams section has no complaint ladder.

### 18. XREF
- where: Background, "The channels", first bullet
- old: `with interviews at the Bangladesh-Korea Technical Training Centre (Step 1) [N0078, N0077].`
- new: `with screening at the Bangladesh-Korea Technical Training Centre from 18 May 2026 [N0078, N0077].` Better: also add to Step 1 a short item: `**Through a named employer's drive.** Dubai Taxi's 2026 hiring (6,000 drivers, 1,500 in the first phase) goes only through Al Anas Overseas, VIP Global and M Bahar Overseas, with screening at the Bangladesh-Korea Technical Training Centre; drivers must communicate in English [N0077, N0078, N0079]. Workers paid at least Tk 3.5 lakh for such jobs in May 2026; the state minister asked for Tk 1 lakh [N0080].` 
- why: "(Step 1)" points to a step that never mentions Dubai Taxi or the TTC screening; the biggest live channel has no "how" in the steps.

### 19. XREF
- where: Going home without valid papers, If you are detained
- old: `The Consulate says WEWB members (see "If a worker dies") get help`
- new: `The Consulate says WEWB members (see "If a worker dies, is injured or loses the job") get help`
- why: Membership is explained in the parent section's intro, not under "If a worker dies".

### 20. XREF
- where: Coming home, second bullet
- old: `travel bans (Dubai Police service, Step 2 above)`
- new: `travel bans (Dubai Police service, Going home without valid papers, Step 2)`
- why: "Step 2 above" has no Step 2 in Coming home.

### 21. XREF
- where: If a worker dies, The family in Bangladesh, item 4 (list numbering)
- old: `   4. **At the airport.** The Board's desk gives a Tk 35,000 cheque`
- new: `4. **At the airport.** The Board's desk gives a Tk 35,000 cheque` (remove the three leading spaces)
- why: The indent nests item 4 inside item 3's list, so pandoc renumbers it and the following "5." and "6." break.

## D. Gaps (coverage, step-9 audits, uncited facts)

### 22. GAP
- where: Background, Size (corridor numbers vs history and other countries)
- old: `Before the curbs about 5,000 to 6,000 a month went [N0061].`
- new: `Over 2004 to May 2025 BMET counts 2,207,991 Bangladeshis sent to the UAE, with a peak of 419,355 in 2008 [B0105]; Saudi Arabia took 38.85 lakh over 2004-2024 [N0122]. In January to September 2026 UAE clearances more than doubled while Saudi Arabia's fell 45.5%, Qatar's 37.4% and Kuwait's 33.4% [N0045, N0046, N0047].`
- why: Step-9 aim (4) asks for corridor numbers against other countries; uncited official B0105 (possibly-outdated) and N0046/N0047; N0122 is "lead".

### 23. GAP
- where: Background, "Visa by visa" (growth opportunities and big names)
- old: `Dubai Taxi Company plans to hire 6,000 Bangladeshi drivers this year, and construction helpers, masons and steel fixers are the largest 2026 clearance categories [N0077, N0090].`
- new: append `Bangladeshis are already the largest group among Dubai Taxi's 15,000 drivers, about 8,000, and the company has taken about 3,000 from Bangladesh since 2017 [N0081]. 788 workers were cleared as delivery bike riders in 2026 [N0091]. The government says it has begun the process of reopening the UAE labour market [G0102].`
- why: Insider test (big employers) and growth opportunities; N0081, N0091 (verified), G0102 (verified) are uncited.

### 24. GAP
- where: Background, What closed it before, 2025 line
- old: `the envoy was told over 25% of the UAE's visa and residency violators are Bangladeshis [N0074, N0075, N0076, N0064].`
- new: append `Government insiders say recruitment fraud, fake documents and visa violations also led the UAE to tighten screening, and visit visas were curbed because Bangladeshis used them to find work [N0063, V0013]; Bangladesh's Foreign Ministry calls the restrictions a UAE policy decision [N0066]. In January 2026 industry insiders listed the UAE among countries that often reject Bangladeshi visa applications [V0207].`
- why: Insider test: the latest refusal status and the stated reasons; N0063, N0066, V0207 uncited; V0013 moves here from "Visas not open" (entry 9).

### 25. GAP
- where: Background, choke point (scandal, 2026)
- old: `Workers sent on those cards got neither legal status nor jobs, and many slept in parks [A0003].`
- new: append `In September 2026 a politician alleged that BMET had suspended clearance cards for a week while cards were being issued through back channels for more money [B0101].`
- why: Insider test: the current smart-card scandal; B0101 uncited (news).

### 26. GAP
- where: Background, What Bangladesh has done
- old: `The Ministry asked the UAE to re-examine the cases [N0017].`
- new: append ` Affected returnees, organised as "Amra Remittance Joddha", demanded monthly allowances of Tk 15,000-20,000, jobs in other countries and high-level talks with the UAE on 7 September 2026 [N0004].`
- why: Insider test (the group journalists cover); N0004 uncited.

### 27. GAP
- where: Tourist visa, Step 3 (real cost); answers an existing Need to know
- old: `compare with the Amer price list (amer247.com) for Dubai visas [V0186].`
- new: append ` Dhaka agencies sell a 30-day Dubai tourist visa package for Tk 1 to 2 lakh, against about AED 340 (about Tk 11,400) for the visa online [N0112].` and delete the Need-to-know bullet `> - What do Dhaka travel agencies charge for a UAE tourist visa package in 2026?`
- why: Insider test (street price vs official); N0112 uncited.

### 28. GAP
- where: Work visa: company worker, Step 1, item 4 (demand letter attestation)
- old: `both companies' licences and the UAE company's quota [B0028, B0029, B0030].`
- new: append ` The Consulate charges the company AED 221, cash, non-refundable, at Room 14 [W0110].`
- why: Cost of the attestation step; W0110 (verified) uncited.

### 29. GAP
- where: Work visa: company worker, Leaving at the end of the job, item 4
- old: `4. **Cancellation.** The employer cancels the work permit and residence; you then have 30 days' grace to leave or change status [G0067].`
- new: append ` To cancel, the employer needs your signature on the labour contract cancellation and on a letter confirming you received all wages and end-of-service benefits [W0034].`
- why: The signature is the worker's only leverage over final pay; W0034 (verified) uncited.

### 30. GAP
- where: If you want to change employer, The one-year ban
- old: `It runs from your departure and lifts by itself [L0132].`
- new: append ` It does not apply to family-sponsored workers, a new permit with the same firm, skilled workers or Golden visa holders [L0129, G0127].`
- why: "Bans after you leave" mentions exemptions; this section (the main one) does not; L0129 uncited.

### 31. GAP
- where: If your employer reports you absent, What it is
- old: `Absence over 7 consecutive days, or 20 in a year, also allows dismissal without notice [L0121].`
- new: append ` Dismissal without notice needs a written investigation and a written, reasoned decision [L0122].`
- why: Rights at work; L0122 (verified) uncited.

### 32. GAP
- where: If you lose your passport, item 2 (cost of a new passport; partly answers a Need to know)
- old: `It takes 4-6 weeks (urgent about 15 days) if no police verification is needed and your data match your NID [G0084].`
- new: append ` Missions charge labourers and students a lower rate: 48 pages, 5 years USD 30 (express USD 45); 10 years USD 50 (USD 75) [B0067].` and add to the Need to know: `> - Does the Abu Dhabi Embassy charge workers the labourer rate (USD 30 [B0067]) or the general AED 405 [F0140]?`
- why: Cost of the most common consular service; B0067 (verified) uncited.

### 33. GAP
- where: If a worker dies, is injured or loses the job, membership steps (Abu Dhabi route missing)
- old: `If you lose it, download it again from wewb.gov.bd with your passport number [G0132].`
- new: append ` In Abu Dhabi, pay the AED 200 into the Embassy's or labour wing's bank account and hand in the application, papers and receipt; the labour wing grants membership after checking [B0025]. Workers who already have a BMET clearance card do not need membership [B0060].`
- why: Steps describe only Dubai; B0025, B0060 (verified) uncited.

### 34. GAP
- where: Work visa: domestic worker, intro (visa types)
- old: `138 were active in July 2026 [D0133, D0136].`
- new: append ` Offices sell three packages: traditional, where the worker is on the household's file and lives with it for the two-year contract; temporary, where the worker is registered with the office on a two-year contract and the office is the employer; and flexible, where an office worker is hired by the hour, day, week or month [D0128, D0129, D0036, D0130].`
- why: Domestic visa types missing (step-9 "types"); who the employer is changes where a worker complains; facts possibly-outdated.

### 35. GAP
- where: Work visa: domestic worker, Step 4 (pay; partly answers a Need to know)
- old: `For the rest of BMET clearance, see Work visa (company worker).`
- new: append ` A Dubai licensed centre quotes general housemaids at AED 1,000-1,400 a month and nannies at AED 1,400-1,800, with no separate Bangladeshi rate [D0194].`
- why: "What will I earn" for domestic workers; D0194 uncited (news).

### 36. GAP
- where: Work visa: domestic worker, Your rights at work, Need to know
- old: `> - Does any UAE rule give a domestic worker the right to keep and use her own mobile phone?`
- new: add after it: `> - Are days 16-30 of a domestic worker's sick leave half-paid (decree-law [D0024]) or unpaid (MOHRE page [D0124])?`
- why: Logged conflict (D0124) never surfaced; it changes what a worker claims.

### 37. GAP
- where: Business visit, Events (official visa list: Sept 2025 categories)
- old: `GDRFA grants 30, 60 or 180 days for AED 200 to 400 plus VAT and an AED 1,000 deposit [V0044, V0139, V0140].`
- new: append ` The same September 2025 decision added visit visas for AI specialists, entertainment visits and cruise or leisure-boat tourism [V0138].` Then a Need to know: `NEED: Is ICP's truck-driver visa (single or multiple trips, sponsored by a shipping or cargo company, from the September 2025 decision) issued to Bangladeshi drivers, and on what terms?` (source saved: icp-news-four-new-visit-visa-categories; no fact logged)
- why: Four visa categories on ICP's list are absent from the doc; the truck-driver visa is a possible work route for Bangladeshi drivers.

### 38. GAP
- where: Visas not open to Bangladeshis, list (official list coverage)
- old: `- **Converting a visit visa to a work visa inside the UAE:** closed to Bangladeshis for several years [V0012].`
- new: add after it: `NEED: log a fact from icp-news-four-new-visit-visa-categories ("foreign nationals whose countries are experiencing wars, disasters, or unrest without the need for a sponsor") and confirm Bangladesh is not covered, then list: "**One-year humanitarian residence without a sponsor:** only for nationals of countries in war, disaster or unrest".`
- why: A residence type on ICP's list that is closed to Bangladeshis is not listed.

### 39. GAP
- where: Other residence visas (Blue visa)
- old: `- **Property-owner visa:** a fully built, wholly owned, habitable property registered with the land authority, plus income of at least AED 10,000 a month or proof of solvency [F0116].`
- new: add after it: `NEED: Who qualifies for the 10-year Blue residence, and can Bangladeshis get it? (u.ae page saved as sources/uae-portal-blue-visa.md; no fact logged)`
- why: The doc cites a 180-day grace period for "Blue residence holders" [G0067] but never says what the Blue visa is.

### 40. GAP
- where: Your rights at work, after Gratuity (migrant's question: pension)
- old: `Unpaid absence does not count as service [L0112]; the employer may deduct money you owe [L0113].`
- new: `NEED: Does a foreign private-sector worker get any pension or social-security contribution in the UAE, or only the end-of-service gratuity, and can low-wage workers join MOHRE's voluntary end-of-service savings scheme?`
- why: Step-9 migrant's question "pension" is not answered anywhere.

### 41. GAP
- where: Work visa: company worker, Step 3, "Why it can be refused" (appeal if refused)
- old: `Companies accused of human trafficking or with unfit labour housing get no new permits [W0007].`
- new: `NEED: Can a refused work permit or employment entry permit be appealed, and by whom (the employer through a MOHRE grievance, or an ICP/GDRFA reconsideration request)?` Also add to Family residence Step 3 Need to know: `> - Can a refused family residence application be appealed, and where?`
- why: Step-9 per-visa "appeal if refused" is missing for work and family residence (only asked for tourist visas).

### 42. GAP
- where: Going home without valid papers, Bans after you leave
- old: `Forging or using a forged visa or residence permit can bring up to 10 years' prison and deportation [G0110].`
- new: append ` A Foreign Ministry official says a cancelled residence or a broken law bars re-entry for 5 to 10 years [N0104]; the protesters deported in 2024 had their fingerprints kept and may not get into the UAE or other Gulf states again [N0103].` Then Background "Bans" can point here.
- why: The ban length is stated only in Background, not in the step it belongs to.

### 43. GAP
- where: What can get you jailed, Protests
- old: `Calling for unpermitted demonstrations online: jail and/or AED 200,000 to 1 million [L0242].`
- new: append ` Article 212 of the 2021 Penal Code sets life imprisonment for calling for, attempting or inciting marches or meetings meant to cause riots [N0105].`
- why: Explains the 2024 life sentences; N0105 is "lead" status, so confirm against the Penal Code text before using.

### 44. GAP
- where: Going home without valid papers, amnesty paragraph (crackdowns)
- old: `about 50,000 Bangladeshis regularised and more than 5,500 went home on travel permits without a ban [G0094].`
- new: append ` After it ended the UAE announced inspections and arrests of violators from January 2025 [G0095].`
- why: Insider test (crackdowns); G0095 uncited.

### 45. GAP
- where: Contacts, In Bangladesh
- old: `- **Airport desks:** Chattogram 01913631797, Sylhet 01558277904 [B0023].`
- new: add after it: `- **UAE Embassy, Dhaka:** House 191, Road 69, Gulshan North Avenue, Gulshan-2; +8802222284295; dhakaemb@mofa.gov.ae; 9 am to 4 pm, closed Friday and Saturday [V0196].`
- why: The doc names the UAE Embassy (attestation, courtesy visas, verifying agents) but never gives its contact; V0196 is possibly-outdated.

### 46. GAP
- where: Work visa: domestic worker, Leaving or changing employer, Need to know (bring a spouse)
- old: `> - Can a domestic worker move to a company (labour law) visa without leaving the UAE, and how?`
- new: add after it: `> - Can a domestic worker sponsor a spouse or children, and does the AED 4,000 (or AED 3,000 plus housing) salary rule apply to them [F0002]?` Also copy the domestic-to-company question into Changing visa type.
- why: Step-9 per-visa "bring a spouse" and "changing visa type" are unanswered for domestic workers.

### 47. GAP
- where: Changing visa type (mission visa)
- old: `- **Student to work:** Only with a new employer work permit; a university visa lasts until 180 days after study ends [F0072].`
- new: add after it: `NEED: Can a worker on a 3-month mission work visa be moved to a two-year employment residence without leaving the UAE?`
- why: The section omits the mission visa, which the doc lists as a work route.

## E. Uncited facts reviewed (168): left out for a good reason

- Duplicates of cited facts: G0003, G0004, G0065, V0047, V0184, W0032, W0043, W0077, W0079, W0090, W0095, W0111, B0034-B0040, B0063, B0089-B0093, B0107-B0112, D0151-D0152, N0030, N0083, N0132, N0134, N0139-N0140, G0096, L0041, L0150, V0197.
- Background or news detail with no bearing on a decision: N0008, N0015, N0016, N0024, N0039, N0040, N0043, N0048, N0054, N0058, N0059, N0060, N0067, N0070, N0072, N0097, N0106, N0114, N0120, N0121, V0014, B0102.
- Old or superseded legal detail (possibly-outdated, kept in facts): V0052, V0059, V0061, V0081, V0082, V0105, V0129, V0132, V0163, V0178, W0001, W0003, W0020, W0025, W0061-W0064, W0075, W0078, W0088, W0108, W0109, L0079, L0099, L0115, L0136, L0143, L0197, L0209, L0249, D0012, D0013, D0028, D0031, D0033, D0034, D0041, D0044, D0047, D0049, D0052, D0056, D0057, D0059, D0061, D0067, D0076, D0089, D0105, D0108, D0109, D0111, D0115, D0131, D0132, D0141, D0142, D0144, D0163, D0165, D0166, D0193, B0006, B0012, B0031, B0033, B0104, B0105 (used in entry 22), B0106, F0125, W0047, N0082.
- Worth a second look but not proposed: L0099 (no ILOE premium due while an absconding complaint is open), D0061 (Court of Appeals vs first-instance court for domestic MOHRE decisions: a conflict that could become a Need to know), W0063 (recruitment agencies' AED 300,000 guarantee).

TOTAL: 47
