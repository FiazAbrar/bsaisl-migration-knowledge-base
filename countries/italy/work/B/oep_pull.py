import json, subprocess, sys, urllib.parse, calendar, os
BASE="https://www.oep.gov.bd/reports/country-clearance"
def q(frm,to,gender=""):
    url=f"{BASE}?draw=1&start=0&length=10&approval_date_from={frm}&approval_date_to={to}&country_id%5B%5D=85&gender_id={gender}"
    out=subprocess.run(["curl","-s","-m","60","-H","X-Requested-With: XMLHttpRequest","-H","Accept: application/json",url],capture_output=True,text=True).stdout
    d=json.loads(out); rows=d["payload"]["data"]
    tot=rows[0]["total_employee"] if rows else 0
    return url,tot,out
TODAY="2026-11-09"
def save(name,lines):
    with open(f"sources/{name}.txt","w",encoding="utf-8") as f: f.write("\n".join(lines)+"\n")
    print(name); print("\n".join(lines[:3]))
logs=[]
for y in [2022,2023,2024,2025,2026]:
    to=f"{y}-12-31" if y<2026 else TODAY
    for g,gl in [("","" ),("2","-women")]:
        url,tot,raw=q(f"{y}-01-01",to,g)
        name=f"oep-clearance-it-{y}{gl}"
        who="women" if g else "all workers"
        save(name,[f"# OEP country-clearance report, Italy (country_id 85), {who}, {y}-01-01 to {to}, queried 2026-11-10",
                   f"Italy {who} {y}: total_employee {tot}", url, raw])
        logs.append((url,name))
for y in [2023,2024,2025,2026]:
    lines=[f"# OEP country-clearance report, Italy (country_id 85), {y} by month, queried 2026-11-10"]
    for m in range(1,13):
        if y==2026 and m>11: break
        last=calendar.monthrange(y,m)[1]
        frm=f"{y}-{m:02d}-01"; to=f"{y}-{m:02d}-{last:02d}"
        if y==2026 and m==11: to=TODAY
        url,tot,raw=q(frm,to)
        lines.append(f"{frm} to {to}: Italy total_employee {tot} ({url})")
    name=f"oep-clearance-it-{y}-monthly"
    save(name,lines); logs.append((f"{BASE}#italy-{y}-monthly",name))
json.dump(logs,open("oep_logs.json","w"))
