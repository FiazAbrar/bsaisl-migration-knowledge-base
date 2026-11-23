Placing held items into a doc: spec

Earlier agents, reading Prothom Alo articles for other docs, found facts that belong in your doc and held them for you, each with an English claim and an exact Bangla quote from the article. Your job: put every held item that adds something into your doc, cited, so nothing from the archive is lost.

Repository: the worktree containing your doc folder (given in your instructions). Edit only your doc folder. Run no git commands.

Read first: the repository's CLAUDE.md ("Format" and "Quality rules" are binding), then your doc.md in full.

Input: a JSON list of held items: held_id, article_id, from (the ledger it came from), claim, quote.

For each item:
1. Check it against the doc. If the doc already says it (same fact, same or better source), mark it "duplicate" with the fact id that covers it.
2. Otherwise read the article itself, not only the held claim (the claim may be wrong or lack context): get the text with Python from /Users/rarba/Programming/brac/bits-migration/prothom-alo-archive/migration-stories.jsonl by id (or stories.jsonl, if not there), and read at least the paragraphs around the quote.
3. Save the source and log the fact from inside your doc folder:
   python3 /Users/rarba/Programming/brac/bits-migration/prothom-alo-archive/extract/kb4/save_pa.py . <article id>
   python3 ../../tools/facts.py add --prefix <your prefix> --name <source name> --claim "<self-contained English sentence, with the article's attribution>" --quote "<exact Bangla passage, contiguous, at most 300 characters>" --page-date <published date> --status unofficial
   Re-copy the quote programmatically from the text if the held one fails. Correct the claim if the article says something different.
4. Write it into the right section of doc.md, following the Format rules (shape that fits, dated statements, attribution kept, acronyms explained, no advice of our own). Where it answers a "Need to know", answer it and remove the bullet. Where it conflicts with the doc, resolve it yourself (primary document beats secondhand summary; specific dated figure beats vague restatement; misprints aren't conflicts) and record the reasoning in notes.md under "Resolved conflicts"; only a truly unsettleable conflict becomes a "Need to know".
5. Items that turn out not to belong in your doc: mark "wrong doc" with the doc they belong in.

Then build (python3 ../../tools/build.py from your folder), fix every error, delete any .pdf, and do a line-by-line pass over what you added.

Output: a JSON list at the path given, one entry per held_id: {"held_id": "...", "outcome": "added|duplicate|wrong doc|no usable fact", "fact_ids": [...], "note": "..."}.

Scratch files only under /tmp/<your prefix>/; no network requests; no sub-agents.

Final message, at most 5 lines: items added, duplicates, wrong doc (and where), sections changed, anything truly unsettled.
