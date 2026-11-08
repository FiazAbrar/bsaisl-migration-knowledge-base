# Maldives doc: coverage audit, round 1 (8 November 2026)

Auditor: coverage (CLAUDE.md research step 9, the three audits, plus uncited facts and structure). Doc read in full (1,567 lines). Facts: 1,120 logged, 1,004 distinct ids cited, 116 uncited, 0 cited ids missing from facts.csv.

Official visa list used: Immigration Act 2007 s.9(a), eight types (Tourist, Diplomatic, Student, Business, Dependant, Work, Resident, Special) (`sources/immigration-mv-act-2007-en.txt` lines 132-142, s.17 at 203-218), plus immigration.gov.mv pages saved as `immigration-mv-*.md` (Work, Business, Tourist, Meeting, Dependent, Marriage, Resident incl. Corporate Resident, Sponsorship Declaration, Traveller Declaration).

Covered and fine (no finding): Tourist (incl. extension, sponsored visit, transit), Meeting, Business (thin, see 10), Dependent, Marriage, Resident/Corporate Resident, Student, Diplomatic (in "Visas not open"), Asylum (discouraging, F0082-F0085), Having a child, Bank account and SIM, Bestinet, Operation Kurangi, the dollar crisis, the 2019 and 2024 halts, the 2024 syndicate, the quota-fraud cases, the "free visa", real costs, hundi, deportations, deaths.

---

## A. The migrant's questions

### 1. How long can I stay: answered (How long you can stay, L635), small gap. LOW
- Where: How long you can stay, L637-657.
- Missing: the regulation lets a worker hold only one work permit (so a second job is illegal). The Need to know on days to leave after cancellation (L657) stays open.
- Fix: add "Each worker may hold only one work permit [L0101]." after L639.

