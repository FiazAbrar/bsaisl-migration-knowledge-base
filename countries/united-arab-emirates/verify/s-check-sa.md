# s-check-sa: changed lines 295-837

### 1. UNSUPPORTED
- line: 301
- old: 1. Fill in the form online at epassport.gov.bd [SA0010, G0083].
- new: 1. Fill in the form online at epassport.gov.bd [SA0010].
- why: G0083 is about a lost passport needing a UAE police report (bcgdubai-e-passport.md); nothing to do with this step. SA0010's source (dip-epassport-instructions-fc.md, URL epassport.gov.bd) supports it alone.

### 2. FAIL
- line: 751
- old: it includes a pregnancy test, and the office must arrange it within 30 days of your entry [SC0014, D0190, MB0003].
- new: it includes a pregnancy test [SC0014, D0190].   + NEED: Is the domestic worker's medical done within 30 days before entry (Executive Regulations) or within 30 days after entry (MOHRE recruitment manual)?
- why: MB0003 has status "conflict" (note: conflicts with D0010, 30 days BEFORE entry; third-party translation). Line 686 of the doc already states the opposite ("no more than 30 days before you enter the UAE [D0010]"), so the doc contradicts itself.

### 3. UNSUPPORTED
- line: 753
- old: then the residence sticker goes in your passport, for 1 year with a foreign resident employer or 2 years with an Emirati one [SC0014, SC0016].
- new: then the residence sticker goes in your passport [SC0014, SC0016]. The Emirates ID application is valid 1 year with a foreign resident employer or 2 years with an Emirati one [SC0015].
- why: tadbeer-process-new.md gives "Local (Emirati): 2 years / Expat: 1 year / GCC: 2 years" under Step 5 Emirates ID as "Validity of this application", not as the residence sticker's length. SC0016's quote says only that the sticker appears once approved.

### 4. FORMAT
- line: 747
- old: 4. **Go through the residence steps** (the employer or office applies; a private Tadbeer centre lists this order) [SC0014]:
- new: 4. **Go through the residence steps** (the employer or office applies) [SC0014]:
- why: "a private Tadbeer centre lists this order" says where the information comes from ("source X says"). The [N] citation already shows that.

### 5. FORMAT
- line: 813
- old: press 2 (domestic workers) and ask an agent;
- new: press 2 (domestic workers), choose to speak to a staff member and ask whether the office is licensed;
- why: the brief bans the word "agent" in the doc text, and it is ambiguous next to recruiting agencies. Source news-gulfnews-tadbeer-three-plans.md lines 46-49: "Select the option to speak to an agent ... ask them if the agency ... is registered". (D0134 is a 2022 Gulf News lead; MOHRE's phone menu may have changed.)

### 6. NUMBER (low confidence)
- line: 821
- old: Director (Employment) 01711111544, diremi@bmet.gov.bd [D0222].
- new: NEED: Which BMET officer and phone number handles written complaints against agencies: Director (Emigration) on 01711-135901, or Director (Employment) on 01711111544?
- why: D0222's quote gives only diremi@bmet.gov.bd, not the title or the phone number. B0020, cited at line 365, gives diremi@bmet.gov.bd to Director (Emigration) on 01711-135901, which looks inconsistent with this line. I could not check bmet-citizen-charter-2026 because the text layer is garbled and the pdftotext output is also garbled. B0020, B0021 and B0022 (lines 352 and 365) have empty quotes, so I could not check them against the source either.

TOTAL: 6 problems in lines 295-837
