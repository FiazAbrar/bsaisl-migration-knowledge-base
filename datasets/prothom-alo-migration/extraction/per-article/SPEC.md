Full-read fact extraction: spec

Purpose. We are building guides for Bangladeshis who want to work abroad: one guide per destination country, covering visas, steps, costs, rights, what goes wrong, and coming home. You will read Bangla news articles (Prothom Alo, 2024 to Nov 2026) and record every concrete fact in them that such a guide could use. A later step will search your records instead of the articles, so anything you leave out is lost, and anything you invent is poison.

Rules
1. Read EVERY article in full, to its last character. Lines are long: print one story at a time with a small Python script (in slices if needed). Never judge from the headline or the opening paragraphs. Long features often carry their best material at the end.
2. Record only what the article states. Never infer, round, convert or fill in from your own knowledge. If the article is vague, be vague in the same way. If two figures in the article disagree, record both and say so.
3. Write in plain English. Keep names of people, agencies, offices, laws, apps and places as printed (transliterated; add the Bangla in brackets when the spelling is uncertain). Give amounts with currency as stated ("BDT 550,000", "5.5 lakh taka" both fine; do not convert currencies).
4. Every fact must stand on its own: a reader who has not seen the article must understand it. Put the country, the date or period, and who is speaking inside the statement.
5. Dates: give the date of the event as the article states it. If the article says only "last Tuesday", work it out from the published date only when unambiguous, and otherwise write it as "about <published date>".

Input: a .jsonl file, one object per line with keys id, url, published, headline, section, text.

Output: one JSON object per input story, same order, one per line, UTF-8, with these keys:
- id, url, published
- headline_en: short English translation
- relevant: true if the article has anything usable about Bangladeshis going abroad for work or study, living or working abroad, being cheated or harmed on the way, or coming home (including remittances, home-side services and government action on these). false for everything else.
- not_relevant_reason: one phrase when relevant is false, else null. When false, set the remaining keys to null or [].
- kinds: list, any of: "market status" (a destination opening, closing, limiting or resuming hiring), "recruitment notice", "cost or fee", "home-side service" (bank loans, welfare board, BMET, training, airport, passport, apps), "destination rule" (residence, permits, amnesties, deadlines, labour law), "death or compensation", "detention, deportation or return", "unpaid or stranded", "women workers", "agency or syndicate", "fraud case", "trafficking or irregular route", "war or safety", "remittance or customs", "student or skilled route", "statistics or research", "opinion or commentary", "other"
- countries: destination or transit countries the article is actually about (not passing mentions)
- summary_en: 2 to 4 sentences saying what the article reports
- facts: a list. One item per distinct usable fact. Be exhaustive; a rich article may yield 15 or more. Each item:
  - type: one of "status" (market open/closed/quota/agreement), "rule" (law, requirement, deadline, eligibility), "official_cost" (a fee, fare or cost set or stated by an authority), "amount_paid" (what a person actually paid or was asked to pay), "wage" (promised or actual pay, hours, contract terms), "process" (how something is done in practice: where to go, what to bring, how long, what you get), "service" (what a body or scheme offers and its terms), "contact" (hotline, office, email, app, website as printed), "death_or_injury", "compensation" (grants, insurance, payouts, body repatriation), "detention_or_return", "unpaid_or_stranded", "fraud_method" (how a trick works), "route" (path, transit, price of an irregular route), "named_actor" (an agency, company or person and what the article says they did, with case status), "enforcement" (cases, arrests, licence actions, court outcomes), "statistic" (a number with its period and source), "safety" (instructions in a war or emergency), "warning_or_advice" (advice the article quotes), "other"
  - country: the destination country it concerns, or "Bangladesh" for home-side facts, or null
  - date: when it happened or took effect, as stated; null if not stated
  - statement: one or two self-contained English sentences with every number, name and place the article gives for this fact
  - source_in_article: who the article attributes it to (a named official, a ministry notice, a victim, police, a study, the reporter's own finding), or null
- named_actors: list of {name, kind ("recruiting agency", "travel agency", "employer", "broker", "official", "other"), licence_no (only if printed), location, what_the_article_says, status} for every agency, company or accused person named
- people_cases: list of short objects for each individual migrant's story in the article: {who (name, age, home district as printed), destination, paid, to_whom, what_happened, outcome}
- key_quote_bn: one Bangla quote under 200 characters copied exactly from the article, capturing its most useful point; null if not relevant

After writing, validate with Python: the output has exactly as many lines as the input, each parses as JSON, ids match in order, and every non-null key_quote_bn is an exact substring of its article's text or headline (apply Unicode NFC to both sides before comparing). Fix problems before finishing.

Write only the output file named in your instructions, plus scratch files under /tmp. Do not touch anything else and make no network requests.

Final message: at most 5 lines: records written, how many relevant, total facts recorded, and anything that went wrong or any article you could not read in full. Do not paste records.
