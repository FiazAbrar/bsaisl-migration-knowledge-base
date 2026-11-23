Scam and harm case records: extraction spec

You are extracting structured case records from Bangla news articles (Prothom Alo, 2024-2026) about Bangladeshis who were cheated, trafficked or harmed while trying to go abroad for work. The records feed a knowledge base that helps would-be migrants avoid brokers and fraud, so the value is in concrete, ground-level detail: who took the money, how much, what convinced the victim, how it came apart.

Input: a .jsonl file, one JSON object per line with keys id, url, published, headline, section, text (Bangla). Read EVERY story in full, to the last line. Do not classify from the headline alone.

Output: exactly one JSON object per input story, same order, UTF-8, one per line. Write values in plain English (transliterate names; keep agency names as printed, adding the Bangla in brackets if the spelling is uncertain). Use null when the article does not say. NEVER guess or infer a value the article does not state; a null is far better than a guess. Amounts: give the number and currency as stated (e.g. "BDT 600,000", "about BDT 4.5 crore total from 200 people").

Fields:
- id, url, published, headline_en (short English translation of the headline)
- relevant: true if the article describes a specific case or pattern of fraud, trafficking, extortion, abandonment or abuse connected to going abroad from Bangladesh (work, study or visit visas used for work). false otherwise.
- not_relevant_reason: one phrase if relevant is false, else null. If false, fill the remaining fields with null.
- case_type: one of "fake visa or job offer", "agency took money and vanished", "overcharging or contract substitution", "trafficking or hostage for ransom", "irregular sea or land route", "recruited into war", "scam compound or forced crime", "stranded or unpaid abroad", "student or visit visa misuse", "official or syndicate corruption", "other"
- destination_promised (country, and job if stated)
- route_and_actual_destination (transit countries, where the person actually ended up)
- promised_job_and_wage
- visa_type_claimed
- amount_per_person, amount_total, payment_method (cash, bank, mobile banking, instalments), how_money_was_raised (loan, land sale, etc.)
- perpetrator_type: e.g. "licensed recruiting agency", "unlicensed agency or travel office", "village broker", "relative or neighbour", "Bangladeshi already abroad", "online contact", "foreign employer", "official"
- perpetrator_names: names of agencies, licence numbers (RL-...), office locations, individuals named, as printed
- how_victim_met_them
- trust_devices: list of the things that made it look real (fake visa, appointment letter, medical test, training, office premises, earlier people who went, video calls, part refund, etc.)
- timeline: key durations (how long from payment to discovery, time held, etc.)
- how_it_was_discovered: the moment and place the fraud or danger became clear (airport immigration, embassy check, on arrival, ransom call, etc.)
- what_happened_abroad
- victims_count, victim_home_districts
- harm: money lost, detention, torture, death, deportation, debt
- ransom_details: amount, how paid, to whom, if any
- official_response: police case and law cited, arrests, agency or ministry action, court outcome
- money_recovered: what the article says about refunds or recovery
- verification_mentioned: any check the article says exists or would have exposed it (who says so)
- advice_or_warning_in_article: warnings or advice quoted from officials, embassies, NGOs or experts, with who said it
- other_practical_details: any other concrete detail useful to a would-be migrant (prices, procedures, place names, which office, typical tricks)
- key_quote_bn: one short Bangla quote from the article (under 200 characters) that best captures the case, copied exactly

If an article covers several distinct cases, record the main one and put the others briefly in other_practical_details.
