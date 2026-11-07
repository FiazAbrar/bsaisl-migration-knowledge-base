# r4audit: coverage and double audit of malaysia.src.md (round 4)

Checked 7 Nov 2026 against malaysia.src.md (449 lines), ledger.csv (part C, C0001-C0048, plus a search of all unused rows for answers to audit items) and raw/ (imi-en-types-of-visas.txt, the IMI menu in imi-ikad-collection.txt, myvisa-home-fc.md, myvisa-faq.md, imi-student-pass.txt, imi-documents-by-category.md, imi-program-istimewa.md). Nothing fetched; malaysia.src.md not edited. All 23 round-3 gaps (G1-G23 in verify/round3/r3coverage.md) are fixed in the doc. Only gaps are listed below.

Key: OK = answered with citations; NtK = explicit "Need to know"; gen = answered once for all visas (Asylum L385-387, Having a child L389-394); n/a = does not apply.

## 1. Coverage against IMI's official list

All 48 C rows map to a doc section or the "not open" table. 12 C rows aren't cited, but each type is covered with other ids, so none is a gap: C0001/C0003/C0004 (Types of Visas page; covered by V0009, Z0068, V0072, V0080), C0005 (VTR; Tourist, V0001/V0005), C0010 (eNTRI; table, V0115), C0012 (PLKS; W0048/L0044), C0014 (short-term SVP; V0068/V0104), C0025 (Residence Pass; E0131/Z0018), C0027 (domestic helper; L0194), C0041 (Dependant Pass; E0014), C0042 (Graduate Pass; S0044/S0073), C0043 (MDAC; V0058). IMI menu items that are Malaysian travel documents (Certificate of Identity, restricted travel document, emergency certificate SPC) and the 2021 COVID-era "Death and Critically Ill Emergency Visit" notice (imi-notice-death-emergency-visit.md, no ledger row) are not visa types for Bangladeshis and are not counted.

- COV-1 | L208 | FAIL | school-level Student Pass (pre-school and school pupils) and the accompanying-family LTSVP for school pupils | doc: "IMI also gives Student Passes for pre-school and school pupils [C0024]; this doc covers higher education." No Bangladesh status and no Need to know | source exists: raw/imi-student-pass.txt l.261-267 (school must be a KPM government/aided school or a registered international/private school; international schools need KDN permission; applied for by the school, parent or legal guardian at the IMI Student Pass unit or state office by school address), l.282-285 (LTSVP "sebagai pengiring" for family/legal guardian of a school-level student), l.422-476 (document checklist); only C0024 is logged | fix: log rows, then add a short school-pass paragraph (relevant to children of EP, MM2H and spouse-pass holders), or at minimum "Need to know: requirements for a Bangladeshi child's school Student Pass".

## 2. Audit 1: the migrant's questions (main focus PLKS)

| Question | Where answered | Verdict |
|---|---|---|
| How long can I stay | PLKS "How long you can stay" L114-119; tourist 30 days L224; Student L208; EP categories L300; MM2H/DE Rantau | OK (PR NtK L119) |
| What will I earn | permission-letter salaries L43; BOESL RM1,700 L41; minimum wage, equal pay, deductions L109; overtime L106-107 | OK (NtK minimum wage order in force) |
| Rights at work | "Your rights at work" L102-112; complaints L128-134 | OK |
| What gets me jailed | L121-126; false statements K0030/K0031; bans L410 | FAIL (A1-1) |
| Bank account and SIM | Step 7.6-7.7 L97-98; Bangladesh accounts L88 | OK (NtK "work permit document") |
| Pension | EPF proposal + NtK L99; PERKESO invalidity pension L419 | UNSUPPORTED (A1-3) |
| Can my family come | L118, L155-157, Family passes L315-344 | OK |
| What can I bring home | Coming home customs L424; banned goods into Malaysia L126 | FAIL minor (A1-2) |

