# Kyrgyzstan doc: independent check, round 1 (time limit about 15 minutes)

You are an independent fact-checker. You have not seen the research. Root: `C:\Users\User\Desktop\Github\bsaisl-migration-knowledge-base\countries\kyrgyzstan` (KW).

Check your assigned line range of `KW\doc.md`. For each sentence with citations `[X0000, ...]`:
1. Look up each id: `grep "^W0030," KW/facts.csv` (columns: id, claim, quote, saved_file, url, page_date, access_date, source_type, status, ...). The quote is the evidence.
2. FAIL if: an id does not exist; the cited quotes don't support the sentence; any number, fee, date, duration, percentage or name in the sentence is not in the cited facts (claim AND quote); the sentence says more than the facts (e.g. "always", a wrong year, a different job); a sentence has no citation. When in doubt about a quote, open the saved file in `KW/sources/`.
3. Also FAIL: research narration in the text ("source X says", "reports conflict", "we could not find"), an instruction to the editor, or a cross-reference like "see above".
Skip headings, ready-to-use sample wording in quotes (a template for the worker to fill in, marked "Sample wording"), the "Need to know" bullets (they need no citation) and blank lines.

Uncited list items (lines starting "- " that state facts) are FAILs too: give the new text with the correct existing ids (find them with `grep -i` on facts.csv claims). Do NOT edit doc.md. Write `KW\verify\r1-<N>.md` containing ONLY failures, each as:

```
### FAIL <line number>
reason: <one line>
old: <exact text copied from doc.md, a unique fragment of that line, at least 30 characters>
new: <replacement text, written as final doc text with its citations; to delete the sentence, write new: (delete)>
```

The `new:` text must be final doc wording, never an instruction or a note. Prefer narrowing the sentence to what the facts support, or re-citing to the right existing id, over deleting. If nothing fails, write `No failures.`

Final reply: one line: lines checked, failures found.

Kyrgyzstan specifics:
- Many quotes are in Russian; read them carefully. Taka conversions use KGS 1 = about Tk 1.42 (G0003) and USD 1 = about Tk 124.42 (G0002); FAIL a conversion more than 3% off.
- Your line range is in `KW\verify\r1-lines-<N>.txt` as "start-end". Ready-to-use "Sample wording" templates in quotes are allowed without citation.
