# Round 2 verifier r2b: changed lines 561-1150

Lines checked (from r2-changed-lines.txt, 561-1150): 575, 596, 601, 614, 616, 637, 639, 661, 673-676, 683, 685, 689, 690, 699, 706, 735, 758, 774, 776, 779-796, 802, 815, 840, 854, 856, 895, 918, 929, 937, 960, 966, 976, 1025, 1027, 1041, 1064, 1067, 1074-1077, 1080.

### L616 UNSUPPORTED
- sentence: "In the worst fire, on 10 November 2022, a blaze in a garage at M. Nirufehi in Malé ..."
- cited: R0025, R0030, R0026, R0029, R0032
- evidence says: none of the cited facts says it was the worst fire. R0033 (same PSM article as R0032, not cited) says: "The incident is the most deadly fire incident to occur in the Maldives."
- fix: add R0033 to the citation: [R0025, R0030, R0026, R0029, R0032, R0033]

### L840 UNSUPPORTED
- sentence: "In 2024 BOESL, the state recruiting agency, recruited 76 doctors, medical officers and specialists for the Maldives Ministry of Health on 2-year contracts [B0156]."
- cited: B0156
- evidence says: B0156 is a BMET permission letter (MV-RL0147-2024-0013954, 11 Jun 2024): "BOESL, 76 doctors (medical officers and specialists) for the Ministry of Health, Maldives ... 2-year contract". It shows permission to recruit, not that 76 were recruited; and the 76 are doctors who are medical officers and specialists, not three groups. L209 words it correctly.
- fix: In June 2024 BOESL, the state recruiting agency, got BMET permission to send 76 doctors (medical officers and specialists) to the Maldives Ministry of Health on 2-year contracts [B0156].

TOTAL: 2
