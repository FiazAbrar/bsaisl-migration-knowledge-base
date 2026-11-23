Drafting additions to the cross-country guide from Prothom Alo case reports: spec

You are helping improve a guide for Bangladeshis who want to work abroad. The guide is
/Users/rarba/Programming/brac/bits-migration/kb-scam-cases/cross-country/doc.md
Its readers include recruiting-agency staff, returnee workers and caseworkers, who can tell real ground-level knowledge from generic advice. Read the repo's rules first: /Users/rarba/Programming/brac/bits-migration/kb-scam-cases/CLAUDE.md (sections "Format" and "Quality rules").

Your input file holds Bangla news articles (Prothom Alo, 2024 to Nov 2026), one JSON object per line: id, url, published, headline, already_used_in_doc, earlier_summary (an English summary record made by an earlier pass; treat it only as a pointer, it has errors), text (the full Bangla article).

Your job: place everything usable from EVERY article into the guide, as draft sentences with evidence. Nothing usable should be left out. The target is full coverage, not a selection.

Steps
1. Read doc.md's structure (grep the lines starting with "## " and "### ") and read IN FULL every section you might add to. The relevant chapters are "Dalal scams: the usual tricks and how to spot them", "Departure bottlenecks: offloading, airport checks, bribes and deportation" and "Illegal routes". Know what each section already says so you add only what is new.
2. Read every article in your input IN FULL, to its last character (lines are long: print one article at a time with Python, in slices if needed). Never work from the headline or the earlier_summary alone.
3. For each article, draft every sentence that would add something the guide does not already say. Typical additions:
   - a dated case for a section's "Cases" list (who, where from, destination, what was paid and to whom, what convinced them, how it came apart, what happened, what the authorities did);
   - a mechanism for "How it works" (a step in how the trick is run that the section lacks);
   - a "Red flags" item (only when the article itself shows it happening);
   - a number for "The numbers" (with its period and source);
   - what the law or the authorities did ("The law", "What to do", "Where to complain and get help"): cases filed, under which Act, arrests, verdicts, licence actions, refunds, and equally what did NOT happen (no case, acquittal, no refund);
   - advice or a warning quoted from a named official, embassy, NGO or expert;
   - a check that exists (who says so, where, how);
   - for articles marked already_used_in_doc: only what the guide has not yet taken from them, especially the additional survivor accounts.
   If an article supports a whole pattern the guide has no section for, propose a new section: give it a short plain heading and say where it should sit.
4. Each draft sentence must:
   - be one self-contained English sentence (country, date or period, who) that a reader with no context understands;
   - say only what the article states, with the article's own attribution kept ("according to the family", "police said", "the case alleges", "X told Prothom Alo"). An allegation must read as an allegation;
   - give numbers, dates, names and places exactly as printed (BDT amounts in lakh/crore as the article gives them);
   - carry one to three exact Bangla quotes copied from the article text that together support it. Each quote must be a contiguous substring of the article's text, at most 300 characters, and contain the key number, name or event.
   Never infer, never generalise beyond the article, never add your own advice.
5. Also list every named agency, company or accused person: name as printed (Bangla in brackets if the spelling is uncertain), licence number only if printed, kind, location, what the article says about them with attribution, the date, and one supporting quote.
6. For every article, account for it: either it yields at least one draft, or you list it under "nothing_to_add" with the reason (for example: everything in it is already in the guide at section X; or it has no concrete fact).

Output: one JSON object written to the output path given in your instructions:
{
 "drafts": [ {"key": "<set>-<n>", "article_id": "...", "target_section": "<exact existing heading text, or NEW: <proposed heading>>", "placement": "Cases | How it works | Red flags | The numbers | The law | What to do | Where to get help | other: <say>", "claim": "...", "quotes": ["..."], "why_new": "what this adds that the section lacks"} ],
 "new_sections": [ {"heading": "...", "after_section": "<existing heading it should follow>", "why": "..."} ],
 "named_actors": [ {"article_id": "...", "name": "...", "licence_no": null, "kind": "recruiting agency | travel agency | consultancy | employer | broker | official | other", "location": "...", "date": "...", "what_the_article_says": "...", "quote": "..."} ],
 "nothing_to_add": [ {"article_id": "...", "reason": "..."} ]
}

Validate with Python before finishing: every article id in the input appears in drafts or nothing_to_add; every quote is an exact substring of its article's text (compare raw strings; if a quote fails, re-copy it from the article text programmatically, never by retyping). Write the output file as you go so partial work is not lost.

Do not modify any file in either project folder except your output file; scratch files only under /tmp; no network requests; do the work yourself without spawning sub-agents.

Final message, at most 6 lines: articles read, drafts written, new sections proposed, named actors listed, articles with nothing to add, and anything that went wrong.
