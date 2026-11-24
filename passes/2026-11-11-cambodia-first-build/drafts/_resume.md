# Cambodia: where we stopped (11 November 2026, about 12:40)

The user paused the work. Nothing is committed for Cambodia yet; everything is on disk in `countries/cambodia/`.

## Done
- Folder set up: `drafts/`, `verify/`, `manual/`, `sources/`, `work/<X>/sources/` for X = N W B L V U S G; helper scripts in `work/` (merge.py, apply.py, questions.py, addm.py), adapted for Cambodia.
- Research brief: `drafts/_brief.md` (8 agents; S = scam compounds and trafficking, the corridor's main danger; outline includes `## Scam compounds and trafficking`).
- Starting numbers (BMET OEP clearances): 1,378 in 2023, 12,263 in 2025, 3,700 in 1 Jan-7 Nov 2026 (2024 not saved).
- The 8 research agents ran about 50 minutes and were stopped before writing their findings files. Saved so far (facts logged in `work/<X>/facts.csv`, all quote-checked):
  - N corridor and money: 96 facts, 132 source files
  - W Cambodian work route: 102 facts, 69 files
  - B Bangladesh side: 242 facts, 254 files
  - L law and work: 90 facts, 103 files
  - V visits, study, family: 0 facts, 126 files (saved pages but logged nothing yet)
  - U irregular routes and asylum: 127 facts, 115 files
  - S scam compounds: 214 facts, 136 files
  - G money: 77 facts, 98 files
- No `drafts/<X>-findings.md` exists yet.

## To do when resuming
1. Relaunch the 8 agents with a short "resume" brief: read `_brief.md`, keep your existing `work/<X>/facts.csv` and `sources/` (do NOT re-log facts already there; check ids before adding), fill gaps for ~20 minutes, then write `drafts/<X>-findings.md` (a. draft doc text, b. notes, c. blocked pages, d. questions). V must log its facts from the 126 saved files first.
2. Merge: `python work/merge.py` (from countries/cambodia).
3. Give the user ONE blocked-pages list (`drafts/_blocked-pages.md`, exact URL + file name, save into `manual/`), then continue without waiting.
4. Gap agent for official texts the others couldn't get (MLVT prakas, GDI visa rules, Labour Law), as K did for Kyrgyzstan.
5. Writer brief (copy `../kyrgyzstan/drafts/_writer-brief.md`; 6-7 parts; add a part for Scam compounds and trafficking), assemble doc.md, build with `python ../../tools/build.py`.
6. Verify until zero failures (copy `../kyrgyzstan/drafts/_verifier-brief.md`; 7 verifiers, then rounds on changed lines), coverage audit (`../kyrgyzstan/drafts/_coverage-brief.md`), questions.py, notes.md.
7. Add `- [Cambodia](countries/cambodia/) (draft, under review)` to the root README; commit the country files locally (not drafts/work/verify/manual); do not push.
8. Final report: files, official vs news citations, rounds, open Need to know, possibly outdated, missing manual files, rating 1-100.
