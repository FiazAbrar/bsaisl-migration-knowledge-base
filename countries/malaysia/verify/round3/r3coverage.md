# r3coverage: coverage check of malaysia.src.md against IMI's list of visas and passes (round 3)

Checked on 7 Nov 2026 against malaysia.src.md (447 lines), ledger.csv part C (C0001-C0048) and the raw files: imi-en-types-of-visas.txt, the IMI menu in imi-ikad-collection.txt, myvisa-home-fc.md, myvisa-faq.md, myvisa-js-bangladesh-notice.md and the IMI pass pages in raw/ (imi-ltsvp.md, imi-residence-pass.md, imi-permit-masuk.md, imi-documents-by-category.md, imi-client-charter.md, imi-pvip-faq.txt, imi-faq-plsxpats.md). I also searched the ledger for official rows the doc does not cite, where they answer an item on the audit list. Nothing was fetched, and malaysia.src.md was not edited. The round 2 fixes (verify/round2/fixlog2.md) are in the doc, and none of the round 2 gaps reappear.

Key: **own** = own H2/H3 section. **mention** = named inside another section. **table** = in "Visas not open to Bangladeshis". **gen** = answered once for every visa by a general section (Asylum, Having a child). **NtK** = a "Need to know" is in the doc.

## 1. IMI visa and pass types: coverage and status for Bangladeshis

