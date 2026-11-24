import subprocess, sys, json, csv
T="../../../../tools/facts.py"
def run(args):
    r=subprocess.run([sys.executable,T]+args,capture_output=True,text=True,encoding="utf-8")
    out=(r.stdout+r.stderr).strip(); print(out[-300:]); return out
def add(name,claim,quote,date,status,note=None,nq=False,v=None):
    a=["add","--prefix","B","--name",name,"--claim",claim,"--quote",quote,"--page-date",date,"--status",status]
    if v: a+=["--visa",v[0],"--field",v[1],"--value",v[2]]
    if nq: a+=["--no-quote-check"]
    if note: a+=["--note",note]
    return run(a)
spec=json.load(open(sys.argv[1],encoding="utf-8"))
for s in spec.get("sources",[]):
    run(["source","--name",s[0],"--publisher",s[1],"--title",s[2],"--official",s[3],"--page-date",s[4]])
for p in spec.get("port",[]):
    path,ids=p["file"],p["ids"]
    rows={r["id"]:r for r in csv.DictReader(open(path,encoding="utf-8"))}
    for i in ids:
        r=rows[i]; name=r["saved_file"].split(";")[0].rsplit(".",1)[0]
        note=(r["note"]+"; " if r["note"] else "")+f"ported from {path.split('countries/')[-1]} {i}"
        nq="garbled" in r["note"] or r["quote"].startswith("garbled")
        q=r["quote"]
        print(i,"->",end=" "); add(name,r["claim"],q,r["page_date"] or "undated",r["status"],note,nq)
for f in spec.get("facts",[]):
    add(f["n"],f["c"],f["q"],f["d"],f["s"],f.get("note"),f.get("nq",False),f.get("v"))
