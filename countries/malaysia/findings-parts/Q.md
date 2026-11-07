# Findings, part Q: family passes, MM2H, DE Rantau, other passes

Rewrite of malaysia.src.md lines 321-376 (draft: drafts/MY6.md). Researched 7 Nov 2026. Ledger rows Q0001-Q0077 (ledger-parts/Q.csv).

## Family of an Employment Pass holder

- Dependant Pass duration follows the principal's pass (or the dependant's passport if shorter) [E0034]. This resolves the old draft's "how long a Dependant Pass lasts" gap.
- LTSVP duration still conflicts: ESD's LTSVP page says it follows the principal's pass [E0147], ESD's payment table (Jul 2025) caps approval at 12 months [E0148]. Kept as one Need to know.
- Parents for Dependant Pass: ESD's older EP page lists parents under DP [E0149]; the 2026 salary policy puts them under LTSVP [E0014]. Newer policy kept; conflict left out of the doc.
- Work: ESD's current Dependant Pass page [Q0001] and the 2025 ESD guidebook [E0145] both say a DP holder must get their own Employment Pass. IMI's 2021 FAQ [E0038] says a spouse can work with an endorsement. Kept the ESD rule (newer, two sources); the IMI 2021 line is dropped from the doc. Secondary sources (Speedhome, AHK, BAL) agree no current work right; BAL reports MDEC stopped "consent to work" for DP spouses (undated).
- New: Budget 2027 speech (9 Oct 2026, Malay text p.75): from 1 Jan 2027 spouses of Category I EP holders on a DP may work, "tertakluk kepada syarat ditetapkan" [Q0003]. The English speech text (raw/mof-budget-2027-speech-en.txt) does not contain the passage in its text layer; the Malay speech was fetched instead. Conditions not yet published (law-firm notes eiglaw.com, tandslaw.com, envoyglobal say the same; not saved).
- New: from 1 Nov 2026 DP spouses can apply online for Permission to Study via the ESD Online Sub-Product menu; counter submissions no longer accepted [Q0005].
- Appeal: ESD's Appeal Module covers only EP and PVP [Q0064]. No official text found on appealing a refused DP or LTSVP (searched ESD FAQ pages: MyXpats, Xpats Gateway, company registration; IMI FAQ). Need to know kept.
- Personal bond: the old draft asked whether an EP holder's family LTSVP needs a bond. ESD guidebook says LTSVP needs a personal bond stamped by IRB [E0031]; bond rate for Bangladeshis RM750 [E0144]. Gap closed.
- Certification: ESD wants certificates certified by the Malaysian mission in Bangladesh or the Bangladesh mission in Malaysia, dated in the current year [E0030]. BHC KL attestation fee: RM42 normal / RM63 urgent for certificates and affidavits from 16 Jan 2026 [Q0062]; the older BHC fee chart PDF (image, 2024 upload) gives RM45 for a marriage/nikahnama certificate [Q0077]; newer page used. Malaysian HC Dhaka pages saved (kln-mhc-dhaka-faqs, home, visa requirement, agencies) cover visas only, nothing on certifying family documents: Need to know kept.
- Scams: searched English and Bangla ("Malaysia family visa scam", "মালয়েশিয়া ফ্যামিলি ভিসা দালাল প্রতারণা"); found only work-permit and fake-visa rings (Daily Star Bangla news-540361, 358361; bribery at the Malaysian HC Dhaka news-501376), nothing on family passes. Need to know kept.

## Spouse of a Malaysian citizen

