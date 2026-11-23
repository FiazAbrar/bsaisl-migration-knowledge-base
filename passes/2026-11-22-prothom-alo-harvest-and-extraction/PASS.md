# Prothom Alo harvest and full-read extraction

Goal: collect Prothom Alo's migration reporting from 1 Jan 2024 to 22 Nov 2026 and record every usable fact.

- Harvest (`scripts/harvest.py`): Prothom Alo's public search API, 14 tags and 22 keywords, then a second pass over 245 inflected word forms (`keywords-pass2.txt`, because the search matches whole words only) and a third over words for Bangladeshis abroad and embassies (`keywords-pass3.txt`). 27,907 unique stories.
- Filter (`scripts/classify.py`): rule-based relevance; 1,787 stories flagged (`output/index.csv`). Sample checks showed a few hundred relevant stories remain in the rejected pile.
- Scam case table (`briefs/SPEC.md`): 270 fraud stories read in full; `output/scam-cases.csv` (184 relevant rows).
- Full-read extraction (`briefs/GENERAL-SPEC.md`): the other 1,597 flagged stories in 62 batches, each read in full by an agent; `output/g-*.jsonl`, 1,394 relevant, 8,542 facts. These records carry one key quote per article, not per fact, so later passes re-read the articles to log facts.

Lesson: extraction should store a quote with every fact, so later passes need not re-read articles.

Inputs outside the repo: stories.jsonl (319 MB) and migration-stories.jsonl (23 MB).
