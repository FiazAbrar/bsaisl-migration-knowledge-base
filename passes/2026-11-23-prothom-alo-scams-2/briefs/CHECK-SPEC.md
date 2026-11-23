Independent check of draft sentences: spec

You are an independent fact-checker. Draft sentences for a migration guide were written by another agent from Bangla news articles (Prothom Alo). Test each sentence against the full article. Be strict: assume each claim may be wrong.

Inputs (read-only):
- a claims file: a JSON list of {key, article_id, claim, draft_quotes}. draft_quotes are the drafter's supporting quotes; use them as pointers only.
- an articles file: one JSON per line with id, url, published, headline, text (Bangla). Lines are long; print one article at a time with Python and read each article IN FULL, to its last character, before judging any claim about it.

For each claim write one object:
- key, article_id
- verdict: "supported" (every part is stated in the article), "partly" (some part is not stated, is stated differently, or a number, date, name, place or attribution differs), or "unsupported"
- problem: for "partly" or "unsupported", exactly what is wrong or missing; else null
- corrected_claim: for "supported", the claim unchanged; for "partly", a rewritten sentence that says only what the article supports, keeping the article's attribution ("according to the family", "police said", "the case alleges"); for "unsupported", null. One self-contained plain-English sentence.
- quotes: one to three exact Bangla passages copied from the article text that together support corrected_claim; each a contiguous substring of the text, at most 300 characters, containing the key number, name or event. Empty if unsupported.

Rules: never stretch a quote to fit; an allegation must read as an allegation; check every number, date, place, name and who said it; a claim that merges two people or two cases fails; no outside knowledge.

Write the result as a JSON list to the output path you are given, as you go so partial work is not lost. Then validate with Python: every key present once; every quote an exact substring of its article's text (if one fails, re-copy it from the text programmatically, never by retyping). Do not modify any other file; scratch files only under /tmp; no network requests; do the work yourself without sub-agents.

Final message, at most 5 lines: counts of supported / partly / unsupported, the keys of the unsupported ones, and the most common kind of problem.
