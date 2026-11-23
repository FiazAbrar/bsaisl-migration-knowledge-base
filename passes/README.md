# Passes

One folder per research or editing pass, so every change to the docs can be traced back to its briefs, drafts, checker verdicts and fixes (see METHOD.md, sections 9 and 11). The evidence itself (saved sources, facts.csv) stays in each doc's folder; these folders hold the process.

Each folder has `PASS.md` (what the pass did and how it was checked), `briefs/` (the specs given to agents), `drafts/` (what agents produced before checking), `checks/` (checker verdicts and the fixes they proposed), `scripts/` (the scripts run) and, where kept, `fixes-applied.json`.

Inputs too large for git (the Prothom Alo article dumps, 319 MB raw and 23 MB filtered) stay outside the repo, on the project owner's machine; each PASS.md says which.

## Fact prefix register

| Prefix | Doc folder | Pass |
|---|---|---|
| PA | cross-country | 2026-11-22-prothom-alo-scams-1 |
| LB, AA, AB, FV, RU, OA, OB | cross-country | 2026-11-23-prothom-alo-scams-2 |
| MA, MB | countries/malaysia | 2026-11-23-prothom-alo-scams-2 |
| PF | agencies | 2026-11-23-prothom-alo-agency-flags |
| MP | countries/malaysia | 2026-11-23-prothom-alo-malaysia-saudi |
| SP | countries/saudi-arabia | 2026-11-23-prothom-alo-malaysia-saudi |
| CQ | cross-country (now global/) | 2026-11-23-prothom-alo-malaysia-saudi |
| GF, GS, GD, GI | global/faq, dalal-scams, departure, illegal-routes | 2026-11-23-prothom-alo-global |
| GM, GV, GO | global/money, services, other-destinations (new docs) | 2026-11-23-prothom-alo-global |
| PU, PI, PJ, PQ, PO, PK, PS, PD, PR, PB, PY, PM, PC, SQ; MP0772 on | countries (existing docs) | 2026-11-23-prothom-alo-countries |
| XU, XC, XK, XI, XL, XG | countries/united-states, canada, united-kingdom, india, lebanon, greece (new docs) | 2026-11-23-prothom-alo-countries |
