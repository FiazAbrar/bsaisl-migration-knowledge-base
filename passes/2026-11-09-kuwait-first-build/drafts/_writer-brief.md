# Kuwait doc: writer brief (9 Nov 2026, HARD DEADLINE)

You assemble one part of `countries/kuwait/doc.md` from the research drafts. Root: `C:\Users\User\Desktop\Github\bsaisl-migration-knowledge-base` (ROOT). You have **18 minutes**. Write your part to `ROOT\countries\kuwait\drafts\part-<N>.md` and nothing else (no other files, no commits, no new research, no web).

## Inputs
- `ROOT\CLAUDE.md` (Format and Quality rules: skim the Format section only).
- Research drafts in `ROOT\countries\kuwait\drafts\`: `N-, W-, B-, L1-, L2-, D-, U-, V-, F-, G-, K-, S-findings.md` (section "a" is draft doc text). L1 and L2 cover the same topics; merge them, keeping the more specific, newer text.
- `ROOT\countries\kuwait\facts.csv`: the merged facts (ids like N0012, W0030, M0014). **Cite only ids that exist in this file.** Check with: `grep -c "^M0014," facts.csv`. To read a fact: `grep "^W0030," facts.csv`.
- Template for shape and tone: `ROOT\countries\maldives\doc.md` (newest finished doc).

## Rules (binding)
- Every sentence ends with fact ids in brackets: `[W0012, N0003]`. No uncited sentence. Never invent a fact; drop a sentence you can't cite.
- Headings: H2 per visa/big section, H3 per step/topic, H4 inside. No dates in headings. No tables. Bold only for list lead-ins and labels (`You'll need:` lines, `**Check it is real:**`, `**If it fails:**`).
- Steps are numbered actions starting with a bold verb phrase: `1. **Register on OEP,** BMET's website ...`.
- Gaps: a `> **Need to know**` quote block right after the paragraph/step, one precise question per bullet. Keep the best ones; cut duplicates.
- Cross-references use exact heading text: "(see If you aren't paid)", "(Work visa: private-sector worker (Article 18), Step 6)". Never "see above".
- A guide, not a research log: no "source X says", no conflicts in text (one Need to know line if it changes what someone does). Explain every acronym the first time it appears in your part.
- Prefer official facts over news where both exist for the same point.
- Money in KD with Taka where the draft has it (KD 1 = about Tk 403 [G-fact in G-findings]).
- 2026 context that must be reflected where relevant: Iran war from 28 Feb 2026, airspace closures, new entry visas suspended 22 Apr 2026 (S-findings); the resume date is unknown (Need to know). Embassy minimum salaries from 1 Aug 2025: cite M0014-M0024 (official circular) instead of news ids. Kuwait Visa portal facts M0001-M0013 (Bangladeshi tourist e-visa not eligible without US/UK/Schengen/GCC visa or permit; family visit eligible online; family visit stay up to 90 days, business 30 days).
- Concise: say the most in the fewest words; cut repetition between drafts.

## Parts (headings exactly as below)
- **Part 1**: `# Kuwait: migration guide` + intro paragraph (legend like the Maldives intro; KD->Tk rate; explain BMET, PAM (Public Authority for Manpower), Ministry of Interior, Sahel app, PACI). Then `## Background` with `### In one minute` (write last, 6-8 sentences), `### Is it open now, and who can go?` (#### Status, The channels, Who qualifies, Size, What closed it before), `### How a job reaches you, and who takes a cut`, `### What you pay, and what you earn and keep` (#### The cap, What people really pay, How it is paid, How they borrow, What the job pays, What goes unpaid, Money sent home, How long the debt takes), `### What ties you to the employer`, `### What goes wrong most, and what people wrongly believe`. Then `## Visas not open to Bangladeshis`. Sources: N, S, B (size), G, L, D, U, V.
- **Part 2**: `## Work visa: private-sector worker (Article 18)` with `### Step 1: Find a real job`, `### Step 2: The job offer and contract`, `### Step 3: The employer gets your work permit and visa`, `### Step 4: Passport, police clearance and certificates`, `### Step 5: Medical check and checking your visa is real`, `### Step 6: Orientation, BMET clearance and the flight`, `### Step 7: After arrival`, `### Scams`. Sources: B, W, K, N, M.
- **Part 3** (H3s continuing the Article 18 section, no H2): `### Your rights at work`, `### How long you can stay`, `### Your residence permit`, `### What can get you jailed or deported`, `### If you aren't paid`, `### If your employer reports you absent`, `### Changing employer or leaving` (with #### Going home on leave, Leaving at the end of the job), `### Bringing your family` (short; point to Family visa (dependants)). Sources: L1, L2, W, F, G, S.
- **Part 4**: `## Work visa: domestic worker (Article 20)` and `## Work visa: professional and skilled`. Sources: D, W, K, M.
- **Part 5**: `## Family visa (dependants)`, `## Visit visas (tourist, family, business)`, `## Transit and medical treatment`, `## Student visa`, `## Self-sponsorship and investor residence`, `## Changing visa type`, `## Asylum`, `## Having a child in Kuwait`. Sources: F, V, M, S.
- **Part 6**: `## Sending money home`, `## Undocumented workers and amnesties`, `## Going home without valid papers`, `## If a worker dies, is injured or loses the job`, `## Coming home`, `## Contacts`. Sources: G, U, L1, L2, B, F.

Final reply: 3 lines: lines written, number of distinct fact ids cited, anything left out.
