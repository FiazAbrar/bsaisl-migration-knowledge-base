Writing checked facts into the guide: spec

You are writing new material into a guide for Bangladeshis who want to work abroad. Every fact you will use has already been checked against its full source article and logged with an id. Your job is to place ALL of them into the guide, well written, in the sections you own, and nowhere else.

Read first, in full:
1. /Users/rarba/Programming/brac/bits-migration/kb-scam-cases/CLAUDE.md, sections "Format" and "Quality rules". They are binding. In short: sharp writing, form follows function, every sentence cited, no conclusions or advice of your own, explain every acronym and organisation at first use, a guide not a research log, cross-references use exact heading text, no tables, at most four heading levels.
2. The guide file you are given, and in particular every section you own, read in full.

Your claims file is a JSON list of {key, fact_ids, claim, target_section, placement, why_new, published}. Each claim is a checked sentence; fact_ids are the ids to cite for it, like [LB0012, LB0013].

Rules for using the claims
- Use every claim, or list it as unused with a reason that is one of: "duplicates existing text at <heading>" (the guide already says the same thing with the same or better source), "merged into <key>" (said once, citing both), or "no bearing on what a migrant does or understands" (pure trivia). Full coverage is the goal: do not drop material for length or because it is "only another case". Repeated cases are exactly what show a pattern.
- Say only what the claim says. Keep every attribution in it ("according to the family", "police said", "the case alleges"). Never strengthen, merge two people into one, or generalise beyond the claims. You may combine several claims into one sentence or one list item only when every part stays true and every fact id is cited.
- Cite with the fact ids given, in square brackets at the end of the sentence or list item, exactly as the existing text does ([PA0012, S0159]). Every sentence you write carries at least one citation. Never cite an id for something it does not say.
- Do not change the existing text's meaning or remove its citations. You may reorganise a section you own (re-order items, add sub-headings, split a long list, move a case to where it fits), fix a cross-reference, and tighten existing wording, as long as every existing claim and citation survives.
- Where a claim conflicts with the existing text (a different figure, date or rule), do not pick one: keep both with their citations, and add one bullet to a "Need to know" block right after that paragraph asking the precise question an insider could answer.
- Where you write a lead sentence that summarises the cases under a heading, it must be true of every case you list there and must itself be cited with the ids of those cases; if it would not be, don't write one.
- Structure inside each section follows the existing pattern where there is one (How it works / Red flags / Check before paying / Cases / What to do; or How it is sold / The path / What happens / The numbers / The law / Where to get help). Cases are listed oldest first, each opening with its date. Use H4 sub-headings or bold lead-in labels to keep long sections navigable.
- New sections (target_section "NEW: ..."): write them in the same pattern as their neighbours, with a heading level matching their siblings. Put each where its target or the drafter suggested (the claim's why_new may say), or where it fits best among the sections you own. If a proposed new section has fewer than about five claims or overlaps an existing section heavily, fold it into the existing section instead.

Output: do NOT edit the guide file. Write two files:
1. <out>.md: one block per section you changed or created, in this exact form:

<<<REPLACE doc="<doc path>" heading="<the exact existing heading line, e.g. ### Libya to Italy by boat>">>>
<the full new text of that section, starting with that same heading line and running to just before the next heading of the same or higher level>
<<<END>>>

<<<NEW doc="<doc path>" after="<exact existing heading line of the section it should follow>">>>
<the full text of the new section, starting with its heading line>
<<<END>>>

   A REPLACE block must contain the whole section including all its sub-sections, since it replaces everything from that heading to the next heading of the same or higher level. Only use headings you own.
2. <out>-unused.json: a JSON list of {key, reason} for every claim not used.

Before finishing, validate with Python:
- every key in your claims file has its fact_ids cited somewhere in your .md output, or appears in the unused file;
- every fact id cited in a block you replaced that was in the original section is still cited in your new version (nothing lost);
- every "(see X)" cross-reference names an exact heading that exists in the guide or in your new blocks;
- every heading line in a REPLACE block's first line exists exactly once in the guide (if a heading text occurs more than once, say so in your final message and include the line number).
Fix problems before finishing. Write nothing else in the project; scratch files only under /tmp; no network requests; do the work yourself without sub-agents.

Final message, at most 6 lines: claims used, claims unused (by reason), sections replaced, sections created, and anything a reviewer should look at.
