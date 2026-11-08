import re
D="C:/Users/User/Desktop/Github/bsaisl-migration-knowledge-base/countries/maldives/"
names={"N":"Corridor, chain and money in practice","W":"Work visa (Maldives side) and professionals","B":"Bangladesh-side steps and the High Commission","L":"Rights at work and problems","U":"Irregular status, regularisation and deportation","V":"Visits and short visas","F":"Family, residence, asylum, domestic work","G":"Money, remittances and customs","R":"Gap research after the audit (flights, pension, fire, appeal, SIM, MQA, costs)","Z":"Lead additions and pages received from the team"}
out=["# Maldives: research notes","","Merged from the per-topic research files in `drafts/` (8 November 2026). Fact ids like [W0012] are rows in facts.csv. Each topic was researched by one agent with its own fact prefix.",""]
blocked=["## Pages we could not download","","Exact URL, suggested file name and what each would prove. Save in a browser and send to the lead; they will be added to `sources/` and logged with `fetch.py --log <url> <name> manual`.",""]
for X,t in names.items():
    try: s=open(D+f"drafts/{X}-findings.md",encoding="utf-8").read()
    except FileNotFoundError: continue
    b=re.search(r"\n## b\..*?\n(.*?)\n## c\.",s,re.S)
    c=re.search(r"\n## c\..*?\n(.*?)(?:\n## d\.|\Z)",s,re.S)
    out+= [f"## {t} (prefix {X})",""]+[re.sub(r"^#+ ","**",l)+("**" if l.startswith("#") else "") for l in b.group(1).strip().splitlines()]+[""]
    blocked+=[f"### {t} ({X})",""]+c.group(1).strip().splitlines()+[""]
open(D+"notes.md","w",encoding="utf-8").write("\n".join(out+blocked)+"\n")
print("ok")
