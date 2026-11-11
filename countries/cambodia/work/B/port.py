import csv, shutil, subprocess, os
KG="../../../kyrgyzstan/work/B"
names="""oep-employee-registration-form-fc demo-sylhet-bmet-registration-notice bmet-demo-list bmet-ttc-list oep-pdo-certificate-fc bmet-pdo-page wewb-portal-bmet-wewbm-check-fc wewb-call-centre dip-epassport-fees-fc dip-epassport-instructions-fc dip-circular-police-verification-2025-02 dip-natore-passport-helpline pcc-police-home-fc mofabd-citizen-charter mofabd-eapostille-chain-of-legalization mofa-bd-apostille-recognized-countries probashi-warning-notice-2025-02-05 probashi-office-address bmet-contacts wewb-ambulance wewb-airport-desk wewb-wage-earners-centre wewb-probashi-lounge wewb-legal-aid bmet-citizen-charter-2026 bmet-safe-migration-leaflet-2025-12 ministry-citizen-charter-2026 wewb-citizen-charter ministry-welfare-fee-circular-2026-09 pkb-migration-loan-page pkb-women-migration-loan mygov-pkb-migration-loan pkb-rehabilitation-loan wewb-body-repatriation wewb-body-transport-burial wewb-3lakh-grant wewb-membership wewb-insurance-help probashi-migration-cost-16-countries-2017 boesl-home bmet-agency-complaint-form-pdf wewb-compensation-recovery wewb-labour-wing-help wewb-safe-house ttcf-feni-pdo-fee-news oep-agencies-list news-prothomalo-en-ministry-approval-12-countries news-banglatribune-ministry-approval-12-countries probashi-special-notice-expatriates-2026-09-22 bmet-misc-infos-p1-of7""".split()
src={r["name"]:r for r in csv.DictReader(open(f"{KG}/sources.csv",encoding="utf-8"))}
log={r["name"]:r for r in csv.DictReader(open(f"{KG}/sources/_fetchlog.csv",encoding="utf-8"))}
for n in names:
    if n not in src: print("NO SRC",n); continue
    files=[f for f in os.listdir(f"{KG}/sources") if f.startswith(n+".")]
    for f in files: shutil.copy(f"{KG}/sources/{f}","sources/"+f)
    s=src[n]
    r=subprocess.run(["python","../../../../tools/fetch.py","--log",s["url"],n,"manual"],capture_output=True,text=True); print(n,r.stdout.strip()[-120:],r.stderr.strip()[-200:])
    r=subprocess.run(["python","../../../../tools/facts.py","source","--name",n,"--publisher",s["publisher"],"--title",s["title"],"--official",s["official"],"--page-date",s["page_date"] or "undated"],capture_output=True,text=True); print(r.stdout.strip()[-120:],r.stderr.strip()[-200:])
