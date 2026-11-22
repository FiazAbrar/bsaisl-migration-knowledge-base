# Knowledge base review

> **Re-check on 22 Nov 2026 against the updated guides (15 countries).** The full review below is from 17 Nov 2026 and covered 12 countries.
>
> **Fixed since 17 Nov:**
> - The police-clearance SMS line ("PCC S <reference number>") now shows correctly in every Word file.
> - Every Word file now has numbered headings (Oman, Jordan and Singapore had none).
> - Repeated cross-reference text ("After arrival: After arrival") is almost gone (one each in Cambodia, Japan and UAE).
> - The UAE "Internal (team only, not public)" note is gone.
> - Lists merging into one paragraph is mostly fixed in the Word files; Qatar and UAE still show some.
>
> **Still open:**
> - Qatar still links `bdembassydoha.org/pa/Travel_permit.pdf`, which opens a gambling site. Remove it.
> - Maldives still says "At the High Commission in Kuala Lumpur" for birth registration (that is the Malaysia mission).
> - Saudi Arabia and Singapore still mention the repo's agencies folder or `agencies/README.md` inside the guide text.
> - Not re-checked automatically: the contradictions, Bangladesh-side fee drift, expired dates and sensitive content listed below. Brunei, Japan and South Korea were not reviewed.

---


Read-only review of `knowledge/`. No source file was changed. The 12 country .docx files plus the agencies .docx were converted to text and read in full; the CSVs, tools, official PDFs and folder layout were checked by script.

## 1. What's in the folder

| Part | What it is |
|---|---|
| `countries/<c>/<Country>.docx` | **Final deliverable.** Built from `doc.md` by `tools/build.py` (README.md is the same doc in Markdown). |
| `countries/<c>/doc.md` | The only hand-edited source; cites fact ids such as `[B0031]`. |
| `countries/<c>/facts.csv` | One row per fact: claim, exact quote, saved file, URL, page date, official/news, status (verified / possibly-outdated / conflict / unofficial / lead), plus optional `visa, field, value`. |
| `countries/<c>/sources.csv` + `sources/` | Saved copies of every page/PDF (the bulk of the 3.4 GB). |
| `countries/<c>/questions.md`, `notes.md` | Open "Need to know" questions; research notes and conflicts. |
| `drafts/ manual/ verify/ work/` | Only in Cambodia, Italy, Kuwait, Kyrgyzstan: agent briefs, doc snapshots, verifier rounds, raw working files, screenshots. Process residue, not knowledge. |
| `agencies/` | `Recruiting agencies.docx` + `agencies.csv` (293 agencies), activity from BMET permission letters, red flags (court/ACC/press), facts and sources. |
| `data/oep-agency-list-2026-10-28.csv` | BMET's full licence list: 2,859 agencies (RL, name, address, phone, status, expiry). |
| `official-pdfs/` | 10 Bangladesh-side PDFs (Ministry, WEWB and PKB charters, the PKB loan page, the BMET safe-migration leaflet, Saudi notices). One (the skill-test notice) has no text layer, so it needs OCR. |
| `tools/` | `fetch.py`, `facts.py`, `build.py`, `datepass.py`, `wayback.py`, `agency_counts.py`. |
| `CLAUDE.md`, `PROMPT.md`, `plans.md` | The doc standard, the new-country prompt, and planned work (shared Bangladesh-side text, answering open questions, repo size). |

## 2. The 12 countries at a glance

| Country | Words | Status as the doc states it | Legal cap → real cost | Need to know |
|---|---|---|---|---|
| Saudi Arabia | 41k | Open but disrupted (flights, Feb 2026 visa cancellations); 315,935 Jan–17 Oct 2026 | Tk 1.65 lakh → Tk 3.5–5 lakh (up to 9) | 119 |
| Malaysia | 58k | Closed to private agencies since 31 May 2024; restart announced 15 Oct 2026, nobody flown; BOESL zero-cost 10k | Tk 78,990 (2022) → Tk 6–7.5 lakh asked | 155 |
| Qatar | 63k | Open at ~60% of 2025's pace; 53,611 to 6 Nov | Tk 1,00,780 → Tk 4–10 lakh | 192 |
| UAE | 47k | "Mostly closed" since Jul 2024; Oct 951, first week of Nov 63 | Tk 1,07,780 → Tk 3.5–7 lakh | 116 |
| Singapore | 63k | Open; 66,657 to 7 Nov (2nd largest) | Tk 2,62,270 → S$9–13k (Tk 8.7–12.6 lakh) | 93 |
| Kuwait | 40k | Company visas (Art. 18) issuing again after the war; domestic (Art. 20) closed to Bangladeshis | Tk 1,06,780 (news only) → Tk 7–10 lakh | 111 |
| Oman | 42k | Closed to ordinary work visas since 31 Oct 2023; farm/fishing quotas only; 506 cleared in 2026 | Tk 1,00,780 → Tk 1.8–3.5 lakh | 125 |
| Maldives | 40k | Open, busy; 32,408 to 7 Nov | Tk 95k–1.15 lakh → Tk 2–4 lakh | 104 |
| Jordan | 42k | Open for garment (QIZ) and women domestic workers; most other sectors stopped 1 Jun 2026 | BOESL "no cost"; private Tk 1,74,300 → Tk 40k–2.5 lakh | 118 |
| Italy | 52k | Open via Decreto Flussi; 2027 click days 12 Jan to 18 Feb 2027 | No BD cap; VFS Tk 21,830 → EUR 7–20k (Tk 9.8–27.9 lakh) | 120 |
| Cambodia | 41k | Closed in practice via BMET (4 Nov 2026 12-country order); scam-compound section | Tk 80k–1.55 lakh → Tk 2–10 lakh | 90 |
| Kyrgyzstan | 35k | Closed in practice via BMET (11 cleared in 2026); no MoU | No BD cap → Tk 3–7 lakh | 104 |

