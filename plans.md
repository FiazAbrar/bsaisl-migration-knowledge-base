# Plans

Work we've decided to think through before starting.

## Write each Bangladesh-side step once

The same Bangladesh-side procedures appear in every country doc, written separately each time: OEP registration, TTC training, the medical check, police clearance, pre-departure orientation (PDO), BMET clearance and the smart card, PKB loans, the Wage Earners' Welfare Board, complaints to BMET and the Ministry, and coming home. They have already drifted apart: the Saudi doc said the smart card is free while Malaysia gave Tk 250 from BMET's newer charter. Every new country multiplies the risk.

The idea: write each procedure once, in a shared folder with its own facts and sources, and have the build insert it into every country doc, followed by a short country-specific part (what's different for that country). Fixing a fee then fixes it everywhere.

To decide first:

- Which procedures are truly identical across countries, and which only look alike (clearance papers, fees and the medical differ by destination).
- How a country doc shows the shared text: inserted in full, so each doc still stands alone, or summarised with a link.
- How shared facts and citations work with each country's own reference list.
- Who owns the shared procedures once fellows are working on separate countries.

## Answer the open questions

Each country has a `questions.md` listing every "Need to know" in its doc (Saudi Arabia 219, Malaysia 290, Qatar 334). Desk research can't answer most of them: the answers sit in offices, behind logins, in insiders' experience or in unpublished data.

The idea:

1. Triage every question by priority (does it block a common decision?) and by who can answer it (an office, a portal, an insider, a Right to Information request, or nobody, so cut it). Merge the Bangladesh-side questions shared across countries.
2. Turn each list into something an insider can answer quickly, for example by stating our current best answer and asking them to confirm or correct it.
3. Answer by channel: calls and visits to offices with scripts, portal walk-throughs with screenshots, insider sessions of about 20 questions each, and Right to Information requests to BMET and the Ministry.
4. Save every answer as a source (call note, screenshot, interview note, RTI reply) so it can be cited like any other fact; an insider's answer gets its own citation type.
5. Track every question in one place: priority, channel, owner, status, answer.

To decide first: who makes the calls and walk-throughs, whether insider answers can be cited and how, which insiders we can reach (BRAC's Migration Programme first?), where the tracker lives, and how much must land before 3 December.

## Repo size

The repo is about 940 MB and grows with every country, mostly from saved sources (pages and PDFs kept as evidence). Everything ever pushed stays in history, so deleting files later doesn't shrink it. Options to decide before it gets much bigger: Git LFS for PDFs, or keeping saved sources outside the repo with a checksum list in it.