- A1-1 | L121-126, L410 | FAIL | partly-supported | "What can get you jailed" lists offences but not what happens after arrest: custody pending removal, depots, and no appeal for overstayers. L410 "can appeal to the Minister in writing within 7 days [K0012, K0013, K0014]" applies to a pass cancellation or entry ban, not to removal of someone whose pass expired | unused: K0017 (convicted of unlawful entry or as a prohibited immigrant, removable by DG order, s.32(1)), K0020 (may be held in prison, police station or immigration depot "for as long as needed" to arrange removal, s.34), K0019 (no appeal against removal where presence is unlawful because the pass expired or was cancelled), L0181 (13 depots), L0179-L0180 (family visiting a detainee needs an Immigration officer's letter) | fix: add 1-2 sentences to "What can get you jailed" and the K0019 limit at L410.
- A1-2 | L424 | FAIL (minor) | partly-supported | "what can I bring home" covers Bangladesh customs only, not cash taken out of Malaysia | unused: L0161 ("ringgit notes up to RM1,000 ... upon arrival in or departure from Malaysia", CAAM AIP, possibly outdated, note "verify with BNM"), L0162 (foreign currency out "up to amount brought into Malaysia") | fix: add with the AIP labelled as such, plus "Need to know: Bank Negara's current cash limit".
- A1-3 | L99, L419 | UNSUPPORTED | pension: only Malaysia's EPF proposal (NtK) and PERKESO's invalidity/survivors' pension; nothing on any Bangladesh-side pension or savings scheme for migrants, and no Need to know | no ledger row found ("pension", "probash", "universal" give only M0172) | fix: "Need to know: whether a Malaysia-based worker can join a Bangladesh government pension scheme, and how."

## 3. Audit 2: the original aim

### 3.1 Per visa

Columns: Ty types, Rq requirements, Wh where to apply, Co cost, Ti processing time, Ap appeal, S→ scams done to the migrant, S← scams tried by the migrant, Wk can work, As asylum, Ch have a child, Sp bring a spouse.

| Visa (lines) | Ty | Rq | Wh | Co | Ti | Ap | S→ | S← | Wk | As | Ch | Sp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PLKS incl. G2G/BOESL (31-169) | OK | OK | OK | FAIL A2-1 | OK | NtK | OK | FAIL A2-2 | OK | gen | FAIL A2-3 | OK (no) |
| Domestic worker (171-173) | not open, cited | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| Student (175-220) | FAIL COV-1 | OK | OK | OK | OK | NtK | FAIL A2-4 | OK | OK | gen | OK | OK |
| Tourist (222-259) | OK + NtK (MEV) | OK | OK | OK | OK | OK | OK | OK | OK (no) | gen | gen | NtK |
| Family visit VDR (261-268) | OK | OK | NtK | OK + NtK | OK | NtK | NtK | OK | OK (no) | gen | gen | n/a |
| Business (270-272) | OK + NtK | OK | OK | OK | OK | OK | NtK | OK | OK | gen | gen | OK |
| Medical (274-282) | OK | OK | OK | OK | OK | OK | NtK | FAIL A2-5 | OK (no) | gen | gen | OK (companions) |
| PVP (284-286) | OK | OK | OK | OK | OK + NtK | OK | NtK | OK | OK | gen | gen | OK (no) |
| Transit + ship crew (288-292) | OK | OK + NtK | OK | OK | OK | OK | n/a | n/a | n/a | gen | n/a | n/a |
| Employment Pass (294-313) | OK | OK | OK | OK | OK | OK | NtK | OK | OK | gen | gen | OK |
| EP family (317-324) | OK | OK | OK | OK | OK | NtK | NtK | NtK | NtK (conflict shown) | gen | gen | OK |
| Spouse of a citizen (326-328) | OK | OK | OK + NtK | NtK | OK | NtK | NtK | OK | OK | gen | gen | n/a |
| Residence Pass (332) | OK | OK | OK | OK | NtK | NtK | NtK | NtK | OK | gen | gen | NtK |
| Other relatives LTSVP (334-336) | OK | OK | NtK | OK + NtK | OK | NtK | NtK | OK | NtK | gen | gen | n/a |
| MM2H (346-355) | OK | OK | OK | OK + NtK | OK + NtK | OK + NtK | FAIL A2-6 | OK | OK | gen | gen | OK |
| DE Rantau (357-359) | OK | OK | OK | OK | OK | OK | NtK | NtK | OK | gen | gen | OK |
| RP-T / MTEP / Investor (363-365) | OK | OK | NtK | OK / NtK | NtK | NtK | NtK | NtK | OK | gen | gen | OK |
| PVIP (366) | OK | OK | OK | OK | NtK | NtK | OK + NtK | OK | OK | gen | gen | OK |
| PLS@XPATS (367) | OK | NtK | OK | NtK | OK | NtK | NtK | NtK | OK | gen | gen | n/a |
| Entry Permit / PR (330, 368) | OK | OK + NtK | NtK | OK (REP) + NtK | NtK | OK (REP) + NtK | n/a | OK | n/a | gen | OK | OK |

- A2-1 | L35, L49 | FAIL | partly-supported | "**Need to know:** the official text of these announcements, and whether private agencies may now charge workers anything." / "**Need to know:** the official maximum for private-agency jobs since the 2026 reopening." These NtKs don't report what was said unofficially | unused: A0097 (8 Apr 2026 joint statement: "employers bear the full cost of recruitment, resulting in zero cost to workers", unofficial), A0104 and A0022 (Apr 2026: fewer intermediaries, AI system, employer bears costs, unofficial), A0105 (Jun 2026: no syndicate, lower cost, unofficial), A0026 and A0011 (Aug 2026: BAIRA members allege a 2026 syndicate fee of RM5,500 and visas sold for RM8,000-9,000, unofficial) | fix: add one sentence to each NtK with "(unofficial, not verified)".
- A2-2 | L169 | FAIL | partly-supported | "**Need to know:** any official Malaysian or Bangladeshi warning about fake ages or documents for Malaysia." | unused: D0035 (Immigration, Feb 2026, via news: a syndicate sold forged Bangladeshi passports to workers in the Klang Valley who had failed FOMEMA so they could re-sit the screening; 22 seized) and N0035 (a Bangladeshi student-pass holder was arrested for running it; held under s.56(1)(i)), both unofficial | fix: "Workers who failed FOMEMA have reportedly bought forged passports to re-sit it; Immigration arrested the ring in Feb 2026 (unofficial, not verified) [D0035, N0035]," then the existing offence penalties [L0089].
- A2-3 | L157, L94 | FAIL (minor) | partly-supported | "**Need to know:** what happens to a pregnant PLKS worker's pass; no official source on the immigration consequences was found." | unused: D0030 (FOMEMA screening covers "HIV, Hepatitis B, syphilis and pregnancy", news-edge-fomema-697767.md, 2024, unofficial) | fix: add "FOMEMA's screening reportedly includes a pregnancy test (unofficial, not verified) [D0030]" to the NtK.
- A2-4 | L220 | FAIL (minor) | partly-supported | "**Need to know:** any official warning from KPT, EMGS, IMI or the Bangladesh High Commission about fake colleges or student-visa agents." | unused: S0137 (lead: KPT "shutting down colleges and tightening scrutiny of Bangladeshi applications after a surge in fake-university enrolments"), S0138-S0140 (2017: colleges with no real classes, 26 licences revoked, agents charging over RM20,000; unofficial) | fix: add S0137 to the NtK as unofficial, not verified ([N (2017)] for S0138-S0140 if used).
- A2-5 | L274-282 | FAIL (minor) | partly-supported | Medical visit has no scam tried by the applicant. Item 6 has only the NtK on official warnings | source: K0031, K0030 (false statement to get a pass: fine up to RM10,000 or up to 5 years' jail), already used in the Tourist, Business, VDR, Student and EP sections | fix: add the same sentence to item 6.
- A2-6 | L354 | FAIL (minor) | partly-supported | "**Need to know:** ... any official warning about MM2H scams." | unused: E0142 (lead, Apr 2024: MOTAC re-vetted all MM2H agents after many complaints; agents had to re-register) | fix: add to the NtK as unofficial, not verified, with year.

Not counted (item already answered): N0056 (agents in Bangladesh reportedly charge Tk 5,000-8,000 for a tourist eVISA) could be added to Tourist "Scams". V0088 is marked "verified" in the ledger, but its quote is a researcher's note (myvisa-faq.md l.419), so the NtK at L267 is correct and the ledger status should be "lead".

### 3.2 Changing visa type (L371-383)

OK. Every route with a source is present, and the open questions are NtKs (L380, L383; PLKS to PR at L119). No gap.

### 3.3 Asylum (L385-387)

OK, written to discourage: no legal status, arrest, detention and deportation, no right to work, long online wait, one appeal, full fees for unregistered pregnant asylum seekers, paid "help" is a lie, fake UNHCR cards, and Bangladesh isn't among UNHCR's named countries. No gap.

### 3.4 Corridor information (L431-438)

Numbers OK [B0091, B0086-B0089, B0092, B0093]. Bans and past stops OK with NtK, and the 2024 closure is in the PLKS intro (L35). Growth partly answered (CLAB, DHL, minimum wage, medical travel).

- A2-7 | L438 | FAIL | partly-supported | Comparison with other countries: "**Need to know:** official figures for Bangladeshi workers in Malaysia compared with Indonesia and Nepal." Only A0070 (costs) is given | unused: H0007 (Feb 2026, Immigration deputy DG via The Star: Bangladeshis had the highest PRM 2.0 participation, then Indonesians; 155,000 joined), H0006 (Apr 2026: Indonesians first, Bangladeshis second among 204,523 returnees), E0141 (lead, 2024: 3,604 Bangladeshi MM2H holders, 5th after China, Australia, South Korea and Japan), N0016 (2023: most of 14,973 Not-to-Land notices went to Bangladesh, Pakistan and India), L0191 (activists: about 800,000 Bangladeshis in Malaysia, 100,000-200,000 jobless), S0136 (lead: over 11,000 Bangladeshi students, up 45%). All unofficial or lead | fix: add as unofficial, not verified, with years where older than 2025.
- A2-8 | L436-437 | FAIL (minor) | partly-supported | Growth opportunities: no tourism or student trend, and no CLAB rejection rate | unused: N0041 (MHTC, Mar 2026, status verified: MHTC is courting Bangladeshi patients after India's visa restrictions, through Bangladeshi facilitators), N0055 (Malaysia targets 300,000 Bangladeshi tourists in 2026, unofficial), S0136 (student enrolment +45%, lead), D0036 (CLAB, Feb 2026: about 1,000 of 3,000 Bangladeshi construction candidates rejected, unofficial) | fix: add to "Where the jobs are" or "Medical travel" with labels.

## Counts

FAIL: 11 (COV-1; A1-1, A1-2; A2-1 to A2-8). 6 are minor (A1-2, A2-3, A2-4, A2-5, A2-6, A2-8).
UNSUPPORTED: 1 (A1-3).
