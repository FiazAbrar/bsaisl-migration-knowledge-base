Drafting additions to a country guide from Prothom Alo reporting: spec

You are helping improve a country guide for Bangladeshis who want to work in that country. Its readers include recruiting-agency staff, returnee workers and caseworkers, who can tell real ground-level knowledge from generic advice. The chatbot that advises migrants answers from this guide.

Read first:
- /Users/rarba/Programming/brac/bits-migration/kb-scam-cases/CLAUDE.md, sections "Format" and "Quality rules" (binding).
- The country guide named in your instructions: first its heading list (lines starting "## ", "### ", "#### "), then IN FULL every section you might add to. Know what each section already says, so you add only what is new. The guide already contains some Prothom Alo material from earlier passes (facts with prefixes such as MA, MB, PA); do not duplicate it.
- For Bangladesh-side facts (BMET, PKB, the Welfare Board, airports, passports, remittance), check whether they belong in this country guide (where they happen in the worker's journey for this country) or in the cross-country guide (/Users/rarba/Programming/brac/bits-migration/kb-scam-cases/cross-country/doc.md, which covers what is common to all countries). Target "CROSS-COUNTRY: <exact heading>" when a fact is not specific to this country.

Input: a .jsonl file of Bangla Prothom Alo articles (2024 to Nov 2026), one per line: id, url, published, headline, earlier_summary (an English summary and the facts an earlier pass recorded for this country; a pointer only, it has errors and gaps), text (the full Bangla article).

Your job: place everything usable from EVERY article into the guide as draft sentences with evidence. Full coverage is the target, not a selection.

Steps
1. Read every article IN FULL, to its last character (lines are long: print one at a time with Python, in slices if needed). Never work from the headline or the earlier summary alone.
2. For each article, draft every sentence that adds something the guide lacks, for this country in particular:
   - status and timeline: openings, closures, quotas, agreements, deadlines, amnesties, with dates;
   - rules and requirements: visas, permits, medical, skill tests, attestation, residence, labour law, what is banned, penalties;
   - costs: official fees and caps, what people actually paid and to whom, wages promised and paid, deductions;
   - how things work in practice: where to go, what to bring, how long it takes, what you get back; how a job reaches a worker and who takes a cut;
   - what goes wrong: unpaid or stranded workers, detention, deportation, deaths, injuries, compensation and how bodies come home, with numbers and cases;
   - services and contacts: embassy, labour wing, hotlines, apps, shelters, what help actually reached people;
   - numbers: departures, stock of workers, remittances, deaths, returns, with period and source;
   - named actors: employers, agencies, officials, with what is alleged and by whom.
   Use the guide's own section structure: the Background parts (In one minute; Is it open now, and who can go?; How a job reaches you, and who takes a cut; What you pay, and what you earn and keep; What ties you to the employer; What goes wrong most, and what people wrongly believe), the visa sections and their steps, and the later sections (if you aren't paid, changing employer, leaving, sending money home, if a worker dies, coming home, contacts and so on).
3. Each draft sentence must be one self-contained English sentence (country, date or period, who); say only what the article states, keeping its attribution ("the minister said", "according to the family", "police said", "the reporter found"); give numbers, dates, names and places exactly as printed; and carry one to three exact Bangla quotes copied from the article text that together support it (contiguous substrings of the text, at most 300 characters each, containing the key number, name or event). Never infer, never generalise, never add advice.
4. Where an article conflicts with the guide (a different figure, date or rule), still draft it, and say so in why_new with the guide's version.
5. Account for every article: it yields drafts, or goes in nothing_to_add with the reason.

Output: one JSON object written to the output path given in your instructions:
{
 "drafts": [ {"key": "<prefix>-<n>", "article_id": "...", "target_section": "<exact existing heading text in the country guide, or CROSS-COUNTRY: <exact heading>, or NEW: <proposed heading> (after <existing heading>)>", "placement": "<e.g. Status | The channels | Cases | The numbers | Step 3 item | Need to know | other: ...>", "claim": "...", "quotes": ["..."], "why_new": "what this adds, or the conflict with the guide"} ],
 "named_actors": [ {"article_id": "...", "name": "...", "kind": "...", "what_the_article_says": "...", "quote": "..."} ],
 "nothing_to_add": [ {"article_id": "...", "reason": "..."} ]
}

Validate with Python before finishing: every input article id appears in drafts or nothing_to_add; every quote is an exact substring of its article's text (if one fails, re-copy it from the text programmatically, never by retyping; the text mixes Unicode forms of letters such as য়). Write the output as you go so partial work is not lost.

Do not modify any file in the knowledge-base folder; scratch files only under /tmp; no network requests; no sub-agents.

Final message, at most 6 lines: articles read, drafts written (country guide / cross-country / new sections), named actors, articles with nothing to add, and any conflict with the guide a reviewer should know about.
