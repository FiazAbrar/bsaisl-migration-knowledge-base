# Migration Pathway Navigator: country knowledge base

Step-by-step guides for people in Bangladesh who want to work abroad, one doc per destination country. Each doc covers every visa open to Bangladeshis, the steps in the order a worker takes them, what each step costs, how to check papers are real, the scams to watch for, and where to complain. Every sentence is cited.

Part of the Migration Pathway Navigator at BSAISL (BRAC Student AI Solutions Lab). The docs are read first by the team, then fact-checked by corridor experts, and later used by a WhatsApp chatbot for aspirant migrants.

## Countries

| Country | Doc | Status |
|---|---|---|
| Saudi Arabia | [countries/saudi-arabia](countries/saudi-arabia/) | Draft, under review |
| Malaysia | [countries/malaysia](countries/malaysia/) | Draft, under review |

Open a country folder to read its doc on GitHub. The same text is in the `.docx` in that folder.

## How it's organised

- `countries/<country>/`: the doc (`README.md` and `<Country>.docx`), its source (`<name>.src.md`), research notes (`findings.md`) and the evidence: a saved copy of every source in `raw/`, and `ledger.csv`, which logs each fact with the exact quote that supports it.
- `tools/`: shared scripts for saving sources, logging facts and building the doc.
- `official-pdfs/` and `data/`: Bangladesh-side documents and BMET's recruiting-agency list, shared by all countries.
- `CLAUDE.md`: the rules every doc follows (format, quality, research process). `PROMPT.md`: the message to paste into Claude Code to start a new country.

## Working on a doc

1. Clone the repo and install pandoc (`brew install pandoc`).
2. Open Claude Code in the repo and paste `PROMPT.md` with your country filled in.
3. To rebuild a doc: `cd countries/<country>` then `python3 ../../tools/build.py`.

Reviewers comment on the doc in Google Docs (upload the `.docx`). Changes go into the source, never into the Google Doc, and the doc is rebuilt.
