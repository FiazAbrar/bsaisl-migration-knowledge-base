Paste this into Claude Code from inside the repo folder, with <COUNTRY> replaced by the country you're researching.

---

I'm working on the Migration Pathway Navigator knowledge base for BSAISL. CLAUDE.md in this repo explains the project, the settled doc format, the quality rules and the research process. They are binding.

My country is <COUNTRY>.

1. Read CLAUDE.md. Then read the two draft docs, countries/saudi-arabia/README.md and countries/malaysia/README.md, to see the format; they are drafts, not finished standards, so follow the rules in CLAUDE.md where they differ. Skim the PDFs in official-pdfs/ for the Bangladesh-side steps that apply to every country.
2. Before researching, list every visa type open to Bangladeshis for <COUNTRY>, most-used first, and the sections the doc will have. Show me that outline and wait for my OK.
3. Research following the process in CLAUDE.md: topic by topic, official sources first, then the practical pass in Bangla news, NGO reports and agency guides. Read official PDFs in full. If a site blocks you, try Firecrawl; if that fails, give me the exact link to download. Save every source and log every fact with the tools in tools/, and keep notes in countries/<country>/findings.md.
4. Write countries/<country>/<country>.src.md, citing ledger ids, then build README.md and the .docx with tools/build.py. Commit as you go.
5. Before handing it over, do the line-by-line pass and both audits in CLAUDE.md (the migrant's questions, and the original aim per visa). Then tell me plainly which files you made, how many citations are official versus news, and every "Need to know" still open.

Ask me whenever something is unclear. Don't skip a source because it's hard to get.
