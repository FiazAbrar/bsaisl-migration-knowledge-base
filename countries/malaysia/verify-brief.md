# Verifier brief (Malaysia doc)

You are an independent verifier. You have not seen the research; check the doc against the saved sources, not against the researchers' summaries and not against your own memory. Today is 6 November 2026.

## Files (all under C:\Users\User\Desktop\Malaysia\countries\malaysia\)
- `malaysia.src.md`: the doc source. Citations are ledger ids like `[W0012, L0003]`.
- `ledger.csv`: one row per id: claim, quote, url, raw_file (saved copy in `raw/`), page_date, source_type (official/news), status (verified / possibly-outdated / conflict / lead / unofficial), note.
- `raw/`: the saved pages. `.md` / `.txt` are text copies of `.html` / `.pdf`. Some Bangla PDFs are image-only: their ledger rows say "--no-quote-check" in the note; read the PDF itself with the Read tool (it renders pages) to check those.
- Rules: `C:\Users\User\Desktop\Malaysia\CLAUDE.md` (the "Malaysia addendum" at the end wins over the rest).

## What to check, sentence by sentence in your line range
1. **Support:** open every cited ledger row, then open its raw file and find the passage. Does the source itself (not only the ledger claim) say what the sentence says? Watch for: numbers, dates, fees, durations, ages, counts, names, phone numbers, URLs; words like "only", "must", "free", "all"; a sentence that combines several facts where one cited source covers only part; and anything added that no source says.
2. **Uncited claims:** any factual statement with no citation.
3. **Status rules:** a row with status `lead` or `unofficial` (source_type news) must not be the basis of an exact fact (fee, eligibility, documents, processing time, legal rule); those must be written as "Need to know" with "unofficial, not verified" in the paragraph. Official and news sources in conflict: both shown, official marked as the rule.
4. **Conflicts:** where two official sources disagree, the doc must show both, not pick one silently.
5. **Opinion or advice of our own** (not from a source): flag it.
6. **Terms:** every acronym, organisation or platform explained the first time it appears in the doc (check earlier lines with grep if needed).

## Output
Mark every sentence you check PASS, FAIL (the source says something different) or UNSUPPORTED (the source doesn't say it, or there is no citation). Report ONLY the FAIL and UNSUPPORTED ones. Write them to `verify/<your-label>.md` (create the folder if missing; touch no other file), one entry per problem:

```
- L<line> | FAIL or UNSUPPORTED | <kind: wrong / partly-supported / uncited / status-rule / conflict-hidden / advice / term> | "<the exact words in the doc>" | cited: <ids> | source says: "<short exact quote from the raw file, or 'nothing found'>" (<raw file>) | fix: <corrected wording, with the ledger ids that support it, or "make it Need to know">
```

End with: `Checked N sentences: P PASS, F FAIL, U UNSUPPORTED.` Do not edit `malaysia.src.md`, the ledger or anything else. Do not fetch new pages unless your task says so. Your final message: the counts and the most serious failures.
