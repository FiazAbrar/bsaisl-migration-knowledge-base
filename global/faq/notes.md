# Frequently asked questions about going abroad: research notes

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

## How this part was built

- 84 questions (H4) in 10 stage groups (H3), under one H2, "Frequently asked questions".
- Most answers reuse facts already researched and cited in the country docs. Each reused fact was copied into this folder's `facts.csv` under prefix F (F0015 to F0364), with its source file, `_fetchlog.csv`, `_wayback.csv` and `sources.csv` rows. The fact's `note` column says which country and id it came from ("imported from qatar B0049"). Facts that the country folder logged with `--no-quote-check` (garbled Bangla PDF text, quote transcribed from the page image) were imported the same way and keep the original note.
- The Qatar doc was the main source for the Bangladesh-side process (OEP, passport, PCC, attestation, PDO, BMET clearance, insurance, PKB, WEWB, death and injury, coming home, baggage rules), because it is the model draft and its Bangladesh-side facts are the most complete. Saudi Arabia supplied the Wafid medical, the SVP skill test, women domestic workers and most myths.
- One fact whose status was "verified" in Qatar (B0140, dated 2025-11-11) became possibly-outdated here because it is now over 12 months old.
- One imported fact did not support the sentence it was cited for in the country doc (Saudi B0132, "Without this, workers become undocumented", cited in the Saudi doc for "no bank, money transfer or SIM, and detention and deportation if stopped"). Here the sentence is limited to what the source says, and a new fact (F0366) from the same TBS article was added for detention and deportation. The Saudi doc should be checked for the bank and SIM part.

## New sources found for this part

- Bonik Barta, Sep 2026 (`bb-offload-81500`): Special Branch figures on passengers turned back at Bangladesh's airports (81,500 from 2021 to June 2026; 15,516 in 2025; 7,819 in January-June 2026), the reasons, cases, the Home Ministry's admission that some bribe and unfair-offload complaints are true, and the State Minister saying BMET can verify visas for only four or five countries and some BMET officials clear people on fake papers. The Malaysia doc already cites the same article (O0031) for the reasons.
- Daily Star Bangla, 23 Aug 2026 (`dsb-immigration-hotline`): the Special Branch's 24-hour immigration hotline at Shahjalal airport, 01320007588, from 19 August 2026, and what people ask it.
- Samakal, 7 Jun 2023 (`samakal-high-interest-loans`): a former expatriates' welfare secretary on high-interest migration loans. Old; used only for one sentence.
- Bhorer Kagoj, 12 Aug 2023 (`bk-bmet-online-clearance`): BMET clearance online through the Ami Probashi app since 24 July 2023. Old; no newer source found that describes the online clearance route.

## Searches that found nothing usable

- No official FAQ page on bmet.gov.bd, wewb.gov.bd or probashi.gov.bd turned up (searched "FAQ", "প্রশ্ন ও উত্তর", "সাধারণ জিজ্ঞাসা" on those sites). WEWB posts Q&A-style notices on its Facebook page (WEWB1990), for example on clearance and the job-loss insurance (October 2026), but Firecrawl cannot read Facebook. Ask a teammate to save these posts in a browser.
- Bangla Facebook groups and YouTube explainers on offloading and the BMET card came up in searches but are not citable; they were used only to choose and phrase questions (offloading, "BMET card", visit visa to work, free visa, smart card check).
- A Bangla Tribune piece on BMET replacing the smart card with a QR "smart certificate" turned out to be from December 2021 and was dropped.

## Pages we could not download

- WEWB Facebook posts (Oct 2026) on BMET clearance and the job-loss insurance: https://www.facebook.com/WEWB1990/ (Firecrawl: site not supported).

## Gaps and open questions (also in the doc's Need to know blocks)

- Whether the Ministry has issued the new country-by-country migration-cost caps promised in October 2026; the caps given are 2016-2019 figures.
- Whether BMET still issues permission letters after it stopped posting them on 10 December 2025.
- A public list of registered sub-agents; a single current list of agencies approved to send women domestic workers.
- PCC fee: Tk 1,500 (portal) or Tk 500 (police guidance).
- Customs: USD 10,000 (Bangladesh Bank circular) or USD 5,000 (Customs page) before declaring foreign currency.
- Not yet covered with a source: what a worker who is offloaded should do next (whether the ticket is refunded, whether the visa is lost, any appeal). The departure-bottlenecks part may cover this.
- The PDO fee: BMET's charter says the institute sets it; the Ami Probashi app charges Tk 100 plus Tk 100.