Every doc has the full standard skeleton from CLAUDE.md. Oman, Jordan and Singapore also have a "Start here" quick-answer section, which the other nine lack. Saudi Arabia has no "Visas not open to Bangladeshis" section. In Italy, Kuwait, Malaysia, Singapore and others, that section comes before the visas rather than after.

## 3. Mechanical checks (all docs)

- **Citations resolve.** Every fact id cited in every `doc.md` exists in its `facts.csv`.
- **Evidence status of cited facts:** a large share is `possibly-outdated` (old or undated official pages) or `unofficial`/`lead` (news only). In Qatar, 862 of the 1,420 cited facts are possibly-outdated. By the docs' own rule, news-only facts "need an official source, or a reviewer's confirmation, before the Navigator uses it".
- **Structured fields are sparse.** Only 34 (Cambodia) to 444 (Malaysia) facts per country carry `visa/field/value`, and the field names aren't normalised across countries (`age` vs `age_kuwait` vs `Age limits`).
- **Re-check dates:** only Saudi Arabia has one (7 Dec 2026). The other docs have none on their status lines.

## 4. Build bugs in the .docx (systemic: fix in `build.py` or `doc.md`, then rebuild)

1. **Lists collapse into one paragraph** wherever a `- ` list in `doc.md` follows a paragraph line with no blank line between. Glued lists per doc: Singapore 55, Qatar 52, UAE 34, Malaysia 31, Jordan 28, Kuwait 25, Oman 24, Maldives 24, Saudi Arabia 16, Italy 15, Cambodia 12, Kyrgyzstan 11.
2. **The `<reference number>` placeholder is stripped.** Nine docx files tell readers to text `"PCC S ” to 26969`, with no reference number: Cambodia, Jordan, Kuwait, Kyrgyzstan, Maldives, Oman, Qatar, Singapore and UAE. Pandoc treats `<...>` as HTML.
3. **No heading numbers** in Oman, Jordan and Singapore (the 14 Nov builds). The other nine are numbered.
4. **Doubled cross-reference text**, for example "Step 7: After arrival: After arrival". Counts: Kuwait 8, Cambodia 7, Kyrgyzstan 3, and 1 each in Malaysia, Maldives, Qatar and UAE.

## 5. Content problems worth fixing before a chatbot uses this

### Leaks and internal notes in published text

- **UAE §3.1 item 3:** "Internal (team only, not public): … team's agencies list".
- **Repo paths and "counted by the team" narration:**
  - "agencies folder" / `agencies/README.md`: Saudi, Malaysia, Qatar, Singapore, Maldives.
  - "its page wouldn't load for us": Qatar.
  - "a search … returns nothing": Oman, Jordan, Kuwait.
- **Dead link to a gambling site:** Qatar §19.2 links `bdembassydoha.org/pa/Travel_permit.pdf`, which now opens a gambling site. Remove it.

### Wrong country or wrong target

- **Maldives §17:** the birth-registration steps say "At the High Commission in Kuala Lumpur".
- **Oman:** reference N61 is a Saudi abuse story. The death-claims cross-reference was copied from Jordan.
- **Saudi §1.2.1:** reference N13, a story about Saudi prisons, is cited for talks on extending visas.

### Contradictions inside a doc (examples)

- **Saudi Arabia:**
  - Bought "fit" medical: Tk 25k vs 30–80k vs 20–30k.
  - Iqama bill: SR 9,150–10,350 vs SR 11,000.
  - Ages: 21–60 vs 18–60.
  - Two different 16135 numbers for calls from abroad.
- **Kuwait:**
  - Salary due by the 20th vs the 7th.
  - Health insurance: KD 5 a month vs KD 100 a year.
- **Oman:**
  - Permit fee: RO 200/250/300 vs 201/251/301.
  - Two different embassy addresses.
  - Two different labour-wing email sets.
- **Jordan:**
  - PDO: Tk 200 vs Tk 305.
  - Three different BOESL age ranges.
  - Ban after deportation: "unless status corrected" vs "5 years".
- **Italy:**
  - Assegno sociale: EUR 7,002.97 vs EUR 7,101.12.
  - Two different Milan welfare emails.
  - The Questura/INL check is stated as current, while the doc's own Need to know says it lapsed.
