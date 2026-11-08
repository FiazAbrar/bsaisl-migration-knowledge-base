# Round 2, r2a: changed lines 9-552

Scope: 54 changed lines between 1 and 560 from verify/r2-changed-lines.txt (9, 13, 15, 26, 29, 33, 34, 35, 40, 47, 48, 56, 70, 72, 79, 125, 134, 149, 158, 160, 166, 180, 192, 207, 209, 210, 229, 242, 244, 261, 285, 286, 292, 293, 350, 379, 387, 388, 400, 425, 434, 435, 448, 453, 455, 491, 501, 509, 518, 522, 535, 539, 550, 552).

### 1. UNSUPPORTED
- line: 535
- old: It does not apply to family-sponsored workers, a new permit with the same firm, skilled workers or Golden visa holders [L0129, G0127].
- new: Where the ban is for a proven work abandonment report, it does not apply to family-sponsored workers, a new permit with the same firm, workers at skill levels the UAE needs, or Golden visa holders [L0129, G0127].
- why: uae-portal-one-year-work-permit-ban.md: "the Decree-Law exempts the following categories of workers from the one-year ban in the case of a proven work abandonment complaint". The exemptions do not cover the probation-quit or fake-company grounds, and "skilled" is narrower in the source ("professional skill or knowledge levels required in the UAE").

### 2. FORMAT
- line: 518
- old: > - Is 80060 (the domestic-worker line in "Check it is real") still a working MOHRE number, alongside 80084 and 600590000?
- new: > - Does MOHRE still run 80060 (option 2 for domestic workers) for checking a recruitment office, alongside 80084 and 600590000?
- why: The pointer is broken. 80060 now appears nowhere else in doc.md: the round-1 coverage fix took it out of line 670 ("Check it is real"), while the round-1 v4 fix rewrote this question to point there. The number comes from D0134 (Gulf News, lead).

### 3. UNSUPPORTED
- line: 9
- old: A UAE job starts with a UAE company's MOHRE work permit for a named worker, and the law makes the employer pay every recruitment cost [W0060, N0129].
- new: A UAE job starts with a MOHRE offer letter and work permit issued to a UAE company for a named worker, and the law makes the employer pay every recruitment cost [W0009, N0129, W0060].
- why: N0129 (uae-portal-labour-visa-fraud-tips.md) covers only the MOHRE offer letter, and W0060 covers only costs. Nothing cited mentions a work permit. W0009 (uae-portal-job-offer-process.md) gives the sequence: job offer, contract, work permit, visa.

### 4. UNSUPPORTED
- line: 501
- old: For help, call 600590000 (24 hours; also WhatsApp) or the Labour Claims and Advisory Centre on 80084 (toll free) [L0055, L0149].
- new: For help, call 600590000 (24 hours; also WhatsApp) or the Labour Claims and Advisory Centre on 80084 (toll free) [W0072, L0055, L0149].
- why: The L0055 source (mohre-guidance-know-your-rights.txt l.258-260) gives the number and WhatsApp but not "24 hours". W0072 (mohre-new-work-permit-overseas.md: "Available 24/7") does. Line 535 gives 8 am-8 pm for the same number (L0130, for ban checks). Both are sourced, but a reader sees two different hours.

### 5. UNSUPPORTED
- line: 550
- old: 1. Call MOHRE on 600590000 (24 hours; also WhatsApp) and ask whether a work abandonment report is on your file [L0055].
- new: 1. Call MOHRE on 600590000 (24 hours; also WhatsApp) and ask whether a work abandonment report is on your file [W0072, L0055].
- why: Same as #4. L0055 does not give the hours; W0072 does.

### 6. FORMAT
- line: 26
- old: Affected returnees, organised as "Amra Remittance Joddha" (We Are Remittance Fighters), demanded monthly allowances of Tk 15,000-20,000, jobs in other countries and high-level talks with the UAE on 7 September 2026 [N0004].
- new: On 7 September 2026, affected returnees organised as "Amra Remittance Joddha" (We Are Remittance Fighters) demanded monthly allowances of Tk 15,000-20,000, jobs in other countries and high-level talks with the UAE [N0004].
- why: As written, the date reads as the date of the talks. news-bdnews24-uae-visa-cancel-jobs-2026-09.md says the demands were made at a Press Club briefing "on Monday" (7 Sept 2026, article dated 8 Sept).

### 7. NUMBER
- line: 48
- old: Saudi Arabia took 38.85 lakh over 2004-2024 [N0122].
- new: Saudi Arabia took 38.85 lakh from 2004 to April 2024 [N0122].
- why: news-dailystarbn-uae-remittance-top.md (1 May 2024) says "২০০৪ সাল থেকে এ পর্যন্ত", i.e. up to the article date, not all of 2024. Minor.

Checked and passed (no entry): the leave-cancellation framing and "no formal reason" (bdnews24 l.26/30, bdmonitor l.41); the minister's identity (Dhaka Post: Expatriates' Welfare Minister Ariful Haque Chowdhury); the embassy forwarding cases (bdmonitor l.19-25); the 2026 monthly clearances; all BMET ranks and totals; B0105 totals; GMI population figures; Dubai Taxi details; the special envoy and visa figures; partner-visa prices and penalties (Dibalok); the smart-card inquiry (Samakal names 9 BMET officials); the Navira letter; AED 4,000 = Tk 1.36 lakh; e-passport and PCC fees and codes; TTC list contacts (bmet-ttc-list-pdf.txt); WPS and Resolution 340 (85%); ILOE fees and policy-check steps (iloe-faq.md l.44-50); residence-law penalties (Art. 27, 29); labour-court deadlines (Art. 54(3)); probation notice rules; work-permit swap (twice within 6 months); and the abandonment rules. Need-to-know lines 29, 210, 286 and 435 are precise. No editing instructions are left in any line. Not verifiable here: Director (Employment) phone 01711111544 (D0222, read from the page image; the text layer is garbled and no PDF renderer is available).

TOTAL: 7 problems in lines 9-552
