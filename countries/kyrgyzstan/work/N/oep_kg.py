import json, subprocess, calendar
BASE="https://www.oep.gov.bd/reports/country-clearance"
TODAY="2026-11-09"
def get(url):
    out=subprocess.run(["curl","-s","-m","90","-H","X-Requested-With: XMLHttpRequest","-H","Accept: application/json",url],capture_output=True,text=True).stdout
    return out,json.loads(out)
def q(frm,to,g="",allsk=False,length=10):
    url=f"{BASE}?draw=1&start=0&length={length}&approval_date_from={frm}&approval_date_to={to}&country_id%5B%5D=94&gender_id={g}"+("&all_skills=1" if allsk else "")
    out,d=get(url); return url,out,d
def log(url,name,title):
    subprocess.run(["python","../../../../tools/fetch.py","--log",url,name,"manual"])
    subprocess.run(["python","../../../../tools/facts.py","source","--name",name,"--publisher","BMET (OEP)","--title",title,"--official","yes","--page-date","2026-11-10"])
def save(name,lines):
    open(f"sources/{name}.txt","w",encoding="utf-8").write("\n".join(lines)+"\n"); print("\n".join(lines[:16]))
# yearly totals and women
lines=["# OEP country-clearance report, Kyrgyzstan (country_id 94), yearly totals, all workers and women, queried 2026-11-10"]
raws=[]
for y in [2022,2023,2024,2025,2026]:
    to=f"{y}-12-31" if y<2026 else TODAY
    for g,gl in [("","all workers"),("1","men"),("2","women")]:
        url,out,d=q(f"{y}-01-01",to,g); rows=d["payload"]["data"]; tot=rows[0]["total_employee"] if rows else 0
        lines.append(f"Kyrgyzstan {gl} {y}-01-01 to {to}: total_employee {tot} ({url})"); raws.append(out)
save("oep-clearance-kg-yearly-by-sex",lines+raws)
log(f"{BASE}#kyrgyzstan-yearly-by-sex","oep-clearance-kg-yearly-by-sex","Country-wise clearance report: Kyrgyzstan, yearly 2022-2026, all, men and women")
# monthly
lines=["# OEP country-clearance report, Kyrgyzstan (country_id 94), by month 2023 to 2026, queried 2026-11-10"]
for y in [2023,2024,2025,2026]:
    for m in range(1,13):
        if y==2026 and m>11: break
        last=calendar.monthrange(y,m)[1]; frm=f"{y}-{m:02d}-01"; to=f"{y}-{m:02d}-{last:02d}"
        if y==2026 and m==11: to=TODAY
        url,out,d=q(frm,to); rows=d["payload"]["data"]; tot=rows[0]["total_employee"] if rows else 0
        lines.append(f"{frm} to {to}: Kyrgyzstan total_employee {tot} ({url})")
save("oep-clearance-kg-monthly-2023-2026",lines)
log(f"{BASE}#kyrgyzstan-monthly-2023-2026","oep-clearance-kg-monthly-2023-2026","Country-wise clearance report: Kyrgyzstan by month, 2023-2026")
# by job
for y,to in [(2023,"2023-12-31"),(2024,"2024-12-31"),(2025,"2025-12-31"),(2026,TODAY)]:
    url,out,d=q(f"{y}-01-01",to,allsk=True,length=300); rows=d["payload"]["data"]
    tot=sum(r["total_employee"] for r in rows)
    rows=sorted(rows,key=lambda r:-r["total_employee"])
    lines=[f"# OEP country-clearance report, Kyrgyzstan (country_id 94), by job category, {y}-01-01 to {to}, queried 2026-11-10",
           f"Sum of categories: {tot}; categories listed: {len(rows)}"]
    for r in rows: lines.append(f"Kyrgyzstan | {r.get('category_name')} | {r['total_employee']}")
    save(f"oep-clearance-kg-{y}-by-job",lines+[url,out])
    log(url,f"oep-clearance-kg-{y}-by-job",f"Country-wise clearance report by job category: Kyrgyzstan, {y}")
