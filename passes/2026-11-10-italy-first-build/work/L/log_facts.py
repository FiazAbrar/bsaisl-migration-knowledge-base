import subprocess, sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
T = "../../../../tools/facts.py"
NV = "2026-11-10"  # Normattiva consolidated text "vigente al 10/11/2026"
SOURCES = [
 ("inps-pensione-stranieri-rimpatriati","INPS","Trattamenti pensionistici ai lavoratori stranieri rimpatriati","yes","2026-06-12"),
 ("poliziadistato-ricevuta-rinnovo-10929","Polizia di Stato","Stranieri: per uscire dall'Italia basta la ricevuta postale","yes","2008-07-31"),
 ("poliziadistato-ricevuta-rinnovo-378","Polizia di Stato","Immigrati: per uscire dall'Italia basta la ricevuta postale","yes","2007-08-08"),
 ("normattiva-tui-art2","Normattiva (Gazzetta Ufficiale)","D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 2","yes",NV),
 ("normattiva-tui-art4","Normattiva (Gazzetta Ufficiale)","D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 4","yes",NV),
 ("normattiva-tui-art5","Normattiva (Gazzetta Ufficiale)","D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 5","yes",NV),
 ("normattiva-tui-art6","Normattiva (Gazzetta Ufficiale)","D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 6","yes",NV),
 ("normattiva-tui-art10bis","Normattiva (Gazzetta Ufficiale)","D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 10-bis","yes",NV),
 ("normattiva-tui-art13","Normattiva (Gazzetta Ufficiale)","D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 13","yes",NV),
 ("normattiva-tui-art14","Normattiva (Gazzetta Ufficiale)","D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 14","yes",NV),
 ("normattiva-tui-art16","Normattiva (Gazzetta Ufficiale)","D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 16","yes",NV),
 ("normattiva-tui-art22","Normattiva (Gazzetta Ufficiale)","D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 22","yes",NV),
 ("normattiva-dpr309-1990-art73","Normattiva (Gazzetta Ufficiale)","D.P.R. 309/1990 (Testo Unico stupefacenti), art. 73","yes",NV),
 ("normattiva-dpr309-1990-art75","Normattiva (Gazzetta Ufficiale)","D.P.R. 309/1990 (Testo Unico stupefacenti), art. 75","yes",NV),
 ("normattiva-codice-civile-art2120-tfr","Normattiva (Gazzetta Ufficiale)","Codice civile, art. 2120 (trattamento di fine rapporto)","yes",NV),
 ("inps-naspi-scheda","INPS","NASpI: indennita mensile di disoccupazione","yes","2026-02-02"),
 ("inl-modulo-31-inglese-2025","Ispettorato Nazionale del Lavoro","Modulo INL 31: Richiesta di intervento ispettivo / Request for inspection (English)","yes","undated"),
 ("inl-modulo-31-bengalese-2025","Ispettorato Nazionale del Lavoro","Modulo INL 31: Richiesta di intervento ispettivo (Bangla)","yes","undated"),
 ("normattiva-dlgs124-2004-art11-conciliazione","Normattiva (Gazzetta Ufficiale)","D.Lgs. 124/2004, art. 11 (conciliazione monocratica)","yes",NV),
 ("normattiva-dlgs124-2004-art12-diffida","Normattiva (Gazzetta Ufficiale)","D.Lgs. 124/2004, art. 12 (diffida accertativa)","yes",NV),
 ("normattiva-l604-1966-art6-impugnazione","Normattiva (Gazzetta Ufficiale)","Legge 604/1966, art. 6 (impugnazione del licenziamento)","yes",NV),
 ("normattiva-dlgs151-2015-art26-dimissioni","Normattiva (Gazzetta Ufficiale)","D.Lgs. 151/2015, art. 26 (dimissioni telematiche)","yes",NV),
 ("normattiva-dlgs66-2003-art3-orario-normale","Normattiva (Gazzetta Ufficiale)","D.Lgs. 66/2003, art. 3 (orario normale)","yes",NV),
 ("normattiva-dlgs66-2003-art4-orario","Normattiva (Gazzetta Ufficiale)","D.Lgs. 66/2003, art. 4 (durata massima)","yes",NV),
 ("normattiva-dlgs66-2003-art5-straordinario","Normattiva (Gazzetta Ufficiale)","D.Lgs. 66/2003, art. 5 (lavoro straordinario)","yes",NV),
 ("normattiva-dlgs66-2003-art7-riposo","Normattiva (Gazzetta Ufficiale)","D.Lgs. 66/2003, art. 7 (riposo giornaliero)","yes",NV),
 ("normattiva-dlgs66-2003-art9-settimanale","Normattiva (Gazzetta Ufficiale)","D.Lgs. 66/2003, art. 9 (riposo settimanale)","yes",NV),
 ("normattiva-dlgs66-2003-art10-ferie","Normattiva (Gazzetta Ufficiale)","D.Lgs. 66/2003, art. 10 (ferie annuali)","yes",NV),
 ("normattiva-dpr1124-1965-art52-inail","Normattiva (Gazzetta Ufficiale)","D.P.R. 1124/1965 (assicurazione infortuni INAIL), art. 52","yes",NV),
 ("normattiva-dpr1124-1965-art68-inail","Normattiva (Gazzetta Ufficiale)","D.P.R. 1124/1965 (assicurazione infortuni INAIL), art. 68","yes",NV),
 ("inps-malattia-visite-controllo","INPS","Indennita di malattia e visite mediche di controllo","yes","2026-09-21"),
 ("esteri-ambdhaka-reentry-2026-07","Embassy of Italy in Dhaka","Check-list for RE-ENTRY visa","yes","undated"),
 ("ance-ragusa-tabella-retribuzioni-edili-2026-03","ANCE Ragusa (builders' association, CCNL signatory)","Tabella delle retribuzioni edili, provincia di Ragusa, dal 1 marzo 2026","no","2026-03-01"),
 ("news-fiscoetasse-ccnl-operai-agricoli-2026","FISCOeTASSE","CCNL Operai Agricoli 2026: rinnovo e tabella nuovi minimi","no","2026-06-08"),
 ("news-leggeinchiaro-edilizia-tabelle-2026","Legge in Chiaro","CCNL Edilizia Industria 2026: tabelle retributive","no","2026-10-26"),
 ("news-leggeinchiaro-turismo-alberghi-tabelle-2026","Legge in Chiaro","CCNL Turismo Pubblici Esercizi 2026: tabelle retributive e minimi","no","2026-10-12"),
 ("news-leggeinchiaro-multiservizi-tabelle-2026","Legge in Chiaro","CCNL Pulizie Multiservizi 2026: tabelle retributive","no","2026-10-26"),
 ("news-ilpost-fincantieri-paga-globale-2023-03","Il Post","Il processo a Venezia per lo sfruttamento degli operai che costruiscono navi da crociera","no","2023-03-31"),
]
meta = {s[0]: s for s in SOURCES}

