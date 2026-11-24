import subprocess,os
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/..')
F=['python','../../../../tools/facts.py']
print(subprocess.run(F+['source','--name','bancaditalia-albi-elenchi','--publisher',"Banca d'Italia",'--title','Albi ed elenchi di vigilanza','--official','yes','--page-date','undated'],capture_output=True,text=True,encoding='utf-8').stdout)
for c,q in [("Banca d'Italia publishes its supervisory registers (banks, payment institutions and other intermediaries, with their branches) for public search at infostat.bancaditalia.it/GIAVAInquiry-public/ng/","[Albi ed elenchi di vigilanza](https://infostat.bancaditalia.it/GIAVAInquiry-public/ng/)"),
            ("Carrying on banking or financial activity without the required authorisation or registration is a criminal offence in Italy","in mancanza delle autorizzazioni/iscrizioni ai pertinenti albi previste dalla legge è sanzionato penalmente")]:
    r=subprocess.run(F+['add','--prefix','G','--name','bancaditalia-albi-elenchi','--claim',c,'--quote',q,'--page-date','undated','--status','possibly-outdated'],capture_output=True,text=True,encoding='utf-8');print(r.stdout,r.stderr)
