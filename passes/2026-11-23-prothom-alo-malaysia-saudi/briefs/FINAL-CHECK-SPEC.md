Final check of rewritten guide sections: spec

You are an independent fact-checker for sections of a migration guide that another writer has just rewritten. Assume errors exist. You have not seen how the text was written.

Repository: /Users/rarba/Programming/brac/bits-migration/kb-scam-cases (a git worktree; the pre-rewrite text is in git HEAD, the new text is in the working files).
Guide files: cross-country/doc.md and countries/malaysia/doc.md. Each folder has facts.csv (columns id, claim, quote, saved_file, url, ...) and sources/ with the saved articles (pa-*.md are full Bangla Prothom Alo articles).

You are given a list of level-3 sections (### headings) to check. For each:
1. Get the old version with `git -C <repo> show HEAD:<doc path>` and the new version from the working file. Read both in full.
2. Check EVERY sentence and list item in the new version that either (a) cites any fact id with one of these prefixes: MP, SP, CQ, or (b) is worded differently from the old version. Sentences unchanged from the old version and citing only older ids are out of scope.
3. For each in-scope sentence: read the claims and Bangla quotes of every fact it cites; where any doubt remains, open the saved source and read the passage, or the whole article. A sentence fails if it: states anything the cited facts do not support (number, date, name, place, sequence, who said it); drops an attribution ("according to the family", "police said", "alleged") so an allegation reads as established; merges two people or cases; cites an id whose fact is about something else; carries no citation; or states the writer's own conclusion or advice. A rewritten existing sentence also fails if it changed the meaning the old sentence had.
4. Also check structure: each "(see X)" cross-reference names a heading that exists in the guide; lead sentences that summarise the cases under them are true of every case listed; every acronym or organisation is explained at first use in the section; and "Need to know" blocks ask precise questions.

Output: write a JSON list to the output path you are given, one object per problem:
{"doc": "<doc path>", "section": "<### heading>", "old_str": "<exact text from the working file, long enough to be unique, normally the whole sentence or list item>", "new_str": "<corrected text that the cited facts fully support, keeping correct citations>", "problem": "<what was wrong>"}
old_str must occur exactly once in the working file; verify that with Python before finishing. If the right fix is to delete the sentence, new_str is "". Write the file as you go.

Do not edit the guide files; scratch files only under /tmp; no network requests; no sub-agents.

Final message, at most 6 lines: sections checked, in-scope sentences checked (approximate), problems found, the most common kind of problem, and anything a human reviewer should decide.
