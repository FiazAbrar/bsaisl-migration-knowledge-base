Step-by-step guides for people in Bangladesh who want to work abroad, one doc per destination country. Every sentence is cited.

Countries:

- [Saudi Arabia](countries/saudi-arabia/) (draft, under review)
- [Malaysia](countries/malaysia/) (draft, under review)
- [Qatar](countries/qatar/) (draft, under review)
- [United Arab Emirates](countries/united-arab-emirates/) (draft, under review)
- [Maldives](countries/maldives/) (draft, under review)
- [Kuwait](countries/kuwait/) (draft, under review)
- [Italy](countries/italy/) (draft, under review)
- [Kyrgyzstan](countries/kyrgyzstan/) (draft, under review)
- [Cambodia](countries/cambodia/) (draft, under review)
- [Singapore](countries/singapore/) (draft, under review)
- [Oman](countries/oman/) (draft, under review)
- [Jordan](countries/jordan/) (draft, under review)
- [South Korea](countries/south-korea/) (draft, under review)
- [Japan](countries/japan/) (draft, under review)
- [Brunei](countries/brunei/) (draft, under review)
- [United States](countries/united-states/) (first version: Prothom Alo reporting plus an official-source pass, 24 Nov 2026)
- [Canada](countries/canada/) (first version: Prothom Alo reporting plus an official-source pass, 24 Nov 2026)
- [United Kingdom](countries/united-kingdom/) (first version: Prothom Alo reporting plus an official-source pass, 24 Nov 2026)
- [India](countries/india/) (first version: Prothom Alo reporting plus an official-source pass, 24 Nov 2026)
- [Lebanon](countries/lebanon/) (first version: Prothom Alo reporting plus an official-source pass, 24 Nov 2026)
- [Greece](countries/greece/) (first version: Prothom Alo reporting plus an official-source pass, 24 Nov 2026)

For all countries:

- [Recruiting agencies](agencies/): the most active licensed agencies, by country, with cited red flags
- [Frequently asked questions](global/faq/): the questions people ask most before, during and after working abroad
- [Dalal scams](global/dalal-scams/): the tricks brokers and fake agencies use, how to spot each, and where to complain
- [Departure bottlenecks](global/departure/): passports, police clearance, the Gulf medical, BMET clearance, offloading and bribes at the airport, refused entry and deportation
- [Illegal routes](global/illegal-routes/): the irregular routes people are sold, how they end, and the law and help in Bangladesh
- [Sending money home](global/money/): ways to send and what each costs, the incentive, exchange rates, hundi, the Wage Earners' Development Bond and the Probashi Card
- [Services for migrants and their families](global/services/): training, loans, the Welfare Board, help in a war or disaster, deaths abroad, reintegration
- [Other destinations](global/other-destinations/): 24 countries with no doc of their own yet, from Prothom Alo reporting

Each country and global folder has the same files:

- README.md and the .docx: the doc. GitHub shows README.md when you open the folder.
- doc.md: the doc's text with citations. The only file edited by hand; README.md and the .docx are built from it.
- facts.csv: every fact in the doc, with the exact quote that proves it and the source it comes from.
- sources.csv and sources: every source used. The sources folder keeps a saved copy of each page or PDF, so the evidence survives if a link breaks.
- questions.md: every open question in the doc (its "Need to know" blocks), grouped by section, for insiders and officials to answer.
- notes.md: research notes, conflicts between sources, known minor issues and pages we couldn't download.

Elsewhere:

- tools: scripts that save sources, check each quote against its saved copy, and build the doc (numbered headings, linked references and a .pdf if LibreOffice is installed)
- official-pdfs and data: Bangladesh-side documents and BMET's recruiting-agency list
- datasets: raw collections behind the docs, such as the Prothom Alo migration archive, with the scripts that built them
- LOG.md: what has been done, by whom, how it was checked, what was tried and dropped, and what is open
- CLAUDE.md: the rules every doc follows
- plans.md: bigger pieces of work we're thinking through before starting

## Start a new country

Paste this into Claude Code from inside the repo folder, with <COUNTRY> replaced by the country you're researching.

```
I'm working on the Migration Pathway Navigator knowledge base for BSAISL. CLAUDE.md in this repo explains the project, the settled doc format, the quality rules and the research process. They are binding.

My country is <COUNTRY>.

1. Read CLAUDE.md. Then read the two draft docs, countries/saudi-arabia/README.md and countries/malaysia/README.md, to see the format; they are drafts, not finished standards, so follow the rules in CLAUDE.md where they differ. Skim the PDFs in official-pdfs/ for the Bangladesh-side steps that apply to every country.
2. Before researching, list every visa type open to Bangladeshis for <COUNTRY>, most-used first, and the sections the doc will have. Show me that outline and wait for my OK.
3. Research following the process in CLAUDE.md: topic by topic, official sources first, then the practical pass in Bangla news, NGO reports and agency guides. Read official PDFs in full. If a site blocks you, try Firecrawl; if that fails, give me the exact link to download. Save every source and log every fact with the tools in tools/, and keep notes in countries/<country>/notes.md.
4. Write countries/<country>/doc.md, citing fact ids from facts.csv, then build README.md and the .docx with tools/build.py. Commit as you go.
5. Before handing it over, do the line-by-line pass and both audits in CLAUDE.md (the migrant's questions, and the original aim per visa). Then tell me plainly which files you made, how many citations are official versus news, and every "Need to know" still open.

Ask me whenever something is unclear. Don't skip a source because it's hard to get.
```
