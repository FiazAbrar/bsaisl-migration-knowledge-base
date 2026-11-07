# r2coverage: coverage check of malaysia.src.md against IMI's list of visas and passes

Checked on 7 Nov 2026 against malaysia.src.md (434 lines), ledger.csv part C (C0001-C0048) and the raw files (imi-en-types-of-visas.txt, imi-ikad-collection.txt menu, myvisa-home-fc.md, myvisa-faq.md, and the IMI pass pages under raw/). Nothing was fetched. malaysia.src.md was not edited.

Key: **own** = own H2/H3 section; **mention** = named inside another section; **table** = in "Visas not open to Bangladeshis"; **gen** = covered once by a general section (Asylum, Having a child) that applies to every visa; **NtK** = a "Need to know" is already in the doc; **FAIL** = missing although a source exists; **UNSUPPORTED** = missing, no source, and no Need to know.

## 1. IMI visa and pass types: coverage and status for Bangladeshis

| IMI visa / pass / service (source) | Where in doc | Bangladeshi status stated and cited? | Verdict |
|---|---|---|---|
| Single Entry Visa (C0002) | own: Tourist (L223-260), L239 | Yes: Bangladeshis need an eVISA, SEV [V0001, V0009, C0002] | PASS |
| Multiple Entry Visa, business / G2G (C0003, C0007) | table L21; Business L272 | NtK whether Bangladesh is among the 31 eligible nationalities [C0007, V0009] | PASS (NtK). Minor: IMI page's social-visit MEV for Indian and Chinese citizens (raw imi-en-types-of-visas.txt, C0003 page) is not in the table; Indian/Chinese exemptions are |
| Transit Visa (C0004) | own: Transit L285-289 | Yes, RM20 fee for Bangladeshis [V0017], visa needed if leaving the airport [V0079, V0080] | PASS (gap on flight change, see G8) |
| eVISA VTR / VDR options (C0005, C0006) | Tourist; VDR family L268 | Yes [V0005, C0006] | PASS |
| Visa Dengan Rujukan / eVDR (C0008, C0039, C0044, C0045) | PLKS step 3 L66-68; own: Family visit L262-268 | Yes, open to all visa-required nationals incl. Bangladesh [V0089] | PASS |
| eVOA / visa on arrival (C0009) | table L19 | Yes, China and India only [V0083] | PASS |
| eNTRI (C0010) | table L18 | Yes, India only [V0115, V0085] | PASS |
| MACS (C0011) | table L27 | Yes, a facility not a pass [C0011] | PASS |
| PLKS / Visitor's Pass (Temporary Employment) (C0012) | own: L33-170 | Yes, Bangladesh allowed in all open sectors [W0041, W0042] | PASS |
| Employment Pass (C0013) | own: L291-308 | Not stated explicitly (no nationality rule cited either way) | UNSUPPORTED (minor, G27) |
| Social Visit Pass, short term (C0014) | Tourist, Business L272 | Yes [V0001, V0068] | PASS |
| Long-Term Social Visit Pass and its categories (C0015-C0020) | Family passes L314, L322, L326 | Yes (no nationality bar on page) | PASS (category for expatriates/children approved for PR while awaiting the Entry Permit, E0137, not mentioned; minor) |
| Professional Visit Pass (C0021, C0022) | own: L281-283 | NtK whether any nationality rule applies; bond rate for Bangladesh exists [V0112] | PASS (NtK) |
| PVP-Expert (C0023) | mention L283 | as PVP | PASS |
| Student Pass (C0024) | own: L176-221; school level mentioned L209 | Yes [S0004, S0059] | PASS |
| Residence Pass (Pas Residen) (C0025) | mention L322 (widowed/divorced spouse only) | Partly | FAIL (G14) |
| Border Pass Malaysia-Indonesia / Malaysia-Thailand (C0026) | table L28 | NtK who is eligible | PASS (NtK) |
| Foreign Domestic Helper (C0027) | table L24; own: L172-174 | Yes, not a source country [L0076, L0194] | PASS |
| Entry Permit (permanent residence) and REP (C0028) | mention L357 (only "fully foreign nationals") | NtK criteria | FAIL (G13, G15): spouse/child-of-citizen categories missing. REP guideline (raw imi-permit-masuk-rep-guideline.pdf) has an empty text layer; not checked, no ledger row |
| Section 66 endorsement (C0029) | table L31 | Yes, Malaysians only | PASS |
| APEC Business Travel Card (C0030) | table L29 | Yes, Malaysians only | PASS |
| Special Programme: Work & Holiday (C0031) | table L30 | Yes, Malaysia/Australia only | PASS |
| Ship crew / seaman entry (C0032, C0033) | Transit L289 | Yes, transit visa needed [V0002] | PASS |
| Premium Visa Programme, PVIP (C0034-C0037) | Other passes L355 | Yes, no nationality bar [C0037] | PASS (gaps G23) |
| PLS@XPATS (C0038, C0048) | Other passes L356; Changing L363 | NtK eligibility | PASS (NtK) |
| Special Pass / Pas Khas (C0040, C0046) | Going home L391-392 | Yes | PASS |
| Dependant Pass (C0041) | Family passes L314 | Yes (via EP holder) | PASS |
| Graduate Pass (C0042) | table L25 | Yes, not eligible [S0044, S0073] | PASS |
| MDAC (C0043) | Tourist step 4 L248 only | Yes for visitors | FAIL for workers/students/EP holders (G7) |
| Investor Pass (E0073, E0075) | Other passes L354 | Not stated | see G26 |
| Residence Pass-Talent (E0078) | Other passes L352 | Not stated | see G26 |
| MM2H (IMI menu) | own: L336-344 | Yes, incl. Bangladesh [E0100] | PASS (gaps G5, G6) |
| i-Kad for foreign workers (imi-ikad-collection) | PLKS step 7 L96 | Yes | PASS |
| Travel documents in the IMI menu (Certificate of Identity, restricted travel documents, document in lieu, emergency certificate SPC) | not covered | These are Malaysian-issued documents, not passes for foreigners | n/a |
| Addendum items: G2G recruitment | BOESL route L37, L43 (term "G2G" never used) | Yes, BOESL zero-cost route [W0001] | PASS (only unofficial A0030/A0059 on past G2G) |
| Addendum: DE Rantau, medical, business, transit, eVISA, MM2H | own sections | Yes | PASS |

