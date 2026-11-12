# Jordan doc: coverage audit

**1. Migrant's questions.** Covered: how long you can stay (one-year permits on a 3-year contract, residence fines), what you earn (JD 230 split into JD 130 cash and JD 100 in kind, BOESL notices, reported pay), rights at work (two full sections), what gets you jailed or deported, bank, e-wallet and SIM (with Need to know on SIM papers and banks), pension (SSC lump sum plus Probash and WEDB), family (garment workers can't bring family; Family residence and Having a child sections), what you can bring home (Bangladesh baggage rules, Jordan cash declaration). Gap: the doc says how to claim the SSC lump sum but leaves out a reported practical block, that the employer's written consent has been needed.

**2. Original aim.** Each visa has types, requirements, where to apply, cost and scams. Appeal, processing time and "can the holder bring a spouse or have a child" are either answered or carried as Need to know, with one exception: the domestic-worker route has no processing time and no question asking for it. Changing visa type, asylum (written to discourage) and corridor information (BMET series, Egyptians against Bangladeshis, bans 2006 to 2026, growth asks) are all present. Gaps: the Entry without prior approval section leaves out the five-year multiple-entry border visa that the same decision gives to eligible travellers. The regularisation section doesn't say the October 2026 extension also covers the Aqaba Special Economic Zone, where many garment factories are. That matters because Aqaba garment workers are otherwise told they are excluded.

**3. Insider test.** Present: BOESL and its factories (Classic, Jerash, Needle Craft/Fine Apparel, Tusker, Mas Al Safi, Prestige, Sana, United Creation), Surah Travels' fake Jerash visas, the Shyamoli arrests of touts, brokers selling BOESL test places (including the nail-polish signal), Tureza Akter, Achilles Apparel, the 2006 to 2010 ban, the 2011 abuse reports, the 2014 domestic-worker suspension, the June 2026 recruitment stop, the Iran war, the amnesty rumour, real costs set against the cap, pregnancy testing, passports kept, the Juweideh detentions, Nazma Begum's trafficking and the MH International child case. Not in the doc and with no fact behind it: the 2011 Classic Fashion sexual-abuse allegations by name. That is left as is; the "Late 2011" ban entry covers what changes a decision.

Of the 271 facts in facts.csv not cited in doc.md, about 220 duplicate a cited fact (the H/KC/D Labour Law and MOL-guide rows, the BOESL notice rows, the R/KF SSC rows), are superseded by newer or official facts (D0147 and R0195 give a 3-year re-entry ban against KC0039's 5 years; V0236 says the period ended 30 September, which the extension overrides; H0142 says 90 days against KC0108's 60), or are statistics or trivia (A0042, H0198, D0194, D0230, A0068, V0145). These were rightly left out. Five fill a gap and are used below: D0173, KF0005, V0019, V0203, G0103, plus R0235 and R0236 for MOL's mobile numbers. D0169 (most MoUs set no base wage) and D0170 (no recruitment office closed in 2024) were judged not to change a decision. V0202's quote is truncated, so it was not used.

### FAIL Employer consent for the SSC lump sum
old: Holding the no-objection no longer stops you being issued a work permit in Jordan later [KC0096].
new: Holding the no-objection no longer stops you being issued a work permit in Jordan later [KC0096]. Migrant workers have been unable to withdraw their contributions without the employer's written consent [D0173].

### FAIL Need to know: employer consent for the lump sum
old: > - How long does SSC's transfer of the lump sum to a Bangladeshi bank take, and what does it cost?
new: > - How long does SSC's transfer of the lump sum to a Bangladeshi bank take, and what does it cost?
> - Does SSC or MOL still require the employer's written consent before a migrant worker can draw the lump sum, and what does a worker do if the employer refuses?

### FAIL Regularisation extension covers Aqaba
old: domestic workers included, who came to Jordan to work and held a work permit before [KF0001, KF0002].
new: domestic workers included, who came to Jordan to work and held a work permit before [KF0001, KF0002]. The extension also applies in the Aqaba Special Economic Zone [KF0005].

### FAIL Need to know: Aqaba garment workers
old: > - Does the October 2026 extension, which names workers "in all sectors", keep the exclusion of QIZ garment workers [KF0001, R0153]?
new: > - Does the October 2026 extension, which names workers "in all sectors", keep the exclusion of QIZ garment workers [KF0001, R0153]?
> - Does the extension's coverage of the Aqaba Special Economic Zone include garment workers in Aqaba's factories [KF0005, R0153]?

### FAIL Five-year border visa for eligible residents
old: - **Schengen or US visa holders** may enter whether or not they have used that visa [KE0008].
new: - **Schengen or US visa holders** may enter whether or not they have used that visa [KE0008].
- **Eligible travellers** get a five-year multiple-entry visa at the border crossing, up to three months a visit, without prior security clearance [V0019].

### FAIL Hospitals and unmarried pregnant women
old: - **Detention after birth:** they are particularly at risk of detention and deportation if they give birth in a Jordanian hospital [V0193].
new: - **Detention after birth:** they are particularly at risk of detention and deportation if they give birth in a Jordanian hospital [V0193]. Hospital staff need not report an unmarried pregnant woman over 18 unless rape is suspected, but some hospitals call the police [V0203].

### FAIL BOESL skilled posts can cost the worker
old: repaid by the company before departure [A0071].
new: repaid by the company before departure [A0071]. For some highly skilled posts the worker bears extra cost [G0103].

### FAIL MOL mobile numbers and after-hours line
old: offices at 11 Issa Al-Naouri Street, Amman, Sunday-Thursday 8:30 am-3:30 pm [H0195, H0192, H0191, H0190, H0193].
new: offices at 11 Issa Al-Naouri Street, Amman, Sunday-Thursday 8:30 am-3:30 pm [H0195, H0192, H0191, H0190, H0193]. The labour-law line from a mobile: Zain 0796580666, Orange 0777580666, Umniah 0785602666; after 3:30 pm an answering machine takes complaints [R0235, R0236].

### FAIL Need to know: domestic-worker processing time
old: > - If MOI refuses the visa or the household cancels it before travel, does the worker get back anything she paid, and can the refusal be appealed?
new: > - If MOI refuses the visa or the household cancels it before travel, does the worker get back anything she paid, and can the refusal be appealed?
> - How long does a Jordan housemaid job take from the agency's selection to the flight?

PASS coverage: 9 fixes