### 2. What will I earn: weak. MEDIUM
- Where: What the job pays, L122-130; Step 1 item 4, L215-220; Step 1 item 5, L244.
- Missing: (a) the job-order pay (USD 250-350, the High Commission's USD 250 minimum) is never given in taka or MVR, so it can't be set against the MVR 6,760 average (L124). USD 250 is about MVR 3,855, roughly half the average, and nothing explains the gap (resort service charge? skilled jobs?). (b) No take-home pay by sector; only a Need to know (L130).
- Fix: add the Tk/MVR conversion of USD 250-350 to L208 and L244, using the G0014/G0015 rates. Research a 2026 take-home figure for resort and construction work (Bangla news, RMMRU, PILC 2024 survey `N0082` source). Add the service-charge link (L574) to What the job pays, because resort pay depends on it.

### 3. My rights at work: answered (Your rights at work, L543), but the protection against retaliation is missing. HIGH
- Where: If you aren't paid, L679-686; Your rights at work, Contract and probation L553-558.
- Missing: the Employment Act says a complaint against the employer is not a reasonable cause for dismissal (L0010). It is logged but uncited, and it is the single fact that most changes whether a worker complains. Also uncited: dismissal without notice only for unacceptable conduct (L0015); disciplinary suspension at most 14 days (L0008).
- Fix: in If you aren't paid, before "Complain in this order", add "Complaining against your employer is not a lawful reason to dismiss you [L0010]." Add L0015 to If you lose the job (L1456-1460) and L0008 to Contract and probation.

### 4. What gets me jailed: answered (What can get you jailed, L659), but the section leaves out the causes that most often hit Bangladeshis. HIGH
- Where: What can get you jailed, L661-671.
- Missing, though the facts are logged (some cited elsewhere):
  - running a business on a work visa, the main reason Bangladeshis are detained in raids: U0045, U0123, N0089 (now only at L171 and L975);
  - trading currency and letting someone else use your bank account (accomplice liability): G0034, G0035 (now only in Sending money home, L1359);
  - gambling: U0046 (38 Bangladeshis handed over for deportation over drugs and gambling, L977);
  - any breach of any Maldivian law can cost you the visa: V0116 (uncited);
  - whipping for small drug amounts: L0154 (uncited);
  - working on a tourist or business visa and overstaying: link to Can you work? (Tourist visa).
- Fix: add a bullet each with those ids, linking to The crackdown and Sending money home rather than repeating them.

### 5. Bank account and SIM: answered (Step 7: After arrival, items 7-8, L523-539). LOW
- Missing: why so many workers don't have accounts (no documents, so they depend on intermediaries): G0051, uncited. SIM cost and Ooredoo's rules are a Need to know.
- Fix: add G0051 to Step 7 item 7 or to Sending money home. Research Ooredoo and Dhiraagu prepaid SIM prices (public tariff pages).

### 6. Pension: Maldives side answered (Pension, L624); Bangladesh side weak. MEDIUM
- Where: High Commission services item 5, L1543.
- Missing: the Bangladesh universal pension scheme for migrants (the "Probash" scheme of the National Pension Authority): monthly contribution tiers, how to register from Malé, what it pays. As written, it is a bare instruction ("register"), which breaks the "Say how" rule.
- Fix: research upension.gov.bd and the National Pension Authority's Probash scheme page (contribution amounts, online registration, payment from abroad), log the facts and turn item 5 into steps.

### 7. Can my family come: answered (Bringing your family, L803). The legal basis conflicts and the conflict isn't flagged. MEDIUM
- Where: Bringing your family L805; Dependent visa L1134; Student visa Need to know L1276.
- Missing: Immigration Act s.14 defines the dependant visa as for the spouse or child of any foreign permit holder (F0025, uncited). Immigration's website limits it to professional-category work visa holders (F0001). The doc gives only the website rule.
- Fix: add one Need to know under Bringing your family: "Immigration Act s.14 gives a dependant visa to the spouse or child of any permit holder [F0025]: does Immigration ever apply it to a non-professional worker or a student?" Cite F0025 in the student-spouse Need to know (L1276).

### 8. What can I bring (in and home): bringing home answered (Coming home, L1462); what you may carry INTO the Maldives is missing. HIGH
- Where: Step 6 item 5 "Before you fly", L489; What can get you jailed.
- Missing: Maldives Customs bans bringing in idols for worship, pork, alcohol (without a permit), vapes and e-cigarettes, pornography, narcotics and materials "contrary to Islam" (G0040, uncited). Hindu Bangladeshi workers carrying a small idol, and anyone carrying a vape, are caught by this. The duty-free allowance on arrival (G0041) is also uncited.
- Fix: add to Step 6 item 5: "Do not pack idols for worship, pork, alcohol, vapes or e-cigarettes, or pornography: Maldives Customs bans them [G0040]." Link it from What can get you jailed. G0041 is optional. G0040 is from a 2024 notice: confirm on customs.gov.mv.

## B. The original aim

### 9. Official visa list: every Act type is present except Special visa, which has no section. MEDIUM
- Where: no H2. The special visa appears only in Transit and medical treatment (L1282), Asylum (L1305-1306), Marriage visa (L1222) and the W0032 scam (L336).
- Missing: one place that states what a special visa is and its four purposes under Act s.17 (humanitarian work, continuing medical treatment, a court case to claim a right, a case where a government authority deems it necessary), with form IM22 and the fee. Humanitarian work isn't mentioned anywhere. "Visas not open to Bangladeshis" is fine for Diplomatic. No visa on the immigration.gov.mv list is missing.
- Fix: add a short H2 "Special visa" after Transit and medical treatment. Use V0035, V0052, V0037 and F0028; log the s.17 humanitarian purpose from `immigration-mv-act-2007-en.txt` (L203-218). Link it from Asylum and Marriage visa instead of explaining it there.

### 10. Business visa: no fee, no processing time, no scams, no appeal. MEDIUM
- Where: Business visa, L1104-1126.
- Missing: fee and processing time (Need to know only). There is no Scams subsection, although the main business-visa scam (sold as a work visa; since 15 September 2026 it can't become a work permit inside the country, W0032) sits under the company worker's Step 2 (L336).
- Fix: add "Scams" under Business visa citing W0032 and link it from the company Step 2. Research the fee on business.egov.mv and the Ministry of Economic Development's service charter.

### 11. Professional work visa: doesn't say the holder can bring family, and gives no timing. MEDIUM
- Where: Work visa: professional, L828-881.
- Missing: (a) the main practical difference from a company worker, that a professional can bring a spouse, children under 18 and parents (F0001, F0002), isn't stated in this H2; (b) MQA processing time (Need to know); (c) no pointer saying the company-worker problem sections (If you aren't paid and the rest) apply.
- Fix: add to the intro "You can bring your spouse, children under 18 or parents (see Dependent visa) [F0001, F0002]." and one line linking Your rights at work through Going home on leave. Research MQA turnaround (mqa.gov.mv service charter).

### 12. Domestic worker: pay, real cost and processing time missing. LOW
- Where: Work visa: domestic worker, L883-915.
- Missing: what the woman pays (the approved agency may take nothing, F0108, which is cited) against what is really paid; pay (Need to know); processing time.
- Fix: research Bangla news on Maldives housemaid recruitment 2024-26; otherwise the Need to knows already ask the right questions.

### 13. Student visa: no scams, no work rule, no spouse rule. LOW
- Where: Student visa, L1236-1276.
- Missing: whether admissions agents in Dhaka sell Maldives "student visas" as a work route; part-time work (Need to know).
- Fix: search Bangla news for "মালদ্বীপ স্টুডেন্ট ভিসা" (Maldives student visa) and MNU international-student rules on work.

### 14. Appeal if refused: absent for every visa except the Employment Tribunal route. MEDIUM
- Where: Step 3 Need to know (L385); Tourist Step 3 (L1035); nothing under Business, Dependent, Marriage, Student or Sponsorship.
- Missing: whether an Immigration refusal or revocation can be challenged (internal review, Civil Court, judicial review) and within what time.
- Fix: read Immigration Act 2007 in full for a review or appeal clause and the Act's revocation section (s.20, `immigration-mv-act-2007-en.txt` L276-290). Log what you find, or add one Need to know under Changing visa type.

### 15. Changing visa type contradicts the Marriage visa section and leaves out the business/special-to-work rule. HIGH
- Where: Changing visa type, L1292; Marriage visa Step 3 item 2, L1207.
- Wrong: L1292 says a switch to a marriage visa needs a Sponsorship Declaration filed from outside the Maldives. F0036 (Immigration's marriage page) says a foreigner already in the Maldives on another valid visa, such as a work visa, can change category after the marriage is registered. The doc states both.
- Missing: business or special visa to work permit is impossible inside the Maldives since 15 September 2026 (W0032).
- Fix: replace the L1292 bullet with two: "To a sponsored visit or dependent visa: the Sponsorship Declaration is filed only while the person is outside the Maldives [V0062, V0055]." and "To a marriage visa: from any valid visa inside the Maldives, once the marriage is registered (see Marriage visa (spouse of a Maldivian)) [F0036]." Add "Business or special visa to work: not possible without leaving; the worker needs an Entry Pass issued before travel [W0032]."

### 16. Corridor numbers against other countries: thin. MEDIUM
- Where: Is it open now, Size L47-52.
- Missing: Bangladesh's share of new Maldives work permits (17,039 of 75,542 foreigners, 17 November 2023 to 30 January 2025: N0024, uncited) and Bangladesh's share of BMET's total (32,408 of 626,601 in 2026: N0003, uncited). The deposit comparison by nationality (L355) is good.
- Fix: add both to Size, "Other nationalities" and "Departures", with N0024 and N0003.

### 17. Growth opportunities: the "demand for nurses and accountants" line ignores the phase-out. HIGH
- Where: Status, Demand L22; The channels, Professionals L34.
- Wrong or missing: the doc reports the High Commissioner's July 2026 claim that the Maldives wants nurses and accountants (N0102). The same doc (L647-648) shows Regulation 2025/R-120 ending quotas for accountants two years after 14 December 2025 (about December 2027) and for nurses after three years (W0139, W0140). Someone training for these jobs would act on the first line without seeing the second. Also uncited: where the demand actually comes from, namely reclamation at RasMale, Gulhi Falhu, Thilafushi and Uthuru Thila Falhu, the new Velana airport terminal and new resorts (N0039, 2024).
- Fix: append to L22 and L34: "but quotas for accountants end two years, and for nurses three years, after 14 December 2025 (see How long you can stay) [W0139, W0140]." Add N0039 as a Demand bullet (construction sites).

### 18. "Tried by workers" scams: one line only. MEDIUM
- Where: Scams, Tried by workers, L824-826.
- Missing (all in facts, mostly cited elsewhere): forged certificates for professional jobs (W0112); buying a "free visa" to work for someone else (N0030, N0031); running a business on a work visa (N0089, U0045); marriage to stay legal, with the Family Court now checking legal residence (F0074, F0073); illegal dollar trading (G0034).
- Fix: turn it into a short list with those ids, linking to the owning sections.

## C. Insider test

What a journalist, a corridor expert and a returnee would expect, and whether it is in the doc:
- Bestinet and the Xpat contract: present (L77-85).
- Operation Kurangi, legalisation and the crackdown: present (L917-978).
- The dollar crisis, the kerb rate and the bank caps: present (L1326-1361).
- The 2019 ban, the 2023 reopening, the March 2024 halt and the 10-per-employer limit: present (L54-61).
- Quota sellers and the ACC/police quota-fraud cases: present (L65-72).
- The 2024 syndicate and the jobs that didn't exist: present but unnamed (L59), which is acceptable given the evidence.
- Real costs (Tk 2-4.6 lakh): present (L104-108). The street price for 2026 is a Need to know.
- Free or open visa, tourist-visa brokers: present.
- Passports held, missing reports, deaths, detention at Hulhumalé: present.
- Bad employers by name: missing (finding 19).
- The 2022 Malé labour-quarters fire: missing (finding 22).
- The 2021 MoU: missing (finding 24).
- The currency-switch pay cut: missing (finding 23).
- Airline fare and PDHA clinic cost: Need to know only (finding 26).

### 19. Two of the four example employers in Step 1 item 4 are on Xpat's Employer Negligence list. HIGH
- Where: Step 1: Find a real job, item 4, L217 (Rasheed Carpentry and Construction Pvt Ltd) and L219 (FEDO Private Limited).
- Missing: `sources/xpat-mv-employer-negligence-list.md` shows FEDO PVT LTD (C-0291/2011) with 58 confirmed negligence cases since 15 September 2025, the most on the list, and RASHEED CARPENTRY AND CONSTRUCTION PVT LTD (C-0235/1995) with 12. The doc presents both as ordinary permission-letter examples, and the notes say the names were deliberately left out. An insider will see this at once, and a worker offered a FEDO job needs to know.
- Fix: log two facts from that file (W prefix) and add to each example: "now on Xpat's Employer Negligence list with 58 (FEDO) / 12 (Rasheed) confirmed cases (Step 5, item 2) [new ids]." Consider naming North Coast Contractors (27) in Step 5 item 2 as an example of what the list shows.

### 20. Agency flag from agencies.csv not carried over. MEDIUM
- Where: Step 1 item 4, L219, The Ifthi Overseas (RL0894).
- Missing: agencies.csv records that the ACC sought RL0894's papers in July 2026 in its inquiry into women domestic workers sent on fake "returnee" passports (an inquiry, not a charge). CLAUDE.md says country docs name an agency's flags from agencies.csv.
- Fix: add one attributed, dated clause with the agencies fact ids (AC0022, AC0023, AC0026), or log a country fact pointing to the same source.

### 21. The agency's written undertaking to bear return costs and compensation is missing. HIGH
- Where: Step 1, Before paying (L268-284) and If an agency or broker takes your money (L286-292).
- Missing: B0164 (uncited). Under the Maldives permission conditions the agency files a Tk 300 stamp undertaking that the approved workers will get the job, pay and benefits, and that it will bear housing, food and return costs and any compensation if they don't. That is exactly the claim a worker stranded without a job (the 2024 pattern) can make at BMET.
- Fix: add to Before paying: "The agency signs an undertaking that you will get the job, pay and benefits in the letter, and that it will pay your housing, food, ticket home and compensation if not [B0164]." Reference it in the BMET complaint item 2.

### 22. Worker housing deaths: the best-known one is missing. MEDIUM
- Where: Housing, health and safety, L613-622; If a worker dies, L1442.
- Missing: the November 2022 fire in a Malé labour-quarters building (M. Nirufehi garage) that killed 10 workers, most of them Bangladeshi. It is the event journalists cite on Bangladeshi housing in Malé. The doc has only the 2026 Dhigurah fire and the gas explosion.
- Fix: research it (Atoll Times, Edition, Daily Star, November 2022), log it, and add one line to Housing, health and safety, showing the year as (2022).

### 23. The currency-switch pay cut is missing from scams. MEDIUM
- Where: What goes unpaid, L132-138; Scams, Done to workers, L813-822.
- Missing: L0149 (uncited): workers promised USD 350 were paid MVR 4,000 after arrival (about USD 260) and had their passports held. Insiders know this as the typical trick, and it explains why the letter of appointment must show both USD and MVR (L306).
- Fix: add a Done to workers bullet, "Pay promised in dollars, paid in fewer rufiyaa [L0149, N0067 (2023)]", linking to Step 2, item 1.

### 24. The 2021 Bangladesh-Maldives recruitment MoU is missing. LOW
- Where: What closed it before, L54-61.
- Missing: N0111: the MoU of 9 February 2021 on recruitment and the regularisation of undocumented workers.
- Fix: add a dated bullet with N0111 (2021). Add a Need to know: is the MoU still the framework in 2026?

### 25. Sector split sits only in the Domestic worker H2. MEDIUM
- Where: L885 (F0098). It is missing from Background Size (L47-52).
- Missing: where Bangladeshis actually work (33% hotels and resorts, 25% construction, 7% day labour, 2% domestic, 2% fisheries) is corridor big-picture information. N0100 (uncited) has the same figures from RMMRU directly.
- Fix: add a "Jobs" bullet to Size citing N0100 and F0098, and shorten L885 to the 2% with a link.

### 26. Two real costs a returnee would expect are still blank. MEDIUM
- Where: Step 6 item 4 Need to know (L486); Step 3 item 4 Need to know (L364).
- Missing: the Dhaka-Malé one-way fare and airlines (US-Bangla and Biman both fly the route); whether the PDHA runs in Bangladesh, with clinic names and fees. Both are researchable.
- Fix: research the airline websites and fare aggregators for Dhaka and Chattogram to Malé, and health.gov.mv's PDHA designated-clinic list. Log the facts and replace the Need to knows.

### 27. Debt bondage and service-access figures not used. LOW
- Where: How they borrow, L117-120; High Commission services intro, L1488.
- Missing: N0075 (PILC: work tied to debt in over 75% of cases); N0119 (74% could get High Commission services).
- Fix: add N0075 to How they borrow; N0119 is optional.

## D. Facts logged but not cited

The 116 uncited ids were reviewed. Findings 1, 3, 4, 7, 8, 16, 17, 21, 23, 24, 25 and 27 cover the substantive ones (L0101, L0010, L0015, L0008, V0116, L0154, F0025, G0040, G0041, N0024, N0003, N0039, B0164, L0149, N0111, N0100, N0075, N0119).

### 28. Other uncited facts worth placing. LOW
- N0114 (March 2025: stricter rules on recruiting Bangladeshis reimposed): What closed it before, before the "29 June 2024" bullet or as a March 2025 bullet.
- B0143 (7 clearances in 2023): Size, Departures, to show the ban year.
- N0065 (83% say formalities took under three months): Step 3, How long, in order.
- F0094 (the High Commission says work permits must be attested by it to be valid): cite in the Need to know at L265.
- W0036 (R-120 fines of MVR 50,000, 75,000 and 100,000 for repeat breaches): Your rights at work, Fines on bad employers, L576.
- W0080 (Xpat live chat, weekdays 8:30 am to 2 pm): Step 5, If it fails, L438.
- U0129 (LRA investigating 2,457 migrant cases, mostly missing workers, April 2025): If your employer reports you absconded, as a backlog figure near the Need to know on investigation time.
- U0030 (release after detention is difficult): If you are detained, L1401.
- L0110 (when a missing report is withdrawn, the deposit moves to the new permit): absconded, item 2.
- L0134 (2021: if an individual employer dies and the heirs do nothing within 30 days, workers are sent home from the deposit): Leaving at the end of the job, item 4, showing the year as (2021).
- B0071 (Chattogram and Sylhet airport desk emails): Coming home, Airport help.

Left out for good reason (duplicates or superseded): N0006, N0010, N0011, N0023, N0025, N0032, N0033, N0034, N0043, N0052 (unproven allegation), N0054, N0055, N0058, N0071 (superseded by the 2024 70%), N0077, N0079, N0081, N0098, N0099, N0107, N0109, N0110, N0112, N0117, B0020, B0058, B0084, B0102, B0126, B0127, B0144, B0148, V0033, V0036, V0050, V0051, V0078, V0081, V0087, V0088, V0118, G0001, G0010, G0012, G0013, G0022-G0025 (already a Need to know at L1335), G0030, G0053, L0052, L0058, L0086, L0096, L0098, L0103, L0111, L0113, L0133, L0142, L0159, L0177, L0178, L0179, F0026, F0080, F0097, U0026, U0047, U0048, U0058, U0087, U0093, U0104, U0125, U0126, U0128, U0130, U0134, W0022, W0028, W0050, W0053, W0142, W0167.

## E. Structure against CLAUDE.md

### 29. Fine for employer negligence: two figures with no explanation. HIGH
- Where: If your employer reports you absconded, L772 ("the employer is fined MVR 2,000", U0072); Step 5 item 2, L440, and Fines on bad employers, L576 (MVR 50,000 per worker, W0035, W0046, L0112); also L138.
- Wrong: a reader can't tell which applies. The Xpat missing-report guide's MVR 2,000 is probably a process fee, and the MVR 50,000 the penalty under the 8th amendment and R-120.
- Fix: at L772 write "the employer is fined (MVR 2,000 in Xpat's missing-report process [U0072]; up to MVR 50,000 per worker under Regulation 2025/R-120 [W0035])". Add a Need to know asking which is charged in practice, or confirm from the Xpat guide's context.

### 30. "Visas not open to Bangladeshis" comes before the visas. MEDIUM
- Where: H2 at L179.
- Wrong: CLAUDE.md says every open visa first, then the short list of visas not open.
- Fix: move the H2 to after Transit and medical treatment (before Changing visa type). Its cross-references stay valid.

### 31. "Undocumented workers: regularisation" sits in the middle of the visa list. MEDIUM
- Where: H2 at L917, between Work visa: domestic worker and Tourist visa.
- Wrong: it is not a visa, and it splits the visa sequence. The rules put problem procedures under the visa, and "going home without valid papers" after the visas.
- Fix: either make it an H3 under Work visa: company worker after If your employer reports you absconded (its H3s become H4s), or move it to just before Going home without valid papers. The first is closer to the rules ("being reported absent, or the country's equivalent").

### 32. Problem sections out of the required order. LOW
- Where: Leaving at the end of the job (L747) comes before If your employer reports you absconded (L765).
- Wrong: the rule order is: if you aren't paid, changing employer, being reported absent, leaving at the end of the job, going home on leave, bringing family, scams.
- Fix: swap the two H3s.

### 33. The Sponsorship Declaration procedure is given in full twice. MEDIUM
- Where: Visiting a relative (sponsored visit), L1062-1072, and Dependent visa Step 3, L1157-1167 (same IMUGA clicks, IM20, 5 working days, 30-day entry). The Marriage visa section links to the Dependent version (L1206).
- Wrong: CLAUDE.md wants one full procedure and links from everywhere else.
- Fix: keep the full steps once, in Dependent visa Step 3 (the more complete one). In Visiting a relative, keep only the visit-specific bits (category "Visiting", who can sponsor) and link "(see Step 3: Submit the Sponsorship Declaration on IMUGA)".

### 34. Ambiguous cross-references. MEDIUM
- Where:
  - L20 "(see Scams)" and L1019 "(see Scams)": four H3s are titled "Scams" (L811, L911, L969, L1084).
  - L982 "(see Can you work?)": two such headings (L1078, L1124).
  - L33 and L102 "(Step 1, item 4)": these sit in the Background, outside any visa H2, and seven H2s have a Step 1.
- Wrong: CLAUDE.md says references must be specific and must not be a bare name that could mean several places.
- Fix: L20 becomes "(see Work visa: company worker, Scams)" or use whatever unique form the build supports. L1019 points to the tourist one or is dropped (it is a self-reference). L982 becomes "(see Can you work? under Tourist visa)" or is dropped. L33 and L102 become "(Step 1: Find a real job, item 4)". Inside an H2 (L262, L328, L461, L517, L821) the bare "Step N, item M" is fine only if build.py resolves it within the same H2: check.

### 35. Rules stated several times instead of once with a link. LOW
- Where:
  - Quota MVR 2,000 and permit fee MVR 350: L11, L69, L190, L322, L342, L908.
  - Contract within 45 days: L299, L326, L378, L557.
  - Deposit MVR 8,000: L322 and L355.
  - 12,552 deported: L177 and L978.
  - Leave rules: L794-795 repeat L595.
  - Tourist cannot switch to work: L153, L181, L1090, L1290.
- Fix: keep the full statement in the owning step (Step 3 for fees and deposit, Step 2 item 3 for the contract, The crackdown for deportations, Leave and public holidays for leave) and cut the others to a link. The Background may keep one mention.

### 36. Our own words or advice, and fluff. LOW
- Where:
  - L186: "(not a Bangladeshi passport issue, listed for completeness)" is editorial, and the whole Israeli-passport bullet is irrelevant to Bangladeshis.
  - L436: "ask the employer for a screenshot of it before you fly" is our advice; W0180 only gives the status.
  - L444: "so use the verification page in item 1 if it fails" is our inference from W0157.
- Fix: drop the L186 bullet. Rephrase L436 as a fact ("The employer's Xpat record shows 'Issued (Pending Arrival)' once the deposit is paid [W0180]."). L444 can keep "The app was last updated in 2023 [W0157]; the verification page is in item 1."

### 37. The same link given twice in one bullet. LOW
- Where: L176, "(see If your employer reports you absconded)" appears twice.
- Fix: keep the second.

---

TOTAL: 37 findings: HIGH 8, MEDIUM 18, LOW 11.

HIGH: 3, 4, 8, 15, 17, 19, 21, 29.
MEDIUM: 2, 6, 7, 9, 10, 11, 14, 16, 18, 20, 22, 23, 25, 26, 30, 31, 33, 34.
LOW: 1, 5, 12, 13, 24, 27, 28, 32, 35, 36, 37.