## 2. Audit matrix per visa section (CLAUDE.md audit list)

| Section (lines) | Types | Requirements | Where to apply | Cost | Processing time | Appeal if refused | Scams done to migrant | Scams tried by migrant | Can work | Asylum | Have a child | Bring spouse |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PLKS (33-170) | OK | OK | OK | OK + NtK (G19) | OK [C0045] | NtK (no source) | OK | OK + NtK | OK | gen | NtK + gen | OK (no) |
| Student (176-221) | OK | OK | OK | OK | OK | NtK (no source) | OK (unofficial) + NtK | FAIL (G21) | OK | gen | OK (pointer) | OK |
| Tourist (223-260) | OK | OK | OK | OK | OK | visa OK [V0042]; entry refusal FAIL (G20) | OK | OK | OK (no) | gen | gen | minor (G28) |
| Family visit VDR (262-268) | OK | OK | UNSUPPORTED (G10) | NtK | OK | NtK | UNSUPPORTED (G10) | FAIL (G9) | FAIL (G9) | gen | gen | n/a |
| Business (270-272) | OK | OK | OK | OK | OK | OK | UNSUPPORTED (G1) | UNSUPPORTED (G1) | OK | gen | gen | not stated (minor) |
| Medical (274-279) | OK | OK | OK | FAIL (G11) | OK | FAIL (G11) | UNSUPPORTED (G3) | UNSUPPORTED (G3) | FAIL (G11) | gen | gen | OK (companions) |
| PVP (281-283) | OK | OK | OK | OK | OK | OK [E0063] | UNSUPPORTED (G4) | FAIL (G22) | OK | gen | gen | OK (no) |
| Transit (285-289) | OK | OK | OK | OK | OK | FAIL minor (G8) | n/a | n/a | n/a | gen | n/a | n/a |
| Employment Pass (291-308) | OK | OK | OK | OK | OK | OK | NtK | FAIL (G21) | OK | gen | gen | OK (Family passes) |
| EP family (312-318) | OK | OK | OK | OK | OK | UNSUPPORTED (G5b) | UNSUPPORTED (G5b) | UNSUPPORTED (G5b) | NtK (conflict) | gen | gen | OK |
| Spouse of citizen (320-322) | FAIL (G13, G14) | OK | FAIL (G12) | NtK | OK | UNSUPPORTED (G5b) | UNSUPPORTED (G5b) | OK [E0128] | OK | gen | gen | n/a |
| Other relatives LTSVP (324-326) | OK | OK | not stated (minor) | NtK | OK | NtK | UNSUPPORTED (G5b) | UNSUPPORTED (G5b) | not stated, no source | gen | gen | n/a |
| MM2H (336-344) | OK | OK | OK | OK | NtK | FAIL (G5) | NtK | not stated (minor) | OK | gen | gen | FAIL (G6) |
| DE Rantau (346-348) | OK | OK | OK | FAIL partial (G4b) | FAIL (G2) | FAIL (G2) | FAIL partial (G2) | not stated (minor) | OK | gen | gen | OK |
| Other passes (350-357) | OK | partial | partial | partial | partial | UNSUPPORTED (G26) | UNSUPPORTED (G26) | UNSUPPORTED (G26) | partial | gen | gen | partial |
| Changing visa type (359-368) | OK + NtK; FAIL minor (G17) | | | | | | | | | | | |
| Asylum (370-372) | Written to discourage: OK; FAIL minor (G16) | | | | | | | | | | | |
| Corridor (416-422) | Numbers OK; comparison with other countries NtK; bans OK + NtK; growth NtK + FAIL (G18) | | | | | | | | | | | |

