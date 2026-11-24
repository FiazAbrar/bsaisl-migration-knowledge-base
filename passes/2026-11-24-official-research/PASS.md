# Official-source research on the docs built from news

24 Nov 2026. The six country docs and three global docs first built from Prothom Alo reporting got the research pass CLAUDE.md requires: official sources found and saved, the "Need to know" questions answered where official pages answer them, and news claims replaced or backed by official ones.

| Doc | New facts | Official sources registered (doc total) | Fixes from the independent check |
|---|---|---|---|
| `countries/united-states` | 127 (OU) | 27 | 14 |
| `countries/canada` | 155 (OC) | 67 | 5 |
| `countries/united-kingdom` | 220 (OK) | 38 | 9 |
| `countries/india` | 107 (OI) | 18 | 9 |
| `countries/lebanon` | 96 (OL) | 25 | 13 |
| `countries/greece` | 96 (OG) | 27 | 11 |
| `global/money` | 126 (OM) | 29 | 14 |
| `global/services` | 127 (OV) | 31 | 15 |
| `global/other-destinations` | 230 (OD) | 59 | 12 |

1284 facts in all; 102 fixes from the checks.

## How

1. **One research agent per doc** (`briefs/RESEARCH-SPEC.md`): made a list of every Need to know and every rule, fee, office or number the doc stated from news alone; searched official sources first (the destination's immigration and labour ministries and visa portals, embassies, BMET, the Ministry of Expatriates' Welfare, the Wage Earners' Welfare Board, PKB, Bangladesh Bank, NBR), then international bodies; saved every page with `fetch.py` or `wayback.py`; logged each fact with its exact quote and status (verified, possibly-outdated); rewrote the doc where official facts change it; recorded conflicts and pages it could not download in `notes.md`. Other destinations, with 25 countries, took two agents in turn.
2. **Independent check** (`briefs/FINAL-CHECK-SPEC.md`, verdicts in `checks/rfix-*.json`): every new or changed sentence against its facts, plus: each official quote is really in the saved page, each "official" source is really official, and scanned or OCR'd text matches the image. Fixes applied with `scripts/apply_fixes.py`; where a fix would have deleted a true statement that lacked a fact, the fact was logged from the saved source instead.
3. **Cross-doc alignment:** the FAQ's PKB loan lines and the Illegal routes doc's US visa-bond section now follow the official pages found here; the Probashi Card status matches across the money, services and FAQ docs.

## Decisions recorded

- Visa-centre contractors appointed by an embassy (VFS, GVCW, IVAC) count as official for the checklists and fees they publish; a ministry page is cited instead wherever one states the same rule.
- A third party's copy of an official page (AILA's copy of the State Department's pause notice) is not official; its facts are marked unofficial until the live page is saved.
- Primary documents beat news and secondhand summaries (for example India's CAA cut-off, the UK's asylum numbers, Greece's 2025 penalties, PKB's loan terms).

## Also in this PR

- **Agency flags:** the 1,110 articles used in the 23 Nov passes were checked for agency flags (`agency-flags/`): 162 name a firm; one new row (Lamisa Enterprise, PF0133).

## Limits

- Pages that blocked automated reading are listed in `PAGES-TO-DOWNLOAD.md` and in each doc's `notes.md`; their content is not in the docs.
- Some quotes were retyped from garbled or scanned PDFs and checked by eye, not by the automatic quote check; each carries a note.