- Office: IMI's spouse-pass extension page says all pass applications can go to the office nearest the applicant's home [Z0046]; new-application page sends only Chinese and African nationals to HQ [Z0047]. Used as the rule; old Need to know dropped.
- Work-endorsement office conflict: one block of IMI's LTSVP page says the Visa, Pass and Permit Division in the state where you work [Z0097]; another says HQ Putrajaya or the nearest state office [Z0098]. The doc gives the state-of-work office (also S0099); conflict left out (doesn't change much: the state office is valid under both).
- Added checklist items from IMI's LTSVP page: sworn declaration with photo stamped by a Commissioner for Oaths, postcard-size wedding photo, divorce/death certificate, children's birth certificates, employer letter, 3 months' payslips/bank book/Form J [Q0006-Q0009].
- Fee: no official fee for a citizen's-spouse LTSVP found. Searched imi.gov.my (Kadar Bayaran Visa page lists only visa fees: Bangladesh RM20), WebSearch in Malay and English. Secondary sources (Santa Fe Relo, MDEC "new update from Immigration", expat forums) say the LTSVP fee moved from RM50 a month to RM90 a year; not official for this category. Need to know kept.
- Appeal for a refused spouse LTSVP: nothing official found. Need to know kept.
- Reality check:
  - Daily Star Bangla, 4 Nov 2023 [Q0010]: IMI DG Ruslin Jusoh (via Berita Harian) said PLKS holders are barred from marrying locals; a marriage in breach automatically cancels the permit and the worker is deported; foreigners must fill a special form with employer details. Old (2023) but consistent with IMI's PLKS page [E0139].
  - FMT, 13 Jul 2025 [Q0011, Q0012]: IMI DG Zakaria Shaaban: syndicates pay elderly Malaysian women monthly allowances to marry young foreign men; IMI won't approve LTSVPs for marriages of convenience; a syndicate selling spouse-category applications and JPN marriage registration was broken. Not specific to Bangladeshis.
  - No report found of Bangladeshi men specifically targeted by spouse-visa syndicates (English and Bangla searches).
- Permanent residence for spouses: now from IMI's Entry Permit e-book (see below): wife 3 years married + >12 months on spouse LTSVP; husband 5 years + 5 continuous years on the LTSVP [Q0016-Q0018].

## Residence Pass and other relatives

- Carried over unchanged in substance; all ids re-checked against claims.py output (Z0018, Z0048, Z0049, Z0069-Z0073, E0131-E0133; C0015-C0020, Z0029, Z0074-Z0076, Z0099, Z0100, S0007, E0057, K0031).
- Residence Pass status check is on IMI's myOnlinePasResiden [E0136].
- Residence Pass processing time: IMI's client charter (imi-client-charter) lists no Residence Pass line. Need to know kept. Appeal: nothing found.

## Complaint routes (Immigration)

- IMI SISPAA (imi.spab.gov.my/eApps/system/index.do) confirmed by Firecrawl scrape: new complaint ("Aduan/Maklum Balas Baharu") and check status ("Semak Aduan/Maklum Balas") [Q0046]; linked from IMI's own site [Q0067].
- IMI Integrity Division complaints unit for officer misconduct or bribery: address, aduanintegriti@imi.gov.my, 03-8880 1246, QR online form, Whistleblower Protection Act 2010 protection if the complainant identifies themselves [Q0068-Q0070].
- Berita Harian (Apr 2026, via search snippet only, not saved) gives IMI's illegal-immigrant reporting line 03-8880 1374 and aduanpati_hq@imi.gov.my; not used.
- EAIC (Enforcement Agencies Integrity Commission) also takes complaints about enforcement officers including Immigration (search result only, eaic.gov.my not saved). Not used in the doc.
- No evidence found on how long SISPAA answers take, or that the Bangladesh High Commission helps with family-pass cases. Outside bodies (ILO, IOM, NGOs) have no role in non-worker pass applications in anything found.
- Note: raw/imi-faq-plsxpats-fc.md was logged with URL ".../soalan-lazim-plsxpats/#fc" because the plain URL was already fetched by curl (empty FAQ body); the scrape adds the SISPAA link and HQ phone.

## MM2H

- Medical check after approval at a MOTAC panel clinic; FD withdrawal up to 50%; OSC MM2H; renewal RM500/year + visa RM0-50; contacts [Q0039-Q0044].
- Fee conflict (not resolved): mm2h.gov.my gives RM5,000 processing per principal [E0107]; MOTAC's 1 Aug 2025 system notice gives "Fi proses: RM500 (tidak termasuk SST) bagi setiap permohonan" [E0118]. Possibly a separate system fee. Need to know kept.
- Child age conflict: mm2h.gov.my (Feb 2026) max 34 [E0104, E0110]; MOTAC "Insights on the Categories" PDF (Jan 2025) max 35 [E0111]. Newer official site used; conflict dropped from the doc.
- IMI's undated MM2H page still has part-time work guidelines [Z0089]; MOTAC's current site says only Platinum may work [E0112]. Current MOTAC rule used.
- MM2H and PVIP time does not count for permanent residence (Entry Permit e-book 2.5) [Q0015].
- Reality check:
  - DayakDaily, 18 Apr 2024 [Q0047, Q0048]: Tourism Minister Tiong: agents charged tens of thousands of ringgit, paying an agent doesn't guarantee approval, agents lost contact and clients couldn't recover money; some "agents" were shell entities leasing licences.
  - The Star, 17 Oct 2024 [Q0049]: all agents told to re-register; 229 recognised agent companies; Certificates of Good Conduct and police screening now mandatory; ~30-day review period. 34 of 249 applications approved by 14 Oct 2024 (statistic, not used).
  - The Star, 27 Aug 2026 [Q0050]: minister says MM2H agents must comply with the laws of the countries where they recruit; a Malaysian licence doesn't meet other countries' rules.
  - Bangladesh side: Desh Rupantor, Apr 2024 [N0051]: Bangladesh Bank spokesperson Mezbaul Haque said BB never approved remittances for MM2H, so the money did not go through legal channels; ACC lawyer says ACC can act only on a referral. TBS 2024: 3,604 Bangladeshi MM2H pass holders as of 31 Jan 2024 (statistic, not used). Daily Star Bangla (news-dailystar-bn-premium-visa-mm2h) on Bangladeshis as a top applicant group (not used).
  - Expat.com forum post (c. 2018, not saved): agent vanished after the visa fee and kept original documents.
