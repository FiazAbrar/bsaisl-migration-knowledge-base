import json, subprocess
BASE="https://www.oep.gov.bd/reports/country-clearance"
for y,to in [(2023,"2023-12-31"),(2025,"2025-12-31"),(2026,"2026-11-09")]:
    url=f"{BASE}?draw=1&start=0&length=200&approval_date_from={y}-01-01&approval_date_to={to}&country_id%5B%5D=85&gender_id=&all_skills=1"
    out=subprocess.run(["curl","-s","-m","90","-H","X-Requested-With: XMLHttpRequest","-H","Accept: application/json",url],capture_output=True,text=True).stdout
    d=json.loads(out); rows=d["payload"]["data"]
    tot=sum(r["total_employee"] for r in rows)
    lines=[f"# OEP country-clearance report, Italy (country_id 85), by job category, {y}-01-01 to {to}, queried 2026-11-10",
           f"Sum of categories: {tot}; categories listed: {len(rows)}; recordsTotal {d['payload'].get('recordsTotal')}"]
    for r in rows: lines.append(f"Italy | {r['category_name']} | {r['total_employee']}")
    lines += [url, out]
    name=f"oep-clearance-it-{y}-by-job"
    open(f"sources/{name}.txt","w",encoding="utf-8").write("\n".join(lines)+"\n")
    print("\n".join(lines[:14]))
    subprocess.run(["python","../../../../tools/fetch.py","--log",url,name,"manual"])
    subprocess.run(["python","../../../../tools/facts.py","source","--name",name,"--publisher","BMET (OEP)","--title",f"Country-wise clearance report by job category: Italy, {y}","--official","yes","--page-date","2026-11-10"])
