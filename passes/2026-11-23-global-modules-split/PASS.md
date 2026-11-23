# Split of the cross-country doc into four global modules

On 23 Nov 2026 the cross-country doc "Going abroad from Bangladesh" (`cross-country/`) was split into four docs under `global/`: `faq/`, `dalal-scams/`, `departure/` and `illegal-routes/`, one per H2 part of the old doc. No sentence was rewritten.

How (`scripts/split_modules.py`, then two clean-up steps):
- Each module's `doc.md` is its old H2 part with every heading promoted one level, under a new title and a one-paragraph intro.
- `facts.csv`: every fact the module cites, with its original id; a fact cited by two modules is in both. Facts no module cites (142) go to the module that cites most facts from the same source, or to `faq` if none does.
- `sources/`, `sources.csv`, `_fetchlog.csv`: every source a module's facts need; 125 sources used by more than one module are copied into each. Source files no fact uses (40 files, 6 registered sources) went to `faq/` so nothing was lost.
- `notes.md` and `questions.md`: each module gets its own part, plus the old doc's general notes.
- 26 references that now point to a heading in another module were rewritten as `see "<heading>" in the <module> doc`.
- Each module builds with `tools/build.py` with no citation errors.

Also updated: the repo README, CLAUDE.md (what goes in a global doc and what in a country doc), and the navigator bot's index of shared guides.
