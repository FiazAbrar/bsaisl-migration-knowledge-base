# Kyrgyzstan doc: writer brief (10 November 2026)

You assemble one part of `countries/kyrgyzstan/doc.md` from the research drafts. Root: `C:\Users\User\Desktop\Github\bsaisl-migration-knowledge-base` (ROOT). Time: about 25 minutes. Write your part to `ROOT\countries\kyrgyzstan\drafts\part-<N>.md` and nothing else (no other files, no commits, no web research).

## Inputs
- `ROOT\CLAUDE.md`: Format and Quality rules. Binding.
- **The standard: `ROOT\countries\malaysia\doc.md`** (and `ROOT\countries\italy\doc.md`, the newest). Match their depth, step pattern ("You'll need:", nested click-by-click steps, `**Check it is real:**`, `**If it fails:**`), escalation ladders and tone. Read the matching sections before writing.
- Research drafts in `ROOT\countries\kyrgyzstan\drafts\`: `N-, W-, B-, L-, V-, U-, G-findings.md` (section "a" is draft doc text; "d" the open questions).
- `ROOT\countries\kyrgyzstan\facts.csv`: the merged facts. **Cite only ids that exist in this file** (check: `grep -c "^W0030," facts.csv`; read: `grep "^W0030," facts.csv`). Prefer official facts (source_type official) over news for the same point.

## Rules (binding)
- Every sentence, and every list item that states a fact, ends with fact ids: `[W0012, N0003]`. Never invent a fact; drop what you can't cite.
- Headings exactly as listed below; H2 per visa/big section, H3 per step/topic, H4 inside. No dates in headings. No tables. Bold only for list lead-ins and labels.
- Steps are numbered actions starting with a bold verb phrase. Explain every acronym and Kyrgyz or Russian term the first time it appears in your part (Unified Permit / Единое разрешение, resident card, e-Visa portal, MFA, Ministry of Labour, Social Security and Migration, GKNB, MVD, som/KGS, INN, Social Fund, OEP, BMET, WEWB, PKB ...).
- Gaps: `> **Need to know**` block right after the paragraph or step, one precise question per bullet. Keep the best; cut duplicates and any question a fact now answers.
- Cross-references use exact heading text: "(see If you aren't paid)", "(Work visa: company worker, Step 5)". Never "see above".
- A guide, not a research log: no "source X says", no conflicts in the text (one Need to know line if it changes what someone does). No advice or conclusions of our own.
- Money: give the source's currency with Taka: KGS 1 = about Tk 1.42 and USD 1 = about Tk 124.42 (cite G0003 or G0002 with the conversion). Round sensibly (Tk 24,900; Tk 1.4 lakh).
- Concise: say the most in the fewest words; no repeats between sections (point to the step that owns a procedure).

## Known decisions
- **Status (state it, dated):** BMET's OEP clearances for Kyrgyzstan: 1,713 in 2023, 12,747 in 2024, 6,652 in 2025, then 57 in August 2025, 1 in September and 11 in all of 2026; no published BMET or Kyrgyz order explains the stop. Kyrgyzstan still issued 3,872 work permits to Bangladeshis in 2026 (to 1 October), so people still go, many without BMET clearance. One Need to know asks why clearances stopped.
- **Legal frame:** since 30 April 2026 Cabinet Resolution No. 312 (a Temporary Regulation valid to 31 December 2026) governs visas, the Unified Permit and the resident card; the 2017 visa rules are suspended; a September 2026 presidential decree moves these functions from the MFA to the Ministry of Labour. Say once in the intro of the work visa that the rules are temporary to 31 December 2026.
- Prefer L's official law texts (Labour Code, Code of Offences, Law On External Migration, Criminal Code, Resolution 312) over news for fines, bans, exit-visa fees and rights. The general Unified Permit fee is unknown (Annex 5 not found): give the 2025 / garment-sector rate as what it is, plus a Need to know.
- Agencies: name only with outside evidence, attributed and dated (e.g. the two agencies flagged by 2022 reports, Jannat Trade International's owner arrested by CID in 2024). No agency is recommended.
- "Kyrgyzstan is a door to Europe" goes in "What people believe", set against the cases (jail, deportation, the 180 returnees of 10 September 2025).
- The Bangladesh Embassy in Tashkent covers Kyrgyzstan; use B's section for its services and point to it.

## Parts (headings exactly as below)
- **Part 1**: `# Kyrgyzstan: migration guide` + intro paragraph (legend like countries/italy/doc.md's intro: raised number = official, N = news, "Need to know", "You'll need:"; the KGS->Tk and USD->Tk rates; explain BMET, OEP, the Unified Permit, the resident card, the e-Visa portal, the MFA and the Ministry of Labour). Then `## Background`: `### In one minute` (write last, 6-8 sentences); `### Is it open now, and who can go?` (#### Status, The channels, Who qualifies, Size, What closed it before); `### How a job reaches you, and who takes a cut` (H4s from N); `### What you pay, and what you earn and keep` (#### The cap, What people really pay, How it is paid, How they borrow, What the job pays, What goes unpaid, Money sent home, How long the debt takes; G's cost of living fits under What the job pays); `### What ties you to the employer` (one line each: enter, renew, quit, change employer, leave; which law covers which jobs; what leaving the job or an expired permit does); `### What goes wrong most, and what people wrongly believe` (#### What people believe, and the facts; #### Irregular routes, and where an irregular stay ends). Then `## Visas not open to Bangladeshis`. Sources: N, B, G, U, W, L, V.
- **Part 2**: `## Work visa: company worker` with a 2-3 line intro, `### Step 1: Find a real job`, `### Step 2: The job offer and contract`, `### Step 3: The employer gets your work permit`, `### Step 4: Passport, police clearance and certificates`, `### Step 5: The work visa, and checking it is real`, `### Step 6: Orientation, BMET clearance and the flight`, `### Step 7: After arrival`, `### Scams` (#### Done to workers, #### Tried by workers). Sources: B, W, N, L, U.
- **Part 3** (H3s continuing the company-worker H2, no H2 of its own): `### Your rights at work` (H4s from L; G's tax and deductions block goes here as `#### Tax and deductions from your pay`), `### Your residence permit` (#### How long you can stay, Renewing, If you lose your job, Permanent residence and citizenship), `### What can get you jailed or deported`, `### If you aren't paid`, `### Changing employer or leaving` (#### Changing employer, Going home on leave, Leaving at the end of the job), `### Bringing your family` (short; point to Family). Sources: L, W, V, G.
- **Part 4**: `## Other work routes` (from W: several employers, self-employed, patent), `## Student visa`, `## Visit visa`, `## Family`, `## Changing visa type`, `## Having a child in Kyrgyzstan`. Sources: V, W.
- **Part 5**: `## Asylum`, `## Irregular routes and undocumented workers`, `## Going home without valid papers`. Sources: U, L, B. Asylum is written to discourage but accurately.
- **Part 6**: `## Sending money home`, `## If a worker dies, is injured or loses the job`, `## Coming home` (with G's "What you can carry home"), `## Contacts` (with `### The Bangladesh Embassy in Tashkent`, `### Contacts in Kyrgyzstan`, `### Contacts in Bangladesh`). Sources: G, L, B, U.

Final reply: 3 lines: lines written, distinct fact ids cited (all checked to exist), anything left out.
