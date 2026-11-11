# Cambodia doc: coverage audit (time limit about 25 minutes)

Root: `C:\Users\User\Desktop\Github\bsaisl-migration-knowledge-base\countries\cambodia` (KW). Read `..\..\CLAUDE.md` (Quality rules and Research process step 9) and `KW\doc.md`. Do not edit doc.md; no web research; no commits.

Do the three audits of CLAUDE.md step 9 on doc.md, using ONLY facts already in `KW\facts.csv`:
1. **Migrant's questions:** how long can I stay, what will I earn, my rights at work, what gets me jailed, bank account and SIM, pension, can my family come, what can I bring home.
2. **Aim per visa:** types, requirements, where to apply, cost, processing time, appeal if refused, scams both ways, can the holder work, claim asylum, have a child, bring a spouse; changing visa type; asylum written to discourage; corridor numbers vs other countries, bans, growth.
3. **Insider test** (journalist, corridor expert, returnee): the big names, scandals, crackdowns, real costs, common scams. And review every fact in facts.csv NOT cited in doc.md (list cited ids with a regex over doc.md): was it left out for a good reason (duplicate, off-topic, superseded, weak)? If a fact would add substance a migrant needs, propose where it goes.

Write `KW\verify\coverage.md` with:
- Edit blocks in this exact format (applied by a script; old must be an exact fragment occurring once in doc.md, on one line):
  ```
  ### FAIL <short reason>
  old: <exact fragment>
  new: <replacement, with fact ids in brackets>
  ```
  Use them to add a missing sentence (new = old fragment + the new sentence) with existing fact ids only, every sentence cited, in the doc's style (USD with Taka at USD 1 = about Tk 124.65 [G0002], 1,000 riel = about Tk 30.5 [G0003]; explain terms on first use; exact heading cross-references).
- For a gap no fact fills, add ` NEEDTOKNOW: <precise one-line question>` at the end of the `new:` text of the relevant line (the script turns it into a Need to know block). Don't duplicate an existing Need to know.
- At the end, a short list "Uncited facts left out on purpose" with reasons, grouped.
Cap: about 25 edit blocks, the most valuable first.

Final reply: 3 lines: edits proposed, Need to know added, the biggest remaining gap.