- Bangladesh Bank rule: no official text found. Searched English and Bangla (GFET capital account, "বিদেশে বাড়ি কেনা বাংলাদেশ ব্যাংকের অনুমতি"), Firecrawl search; bb.org.bd GFET PDFs return HTML; US State Dept investment climate statement returned 403. Secondary sources: Capital Account Transaction (Equity Investment Abroad) Rules 2022 require BB permission for equity investment abroad (companies). Need to know kept; blocked list has the GFET request.
- MOTAC complaints: MOTAC SISPAA at motac.spab.gov.my confirmed by Firecrawl [Q0045]. News (Bernama/Sinar Harian, NST 2022/2025) shows MOTAC tells scam victims to file on SISPAA plus a police report, with receipts; not saved, not used. No evidence MOTAC has recovered money for MM2H applicants.
- MM2H contact email on mm2h.gov.my is Cloudflare-obfuscated; decodes to info@motac.gov.my, but the saved text copy doesn't contain it, so not cited.
- MOTAC's step-by-step MM2H guide PDF is broken/image-only (blocked list).

## DE Rantau

- FAQ v11 (1 Nov 2026): English only; approval letter valid 6 months; eVISA or VDR; normal counter, not autogate; tourist-pass holders must exit and re-enter; endorsement documents incl. LHDN tax registration slip; endorsement within 1 month of entry; stay until e-Pass [Q0051-Q0058].
- Document checklists (Nov 2025) [Q0072-Q0076]. Conflict: freelancer checklist allows "foreign or Malaysian clients" [Q0075] while the FAQ wording logged as Z0066 asks for contracts with foreign clients. Kept as a Need to know because it changes who can apply.
- Budget 2027: holders who reached the two-year limit get two more years, subject to conditions [Q0004]; consistent with the enhanced framework (48 months, E0086/E0098).
- MDEC's 2024 FAQ for China and Bangladesh (v4.0, 28 May 2024): bank guarantee requirement for these nationals waived [Q0071]. Superseded FAQ; not used in the doc. Bond for Bangladeshis RM750 in both.
- Scams: MDEC FAQ Q22 says no agent or MDEC can guarantee approval [E0094]; Q23 says legal threats don't change processing. No news found of DE Rantau scams aimed at Bangladeshis (English search). Sun report (undated, not saved): a holder told to leave after 2 months. MDEC complaint channel not found. Need to know kept.

## Other passes

