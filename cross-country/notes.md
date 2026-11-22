# Going abroad from Bangladesh: research notes

Research notes behind `doc.md`, one section per part. Each part was researched separately (its own facts and sources), fact-checked by an independent verifier, then merged here; the fact ids keep each part's prefix.

## How the doc was put together

- Four parts, researched in parallel in separate work folders so their facts files never clashed, then merged: facts.csv and sources.csv combined (no id or name clashes); where two parts had saved different captures of the same page under one name, both captures are kept in the text copy so every quote still matches.
- Bangladesh's trafficking law: the Prevention and Suppression of Human Trafficking Act 2012 was repealed by the Prevention and Suppression of Human Trafficking and Migrant Smuggling Act 2026 (Act 55 of 2026). The fact-check rewrote every legal reference from the official text on bdlaws; press summaries had it wrong in places.
- Lower-confidence facts: about 98 quotes were typed from scanned Bangla PDFs (BMET and Ministry charters, the safe migration leaflet, WEWB's annual report) and can't be matched to a text layer; most were first transcribed for the country docs.
- Open conflicts kept as Need to know: the 12 countries in the Ministry's order of 4 November 2026 (press lists differ; no official copy found); BMET's Cambodia and Russia clearance counts; the Gulf medical fee; the migration-cost caps date from 2016 to 2025 and new ones are promised.
- A problem found in another doc: the Saudi Arabia doc cites fact B0132 for "no bank, money transfer or SIM", which its source does not say.

## Frequently asked questions (prefix F; fact-check VF)

### How this part was built

- 84 questions (H4) in 10 stage groups (H3), under one H2, "Frequently asked questions".
- Most answers reuse facts already researched and cited in the country docs. Each reused fact was copied into this folder's `facts.csv` under prefix F (F0015 to F0364), with its source file, `_fetchlog.csv`, `_wayback.csv` and `sources.csv` rows. The fact's `note` column says which country and id it came from ("imported from qatar B0049"). Facts that the country folder logged with `--no-quote-check` (garbled Bangla PDF text, quote transcribed from the page image) were imported the same way and keep the original note.
- The Qatar doc was the main source for the Bangladesh-side process (OEP, passport, PCC, attestation, PDO, BMET clearance, insurance, PKB, WEWB, death and injury, coming home, baggage rules), because it is the model draft and its Bangladesh-side facts are the most complete. Saudi Arabia supplied the Wafid medical, the SVP skill test, women domestic workers and most myths.
- One fact whose status was "verified" in Qatar (B0140, dated 2025-11-11) became possibly-outdated here because it is now over 12 months old.
- One imported fact did not support the sentence it was cited for in the country doc (Saudi B0132, "Without this, workers become undocumented", cited in the Saudi doc for "no bank, money transfer or SIM, and detention and deportation if stopped"). Here the sentence is limited to what the source says, and a new fact (F0366) from the same TBS article was added for detention and deportation. The Saudi doc should be checked for the bank and SIM part.

### New sources found for this part

- Bonik Barta, Sep 2026 (`bb-offload-81500`): Special Branch figures on passengers turned back at Bangladesh's airports (81,500 from 2021 to June 2026; 15,516 in 2025; 7,819 in January-June 2026), the reasons, cases, the Home Ministry's admission that some bribe and unfair-offload complaints are true, and the State Minister saying BMET can verify visas for only four or five countries and some BMET officials clear people on fake papers. The Malaysia doc already cites the same article (O0031) for the reasons.
- Daily Star Bangla, 23 Aug 2026 (`dsb-immigration-hotline`): the Special Branch's 24-hour immigration hotline at Shahjalal airport, 01320007588, from 19 August 2026, and what people ask it.
- Samakal, 7 Jun 2023 (`samakal-high-interest-loans`): a former expatriates' welfare secretary on high-interest migration loans. Old; used only for one sentence.
- Bhorer Kagoj, 12 Aug 2023 (`bk-bmet-online-clearance`): BMET clearance online through the Ami Probashi app since 24 July 2023. Old; no newer source found that describes the online clearance route.

### Searches that found nothing usable

- No official FAQ page on bmet.gov.bd, wewb.gov.bd or probashi.gov.bd turned up (searched "FAQ", "প্রশ্ন ও উত্তর", "সাধারণ জিজ্ঞাসা" on those sites). WEWB posts Q&A-style notices on its Facebook page (WEWB1990), for example on clearance and the job-loss insurance (October 2026), but Firecrawl cannot read Facebook. Ask a teammate to save these posts in a browser.
- Bangla Facebook groups and YouTube explainers on offloading and the BMET card came up in searches but are not citable; they were used only to choose and phrase questions (offloading, "BMET card", visit visa to work, free visa, smart card check).
- A Bangla Tribune piece on BMET replacing the smart card with a QR "smart certificate" turned out to be from December 2021 and was dropped.

### Pages we could not download

- WEWB Facebook posts (Oct 2026) on BMET clearance and the job-loss insurance: https://www.facebook.com/WEWB1990/ (Firecrawl: site not supported).

### Gaps and open questions (also in the doc's Need to know blocks)

- Whether the Ministry has issued the new country-by-country migration-cost caps promised in October 2026; the caps given are 2016-2019 figures.
- Whether BMET still issues permission letters after it stopped posting them on 10 December 2025.
- A public list of registered sub-agents; a single current list of agencies approved to send women domestic workers.
- PCC fee: Tk 1,500 (portal) or Tk 500 (police guidance).
- Customs: USD 10,000 (Bangladesh Bank circular) or USD 5,000 (Customs page) before declaring foreign currency.
- Not yet covered with a source: what a worker who is offloaded should do next (whether the ticket is refunded, whether the visa is lost, any appeal). The departure-bottlenecks part may cover this.
- The PDO fee: BMET's charter says the institute sets it; the Ami Probashi app charges Tk 100 plus Tk 100.

### Conflicts noted

- Kuwait's migration cap (Tk 1,06,780) is a "conflict" fact in the Kuwait folder: the Embassy's figure; kept as the reported figure.
- The welfare fee (Tk 5,500 from 1 October 2026) is a "conflict" fact in the Qatar folder because BMET's charter still prints Tk 3,500; the Ministry's order raising it is the newer source.
- The Ministry's 4 November 2026 list of 12 countries: Prothom Alo English lists Cambodia, Bangla Tribune lists Croatia instead (see the Cambodia folder's B0069 note).

### Fact-check report

About 330 cited sentences and list items were checked against the facts' quotes, and against the saved sources wherever a sentence said more than the quote. Every number, phone number and cross-doc pointer was checked again. No new facts were needed: every fix was a rewording or used a fact already in `facts.csv`, so no VF ids were added. The build (`build.py`) finishes without citation errors.

#### Changes (before → after, reason, facts)

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

#### Checked and correct (no change)

- Phone numbers, against the saved sources: 01320007588 (Special Branch hotline), 01320001824/25 (PCC helpdesk), 26969 (PCC SMS), 09614445271 (OEP), 01711-135901 (Director, Emigration), 16238 (PKB), 16135 and +8809610102030 (Probash-Bondhu), 8001000125 (Saudi labour wing), 1919 (Saudi abuse line), 01842773300 (OKUP).
- Fees and caps: passport Tk 4,025/6,325/8,625; OEP Tk 200; welfare fee Tk 5,500 from 1 October 2026; insurance Tk 1,000; smart card Tk 250; source tax Tk 250-1,200 (Tk 500 on a Saudi single visa); caps Tk 1,65,000, 2,62,270, 1,07,780, 1,06,780 and 78,990. S$9,000-13,000 is Tk 8.7-12.6 lakh at Tk 96.6 to the Singapore dollar.
- Penalties: s.31 (up to 5 years and a fine of at least Tk 1 lakh), s.32 (up to 1 year), s.33 (2-7 years), s.33A (1-2 years), s.35 (1 year, or Tk 50,000-2 lakh for the sub-agent, Tk 1-5 lakh for the agency).
- All other country-doc pointers resolve to real headings, including Saudi Steps 3, 4 and 7, "Who pays what", Domestic worker Step 2; Qatar Step 1 items 4 and 5, Step 2 item 3, Step 4, Step 6 item 3, "Scams, If the agency cheats you", "If a worker dies, is injured or loses the job", "Coming home, What you can bring home" and "Background, Status"; and Italy "Work visa: Decreto Flussi worker (non-seasonal), Step 4". "Is it open now, and who can go?", "If you aren't paid", "Going home without valid papers", "Sending money home" and "Contacts" exist in all 12 country docs. The Recruiting agencies doc exists (`agencies/doc.md`).

#### Issues not fixed

