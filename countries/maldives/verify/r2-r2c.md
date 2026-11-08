# Round 2 verifier r2c: doc.md changed lines 1151 and higher (from r2-changed-lines.txt)

Lines checked: 1156, 1178, 1232, 1238-1252, 1257-1260, 1266-1270, 1273, 1302, 1304, 1333, 1337, 1342-1404, 1442, 1463, 1466, 1476, 1492, 1541, 1557, 1572, 1579-1588, 1602. Cross-references in these lines were checked against the doc's headings (all resolve to unique headings or items).

### L1240 NUMBER
- sentence: "It is applied for on form IM22, signed by a sponsor that takes full responsibility for the person, and costs MVR 750 (about Tk 6,000) for each three months or part [V0052, V0037, G0015, G0014]."
- cited: V0052, V0037, G0015, G0014
- evidence says: Immigration Act fee schedule: "Amongst persons granted a special visa, for persons specified in Section 17 (b), (c) and (e) Ruffiya 750/- for every three months or part of the three months." Section 17(b) is continuing medical treatment, (c) legal proceedings to seek a right, (e) taking part in organised programmes or events. No fee is set for (a) humanitarian work or (d) a government authority finding it imperative, both of which the previous sentence lists. The sentence applies the MVR 750 fee to every special visa.
- fix: It is applied for on form IM22, signed by a sponsor that takes full responsibility for the person; to continue medical treatment or finish a court case it costs MVR 750 (about Tk 6,000) for each three months or part [V0052, V0037, G0015, G0014].

### L1476 OUTDATED
- sentence: "Under the 2021 regulation it must also tell the family and the Bangladesh High Commission and pay for burial, or send the body home if the family wishes, arranged with the family [L0130, L0131]. The 2023 regulation also made the employer pay burial costs [L0138]."
- cited: L0130, L0131, L0138
- evidence says: L0130/L0131 come from the 2021 Regulation on Foreign Employment, and L0138 from the 2023 regulation (ILO 2024 summary). The doc itself says "the rules now in force are Regulation 2025/R-120 (Regulation on Expatriate Employment)" [U0086], published 14 December 2025 [W0047]. The sentence sits under "The employer's duties" and uses "must", so it presents a superseded regulation's duties as current. No fact in facts.csv gives the death duties under 2025/R-120.
- fix: The 2021 and 2023 regulations, since replaced by Regulation 2025/R-120, made the employer tell the family and the Bangladesh High Commission and pay for burial, or send the body home if the family wished, arranged with the family [L0130, L0131, L0138, U0086]. (Add a Need to know line after the list: "Does Regulation 2025/R-120 still make the employer tell the family and High Commission, pay for burial or send the body home?")

### L1348 UNSUPPORTED
- sentence: "Most undocumented Bangladeshis entered on a work permit and lost their status after arrival [U0051, U0059]."
- cited: U0051, U0059
- evidence says: U0051: "over 70 percent of Bangladeshi workers entered the Maldives through legal channels. But the majority fell into irregular status post-migration." U0059: 44.01% of undocumented respondents "reported migrating through irregular channels" (so 55.99% arrived legally). Neither source says the legal entry was on a work permit.
- fix: Most undocumented Bangladeshis entered legally and lost their status after arrival [U0051, U0059].

### L1377 UNSUPPORTED
- sentence: "work permit expired, or reported missing or "Missing Abscond" before 31 December 2025;"
- cited: U0012 (lead-in citation on L1374)
- evidence says: "Status Cut-off: Work Permit expired / Status Cut-off: Work Permit marked as 'Missing (Abscond)' before 31-Dec-2025." "Reported missing" also covers "Missing Negligence", which the same guide excludes from legalisation (U0018), and the doc says so on L1382.
- fix: work permit expired, or marked "Missing (Abscond)" before 31 December 2025;

### L1304 UNSUPPORTED
- sentence: "Since 25 September 2026, employers must pay all foreign workers' salaries and benefits into a bank account in the worker's own name at a bank licensed by the MMA (how to open one: Step 7: After arrival, item 7) [W0147, G0017, G0018]."
- cited: W0147, G0017, G0018
- evidence says: the Atoll Times sources behind W0147/G0017/G0018 mention only "salaries" ("salaries payable to foreign employees ... must be deposited into accounts opened in the employees' names"). "Benefits" appears only in the Adhadhu article behind G0020 ("all salaries and benefits due to expatriate employees ... must be deposited into an account held in the employee's name"), which this sentence does not cite.
- fix: replace "[W0147, G0017, G0018]" with "[W0147, G0017, G0018, G0020]"

### L1572 UNSUPPORTED
- sentence: "Sample wording: "I came to the Maldives in [year] for work. I have no valid passport. I need to return to Bangladesh urgently. I attach the papers and fee and request a travel permit." [B0167]."
- cited: B0167
- evidence says: B0167 (read from the page image, per its note) lists the attachments as "১। পাসপোর্ট কপি/জাতীয় পরিচয় পত্র/ জন্ম নিবন্ধন সনদ কপি ২। ছবি পাসপোর্ট সাইজ-১, স্টাম্প সাইজ-১টা ৩। ইমিগ্রেশন ক্লিয়ারেন্স কপি": a passport, NID or birth certificate copy, photos and the immigration clearance copy. The High Commission's sample does not mention a fee. (The PDF has no usable text layer and could not be rendered here, so this relies on the fact's note.)
- fix: replace "I attach the papers and fee and request a travel permit." with "I attach the papers and request a travel permit."

TOTAL: 6