| # | IMI visa / pass / service (source) | Where in doc | Status for Bangladeshis stated and cited? | Verdict |
|---|---|---|---|---|
| 1 | Single Entry Visa (C0002) | own: Tourist L222-259 | Yes [V0001, V0009, R0005] | PASS |
| 2 | Multiple Entry Visa (C0003, C0007) | table L21; Tourist L224; Business L272 | NtK [V0009, Z0016] | FAIL minor (G1): IMI's own page on social-visit MEVs (only Indian and Chinese citizens) is left out of the L224 conflict |
| 3 | Transit Visa (C0004) | own: Transit L287-291 | Yes: RM20 [V0017]; New Delhi rule plus an NtK [V0081] | PASS |
| 4 | eVISA VTR / VDR options (C0005, C0006) | Tourist; Family visit L267 | Yes | PASS |
| 5 | VDR / eVDR (C0008, C0039, C0044, C0045) | PLKS Step 3; own: Family visit L261-268 | Yes [V0089] | PASS (fees gap G3) |
| 6 | eVOA / visa on arrival (C0009) | table L19 | Yes (China and India only) | PASS |
| 7 | eNTRI (C0010) | table L18 | Yes (India only) | PASS |
| 8 | MACS (C0011) | Other passes L368 | Yes: a facility, not a pass, and a visa is still needed [C0011, Z0044] | PASS |
| 9 | PLKS (C0012) | own: L31-169 | Yes [W0041, W0042] | PASS |
| 10 | Employment Pass (C0013) | own: L293-312 | NtK on nationality [E0045] | PASS (where-to-apply gap G6) |
| 11 | Social Visit Pass, short term (C0014) | Tourist, Business | Yes | PASS |
| 12 | Long-Term Social Visit Pass and its categories (C0015-C0020, Z0029, E0137) | Family passes L318, L327, L335; Other passes L367 | All categories on imi-ltsvp.md are covered (child of a citizen aged 7 or under, aged 60+, student's family, spouse of a citizen, abused, divorced or widowed wife, medical, wife of a PR, expatriates awaiting PR) | PASS (requirement gaps G11, G20) |
| 13 | Professional Visit Pass (C0021, C0022) | own: L283-285 | NtK on nationality; the bond table has a Bangladesh rate [V0112] | PASS (gaps G5, G18) |
| 14 | PVP-Expert (C0023) | mention L285 | as PVP | PASS |
| 15 | Student Pass (C0024) | own: L175-220; school level L208 | Yes | PASS (gap G8) |
| 16 | Residence Pass (C0025) | mention L331 | Categories listed, no nationality bar | PASS (gaps G10, G19) |
| 17 | Border Pass, Malaysia-Indonesia / Malaysia-Thailand (C0026) | table L26 | NtK on eligibility | PASS |
| 18 | Foreign Domestic Helper (C0027) | table L23; own: L171-173 | Yes, not a source country | PASS |
| 19 | Entry Permit (PR) and REP guideline (C0028) | L329, L367 | Categories listed; NtK on criteria | FAIL minor (G12); UNSUPPORTED (G22) |
| 20 | Section 66 endorsement (C0029) | table L29 | Yes | PASS |
| 21 | APEC Business Travel Card (C0030) | table L27 | Yes | PASS |
| 22 | Special Programme: Work & Holiday (C0031) | table L28 | Yes | PASS |
| 23 | Ship crew / seaman (C0032, C0033) | Transit L291 | Yes, a transit visa is needed [V0002] | PASS |
| 24 | PVIP (C0034-C0037) | Other passes L365 | Yes, no nationality bar [C0037] | PASS (gaps G13, G21) |
| 25 | PLS@XPATS (C0038, C0048) | Other passes L366; Changing L375 | NtK on eligibility | PASS (gaps G14, G23) |
| 26 | Special Pass / Pas Khas (C0040, C0046) | Going home L405-406 | Yes | PASS |
| 27 | Dependant Pass (C0041) | Family passes L318 | Yes | PASS (gap G7) |
| 28 | Graduate Pass (C0042) | table L24 | Yes, not eligible | PASS |
| 29 | MDAC (C0043) | PLKS L92, Student L202, Tourist Step 4, EP L306 | Yes | PASS |
| 30 | MM2H (IMI menu) | own: L345-354 | Yes [E0100] | PASS |
| 31 | Investor Pass (E0073) | Other passes L364 | NtK | PASS |
| 32 | Residence Pass-Talent | Other passes L362 | NtK | PASS |
| 33 | i-Kad (imi-ikad-collection) | PLKS Step 7 L95 | Yes | PASS |
| 34 | DE Rantau, medical, business (addendum) | own sections | Yes | PASS (gaps G9, G4, G17) |
| 35 | G2G recruitment (addendum) | BOESL route L35, L41; the term "G2G" is never used | Government route stated [W0001] | FAIL minor (G16) |
| 36 | IMI travel documents (Certificate of Identity, restricted travel documents, document in lieu, emergency certificate SPC) | not covered | Issued to Malaysians or residents, not passes for Bangladeshi visitors | n/a |
| 37 | "Death and Critically Ill Emergency Visit" notice (imi-notice-death-emergency-visit.md) | not covered | A 2021 COVID-era notice that points to Singapore's DCEV scheme | n/a |

## 2. Audit matrix per visa section (CLAUDE.md audit list)

"OK" = answered with a citation or an explicit NtK. Claim asylum and have a child are answered once for every visa by the Asylum and Having a child sections ("gen").

| Section | Types | Requirements | Where | Cost | Time | Appeal | Scams done to migrant | Scams tried by migrant | Work | Asylum | Child | Spouse |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PLKS | OK | OK | OK | OK + NtK | OK | NtK | OK | OK + NtK | OK | gen | NtK + gen | OK (no) |
| Student | OK | OK | OK | OK | OK | NtK | OK + NtK | OK | OK | gen | OK | FAIL (G8) |
| Tourist | FAIL minor (G1) | OK | OK | OK | OK | OK + NtK | OK | FAIL (G2) | OK | gen | gen | OK (NtK) |
| Family visit VDR | OK | OK | NtK | FAIL (G3) | OK | NtK | NtK | OK | OK | gen | gen | n/a |
| Business | OK | OK | OK | OK | OK | OK | NtK | OK | OK | gen | gen | UNSUPPORTED (G17) |
| Medical | FAIL minor (G4) | OK | OK | OK | OK | OK | NtK | NtK | OK | gen | gen | OK (companions) |
| PVP | OK | FAIL (G5) | OK | OK | UNSUPPORTED (G18) | OK | NtK | OK | OK | gen | gen | OK (no) |
| Transit | OK | OK | OK | OK | OK | OK | n/a | n/a | n/a | gen | n/a | n/a |
| Employment Pass | OK | OK | FAIL minor (G6) | OK | OK | OK | NtK | OK | OK | gen | gen | OK |
| EP family | OK | OK | OK | OK | OK | NtK | NtK | NtK | NtK (conflict shown) | gen | gen | OK; duration / conflict FAIL (G7) |
| Spouse of a citizen | OK | OK | OK + NtK | NtK | OK | NtK | NtK | OK | OK | gen | gen | n/a |
| Residence Pass (L331) | OK | FAIL (G10) | OK | OK | UNSUPPORTED (G19) | UNSUPPORTED (G19) | UNSUPPORTED (G19) | UNSUPPORTED (G19) | OK | gen | gen | NtK |
| Other relatives (LTSVP) | OK | FAIL (G11) | UNSUPPORTED (G20) | NtK | OK | NtK | NtK | OK | UNSUPPORTED (G20) | gen | gen | n/a |
| MM2H | OK | OK | OK | OK + NtK | NtK | OK + NtK | NtK | OK | OK | gen | gen | OK |
| DE Rantau | OK | FAIL (G9) | OK | OK | OK | OK | NtK | NtK | OK | gen | gen | FAIL (G9) |
| RP-T / MTEP / Investor | OK | partial | NtK | partial | NtK | NtK | NtK | NtK | OK | gen | gen | partial |
| PVIP | OK | OK | OK | OK | UNSUPPORTED (G21) | UNSUPPORTED (G21) | FAIL (G13) | FAIL (G13) | OK | gen | gen | OK |
| PLS@XPATS | OK | FAIL (G14) | NtK | NtK | OK | UNSUPPORTED (G23) | UNSUPPORTED (G23) | UNSUPPORTED (G23) | OK | gen | gen | n/a |
| Entry Permit (PR) | FAIL minor (G12) | NtK | UNSUPPORTED (G22) | UNSUPPORTED (G22) | UNSUPPORTED (G22) | UNSUPPORTED (G22) | n/a | OK (withdrawal [E0135]) | n/a | gen | FAIL (G15) | OK (categories) |
| Changing visa type (L370-382) | OK: all routes with sources are present, and the open ones are NtKs | | | | | | | | | | | |
| Asylum (L384-386) | OK: written to discourage (no legal status, arrest and deportation, long waits, duty to tell the truth, full fees for pregnant asylum seekers, paid "help" is a lie) | | | | | | | | | | | |
| Corridor (L430-436) | OK: numbers; comparison NtK plus unofficial A0070; bans and past stops with an NtK; growth (CLAB, DHL, minimum wage) with an NtK | | | | | | | | | | | |

## 3. Remaining gaps (FAIL and UNSUPPORTED only)

### FAIL: missing although a ledger row or raw source exists

- **G1** L224 | FAIL | conflict-hidden | "**Need to know:** whether a Bangladeshi tourist can still get a multiple-entry visa." | cited: V0009, Z0016 | source says: "Citizens of India and the People's Republic of China who wish to enter Malaysia for the purpose of a Social Visit are eligible to apply for the Multiple Entry Visa." (imi-en-types-of-visas.txt; ledger V0072 and C0003, but neither quote covers this sentence, so extend one) and, from news, "Bangladeshi tourists will generally receive single-entry visas instead of one-year multiple-entry social visit visas." (news-observer-mev-limit-2026-09.md, V0108, lead) | fix: add "IMI's undated Types of Visas page offers social-visit multiple-entry visas only to Indian and Chinese citizens [V0072]; a Sep 2026 news report says Bangladeshi tourists will get single-entry visas (unofficial, not verified) [V0108]," and keep the Need to know.
- **G2** L253-259 | FAIL | partly-supported | Tourist "Scams" / "Don't work" has no scam tried by the applicant (false documents or statements to get the visa) | cited: V0046, V0100, V0047 | source says: getting a pass by a false statement is an offence, fine up to RM10,000 or up to 5 years' jail (K0031, K0030; already cited for Business, VDR, Student and EP) | fix: "Getting a pass for yourself or someone else by a false statement is an offence, with a fine up to RM10,000 or up to 5 years' jail [K0031, K0030]."
- **G3** L267 | FAIL | partly-supported | "**Need to know:** the fees, whether a refusal can be appealed" | cited: C0006 | source says: "RM 20" visa fee for Bangladesh (IMI fee table, V0017), and Bangladesh's bond rate "RM 750 - Bangladesh" (imi-security-bond-rates.md, V0112, whose claim names VDR) | fix: "The visa fee is RM20 for a Bangladeshi [V0017]; Need to know: whether the RM105 eVISA processing charge [V0016] and a RM750 bond [V0112] apply to a social VDR."
- **G4** L274-281 | FAIL (minor) | partly-supported | Medical visit doesn't mention the long-term route for longer treatment | cited: V0073-V0077 | source says: "Terhad kepada rawatan di Hospital kerajaan / Hospital pakar sahaja" (LTSVP for treatment, one companion; imi-ltsvp.md, C0018, now cited only under Other relatives) | fix: "For longer treatment at a government or specialist hospital, IMI gives a Long-Term Social Visit Pass with one companion (see Family passes) [C0018]."
- **G5** L285 | FAIL | partly-supported | PVP requirements: "Only a registered Malaysian sponsor (a company, organisation or institution) can apply, mainly through its account with ESD" (it doesn't say the sponsor needs the Labour Department's prior approval) | cited: V0092, V0094 | source says: "From 1 July 2025 new EP and PVP applications need JTKSM prior approval under Section 60K ... and a MYFutureJobs advertisement acknowledgement" (E0050; also "All applications of EP and PVP are presented to the" Expatriate Committee, E0049). V0097: "Organizers of any professional training programmes to be held in Malaysia must apply for the relevant professional training pass prior to the entry of the applicant" (kln-mhc-dhaka-faqs.md) | fix: add "As for the Employment Pass, the company first needs the Labour Department's section 60K approval and a MYFutureJobs advert acknowledgement [E0050]; for a training programme the organiser applies for the pass before you travel [V0097]."
- **G6** L295, L303 | FAIL (minor) | partly-supported | "only the employer can apply" / "The employer registers with ESD" (doesn't say that some sectors go to other approving authorities) | cited: E0002, E0006, E0011, E0016 | source says: "Expatriate Employment Pass applications in the following sectors or regions will still be under the purview of the following Approving Authorities:" MIDA (manufacturing), MDEC (ICT), Bank Negara (banking and finance), Securities Commission, Public Services Department, ECERDC and IRDA (esd-myxpats-key-services.md, E0007; C0013 "approved by the Expatriate Committee or the relevant regulating agency") | fix: add one sentence [E0007, C0013].
- **G7** L318 | FAIL | conflict-hidden | "From 1 June 2026 a spouse and children under 18 get a Dependant Pass; parents, parents-in-law, children aged 18 to 25 and a common-law spouse get a Long-Term Social Visit Pass (LTSVP) [E0014]." The section also never says how long these passes last | cited: E0014 | source says: "Duration of pass is based on the principal applicant." (esd-ltsvp.md, E0147) vs "Note: maximum duration of LT-SVP approval is 12 months" (esd-payment-table-v13.txt, E0148): both official and marked conflict in the ledger. ESD's EP page still lists parents under the Dependant Pass (esd-employment-pass.md, E0149/E0036, marked conflict) | fix: "ESD's LTSVP page says the pass lasts as long as the principal's [E0147], while its payment table caps LTSVP approval at 12 months [E0148]; Need to know: which applies." Note that ESD's older EP page still lists parents for a Dependant Pass [E0149], and that the 2026 policy is the newer rule [E0014].
- **G8** L216 | FAIL | partly-supported | "IMI allows dependants ... only for master's and PhD students [S0008, S0009, S0010]" (no word on where a Bangladeshi postgraduate's family applies or what it costs) | cited: S0008-S0011, S0038 | source says: "Permohonan hendaklah dikemukakan melalui Sistem STARS, Education Malaysia Global Services (EMGS)." (imi-student-pass.md, S0021); "Dependant Processing Fee 250 140 Dependant to procure own insurance policy" (emgs-schedule-fees-student-dependant.txt, S0067, verified) | fix: "A master's or PhD student's dependants apply through EMGS's STARS system [S0021]; EMGS charges RM250 per dependant (RM140 to renew), and each dependant buys their own insurance [S0067]."
- **G9** L358 | FAIL | partly-supported | DE Rantau: "You need an income of more than USD 36,000 ..." and "plus RM540 per dependant" (no other requirements; who counts as a dependant isn't said) | cited: E0085, E0091 | source says: "Husband / Wife/ Common-Law partner." ... "Special needs child (no age limit)" (mdec-derantau-faq-v11.txt, E0087: spouse or common-law partner, children under 18, special-needs children, parents); passport validity "fourteen (14) months" (E0096); "Letter of Good Conduct ... Issued by the relevant authority in your country", highest education certificate and medical insurance (mdec-derantau-docs-remote.txt, E0097, possibly outdated) | fix: add the dependants list [E0087], passport valid more than 14 months [E0096], and the document list [E0097]. The Letter of Good Conduct links to the Bangladesh police clearance steps in PLKS Step 4 [B0105].
- **G10** L331 | FAIL (minor) | partly-supported | Residence Pass: what to bring isn't said | cited: E0131, E0132, Z0018, E0133, Z0049, Z0048 | source says: "Borang IMM 16A", "Gambar Berukuran Pasport – 2 Keping", "Salinan Kad Pengenalan Penaja", "Setiap salinan dokumen yang dikeluarkan daripada negara asal pemohon hendaklah mendapat pengesahan daripada kedutaan negara masing-masing", plus the multiple-entry visa fee by country (imi-residence-pass.md; no ledger row for these lines) | fix: log a ledger row, then add "Bring Form IMM 16A, 2 passport photos, old and new passports, the sponsor's ID card copy and the relationship documents; documents from Bangladesh must be attested by the Bangladesh High Commission; a multiple-entry visa fee is added."
- **G11** L335 | FAIL (minor) | partly-supported | "Bring originals of all documents; only complete applications are accepted [C0016]." (the forms and bond aren't listed) | cited: C0015-C0020, Z0029 | source says: for these categories "Borang Imm.12 / Imm.55", "Borang Imm.38", "Borang Personal Bond (dimatikan setem hasil RM10.00)", "Akuan Penaja", sponsor's ID card and income proof (imi-ltsvp.md; imi-documents-by-category.md; no ledger row for the forms) | fix: log a row, then add "Forms Imm.12 (or Imm.55) and Imm.38, a personal bond stamped RM10, the sponsor's sworn declaration, ID card and proof of income."
- **G12** L367 (and L329) | FAIL (minor) | partly-supported | Permanent residence doesn't mention IMI's separate Returning Expert Programme (REP) guideline | cited: E0134, Z0050, C0028 | source says: "Garis Panduan Permohonan Permit Masuk Di Bawah Kategori Returning Expert Programme (REP)" (imi-permit-masuk.md; in the C0028 claim). The guideline PDF (imi-permit-masuk-rep-guideline.pdf) has no text layer (the .txt is 40 bytes), and I couldn't render it here because pdftoppm isn't installed | fix: "IMI also publishes an Entry Permit guideline for its Returning Expert Programme [C0028]; Need to know: whether it covers a Bangladeshi spouse or child of a returning Malaysian expert."
- **G13** L365 | FAIL (minor) | uncited | PVIP: no scams either way, though the FAQ sets rules for agents | cited: C0034-C0037, Z0052-Z0055 | source says: "Agents can only act on behalf of clients who have been given power of attorney in writing to represent them." and agent companies "cannot be directly involved in the activities of fraud" (imi-pvip-faq.txt lines 68, 139-143; no ledger row) | fix: log a row, then add "An agent may act for you only with your written power of attorney [new id]; Need to know: any official warning about PVIP scams."
- **G14** L366 | FAIL (minor) | partly-supported | "**Need to know:** who is eligible and the fee (IMI's FAQ page for it saved empty)." | cited: C0038, C0048 | source says: "Permohonan bagi tugasan kecemasan boleh dipertimbangkan melalui kemudahan PLS@EXPATS tertakluk kepada jenis insiden, keperluan sebenar dan dasar semasa." (esd-pvp-faq.txt, E0071, verified) | fix: "ESD's PVP-Expert FAQ says emergency work can be considered under PLS@XPATS, depending on the incident [E0071]," and keep the Need to know on eligibility and the fee.
- **G15** L391 | FAIL (minor) | partly-supported | "a child born in Malaysia is a citizen by law if at least one parent is a Malaysian citizen or permanent resident at the time of birth [K0001, K0002]" | cited: K0001, K0002, Z0051 | source says: Act A1752, "not yet in force", substitutes "a citizen" for "either a citizen or permanently resident in the Federation" (federal-constitution-en.txt, K0005, verified); and citizenship decisions of the Federal Government cannot be appealed or reviewed in any court (K0006) | fix: add "A 2025 amendment, not yet in force on 30 Nov 2025, will limit this to a citizen parent [K0005]; Need to know: whether it has come into force."
- **G16** L35, L41 | FAIL (minor) | term | The addendum lists "G2G (government-to-government) recruitment", but the doc never names it, so a reader or the chatbot searching for "G2G" finds nothing | cited: W0001, W0068 | source says: "has sent only 1,381 migrants to Malaysia under the Government to Government (G2G) arrangement" (A0059, news, unofficial, 2024) | fix: in Step 1.3, "BOESL's zero-cost recruitment is the government-to-government (G2G) route; news reports say BOESL sent 1,381 workers under it from Oct 2022 to May 2024 (unofficial, not verified) [A0059]."

### UNSUPPORTED: missing, no ledger source, and no Need to know

- **G17** L270-272 | UNSUPPORTED (minor) | Business visit: bringing a spouse isn't covered | fix: "A spouse applies for their own eVISA; see Tourist visa, Step 2 [V0023]," plus the Need to know already in the Tourist section.
- **G18** L285 | UNSUPPORTED | PVP: processing time for a standard PVP through ESD isn't given. Only fast-track PVP-Expert (5 days), artistes (5) and missionaries (25) are | fix: "Need to know: how long a standard PVP takes." The raw charter also gives "Permohonan PLIK (Pas Lawatan Ikhtisas) (Manual) | 30 hari bekerja" for Sarawak (imi-client-charter.md line 103; no ledger row). Log it if used.
- **G19** L331 | UNSUPPORTED | Residence Pass: processing time, appeal if refused, and scams aren't stated, and there's no Need to know (imi-residence-pass.md doesn't give them, and the charter has no Residence Pass line) | fix: "Need to know: how long a Residence Pass application takes, whether a refusal can be appealed, and any official scam warning."
- **G20** L335 | UNSUPPORTED | Other relatives (LTSVP): where to apply, and whether the holder may work, aren't stated, and there's no Need to know. IMI's work-permission rules cover only a citizen's spouse (imi-ltsvp.md), and Z0046 (nearest office) is on the spouse-extension page only | fix: "Need to know: which Immigration office takes these applications, and whether these pass holders may work."
- **G21** L365 | UNSUPPORTED | PVIP: processing time for a participant and appeal if refused are missing. The FAQ gives only 30 working days for an agency's company registration (imi-pvip-faq.txt line 172) | fix: "Need to know: how long a participant's application takes and whether a refusal can be appealed."
- **G22** L329, L367 | UNSUPPORTED | Entry Permit (PR): where to apply, the fee, the processing time and appeal aren't stated. The only Need to know is "the criteria" | fix: widen it to "Need to know: the criteria, where to apply, the fee, how long it takes and whether a refusal can be appealed (IMI's e-book on Google Drive has not been saved)."
- **G23** L366 | UNSUPPORTED (minor) | PLS@XPATS: appeal and scams aren't stated | fix: add them to the existing Need to know.

## Notes (not counted)

- Table at L7-29: the addendum asks for an access-date column. The date is given once in the lead sentence ("all checked on 6 Nov 2026"), which covers it but isn't a column.
- MEV list (L21, L272): the MyVISA FAQ's only published list of 31 nationalities, those who must get an eVISA, includes Bangladesh [V0001]. The page doesn't say whether this is the same list as the 31 MEV-eligible nationalities, so the Need to know stands. It could say that only this list is published.
- E0053 (ePPAx FAQ, 2023: section 60K approval in 14 working days) vs E0016 (ESD 2026: about 10 working days), used at L303. The newer official source is used. Leave it to the number checker whether to show both.
- E0121 (IMI's older MM2H page: part-time work allowed with employer documents) vs L352 "only Platinum holders may work" [Z0019]. Older official page; the number or statement checker may want it shown as a conflict.
- E0143 (lead): Sarawak's separate S-MM2H scheme isn't mentioned. Lead only, so it could be a Need to know.
- The IMI charter gives 3 working days for an electronic Check-Out Memo (eCOM) (imi-client-charter.md line 58; no ledger row). It isn't in "Leaving at the end of the job". This isn't an audit-list item.
- V0045 (a newly approved eVISA cancels any earlier active visa) and V0044 (wrong details mean re-applying) aren't in the Tourist steps. They're useful, but not audit-list items.

Table 1: 37 IMI or addendum types checked: 32 PASS (some resting on an existing Need to know), 3 FAIL minor (MEV G1, Entry Permit REP G12, G2G G16), 2 n/a. Remaining gaps: 23 in all, 16 FAIL (G1-G16) and 7 UNSUPPORTED (G17-G23).

Checked 37 visa/pass types and 21 section rows of the audit matrix: 23 gaps reported, 16 FAIL, 7 UNSUPPORTED.