- The caps listed under "What is the most an agency may charge me?" come from different years (2016 Saudi, 2017 UAE, a 2019 Bangladesh Bank table for Singapore, a 2025 Embassy figure for Kuwait that conflicts with the 2017 table's Tk 1,03,780). The existing Need to know on new caps covers this, but the list doesn't show the years.
- Many Bangladesh-side rules rest on undated pages ("possibly-outdated"): the PKB loan page, OEP pages, the bdlaws Act text and the BMET leaflet. These were kept because no newer source exists.
- Several pointers say "in each country doc" (for example "If you aren't paid"). The headings exist, but the build can't link a pointer that names no doc.
- `facts.csv` row F0107 has an empty quote column; its text sits in the note. It isn't load-bearing, because F0222 carries the same figures.

## Dalal scams (prefix S; fact-check VS)

### How this part was built

- About 120 facts were re-logged from the country folders (Saudi Arabia, Malaysia, Jordan, Cambodia, Kuwait, Qatar, Italy, Kyrgyzstan, Singapore, UAE, Maldives, Oman, agencies) with a helper that copies the source files, fetch-log, wayback and sources.csv rows and re-runs `facts.py add` under prefix S (note column says "from <country> <id>"). Status was recomputed against the 2025-11-19 cutoff.
- About 95 facts are new, from: the consolidated OEM Act 2013 text on bdlaws (copied from the Jordan folder; sections 27, 28, 31-41, including the 2026 amendment's s.35A and revised s.39/40); the Prevention and Suppression of Human Trafficking Act 2012 (bdlaws, act-details-1086); and Bangla/English news (Finance Today, Balkan Insight, The Shift, Daily Star Bangla, Gramer Kagoj, Prothom Alo, Bangla Tribune, TBS, Protidiner Bangladesh, Samakal, Bangla Telegraph, Bangladesh Pratidin, Radio Today/Samakal).
- Country-doc cross-references are written as "(<Country> doc: <H2>, <H3>)" with exact heading text, so the lead can turn them into links after the merge.

### Conflicts and cautions

- The Ministry's 4 Nov 2026 list of 12 countries needing approval (S0127) is logged as a conflict in the Cambodia/Kyrgyzstan folders: Bangla Tribune lists Croatia instead of Cambodia. The doc uses the Cambodia folder's list; check the letter itself.
- Radio Today's Dubai dance-club story (S0189-S0191) is a reproduction of a Samakal report; the page shows 20 May 2026, and the woman's travel date (13 April 2023, "three years ago") is consistent with that, but the original Samakal date was not seen.
- The OKUP survey figures (72% borrowed, 11% mortgaged land, 6% sold assets; five times the official cost) come from an opinion piece in Bangla Telegraph (S0178), not OKUP's report itself.
- S0045 (OEP online complaint module from 30 July 2026) is news-sourced in the Saudi folder; an official notice would be better.
- BBS SEDS 2023: the 42.09% (agencies) and 3.09% (government) shares exist in the Qatar folder (A0002) but were not imported; only the 52.03% broker share is cited.

### Searched, not found (open questions)

- A public list of BMET-registered sub-agents (rule 17(4) of the 2025 rules says BMET or the DEMO publishes it); not found on bmet.gov.bd.
- Dalal's cut per worker on a typical Saudi or Malaysia visa in 2026.
- Fake nikahnama use for Gulf or Italian family visas: only China marriage-trafficking cases found.
- Money mules: no Bangladeshi case found of migrants lending bank/MFS accounts; only digital-hundi arrests of MFS agents.
- Croatia's reported suspension of work visas for Bangladeshis (early 2025): found only on blogs and social media, no official or mainstream source saved.
- Prices for Serbia, Croatia or Malta work permits in Dhaka.
- Village moneylender interest rates.
- A direct CID/police anti-trafficking complaint number for families.

### Pages we could not download

- dhakastream.net report on 56 agencies revoked (403); replaced by Bangladesh Pratidin, 15 Nov 2026.
- jagonews24.com/national/news/1166537 (Bangladesh-Libya trafficking ring) (403).
- jagonews OKUP "18% borrow at high interest" page saved with an empty .md; deleted, not used.

### Fact-check report

Checked 19 Nov 2026. About 190 cited sentences and list items checked against the quotes, and against the saved source wherever the sentence said more than the quote. Scanned PDFs (BMET skill-test notice, Takamol poster, BOESL warning, sub-agent rules p.18, BMET charter pp.2 and 17) were read from page images.

New source: `bdlaws-hmspsa-2026-full` (Prevention and Suppression of Human Trafficking and Migrant Smuggling Act 2026, Act 55 of 2026, bdlaws act-1684, dated 10 Apr 2026). New facts: VS0001-VS0052. Build passes.

#### Changes

#### Law

1. **Trafficking law out of date (most serious).** The bdlaws page saved for the 2012 act says it was repealed by the Prevention and Suppression of Human Trafficking and Migrant Smuggling Act 2026 (Act 55 of 2026). The doc cited the 2012 act (PSHTA) as current in five places.
   - File a trafficking case: rewrote all bullets on the 2026 Act: definition s.5 [VS0002, VS0003]; exploitation now covers fraudulent marriage, forced online scamming and ransom [VS0004-VS0006]; penalties ss.6-7 (unchanged: 5 years to life, Tk 50,000; organised group death/life/7 years, Tk 5 lakh) [VS0007, VS0008]; new migrant-smuggling penalty s.15, 3-10 years, Tk 1 lakh [VS0044]; complaint to police or Tribunal s.28 [VS0009]; tribunals s.36(2) [VS0010]; compensation s.46 [VS0011]; repeal [VS0001, VS0014]. Was [S0034-S0040, S0042].
   - Sue for compensation: "PSHTA section 39" → "section 56 of the 2026 trafficking act" [VS0012]. Was [S0041].
   - In one minute: trafficking penalty [S0037] → [VS0007]; marriage scam [S0036] → [VS0004]. Marriage "What to do" [S0036] → [VS0004, VS0014]. Visit visa "What to do" [S0035] → [VS0003]. Trafficking-as-job "What to do" [S0034] → [VS0002]. "Your visa is stuck" What to do: added that ransom counts as exploitation [VS0006].
2. **OEM Act sections checked against the consolidated bdlaws text** (which includes the 2023 amendment, Act 41 of 2023, and the 2026 amendment, Act 42 of 2026, which added s.35A). Sections 31, 32, 33, 34, 35, 38, 39, 40 and 41 match. Fixes:
   - Section 33: before "buying or selling a visa inside Bangladesh is itself an offence ... 2 to 7 years ... Tk 3 lakh, so a seller may threaten to name the buyer" [S0054] → the offence is illegal means to obtain a demand letter/visa/work permit *and* buying or selling it in Bangladesh; penalty logged [VS0042]; "seller may threaten" cut (no source). Added a s.33 bullet under File a police case.
   - Section 32: "any overseas job advert" → "an overseas job advert without government or BMET approval", with penalty (1 year, Tk 50,000) [VS0043].
   - Section 41(3): "within 3 months" now has its own fact [VS0041].
   - "The OEM Act" now defined at first use (sub-agent section).
3. **2025 sub-agent rules.** Read gazette p.18 from the page image: Tk 3 lakh security by pay order, refunded at contract end, compensation from it if irregularity proved, DG may suspend/cancel after inquiry and hearing. All confirmed. Added "after an inquiry and hearing" and "well-wisher" to S0099's sentence; named the 2025 rules. Heading "The 2023 law: registered sub-agents" → "The law on sub-agents" (no dates in headings). The 2026 amendment SRO (02-Law/2026) did not change these rules per the Malaysia folder's TRW source.

#### Wrong citations

4. S0021 (Gramer Kagoj, China marriages) was cited for the Dream Visa raid and fake Fiji demand letters → S0022 plus new VS0023, VS0024 (Prothom Alo 2020).
5. S0142 (Italian report) quote was about a relative, not the passport → VS0029, VS0030 (passport kept until last instalment; EUR 18,000).
6. S0014 cited for "forced into sex work or labour" (quote is about the groom's religion) → VS0020; "or labour" cut.
7. S0108 quote didn't support the security-deposit claim → VS0040, attributed to the 2026 RMMRU study.
8. S0209 cited for "Wafid booking needs only the passport details" → reworded to the slip printed with passport number and nationality [VS0031].
9. S0212 (membership text) → VS0035 (the WEWB clearance-check link).
10. S0086 cited for "PKB grievance officers"; that sentence cut, cross-reference folded into the bribe item.
11. S0102 cited for the email address → VS0034.

#### Figures

12. **North Macedonia / Serbia.** Before: "Oct 2025: Serbia and North Macedonia stopped issuing work permits ... about 90% ... fake". The source (Financial Today, 28 Oct 2025) attributes 90% to "diplomatic sources", says "the same situation exists in Serbia", and that no permits had been issued "for the past two months". Rewritten with attribution and that timeframe [S0001, S0002]. Item 1 of How it works listed Croatia, Poland, Malta and "far more than the official route" on a Romania-only source → "Serbia, North Macedonia or Romania" [S0001, S0148].
13. **Q-1 visas.** 4,226 (2020-2025), 35 (2022), 1,721 (2025) confirmed; also 1,016 (2023) and 1,378 (2024); arithmetic consistent (4,150 for 2022-25). The source stresses this is not a trafficking count and gives it as data from an anti-trafficking-law workshop. Moved out of "Cases" into a sentence with that caveat [S0019, VS0015-VS0017]. "Arrangers are said to get Tk 10-20 lakh" (anonymous Uttara resident, 2024) → "middlemen allegedly dealt in up to Tk 10-20 lakh" [VS0018, S0017].
14. **Kuwait visa.** "Costs the sponsor 6 KWD" was misleading: KWD 6 is processing plus attestation fees; the employer also spends about KWD 250 on the work permit [VS0025, VS0026]. Press Club claim attributed to its joint general secretary, July 2025.
15. **Gulf medical fee conflict.** Daily Star (Jul 2025) says total should not exceed Tk 8,500-9,000; TBS (Sep 2025) says the set fee is about Tk 10,000. Red flag now "well above about Tk 8,500-10,000" [S0210, VS0033, status conflict], plus a Need to know.
16. **Skill test.** Added the USD 50 fee and SVP expansion from the notice and poster images [VS0050, VS0051]; dropped unsupported "listed trades".
17. Trafficking cases: "122 in 2025, up from 86 in 2023" (cherry-picked) → full series 114/86/100/122 [S0191].
18. Malta EUR 600 and EUR 925 now have their own facts [VS0045, VS0046].

#### Dates and attribution of cases

19. Every case dated to the event, with "reported" where only the article date is known: Dream Visa 15 Sept 2020; Saudi pharmacy case Oct 2022 (reported Sept 2024, was "2024"); Romania case July 2024 (reported Feb 2026, three places, was "Feb 2026"); Italy loans early 2023 (reported June 2026); Keraniganj woman Apr 2023 to May 2026 (was "2026"); Singapore case Apr-May 2026; Cambodia WhatsApp case 2025; Jhenaidah 2020; Chuadanga case filed 31 Mar 2024 (was "June 2024"); Fatema Overseas 15 Sept 2020.
20. Allegations attributed: shell-company visas (a broker to Bonik Barta, 2024); disappearing Saudi visas (former BAIRA official) and MHRSD cancellations (industry insiders) [VS0028]; Saudi permit-selling (an agent to Bonik Barta, "Gulf" → "Saudi Arabia"); medical bribes ("alleged"); PKB bribes (state minister citing complaints); CID cases ("accused", "allegedly"); Nepal case (according to BRAC). Nepal case corrected: the joint police-CID raid arrested a local broker; the traffickers then released the men near Kathmandu airport [VS0039] (doc said the raid freed them). Jhenaidah case: the Tk 50,000 went to two brokers, not the village recruiter [VS0047, VS0048].
21. "A dalal is often a friend or relative" attributed to an ILO consultant. "Agencies need dalals" (no source) cut; ITUC survey described as Recruitment Advisor reviews. Cambodia agency "licensed" → "manpower agency" (source doesn't say licensed).

#### Overstatements and dropped conditions

22. In one minute: "The money is usually lost: few victims file cases" → CID statement on Cambodia returnees (2026); "The law is on paper strong" (opinion) cut; "most destinations" → "Saudi Arabia, Singapore and other destinations".
23. Free visa: "sold as a visa that lets you work anywhere" → entry permission with no job [VS0027].
24. Contract substitution: red flag "permit in the name of a company never heard of" cut (source doesn't say it); S0074 removed from the visa-title flag; IPA salary now cited to S0151, MOM salary check to S0154.
25. Staged payments: "passport is kept" → "may be kept"; "pay only through its bank account" → "deal with the agency through a bank"; "the bulk asked before the visa is checked" → the permission-letter condition.
26. UAE check: "job offer and work permit" → job offer by reference number (source covers only that). Oman: "ask the employer for the PDF" → status shows only in the sponsor's account.
27. Romania: "a way into Italy" → "to move on to another country"; "Romania or Malta contract" split into two attributed sources; Romania 90-day rule reworded to what the source says.
28. "Call 16699 before going to the police" (our advice) → plain helpline fact.
29. Acronyms explained at first use: MOHRE, MOM, ITUC, SVP, WEWB, NID, RL, RMMRU, JD, MFS; duplicate expansions of ILO and BAIRA removed.

#### Cross-links

All 17 country-doc links checked against `countries/<c>/doc.md`; all named sections exist (Saudi, Malaysia, Qatar, UAE, Singapore, Maldives, Kyrgyzstan, Oman, Kuwait, Cambodia).

#### Issues not fixed

- **Fact VS0005's claim text** also mentions ransom (the quote covers only online scamming); VS0006 is the ransom fact. Harmless but the claim could be trimmed.
- **Gulf medical fee:** conflicting news figures (Tk 8,500-9,000 vs about Tk 10,000); no official 2026 figure found. Left as a Need to know.
- **S0044 (complaint form fields) and S0043/S0046 (charter)** were verified in the Saudi folder; here the form PDF has no text layer. The charter's complaint officer (Director (Employment), 01711111544) was confirmed on p.17's image.
- **S0158 (BMET visa check):** the charter page read here appears to be the Chattogram DEMO's version; the service (demand letter/job visa check, free, 3 working days) matches.
- **S0055:** the Tk 165,000 Saudi cost dates from 2016; no newer official figure checked.
- **Rest of the 2026 trafficking Act** not mined: e.g. s.20 (advertising for migrant smuggling, 3-7 years, logged as VS0013 but not cited) could go in the Online scams section.
- The Need to know items in the doc were not researched further in this pass.

## Departure bottlenecks (prefix D; fact-check VD)

### What was searched
- Bangla and English news on offloading (অফলোড), the three women stopped on the way to Nepal (8 Aug 2026; High Court rule 29 Sep 2026), the "airport contract", deportees, luggage, BMET clearance bribes, Gulf medical (Wafid/GAMCA) rackets, Saudi visa stamping.
- Official: Special Branch immigration site (immi.specialbranch.gov.bd: laws, complaint form, contacts, OFMS), HSIA pages, WEWB airport desk, NHRC complaint procedure, ACC home page, Ministry FB notice on the Malaysia medical fee (31 Oct 2026).
- Research: TIB National Household Survey 2025 (published 25 Jun 2026), TIB labour migration governance 2017, Global Voices (Jan 2026).
- Reused from country folders: BMET citizen charter 2026, welfare fee circular (Tk 5,500 from 1 Oct 2026), PCC pages, e-passport fees, Malaysia KLIA refusals, Kuwait/Malaysia/UAE/Qatar/Italy re-entry bans, Air Arabia OK to Board, Baggage Rules 2025, Saudi Tasheer stamping.

### Conflicts
- Welfare fee: BMET charter (Sep 2026) gives Tk 3,500 (D0003); ministry circular raises it to Tk 5,500 from 1 Oct 2026 (D0007). Doc uses Tk 5,500.
- PCC fee: older police guidance Tk 500 (D0013); SB/RMP notice says re-fixed to Tk 1,500 (D0103). Doc uses Tk 1,500.
- Airport desk numbers differ between WEWB page (D0021-D0023) and BMET charter (D0020): kept as a Need to know.
- Police verification for passports: reported abolished (DW Feb 2025, TIB list of reforms), yet TIB's survey (Nov 2024-Oct 2025) still records passport verification bribes. Need to know.

### Dates
- Daily Star "Migrants trapped in medical scam" has no visible date; logged as 2025 (article id 3936961, cites a 26 June event).
- BBC Bangla US deportee article dated Dec 2025 from its text ("28 November" this year; related links 28 Nov 2025).
- Bonik Barta English (2026) and Bangla (19 Sep 2026) carry the same SB figures.

### Practice findings worth an insider's review
- SB figures: 81,500 turned back 2021 to Jun 2026; 15,516 in 2025; 7,819 in H1 2026.
- Home Ministry additional secretary on record (2026): some complaints of paying police to pass, or being unjustly stopped, are true.
- State minister: BMET can verify visas for only 4-5 countries; some BMET officials clear fake documents.
- TIB 2025: passport the most corrupt service (76.6% paid bribes); SB 66.1% paid.
- Gulf medical: "fit" packages Tk 20,000-50,000 vs Tk 8,500-9,000 official; 260 GHC centres, ~20 get 90% of slips.

### Pages we could not download
- kalbela.com/national/191922 (ACC raid on BMET): 403.
- Biman refund and change policy PDF (biman-airlines.com): 403. Airline refunds for offloaded passengers remain a Need to know.

### Gaps (Need to know in doc)
- Written reason for offloading; what OFMS does; whether an offload stays on record; airline refunds.
- GHC delisting of Bangladeshi centres; appeal of an "unfit" result.
- Fake smart cards caught at the airport; DEMO fees in practice.
- Deportees questioned or held at Dhaka in 2026; SB record of deportation.
- Arrival refusals in Saudi Arabia, UAE and Oman, with numbers.
- Customs complaint channel for returnees.
- Searched but not found: RMMRU or OKUP data specifically on offloading or airport harassment of returnees.

### Logged but not cited
- D0013 (old PCC fee), D0099-D0100 (lead version of official fee notice), D0098, D0109, D0111, D0133, D0040, D0052, D0058, D0062, D0088: duplicates or weaker versions of cited facts.

### Fact-check report

Independent fact-check, 19 November 2026. About 150 sentences and list items checked against their cited facts. Where a sentence went beyond its quote, I checked the saved source (BMET charter pages 2, 7 and 12 were checked from page images). Every number was checked again, and the offloading arithmetic was recomputed: 11,528 + 18,756 + 9,872 + 18,009 + 15,516 + 7,819 = 81,500, which matches.

#### Confirmed as written (special-attention items)

- **Special Branch offloading figures by year (D0028-D0030):** all six yearly figures and both traveller totals match Bonik Barta.
- **High Court rule (D0046, D0047):** 29 September 2026 was a Tuesday, which matches New Age ("on Tuesday"). Bench: Justices KM Kamrul Kader and Fatema Anwar. The rule asks why stopping the women should not be declared illegal or without lawful authority. It directs the Additional IGP (immigration) to investigate and dispose of the complaint within seven days and report to the court. It tells immigration not to obstruct the petitioners' future travel, subject to law. It also asks why guidelines should not be issued.
- **TIB National Household Survey 2025 (D0134-D0145):** published 25 June 2026. Reference period November 2024 to October 2025; fieldwork 12 November to 20 December 2025. These figures all match the executive summary: 84.4, 76.6, 4,532, 39.7, 76.8, 6,680, 12,444, 93.3, 91.7, 80.7, 77.5, 66.1 and 1,279.
- **Wafid medical:** USD 10 token and Tk 8,500-9,000 (Daily Star). Result within 26 days (Wafid FAQ). Certificate valid two months (GHC regulations). Qatar fee at least USD 137 with two centres. Malaysia fee Tk 8,000 (ministry, 31 October 2026). All match.
- **Contacts:** welfare desks (WEWB page), SB numbers (contact and complaint pages), BMET Director (Emigration) and ADG, NHRC and ACC all match their saved sources. The charter's Chattogram 01913631797 and Sylhet 01558277904 were confirmed from the page-12 image.

#### Changes (before → after; reason; fact ids)

1. **In one minute: "a Gulf-approved medical centre"** → "an approved medical centre (for the Gulf, one approved by the Gulf Health Council)". The sentence covers every destination. [D0160]
2. **In one minute: "surveys and court cases show … in 2024-25 paid a bribe, medical centres declare workers 'unfit' and then sell a 'fit' report, and BMET officials have been sued"** → "surveys, news reports and an anti-corruption case … November 2024 to October 2025 paid a bribe or unauthorised money; centres have been reported to threaten 'unfit' and sell guaranteed 'fit' reports; in July 2025 the ACC filed a case against BMET officials it accuses of …". No court case is cited, and the allegations are now attributed and dated. [D0134 added, D0135, D0147, D0157, D0154]
3. **In one minute: "mostly over mismatched visas …"** → "often over …". Bonik Barta says "often". [D0031]
4. **In one minute: "three young women … in August 2026 who were asked … the High Court has asked … why that was not illegal"** → "three adult women … on 8 August 2026 who, their lawyer says, were asked … on 29 September 2026 the High Court asked … why stopping them should not be declared illegal". "Young" is unsupported, and the questioning is the lawyer's account. [D0041 added, D0042, D0046]
5. **In one minute: "but may face the police, and most destinations bar them"** → "though in 2020 some deportees were jailed on arrival, and destinations such as Kuwait and Malaysia bar deportees". The old text generalised from one 2020 case and five countries. [D0188, D0122, D0119]
6. **Police verification: "Before that, TIB had found three in four …"** → "In a 2017 study, TIB had found …". The figure comes from TIB's 21 August 2017 passport study, not a recent one. [D0104, new VD0001, D0105]
7. **"In the 2025 survey, passport verification was still …"** → "In the 2025 survey (November 2024 to October 2025), passport verification was …". "Still" was an inference. [D0141]
8. **PCC: "which most work visas need"** cut. No cited source says this.
9. **PCC and BMET bribes: "In 2016 TIB found … per worker"** → "TIB's 2017 study found … per visa". TIB published in 2017, and its table is per visa (2016 volumes). [D0106, D0151]
10. **Training certificate bullet:** attributed to "TIB reported in 2017". [D0107]
11. **Wafid: "(once called GAMCA, the association of GCC-approved medical centres)" and "or 'slip'"** → "the approved centres were previously known as GAMCA (GCC-approved medical centres, the GCC being the Gulf Cooperation Council)", and "slip" dropped. The Daily Star says the centres, not Wafid, were known as GAMCA, and it doesn't use "slip". GCC is now explained. [D0160]
12. **Chattogram/Panthapath case** → attributed to a worker speaking to TBS (The Business Standard, expanded) in 2025, with "in Dhaka" added. [D0167]
13. **Ministry and GHC sentence** → reordered by date: in July 2025 the monitoring wing reported no formal complaints and had contacted the GCC; by September 2025 the ministry had written to the GHC. The old "but" reversed the sequence. [D0164, D0173]
14. **BAIRA Malaysia syndicate:** "earlier" → "over the previous three years", as the source says. [D0172]
15. **Tasheer** explained as a visa service centre. Stamping time gets "in some cases" (source: ক্ষেত্রবিশেষে). Enjaz explained. [D0130, D0132, D0177]
16. **"TIB's 2026 research found …"** → "TIB has reported …". Bonik Barta (Oct 2026) cites TIB undated; its other TIB figures are from 2016. [D0108]
17. **BMET fees: "Fees, paid by bank pay order"** → the welfare, insurance and smart card fees go by pay order and the tax by treasury challan. Charter item 8 says so. [D0002]
18. **Source income tax:** added the dropped "Tk 500 for a Saudi visa". [D0003]
19. **ACC case** → "On 3 July 2025 the ACC filed a case against four BMET officials and the owners or officials of five agencies; it says its 29 May 2025 raid found …". Not all four were emigration officials (one is a survey officer, one an office assistant), and the agencies' people, not the agencies, are the accused. The findings are now attributed to the ACC. No individuals are named. [D0154-D0156]
20. **Added after the minister's quote:** "BMET's charter lists online visa checks for Saudi Arabia, Qatar, Bahrain, Singapore and the UAE". [new VD0004, charter p.2]
21. **Agency complaint: "decided in 30 working days"** → "handled within 30 working days", with an official cite for "free" and 30 days. The ministry takes the final decision. [D0010, new VD0005, charter p.7]
22. **SB screening desk** → dated "In 2021". The only source is Dhaka Post 2021. [D0087]
23. **Offloading definition: "often marked with an 'offload' stamp"** → "in cases reported in 2021 it was marked …". [D0082, D0086]
24. **"SB's own reasons are …"** → "Reported reasons include …". The reasons are Bonik Barta's narration, not SB's. [D0031]
25. **Nepal case:** "visas, return tickets, hotel bookings and a dollar endorsement" → "visas or entry permits, return tickets and hotel bookings, one also carrying a dollar endorsement". The questioning, the phone calls, the passport kept and the escort out are now attributed ("They say", "their lawyer says"). These are the women's allegations. [D0041, D0198, D0051, D0050, D0042, D0049, D0043]
26. **Case labels "2026"** → "Reported 2026". Bonik Barta doesn't date the incidents. [D0032, D0034, D0035]
27. **Rights: High Court bullet** → "issued a rule … ordered the Additional IGP to investigate and resolve their complaint within seven days and report to the court". The investigation and report duties had been dropped. [D0046, D0047]
28. **"For workers, the BMET card and the welfare desk's seal"** → the airport says the seal speeds immigration. Officers were not shown asking for it. [D0075]
29. **If you are offloaded, step 1 "Ask for the reason and the officer's name and rank"** cut. It was our own advice. It is replaced by a cited lead-in, and the steps are renumbered. [D0050]
30. **"as the three women did on 31 August 2026"** → "in late August 2026". TBS says 31 August and Prothom Alo English says 30 August. [D0044]
31. **New Need to know:** OC Immigration's mobile is 01320005902 on SB's contact page but 01713373073 on its complaint page.
32. **OC, SSP and DIG** expanded at first use. **KLIA** expanded.
33. **Malaysia refusals** reordered by date (204 on 13 Aug, then 98 on 15 Aug). The counter-setting sentence now says MACC "arrested 60 people, including 49 immigration officers", not "until", which implied the racket ended. [D0179, D0114, D0117, D0118]
34. **US deportees:** "paying Tk 30 to 35 lakh" → BRAC says such journeys cost Tk 30-35 lakh. That figure is BRAC's general estimate, not the seven's. Also "entered the US irregularly via Mexico". [D0184]
35. **Customs rule 8(3):** added the dropped conditions: by mistake or unavoidable reason, within 30 days, Schedule 1 form, an officer not below Assistant Commissioner. [D0192]
36. **"Italy and the Schengen area: 3 to 5 years"** → "Italy: 3 to 5 years, longer in some cases, entered in the Schengen Information System, so it also bars entry to EU and other Schengen states". The Schengen part had no cite. [D0128, new VD0002, VD0003]
37. **TIB complaints:** "about half did not know where or how" → "about half of all households". The source's base is all households. [D0144]

#### Source date fixed

- `news-dailystar-migrants-medical-scam` (Daily Star, "Migrants trapped in medical scam") shows "Published : 10 July 2025, Updated : 11 July 2025" in the saved copy. Its page_date is now 2025-07-10 in `sources.csv` and in the facts that cite it (D0157-D0164), with a note. A small script made this change, since `facts.py` has no edit command. The citation year (2025) is unchanged.

#### New facts

- VD0001: DW, TIB passport study, 21 August 2017
- VD0002: Italy TUI art. 13(14-bis), Schengen-wide ban
- VD0003: Italy, ban can exceed five years
- VD0004: BMET charter p.2, online visa checks for five countries (quote check skipped, garbled text layer; transcribed from page image)
- VD0005: BMET charter p.7, agency complaint free, 30 working days (same)

#### Issues not fixed

- **D0167:** the Kuwait re-test fee is "5 dirhams" in the source. Kuwait's currency is the dinar, so this is probably a source error. Kept as quoted.
- **Old official pages:** many official SB, HSIA, NHRC and ACC pages are undated (possibly outdated). The OK to Board (Air Arabia) and SB screening-desk facts rest on single old or undated sources.
- **Unofficial sources:** the Malaysian refusal figures are news only. The Kuwait lifetime ban rests on Arab Times (2025), and the Malaysia 1-5-year blacklist on a 2017 news report. An official source is still needed for each.
- **Desk numbers:** the Dhaka desk number in BMET's charter is printed as 07152228307 (it looks malformed). It is cited only inside a Need to know.
- **Unexplained title:** "SS Immigration" is left as SB prints it. Its meaning is not given in any saved source.
- **Country-doc links:** the part has no links to country docs, so there was nothing to check. The internal cross-references ("see Where to complain", "see BMET clearance and the smart card") match real headings.
- **Build:** `build.py` runs clean.

## Illegal routes (prefix I; fact-check VI)

### What this part covers
Libya-Italy boats; Balkans and Eastern Europe; visit/tourist visas sold as jobs (UAE, Saudi, Oman, Kuwait, Qatar, Malaysia, Maldives); free/azad visas and visa trading; Malaysia via Cambodia-Thailand and the old boat route; scam compounds in Cambodia, Myanmar, Laos; Kyrgyzstan and Central Asia; Russia war recruitment; student visas; forged documents; Bangladesh law; help contacts.

### Sources
- About 260 facts were imported from the country folders (italy, cambodia, kyrgyzstan, malaysia, kuwait, oman, qatar, jordan, maldives, saudi-arabia, united-arab-emirates, singapore) with source files, fetchlog rows and sources.csv rows copied. Each imported fact's note says "from <country> <id>". Statuses were recomputed for this folder (official dated within 12 months = verified, else possibly-outdated; news = unofficial).
- New sources fetched for this part: Al Jazeera, RFE/RL (x2), Fortify Rights (Russia war); Dhaka Tribune (Bosnia; Libya longform; "lose millions"; Myanmar 18; home minister on new law); TBS (Europe surge; Mizdah 2020; CID Libya mafia); TBS Bangla (flawed vetting/warfront); IJ4EU (Romania); Daily Star Bangla (Eastern Europe work permits, 2021); ANN (13 embassies warning; 18 dead Greece via Libya); Prothom Alo English (Al Khums capsize); BSS (ordinance approval; 2026 Act); Daily Observer (2026 Act workshop); Freedom Collaborative (new law replaces 2012 Act); Polish Border Guard (forged visa, 2022); Bangladesh Police CID unit page; Bangladesh Monitor (Biman officer; Bangkok embassy Myawaddy).

### Key findings and conflicts
- The Prevention and Suppression of Human Trafficking Act 2012 has been replaced. Ordinance approved by the Council of Advisers 27 Nov 2025 (BSS); Act adopted 9 April 2026 (UNODC). Names vary across sources: "Prevention and Suppression of Human Trafficking and Migrant Smuggling Act, 2026", "Human Trafficking and Migrant Smuggling Prevention and Suppression Act, 2026", "Prevention and Suppression of Trafficking in Persons and Smuggling of Migrants Act, 2026". The official gazette text was not found on bdlaws; section numbers and exact penalties come from BSS/Observer press summaries of the Home Ministry briefing. A Dec 2025 Chandpur case was still filed under the 2012 Act (I0365 source).
- Russia deaths: police/SRB say 20 of 30 May 2026 recruits dead (17 on day one); Minister told Parliament on 9 July 2026 that 4 had died (earlier count); Fortify Rights counts at least 34 killed of 104 recruited (to Feb 2026). Agencies: three licences cancelled (Kaler Kantho, Jun 2026) vs suspended (Minister, Jul 2026).
- Russia clearances: 7,449 (RFE/RL, 1 Jan 2025-27 Oct 2026) vs 7,752 in "21 months" (bdnews24 via cambodia doc). Different windows.
- 12-country list in the 4 Nov 2026 Ministry letter differs between Prothom Alo, Bangla Tribune and bdnews24 (Cambodia vs Croatia; Kosovo, Bosnia).
- Libya route totals: 92,427 (2009-2024) and 105,719 sea crossings (Dhaka Tribune longform) vs ~110,000 to June 2026 (Frontex via Dhaka Tribune Nov 2026). Used the latter.
- ANN pages (13-embassy warning; 18 dead Greece-via-Libya) show no date in the saved HTML; search snippets suggest April/March 2026. Logged as undated.
- Daily Star Bangla Eastern Europe work-permit piece is from 2021 (cited with year).
- Polish Border Guard PDF text lost Polish diacritics; fact I0316 logged with --no-quote-check and a note.

### Pages we could not download / gaps
- Bangladesh Embassy Tripoli and Moscow contact pages: new mofa.gov.bd portal renders contact pages via JS; Firecrawl returned empty content. Needs a browser.
- IOM Bangladesh contact page returns 404.
- CID THB Unit public phone/email not found on police.portal.gov.bd.
- business-humanrights.org Romania page (403); asianews.it 23 drowned 2025 (403).
- No 2025-26 source found on Bangladeshis on the Belarus-Poland route, or on 2026 street prices for Serbia/Croatia/Romania permits.
- Official text of the 2026 Act (bdlaws) not located.

### Fact-check report

Checked 19 November 2026 against facts.csv quotes and the saved sources. All changes are in doc.md; new facts VI0001-VI0033 are in facts.csv; build.py runs without citation errors.

#### Changes

#### 1. Maldives had no citation; added I0206

- Before: a Gulf or Maldives street with no permit, a Thai or Malaysian immigration depot, or an airport counter where a fake visa is found and you are sent home [I0021, I0346, I0088, I0311, I0265, I0185, I0148, I0146, I0040]
- After: a Gulf or Maldives street with no permit, a Thai or Malaysian immigration depot, or an airport counter where a fake visa is found and you are sent home [I0021, I0346, I0088, I0311, I0265, I0185, I0206, I0148, I0146, I0040]

#### 2. 'almost always' is our own generalisation, unsupported

- Before: The giveaway is almost always the same: a tourist or visit visa instead of a work visa
- After: Common signs: a tourist or visit visa instead of a work visa

#### 3. removed own conclusion; explained BMET at first use

- Before: Many victims left with real BMET clearance and a licensed agency, so clearance alone does not make a job real [I0068, I0073].
- After: Many victims left with real emigration clearance from BMET (the Bureau of Manpower, Employment and Training) and still ended up in scam compounds [I0068, I0073].

#### 4. source says 'often', not 'most'

- Before: Most of the Italy-bound boats are the last stage of an attempt at legal migration that failed [I0019, I0282].
- After: Taking the boat to Italy is often the last stage of an attempt at legal migration that failed [I0019, I0282].

#### 5. replaced press summary with official Act text (ss.15, 16, 54); s.16 is 1-3 years, so 'long' dropped; s.54 is narrower than 'breaking the law'

- Before: selling a fake job, trading visas, forging papers and smuggling people are crimes with long prison terms, and a person trafficked into breaking the law abroad is to be treated as a victim, not an accused [I0197, I0189, I0320, I0324].
- After: selling a fake job, trading visas, forging papers for smuggling and smuggling people are crimes with prison terms, and a trafficking victim cannot be charged for illegal entry or a false travel document that resulted from the trafficking [I0197, I0189, VI0007, VI0006, VI0019].

#### 6. Ministry claim uncited (added I0222); CID and IOM explained at first use

- Before: Families can complain to the CID, local police, BMET and the Ministry, and BRAC and IOM help with returns (see Where victims and families get help) [I0361, I0356, I0224, I0027, I0228].
- After: Families can complain to the CID (the police's Criminal Investigation Department), local police, BMET and the Ministry of Expatriates' Welfare, and BRAC and IOM (the International Organization for Migration, the UN migration agency) help with returns (see Where victims and families get help) [I0361, I0356, I0224, I0222, I0027, I0228].

#### 7. one case stated as general; source is about two men

- Before: Men unpaid in Dubai have been offered Libya by facilitators there [I0283]. One ring in 2025 promised jobs in Greece for Tk 15 lakh each and flew the men to Libya instead [I0362].
- After: A man left unpaid in Dubai was offered Libya by a facilitator there [I0283]. In 2025 two men promised jobs in Greece for Tk 15 lakh each were flown to Libya instead [I0362].

#### 8. ransom amounts dated; Bhairab figure is 'reportedly' in source

- Before: In 2026 families were asked Tk 25 lakh per person, for six men from Manoharganj, Cumilla, and for more than 300 from Bhairab, Kishoreganj [I0021, I0024, I0348].
- After: In July 2026 families of six men from Manoharganj, Cumilla, were asked Tk 25 lakh per person, and in November 2026 the same sum was reportedly being demanded for each of more than 300 men from Bhairab, Kishoreganj [I0021, I0024, I0348].

#### 9. clarity: the sums were ransom

- Before: - **Paying does not free you.** In a 2025 case the families paid Tk 21.8 lakh and Tk 16 lakh, and the men were then handed to Libyan police and held 45 days [I0363, I0364].
- After: - **Paying does not free you.** In a 2025 case the families paid Tk 21.8 lakh and Tk 16 lakh in ransom, and the men were then handed to Libyan police and held 45 days [I0363, I0364].

#### 10. allegation attributed (source: Libya's GNA)

- Before: - **Death.** In May 2020 a trafficker's family killed 26 Bangladeshis and four Africans in Mizda, Libya [I0332].
- After: - **Death.** In May 2020, according to Libya's then government, a trafficker's family killed 26 Bangladeshis and four Africans in Mizda, Libya [I0332].

#### 11. source was logged undated; found dateline 30 March 2026 and departure 21 March from Tobruk (VI0024); minister's claim attributed as allegation as in source

- Before: In 2026 at least 18 Bangladeshis died on a boat from Libya to Greece that carried 38 Bangladeshis among 43 people [I0333, I0334]. The State Minister for Expatriates' Welfare said smugglers abandon
- After: In March 2026 at least 18 Bangladeshis died on a boat that left Tobruk, Libya, for Greece, carrying 38 Bangladeshis among 43 people [I0333, VI0024, I0334]. The State Minister for Expatriates' Welfare alleged that smugglers abandon

#### 12. count runs to 3 Nov 2025; 'two of whom' referred to the 4 returned on 31 Oct, not the 120

- Before: Italy returned over 120 Bangladeshis in 2025, two of whom had arrived from Libya without a visa a month before [I0035, I0066].
- After: Italy returned over 120 Bangladeshis in 2025 up to early November, including four on 31 October, two of whom had arrived from Libya without a visa a month before [I0035, I0066].

#### 13. cited official Act text (ss.2(20), 4, 14-15) instead of press summary

- Before: - **Bangladesh:** organising this journey is migrant smuggling, and holding people for ransom is trafficking, under the 2026 Act (see The law in Bangladesh) [I0331, I0321].
- After: - **Bangladesh:** under the 2026 Act, organising this journey is migrant smuggling, holding people for ransom is a form of exploitation under the trafficking offence, and the Act also covers offences committed abroad against Bangladeshis (see The law in Bangladesh) [VI0006, VI0003, VI0020].

#### 14. conversion cited the USD rate (I0067); EUR rate now logged (VI0031, Tk 139.61)

- Before: fined EUR 5,000 to 10,000 (about Tk 6.98 to 13.96 lakh) [I0049, I0067]
- After: fined EUR 5,000 to 10,000 (about Tk 6.98 to 13.96 lakh) [I0049, VI0031]

#### 15. unconvicted person: stated as accused

- Before: which led the CID to arrest the man who ran the ransom calls (see Where victims and families get help) [I0365, I0356].
- After: which led the CID to arrest a man accused of coordinating the ransom demands (see Where victims and families get help) [I0365, I0356].

#### 16. source logged undated; dateline 9 April 2026 found (VI0025)

- Before: Thirteen Western embassies, including Italy, Hungary and Germany, have jointly warned Bangladeshis
- After: In April 2026 thirteen countries' missions, including Italy, Hungary and Germany, jointly warned Bangladeshis

#### 17. date support

- Before: none of them works with any agent [I0309, I0310].
- After: none of them works with any agent [I0309, VI0025, I0310].

#### 18. EUR conversion needs EUR rate (11,000 x 139.61 = Tk 15.36 lakh)

- Before: A Romanian job sold for EUR 11,000 (about Tk 15.4 lakh) turned out to be undeclared building work, 12 hours a day, 7 days a week [I0043, I0044, I0067].
- After: A Romanian job sold for EUR 11,000 (about Tk 15.4 lakh) turned out to be undeclared building work, 12 hours a day, 7 days a week [I0043, I0044, VI0031].

#### 19. source context: Decreto Flussi

- Before: Thousands of Bangladeshis have paid up to EUR 20,000 for Italian work permits that never came [I0300].
- After: Thousands of Bangladeshis have paid up to EUR 20,000 for Italian work permits under Italy's quota scheme (Decreto Flussi) that never came [I0300].

#### 20. wage claim is what workers told rights groups; attributed

- Before: rights groups reported possible trafficking [I0295]. Many had borrowed up to USD 10,000, had passports taken on arrival, were paid below
- After: rights groups reported possible trafficking [I0295]. Many had borrowed up to USD 10,000 and had passports taken on arrival; workers said they were paid below

#### 21. Russia is not on bdnews24's list; added Daily Star's fourth version (VI0026) and stated only what all lists share

- Before: - **Bangladesh:** on 4 November 2026 the Ministry of Expatriates' Welfare told BMET to give no clearance without its permission for 12 countries, including Serbia, Moldova, Belarus and Russia [I0114]. Published lists of the 12 differ, some naming Croatia, Kosovo and Bosnia [I0115, I0116].
- After: - **Bangladesh:** on 4 November 2026 the Ministry of Expatriates' Welfare told BMET to give no emigration clearance for 12 countries without the Ministry's recruitment permission or approval [I0114]. Every published list names Serbia, Moldova, Belarus, Japan, Iraq, Laos, Vietnam, Ukraine and Libya; most also name Russia and Cambodia; the rest differ between reports (Congo, Kosovo, Croatia or Bosnia) [I0114, I0115, I0116, VI0026].

#### 22. 'usually' unsupported; Saudi case is reported as allegations (2024)

- Before: The person is usually told he has a work visa: to Saudi Arabia, a three-month tourist visa sold with a promised 15-month iqama (residence permit); to Cambodia,
- After: Brokers tell people they have a work visa: to Saudi Arabia, allegedly, a three-month tourist visa sold with a promised 15-month iqama (residence permit); to Cambodia,

#### 23. 'main' supported only for Libya

- Before: Dubai remains the main transit to Libya, Kyrgyzstan and Russia [I0290, I0120, I0269].
- After: Dubai is the usual transit point to Libya and has also been used for Kyrgyzstan and Russia [I0290, I0120, I0269].

#### 24. source: anonymous official, 'sometimes'

- Before: Traffickers also use Umrah (pilgrimage) visas to get people out before sending them elsewhere [I0355].
- After: An immigration official said traffickers sometimes use a valid visa for one country, such as a tourist or Umrah (pilgrimage) visa, before sending people elsewhere [I0355].

#### 25. acronym

- Before: Only some visit visas can be converted, for KD 150 [I0166].
- After: Only some visit visas can be converted, for KD 150 (Kuwaiti dinars) [I0166].

#### 26. unconvicted person: allegation stated as accusation; Sepang: employers misused passes

- Before: - **Malaysia:** in October 2026 the CID arrested a Paltan travel agency owner who took two people to Malaysia on visit visas promising work permits, held them and demanded Tk 5 lakh from their families [I0153]. In September 2026 Malaysian immigration detained 147 Bangladeshis on Sepang building sites where social visit passes were misused [I0159].
- After: - **Malaysia:** in October 2026 the CID arrested a Paltan travel agency owner accused of taking two people to Malaysia on visit visas with a promise of work permits, holding them and demanding Tk 5 lakh from their families [I0153]. In September 2026 Malaysian immigration detained 147 Bangladeshis on Sepang building sites where employers had misused social visit passes [I0159].

#### 27. allegation dated

- Before: - **Airport collusion:** brokers allegedly pay airport staff Tk 30,000 to 50,000 per passenger, called a "body contract", to pass immigration with incomplete papers [I0354].
- After: - **Airport collusion:** allegations reported in November 2026 say brokers pay some airport staff Tk 30,000 to 50,000 per passenger, called a "body contract", to pass immigration with incomplete papers [I0354].

#### 28. I0194 (no conversion) and I0247 (prohibited immigrants) don't say working is illegal; UAE/Saudi/Oman uncited; 'see the path above' is not an allowed link

- Before: - **Destinations:** working on a visit visa is illegal in every Gulf country covered, in Malaysia and in the Maldives (see the path above) [I0165, I0194, I0247, I0207].
- After: - **Destinations:** Kuwait bars every visit visa holder from working, and in the Maldives trying to work on a tourist visa can mean jail and a fine (see The path, country by country) [I0165, I0207].

#### 29. advice of our own with no source (I0219 is only the call centre)

- Before: Before travelling, check the visa type with the destination's own visa portal or the Bangladesh embassy; after it goes wrong, call the Probash-Bondhu call centre (see Where victims and families get help) [I0219].
- After: The Probash-Bondhu call centre answers workers and families 24 hours (see Where victims and families get help) [I0219].

#### 30. source says 'recruiting agencies', not 'licensed'; ring quote is in I0162

- Before: Of those who knowingly bought one, 54% went through illegal broker networks, 31% through distant relatives and 7% through licensed agencies [I0182]. In Kuwait an organised ring sells visas for lakhs of taka under the "free visa" name [I0161].
- After: Of those who knowingly bought one, 54% went through illegal broker networks, 31% through distant relatives, 8% through family and 7% directly through recruiting agencies [I0182]. In Kuwait an organised ring sells visas for lakhs of taka under the "free visa" name [I0161, I0162].

#### 31. source is Qatar, 'sometimes'

- Before: Sponsors demand regular payments to keep sponsoring [I0186].
- After: In Qatar, sponsors sometimes demand regular payments to keep sponsoring [I0186].

#### 32. two sources merged into a claim neither makes

- Before: - **Absconding cases:** sponsors file false "absconding" (runaway) reports to free up quotas for resale, which makes the worker illegal [I0163, I0171].
- After: - **Absconding cases:** brokers in Kuwait file false "absconding" (runaway) reports to free up visa quotas for resale, and some sponsors in Oman report free-visa workers as absconding so they are not punished if the worker is caught elsewhere [I0163, I0171].

#### 33. Qatar-only sources stated as general

- Before: - **No rights:** a free-visa worker has no legal help if unpaid [I0178]. Free-visa workers hunt for illegal day labour and many face harassment, arrest or deportation [I0185].
- After: - **No rights:** in Qatar a free-visa worker has no legal help if unpaid [I0178]. Free-visa workers there hunt for illegal day labour and many face harassment, arrest or deportation [I0185].

#### 34. fine is a maximum

- Before: - **Qatar:** visa trading, and working on a free visa, carry up to 3 years in prison and a QR 50,000 fine [I0176, I0178].
- After: - **Qatar:** visa trading, and working on a free visa, carry up to 3 years in prison and a fine of up to QR 50,000 (Qatari riyals) [I0176, I0178].

#### 35. I0224 is the complaint route, not visa checking; I0191 (BMET leaflet) supports checking

- Before: Before paying, ask BMET whether a visa is real; after it goes wrong, complain about the broker under the 2013 Act (see Where victims and families get help) [I0224, I0196].
- After: BMET asks anyone handed such a visa to have it and the other papers checked at BMET in Dhaka or the District Employment and Manpower Office; after it goes wrong, anyone cheated can complain to the government under the 2013 Act (see Where victims and families get help) [I0191, I0196].

#### 36. 'fill the gap' is our conclusion; figures are 'believed'/'estimated'; gang name derives from a person's name, dropped

- Before: Smuggling rings fill the gap: one Bangladeshi ring, the "Karim Gang", charged up to RM15,000 (Malaysian ringgit) per person and made about RM3.2 million in 2026 [I0144].
- After: A Bangladeshi smuggling ring broken up in Malaysia in July 2026 is believed to have charged up to RM15,000 (Malaysian ringgit) per person and made about RM3.2 million since January 2026 [I0144].

#### 37. no source gives Tk 4.8 lakh for Cambodia; cited sources give 5.3, 5.5, 5.6 and 6 lakh

- Before: for about Tk 4.8 to 5.5 lakh [I0073, I0076, I0090, I0069].
- After: for about Tk 5.3 to 6 lakh [I0073, I0076, VI0028, VI0029].

#### 38. the study's 66% via middlemen contradicted 'through licensed agencies'

- Before: Many go through licensed agencies with BMET clearance: a BRAC study found 66% were recruited through middlemen and 98% never got the promised job [I0068, I0081].
- After: Many went with BMET clearance [I0068, I0073]. A BRAC study found 66% of cyber-scam victims were recruited through middlemen and 98% never got the promised job [I0081].

#### 39. I0087 (The Star) says 583 'by June' including 109; TBS says 583 in June plus 109 on 1 July; Myawaddy figure dated

- Before: - **Returns:** 583 Bangladeshis came home from Cambodia in June 2026, 109 of them rescued from compounds; 221 returned in four days that month [I0087, I0075]. About 50 rescued from Myawaddy, Myanmar, have been repatriated through the Embassy in Bangkok [I0342].
- After: - **Returns:** 583 trafficking victims came home from Cambodia in June 2026, including 221 in four days, and another 109 on 1 July [VI0027, I0075]. By April 2026 about 50 people rescued from Myawaddy, Myanmar, had been repatriated through the Embassy in Bangkok [I0342, VI0030].

#### 40. undated window

- Before: - **Laos:** 7,532 Bangladeshis went to Laos in 21 months [I0079].
- After: - **Laos:** 7,532 Bangladeshis went to Laos in the 21 months before October 2026 [I0079].

#### 41. official text (s.2(20)); 'victims, not offenders' goes beyond s.54, which covers only entry, stay and travel documents

- Before: - **Bangladesh:** the 2026 Act treats forced criminality in scam compounds as trafficking, so those held there are victims, not offenders [I0329].
- After: - **Bangladesh:** the 2026 Act counts forcing a person into crimes such as online scamming as exploitation under the trafficking offence [VI0003, I0329].

#### 42. Bangla Tribune's list omits Cambodia

- Before: Cambodia is one of the 12 countries needing Ministry approval (see The Balkans and Eastern Europe) [I0114].
- After: Most published lists of the 12 countries needing Ministry approval since 4 November 2026 include Cambodia (see The Balkans and Eastern Europe) [I0114, I0116, VI0026].

#### 43. no source says Saudi Arabia; I0132 does not mention routing

- Before: 1. **Dhaka to Dubai, then Moscow** [I0269]. Some groups were routed through Saudi Arabia and the UAE [I0132].
- After: 1. **Dhaka to Dubai, then Moscow**, or through other third countries [I0269, I0268].

#### 44. death counts dated and attributed; '20 of the 30' not in source (20 Bangladeshis confirmed dead); earlier official count added

- Before: - **Death:** of 30 men who landed in Moscow on 7 May 2026, 17 were killed on their first day of deployment after minimal training, and 20 were confirmed dead [I0265, I0273]. Police said the Bangladeshis were used as bait to locate enemy positions [I0266]. Fortify Rights and Truth Hounds, two rights groups, documented at least 104 Bangladeshis recruited and at least 34 killed [I0275].
- After: - **Death:** 30 men flew out on 7 May 2026 [I0273]. In October 2026 the commander of the police's Special Response Battalion said 17 who arrived that May were killed on their first day of deployment after minimal training, 20 Bangladeshis were confirmed dead, and they had been used as bait to locate enemy positions [I0265, I0266]. On 9 July 2026 the Minister had told Parliament that four of the 30 had died [I0314]. A joint investigation by Fortify Rights and Truth Hounds, two rights groups, counted at least 104 Bangladeshis recruited and at least 34 killed [I0275].

#### 45. allegation against agencies dated and attributed; bdnews24's list omits Russia

- Before: - **Bangladesh:** the government cancelled the licences of three agencies and forfeited their deposits over the 30 men, and police arrested two men accused of the trafficking in October 2026 [I0158, I0263]. The Expatriates' Welfare Minister told Parliament on 9 July 2026 that three agencies' licences had been suspended [I0314]. Russia is one of the 12 countries needing Ministry approval before clearance [I0114].
- After: - **Bangladesh:** in June 2026 the government cancelled the licences of three agencies accused of sending the 30 men, and forfeited their deposits [I0158]; on 9 July 2026 the Expatriates' Welfare Minister told Parliament the three licences had been suspended [I0314]. In October 2026 police arrested two men accused of the trafficking [I0263]. Most published lists of the 12 countries needing Ministry approval since 4 November 2026 include Russia [I0114, I0115, VI0026].

#### 46. dated

- Before: - **Fake visas:** two men agreed Tk 30 lakh each for Italy, paid Tk 20 lakh up front, and were given fake Schengen visas [I0359, I0038].
- After: - **Fake visas:** in May 2026 two men agreed Tk 30 lakh each for Italy, paid Tk 20 lakh up front, and were given fake Schengen visas [I0359, I0038].

#### 47. allegation attributed and dated

- Before: A ring sent another woman to Italy on a woman's visa; CID seized 56 passports and 153 seals [I0042].
- After: In July 2026 the CID arrested members of a ring accused of sending a woman to Italy on another woman's visa, and seized 56 passports and 153 seals [I0042].

#### 48. unconvicted: stated as accusation, dated

- Before: A Biman ground officer who helped them board was arrested [I0039].
- After: In June 2026 a Biman ground officer was arrested, accused of helping them board [I0039].

#### 49. I0253 is a 2019 rule, not a report of cases

- Before: applicants caught with fake papers have been banned and reported to the police [I0252, I0253].
- After: the visa centre's rules say applicants caught with fake papers are banned from applying and reported to the police [I0252, I0253].

#### 50. replaced press summary with official text (ss.16, 54)

- Before: - **Bangladesh:** passport or visa forgery for smuggling is a serious offence under the 2026 Act [I0320]. A person trafficked into carrying a forged passport is not to be treated as accused [I0324].
- After: - **Bangladesh:** making, obtaining, supplying or holding a document to help migrant smuggling carries 1 to 3 years' rigorous imprisonment and a fine of at least Tk 50,000 under the 2026 Act [VI0007]. A trafficking victim cannot be charged for getting or holding a false travel document as a direct result of the trafficking [VI0019].

#### 51. section rested on BSS/Observer press summaries; rewritten from the official text on bdlaws (Act No. 55 of 2026). Corrections: '3 to 7 years for fake online job ads or fraud in the name of migration' is officially s.20, advertising for migrant smuggling; victim protection (s.54) is limited to illegal entry/stay and false travel documents; added minimum penalties, s.27, s.28 complaint route, s.4 extraterritorial reach; UNODC 9 April date kept as 'April 2026' since bdlaws dates the Act 10 April

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

#### 52. added the official filing route and protection from the Act (s.28)

- Before: 2. **File a criminal case with the local police.** CID asks returnees to file cases with their local police so the brokers and agencies can be prosecuted [I0356].
- After: 2. **File a criminal case with the local police.** CID asks returnees to file cases with their local police so the brokers and agencies can be prosecuted [I0356]. Under the 2026 Act a case can be filed at a police station or directly with the tribunal, and the police must protect the complainant and keep their identity confidential [VI0014].

#### 53. acronym

- Before: OEP hotline: 09614445271 [I0225].
- After: Hotline of OEP (the Overseas Employment Platform, BMET's online system): 09614445271 [I0225].

#### 54. acronym

- Before: apply to the Welfare Board directly or through the DC office's expatriate welfare branch or the DEMO (District Employment and Manpower Office)
- After: apply to the Welfare Board directly or through the expatriate welfare branch of the Deputy Commissioner's (district administration) office or the DEMO (District Employment and Manpower Office)

#### 55. law says 'breaking the purpose of entry'; currency explained

- Before: - **Fines and deportation:** working on a tourist visa is fined 10,000 som in Kyrgyzstan, and in September 2025, 180 Bangladeshis were sent back [I0138, I0137].
- After: - **Fines and deportation:** breaking the purpose of entry, such as working on a tourist visa, is fined 10,000 som (Kyrgyz currency) in Kyrgyzstan, and in September 2025, 180 Bangladeshis were sent back [I0138, I0137].

#### 56. acronym; fine is per student

- Before: the employer is fined at least JD 800 [I0257, I0258].
- After: the employer is fined at least JD 800 (Jordanian dinars) per student [I0257, I0258].

#### New sources and facts

- **bdlaws-trafficking-smuggling-act-2026-full** (official, Legislative and Parliamentary Affairs Division, http://bdlaws.minlaw.gov.bd/act-details-1684.html): full official text of the Human Trafficking and Migrant Smuggling Prevention and Suppression Act, 2026, Act No. 55 of 2026, dated 10 April 2026. Facts VI0001-VI0023, VI0032, VI0033. (A table-of-contents copy, bdlaws-trafficking-smuggling-act-2026, was also fetched but is not registered or cited.)
- VI0024 (ANN/Daily Star 18 dead, dated 30 March 2026), VI0025 (13-country warning, dated 9 April 2026), VI0026 (Daily Star's 12-country list with Kosovo), VI0027 (TBS: 583 in June plus 109 on 1 July), VI0028-VI0029 (Cambodia prices Tk 5.6 and 6 lakh), VI0030 (Myawaddy report dated 28 April 2026), VI0031 (Bangladesh Bank EUR rate Tk 139.61, 10 Nov 2026).

#### Issues not fixed

- **12-country list (4 Nov 2026):** no official copy found on probashi.gov.bd or bmet.gov.bd (searched; BAIRA reportedly circulated the letter). Four press versions: Prothom Alo (Congo, Russia, Cambodia), Bangla Tribune (Croatia instead of Cambodia), bdnews24 (Kosovo and Bosnia instead of Congo and Russia), Daily Star (Kosovo instead of Congo). Need to know line kept.
- **Cambodia clearance counts conflict:** 15,921 in 18 months (TBS, Jul 2026), 15,963 in 21 months (bdnews24, Oct 2026), 15,235 Jan 2025-30 Oct 2026 (Daily Star, Nov 2026). Doc keeps the TBS figure; not resolvable without BMET data. Russia: 7,449 (RFE/RL) vs 7,752 (bdnews24) vs 5,776 (Daily Star).
- **Act date:** UNODC says adopted 9 April 2026; bdlaws dates Act No. 55 to 10 April 2026. Doc now says 'April 2026'. The Act is in Bangla only; s.66 says an English translation will be published. English title is our translation.
- **I0087 vs VI0027:** The Star says 583 by June including 109 rescued; TBS says 583 in June plus 109 on 1 July. Doc follows TBS. I0087 now uncited.
- Facts I0320, I0322, I0323, I0324, I0317, I0318, I0319, I0321, I0325, I0327, I0375, I0067 (for EUR), I0090, I0069, I0132 (routing) are no longer cited where they were; the press summary I0322 ('fake online job ads or fraud in the name of migration, 3-7 years') does not match the official text (s.20 is advertising for migrant smuggling).
- I0333-I0335, I0309-I0310 and I0342 rows still show page_date 'undated'; dates are now carried by VI0024, VI0025 and VI0030.
- Fortify Rights/Truth Hounds figures (104 recruited, 34 killed) come from RFE/RL (Nov 2026); the saved Fortify Rights March 2026 page doesn't contain them.
- Embassy contacts for Tripoli and Moscow and the CID THB Unit's public number remain Need to know items (not re-searched).
- Not every source behind every sentence was opened in full; numbers and allegations were all checked against saved text, other sentences against the quotes.

## Conflicts resolved, 22 Nov 2026 (from the bot's prompt test)

- SVP fee: skills-test racket section said USD 50 (BMET leaflets VS0050/VS0051, Oct-Dec 2025); the fee rose to USD 85 in early September 2026 (F0091). Section now says USD 85 since September 2026.
- Debt payback example aligned with the Saudi guide's rate (SR 1 = Tk 33): Tk 8,250, about 55 months (was Tk 8,300 at Tk 33.20, 54 months).
