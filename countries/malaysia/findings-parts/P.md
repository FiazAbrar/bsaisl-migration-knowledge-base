# Findings, part P: family visit VDR, business, medical, Professional Visit Pass, transit, Employment Pass

Researched 7 Nov 2026 for draft chunk drafts/MY5.md (source lines 267-320). New ledger rows P0001-P0047 (ledger-parts/P.csv). The draft also cites existing verified/possibly-outdated rows from ledger.csv (V, C, Z, E, K, B, N series), each re-read against its claim and quote before reuse.

## Family visit VDR (social Visa Dengan Rujukan)

- IMI's 2023 checklist PDF (SENARAI-SEMAK-Borang-VDR.pdf, scanned, no text layer; rows logged with --no-quote-check, quotes transcribed from page images) contains the full kit: Imm.12 x2, passport copy, personal/security bond stamped RM10 at LHDN, sponsor IC (sponsor must attend), sponsor's declaration (Commissioner for Oaths), income proof RM2,000+/month, employer letter, sponsor information form, cover letter, relationship proof; 7 working days [P0010-P0012]. Same content as the IMI VDR web page [Z0025-Z0028, V0090].
- Security bond only for China and Nigeria nationals; everyone else, including Bangladeshis, gives a personal bond [P0006]. Personal bond form: sponsor binds himself to forfeit a sum deposited against a receipt [P0014]. The sponsor information form asks "if approved, are you willing to pay a deposit (wang cagaran)?" [P0012]. IMI's bond-rate table gives RM750 for Bangladesh [V0112]. Whether a cash deposit is actually taken on a family VDR for a Bangladeshi is not stated anywhere: kept as Need to know.
- Relationship-proof table: parents/parents-in-law (marriage cert, birth cert and passport of sponsor's spouse, notarial certificate endorsed by Malaysian mission abroad and Wisma Putra), child under 7, spouse of citizen [P0008].
- Processing: VDR page and checklist say 7 working days; IMI client charter says 5 working days [V0090, P0010 vs C0044]. Doc uses 7 (two sources, and charter applies only to normal cases). Not shown as conflict (doesn't change what anyone does).
- Where the sponsor submits: VDR is approved by IMI HQ; the charter lists it under the Visa, Pass and Permit Division [C0008, C0044]. IMI's LTSVP page says some related applications (work endorsement for spouses) can be made at HQ Putrajaya "or the nearest state Immigration office", and that China/Nigeria spouse applications go to HQ only; nothing says which for a social VDR. Searched: IMI VDR page, IMI forms page, IMI FAQ Visa/Pass/Permit (FAQ body is JS-loaded and empty in both curl and Firecrawl copies), HC Dhaka FAQ, web and Malay search ("permohonan VDR sosial ... pejabat imigresen negeri"). Kept as Need to know; HQ address and MyGCC phone 03-8000 8000 given [P0005].
- eVISA after VDR approval: MyVISA's VDR eVISA-exempt list (51 countries) was re-scraped with Firecrawl directQuote on 7 Nov and saved as raw/myvisa-faq-vdr-exempt-list.md; Bangladesh is not on it [P0015]. This resolves the earlier draft's doubt about the researcher-note list in raw/myvisa-faq.md. VDR eVISA needs passport biodata page (6+ months) and the eVAL [P0016]; mismatches must be fixed by the letter-issuing office before payment [P0017]. MyVISA's rate table (visa fee + RM105 + 0.8/1.7%) does not separate VTR from VDR, so the doc applies it to VDR [P0018].
- Appeal against a refused social VDR: nothing on IMI VDR page, checklist, MyVISA FAQ/terms (MyVISA only says missions may refuse without reasons [V0042], which is about eVISA). Kept as Need to know.
- Practice: no news found on family-visit VDR abuse specifically (searched English and Bangla). General visit-pass misuse arrests used instead [P0020, P0022].

## Business visit

- Multiple-entry eligibility: IMI/MyVISA say MEV is limited to 31 (IMI notice: 30) eligible nationalities without naming them [C0007, V0009, V0010, V0011]. VisasNews (4 Sep 2026) ran test applications on MyVISA for the 31 eVISA nationalities, Bangladesh among them, and the form allowed MEV for Business, Fly & Cruise, Medical, Wedding Tourism [P0001]; Observer (4 Sep 2026) says business/medical MEVs remain available to Bangladeshis [P0002]. Unofficial only: doc keeps one Need to know for an official statement. Jagonews24 English article (MEV tightened for Bangladesh and 30 others) returned 403; not needed after VisasNews.
- MEV validity conflict carried from part V: 6 months/30 days per entry (MyVISA terms, 2026) vs 3-12 months (undated IMI Types of Visas and HC Dhaka FAQ) [V0071 vs V0072, V0114]. Doc states only the current MyVISA rule.
- PLS@Xpats (new to the doc): IMI FAQ PDF (Lampiran B, Oct 2022) [P0024-P0031]: critical/emergency professional work on a social visit pass, max 30 days, approval valid 30 days single entry, no extension, free, 3 working days, ESD Putrajaya decides, company applies at mtp.imi.gov.my/plsXpats/main with company letter, full passport copy, e-SSM, schedule, return ticket; all nationalities except Israel, 18+, company need not be ESD-registered; visa-required nationals still need an eVISA; no entry without the approval letter; Peninsular Malaysia and Labuan only; no dependant pass. Charter confirms 3 working days [C0048]. 2022 PDF, so possibly-outdated; IMI home page still lists PLS@XPATS as a live service [E0072].
- Reality check: government directive 8 Jun 2026 for a nationwide crackdown on misuse of short-term passes including business travellers (EY alert) [P0021]; 79 Bangladeshis arrested in Perak glove factories for visit-pass misuse (Apr 2026) [P0020]; 173 foreign workers, 147 Bangladeshi, at Sepang construction sites, employers misusing others' PLKS and social visit passes (Sep 2026) [P0022]; 2024 syndicate bringing Bangladeshis on fake sports invitations, RM2,000-5,000 each [P0040]. KLIA "Not To Land" refusals of Bangladeshi visitors 2025 are in part V [V0109-V0111]; none of the reports found was about business visas specifically.
- Speed money: 2023 MACC arrest of an HC Dhaka enforcement officer for USD 300-500 bribes per visa [N0025]. Immigration DG (Aug 2025): matters only through JIM counters/official portal; fake ePASS sold for RM5,000; report to police or MACC [P0038, P0039].
- Complaint routes: Malaysia: police or MACC [P0039]; MyVISA Live Chat (24h) for payment problems [P0019]. Bangladesh: BMET complaint to DG (complaint cell, free, 30 working days) [B0034]; mobile courts under the Overseas Employment and Migrants Act 2013 [B0047]; full procedure lives in the PLKS Scams section (other agents' chunk). ILO/IOM don't take individual cases (part G, G0027) - not repeated in this chunk.

## Medical visit

- MHTC's Aug 2026 press release (carried by Utusan Malaysia) names Irving Aviation Ltd as "MHTC's local partner in Bangladesh", contact Abid Rahman Rafsan +8801762001467 [P0032]. Registered as official (MHTC is under the Ministry of Health and authored the release). The 2022 GD Assist appointment [V0078] and the Dhaka Tribune Sep 2026 report [N0042] are superseded in the doc. MHTC's Sep 2026 Healthcare Week release (Bernama/Macau Business copy) names no partner.
- Conflict that changes action: HC Dhaka (undated) says Bangladeshi medical visitors apply through MHTC's authorised partners [V0075]; MyVISA (Oct 2026) and MHTC's own steps describe applying online yourself [V0073, V0076]. Kept as one Need to know.
- MHTC procedure: appointment letter in English [P0034], MHTC support letter [V0076], Find A Hospital directory and WhatsApp concierge +60 18 870 0100 [P0035], print approval [P0036], Special Lane conditions [P0037], what to bring [P0046]. 91 member hospitals [P0033].
- Long-term medical pass: IMI 2023 checklist (Imm.38, Imm.12, hospital letter, 3 months' bank statements, relationship proof certified by Malaysian mission, MHTC letter, payment proof) [P0013]; LTSVP web page: government or specialist hospitals, one companion [C0018].
- Scams: searched Bangla ("মেডিকেল ভিসা মালয়েশিয়া ... দালাল প্রতারণা") and English. Results were about fake Indian-hospital appointments for Indian medical visas and hospital brokers in Bangladeshi public hospitals, nothing on the Malaysia route. Kept as Need to know.

## Professional Visit Pass

- PVP-Expert FAQ (ESD, Sep 2026): document list by category [P0041]; approval period depends on the task, max not automatic [P0042]; earlier rows E0070, V0092-V0094.
- ePASS covers EP, DP, LTSVP and PVP; endorsement steps (company submits and pays in ESD Online; KLIA ESC T1/T2 without appointment, or MYXpats Centre); corrections via MYXpats helpdesk 3-5 working days; i-KAD only for EP holders [P0043-P0045].
- Standard PVP processing time: client charter gives 5 days (fast-track PVP-Expert), artistes 5, missionaries 25, Sarawak manual 30 [C0048, C0047, Z0079]; nothing for a standard PVP via ESD. Kept as Need to know.
- "PVP sold to general workers": searched English ("professional visit pass misuse ... Bangladesh") and Bangla ("প্রফেশনাল ভিসা মালয়েশিয়া ... প্রতারণা"); found only PLKS/social-visit-pass misuse and fake e-PLKS rings [P0023, D0045]. Kept as Need to know.

## Transit

- Unchanged rules [V0079-V0082]. Only Malaysia's missions in India state the PNR/KLIA-KLIA2 rule [V0081]; no IMI or HC Dhaka statement for Bangladeshis. Third-party airport guides (klia2.com.my, visatraveler) are unofficial and disagree with each other; not used. Need to know kept.

## Employment Pass

- Bangladesh side added: a worker with an individually obtained visa applies for BMET emigration clearance himself at BMET's emigration branch (Dhaka) or Chattogram DEMO, 3 working days; fees Tk 4,500 welfare+insurance, Tk 250 smart card, source tax Tk 400/250 [B0029, B0030]. B0028 (same charter, conflict status in ledger) not cited.
- Section 60K timing conflict: ESD Aug 2026 booklet 10 working days [Z0086] vs JTKSM 2023 FAQ 14 working days [Z0085]. Doc uses the newer ESD figure only; the difference doesn't change what the worker does.
- Earlier draft's Need to know "what MSC Malaysia status is": ESD's own line names the Multimedia Development Corporation and ICT; MIDA's MSC page is 404 and MDEC's Malaysia Digital page is JavaScript-only (Firecrawl got only a heading). Doc now explains it as ICT companies with MSC Malaysia status approved by the Multimedia Development Corporation [E0007]; no separate Need to know.
- Earlier Need to know "nationality restriction for Bangladeshis": ESD's visa-charge table has a Bangladesh rate [E0045] and nothing found restricts Bangladeshis; dropped from the doc rather than kept as a gap.
- EP scams: no official ESD scam notice found (search "ESD scam alert fake Employment Pass"). Used the Aug 2025 fake-ePASS case [P0038]. The Indian High Commission KL advisory for professionals exists only as a 2017 Wayback copy (raw/hci-kl-advisory-professionals, not registered, not used).

## Dropped from the old chunk

- "The Malaysian High Commission in New Delhi tells Indian travellers..." phrasing replaced by the rule itself with citation.
- 2023 news on refused travellers' airlines etc. belongs to part V (Tourist visa).
- "IMI's VDR page says 7 days while client charter says 5" and "older official pages still describe 3 to 12 months" removed from the doc (research log).

## Need to know (open, at the step)

1. Family VDR, Step 2: whether a cash deposit is taken from the sponsor of a Bangladeshi relative.
2. Family VDR, Step 2: whether a state Immigration office also takes the application, or only HQ.
3. Family VDR: whether a refused VDR can be appealed.
4. Business visit, Step 2: official statement that Bangladesh is one of the 31 MEV nationalities.
5. Medical visit, Step 2: whether Bangladeshis must go through MHTC's authorised partners (HC Dhaka) or may apply themselves (MyVISA).
6. Medical visit: scams on the Malaysia medical-visa route.
7. PVP, Step 2: standard PVP decision time through ESD.
8. PVP: any case of a "PVP" sold to general workers.
9. Transit: whether the single-PNR / KLIA-KLIA2 rule applies to Bangladeshis.

## Conflicts

- C0044 (5 days) vs V0090/P0010 (7 days), social VDR processing.
- V0075 (HC Dhaka: via MHTC partners) vs V0073/V0076 (apply online yourself), medical eVISA.
- Z0086 vs Z0085, section 60K timing.
- V0071 vs V0072/V0114, MEV validity.

## Blocked

See blocked-parts/P.md.

## Fix round, 7 Nov 2026 (checker failures on drafts/MY5.md)

New rows P0048-P0068. New raw files: imi-vdr-social-checklist-2023.ocr.txt (OCR of the scanned checklist; pages 6-7 with --psm 6; Q18 "wang cagaran" confirmed on the page image), kln-attestation-of-documents, sprm-report-corruption-en-wb (Wayback 24 Jun 2024), mygov-keselamatan-siber, mygov-mers-999, mygov-semak-scammer, pdrm-home, pdrm-faq, moh-ckaps-faq, moh-medicalprac-contact, mhtc-concierge-service, imi-form-imm38 (+ .ocr.txt).

- VDR deposit question re-checked against the OCR copy: P0048 (Q18). P0010/P0011 quotes match the OCR text; P0012's joined quote spans non-adjacent lines, so the deposit point now cites P0048.
- VDR is issued by a Malaysian mission abroad after HQ approval [P0049]. How the eVAL reaches the applicant: not stated on IMI VDR page, checklist or MyVISA FAQ (Visa With Reference section). Need to know.
- Notarial certificate for parents/in-laws: Wisma Putra Consular Division walk-in attestation, address/hours/phone/email, same or next working day [P0050, P0051]; no fee on the page. Wisma Putra says foreign documents first need the foreign country's mission in Malaysia [P0052], while the VDR checklist says Malaysian mission abroad + Wisma Putra [P0008]: kept as one Need to know. HC Dhaka home page links only to the general KLN attestation page; no Dhaka fee found. Bangladesh-side attestation (MoFA/Law) is documented only for BHC KL attestations [Q0079], not used.
- VDR approval fee and counter hours: searched IMI VDR page, checklist, Malay web search ("bayaran permohonan VDR sosial penaja"); nothing. Need to know.
- 5 vs 7 day VDR conflict (C0044 vs V0090/P0010): doesn't change what anyone does; C0044 dropped from the doc.
- Complaint route: MACC hotline 1-800-88-6000, portal portaladuan.sprm.gov.my, email, SMS, HQ address [P0053, P0054] (live sprm.gov.my and portaladuan refused curl and Firecrawl; Wayback copy used). NSRC 997 24h, police report at nearest station, contact bank [P0055]; Semak Mule check [P0056]; 999 free [O0073, O0074]. PDRM e-Reporting (ereporting.rmp.gov.my) failed to load (curl 000, Firecrawl proxy error); PDRM home and FAQ fetched but give no procedure; not used.
- MYXpats Centre: TalentCorp-IMI joint company [P0057]; Surian Tower address, +603-7839 7171, helpdesk@myxpats.com.my, Mon-Fri 9-5 [P0058].
- Medical: MHTC concierge arranges appointments [P0059]; no fee stated. Irving Aviation line removed (company named without evidence of what it does or fees); folded into the MHTC-partner Need to know. 91-hospitals statistic cut. Private-hospital complaints: MOH CKAPS FAQ (portal, 03-8883 1362, letter, 14-day hospital reply, 30 days simple cases, refunds at hospital's discretion) [P0060-P0062]. Imm.38 = IMI visa application form [P0063]. LTSVP 25 working days [E0057]; office, fee, result document and appeal for medical LTSVP not on IMI's LTSVP page or checklist: Need to know.
- EP documents rewritten from ESD Online Guidebook v6 [P0064-P0067]; dependants in all categories and "same employer, position and EP category" wording from the Revised Expatriate Salary booklet [P0068]. ESD registration 5 working days [E0016]; 60K step kept at 10 days citing E0016 only (Z0086 conflict row no longer cited).
- Seaman Letter of Guarantee: IMI page gives no procedure; web search found only shipping-agent material. Need to know.
- PVP BMET clearance: B0029 covers individually obtained visas; nothing on PVP holders sent by an overseas employer. Need to know.
- Cut per checker: P0021 crackdown line, N0025 HC Dhaka bribery anecdote, E0045 "visa-charge table" filler, "test applications" narration (P0001/P0002 no longer cited). Offence (false statement, K0031/K0030) now stated only in Tourist visa, Scams (existing text, outside this chunk); MY5 cross-refers to it from each visa.
