# Italy doc: new manual files (10 November 2026, about 30 minutes)

The team saved more blocked official pages by hand. Your job: read your files in full, log every useful fact, and propose exact edits to `doc.md` so the doc uses them. Root: `C:\Users\User\Desktop\Github\bsaisl-migration-knowledge-base` (ROOT). Italy folder: `ROOT\countries\italy` (IT).

## Read first
- `ROOT\CLAUDE.md` (Format and Quality rules: binding).
- `IT\doc.md`: the finished doc. Read the sections your files touch (grep for keywords; check the "Need to know" blocks there).
- `IT\facts.csv`: the existing facts (columns id, claim, quote, saved_file, url, page_date, access_date, source_type, status, ...).

## Your files
They are already saved in `IT\work\<X>\sources\` (X = your prefix) with `_fetchlog.csv` rows and text copies (`.txt`). Where a text copy is missing or empty (image-only PDF), read the PDF page by page with the Read tool (`pages` parameter, max 20 pages a call), write a faithful transcription to `sources\<name>.md` (first line: "Transcription of <file>, saved by a team member on 10 November 2026 from <url>"; then the text as printed, Bangla translated into English line by line with the Bangla kept where short), delete the useless `.txt`, and add the `.md` to that row's `files` column in `_fetchlog.csv`.

## Log facts
1. Write `IT\work\<X>\x.json` in this shape and run `python ../addm.py x.json` **from inside `IT\work\<X>`** (it registers sources, then adds facts and checks each quote against the saved text):
   ```
   {"prefix": "<X>",
    "sources": [["<name>", "<publisher>", "<title in English>", "yes|no", "<page date YYYY-MM-DD or undated>"]],
    "facts": [{"n": "<name>", "c": "<claim in plain English>", "q": "<exact words copied from the text copy, 6-30 words, one line>", "d": "<page date>", "s": "<status>", "v": ["<visa>", "<field>", "<value>"], "note": "..."}]}
   ```
   `v` and `note` are optional. `official` = yes only for a government, EU or embassy publisher. Status: official and dated within 12 months of 10 Nov 2026 → `verified`; official but older or undated → `possibly-outdated`; anything else → `unofficial`. If a quote is refused, copy it again exactly from the `.txt`/`.md` (watch line breaks, hyphenation, curly quotes) and rerun only the failed facts.
2. Log what changes what a migrant does or understands: fees, deadlines, documents, rights, numbers for Bangladeshis, procedures, who to contact. Skip trivia.

## Propose doc edits
Write `IT\verify\q-<X>.md` with one block per edit, in this exact format (it is applied by a script):
```
### FAIL <short reason>
old: <exact text copied from doc.md, unique in the doc, on one line>
new: <replacement text, with fact ids in square brackets>
```
- `new: (delete)` removes the old text (use it for a Need to know bullet your facts now answer: old = the whole bullet line).
- Prefer official over news: where your new official fact supports a sentence now cited only to news (`N....` ids, or other unofficial facts), add your id and drop the news id only if the official fact covers everything the sentence says.
- Add new sentences or list items where they belong (put them in `new` together with the old text they follow). Keep the doc's style: every sentence or list item ends with fact ids; EUR with Taka at EUR 1 = about Tk 139.6 cited to G0001; no "source X says"; explain Italian terms on first use in that section; no tables; no dates in headings; cross-references use exact heading text.
- Narrow or remove Need to know bullets your facts answer; if a fact only partly answers one, rewrite the question to what is still open.
- Do not edit `doc.md` yourself. Do not touch other folders. No web research, no commits.

## Final reply (3 lines)
Facts logged (ids), edits proposed, Need to know bullets removed or narrowed, anything you couldn't read.
