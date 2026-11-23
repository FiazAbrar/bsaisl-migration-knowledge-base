# Prothom Alo archive into the country docs

23 Nov 2026. Every relevant Prothom Alo article (1 Jan 2024 to 22 Nov 2026) that earlier passes had not used was routed to the country it is about and read in full. Thirteen existing country docs were extended; six countries with enough reporting got a first doc built from that reporting alone.

## What changed

| Doc | New facts | Fixes from the final check |
|---|---|---|
| Italy | 416 (PI) | 20 |
| United Arab Emirates | 185 (PU) | 16 |
| Japan | 115 (PJ) | 19 |
| South Korea | 57 (PR) | 8 |
| Kuwait | 51 (PK) | 6 |
| Saudi Arabia | 51 (SQ) | 8 |
| Oman | 47 (PO) | 6 |
| Singapore | 41 (PS) | 6 |
| Jordan | 32 (PD) | 3 |
| Qatar | 26 (PQ) | 3 |
| Brunei | 23 (PB) | 5 |
| Kyrgyzstan | 19 (PY) | 0 |
| Maldives | 10 (PM) | 3 |
| Malaysia | 8 (MP0772 on) | 1 |
| Cambodia | 7 (PC) | 1 |
| United States (new) | 221 (XU) | 17 |
| Canada (new) | 167 (XC) | 20 |
| United Kingdom (new) | 163 (XK) | 26 |
| India (new) | 141 (XI) | 32 |
| Lebanon (new) | 89 (XL) | 28 |
| Greece (new) | 88 (XG) | 16 |

About 1,960 facts in all, every one with an exact Bangla quote checked by `facts.py` against the saved article in the doc's `sources/` (`pa-<date>-<slug>.md`).

## How

The simplified process (METHOD.md, section 12):
1. **One agent per country chunk** (`briefs/COUNTRY-WRITE-SPEC.md`; new countries `briefs/NEW-COUNTRY-SPEC.md`) read every article in full, saved it as a source (`scripts/save_pa.py`), logged each fact, wrote it into the doc, built it, and accounted for every article in a ledger (`ledgers/`): used, or unused with a reason. Facts about another doc were held, not written.
2. **Held facts** were placed by a later agent for the doc they belong to (`briefs/HELD-SPEC.md`), after re-reading the article.
3. **Articles the keyword filter had missed:** 472 rejected stories carrying migration words were triaged (117 useful) and read in full into the docs (`ledgers/lledger-*.json`).
4. **Independent final check** of every doc (`briefs/FINAL-CHECK-SPEC.md`): a checker that had not seen the writing read every new or changed sentence against its facts and the article, and proposed fixes (`checks/fix-*.json`), applied with `scripts/apply_fixes.py`. 245 fixes across 21 docs; the commonest kinds were claims wider than the source, dropped attributions and unexplained terms.
5. **Conflicts settled by the agents, not left open:** a primary document beats a secondhand summary, a specific dated figure beats a vague one, and misprints are not conflicts. Each is recorded under "Resolved conflicts" in the doc's `notes.md`; only conflicts no source can settle became a "Need to know".
6. **Open questions:** `questions.md` updated with `scripts/sync_questions.py` (new bullets added, answered ones removed); each new doc got its own.

## Limits

- The six new docs are built from news only (0 official sources). Their "Need to know" bullets list what an official research pass must find first (visa rules, fees, embassy details).
- Inputs too large for this folder (the article dumps) are in `datasets/prothom-alo-migration/`; the article-by-article coverage ledger will be added there.
