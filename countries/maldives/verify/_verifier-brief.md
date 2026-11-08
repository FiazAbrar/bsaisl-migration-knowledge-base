# Verifier brief, Maldives doc, round 1 (8-9 November 2026)

You are an independent fact-checker. You have not seen the research. Your job is to check one stretch of `countries/maldives/doc.md` against its evidence and report problems. Do NOT edit doc.md, facts.csv or any other file except your own report.

Repo root: `C:\Users\User\Desktop\Github\bsaisl-migration-knowledge-base` (ROOT). Country folder: `ROOT\countries\maldives` (C).

## How the evidence works

- Every sentence in doc.md ends with fact ids like `[W0012, N0003]`.
- Each id is a row in `C\facts.csv` (columns: id, claim, quote, saved_file, url, page_date, status, note). The `quote` is copied from the saved source; `saved_file` names the text copy in `C\sources\` (.md or .txt).
- Quick lookup: `cd` to C and run `python ../../tools/facts.py cited doc.md <start_line> <end_line>` (use `python`, not python3) to list the facts a stretch cites. To read a fact's quote: `python -c "import csv;F={r['id']:r for r in csv.DictReader(open('facts.csv',encoding='utf-8'))};r=F['W0012'];print(r['claim'],'||',r['quote'],'||',r['saved_file'],r['note'])"` (set `PYTHONIOENCODING=utf-8`).
- When a quote is short, ambiguous or empty (some Bangla PDFs have no quote and a note saying it was read from the page image), open the saved file in `C\sources\` and read the surrounding text, or the PDF itself, to judge.

## What to check, sentence by sentence

1. **Support:** does the cited evidence (quote, read in context of the saved file) say what the sentence says? Every part of the sentence: each number, date, name, condition, "only", "must", "since". A sentence that adds a detail none of its cited facts support is UNSUPPORTED.
2. **Numbers:** every fee, amount, duration, validity, date, count, phone number and percentage matches the source exactly. Taka conversions use MVR1 = Tk 8.06 (G0015, G0014: 124.35 / 15.42); check the arithmetic, rounding to a sensible figure is fine.
3. **Wrong id:** a sentence citing a fact that is about something else (ids are sometimes shifted by one or two). If you can find the right id in facts.csv (search the claims), give it.
4. **Status vs wording:** a fact with status `unofficial`/`lead` (news) stated as official rule is fine as long as the sentence doesn't misattribute it; flag only if the doc presents a news claim as a law or official figure in a misleading way.
5. **Currency:** a sentence that states as current a rule the evidence shows is old or superseded (e.g. a 2021 rule, when a newer source in facts.csv says otherwise). Flag as OUTDATED.
6. **Uncited sentences** (no [id] at the end): flag as UNCITED. List items covered by a lead-in citation ("You'll need [B0013]:") are fine. Headings and Need to know questions don't need citations.
7. **Clarity errors:** a cross-reference that points to the wrong place, an acronym used before it is explained in your stretch's first use (only if it isn't explained earlier in the doc; check with grep), or a sentence that is self-contradictory.

Do not report style preferences. Do not report things that are correct. Be strict on facts.

## Report

Write `C\verify\r1-<your id>.md`. For each problem, one block:

```
### L<line number> FAIL|UNSUPPORTED|OUTDATED|WRONG-ID|UNCITED|NUMBER
- sentence: "<the exact sentence or the part at issue, copied from doc.md>"
- cited: <ids>
- evidence says: "<the relevant words of the quote or source>"
- fix: <what the sentence should say, as doc text with ids, e.g.: Probation is at most 3 months [L0004].> OR <drop the sentence> OR <replace W0012 with W0013>
```

The `fix:` line must contain only replacement doc text or a short instruction like "drop", "replace X with Y", never commentary inside the replacement text.

End the report with a line `TOTAL: <n> problems in lines <a>-<b>` and, if zero, write `TOTAL: 0`.

Final message back to the lead: the total and the 3-5 most serious problems in one line each. Time limit: about 30 minutes; check every cited sentence in your stretch.
