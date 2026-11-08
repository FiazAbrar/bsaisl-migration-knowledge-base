# Round 2 verifier r2a: changed lines 1-560 of doc.md

Checked the 50 changed lines in r2-changed-lines.txt that fall between 1 and 560 (11, 22, 26, 34, 35, 36, 43, 52, 53, 54, 62, 68, 92, 105, 112, 124, 130, 158, 165, 181, 186, 204, 209, 213, 215, 220, 266, 267, 319, 327, 337, 345, 358, 362, 379, 417, 433, 435, 441, 453, 475, 482, 483, 485, 488, 492, 535, 538, 544, 554). Taka conversions, BMET counts, cross-references and acronym first uses in these lines check out except as below.

### L554 FAIL
- sentence: "A disciplinary suspension may last at most 14 days [L0008]. During it either side can end the job without notice [L0005], but the rules on hours, leave and pay still apply to you [L0184]."
- cited: L0008, L0005, L0184
- evidence says: L0005 "During probation either side may end the contract without notice"; L0184 "Probationers keep the rights in sections 32 to 57 (hours, leave, pay)". With the suspension sentence placed in between, "During it" now refers to the suspension, not probation.
- fix: Probation is at most 3 months [L0004]. During probation either side can end the job without notice [L0005], but the rules on hours, leave and pay still apply to you [L0184]. A disciplinary suspension may last at most 14 days [L0008].

### L124 UNSUPPORTED
- sentence: "A 2024 legal-aid study found work tied to debt in over 75% of cases [N0075]."
- cited: N0075
- evidence says: the finding comes from RMMRU Policy Brief 36, dated July 2023 ("the PILC research shows the employment of workers is tied to debt in more than 75 percent cases"), so the study is from 2023 or earlier, not 2024. It also sits under the "2024:" bullet.
- fix: move the sentence to the "2023:" bullet as: A legal-aid study (PILC) found work tied to debt in over 75% of cases [N0075].

### L53 UNSUPPORTED
- sentence: "Bangladeshis got 17,039 of the 75,542 work permits given to arriving foreigners from 17 November 2023 to 30 January 2025 [N0024]."
- cited: N0024
- evidence says: "a total of 75,542 foreigners had arrived in the country under work permits between November 17, 2023 and January 30, 2025. During the same period, work permits were issued to 17,039 Bangladeshis." The source gives arrivals and permits issued as two separate figures, not 17,039 as a share of 75,542 permits.
- fix: From 17 November 2023 to 30 January 2025, 75,542 foreigners arrived on work permits and 17,039 work permits were issued to Bangladeshis [N0024].

### L417 UNCITED
- sentence: "The Maldives side (MQA recognition) is in Work visa: professional (teachers, doctors, nurses, engineers)."
- cited: none
- evidence says: n/a (W0012 covers MQA recognition for professional permits)
- fix: The Maldives side (MQA recognition) is in Work visa: professional (teachers, doctors, nurses, engineers) [W0012].

### L22 UNSUPPORTED
- sentence: "Regulation 2025/R-120 ends quotas for accountants two years, and for nurses three years, after 14 December 2025"
- cited: N0101, N0102, W0139, W0140, W0047
- evidence says: W0139/W0140 say only "must be cancelled after two years" / "after three years", and W0047 gives the publication date. Neither ties the period to the regulation's start. N0106 (rules gazetted December 2025, "more jobs phased out over 2-5 years") and the Atoll Times source ("after three years from the date the rules came into force") do.
- fix: add N0106 to the citation: [N0101, N0102, W0139, W0140, W0047, N0106]

TOTAL: 5
