# Fix log, round 4 (r4s1-r4s4, r4audit)

Line numbers in the entries are the verifiers' (malaysia.src.md before this pass). New ledger rows Z0091-Z0123 are in ledger-parts/Z.csv (facts in Z.facts.csv). New sources registered: brac-about-us (fetched with curl, BRAC "About us", undated), bb-fepd2-circular-09-2026-10 (already in raw/, Bangladesh Bank FEPD-2 circular 9 of 29 Oct 2026). Rounds 1-3 fixes kept. merge.py and build.py run with no citation errors.

## r4s1 (lines 1-115)
- L35 "Only in a limited way." | fixed: sentence deleted; the dated facts answer the question.
- L35 BOESL "government's own" | fixed: "BOESL describes itself as Bangladesh's only state-owned recruiting organisation" [Z0091, BOESL notice 6 Aug 2025, read on rendered page 1].
- L41 news for state-owned | fixed: "BOESL is state-owned, according to its own notice" [Z0091]; news kept only for the G2G label and 1,381 count, labelled [Z0084, A0059].
- L43 demand-letter rule | fixed: dated BMET notice of 27 Sep 2023 [W0039] shown against the Dec 2024 (BHC-LW-36) and Sep 2025 (attestation letter 158) letters [W0033, W0038]; "Need to know: which reference BMET requires now".
- L43 KSM term | fixed: KSM and KDN explained at first use [W0044, W0043].
- L49 syndicate fees | fixed: "In 2022-24 ... Tk 1.07 lakh per worker to syndicate leaders among the 100 agencies Malaysia had selected then and Tk 1.6 to 2 lakh to middlemen" [W0070, W0072, A0001, A0002, A0064].
- L95 i-Kad colour | fixed: "grey" removed from the main sentence; both IMI pages shown (Malay: grey for all sectors [Z0093]; English: colour by sector, and sent by an authorised vendor [Z0092]); Feb 2026 poster's collection rule kept [L0126, L0127].

## r4s2 (lines 116-225)
- L194 | fixed: V0007 added.
- L133 | fixed: "From Bangladesh" removed: "You can also apply to the Ministry of Expatriates' Welfare" [B0048].
- L189 | fixed: 8% service tax since 1 Mar 2024 [Z0094]; medical RM340 (RM350 Sarawak; calculator also lists RM250 and public-university clinics) [S0061]; public-university students may use their university [Z0095].

## r4s3 (lines 226-340)
- L267 | fixed: Z0096 (MyVISA terms clause 06, VDR eVISA covers social purpose) cited with C0006.
- L272 | fixed: "none of these notices names the eligible nationalities; the same FAQ separately lists 31 nationalities, Bangladesh among them, for which an eVISA is compulsory, without saying whether this is the multiple-entry list" [C0007, V0001, V0010].
- L296 MSC/ICT | partly fixed: ICT spelled out; no saved source explains MSC Malaysia status, so "Need to know: what MSC Malaysia status is" added inline.
- L328 | fixed: both places from the same IMI page shown [Z0097, Z0098 (conflict rows)].
- L336 | fixed: widow's sponsor must be a close relative of her late husband and attend with her [Z0099, Z0100].

## r4s4 (lines 341-449)
- L406 Pas Khas | fixed: parenthesis removed; HC's Jan 2025 FAQ order shown as older guidance [L0013]; PRM 2.0 poster marked as the rule (ticket within 14 days when you attend) [L0116].
- L368 appeal channels | fixed: appeal by letter through the Chief Secretary; phone and email are for questions about an appeal [Z0082, Z0083].
- L369 MACS "visa still needed" | fixed: "It does not replace a pass or visa: you still need any visa required for your nationality and the relevant immigration pass" [C0011, Z0109].
- L367 "FAQ page saved empty" | fixed: deleted.
- L368 e-book note | fixed: "IMI's Entry Permit page links its application guideline as an e-book on Google Drive" [Z0101]; research note removed; Need to know kept.
- L368 TalentCorp | fixed: "TalentCorp, Talent Corporation Malaysia Berhad, one of the government agencies IMI's Expatriate Services Division works with" [Z0102].
- L355 Bangladesh Bank | fixed: "Bangladesh Bank issues Bangladesh's foreign-exchange rules, under the Foreign Exchange Regulation Act 1947" [Z0103]. No saved official text calls it "the central bank" in so many words, so that phrase was not used.
- L429 BRAC | fixed: "founded in Bangladesh in 1972, which describes itself as the world's largest southern-led development organisation" [Z0104, new fetch raw/brac-about-us].
- Note (Investor Pass L365) | fixed: Need to know on processing time answered: processed within 5 working days, ePASS 1 working day after payment [Z0105, Z0106]; where to apply added (Xpats Gateway, from outside Malaysia) [Z0108, Z0107].

## r4audit
- COV-1 | fixed: new "School pupils" subsection under Student visa (school types, KDN permission for international schools, who applies, where, documents, companions' LTSVP, no work) [C0024, Z0110-Z0123, E0138]; Need to know: fee, time, appeal. Old one-line mention removed.
- A1-1 | fixed: "After arrest" bullet in What can get you jailed (removal, custody, 13 depots, visiting a detainee, no appeal against removal) [K0017, K0020, L0181, L0179, L0180, K0019]; Bans bullet now separates the 7-day appeal against the ban/cancellation [K0014] from the no-appeal rule for removal [K0019].
- A1-2 | fixed: "Cash out of Malaysia" bullet in Coming home (CAAM AIP, May 2026) [L0161, L0162] + Need to know: Bank Negara's current limits.
- A1-3 | fixed: "Pension" bullet in Your rights at work pointing to PERKESO invalidity/survivors' pension [M0168, M0172] and the 2025 EPF proposal [M0163, M0164]; Need to know: retirement pension in Malaysia or through a Bangladesh government scheme.
- A2-1 | fixed: unofficial lines added to both NtKs: L35 [A0097, A0104, A0022, A0105]; L49 BAIRA allegations (BAIRA explained) [A0026, A0011].
- A2-2 | fixed: forged-passport/FOMEMA ring line [D0035, N0035], labelled.
- A2-3 | fixed: pregnancy screening in FOMEMA added to the NtK, labelled [D0030]; "no official source ... was found" research note removed.
- A2-4 | fixed: [S0137, S0140, S0138] added to the student-scam NtK, labelled.
- A2-5 | fixed: medical item 6 now "Scams" with the false-statement offence [K0031, K0030].
- A2-6 | fixed: MOTAC vetting/re-registration of MM2H agents (2024), labelled [E0142].
- A2-7 | fixed: "Compared with other nationalities" bullet in Malaysia as a destination, all labelled; PRM ranking conflict shown both ways [H0007, H0006, L0191, E0141, N0016].
- A2-8 | fixed: MHTC courting Bangladeshi patients (official) [N0041]; "Tourists and students" bullet [N0055, S0136]; CLAB rejection figure in Where the jobs are [D0036], labelled.

Not changed (outside the fix list): V0088 status (audit note) is in another part file; H0006 says PRM 2.0 began on 19 May 2025, while the doc (L0113) gives 1 May 2026 to 31 May 2027. Worth a check next round.

## Lines changed or added in malaysia.src.md (new numbering)
35, 41, 43, 49, 95, 113, 125, 135, 159, 171, 191, 196, 210, 220-223, 226, 273, 278, 287, 302, 334, 342, 360, 361, 371, 373, 374, 375, 412, 416, 431, 436, 443, 444, 445, 447.
