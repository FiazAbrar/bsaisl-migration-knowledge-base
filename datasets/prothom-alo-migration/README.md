# Prothom Alo migration archive, 2024 to November 2026

Every Prothom Alo story published from 1 January 2024 to 22 November 2026 that a migration keyword search returned, with full Bangla text, plus the structured data extracted from the migration-relevant ones. Built 22 to 23 Nov 2026 for the BSAISL Migration Pathway Navigator knowledge base.

The article texts are Prothom Alo's and remain its copyright; they are shared here for research on labour migration, with attribution and a link to each original. The extracted files are this project's own work.

## Files

| Path | Records | What it is |
|---|---|---|
| `raw/stories.jsonl.xz` | 27,907 | Every story the searches returned, one JSON per line (unpack with `xz -dk`). Fields: id, url, headline, subheadline, summary, published, updated, author, template, sections, tags, text (full Bangla body, no page furniture). |
| `filtered/migration-stories.jsonl.gz` | 1,787 | The stories `scripts/classify.py` flagged as migration-related, same fields. |
| `filtered/index.csv` | 1,787 | One row per flagged story: published, level (core/related), score, headline, url, section, countries, topics, signals, tags, words, author. |
| `extraction/per-article/articles-extracted.jsonl` | 1,597 | One record per flagged story read in full by an AI reader (1,394 judged relevant): relevant, not_relevant_reason, kinds, countries, summary_en, facts (8,542: type, country, date, statement), named_actors, people_cases, key_quote_bn. Brief: `SPEC.md`. |
| `extraction/scam-cases/scam-cases.jsonl` and `.csv` | 184 | One record per fraud or trafficking case: destination promised, route, job and wage promised, visa claimed, amounts, payment method, how the money was raised, perpetrator type and names, how they met, trust devices, timeline, harm, ransom, official response, money recovered, key quote. Brief: `SPEC.md`. |
| `extraction/agency-flags/agency-flags.json` | 262 | One row per agency, travel firm or consultancy linked to cheating or trafficking: name as printed, RL number if printed, match to BMET's licence list, flag type, date, summary, exact Bangla quote, people named. Brief: `SPEC.md`. |
| `scripts/` | | `harvest.py` (the harvester), `classify.py` (the relevance filter), and the keyword lists for the second and third search passes. |

Ids: every record carries Prothom Alo's story id (`id` or `article_id`), so the files join on it.

## How it was collected

- Source: Prothom Alo's public search API, `https://www.prothomalo.com/api/v1/advanced-search`, with `q`, `published-after`/`published-before` (milliseconds) and paging; the response includes the story cards, so the full text comes with each hit.
- Three keyword passes: base migration terms; 245 inflected Bangla forms (the search matches whole words only, so বিদেশে and বিদেশগামী need separate queries); words for Bangladeshis abroad and the embassies.
- Search windows were split by date to stay under the API's 10,000-result paging limit.
- `classify.py` scores each story on strong signals (fraud abroad, visa fraud, Bangladeshis abroad and so on), after NFC normalisation of the Bangla text.

## How it was used

This repo records each use in `passes/`: one folder per pass with its briefs, drafts, checks and scripts. Every fact taken into a doc is logged in that doc's `facts.csv` with an exact Bangla quote, and the article is saved under the doc's `sources/` as `pa-<date>-<slug>.md`. A coverage ledger (which pass used each relevant article, or why not) will be added here as `coverage/ledger.csv` when the current passes finish.

## Known limits

- Keyword search: a migration story using none of the search words is missing. The third pass was added after a sample story was found to be missed.
- The AI extraction has errors and gaps; treat it as a pointer and check the article text before relying on a fact.
- Up to 22 Nov 2026 only.