- RP-T: TalentCorp page: register interest via contact form; EP with more than 3 months' validity; contacts [Q0059-Q0061]. No nationality restriction stated, so the old "whether Bangladeshis are eligible" gap was dropped. Fee, processing time and appeal not on the page.
- PLS@XPATS: IMI's FAQ page exists but has no questions (empty, dated 28 Oct 2022) [Q0067]. Eligibility and fee not found.
- Permanent residence: IMI's Entry Permit e-book (Google Drive folder linked from imi.gov.my; file "e-BOOK GARIS PANDUAN PERMOHONAN PERMIT MASUK (OKT '26).pdf"; cover says SEPT '25) fetched via drive.usercontent.google.com, 39 MB, text layer fine. Resolves the old Need to know on criteria, office, fee, time and appeal [Q0014-Q0038]:
  - Categories: wife, husband, biological child under 18 of a citizen, and fully foreign (WAS: investors, experts, professionals recognised by a regulating agency; 5 continuous years on EP/Student/PVP/Residence Pass).
  - PLKS, UNHCR card and IMM.13 holders excluded from the spouse categories; MM2H, PVIP, PLKS, UNHCR, IMM.13 excluded from WAS. This answers the mentor's "PR for PLKS workers: as far as I know, no": confirmed no.
  - Nearest Immigration office; interview; PDRM screening; status after 6 months online; fee RM120 cashless; deposit RM750 for Bangladeshis (WAS); appeal within 30 days to the Home Minister via KSU KDN; reapply after 1 year; processing now 6 months (DG's preface).
  - Copies of foreign documents: home MOFA or home embassy in Malaysia attestation, translation, then re-attestation by a Malaysian mission or Wisma Putra [Q0035].
  - The REP-specific guideline [Z0080-Z0083] is now covered by the general e-book (same appeal address), so REP detail was cut from the doc as not relevant to Bangladeshis.
- MTEP, Investor Pass: nationality restriction not checked in this pass; kept as Need to know.

## Fix round 2 (7 Nov 2026): checker failures on drafts/MY6.md

- Category III band: the pre-1 June 2026 band is RM3,000-4,999 [E0012]; E0019 gives no salary. Fixed.
- Spouse of a Category I holder: RM20,000 now cited to E0009.
- Permission to Study: counters closed to paper submissions from 1 Nov 2026 [Q0078]. No fee or charter time for PTS found in the ESD guidebook v6, the fee revision FAQ, the MyXpats FAQ or the key-services page: Need to know.
- Bangladesh-side attestation: read the BHC KL attestation checklist PDF (image-only, 2 pages) and the MoFA Dhaka citizen charter PDF (scanned, 12 pages; pp.1-6 read (items 1-32: attestation, then welfare services); pp.7-12 not read in this round). Logged Q0079-Q0084. MoFA Dhaka: family and marriage documents go via notary public and Ministry of Law, two sets, submit 8-12, collect 2-3 pm same day, free (charter dated 24 Aug 2022). BHC KL wants marriage certificates attested by both Law Ministry and MoFA Dhaka first; birth certificates attested in Dhaka or with online-verification proof; one extra set of copies. BHC KL counter hours and turnaround for attestation not published on the fee page, checklist or labour FAQ (the labour FAQ gives 9:30-1:00 only for travel permits): Need to know.
- Personal bond: ESD guidebook describes it as a written undertaking backed by a Malaysian company representative's pledge of a nationality-based sum [Q0086]; the IMI personal bond form says the sum is deposited with the Government and forfeited on default (raw/imi-personal-bond-form.txt), but nothing official says how an ESD dependant's LTSVP bond is paid or refunded. Need to know kept.
- MYXpats Centre gloss now cited to E0001.
- Marriage to a Malaysian: found IMI's form "Permohonan Pengesahan Pas bagi Tujuan Perkahwinan Warganegara Asing" (2022 upload; PDF created 2006) [Q0087, Q0088]: applied for by the citizen, not open to PLKS holders, any state Immigration HQ, documents listed; no fee given. IMI's Facebook (Nov 2026, "PEMEGANG PLKS BOLEH BERKAHWIN DI MALAYSIA? JAWAPANNYA TIDAK") repeats the special-form rule but Facebook can't be scraped (Firecrawl unsupported, curl fails); Q0010 kept for the deportation consequence. BHC KL's requirement for a Bangladeshi marrying a Malaysian logged as Q0081.
- Spouse LTSVP: form links from IMI's new-spouse page [Q0111]; Naziran inspection [Q0089]. Fee: Firecrawl search of imi.gov.my found only RM90 for a dependant/guardian LTSVP (Student Pass page, S0007) and a Scribd copy of an old IMI document mentioning a deposit for citizen's spouses (not official host, not used). Need to know kept.
- Spouse work permission: added Borang_Maklumat and MyData SSM form [Q0090, Q0091]. Office: the newer, top block of the IMI LTSVP page says the state where the applicant works [Z0097]; the older lower block says Putrajaya HQ or nearest state office [Z0098]. Doc uses Z0097 with one Need to know.
- Residence Pass: dropped the inferred "living spouse is not a category" sentence.
- Other relatives: office now cited to Z0046. Bangladesh High Commission and family passes: read the Labour Wing FAQ PDF in full (3 pages, image-only) [Q0085] and the citizen charter; neither covers family passes. Need to know kept.
- MM2H: dropped the High Commission inference; N0051 and Q0050 rewritten as plain rules; Q0049 moved out of the Need to know and pointed to the PLKS Step 4 police clearance (which carries the Tk 1,500 vs Tk 500 conflict).
- DE Rantau: income "at least"; over-18 rule [E0084]; freelancer conflict reduced to one Need to know line; insurance requirement from the remote-worker checklist [Q0109] (no minimum cover or insurer list found in the FAQ v11, enhanced FAQ or checklists: Need to know); eVISA charges and time borrowed from the tourist section [V0005, V0006, V0012, V0016, V0017, V0019]; VDR cost not found: Need to know. Complaint route: MDEC's DE Rantau page gives expatctr@mdec.com.my and 03-8315 3106/3157 [Q0097]; MDEC contact form [Q0098]. MDEC's Facebook announcement (same email) could not be scraped.
- RP-T: fetched rpt.talentcorp.com.my fees (Firecrawl; curl copy near-empty) and FAQ (curl) [Q0099-Q0102, Q0110]. Old "register interest" step and Need to know replaced.
- MTEP: sponsor rules and RM5,400 fee [Q0103]; URL mdec.my/mtep.
- Investor Pass: Xpats Gateway URL [Q0107]. PVIP: portal URL [Q0104], registration check [Q0105]; Firecrawl search found no published IMI list of appointed agencies. PLS@XPATS URL [Q0106].
- Entry Permit: Appendix C1-C3 checklists transcribed from page images (e-book pp.57-59) [Q0096]; issuing procedure per section 10 [Q0094, Q0095]; deposit paid at application per 3.19 [Q0093]; points calculator [E0136].
- MACS: STO booking URL and form link [Q0108]; no fee or time on the MACS page: Need to know.
- Not used: raw/talentcorp-rpt-fees.md and raw/mdec-contact-us.md (curl copies, empty; Firecrawl copies are the -fc files).

## Need to know (open, as in drafts/MY6.md after fix round 2)

1. EP family: how long an LTSVP is approved for at a time (conflict E0147/E0148).
2. BHC KL counter hours and turnaround for attestation; Malaysian High Commission in Dhaka's procedure and fee for certifying family documents.
3. Whether the RM750 LTSVP personal bond is paid as a deposit, and whether and when it is returned.
4. Whether a refused Dependant Pass or LTSVP can be appealed.
5. Conditions for Category I spouses working on a Dependant Pass from 1 Jan 2027.
6. Permission to Study: fee, processing time, what the holder receives.
7. Any official warning about family-pass scams.
8. Marriage pass-confirmation form: fee and time.
9. Citizen's spouse LTSVP: fee; whether a refusal can be appealed.
10. Spouse work permission: whether it can also be applied for at Putrajaya HQ or the nearest state office; fee and time.
11. Residence Pass: processing time; appeal.
12. Other relatives' LTSVP: whether holders may work; fees for other categories; appeal.
13. SISPAA response time; whether the Bangladesh High Commission helps with family-pass cases.
14. MM2H: Bangladesh Bank's written rule and how to ask permission.
15. MM2H: whether the RM500 system fee is on top of RM5,000; full document list; processing time.
16. MM2H: how to appeal and by when.
17. MM2H: whether MOTAC has ever recovered money for a cheated applicant.
18. DE Rantau: minimum insurance cover and accepted insurers.
19. DE Rantau: whether contracts with Malaysian clients count.
20. DE Rantau: cost, documents and processing time of a VDR.
21. DE Rantau: any official scam warning.
22. MTEP: processing time, appeal, nationality restriction.
23. Investor Pass: appeal, nationality restriction.
24. PVIP: where IMI publishes the appointed-agency list; processing time; appeal.
25. PLS@XPATS: eligibility, fee, appeal.
26. MACS: fee and processing time.

## Conflicts

- E0147 vs E0148 (LTSVP duration).
- E0038 vs E0145/Q0001 (DP work) - resolved toward ESD.
- Z0097 vs Z0098 (spouse work-endorsement office).
- E0107 vs E0118 (MM2H processing fee).
- E0146/E0104 vs E0111 (MM2H child age 34 vs 35) - newer official used.
- Q0075 vs Z0066 (DE Rantau freelancer clients).
- Q0062 vs Q0077 (BHC KL attestation fee RM42 vs RM45) - newer page used.

## Blocked

See blocked-parts/Q.md: MOTAC MM2H guide (broken/image PDF); Bangladesh Bank GFET capital-account chapter.