def st(name):
    s = meta[name]
    if s[3] == "no":
        return "unofficial"
    if s[4] == "undated" or s[4] < "2025-11-10":
        return "possibly-outdated"
    return "verified"

F = []
def f(name, claim, quote, note=""):
    F.append((name, claim, quote, note))

# pension
P = "inps-pensione-stranieri-rimpatriati"
f(P, "A non-seasonal foreign worker who returns home for good keeps the pension and social security rights earned in Italy, even without an agreement with the home country", "mantenere i diritti previdenziali e di sicurezza sociale maturati in Italia")
f(P, "The returned-worker pension rule applies to workers with a non-seasonal contract who return home permanently", "con contratto non stagionale, in caso di")
f(P, "Workers hired after 1 January 1996 who return home can get the contributory old-age pension at pensionable age even without 20 years of contributions", "anche se non hanno maturato 20 anni di contributi")
f(P, "Pensionable age is given as 67 for 2023-2024, with possible life-expectancy adjustments", "67 anni per il 2023-2024) con possibili adeguamenti basati sulla speranza di vita")
f(P, "Workers hired before 1996 who return home need 20 years of contributions for the old-age pension", "con 20 anni di contributi")
f(P, "A returned worker with online credentials applies online, attaching documents authenticated by the Italian consulate, then posts them to INPS Perugia, via Canali 5, 06122 Perugia", "Direzione provinciale INPS di Perugia, in via Canali, 5 - 06122 Perugia")
f(P, "Without online credentials, the returned worker applies at the Italian consulate where he lives", "presentare domanda al Consolato italiano dove risiede, se non in possesso di credenziali")
f(P, "Both application routes are for nationals of countries with no social security convention with Italy", "Paesi con i quali non esiste una convenzione in materia di Sicurezza sociale sottoscritta dall'Italia")
f(P, "The application can also be made through a patronato", "rivolgendosi a un patronato")
f(P, "If the worker dies after pensionable age, survivors get a survivors' pension under the general conditions", "spetta la pensione ai superstiti")
T22 = "normattiva-tui-art22"
f(T22, "TUI art. 22(13): on repatriation a non-EU worker (except seasonal) keeps social security rights regardless of a reciprocity agreement", "in caso di rimpatrio il lavoratore extracomunitario conserva i diritti previdenziali e di sicurezza sociale maturati")
f(T22, "TUI art. 22(14): patronati serve non-EU workers working legally in Italy", "sono estese ai lavoratori extracomunitari che prestino regolare attività di lavoro in Italia")
f(T22, "TUI art. 22(11): losing the job, even by resigning, does not revoke the permit; the worker can register as available and stay at least one year (not seasonal), or as long as unemployment benefit lasts if longer", "per un periodo non inferiore ad un anno ovvero per tutto il periodo di durata della prestazione di sostegno al reddito percepita dal lavoratore straniero, qualora superiore")
f(T22, "TUI art. 22(11): loss of job does not revoke the permit of the worker and family", "La perdita del posto di lavoro non costituisce motivo di revoca del permesso di soggiorno")
f(T22, "TUI art. 22(11): the job-loss rule applies even when the worker resigned", "che perde il posto di lavoro, anche per dimissioni")
f(T22, "TUI art. 22(11): after that period, income requirements (art. 29(3)(b)) apply for a further permit", "trovano applicazione i requisiti reddituali di cui all'articolo 29, comma 3, lettera b)")
f(T22, "TUI art. 22(12): an employer who employs foreigners without a valid permit faces 6 months to 3 years' prison and EUR 5,000 fine per worker", "è punito con la reclusione da sei mesi a tre anni e con la multa di 5000 euro per ogni lavoratore impiegato")
f(T22, "TUI art. 22(2-ter): an employer who got a nulla osta in the past three years but did not sign the contratto di soggiorno cannot apply again unless not at fault", "non abbia sottoscritto il contratto di soggiorno di cui all'articolo 5-bis")
# rights
f("normattiva-tui-art2", "TUI art. 2(3): Italy guarantees legally resident foreign workers equal treatment and full equality of rights with Italian workers", "parità di trattamento e piena uguaglianza di diritti rispetto ai lavoratori italiani")
f("normattiva-dlgs66-2003-art3-orario-normale", "Normal working hours are 40 a week", "L'orario normale di lavoro è fissato in 40 ore settimanali")
f("normattiva-dlgs66-2003-art4-orario", "Average weekly hours including overtime may not exceed 48 per 7 days", "le quarantotto ore, comprese le ore di lavoro straordinario")
f("normattiva-dlgs66-2003-art5-straordinario", "Without a collective contract rule, overtime needs the worker's agreement and is capped at 250 hours a year", "previo accordo tra datore di lavoro e lavoratore per un periodo che non superi le duecentocinquanta ore annuali")
f("normattiva-dlgs66-2003-art5-straordinario", "Overtime must be counted separately and paid with the premiums set by collective contracts", "Il lavoro straordinario deve essere computato a parte e compensato con le maggiorazioni retributive previste dai contratti collettivi di lavoro")
f("normattiva-dlgs66-2003-art7-riposo", "Workers are entitled to 11 consecutive hours of rest every 24 hours", "il lavoratore ha diritto a undici ore di riposo consecutivo ogni ventiquattro ore")
f("normattiva-dlgs66-2003-art9-settimanale", "Workers are entitled to at least 24 consecutive hours of rest every 7 days, normally on Sunday", "un periodo di riposo di almeno ventiquattro ore consecutive, di regola in coincidenza con la domenica")
f("normattiva-dlgs66-2003-art10-ferie", "Paid annual leave is at least four weeks", "ha diritto ad un periodo annuale di ferie retribuite non inferiore a quattro settimane")
f("normattiva-dlgs66-2003-art10-ferie", "The four weeks' minimum leave cannot be replaced by pay except when the job ends", "non può essere sostituito dalla relativa indennità per ferie non godute, salvo il caso di risoluzione del rapporto di lavoro")
f("normattiva-codice-civile-art2120-tfr", "Every employee gets a TFR (end-of-service payment) whenever the job ends", "In ogni caso di cessazione del rapporto di lavoro subordinato, il prestatore di lavoro ha diritto ad un trattamento di fine rapporto")
f("normattiva-codice-civile-art2120-tfr", "TFR accrues each year at that year's pay divided by 13.5", "all'importo della retribuzione dovuta per l'anno stesso divisa per 13,5")
# CCNL wages
A = "news-fiscoetasse-ccnl-operai-agricoli-2026"
f(A, "The agricultural workers' CCNL was renewed on 28 May 2026, with +3.4% from 1 June 2026 on provincial wages", "+3,4% a decorrere dall'1 giugno 2026")
f(A, "A further +1.7% applies from 1 January 2027", "+1,7% a decorrere dall'1 gennaio 2027")
f(A, "National minimum for Area 3 (common) farm workers from 1 June 2026: EUR 1,042.434 a month", "Area 3 (comuni) | 1.042,434 | 1° giugno 2026")
f(A, "National minimum for Area 3 (common) nursery and flower workers from 1 June 2026: EUR 7.988 an hour", "Area 3 (comuni) | 7,988 | 1° giugno 2026")
f(A, "Provincial farm contracts may not set wages below the national area minimums", "I contratti provinciali non potranno fissare salari inferiori a tali minimi di area")
E = "news-leggeinchiaro-edilizia-tabelle-2026"
f(E, "Construction CCNL: from 1 March 2026 the national minimum for a common labourer (operaio comune) is EUR 9.48 an hour before provincial elements", "dal 1° marzo 2026 l'operaio comune ha un minimo di 9,48 € l'ora, prima degli elementi provinciali")
f(E, "Construction workers' holiday pay and Christmas bonus come through the Cassa Edile via an 18.5% gross set-aside", "ferie e gratifica natalizia (la tredicesima) si pagano con una maggiorazione lorda del 18,5% della retribuzione")
f(E, "The Cassa Edile, not the employer, pays the construction worker's holiday pay and Christmas bonus", "è la Cassa Edile a pagare all'operaio ferie e gratifica")
R = "ance-ragusa-tabella-retribuzioni-edili-2026-03"
f(R, "Construction hours are 40 a week over 5 days (Ragusa table)", "ORARIO DI LAVORO: 40 ORE SETTIMANALI DA EFFETTUARSI IN 5 GIORNI")
f(R, "In Ragusa province from 1 March 2026 a common construction labourer gets EUR 1,807.23 a month, EUR 10.45 an hour", "1.807,23 10,45")
H = "news-leggeinchiaro-turismo-alberghi-tabelle-2026"
f(H, "Hotel CCNL (Turismo): from May 2026 monthly minimums start at EUR 1,412.60 gross (level 7), for 14 monthly payments", "Dal maggio 2026 i minimi delle aziende alberghiere vanno da 1.412,60 € (7° livello)")
f(H, "Hotel CCNL level 6 minimum from May 2026 is EUR 1,507.45 a month, EUR 8.76 an hour", "6° | 1.507,45 € | 8,76 €")
f(H, "Hotel CCNL pays 14 months: 13th in December, 14th in July", "Le mensilità sono 14: la tredicesima a dicembre e la quattordicesima")
f(H, "Bars, restaurants, pizzerias, canteens and catering have their own CCNL (FIPE) since 2018", "Dal 2018 bar, ristoranti, pizzerie, mense e catering hanno un contratto proprio")
f(H, "Seasonal hotel workers get the same minimums as permanent staff", "gli stessi minimi tabellari")
f(H, "Seasonal workers' 13th, 14th and unused leave accrue pro rata and are paid at the end with TFR", "vengono pagate a fine contratto insieme al TFR")
M = "news-leggeinchiaro-multiservizi-tabelle-2026"
f(M, "Cleaning CCNL: from 1 October 2026 a level-2 cleaner's full-time minimum is EUR 1,413.50 gross a month", "L'addetto alle pulizie di 2° livello è a **1.413,50 €**")
f(M, "Cleaning CCNL: level 2 from 1 October 2026 is EUR 8.17 gross an hour (monthly divided by 173)", "1.413,50 € / 173 = 8,17 € lordi l'ora")
f(M, "Cleaning work is often part-time and pay is pro-rated to hours", "spesso part-time: gli importi vanno riproporzionati sull'orario")
I = "news-ilpost-fincantieri-paga-globale-2023-03"
f(I, "Workers from Bangladesh and elsewhere at Fincantieri shipyard subcontractors were paid a flat 'paga globale' that folded in leave, permits and TFR", "Gli operai, provenienti dal Bangladesh, dall’Europa dell’Est e dal Sud Italia, erano retribuiti attraverso un meccanismo definito «paga globale»")
f(I, "Payslips carried fictitious items that were not actually paid", "«voci artificiose» che servivano solo a ottenere sgravi fiscali ma non venivano pagate")
f(I, "383 workers accepted under EUR 7 gross an hour because they needed the job to renew their permit", "383 lavoratori sarebbero invece stati costretti ad accettare una paga oraria inferiore ai 7 euro lordi all’ora perché avevano bisogno di lavorare per rinnovare il permesso di soggiorno")
f(I, "Guardia di Finanza found 1,951 subcontractor workers paid irregularly", "la scoperta di 1.951 lavoratori delle aziende in appalto che sarebbero stati retribuiti in maniera irregolare")
f(I, "EUR 6 million was allegedly paid off the books (fuori busta)", "Sei milioni di euro sarebbero stati pagati «fuori busta»")
# sick, injury
S = "inps-malattia-visite-controllo"
f(S, "For sick pay, the worker's own doctor issues a sickness certificate and sends it online to INPS", "il lavoratore deve farsi rilasciare il certificato di malattia dal medico curante che provvede a trasmetterlo telematicamente all’INPS")
f(S, "INPS sick pay starts on day 4; the first three days are paid by the employer if the contract provides", "dal quarto giorno. I primi tre giorni sono a totale carico dell’azienda, se previsto dal contratto di lavoro")
f(S, "Sick pay is 50% of average daily pay from day 4 to day 20", "50% della retribuzione media giornaliera, dal quarto al ventesimo giorno")
f(S, "Sick pay is 66.66% from day 21 to day 180", "66,66% dal ventunesimo al centottantesimo giorno")
f(S, "A sick worker must be at home for checks from 10 to 12 and 17 to 19 every day on the certificate, weekends included", "compreso sabato, domenica e festivi), dalle 10 alle 12 e dalle 17 alle 19")
f("normattiva-dpr1124-1965-art52-inail", "An insured worker must tell the employer at once of any injury, however slight", "dare immediata notizia di qualsiasi infortunio che gli accada, anche se di lieve entità, al proprio datore di lavoro")
f("normattiva-dpr1124-1965-art52-inail", "If the worker does not report and the employer does not know, days before the employer learns of the injury are not paid", "non è corrisposta l'indennità per i giorni antecedenti a quello in cui il datore di lavoro ha avuto notizia dell'infortunio")
f("normattiva-dpr1124-1965-art68-inail", "INAIL pays 60% of daily pay from the fourth day after a work accident while the worker cannot work", "un'indennità giornaliera nella misura del sessanta per cento della retribuzione giornaliera")
f("normattiva-dpr1124-1965-art68-inail", "From day 91 of incapacity (even non-continuous) INAIL pays 75%", "al settantacinque per cento della retribuzione giornaliera")
# NASpI
N = "inps-naspi-scheda"
f(N, "NASpI goes to employees who lost their job involuntarily", "lavoratori con rapporto di lavoro subordinato che hanno perduto involontariamente l'occupazione")
f(N, "Non-EU workers on a seasonal permit cannot get NASpI", "lavoratori extracomunitari con permesso di soggiorno per lavoro stagionale")
f(N, "Fixed-term farm workers cannot get NASpI", "operai agricoli a tempo determinato")
f(N, "NASpI needs at least 13 weeks of unemployment contributions in the four years before unemployment", "Sono necessarie almeno 13 settimane di contribuzione contro la disoccupazione nei quattro anni precedenti")
f(N, "NASpI is paid monthly for half the contribution weeks of the last four years", "per un numero di settimane pari alla metà delle settimane contributive presenti negli ultimi quattro anni")
f(N, "NASpI is 75% of average monthly pay below a yearly reference amount", "La misura della prestazione è pari al 75% della retribuzione media mensile")
f(N, "NASpI falls 3% a month from the sixth month", "La NASpI si riduce del 3% ogni mese a decorrere dal primo giorno del sesto mese di fruizione")
f(N, "Resigning excludes NASpI", "sono esclusi pertanto i lavoratori il cui rapporto di lavoro sia cessato a seguito di dimissioni")
f(N, "Resignation for just cause, forced by others' conduct, still qualifies for NASpI", "qualora le dimissioni non siano riconducibili alla libera scelta del lavoratore")
f(N, "The NASpI application is online only and must be made within 68 days", "esclusivamente in via telematica** e a pena di decadenza **entro 68 giorni")
f(N, "NASpI can also be claimed via the INPS contact centre 803 164 (landline, free) or 06 164 164 (mobile), or a patronato", "Contact center al numero 803 164 (gratuito da rete fissa) oppure 06 164 164 da rete mobile")
f(N, "NASpI is paid into a bank or postal account in the claimant's own name", "Il conto corrente deve necessariamente essere intestato o cointestato al richiedente la prestazione")
f(N, "NASpI is paid from the eighth day after the job ends if applied for by then", "dall'ottavo giorno successivo alla data di cessazione del rapporto di lavoro, se la domanda viene presentata entro l'ottavo giorno")
f(N, "Going to a non-EU country for reasons other than job-seeking keeps NASpI subject to conditionality rules", "in un paese extracomunitario per motivi diversi dalla ricerca di lavoro")
# INL
L31 = "inl-modulo-31-inglese-2025"
f(L31, "INL form 31 (request for inspection) covers unpaid wages, whether or not shown on the payslip", "retribution (indicated/not indicated on the paycheck) not received")
f(L31, "Form 31 covers unregistered (in nero) work", "Unregistered employment regularization")
f(L31, "Form 31 covers unpaid 13th/14th month pay and TFR", "13th/14th monthly payment")
f(L31, "Form 31 covers unregistered and unpaid overtime", "overtime/hours not registered on paycheck and not paid")
f(L31, "Form 31 cannot be used to contest a dismissal", "the present form cannot be used to contest a dismissal")
f(L31, "Form 31 goes to the Territorial Labour Inspectorate of the province where the workplace is", "corresponding to that of the province where the workplace is")
f(L31, "Without a copy of an identity document the complaint is not accepted", "in the absence of an identity document, the complaint will not be accepted")
f(L31, "Attach evidence such as pay receipts and sheets of hours and days worked", "sheets showing the hours and days of presence at work")
f(L31, "Free-text fields can be in your own language, but should also be in Italian", "It is possible to fill in the free text fields of this form in your own language")
f(L31, "To protect claims from expiring, send the employer a formal notice by registered letter with return receipt and report missing contributions to INPS", "sending a formal notice to the employer with registered letter with return receipt")
f(L31, "The ITL may start a conciliation on the issues reported", "initiate an attempt to conciliation")
f(L31, "The list of ITL offices is at ispettorato.gov.it/contatti", "https://www.ispettorato.gov.it/contatti/")
f("inl-modulo-31-bengalese-2025", "INL form 31 is also published in a Bangla version", "RICHIESTA DI INTERVENTO ISPETTIVO", "Bangla text layer garbled; Italian header and the file name (bengalese) identify the Bangla version")
f("normattiva-dlgs124-2004-art11-conciliazione", "At a conciliation the worker can be assisted by a union or a professional", "Le parti convocate possono farsi assistere anche da associazioni o organizzazioni sindacali")
f("normattiva-dlgs124-2004-art12-diffida", "If inspectors find unpaid contractual amounts, they order the employer to pay (diffida accertativa)", "il personale ispettivo delle Direzioni del lavoro diffida il datore di lavoro a corrispondere gli importi risultanti dagli accertamenti")
f("normattiva-dlgs124-2004-art12-diffida", "The employer has 30 days from the diffida to seek conciliation", "Entro trenta giorni dalla notifica della diffida accertativa")
f("normattiva-l604-1966-art6-impugnazione", "A dismissal must be challenged in writing within 60 days of receiving it, also via a union", "Il licenziamento deve essere impugnato a pena di decadenza entro sessanta giorni dalla ricezione della sua comunicazione in forma scritta")
f("normattiva-l604-1966-art6-impugnazione", "The challenge lapses unless a court claim or conciliation request follows within 180 days", "entro il successivo termine di centottanta giorni")
D = "normattiva-dlgs151-2015-art26-dimissioni"
f(D, "A resignation is valid only if made online on Ministry of Labour forms", "esclusivamente con modalità telematiche su appositi moduli resi disponibili dal Ministero del lavoro")
f(D, "A resignation can be withdrawn within seven days", "Entro sette giorni dalla data di trasmissione del modulo di cui al comma 1 il lavoratore ha la facoltà di revocare")
f(D, "Resignation forms can be sent through patronati, unions, labour consultants or the ITL", "anche per il tramite dei patronati, delle organizzazioni sindacali")
# jail / deport
f("normattiva-tui-art10bis", "Entering or staying illegally is an offence fined EUR 5,000 to 10,000", "è punito con l'ammenda da 5.000 a 10.000 euro")
T13 = "normattiva-tui-art13"
f(T13, "The Prefect orders expulsion when a permit expired more than 60 days ago without renewal being requested", "quando il permesso di soggiorno sia scaduto da più di sessanta giorni e non ne è stato chiesto il rinnovo")
f(T13, "An expelled person may ask for 7 to 30 days to leave voluntarily", "entro un termine compreso tra 7 e 30 giorni")
f(T13, "Voluntary departure can be through assisted voluntary return programmes", "anche attraverso programmi di rimpatrio volontario ed assistito")
f(T13, "Re-entering after expulsion without authorisation is punished by 1 to 4 years' prison", "è punito con la reclusione da uno a quattro anni")
f(T13, "The re-entry ban lasts 3 to 5 years", "per un periodo non inferiore a tre anni e non superiore a cinque anni")
f(T13, "The re-entry ban is entered in the Schengen Information System and bars entry to EU and Schengen states", "comporta il divieto di ingresso e soggiorno nel territorio degli Stati membri della Unione europea")
f(T13, "At the expulsion validation hearing the person can get free legal aid and an interpreter", "è altresì ammesso al gratuito patrocinio a spese dello Stato")
T14 = "normattiva-tui-art14"
f(T14, "If removal cannot be immediate, the Questore orders detention in the nearest CPR (repatriation detention centre)", "presso il centro di permanenza per i rimpatri più vicino")
f(T14, "CPR validation means three months in the centre", "La convalida comporta la permanenza nel centro per un periodo di complessivi tre mesi")
f(T14, "The judge can extend by three months and then by up to twelve more months in total", "per una durata complessiva non superiore ad altri dodici mesi")
T5 = "normattiva-tui-art5"
f(T5, "Renewal must be requested from the Questore of the province where you live, at least 90 days before expiry", "Il rinnovo del permesso di soggiorno è richiesto dallo straniero al questore della provincia in cui dimora, almeno", "next lines read '((novanta giorni)) prima della scadenza'; Normattiva markup splits the quote")
f(T5, "The permit is issued, renewed or converted within 90 days of the application", "Il permesso di soggiorno è rilasciato, rinnovato o convertito entro", "next lines read '((novanta giorni)) dalla data in cui è stata presentata la domanda'")
f(T5, "Renewal applicants are fingerprinted", "Lo straniero che richiede il rinnovo del permesso di soggiorno è sottoposto a rilievi fotodattiloscopici")
f(T5, "Forging or using a forged visa, permit or contratto di soggiorno, or documents to obtain them, is punished by 1 to 6 years' prison", "oppure utilizza uno di tali documenti contraffatti o alterati, è punito con la reclusione da uno a sei anni")
f("normattiva-tui-art6", "Failing without good reason to show passport and permit to police is punished by arrest up to one year and a fine up to EUR 2,000", "con l'ammenda fino ad euro 2.000")
f("normattiva-tui-art6", "A permit for employment can be used for the other permitted activities", "Il permesso di soggiorno rilasciato per motivi di lavoro subordinato, lavoro autonomo e familiari può essere utilizzato anche per le altre attività consentite")
f("normattiva-tui-art4", "A foreigner convicted, even not finally, of serious offences (art. 380 c.p.p.) is not admitted; this also bars permits", "che risulti condannato, anche con sentenza non definitiva")
f("normattiva-tui-art16", "A judge may substitute a prison sentence of up to two years with expulsion", "entro il limite di due anni")
f("normattiva-dpr309-1990-art73", "Dealing drugs (Table I) is punished by 6 to 20 years' prison and EUR 26,000 to 260,000 fine", "è punito con la reclusione da sei a venti anni e con la multa da euro 26.000 a euro 260.000")
f("normattiva-dpr309-1990-art73", "Minor drug dealing (lieve entità) is punished by 6 months to 5 years", "è punito con le pene della reclusione da sei mesi a cinque anni")
f("normattiva-dpr309-1990-art75", "Possession for personal use brings administrative sanctions including suspension of the passport", "sospensione del passaporto e di ogni altro documento equipollente o divieto di conseguirli")
# re-entry
f("poliziadistato-ricevuta-rinnovo-378", "Police (2007): people awaiting renewal may leave and re-enter Italy showing the Poste Italiane renewal receipt", "presentando solo la ricevuta delle Poste italiane che attesta l'avvenuta presentazione della domanda")
f("poliziadistato-ricevuta-rinnovo-378", "They must show a valid passport, the renewal receipt and a copy or the original of the expired permit", "copia o originale del titolo di soggiorno scaduto")
f("poliziadistato-ricevuta-rinnovo-10929", "Police (2008): first-issue applicants with the receipt may leave and return only with no transit through other Schengen countries", "il viaggio non preveda il transito in altri Paesi Schengen")
f("poliziadistato-ricevuta-rinnovo-10929", "Police (2008): first-issue applicants must exit and re-enter through the same border crossing", "l'uscita ed il rientro avvengano attraverso lo stesso valico di frontiera")
f("poliziadistato-ricevuta-rinnovo-10929", "Police (2008): border staff stamp the post-office receipt as well as the passport", "metta il timbro di uscita oltre che sul documento di viaggio anche sulla ricevuta delle Poste italiane")
X = "esteri-ambdhaka-reentry-2026-07"
f(X, "Italian Embassy Dhaka re-entry visa: for a permit expired no more than 60 days before application, bring a copy of the expired permit and the renewal receipt", "In case the Italian residence permit expired no longer than 60 days before the visa")
f(X, "Re-entry visa: for a lost or stolen permit, an apostilled police report from the country where it was lost", "Copy of the apostilled police report issued by relevant police authorities of the country")
f(X, "Re-entry visa: passport valid at least 15 months with two blank visa pages", "Passport must be valid for at least for 15 months from the date of application")
f(X, "Re-entry visa: proof of exit date (passport exit stamp, or flight ticket if passport lost)", "Copy of the passport with Italian exit stamp")
f(X, "Re-entry visa: a letter explaining the reasons, in Italian or English", "explaining the reasons for the application of re-entry visa")
f(X, "Re-entry visa is issued only after the Questura's clearance", "Visa will be issued only after no-impediment to proceed by Italian Immigration")
f(X, "Re-entry visa: national D visa form, one ICAO photo (3.5 x 4 cm, white background, last 6 months), flight booking", "Photos must be ICAO format")

if __name__ == "__main__":
    for s in SOURCES:
        r = subprocess.run([sys.executable, T, "source", "--name", s[0], "--publisher", s[1], "--title", s[2], "--official", s[3], "--page-date", s[4]], capture_output=True, text=True)
        if r.returncode:
            print("SRC ERR", s[0], r.stdout.strip(), r.stderr.strip()[-200:])
    for name, claim, quote, note in F:
        args = [sys.executable, T, "add", "--prefix", "L", "--name", name, "--claim", claim, "--quote", quote, "--page-date", meta[name][4], "--status", st(name)]
        if note:
            args += ["--note", note]
        r = subprocess.run(args, capture_output=True, text=True)
        print((r.stdout.strip() or "ERR"), "|", claim[:80], "|", r.stderr.strip()[-200:])
