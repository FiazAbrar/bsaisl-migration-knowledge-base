# Italy doc: independent check of new edits (time limit about 15 minutes)

Same rules as `_verifier-brief.md` in this folder (read it first), with these changes:
- Check ONLY the doc.md line numbers listed in your file `KW\verify\q4-lines-<N>.txt` (comma-separated). These lines were rewritten after two checks. A cross-reference written as "Work visa: Decreto Flussi worker (non-seasonal)", Step N (with quotes) is deliberate: the build needs the quotes to link it.
- Also FAIL a line if a list item or sentence repeats a fact already given in the same paragraph, or if Italian or Bangla terms are left unexplained on first use in that section.
- Write `KW\verify\q-r4-<N>.md` in the same FAIL/old/new format (only failures; `No failures.` if none).
- Ready-to-use "Sample wording" templates in quotes are allowed without citation.
- Final reply: one line: lines checked, failures found.
