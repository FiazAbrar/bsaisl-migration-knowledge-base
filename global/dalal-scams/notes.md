# Dalal scams: research notes

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

- About 120 facts were re-logged from the country folders (Saudi Arabia, Malaysia, Jordan, Cambodia, Kuwait, Qatar, Italy, Kyrgyzstan, Singapore, UAE, Maldives, Oman, agencies) with a helper that copies the source files, fetch-log, wayback and sources.csv rows and re-runs `facts.py add` under prefix S (note column says "from <country> <id>"). Status was recomputed against the 2025-11-19 cutoff.
- About 95 facts are new, from: the consolidated OEM Act 2013 text on bdlaws (copied from the Jordan folder; sections 27, 28, 31-41, including the 2026 amendment's s.35A and revised s.39/40); the Prevention and Suppression of Human Trafficking Act 2012 (bdlaws, act-details-1086); and Bangla/English news (Finance Today, Balkan Insight, The Shift, Daily Star Bangla, Gramer Kagoj, Prothom Alo, Bangla Tribune, TBS, Protidiner Bangladesh, Samakal, Bangla Telegraph, Bangladesh Pratidin, Radio Today/Samakal).
- Country-doc cross-references are written as "(<Country> doc: <H2>, <H3>)" with exact heading text, so the lead can turn them into links after the merge.

## Conflicts and cautions

- The Ministry's 4 Nov 2026 list of 12 countries needing approval (S0127) is logged as a conflict in the Cambodia/Kyrgyzstan folders: Bangla Tribune lists Croatia instead of Cambodia. The doc uses the Cambodia folder's list; check the letter itself.
- Radio Today's Dubai dance-club story (S0189-S0191) is a reproduction of a Samakal report; the page shows 20 May 2026, and the woman's travel date (13 April 2023, "three years ago") is consistent with that, but the original Samakal date was not seen.
- The OKUP survey figures (72% borrowed, 11% mortgaged land, 6% sold assets; five times the official cost) come from an opinion piece in Bangla Telegraph (S0178), not OKUP's report itself.
- S0045 (OEP online complaint module from 30 July 2026) is news-sourced in the Saudi folder; an official notice would be better.
- BBS SEDS 2023: the 42.09% (agencies) and 3.09% (government) shares exist in the Qatar folder (A0002) but were not imported; only the 52.03% broker share is cited.

## Searched, not found (open questions)

- A public list of BMET-registered sub-agents (rule 17(4) of the 2025 rules says BMET or the DEMO publishes it); not found on bmet.gov.bd.
- Dalal's cut per worker on a typical Saudi or Malaysia visa in 2026.
- Fake nikahnama use for Gulf or Italian family visas: only China marriage-trafficking cases found.
- Money mules: no Bangladeshi case found of migrants lending bank/MFS accounts; only digital-hundi arrests of MFS agents.
- Croatia's reported suspension of work visas for Bangladeshis (early 2025): found only on blogs and social media, no official or mainstream source saved.
- Prices for Serbia, Croatia or Malta work permits in Dhaka.
- Village moneylender interest rates.
- A direct CID/police anti-trafficking complaint number for families.

## Pages we could not download

- dhakastream.net report on 56 agencies revoked (403); replaced by Bangladesh Pratidin, 15 Nov 2026.
- jagonews24.com/national/news/1166537 (Bangladesh-Libya trafficking ring) (403).
- jagonews OKUP "18% borrow at high interest" page saved with an empty .md; deleted, not used.

## Fact-check report

Checked 19 Nov 2026. About 190 cited sentences and list items checked against the quotes, and against the saved source wherever the sentence said more than the quote. Scanned PDFs (BMET skill-test notice, Takamol poster, BOESL warning, sub-agent rules p.18, BMET charter pp.2 and 17) were read from page images.

New source: `bdlaws-hmspsa-2026-full` (Prevention and Suppression of Human Trafficking and Migrant Smuggling Act 2026, Act 55 of 2026, bdlaws act-1684, dated 10 Apr 2026). New facts: VS0001-VS0052. Build passes.

### Changes

### Law

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

### Wrong citations

4. S0021 (Gramer Kagoj, China marriages) was cited for the Dream Visa raid and fake Fiji demand letters → S0022 plus new VS0023, VS0024 (Prothom Alo 2020).
5. S0142 (Italian report) quote was about a relative, not the passport → VS0029, VS0030 (passport kept until last instalment; EUR 18,000).
6. S0014 cited for "forced into sex work or labour" (quote is about the groom's religion) → VS0020; "or labour" cut.
7. S0108 quote didn't support the security-deposit claim → VS0040, attributed to the 2026 RMMRU study.
8. S0209 cited for "Wafid booking needs only the passport details" → reworded to the slip printed with passport number and nationality [VS0031].
9. S0212 (membership text) → VS0035 (the WEWB clearance-check link).
10. S0086 cited for "PKB grievance officers"; that sentence cut, cross-reference folded into the bribe item.
11. S0102 cited for the email address → VS0034.

### Figures

12. **North Macedonia / Serbia.** Before: "Oct 2025: Serbia and North Macedonia stopped issuing work permits ... about 90% ... fake". The source (Financial Today, 28 Oct 2025) attributes 90% to "diplomatic sources", says "the same situation exists in Serbia", and that no permits had been issued "for the past two months". Rewritten with attribution and that timeframe [S0001, S0002]. Item 1 of How it works listed Croatia, Poland, Malta and "far more than the official route" on a Romania-only source → "Serbia, North Macedonia or Romania" [S0001, S0148].
13. **Q-1 visas.** 4,226 (2020-2025), 35 (2022), 1,721 (2025) confirmed; also 1,016 (2023) and 1,378 (2024); arithmetic consistent (4,150 for 2022-25). The source stresses this is not a trafficking count and gives it as data from an anti-trafficking-law workshop. Moved out of "Cases" into a sentence with that caveat [S0019, VS0015-VS0017]. "Arrangers are said to get Tk 10-20 lakh" (anonymous Uttara resident, 2024) → "middlemen allegedly dealt in up to Tk 10-20 lakh" [VS0018, S0017].
14. **Kuwait visa.** "Costs the sponsor 6 KWD" was misleading: KWD 6 is processing plus attestation fees; the employer also spends about KWD 250 on the work permit [VS0025, VS0026]. Press Club claim attributed to its joint general secretary, July 2025.
15. **Gulf medical fee conflict.** Daily Star (Jul 2025) says total should not exceed Tk 8,500-9,000; TBS (Sep 2025) says the set fee is about Tk 10,000. Red flag now "well above about Tk 8,500-10,000" [S0210, VS0033, status conflict], plus a Need to know.
16. **Skill test.** Added the USD 50 fee and SVP expansion from the notice and poster images [VS0050, VS0051]; dropped unsupported "listed trades".
17. Trafficking cases: "122 in 2025, up from 86 in 2023" (cherry-picked) → full series 114/86/100/122 [S0191].
18. Malta EUR 600 and EUR 925 now have their own facts [VS0045, VS0046].

### Dates and attribution of cases

19. Every case dated to the event, with "reported" where only the article date is known: Dream Visa 15 Sept 2020; Saudi pharmacy case Oct 2022 (reported Sept 2024, was "2024"); Romania case July 2024 (reported Feb 2026, three places, was "Feb 2026"); Italy loans early 2023 (reported June 2026); Keraniganj woman Apr 2023 to May 2026 (was "2026"); Singapore case Apr-May 2026; Cambodia WhatsApp case 2025; Jhenaidah 2020; Chuadanga case filed 31 Mar 2024 (was "June 2024"); Fatema Overseas 15 Sept 2020.
20. Allegations attributed: shell-company visas (a broker to Bonik Barta, 2024); disappearing Saudi visas (former BAIRA official) and MHRSD cancellations (industry insiders) [VS0028]; Saudi permit-selling (an agent to Bonik Barta, "Gulf" → "Saudi Arabia"); medical bribes ("alleged"); PKB bribes (state minister citing complaints); CID cases ("accused", "allegedly"); Nepal case (according to BRAC). Nepal case corrected: the joint police-CID raid arrested a local broker; the traffickers then released the men near Kathmandu airport [VS0039] (doc said the raid freed them). Jhenaidah case: the Tk 50,000 went to two brokers, not the village recruiter [VS0047, VS0048].
21. "A dalal is often a friend or relative" attributed to an ILO consultant. "Agencies need dalals" (no source) cut; ITUC survey described as Recruitment Advisor reviews. Cambodia agency "licensed" → "manpower agency" (source doesn't say licensed).

### Overstatements and dropped conditions

22. In one minute: "The money is usually lost: few victims file cases" → CID statement on Cambodia returnees (2026); "The law is on paper strong" (opinion) cut; "most destinations" → "Saudi Arabia, Singapore and other destinations".
23. Free visa: "sold as a visa that lets you work anywhere" → entry permission with no job [VS0027].
24. Contract substitution: red flag "permit in the name of a company never heard of" cut (source doesn't say it); S0074 removed from the visa-title flag; IPA salary now cited to S0151, MOM salary check to S0154.
25. Staged payments: "passport is kept" → "may be kept"; "pay only through its bank account" → "deal with the agency through a bank"; "the bulk asked before the visa is checked" → the permission-letter condition.
26. UAE check: "job offer and work permit" → job offer by reference number (source covers only that). Oman: "ask the employer for the PDF" → status shows only in the sponsor's account.
27. Romania: "a way into Italy" → "to move on to another country"; "Romania or Malta contract" split into two attributed sources; Romania 90-day rule reworded to what the source says.
28. "Call 16699 before going to the police" (our advice) → plain helpline fact.
29. Acronyms explained at first use: MOHRE, MOM, ITUC, SVP, WEWB, NID, RL, RMMRU, JD, MFS; duplicate expansions of ILO and BAIRA removed.

### Cross-links

All 17 country-doc links checked against `countries/<c>/doc.md`; all named sections exist (Saudi, Malaysia, Qatar, UAE, Singapore, Maldives, Kyrgyzstan, Oman, Kuwait, Cambodia).

### Issues not fixed

- **Fact VS0005's claim text** also mentions ransom (the quote covers only online scamming); VS0006 is the ransom fact. Harmless but the claim could be trimmed.
- **Gulf medical fee:** conflicting news figures (Tk 8,500-9,000 vs about Tk 10,000); no official 2026 figure found. Left as a Need to know.
- **S0044 (complaint form fields) and S0043/S0046 (charter)** were verified in the Saudi folder; here the form PDF has no text layer. The charter's complaint officer (Director (Employment), 01711111544) was confirmed on p.17's image.
- **S0158 (BMET visa check):** the charter page read here appears to be the Chattogram DEMO's version; the service (demand letter/job visa check, free, 3 working days) matches.
- **S0055:** the Tk 165,000 Saudi cost dates from 2016; no newer official figure checked.
- **Rest of the 2026 trafficking Act** not mined: e.g. s.20 (advertising for migrant smuggling, 3-7 years, logged as VS0013 but not cited) could go in the Online scams section.
- The Need to know items in the doc were not researched further in this pass.
