# Prothom Alo archive into the global docs

23 Nov 2026. The relevant Prothom Alo articles (1 Jan 2024 to 22 Nov 2026) about the Bangladesh side of migration, or about countries with no doc of their own, were read in full into the global docs. Three new global docs were started because about 460 Bangladesh-side articles had no home: Sending money home, Services for migrants and their families, and Other destinations.

## What changed

| Doc | New facts | Fixes from the final check |
|---|---|---|
| Illegal routes | 465 (GI) | 7 |
| Sending money home (new) | 428 (GM) | 12 |
| Other destinations (new, 24 countries) | 380 (GO) | 15 |
| Services for migrants and their families (new) | 357 (GV) | 28 |
| FAQ | 188 (GF) | 10 |
| Departure bottlenecks | 181 (GD) | 9 |
| Dalal scams | 116 (GS) | 17 |

About 2,115 facts, each with an exact Bangla quote checked against the saved article.

## How

The same simplified process as the country pass (METHOD.md, section 12; briefs in `briefs/`): one agent per doc and chunk read, logged and wrote; chunks of the same doc ran one after another; facts for other docs were held and placed later (`briefs/HELD-SPEC.md`, outcomes in `ledgers/heldout*.json`); stories the keyword filter had rejected were triaged (`ledgers/rejected-triage.json`: 117 of 472 useful) and read in full; then an independent final check of every new or changed sentence (`checks/`), including whether the FAQ's short answers agree with the fuller docs. Conflicts were settled from the sources and recorded in each `notes.md` (for example the remittance incentive at 2.5% per the June 2026 budget; PKB's rehabilitation loan at 9% and Tk 3 lakh per PKB's own page; Mediterranean crossings since 2009 per Frontex; the March 2026 Tobruk boat counts).

## Coverage

`datasets/prothom-alo-migration/coverage/ledger.csv` lists every story any pass looked at (1,904) and what happened to it: used in a doc (1,365), read with nothing new (261), not relevant (203), used in the earlier passes of 22 and 23 Nov (75). None is unaccounted for. Script: `scripts/build_ledger.py`. Not checked: 1,495 rejected stories carrying a single weak migration keyword and none in the headline.

## Limits

- The three new docs cite news only; their "Need to know" bullets list what an official research pass must find first.
- `questions.md` for the four older global docs keeps its curated wording, so questions answered in this pass whose wording differed could not be matched and removed automatically.
