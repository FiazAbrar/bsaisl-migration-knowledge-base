import json, subprocess, calendar
BASE="https://www.oep.gov.bd/reports/country-clearance"
CID=30; TODAY="2026-11-10"; Q="2026-11-11"
def get(url):
    out=subprocess.run(["curl","-s","-m","90","-H","X-Requested-With: XMLHttpRequest","-H","Accept: application/json",url],capture_output=True,text=True).stdout
    return out,json.loads(out)
def q(frm,to,gender="",skills=False):
    url=f"{BASE}?draw=1&start=0&length={200 if skills else 10}&approval_date_from={frm}&approval_date_to={to}&country_id%5B%5D={CID}&gender_id={gender}"+("&all_skills=1" if skills else "")
    out,d=get(url); rows=d["payload"]["data"]
    return url,rows,out
def save(name,lines):
    open(f"sources/{name}.txt","w",encoding="utf-8").write("\n".join(lines)+"\n"); print("\n".join(lines[:2]))
logs=[]
for y in [2022,2023,2024,2025,2026]:
    to=f"{y}-12-31" if y<2026 else TODAY
    for g,gl in [("",""),("2","-women")]:
        url,rows,raw=q(f"{y}-01-01",to,g); tot=rows[0]["total_employee"] if rows else 0
        who="women" if g else "all workers"; name=f"oep-clearance-kh-{y}{gl}"
        save(name,[f"# OEP country-clearance report, Cambodia (country_id 30), {who}, {y}-01-01 to {to}, queried {Q}",f"Cambodia {who} {y}: total_employee {tot}",url,raw])
        logs.append((url,name,f"Country-wise clearance report: Cambodia, {who}, {y}"))
for y in [2023,2024,2025,2026]:
    lines=[f"# OEP country-clearance report, Cambodia (country_id 30), {y} by month, queried {Q}"]
    for m in range(1,13):
        if y==2026 and m>11: break
        last=calendar.monthrange(y,m)[1]; frm=f"{y}-{m:02d}-01"; to=f"{y}-{m:02d}-{last:02d}"
        if y==2026 and m==11: to=TODAY
        url,rows,raw=q(frm,to); tot=rows[0]["total_employee"] if rows else 0
        lines.append(f"{frm} to {to}: Cambodia total_employee {tot} ({url})")
    name=f"oep-clearance-kh-{y}-monthly"; save(name,lines); logs.append((f"{BASE}#cambodia-{y}-monthly",name,f"Country-wise clearance report: Cambodia, {y} by month"))
for y in [2023,2024,2025,2026]:
    to=f"{y}-12-31" if y<2026 else TODAY
    url,rows,raw=q(f"{y}-01-01",to,skills=True); tot=sum(r["total_employee"] for r in rows)
    rows=sorted(rows,key=lambda r:-r["total_employee"])
    lines=[f"# OEP country-clearance report, Cambodia (country_id 30), by job category, {y}-01-01 to {to}, queried {Q}",f"Sum of categories: {tot}; categories listed: {len(rows)}"]
    lines+= [f"Cambodia | {r['category_name']} | {r['total_employee']}" for r in rows]+[url,raw]
    name=f"oep-clearance-kh-{y}-by-job"; save(name,lines); logs.append((url,name,f"Country-wise clearance report by job category: Cambodia, {y}"))
json.dump(logs,open("oep_logs.json","w"))
