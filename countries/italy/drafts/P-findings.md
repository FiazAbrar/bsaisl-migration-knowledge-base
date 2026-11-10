# P findings: the 10 hand-saved official files (Italy)

Agent P, 10 November 2026. Staging folder `countries/italy/work/P/` (facts.csv P0001-P0130, sources.csv 10 rows, scripts `log_facts.py` and `log_facts_fix.py`). No web research. Every file below was read in full.

**Two filing problems for the lead:**
- `interno-cruscotto-2024-12-31` and `interno-cruscotto-2025-12-31` are not the Interior Ministry's cruscotto. They are **UNHCR's "Italy Sea arrivals dashboard"** (December 2024, dated 11 April 2025; December 2025, dated 6 March 2026), built on Ministry figures. I registered them with publisher UNHCR, `official no`, so their facts are `unofficial` (or `conflict`). U already holds the real Ministry cruscotti (U0001-U0007).
- `gu-dl-146-2025` is the **original text** of Decree-Law 146/2025 as published on 3 October 2025 ("Vigente al: 4-10-2025"), **not** the version converted by Law 179 of 1 December 2025. The conversion law, where any Bangladesh/high-risk-country rule would sit, is not in the folder.

All text copies except `interno-it-decreto-flussi.md` are Windows-1252, not UTF-8. facts.py reads them with `errors="replace"`, so accented letters, guillemets, the euro sign and the soft hyphen become U+FFFD. I kept quotes to unaccented stretches; P0128 quotes the U+FFFD characters as they appear in the text copy.

## a. Facts by file

### 1. interno-circolare-7185-2026-flussi-2027: joint circular 7185, 1 October 2026 (Interior, Labour, Agriculture, Tourism), official, verified