## Conflicts noted

- Kuwait's migration cap (Tk 1,06,780) is a "conflict" fact in the Kuwait folder: the Embassy's figure; kept as the reported figure.
- The welfare fee (Tk 5,500 from 1 October 2026) is a "conflict" fact in the Qatar folder because BMET's charter still prints Tk 3,500; the Ministry's order raising it is the newer source.
- The Ministry's 4 November 2026 list of 12 countries: Prothom Alo English lists Cambodia, Bangla Tribune lists Croatia instead (see the Cambodia folder's B0069 note).

## Fact-check report

About 330 cited sentences and list items were checked against the facts' quotes, and against the saved sources wherever a sentence said more than the quote. Every number, phone number and cross-doc pointer was checked again. No new facts were needed: every fix was a rewording or used a fact already in `facts.csv`, so no VF ids were added. The build (`build.py`) finishes without citation errors.

### Changes (before → after, reason, facts)

1. **Saudi status:** "departures in 2026 were 45% below 2025" → "departures from January to 17 October 2026 were 45% below the same period of 2025". The source compares the same period, not whole years. F0015, and F0016 added for "largest destination".
2. **Kuwait status:** "closed to new Bangladeshi domestic workers" now gives the reason: the June 2026 list of approved countries leaves out Bangladesh, and the Embassy attests no women's domestic-worker visas. F0197 added.
3. **Jordan status:** "domestic work" → "women in domestic work". The Ministry of Labour (MOL) guide allows recruiting women for domestic work and men only under their own conditions. F0175.
4. **12-country list:** removed F0188 from the list sentence, because it names Kosovo, not Congo. Added a **Need to know** on Congo or Kosovo, and Cambodia or Croatia. The sources conflict: F0187 (Prothom Alo English), F0188 (Daily Star), and Bangla Tribune in the note.
5. **Women, "Qatar and the UAE: domestic work"** → Qatar only, citing BMET's August 2025 permission for 100 women housemaids (F0233, F0195). The UAE doc says its domestic-worker route is "not confirmed open", so the UAE claim was unsupported. Added a **Need to know** for the UAE.
6. **"Domestic work needs no skill test"** (in two places) → "Saudi Arabia's skill certificate is not required of domestic workers". The source covers Saudi Arabia only. F0204.
7. **Jordan pay:** "JD 100 counts as food and a dormitory bed" → "paid in kind as housing and food". Matches the source's words. F0229.
8. **Maldives pay:** "average pay was MVR 6,760" → "migrant workers surveyed in 2024 averaged MVR 6,760". The figure comes from a survey. F0230.
9. **Repayment arithmetic:** "SR 800 who buys his own food and phone keeps at most SR 250 (Tk 8,250); about 55 months" dropped the source's assumption of free housing and used Tk 33 to the riyal. Now it says "with free housing", gives the cost floors (food SR 500, phone SR 50), and uses the source's rate of Tk 33.20 (SR 250 = Tk 8,300, so 4.5 lakh ÷ 8,300 is about 54 months, before interest). The Tk 15,000-20,000 figure is now stated as what many workers struggle to send, as the source says. F0223, F0037, F0039.
10. **BOESL DHL:** added "for skilled men". The circular is for male workers only. F0043.
11. **Permission letters:** "BMET posted these letters… until it stopped on 10 December 2025" → "the newest one there is dated 10 December 2025". The source shows the newest posted letter, not a decision to stop. The Need to know was reworded to match. F0236.
12. **Paying the agency:** a rule from one letter had been stated for all letters. Now it reads "BMET's September 2025 permission letter for Saudi kitchen workers, for example, let the agency…". F0208.
13. **Bonanza pilot:** "2018-21 ILO and Qatar labour ministry pilot" → "a fair-recruitment pilot the ILO began in 2018 with QDVC, a construction company in Qatar". The source names QDVC, not the ministry, and gives no end year. F0245.
14. **Attestation:** "then that country's embassy" had no support in F0083-F0085, so it was cut. The pointer to Qatar Step 2, item 3 now says that step includes legalisation by the Qatari mission. SSC and HSC are now expanded correctly as "Secondary School Certificate" and "Higher Secondary Certificate".
15. **Wafid:** "booked online through the Gulf Health Council" → "booked online, at a medical centre assigned by your city". The cited quote doesn't name the Council. F0253.
16. **Medical "fit" packages:** the allegations are now attributed and dated: "The Daily Star reported in July 2025…", "allegedly controlled…". F0260-F0263.
17. **Clearance bribes:** "No: the only charges are the fees listed above" was our own conclusion. Now: "BMET's charter lists only the fees above, and BMET asks anyone offered clearance for money to tell the nearest law-enforcement office". F0222, F0098.
18. **Pointer:** "Qatar doc, Work visa: company worker, Welfare Board sign-up…" → added "Step 7", because that H4 sits under Step 7.
19. **Borrowing:** "81% of men borrow" → "In a 2020 government survey, 81% of men had borrowed". F0123 is the 2020 BBS (Bangladesh Bureau of Statistics) survey.
20. **Malaysia permit loans:** "Workers in Malaysia borrow at 10% a month" → "Many workers…, a CPD economist said in October 2025". The claim is attributed, and CPD is explained. F0267.
21. **Oman offload case:** the draft said she was stopped "because Oman's… domestic visas are closed". The source says she was stopped because the same spouse-visa approval had been used to send five women. The route closed is "women's domestic-worker recruitment". F0008.
22. **Pointer:** "Qatar doc, …, If something goes wrong" → added the exact H4, "If you aren't paid, are abused or your passport is taken".
23. **Qatar passport:** added the dropped condition "unless you ask in writing for the employer to keep it". F0281.
24. **Saudi transfer:** "your iqama expires" → "your work permit or visa expires", the source's wording. F0279.
25. **"Illegal in the Gulf"** generalised from one Saudi rule. Now it reads "In Saudi Arabia you may not be employed in a profession other than the one on your work permit", here and in the free-visa myth. F0298.
26. **No job on arrival:** "Contact the embassy's labour wing" rested only on the Qatar embassy's 2021 page. Now: "The embassy can advise and help in a labour dispute (in Qatar, for example)". F0302.
27. **UAE overstay:** added the condition that the AED 50 a day applies after the grace period following the end of a residence permit. F0129.
28. **Housekeeping certificates:** cut "don't buy one" (our own advice). F0312.
29. **Age change:** "If an agent offers to change your age, call 16135" was not in the source. Now it states what the call centre does. F0320.
30. **Pointer:** "Work visa: domestic worker, Your rights at work, in [each] doc" is not true of every doc (Kuwait and the Maldives differ). Now: "each country doc's domestic-worker section (for example, see the Qatar doc, Work visa: domestic worker, Your rights at work)".
31. **Saudi abuse:** "go to the embassy or consulate, which runs safe homes" (advice, and the wrong body) → "the labour wings run safe homes for women in Riyadh, Jeddah and Madinah". F0150.
32. **Jordan garment scam:** "Fake 'garment visas' are sold in real factories' names" generalised from one case. Now it states the June 2026 CID case. The pointer "Steps: the Jordan doc" now names the section: "Work visa: garment and factory worker". F0323.
33. **Death, airport cheque:** "free and at once" → "free, collected within 3 months of the body's arrival". The deadline had been dropped. F0328.
34. **Natural-cause deaths:** "Most deaths" (a general rule) → "Many deaths… in Qatar". The compensation point is now attributed to Amnesty, 2021. F0337, F0338.
35. **Gold jewellery:** added the dropped limit of 100 g of gold or 200 g of silver in total. F0352.
36. **"Agency guarantees the job" myth:** "A 2019 study found the contract… often differs" was one worker's quote presented as a finding. It is now attributed to the worker. F0165.
37. **UAE visa cancellations:** "Since July 2026 the UAE has cancelled about 5,000 Bangladeshis' visas" → the cancellations began in July 2026, and on 13 October 2026 the Law Minister said 5,000 had been cancelled. F0170, F0171.

