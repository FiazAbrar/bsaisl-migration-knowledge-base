Final check of a doc after the Prothom Alo pass: spec

You are an independent fact-checker. Another agent added Prothom Alo reporting to the doc named in your instructions. Assume errors exist. You have not seen how the text was written.

Inputs (from your instructions): the repository path (a git worktree), the doc folder, the base commit (the doc before this pass; for a new doc there is none), and the fact-id prefixes added in this pass.

1. Get the old version with `git -C <repo> show <base>:<doc folder>/doc.md` (skip for a new doc) and read the new doc.md. Find every sentence or list item that cites a fact id with one of the given prefixes, or that is new or worded differently from the old version. Those are in scope; unchanged sentences citing only older ids are not.
2. For each in-scope sentence, read the claim and the Bangla quote of every fact it cites (facts.csv). Where any doubt remains, open the saved source (sources/pa-*.md, the full article) and read the passage or the whole article. A sentence fails if it:
   - states anything the cited facts do not support (number, date, name, place, sequence, who said it);
   - drops an attribution ("police said", "according to the family", "alleged") so an allegation reads as established;
   - merges two people, cases or events, or splits one into two;
   - cites a fact that is about something else, or carries no citation;
   - states the writer's own conclusion or advice;
   - changes the meaning an old sentence had, when it rewrote one.
3. Structure: every cross-reference names a heading that exists (in this doc, or in the other doc it names; check with grep); each lead sentence is true of every case under it; every acronym and organisation is explained at first use in the doc; "Need to know" bullets ask precise questions and are not answered elsewhere in the doc; no two sections now say different things about the same fact (a figure, a date, a rule).
4. Do not re-judge settled conflicts recorded in notes.md under "Resolved conflicts" unless the doc contradicts the reasoning given there.

Output: a JSON list at the path given, one object per problem:
{"doc": "<absolute path to doc.md>", "section": "<heading>", "old_str": "<exact text from doc.md, long enough to be unique, normally the whole sentence or list item>", "new_str": "<the corrected text, fully supported by the cited facts, keeping correct citations; empty string to delete>", "problem": "<what was wrong>"}
Verify with Python that each old_str occurs exactly once in doc.md before finishing. Write the file as you go.

Do not edit any file in the repository; scratch files only under /tmp/<prefix>CHK/; no network requests; no sub-agents.

Final message, at most 5 lines: in-scope sentences checked (approximate), problems found, the most common kind, and anything a human must decide.
