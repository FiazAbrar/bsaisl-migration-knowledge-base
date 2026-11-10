import csv, shutil, subprocess, os, json, sys
KW="../../../kuwait"
names="""oep-employee-registration-form-fc demo-sylhet-bmet-registration-notice bmet-demo-list bmet-ttc-list oep-pdo-certificate-fc bmet-pdo-page wewb-portal-bmet-wewbm-check-fc wewb-call-centre dip-epassport-fees-fc dip-epassport-instructions-fc dip-circular-police-verification-2025-02 dip-natore-passport-helpline pcc-police-home-fc mofabd-citizen-charter mofabd-eapostille-chain-of-legalization mofa-bd-apostille-recognized-countries mofa-bd-chain-of-legalization probashi-warning-notice-2025-02-05 probashi-office-address bmet-contacts wewb-ambulance wewb-airport-desk wewb-wage-earners-centre wewb-probashi-lounge wewb-legal-aid bmet-citizen-charter-2026 bmet-safe-migration-leaflet-2025-12 ministry-citizen-charter-2026 wewb-citizen-charter ministry-welfare-fee-circular-2026-09 pkb-migration-loan-page pkb-women-migration-loan mygov-pkb-migration-loan pkb-rehabilitation-loan wewb-body-repatriation wewb-body-transport-burial wewb-3lakh-grant wewb-membership wewb-insurance-help bmet-misc-infos-p1-of7 probashi-migration-cost-16-countries-2017 boesl-home bmet-agency-complaint-form-pdf wewb-compensation-recovery wewb-labour-wing-help wewb-safe-house probashi-special-notice-expatriates-2026-09-22""".split()
src={r["name"]:r for r in csv.DictReader(open(f"{KW}/sources.csv",encoding="utf-8"))}
log={r["name"]:r for r in csv.DictReader(open(f"{KW}/sources/_fetchlog.csv",encoding="utf-8"))}
for n in names:
    if n not in src: print("NO SRC",n); continue
    files=[f for f in os.listdir(f"{KW}/sources") if f.startswith(n+".")]
    for f in files: shutil.copy(f"{KW}/sources/{f}","sources/"+f)
    s=src[n]
    r=subprocess.run(["python","../../../../tools/fetch.py","--log",s["url"],n,"manual"],capture_output=True,text=True); print(n,r.stdout.strip(),r.stderr.strip()[-200:])
    r=subprocess.run(["python","../../../../tools/facts.py","source","--name",n,"--publisher",s["publisher"],"--title",s["title"],"--official",s["official"],"--page-date",s["page_date"] or "undated"],capture_output=True,text=True); print(r.stdout.strip(),r.stderr.strip()[-200:])
logs=json.load(open("oep_logs.json"))
for url,n in logs:
    r=subprocess.run(["python","../../../../tools/fetch.py","--log",url,n,"manual"],capture_output=True,text=True); print(n,r.stdout.strip(),r.stderr.strip()[-200:])
    title="Country-wise clearance report: Italy, "+n.replace("oep-clearance-it-","").replace("-"," ")
    r=subprocess.run(["python","../../../../tools/facts.py","source","--name",n,"--publisher","BMET (OEP)","--title",title,"--official","yes","--page-date","2026-11-10"],capture_output=True,text=True); print(r.stdout.strip(),r.stderr.strip()[-200:])