### Checked and correct (no change)

- Phone numbers, against the saved sources: 01320007588 (Special Branch hotline), 01320001824/25 (PCC helpdesk), 26969 (PCC SMS), 09614445271 (OEP), 01711-135901 (Director, Emigration), 16238 (PKB), 16135 and +8809610102030 (Probash-Bondhu), 8001000125 (Saudi labour wing), 1919 (Saudi abuse line), 01842773300 (OKUP).
- Fees and caps: passport Tk 4,025/6,325/8,625; OEP Tk 200; welfare fee Tk 5,500 from 1 October 2026; insurance Tk 1,000; smart card Tk 250; source tax Tk 250-1,200 (Tk 500 on a Saudi single visa); caps Tk 1,65,000, 2,62,270, 1,07,780, 1,06,780 and 78,990. S$9,000-13,000 is Tk 8.7-12.6 lakh at Tk 96.6 to the Singapore dollar.
- Penalties: s.31 (up to 5 years and a fine of at least Tk 1 lakh), s.32 (up to 1 year), s.33 (2-7 years), s.33A (1-2 years), s.35 (1 year, or Tk 50,000-2 lakh for the sub-agent, Tk 1-5 lakh for the agency).
- All other country-doc pointers resolve to real headings, including Saudi Steps 3, 4 and 7, "Who pays what", Domestic worker Step 2; Qatar Step 1 items 4 and 5, Step 2 item 3, Step 4, Step 6 item 3, "Scams, If the agency cheats you", "If a worker dies, is injured or loses the job", "Coming home, What you can bring home" and "Background, Status"; and Italy "Work visa: Decreto Flussi worker (non-seasonal), Step 4". "Is it open now, and who can go?", "If you aren't paid", "Going home without valid papers", "Sending money home" and "Contacts" exist in all 12 country docs. The Recruiting agencies doc exists (`agencies/doc.md`).

