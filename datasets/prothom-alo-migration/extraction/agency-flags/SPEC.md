Agency red flags from Prothom Alo: spec

Goal: find every recruiting agency, travel agency, visa or study-abroad consultancy, training centre or other firm that a Prothom Alo article (2024 to Nov 2026) links to cheating, overcharging, trafficking or harm of people going abroad, and record each allegation or official action as a flag row for the knowledge base's agency list, so migrants can be warned before they pay.

Read first:
- /Users/rarba/Programming/brac/bits-migration/kb-scam-cases/agencies/notes.md (how flags and RL matching work; read "RL matching", "Official red flags" and "Press and civil-society flags" in full).
- /Users/rarba/Programming/brac/bits-migration/kb-scam-cases/agencies/flags.csv and flags-press.csv (existing flags; columns rl, agency, flag_type, date, summary, source_url, fact_id). Use their flag_type vocabulary: licence-cancelled, licence-suspended, court-order, court-case, acc-case, acc-inquiry, cid-case, arrest, allegation, complaint, worker-complaint, ministry-inquiry, mobile-court-conviction, mobile-court-fine-sealed, ownership-link, show-cause, death-case-arrest; add a new type only if none fits.
- /Users/rarba/Programming/brac/bits-migration/kb-scam-cases/data/oep-agency-list-2026-10-28.csv (BMET's licence list: licence, name, address, phone, status, valid_until).

Inputs:
- articles file: one JSON per line (id, url, published, headline, text). Read EVERY article in full, to its last character; lines are long, so print one at a time with Python.
- candidates file: names an earlier pass picked out of these articles (fields name, kind, says, article_id). Treat it as a pointer only: it misses names and contains errors. Find every firm named in the text yourself.

For each firm-and-event in each article, write one flag object:
- article_id, url, published
- agency_as_printed: the firm's name as the article prints it (Bangla in brackets if you transliterated)
- rl_printed: the RL number only if the article prints it
- oep_match: the OEP list entry you match it to, as "RLnnnn Name (status)", or null. Match only when the name is the same or a clear spelling variant AND nothing contradicts it (address, district, owner). Say how confident: "exact", "spelling variant", or "uncertain: <why>". Never force a match; a travel agency or consultancy usually has no RL.
- firm_kind: licensed recruiting agency / travel agency / visa or study consultancy / training centre / medical centre / other
- flag_type: from the vocabulary above
- date: the date of the event as stated (or about the published date)
- summary: one sentence in the style of the existing summaries: "Prothom Alo reports ...", with the article's own attribution ("police said", "the case alleges", "victims say"), what is alleged or done, the corridor, and amounts. No inference.
- quote: one exact Bangla passage (at most 300 characters, a contiguous substring of the article text) that names the firm and supports the summary.
- already_flagged: if flags.csv or flags-press.csv already has a row for the same firm and the same event, give that row's fact_id; else null. A new event about an already-flagged firm is a new row.
- people: owners or staff named in connection with the firm, as printed, with their role.

Do not include: firms named only positively or neutrally (for example a BOESL notice), government bodies, foreign employers unless the article accuses them of something, or private individuals with no firm (those are brokers, not agencies).

Write a JSON list to the output path you are given, as you go. Validate with Python before finishing: every quote is an exact substring of its article's text (if not, re-copy it from the text programmatically); every oep_match RL exists in the OEP list. Do not edit any file in the repository; scratch files only under /tmp; no network requests; no sub-agents.

Final message, at most 5 lines: articles read, flag rows written, how many matched to an RL (exact / variant / uncertain), how many already flagged, and anything odd.
