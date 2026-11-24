import subprocess, sys
T="../../../../tools/facts.py"
C="assindatcolf-ccnl-lavoro-domestico-2025-2028"; E="news-edotto-flussi-2027-click-day"; A24="normattiva-tui-art24-lavoro-stagionale"; A18="normattiva-tui-art18ter-sfruttamento-lavoro"
F=[
(C,"2025-10-28","lead","Non-live-in domestic workers work at most 8 non-consecutive hours a day, 40 a week","8 ore giornaliere, non consecutive, per un totale di 40 ore settimanali"),
(C,"2025-10-28","lead","Overtime on public holidays or Sunday is paid at +60%","del 60% in una delle festività indicate nell'art. 16 o nella giornata di domenica"),
(C,"2025-10-28","lead","Employer's notice for jobs of 25 hours a week or more is 15 calendar days up to five years' service","no a 5 anni di anzianità presso lo stesso datore di lavoro: 15 giorni di calendario"),
(C,"2025-10-28","lead","After five years' service the notice is 30 calendar days","oltre i 5 anni di anzianità presso lo stesso datore di lavoro: 30 giorni di calendario"),
(C,"2025-10-28","lead","When sick after probation with up to 6 months' service, the job is kept for 10 calendar days","superato il periodo di prova, 10 giorni di calendario"),
(C,"2025-10-28","lead","With over 2 years' service the job is kept for 180 calendar days of sickness","per anzianità oltre i 2 anni, 180 giorni di calendario"),
(E,"2026-10-02","unofficial","The 2027 click day for seasonal tourism is 9 February 2027 at 9:00","9 febbraio 2027, ore 9:00"),
(E,"2026-10-02","unofficial","The 2027 click day for domestic work (form A-bis) is 18 February 2027","il 18 febbraio 2027 sarà dedicato agli ingressi per lavoro subordinato non stagionale nel settore dell’assistenza familiare"),
(A24,"2025-12-02","verified","The employer or its trade association files a named request for a seasonal worker with the SUI of the province of residence","devono presentare richiesta nominativa allo sportello unico per l'immigrazione della provincia di residenza"),
(A18,"2025-12-02","verified","The Article 18-ter permit is marked 'casi speciali'","reca la dicitura «casi speciali»"),
(A18,"2025-12-02","verified","The Article 18-ter permit allows employed and self-employed work","o lo svolgimento di lavoro subordinato e autonomo"),
("news-lapresse-flussi-30-arresti-2026-06","2026-06-30","unofficial","Carabinieri executed custody orders against 30 people in nine provinces including Latina and Ragusa","nei confronti di 30 persone, nelle province di Taranto, Lecce, Foggia, Matera, Campobasso, Milano, Verona, Ragusa e Latina"),
("news-lapresse-flussi-30-arresti-2026-06","2026-06-30","unofficial","The false applications were handled by a CAF (tax assistance centre) in Taranto with intermediaries and compliant employers","Le pratiche sarebbero state gestite da un Caf di Taranto con il coinvolgimento di intermediari e imprenditori compiacenti"),
("news-bdnews24-grosseto-flussi-fraud-2025-09","2025-09-28","unofficial","The money was collected in both Bangladesh and Italy; some families mortgaged land to pay","In some cases, families were forced to mortgage land to pay the required amounts"),
]
for n,d,st,c,q in F:
    r=subprocess.run([sys.executable,T,"add","--prefix","D","--name",n,"--claim",c,"--quote",q,"--page-date",d,"--status",st],capture_output=True,text=True)
    print(r.returncode,(r.stdout+r.stderr).strip()[-90:])