### Issues not fixed

- The caps listed under "What is the most an agency may charge me?" come from different years (2016 Saudi, 2017 UAE, a 2019 Bangladesh Bank table for Singapore, a 2025 Embassy figure for Kuwait that conflicts with the 2017 table's Tk 1,03,780). The existing Need to know on new caps covers this, but the list doesn't show the years.
- Many Bangladesh-side rules rest on undated pages ("possibly-outdated"): the PKB loan page, OEP pages, the bdlaws Act text and the BMET leaflet. These were kept because no newer source exists.
- Several pointers say "in each country doc" (for example "If you aren't paid"). The headings exist, but the build can't link a pointer that names no doc.
- `facts.csv` row F0107 has an empty quote column; its text sits in the note. It isn't load-bearing, because F0222 carries the same figures.

## Resolved conflicts

- PKB guarantors (23 Nov 2026): PKB's own migration-loan page says at least two guarantors, one financially solvent (with three signed cheques) and one family member or close relative [F0116]; a July 2024 Prothom Alo report agrees (see global/services/notes.md, GV0009). The July 2025 Prothom Alo guide's "one guarantor's papers" [OA0108, OA0109] and the Cumilla PKB officer's "a capable guarantor" [AA0237] are secondhand summaries that name only the guarantor who carries the repayment risk. PKB's page wins; the doc no longer cites OA0108/OA0109 or AA0237 for the number of guarantors, and the Need to know was removed.
- Workers who went abroad in 2023 (23 Nov 2026): the State Minister's written answer to parliament on 27 February 2024 gives 13,05,453 [GF0005], the same figure RMMRU gives [MA0079]; BMET's "about 13 lakh" [CQ0055] is a rounding of it. The Ami Probashi 2024 report's 13,90,811 [CQ0070] is a secondhand figure from a private app operator and is outnumbered by the official one; the doc no longer cites it for 2023 (it still cites the report for 2024). The Need to know was removed.

## Prothom Alo archive pass (gchunk-faq-1, prefix GF)

- New: State Minister's parliamentary figures (1976 to March 2024 total; 2022 and 2023 totals and 2023 by country; FY2023-24 as of 8 May 2024; 1,27,557 sent through government at low or no cost FY2009-10 to FY2022-23); 60 lakh five-year plan (Feb 2024); British Council youth survey (55% want to go abroad); January 2025 editorial on the job market; Salma Begum debt case (Munshiganj, Feb 2024); 2024 passport indexes; study-abroad requirements and traps (new question "Can I go abroad to study instead?").
- Not used: opinion pieces and readers' essays with no checkable facts; a reader's letter giving FY2023-24 remittance as USD 2,542 million, an obvious misprint; the arrest of the former minister Imran Ahmad (no bearing on a migrant's decisions).