- **Malaysia:**
  - Labour-wing phone 0934 (a fax number) vs 0929.
  - The welfare fee of Tk 5,500 is counted among 2022–24 fees.
- **UAE:**
  - MoFA attestation: Tk 200 a page vs "free".
  - Some Need-to-know blocks swallow real content (§1.2, §17, §24).
- **Kyrgyzstan:** the tourist visa is listed as "not open" in §2 but allowed in §6.1.
- **Cambodia:** two names for the same 2026 Act, and three different clearance totals.
- **Qatar:** the approval letter is dated 1 Sep 2025, but it is really 1 Sep 2024. The error was copied into Jordan.

### Bangladesh-side figures that drift between countries

`plans.md` already flags this risk. These figures are found in two or more versions:

| Item | Versions found |
|---|---|
| BMET clearance / smart-card fee | Tk 250 stated as fact (Kuwait, Italy, Oman, Qatar, Singapore) · Tk 250 plus a Need to know about its Dec 2024 abolition (UAE, Malaysia, Maldives) · no figure (Saudi Arabia) |
| Source tax, single visa | Tk 250/400 (most) vs Tk 500 (Saudi Arabia) |
| PDO fee | Tk 200 (Feni TTC) · Tk 100 + 100 (Saudi Arabia) · Tk 305/200 (Jordan) · "set by the institute" (Italy) |
| OEP registration fee | Tk 200 (most) vs a Need to know (Jordan, Qatar) |
| Insurance covers departures from | 12 Mar 2023 (Oman, Qatar, Singapore, Cambodia) vs 1 Jan 2023 (Jordan, UAE, Malaysia) |
| Welfare Board injury/treatment grant | Tk 2 lakh (Saudi Arabia, Kyrgyzstan, Malaysia) vs Tk 1 lakh (Kuwait) vs a Need to know (Cambodia) |
| Legal aid hotline | 16430 (Saudi Arabia, 2023 news) vs 16699 (Kuwait, official 2026) |
| PKB women's loan | "same terms" (Qatar) vs "one guarantor, no fee" (UAE) |
| Wage Earner Bond | "12% at maturity" (Cambodia) vs "every six months" (Kyrgyzstan) |
| Airport desk / Wage Earners' Centre / Ministry grievance contacts | different numbers and emails across Saudi Arabia, Kuwait, Malaysia and Singapore |
| BMET director email | diremi@ labelled Director (Emigration) in one place and Director (Employment) in another, with different phones (Saudi Arabia, Kuwait) |

### Dates already past or expiring within weeks

- **Already past (dates within the next few days included):**
  - Maldives: the "remove the rest by 17 Nov 2026" target.
  - Jordan: the BOESL test on 13 Nov.
  - Malaysia: the DHL window, 6–8 Nov.
  - Cambodia: the waiver due to end 31 Oct.
  - Singapore: the Deepavali dates.
  - Kyrgyzstan: the garment fee rate that lapsed 1 Nov.
  - Italy: Questura registration "until 31 Oct".
- **Expiring within weeks:**
  - Italy: student deadline 30 Nov; pre-fill until 7 Dec.
  - Jordan: regularisation deadline 1 Dec.
  - Saudi Arabia: Hajj registration 10 Dec.
  - Malaysia: MoU ends 31 Dec.
  - Kyrgyzstan: the Temporary Regulation ends 31 Dec.

### Sensitive content for a public bot

- **Named people with allegations:**
  - Malaysia: Amin and Ruhul Amin Swapan.
  - UAE: MP Kiron and his wife.
  - Italy: embassy bribery suspects.
  - Kyrgyzstan: brokers by first name.
- **Named victims with their villages:** Jordan.
- **Brands:** linked to a worker's suicide in Jordan.
- **Personal WhatsApp and phone numbers of officials:** these go stale quickly.
- **Lists that can read as endorsements:**
  - Singapore: 22 agents with phone numbers, and BRAC Probashbandhu used as the example agency.
  - Jordan: the list of 21 agencies.
  - Malaysia: agencies with "nothing reported".
- **BRAC described as "the organisation behind this guide":** Jordan, Singapore and the agencies doc.

## 6. Implications for the WhatsApp bot

- **The .docx is a rendering, not the best input.** Ingest `doc.md`, which has clean heading structure and fact ids, together with `facts.csv`. Then each answer can carry its quote, source URL, date and official/news status. The .docx loses that link.
- **Chunk by H3/H4 heading.** Some steps are 2–4k words (Saudi §2.2.2, Qatar §3.2, Malaysia PLKS Step 1, Italy §3.7), so chunk those by numbered item.
- **Treat "Need to know" blocks as open questions, never as answers.** There are about 1,450 of them across the docs.
- **Gate every work-visa answer on the country's current status.** Malaysia, UAE, Oman, Cambodia and Kyrgyzstan are closed or near-closed. Status lines need a re-check date and an owner.
- **Decide a policy for news-only facts** (`unofficial`/`lead`). The docs' own rule says they need confirmation before the Navigator uses them.
- **Fix the shared Bangladesh-side figures once**, as `plans.md` proposes, before the bot quotes fees.