"Claim asylum" and "have a child" are answered once, for every visa, by the Asylum and Having a child sections; PLKS and Student point to them. No section-level failure is counted for these.

## 3. Remaining gaps (FAIL and UNSUPPORTED only)

### FAIL: missing although a source exists

- **G2** L348 | FAIL | DE Rantau: "**Need to know:** how long a decision takes, whether a refusal can be appealed, and any official warning about DE Rantau scams." | source exists: E0089 ("The application will be processed within six (6) to eight (8) weeks upon receipt of the completed submission."), E0093 ("No appeals will be accepted for rejected applications."), E0094 ("Neither MDEC nor any third party can guarantee approval.") (mdec-derantau-faq-v11.txt), all verified, official | fix: "A decision takes 6 to 8 weeks after a complete application [E0089]. There is no appeal; you can reapply later [E0093]. Neither MDEC nor anyone else can guarantee approval [E0094]."
- **G4b** L348 | FAIL | DE Rantau cost incomplete: only "RM1,080, plus RM540 per dependant" | source exists: E0092 (refundable bond RM750 for Bangladeshis, raw line 833), E0091 claim (immigration pass fee RM90 per 3 months or RM360 a year plus the visa, raw mdec-derantau-faq-v11.txt lines 800-802; the ledger quote of E0091 covers only the processing fee, so add the pass-fee text to the quote) | fix: add the bond and the pass fee.
- **G5** L343 | FAIL | MM2H: "**Need to know:** ... whether a refusal can be appealed" | source exists: E0102; raw mm2h-guidelines.md line 40 says "Any appeals, if any, is under the purview of the Ministry of Home Affairs." (the ledger quote stops before this sentence; extend it) | fix: "Appeals go to the Ministry of Home Affairs [E0102]." Keep a NtK on how and when.
- **G6** L338-343 | FAIL | MM2H, bring a spouse: who counts as a dependant isn't stated (only the RM2,500 fee per dependant) | source exists: E0104 (spouse, children under 21, or 21-34 if single and unemployed, disabled children, parents and parents-in-law). Note the official conflict on the child age limit: E0110/E0146 (34) vs E0111 (35, MOTAC PDF); show both | fix: add the dependant list with both official ages.
- **G7** L94-96, L201-205, L304 | FAIL | MDAC is only in the Tourist section; PLKS, Student and Employment Pass arrival steps don't say whether the worker or student must fill it in on first entry | source exists: C0043, V0058 ("All foreign nationals are REQUIRED to register"), V0060 (mandatory for all foreign citizens except, among others, PR and long-term pass holders; raw mdac-infographic-2.md) | fix: in each arrival step, "Register the MDAC within 3 days before arriving [V0058]; holders of a long-term pass are exempt on later entries [V0060]."
- **G8** L287 | FAIL | Transit: "**Need to know:** whether a Bangladeshi changing to a different flight without leaving the airport needs a visa." | source exists: V0081 (Malaysian High Commission New Delhi: "you do not need any visa during transit if your flights are booked under a single PNR and you have no plans to leave the transit hall"; separate PNRs or a KLIA-KLIA2 change need a visa), official but written for Indian travellers and possibly outdated | fix: state V0081 with "written for Indian travellers; Need to know whether the same applies to Bangladeshis". Also the eVISA refusal rule (no reasons, no published appeal [V0042]) applies to transit eVISAs and isn't stated.
- **G9** L262-268 | FAIL | Family visit (VDR): can the holder work, and scams tried by the applicant, are not stated | source exists: V0046 / V0104 (visit pass allows no work); K0031 (getting a pass by a false statement is an offence); Z0026 (sponsor's sworn declaration) | fix: "A visit on a VDR is a social visit: no work [V0046, V0104]. A false statement to get a pass is an offence [K0031]."
- **G11** L274-279 | FAIL | Medical visit: cost, appeal and work are not stated | source exists: V0016, V0017, V0019 (eVISA fees RM20 + RM105 + card/e-wallet charge, non-refundable), V0077 (MHTC Meet and Greet RM189 per companion, optional), V0042 (refusal without reasons, no appeal route), V0046 (no work on a visit) | fix: add those, cited.
- **G12** L322 | FAIL | Spouse of citizen: "**Need to know:** which Immigration office takes the application." | source exists in raw but no ledger row: imi-spouse-citizen-extension.md ("Semua permohonan pas boleh dikemukakan di pejabat imigresen berdekatan mengikut alamat kediaman pemohon", the nearest immigration office for the applicant's home address); imi-spouse-citizen-new.md (Chinese and African nationals must apply at IMI headquarters); imi-ltsvp.md line 108 (work endorsement at the Visa, Pass and Permit Division, Putrajaya, or the nearest state Immigration office) | fix: log ledger rows, then replace the NtK.
- **G13** L322, L357 | FAIL | Permanent residence for a citizen's spouse or child isn't mentioned; the PR bullet names only "fully foreign nationals" | source exists: C0028 / E0134 (Entry Permit categories: wife of a citizen, husband of a citizen, child under 18 of a citizen, fully foreign nationals) | fix: list the four categories [C0028]; keep the NtK on criteria.
- **G14** L322 | FAIL | Residence Pass: only the widowed or divorced spouse category is described | source exists: Z0018, E0131, C0025 (raw imi-residence-pass.md also lists biological, step or adopted children of citizens; parents and parents-in-law of citizens; children and spouses of permanent residents, after 5 years on a long-term pass; apply at Putrajaya HQ or the nearest Immigration office with the sponsor present) | fix: list all categories, especially the spouse of a PR.
- **G15** L357 | FAIL (partial) | PR: "**Need to know:** the criteria" | source exists: E0136 (Entry Permit points calculator at app.imi.gov.my/epc), E0135 (Entry Permit can be withdrawn if conditions are broken), E0137 (expatriates approved for PR get an LTSVP while waiting) | fix: add these; keep the NtK for the criteria themselves.
- **G16** L372 | FAIL (minor) | Asylum: scams tried by the migrant, and having a child, aren't covered | source exists: S0105 ("You have a duty to tell the truth...", coaching harms the case), S0113 (unregistered pregnant asylum seekers pay full foreigners' fees for antenatal care and birth), S0103 (no estimate of when an interview happens) | fix: add S0105 and S0113 to strengthen the discouraging message.
- **G17** L359-368 | FAIL (minor) | Changing visa type: missing routes with sources | source exists: S0141 / E0032 (an LTSVP family member must convert to a Student Pass to study and to an EP to work); E0095 (a tourist pass can't be converted to DE Rantau); S0037 (student progression, e.g. bachelor's to master's, within 3 months); E0058 (an EP application can be made while the applicant is in Malaysia; a VDR is needed only if abroad), a partial answer to the NtK at L368 | fix: add these lines.
- **G18** L421-422 | FAIL | Corridor, growth opportunities: the CLAB construction agreement isn't mentioned | source exists: W0019 (official, verified, 25 Nov 2025: agreement with CLAB signed 7 Aug 2025; demand for 500 workers, 255 visas issued) | fix: add under "Where the jobs are". The NtK on comparison with other countries could add the unofficial A0070 (Bangladeshi costs far above Indonesian or Nepali workers', unofficial, not verified) and H0006/H0007 (Bangladeshis first or second in PRM 2.0, unofficial, not verified).
- **G19** L41 | FAIL (minor) | PLKS cost: "**Need to know:** the OEP registration fee." | source exists: W0040 (BMET notice, June 2022, possibly outdated: Tk 200 non-refundable for registration in the Malaysia database, or Tk 200 + Tk 100 through the Ami Probashi app) | fix: "In 2022 BMET charged Tk 200 [W0040 (2022)]; Need to know: the current OEP fee."
- **G20** L252 | FAIL (minor) | Tourist: no statement on appeal against refusal of entry at the border | source exists: V0055 / K0011 (Act 155 s.8(6): only a Permit holder refused entry may appeal to the Minister, so a visit-pass holder has no such appeal) | fix: add, cited.
- **G21** L211-221, L308 | FAIL | Student and Employment Pass: no scams tried by the applicant | source exists: K0031 / K0030 (getting a pass by a false statement, using another's pass), S0016 (breaking a condition can cancel the pass); for EP, E0070 is the same rule in ESD's PVP FAQ | fix: one sentence each, cited.
- **G22** L283 | FAIL | PVP: no scams tried by the applicant | source exists: E0070 ("boleh menyebabkan permohonan ditolak, kelulusan dibatalkan, pas ditarik balik, tindakan imigresen diambil dan senarai hitam": false information leads to rejection, cancellation, immigration action and blacklisting) | fix: add, cited.
- **G23** L355 | FAIL (minor) | PVIP: pass fee and dependants are missing | source in raw imi-pvip-faq.txt but no ledger row: pass fee RM2,000 a year, initial fee RM2,000 at registration, dependants are spouse, children under 25, disabled children and parents/parents-in-law; PVIP holders may bring a domestic helper | fix: log ledger rows, then add.

### UNSUPPORTED: missing, no source in the ledger, and no Need to know

- **G1** L270-272 | UNSUPPORTED | Business visit: no scams either way and no Need to know | fix: "Need to know: any official warning about fake business invitations or business-visa agents."
- **G3** L274-279 | UNSUPPORTED | Medical visit: no scams either way; the NtK on MHTC's partners doesn't cover scams | fix: add a Need to know.
- **G4** L281-283 | UNSUPPORTED | PVP: no scams done to the migrant (e.g. a "PVP" sold as a general work visa) and no Need to know | fix: add a Need to know (V0093, "not for general workers", is already cited and can be framed as the warning).
- **G5b** L312-326 | UNSUPPORTED | Family passes (EP dependants, spouse of a citizen): appeal if refused isn't stated and has no NtK (only "Other relatives" has one); no scams either way for any family pass (E0128 covers only false statements in a spouse application) | fix: add "Need to know: whether a refused Dependant Pass or spouse LTSVP can be appealed" and a scams NtK.
- **G10** L262-268 | UNSUPPORTED | Family visit (VDR): where the sponsor applies (which IMI office) isn't stated and the raw imi-vdr.md doesn't say; no scams done to the migrant | fix: "Need to know: which Immigration office takes a social VDR application" and a scams NtK. Also not in the doc: Form Imm.12 (2 copies, photo attached), which is on raw imi-vdr.md but has no ledger row.
- **G26** L352-354 | UNSUPPORTED | Residence Pass-Talent, MTEP and Investor Pass: processing time, appeal, scams and whether Bangladeshis are eligible aren't stated, with no Need to know (RP-T also lacks where to apply and cost) | fix: one Need to know per pass listing what is unknown.
- **G27** L291-293 | UNSUPPORTED (minor) | Employment Pass: the doc never states that Bangladeshis are eligible (no nationality rule is cited either way) | fix: "Need to know: whether any nationality restriction applies" or a cited statement.
- **G28** L225-240 | UNSUPPORTED (minor) | Tourist, bring a spouse: not stated that a spouse needs their own eVISA; V0023 (one account, 5 applications for up to 5 people) is cited only for the account limit | fix: one sentence using V0023.

### Notes (not counted)
- L158: "**Need to know:** what happens to a PLKS worker who becomes pregnant; no official source was found." The Rights at work bullet (L109) already cites L0094 (no dismissal while pregnant, except misconduct, wilful breach of contract or closure), and M0240 (JTKSM) says the same. Change the wording to "no official source on immigration consequences".
- L341 vs ledger E0118: MOTAC's announcement gives "Fi proses: RM500 (tidak termasuk SST) bagi setiap permohonan" from 1 Aug 2025, while L341 gives a RM5,000 processing fee [E0107]. The ledger marks this as unclear. Two official sources; the number checker should decide whether these are different fees or a conflict to show.

Table 1: 36 IMI/addendum types checked: 29 PASS (some resting on an existing Need to know), 3 FAIL (Residence Pass, Entry Permit, MDAC), 3 UNSUPPORTED (Employment Pass eligibility; Investor Pass and RP-T under G26), 1 n/a (Malaysian travel documents). Remaining gaps: 28 in all, 20 FAIL (G2, G4b, G5, G6, G7, G8, G9, G11, G12, G13, G14, G15, G16, G17, G18, G19, G20, G21, G22, G23) and 8 UNSUPPORTED (G1, G3, G4, G5b, G10, G26, G27, G28).