- **Quotas 2027:** 165,850 in total: 76,200 non-seasonal, including 14,000 domestic and care workers; 89,000 seasonal; 650 self-employed [P0001-P0004]. **Confirms** W0001-W0004 and N0026 (165,850 for 2027).
- Kenya is added from 2027 (MoU of 2 July 2026); the DPCM's other breakdowns and reserved quotas are unchanged [P0005, P0006]. So the 25,000 reserved non-seasonal places for agreement countries still apply (W0023), but **the circular does not give Bangladesh's own share**.
- **Pre-filling:** 9:00 on 23 Oct 2026 to 20:00 on 7 Dec 2026 on the Portale Servizi ALI (https://portaleservizi.dlci.interno.it/AliSportello/ali/home.htm), including holidays, at any hour; the INL (labour inspectorate) may check pre-filled forms in advance [P0007-P0010]. Reopens 9:00 on 9 Dec to 20:00 on 13 Dec 2026 only to complete and save (status "da completare" to "da inviare"); no new applications [P0013-P0015]. **Confirms** W0005-W0008.
- **Forms:** C-Stag agricolo, C-Stag turistico, B2020 (non-seasonal), A-bis in quota (domestic and care) [P0011, P0012].
- **2027 click days, all from 9:00** [P0016-P0020]: 12 Jan 2027 seasonal agriculture; 9 Feb 2027 seasonal tourism; **16 Feb 2027 non-seasonal (B2020)**; 18 Feb 2027 domestic and care (A-bis). Applications are open until 31 Dec 2027 while quota lasts [P0021]. **Confirms** W0009-W0014.
- Circulars 8047 (16 Oct 2025) and 8524 (30 Oct 2025) still apply where compatible [P0022]. The immigration law (TUI) was amended by DL 146/2025, converted by Law 179/2025, and by D.Lgs. 83 of 16 April 2026 [P0023].
- **Employer confirmation:** within 15 days of being told the visa checks are finished (new TUI art. 22(5-quinquies)); otherwise the request counts as refused and the nulla osta is revoked [P0024, P0025]. **Confirms** W0039.
- **New:** the employer must promptly tell the worker of every communication it receives about the nulla osta [P0026]. Useful for Step 3/5 ("ask your employer to forward every SUI message").
- **Contract of stay:** signed within 15 days of entry (was 8), and sent online to the SUI within the same 15 days [P0027, P0028]. **Confirms** W0019 and W0041. **Contradicts** the brief's "within 8 days" and older integrazionemigranti text.
- Both steps can be done through labour consultants (Law 12/1979) or the main employer organisations [P0029]. Housing for workers in hotels or construction-site dormitories: circular 9859 of 15 Dec 2025 and art. 4 of Law 182/2025 [P0030]. No change in ATECO sector codes [P0031].
- **Not in the circular:** no word on Bangladesh, Pakistan, Sri Lanka, "high-risk" countries or extra checks on their nulla osta.

### 2. gu-dl-146-2025: Decree-Law 146 of 3 October 2025, original text (GU n. 230), official, possibly-outdated (13 months old, and amended on conversion)

- In force 4 October 2025; aims include fighting caporalato and illegal recruitment of foreign workers [P0032, P0033].
- The nulla osta time limit now runs from the date the request is **assigned to the quota**, not from submission [P0034].
- Truthfulness checks on employer declarations for out-of-quota (art. 27) authorisations [P0035].
- **Pre-filling is mandatory** before click day, with truthfulness checks when the user logs in to pre-fill [P0036, P0037].
- **A private employer may file at most 3 nulla osta requests a year**; the limit does not apply through employer organisations or labour consultants, who must keep numbers proportional to the firm's turnover, staff and sector [P0038, P0039]. Useful for N (How a job reaches you): it targets the one-employer-many-nulla-osta fraud.
- **Work while the permit is pending:** a foreigner waiting for issue, renewal or conversion may stay and work, even past 60 days, with the post-office receipt, until police notify a reason to refuse [P0040, P0041]. Useful for W (Your residence permit) and L.
- Art. 18 special permit (victims of violence or exploitation, used in caporalato cases) lasts one year, up from six months; holders can get the assegno di inclusione [P0128, P0042]. Useful for D (caporalato).
- **Out-of-quota care workers** for the very elderly and people with disabilities (DL 145/2024 art. 2) extended to each year 2026-2028 [P0043]. Useful for D.
- **Family reunification:** the SUI deadline rises from 90 to 150 days [P0044]. **Official Gazzetta confirmation of F0020**, which rested on Normattiva and Brocardi.
- Lampedusa hotspot measures extended to 31 Dec 2027 [P0045].
- **On Bangladesh and high-risk countries:** the original text (arts. 1-12) has **no** rule on Bangladesh, Pakistan, Sri Lanka or high-risk countries, and does not extend DL 145/2024 art. 3. **No 15-day rule either**: the 15-day confirmation and contract deadlines came on conversion (Law 179/2025) or with D.Lgs. 83/2026, as circular 7185 says [P0023]. Seasonal work is not mentioned separately, beyond pre-filling applying to seasonal requests too [P0036]. I logged no fact for the absence.

### 3. interno-cruscotto-2024-12-31: UNHCR Italy sea arrivals dashboard, December 2024 (11 April 2025), unofficial

- 66,617 sea arrivals in 2024, 58% fewer than the 157,651 of 2023 [P0046]. **Matches** U0006.
- **Bangladesh ranked first, with 21% of arrivals**, ahead of Syria (19%) and Tunisia (12%) [P0047]. Over 14,200 Bangladeshis arrived, up 12% on 2023 [P0048]. **Conflicts** with U0007 (Ministry: 13,779). Bangladesh is first either way.
- UNHCR links the rise to smuggling businesses that fly people into Benina (Benghazi) airport; Asians fly to Benghazi and then move to Tripolitania to embark [P0049, P0050]. **Confirms** U0065/U0066 (flight to Benghazi).
- Top nationalities on the Libya route: Bangladesh, Syria, Egypt, Pakistan, Eritrea [P0051]. In December 2024 Bangladeshis were 40% of all arrivals and 50% of departures from Libya [P0052, P0053].
- **Deaths:** 1,718 dead or missing on the central Mediterranean in 2024, one for every 39 arrivals (1 in 83 in 2023); IOM data, not broken down by nationality [P0054]. Partly answers U's question on deaths (2024 only, all nationalities).
- Lampedusa took over 45,500 arrivals (68%); 63% left from Libya (42,279) [P0055, P0056]. Bangladeshis were the top unaccompanied-child nationality in December 2024 (55 of 272) [P0057].

### 4. interno-cruscotto-2025-12-31: UNHCR Italy sea arrivals dashboard, December 2025 (6 March 2026), unofficial

- 66,316 sea arrivals in 2025 [P0058]; **Bangladesh first with 20,259**, about twice Egypt (second) [P0059]. **Conflicts slightly** with U0005/U0006 (Ministry: 20,164 of 66,296). For the doc, use U's Ministry figures (official); the rank is the same.
- December 2025: Bangladeshis were 31% of arrivals (30% in November) and 39% of departures from Libya [P0060, P0061]. 88% of 2025 arrivals left from Libya (58,408 in 1,103 landings) [P0062]. 18% were unaccompanied children, 74% adult men; Bangladeshis were the second unaccompanied-child group in December (99 of 506) [P0063, P0064].

### 5. unhcr-sea-arrivals-dashboard-2025-08: UNHCR Italy sea arrivals dashboard, August 2025 (24 October 2025), unofficial

- Publisher confirmed: UNHCR, "All data are based on official Ministry of Interior figures shared with UNHCR … provisional" [P0071].
- January-August 2025: 42,693 arrivals (+2%); **Bangladesh first with 13,148** [P0065, P0066]. August: 21% Bangladeshi (33% in July); 26% of departures from Libya (37% in July) [P0067, P0068]. 88% from Libya [P0069]. 122 Bangladeshi unaccompanied children arrived in August, third after Egyptians and Eritreans [P0070].
- **Deaths:** this dashboard has no death figures.

### 6. interno-avr-2026: Interior Ministry decree of 28 May 2026 (Department for Civil Liberties and Immigration), official, verified

What it is: a decree extending the FAMI 2021-2027 "system action" for assisted voluntary return and reintegration (RVA&R). It is not a public information page.
- **Who runs it:** one project only, run by **IOM (OIM)**, worth EUR 14,999,999.99, planned for 36 months from 2 January 2024 [P0072, P0073, P0129, P0074]. **Answers U's "Which organisation runs AVR from Italy in 2026"**: IOM, for the national programme. Contacts are still missing.
- **Deadlines:** counselling, pre-departure and return assistance run until **2 February 2027**; reintegration and monitoring until **2 August 2027**; the project now lasts 43 months [P0130, P0076, P0082]. So the current programme stops taking departures on 2 Feb 2027, and there is no word yet on a successor.
- **Cash grant:** reintegration grants are paid in goods and services; from this decree they **may also be paid by money transfer or in cash**, if traceable [P0077, P0078]. **No amount** is given, so the EUR 615 in U's question is still unconfirmed.
- **Applying:** Decree-Law 55 of 24 April 2026 pays a mandated representative who helps a migrant apply, at the end of the procedure [P0079] (matches U's note on DL 55/2026). The FAMI project PROG-1174 "F.A.S.T.E.R." gives local counselling before departure and for reintegration [P0080]. **No application route, phone or office** is in the decree.
- Context: the Ministry wants more voluntary departures to free reception places for the EU Pact border procedure (Regulation 2024/1348, capacity due 12 June 2026); progress was "limited" at 30 June 2025 [P0081, P0075]. Signed 28 May 2026 [P0083].

### 7. interno-it-decreto-flussi: Interior Ministry "Entry mode" page (English version), undated, possibly-outdated

General rules: a passport and an entry visa from the Italian embassy; short visas up to 3 months; overstaying makes a person irregular and leads to expulsion; expulsion orders are issued by the Prefettura and carried out by the Questura; no re-entry without authorisation until the ban ends [P0084-P0088]. Work entry stays within the flow-decree quotas, which usually reserve places for countries with entry and readmission agreements [P0089, P0090]. Useful for L (What can get you jailed or deported) and N (Bangladesh's reserved quota is tied to readmission cooperation, N0027). No dates, numbers or Bangladesh-specific content.

### 8. vfs-italy-bd-family-reunion-checklist: VFS family reunion checklist, "Update 02/12/24", possibly-outdated (superseded)

Documents [P0091-P0105]:
- Schengen D-type form, original, in English or Italian, signed (both parents sign for a minor) [P0091].
- 2 identical ICAO photos, 4.0 x 3.5 cm, white background, taken within the last 6 months [P0092].
- Passport valid 3 months beyond the visa, with 2 blank pages, plus a copy of the bio page [P0093].
- A copy of the SUI's nulla osta notice; check that the name, surname, sex and date of birth are right [P0094].
- A one-way flight booking with PNR [P0095].
- **Spouse:** nikahnama and marriage certificate in Bangla and English with columns 12 and 24, volume, page and serial number; a talaknama if either spouse married before; legalised by MOFA **and** the Embassy [P0096-P0098].
- Family certificate from the chairman or commissioner [P0099].
- **Minors:** both parents' consent, copies of the parents' passports, the birth certificate, and court papers for a guardian [P0100].
- **Optional:** copies of all the Italy-based spouse's passports since the wedding, the witnesses' IDs, and the witnesses' Italian permits for phone or video marriages [P0101, P0102].
- Eligible relatives [P0103] (**confirms** F0079). Legalisation at the Embassy together with the visa application, for the visa fee plus legalisation fees [P0104] (same as F0082, old procedure). The Embassy may ask for more [P0105].

The two-step legalisation is **superseded** by the apostille (F0068, P0106).

### 9. vfs-italy-bd-family-sui-bn: VFS "FAMILY-SUI updated" checklist (English, Italian, Bangla), undated (after 19 May 2025), possibly-outdated

- Same structure as file 8, but every document is **original and apostilled**: nikahnama and marriage certificate, the other-faith marriage certificate, the family certificate, the child's birth certificate, consent and court papers [P0106-P0109].
- **Only one apostille per document** [P0110].
- Applicants are personally responsible for the authenticity of every document (Embassy communique of 19 May 2025) [P0111, P0112].
- **No applicant may file two visa applications at once, even with two passports** [P0113] (a scam "tried by workers", for F/N/V).
- **Confirms** F0068 and F0151 (apostille replaces legalisation). The Bangla text layer is empty, so only the English and Italian could be quoted [P0114].

### 10. vfs-italy-bd-selfemployment: VFS self-employment checklist (consultants or officers of existing companies), undated, possibly-outdated

Documents [P0115-P0127]:
- National D-type form; 2 photos [P0115].
- Passport valid 3 months after leaving Schengen, with 2 blank pages, and a copy of **all** pages [P0116].
- A **Questura nulla osta issued within 120 days** before applying [P0117, **conflict** with W0121: the Embassy's July 2026 checklist says 90 days].
- A Direzione Provinciale del Lavoro certificate that the contract is not employment [P0118].
- A Chamber of Commerce certificate that the company has been active for 3 years [P0119] (**confirms** W0122), and its visura camerale (registration extract) [P0120].
- A legal representative's guarantee of pay of at least **EUR 8,400** [P0121, **conflict** with W0123: EUR 8,500 in July 2026; keep W's].
- The last balance sheet or tax return [P0122].
- 6 months of bank statements from a bank in Bangladesh [P0123] (**confirms** W0124).
- Housing: a purchase or rental contract, or a Law 15/1968 declaration from an Italian or a legal resident, with a copy of their ID [P0124].
- Schengen travel insurance of EUR 30,000 covering the first 3 months [P0125].
- Civil-status papers in English: nikahnama or marriage act, talaknama, or the spouse's death certificate [P0126].
- A flight booking [P0127].

The items new to W are the Direzione Provinciale del Lavoro certificate, the visura camerale, the balance sheet, housing and insurance.

## b. Which open questions these files answer

**N (Status) and W (Step 3):**
- "Was the Bangladesh/Pakistan/Sri Lanka check of DL 145/2024 (INL verification, no silent consent) extended into 2026, or replaced by a Foreign Ministry high-risk list?" (N, W lines 61-62): **NOT answered.** Neither the original DL 146/2025 nor circular 7185 mentions Bangladesh, high-risk countries or extra checks. Indirectly, DL 146 makes truthfulness checks universal at pre-filling [P0037], caps private employers at 3 requests [P0038], and lets the INL check pre-filled forms early [P0010]. These apply to all nationalities and are not a Bangladesh-specific rule. Still needed: Law 179/2025 (the conversion law) on the Gazzetta, or Normattiva's DL 145/2024 art. 3 "vigente al 10/11/2026", and any MAECI (Foreign Ministry) decree listing high-risk countries.
- "What is Bangladesh's reserved quota 2026-2028?": **not answered**; the circular only says the reserves are unchanged [P0006].
- 2027 click days and pre-filling: **confirmed** on the official circular PDF [P0007, P0013, P0016-P0021]. W's draft can cite P ids alongside W0005-W0014.

**W:**
- Contract of stay in 15 days and employer confirmation in 15 days: **confirmed** [P0024, P0025, P0027, P0028]. Also new: the employer's duty to pass every communication on to the worker [P0026].
- Self-employment: two conflicts with W's July 2026 Embassy checklist (P0117 against W0121, P0121 against W0123). W's newer figures stand, plus 5 more required documents.
- None of W's insider questions (VFS charge, processing days, the kit fee and so on) is answered.

**F:**
- 150-day SUI deadline: **confirmed** on the Gazzetta [P0044] (F0020).
- Eligible relatives: **confirmed** [P0103] (F0079).
- Apostille instead of legalisation: **confirmed** [P0106-P0110] (F0068, F0151); one apostille per document [P0110].
- New for Step 5/Scams: no two simultaneous applications, even with two passports [P0113]; check the personal data on the nulla osta before applying [P0094].
- **Not answered:** the MOFA apostille fee; whether the e-apostille is accepted; DNA tests; processing times.

**U (Irregular routes, Going home without valid papers):**
- "Which organisation runs AVR from Italy to Bangladesh in 2026?": **partly answered**: the national FAMI programme is run by IOM until 2 Feb 2027 (departures) and 2 Aug 2027 (reintegration) [P0129, P0130, P0076]. Phone numbers and offices are not in the file.
- "How much is the AVR cash grant?": **not answered**; the grant can now be paid in cash or by money transfer [P0078], but no amount is given.
- "How does one apply?": partly: through a mandated representative, paid under DL 55/2026 [P0079], with local F.A.S.T.E.R. counselling [P0080].
- Sea arrivals: Bangladesh was the first nationality in 2024 and 2025 and in January-August 2025 [P0047, P0059, P0066]. UNHCR totals differ slightly from the Ministry's (P0048 against U0007; P0058 and P0059 against U0005 and U0006). Keep the Ministry figures in the doc.
- Benghazi flight route: **confirmed** by UNHCR [P0049, P0050].
- Deaths: 1,718 in 2024, all nationalities [P0054]. Still missing: Bangladeshi deaths and 2025-2026 figures.

## c. Still to get (not in these files)

- Law 179 of 1 December 2025 (conversion of DL 146/2025), Gazzetta Ufficiale, to check for any Bangladesh or high-risk-country clause → `gu-legge-179-2025.pdf`.
- Normattiva DL 145/2024 art. 3 "vigente al 10/11/2026" → `normattiva-dl-145-2024-art3-2026`.
- A MAECI decree on high-risk countries, if one exists.
- IOM Italy's AVR page with contacts and the grant amount (italy.iom.int, "ritorno volontario assistito").
- The real interno.gov.it cruscotto PDFs are already with U, so there is no need to re-download them.

## d. Insider questions (still open)

- Was the DL 145/2024 extra check on Bangladeshi nulla osta extended past 31 Dec 2025 by Law 179/2025 or a later act, and is Bangladesh on a Foreign Ministry high-risk list?
- How many of the 2027 reserved non-seasonal places (inside the 25,000 for agreement countries) go to Bangladesh?
- What is IOM Italy's AVR phone number and office for Bangladeshis in Rome and Milan, and how much is the 2026 reintegration grant (cash or in kind)?
- Will a new AVR programme replace the IOM project after 2 February 2027?
- How many Bangladeshis died or went missing on the central Mediterranean in 2024-2026?
