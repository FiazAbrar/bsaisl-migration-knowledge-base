import subprocess, sys
T = "../../../../tools/facts.py"

SOURCES = [
    ("lavoro-it-flussi-2027-circolare-news", "Ministry of Labour and Social Policies (Italy)", "Decreto Flussi 2027, pubblicata la Circolare con le indicazioni operative", "yes", "2026-10-01"),
    ("lavoro-it-circolare-7185-2026-page", "Ministry of the Interior, Ministry of Labour, Ministry of Agriculture, Ministry of Tourism (Italy)", "Circolare congiunta prot. n. 7185 del 1 ottobre 2026: flussi 2027, quote, precompilazione e click day", "yes", "2026-10-01"),
    ("gu-dpcm-flussi-2026-2028-art6", "Gazzetta Ufficiale", "DPCM 2 ottobre 2025, programmazione dei flussi 2026-2028, art. 6", "yes", "2025-10-15"),
    ("gu-dpcm-flussi-2026-2028-art8", "Gazzetta Ufficiale", "DPCM 2 ottobre 2025, programmazione dei flussi 2026-2028, art. 8", "yes", "2025-10-15"),
    ("gu-dpcm-flussi-2026-2028-art9", "Gazzetta Ufficiale", "DPCM 2 ottobre 2025, programmazione dei flussi 2026-2028, art. 9", "yes", "2025-10-15"),
    ("normattiva-tui-art22", "Normattiva", "D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 22, text in force 10 Nov 2026", "yes", "2026-11-10"),
    ("normattiva-tui-art5", "Normattiva", "D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 5, text in force 10 Nov 2026", "yes", "2026-11-10"),
    ("normattiva-tui-art5bis", "Normattiva", "D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 5-bis, text in force 10 Nov 2026", "yes", "2026-11-10"),
    ("normattiva-tui-art9", "Normattiva", "D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 9, text in force 10 Nov 2026", "yes", "2026-11-10"),
    ("normattiva-tui-art24", "Normattiva", "D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 24, text in force 10 Nov 2026", "yes", "2026-11-10"),
    ("normattiva-tui-art24bis", "Normattiva", "D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 24-bis, text in force 10 Nov 2026", "yes", "2026-11-10"),
    ("normattiva-tui-art26", "Normattiva", "D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 26, text in force 10 Nov 2026", "yes", "2026-11-10"),
    ("normattiva-tui-art27", "Normattiva", "D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 27, text in force 10 Nov 2026", "yes", "2026-11-10"),
    ("normattiva-tui-art27quater", "Normattiva", "D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 27-quater (EU Blue Card), text in force 10 Nov 2026", "yes", "2026-11-10"),
    ("normattiva-dl-145-2024-art3", "Normattiva", "Decreto-legge 11 ottobre 2024, n. 145, art. 3 (Paesi a particolare rischio)", "yes", "2026-11-10"),
    ("ambdhaka-news-2804", "Embassy of Italy in Dhaka", "Important news for work visa applicant (communique, 17 October 2024)", "yes", "2024-10-17"),
    ("ambdhaka-ambassador-interview-kalerkantho-2026-09", "Embassy of Italy in Dhaka", "Interview with the Italian Ambassador to Bangladesh, Antonio Alessandro, with Kaler Kantho", "yes", "2026-09-16"),
    ("ambdhaka-political-consultations-2026-08", "Embassy of Italy in Dhaka", "Third round of bilateral political consultations between Italy and Bangladesh. Focus on migration cooperation.", "yes", "2026-08-05"),
    ("ambdhaka-where-to-apply", "Embassy of Italy in Dhaka", "Where to apply for a visa", "yes", "2026-06-30"),
    ("ambdhaka-visa-cost", "Embassy of Italy in Dhaka", "Cost for a visa and how to pay", "yes", "2026-06-30"),
    ("ambdhaka-choose-visa", "Embassy of Italy in Dhaka", "Choose the right visa based on your needs and check the documents required", "yes", "2026-09-14"),
    ("ambdhaka-checklist-decreto-flussi-2026-07", "Embassy of Italy in Dhaka", "Check-list for Work VISA (D type), Decreto Flussi", "yes", "2026-09-14"),
    ("ambdhaka-checklist-bluecard-2026-07", "Embassy of Italy in Dhaka", "Check-list for Qualified Work VISA L/N ART 27 (D type), Blue Card", "yes", "2026-09-14"),
    ("ambdhaka-checklist-art23-2026-07", "Embassy of Italy in Dhaka", "Check-list for Work VISA L/N ART 22/23 (D type)", "yes", "2026-09-14"),
    ("ambdhaka-checklist-selfemployment-2026-07", "Embassy of Italy in Dhaka", "Check-list for SELF-EMPLOYMENT visa", "yes", "2026-09-14"),
    ("vfs-italy-bd-bluecard-2026-02", "VFS Global (Italy visa centre, Bangladesh)", "Check-list for Qualified Work VISA L/N ART 27 (BLUECARD-002, Feb 2026)", "yes", "2026-02-01"),
    ("vfs-italy-bd-notice-work-visa-webform-2025-03", "VFS Global (Italy visa centre, Bangladesh)", "Important Notice for the work visa application", "yes", "2025-03-31"),
    ("vfs-italy-bd-webform-login", "VFS Global (Italy visa centre, Bangladesh)", "Italy Bangladesh work visa webform (login page)", "yes", "undated"),
    ("vfs-italy-bd-ln-nulla-osta-walkin-2026-08", "VFS Global (Italy visa centre, Bangladesh)", "Update on L/N Nulla Osta submission process", "yes", "2026-08-01"),
    ("questure-poliziadistato-kit-postale-documenti", "Polizia di Stato (Questura)", "Documenti da inserire nel kit postale per le principali tipologie di permesso di soggiorno", "yes", "undated"),
    ("integrazionemigranti-ingressi-soggiorno-lavoro-novita", "Ministry of Labour and Social Policies (Italy), Integrazione Migranti portal", "Ingressi e soggiorno per lavoro: le ultime novita normative", "yes", "undated"),
    ("ambdhaka-communique-ln-bluecard-2025-08", "Embassy of Italy in Dhaka", "Communique on Nulla Osta code L/N Blue Card (31 August 2025)", "yes", "2025-09-01"),
    ("ambdhaka-communique-suspended-nulla-osta-2025-09", "Embassy of Italy in Dhaka", "Communique on suspended Nulla Osta for work visa (9 September 2025)", "yes", "2025-09-09"),
]

def st(date):
    if date == "undated":
        return "possibly-outdated"
    return "verified" if date >= "2025-11-10" else "possibly-outdated"

D = {s[0]: s[4] for s in SOURCES}
VFSNOTE = "VFS Global is the Embassy of Italy in Dhaka's exclusive visa application centre (ambdhaka-where-to-apply); treated as official"
IMG = "page text is an image (Embassy communique screenshot); quote transcribed exactly from the image, see sources/<name>.html image link"

# (key, name, claim, quote, extra args)
FACTS = [
 # quotas and dates
 ("q2027", "lavoro-it-circolare-7185-2026-page", "For 2027 Italy admits 165,850 non-EU workers in total: 76,200 non-seasonal (14,000 of them domestic and care work), 89,000 seasonal and 650 self-employed", "complessivamente n. 165.850 cittadini non comunitari", ["--visa","Decreto Flussi","--field","quota 2027 total","--value","165850"]),
 ("q2027ns", "lavoro-it-circolare-7185-2026-page", "2027 quota: 76,200 entries for non-seasonal employed work, of which 14,000 for domestic and care work", "n. 76.200 ingressi per lavoro subordinato non stagionale, di cui n. 14.000", ["--visa","Decreto Flussi","--field","quota 2027 non-seasonal","--value","76200"]),
 ("q2027s", "lavoro-it-circolare-7185-2026-page", "2027 quota: 89,000 seasonal entries in agriculture and tourism", "n. 89.000 ingressi per lavoro subordinato stagionale nei settori agricolo e", []),
 ("q2027a", "lavoro-it-circolare-7185-2026-page", "2027 quota: 650 entries for self-employment", "n. 650 ingressi per lavoro autonomo", ["--visa","Self-employment","--field","quota 2027","--value","650"]),
 ("pre2027", "lavoro-it-circolare-7185-2026-page", "Pre-filling of 2027 nulla osta applications on the ALI portal runs from 9:00 on 23 October 2026 to 20:00 on 7 December 2026", "dalle ore 9:00 del 23 ottobre 2026 alle", ["--visa","Decreto Flussi","--field","pre-filling 2027","--value","23 Oct - 7 Dec 2026"]),
 ("pre2027b", "lavoro-it-circolare-7185-2026-page", "Pre-filling closes at 20:00 on 7 December 2026", "ore 20:00 del 7 dicembre 2026", []),
 ("reopen", "lavoro-it-circolare-7185-2026-page", "The ALI pre-filling section reopens from 9 to 13 December 2026 only to complete and save forms already started; no new applications can be added", "possibile inserire nuove domande", []),
 ("reopen2", "lavoro-it-circolare-7185-2026-page", "The reopening runs from 9:00 on 9 December to 20:00 on 13 December 2026", "dalle ore 9:00 del giorno 9 alle ore 20:00 del giorno 13 dicembre 2026", []),
 ("cd-agri", "lavoro-it-circolare-7185-2026-page", "2027 click day for seasonal agriculture (form C-Stag agricolo): 12 January 2027 from 9:00", "12 gennaio 2027, per gli ingressi per lavoro subordinato stagionale nel settore", []),
 ("cd-tour", "lavoro-it-circolare-7185-2026-page", "2027 click day for seasonal tourism (form C-Stag turistico): 9 February 2027", "9 febbraio 2027, per gli ingressi per lavoro subordinato stagionale nel settore", []),
 ("cd-ns", "lavoro-it-circolare-7185-2026-page", "2027 click day for non-seasonal employed work (form B2020): 16 February 2027", "16 febbraio 2027, per gli ingressi per lavoro subordinato non stagionale", ["--visa","Decreto Flussi","--field","click day non-seasonal 2027","--value","16 Feb 2027 09:00"]),
 ("cd-dom", "lavoro-it-circolare-7185-2026-page", "2027 click day for domestic and care work (form A-bis): 18 February 2027", "18 febbraio 2027, per gli ingressi per lavoro subordinato non stagionale nel", []),
 ("cd-9", "lavoro-it-circolare-7185-2026-page", "Click-day applications can be sent from 9:00 on the set days", "potranno essere presentate, a decorrere dalle ore 9:00, nei seguenti giorni", []),
 ("until", "lavoro-it-circolare-7185-2026-page", "All 2027 applications can be sent until 31 December 2027 while quota remains", "Tutte le domande potranno essere presentate fino al 31 dicembre 2027, ferma", []),
 ("forms", "lavoro-it-circolare-7185-2026-page", "The non-seasonal nulla osta form is B2020", "nulla osta/comunicazione al lavoro subordinato non stagionale nei", []),
 ("ali-url", "lavoro-it-circolare-7185-2026-page", "Pre-filling is done on the Interior Ministry's Portale Servizi ALI at portaleservizi.dlci.interno.it", "(https://portaleservizi.dlci.interno.it/AliSportello/ali/home.htm)", []),
 ("confirm15", "lavoro-it-circolare-7185-2026-page", "The employer must confirm the nulla osta request to the SUI within 15 days of being told the visa checks are complete; without confirmation the request is treated as refused and the nulla osta revoked", "In assenza di conferma entro tale termine, la richiesta si intende rifiutata e il nulla", []),
 ("inform", "lavoro-it-circolare-7185-2026-page", "The employer must promptly inform the worker of every communication received about the nulla osta", "l'obbligo in capo al datore di lavoro di informare tempestivamente il cittadino", []),
 ("cs15c", "lavoro-it-circolare-7185-2026-page", "The deadline to sign the contratto di soggiorno rose from 8 to 15 days from the worker's entry into Italy", "soggiorno, che passa da otto a quindici giorni dalla data di ingresso del lavoratore", ["--visa","Decreto Flussi","--field","contratto di soggiorno deadline","--value","15 days from entry"]),
 ("kenya", "lavoro-it-circolare-7185-2026-page", "From 2027 Kenya is added to the countries of origin, after an MoU signed 2 July 2026", "anche il Kenya con il quale l'Italia ha stipulato il 2 luglio 2026 il Memorandum", []),
 ("lavnews", "lavoro-it-flussi-2027-circolare-news", "Ministry of Labour summary: pre-filling from 23 October to 7 December 2026; click days 12 Jan, 9 Feb, 16 Feb, 18 Feb 2027", "Dal 23 ottobre 2026 al 7 dicembre 2026", []),
 # DPCM
 ("dpcm-ns", "gu-dpcm-flussi-2026-2028-art6", "The 2026-2028 decree sets 76,850 non-seasonal and self-employed entries a year: 76,200 employed and 650 self-employed", "76.850 unita' per l'anno 2026, di cui 76.200 per lavoro", []),
 ("dpcm-bd", "gu-dpcm-flussi-2026-2028-art6", "Bangladesh is among the countries with a cooperation agreement whose citizens share a reserved non-seasonal quota", "Albania, Algeria, Bangladesh, Bosnia-Herzegovina", ["--visa","Decreto Flussi","--field","Bangladesh eligible","--value","yes, reserved cooperation quota"]),
 ("dpcm-25k", "gu-dpcm-flussi-2026-2028-art6", "The reserved quota for these cooperating countries (Bangladesh included) is 25,000 non-seasonal workers a year in 2026, 2027 and 2028", "Uzbekistan: 25.000 unita' nel 2026, 25.000 unita' nel 2027  e  25.000", ["--visa","Decreto Flussi","--field","reserved quota cooperating countries","--value","25000/year"]),
 ("dpcm-sect", "gu-dpcm-flussi-2026-2028-art6", "Non-seasonal sectors include agriculture, food, textiles, metalworking, construction, trade, hotels and restaurants, tourism, transport and logistics, support services, health and social care", "costruzioni;  commercio  all'ingrosso  e  al   dettaglio", []),
 ("dpcm-dom", "gu-dpcm-flussi-2026-2028-art6", "Domestic and care quota: 13,600 in 2026, 14,000 in 2027, 14,200 in 2028", "1. per il 2026, 13.600 unita';", []),
 ("dpcm-lapse", "gu-dpcm-flussi-2026-2028-art8", "Applications not within quota 6 months after 31 December of the year, and nulla osta not followed by a visa in that time, lapse and are archived", "decadono e vengono archiviati d'ufficio", []),
 ("dpcm-split", "gu-dpcm-flussi-2026-2028-art9", "The Ministry of Labour splits the quotas by province within 10 days of the click day", "Ministero del lavoro e delle politiche sociali entro dieci giorni dal", []),
 ("dpcm-cpi", "gu-dpcm-flussi-2026-2028-art9", "The employer must show it first checked with the Centro per l'impiego that no worker already in Italy is available", "presso il Centro per l'impiego competente,  dell'indisponibilita'  di", []),
 # Art 22
 ("a22-sui", "normattiva-tui-art22", "Each province has a Sportello Unico per l'Immigrazione at the Prefettura, responsible for the whole procedure to hire a foreign employee", "In ogni provincia è istituito presso la prefettura-ufficio territoriale del Governo uno sportello unico per l'immigrazione", []),
 ("a22-docs", "normattiva-tui-art22", "The employer's application includes a named nulla osta request, housing documentation, the proposed contract of stay with a commitment to pay the return journey, and the asseverazione", "richiesta nominativa di nulla osta al lavoro", []),
 ("a22-ret", "normattiva-tui-art22", "The proposed contract includes the employer's commitment to pay the worker's return travel", "comprensiva dell'impegno al pagamento da parte dello stesso datore di lavoro delle spese di ritorno dello straniero nel Paese di provenienza", []),
 ("a22-8d", "normattiva-tui-art22", "The labour-market check counts as negative if the Centro per l'impiego does not report an available worker within 8 days", "se il centro per l'impiego non comunica la disponibilità di lavoratori presenti sul territorio nazionale entro otto giorni", []),
 ("a22-3", "normattiva-tui-art22", "A private employer can file no more than three nulla osta requests per year; the limit does not apply through employer organisations, labour consultants and similar professionals or temp agencies", "possono presentare come utenti privati non più di tre richieste di nulla osta al lavoro subordinato", []),
 ("a22-irr", "normattiva-tui-art22", "An employer who did not sign the contract of stay after a previous nulla osta in the last three years cannot apply, unless not at fault", "all'esito della relativa procedura non abbia sottoscritto il contratto di soggiorno", []),
 ("a22-60", "normattiva-tui-art22", "The SUI issues the nulla osta within at most 60 days from when the request is counted against the quota", "nel complessivo termine massimo di sessanta giorni dalla data di imputazione della richiesta alle quote", ["--visa","Decreto Flussi","--field","nulla osta processing","--value","max 60 days from quota allocation"]),
 ("a22-6m", "normattiva-tui-art22", "A work nulla osta is valid for at most six months from issue", "Il nulla osta al lavoro subordinato ha validità per un periodo non superiore a sei mesi dalla data del rilascio", ["--visa","Decreto Flussi","--field","nulla osta validity","--value","6 months"]),
 ("a22-fraud", "normattiva-tui-art22", "A nulla osta is refused or revoked if documents were obtained by fraud or forged, or if the signed contract of stay is not sent to the SUI in time", "se i documenti presentati sono stati ottenuti mediante frode o sono stati falsificati o contraffatti", []),
 ("a22-5q", "normattiva-tui-art22", "The employer must confirm the nulla osta request to the SUI within 15 days of being told the visa checks are complete", "entro quindici giorni dalla comunicazione di avvenuta conclusione degli accertamenti di rito sulla domanda di visto", []),
 ("a22-cons", "normattiva-tui-art22", "Only after confirmation does the consulate issue the entry visa; consulate and SUI communicate only through the visa IT portal", "In caso di conferma, l'ufficio consolare presso il Paese di residenza o di origine dello straniero rilascia il visto di ingresso", []),
 ("a22-cs", "normattiva-tui-art22", "Within 15 days of the worker's entry, employer and worker sign the contract of stay; the worker may sign by hand; the employer sends it online to the SUI", "Entro quindici giorni dalla data di ingresso del lavoratore straniero nel territorio nazionale, il datore di lavoro e il lavoratore straniero sottoscrivono", []),
 ("a22-hand", "normattiva-tui-art22", "The worker may sign the contract of stay by hand", "Il lavoratore può altresì firmare il contratto in forma autografa", []),
 ("a22-work", "normattiva-tui-art22", "Until the contract of stay is signed, the nulla osta allows the worker to work in Italy", "Nelle more della sottoscrizione del contratto di soggiorno il nulla osta consente lo svolgimento dell'attività lavorativa", []),
 ("a22-cf", "normattiva-tui-art22", "The SUI can send the documents, including the codice fiscale, to the consulate", "trasmette la documentazione, ivi compreso il codice fiscale, agli uffici consolari", []),
 ("a22-lose", "normattiva-tui-art22", "Losing the job does not revoke the residence permit; the worker can register as available for work for the remaining validity and at least one year", "La perdita del posto di lavoro non costituisce motivo di revoca del permesso di soggiorno", []),
 ("a22-1y", "normattiva-tui-art22", "The unemployed worker keeps the right to stay for at least one year (not for seasonal permits)", "per un periodo non inferiore ad un anno", []),
 ("a22-pen", "normattiva-tui-art22", "An employer who employs workers without a valid permit faces 6 months to 3 years' prison and a EUR 5,000 fine per worker", "è punito con la reclusione da sei mesi a tre anni e con la multa di 5000 euro per ogni lavoratore impiegato", []),
 ("a22-65", "normattiva-tui-art22", "A worker who goes home keeps INPS contributions and can draw a pension at 65 without a reciprocity agreement", "al compimento del sessantacinquesimo anno di età", []),
 ("a22-patr", "normattiva-tui-art22", "Patronati (free welfare advice offices) serve non-EU workers employed legally in Italy", "Le attribuzioni degli istituti di patronato e di assistenza sociale", []),
 ("a22-5bis", "normattiva-tui-art22", "The nulla osta is refused if the employer was convicted in the last five years of smuggling, caporalato (illegal gangmastering, art. 603-bis) or employing undocumented workers", "intermediazione illecita e sfruttamento del lavoro", []),
 # 24-bis
 ("a24b", "normattiva-tui-art24bis", "Labour consultants and similar professionals or employer organisations check the employer's compliance with the national contract and that the number of requests fits its turnover and staff, and issue an asseverazione", "In caso di esito positivo delle verifiche è rilasciata apposita asseverazione", []),
 ("a24b-2", "normattiva-tui-art24bis", "The congruity check considers the firm's assets, finances, turnover and number of employees", "capacità patrimoniale, dell'equilibrio economico-finanziario, del fatturato, del numero dei dipendenti", []),
 ("a24b-4", "normattiva-tui-art24bis", "The Ispettorato Nazionale del Lavoro can run random checks with the Agenzia delle Entrate", "di effettuare controlli a campione", []),
 # DL 145 art 3
 ("dl145-bd", "normattiva-dl-145-2024-art3", "Until 31 December 2025, nulla osta requests and nulla osta for Bangladeshi, Pakistani and Sri Lankan workers required prior checks by the labour inspectorate, with no automatic issue after 60 days", "i commi 1 e 2 si applicano alle domande di nulla osta e ai nulla osta per lavoratori cittadini del Bangladesh, del Pakistan e dello Sri Lanka", []),
 ("dl145-susp", "normattiva-dl-145-2024-art3", "Nulla osta already issued to these workers without a visa were suspended until the SUI expressly confirmed the checks", "è sospesa fino alla conferma espressa da parte dello sportello unico per l'immigrazione", []),
 ("dl145-dec", "normattiva-dl-145-2024-art3", "The high-risk countries are to be named by a decree of the Foreign Minister", "Gli Stati e i territori di cui al comma 1 sono individuati con decreto del Ministro degli affari esteri", []),
 # Art 5, 5-bis
 ("a5-3bis", "normattiva-tui-art5", "A work permit lasts as long as the contract of stay, up to 1 year for a fixed-term contract and 2 years for a permanent one; each renewal up to 3 years", "in relazione ad un contratto di lavoro subordinato a tempo indeterminato, la durata di due anni", ["--visa","Decreto Flussi","--field","permit length permanent contract","--value","up to 2 years; renewals up to 3"]),
 ("a5-1y", "normattiva-tui-art5", "Fixed-term contract: permit up to one year", "in relazione ad un contratto di lavoro subordinato a tempo determinato, la durata di un anno", []),
 ("a5-ren3", "normattiva-tui-art5", "Each renewal can last up to three years", "Ciascun rinnovo non può superare la durata di tre anni", []),
 ("a5-8d", "normattiva-tui-art5", "The permesso di soggiorno must be requested from the Questura within 8 working days of entry", "entro otto giorni lavorativi dal suo ingresso nel territorio dello Stato", []),
 ("a5-ren90", "normattiva-tui-art5", "Renewal must be requested from the Questura at least 90 days before expiry (text as amended by D.Lgs. 83/2026)", "Il rinnovo del permesso di soggiorno è richiesto dallo straniero al questore della provincia in cui dimora, almeno", ["--note","the 90-day figure is on the next line of the Normattiva text, in double brackets as amended by D.Lgs. 16 April 2026 n. 83 (applies from 22 May 2026); integrazionemigranti page still says 60 days"]),
 ("a5-fp", "normattiva-tui-art5", "Renewal applicants are fingerprinted", "Lo straniero che richiede il rinnovo del permesso di soggiorno è sottoposto a rilievi fotodattiloscopici", []),
 ("a5-9", "normattiva-tui-art5", "The permit is issued, renewed or converted within 90 days of the application (as amended by D.Lgs. 83/2026)", "Il permesso di soggiorno è rilasciato, rinnovato o convertito entro", ["--note","'novanta giorni' follows on the next line in double brackets (D.Lgs. 83/2026, from 22 May 2026); conflicts with integrazionemigranti page (60 days), which predates it"]),
 ("a5-83", "normattiva-tui-art5", "D.Lgs. 16 April 2026 n. 83 amendments apply from 22 May 2026", "Le disposizioni di cui al presente decreto si applicano a decorrere dal 22 maggio 2026", []),
 ("a5-fake", "normattiva-tui-art5", "Forging or using a forged visa, permit or contract of stay, or forging documents to obtain one, carries 1 to 6 years' prison", "è punito con la reclusione da uno a sei anni", []),
 ("a5-auto", "normattiva-tui-art5", "Self-employment permit: up to 2 years; renewals up to 3 years", "Il permesso di soggiorno non può avere validità superiore ad un periodo di due anni", []),
 ("a5bis", "normattiva-tui-art5bis", "The contract of stay contains the employer's guarantee of housing and commitment to pay the worker's return travel", "l'impegno al pagamento da parte del datore di lavoro delle spese di viaggio per il rientro del lavoratore nel Paese di provenienza", []),
 ("a5bis-h", "normattiva-tui-art5bis", "The employer guarantees housing meeting minimum standards", "la garanzia da parte del datore di lavoro della disponibilità di un alloggio per il lavoratore", []),
 # Art 9 long-term
 ("a9-5y", "normattiva-tui-art9", "After 5 years with a valid permit and income at least the annual assegno sociale, a worker can apply to the Questura for the EU long-term residence permit", "in possesso, da almeno cinque anni, di un permesso di soggiorno in corso di validità", ["--visa","EU long-term permit","--field","eligibility","--value","5 years legal stay"]),
 ("a9-inc", "normattiva-tui-art9", "Income must be at least the annual amount of the assegno sociale", "un reddito non inferiore all'importo annuo dell'assegno sociale", []),
 ("a9-10y", "normattiva-tui-art9", "The long-term permit is issued within 90 days, valid 10 years and renewed automatically", "è rilasciato entro novanta giorni dalla richiesta, è valido per dieci anni", []),
 ("a9-lang", "normattiva-tui-art9", "It requires passing an Italian language test", "test di conoscenza della lingua italiana", []),
 # Art 24 conversion
 ("a24-conv", "normattiva-tui-art24", "A seasonal worker with at least 3 months of regular work who is offered a fixed-term or permanent job can ask the SUI to convert to a non-seasonal work permit", "ha svolto regolare attività lavorativa sul territorio nazionale per almeno tre mesi", []),
 # Art 27, 27-quater
 ("a27-list", "normattiva-tui-art27", "Out-of-quota categories include managers and highly specialised staff, university teachers, translators, seafarers, posted workers, artists, athletes, journalists, digital nomads and nurses", "infermieri professionali assunti presso strutture sanitarie pubbliche e private", []),
 ("a27-dn", "normattiva-tui-art27", "Digital nomads and remote workers are an out-of-quota category", "nomadi digitali e lavoratori da remoto", []),
 ("bc-out", "normattiva-tui-art27quater", "The EU Blue Card (highly qualified work) is outside the quotas", "al di fuori delle quote di cui all'articolo 3, comma 4, agli stranieri, di seguito denominati lavoratori stranieri altamente qualificati", ["--visa","EU Blue Card","--field","quota","--value","outside quota"]),
 ("bc-deg", "normattiva-tui-art27quater", "Qualifies with a tertiary degree of at least three years", "percorso di istruzione superiore di durata almeno triennale", []),
 ("bc-5y", "normattiva-tui-art27quater", "Or with at least five years of relevant professional experience at a comparable level", "almeno cinque anni di esperienza professionale di livello paragonabile", []),
 ("bc-ict", "normattiva-tui-art27quater", "ICT managers and specialists: three years' experience in the previous seven", "almeno tre anni di esperienza professionale pertinente acquisita nei sette anni precedenti", []),
 ("bc-6m", "normattiva-tui-art27quater", "Needs a contract or binding offer of at least six months", "offerta di lavoro vincolante della durata di almeno sei mesi", []),
 ("bc-pay", "normattiva-tui-art27quater", "Pay must be at least the national contract level and the ISTAT average gross annual pay", "non inferiore alla retribuzione media annuale lorda come rilevata dall'ISTAT", []),
 ("bc-30", "normattiva-tui-art27quater", "The SUI issues or refuses the Blue Card nulla osta within 30 days", "giorni dalla presentazione della domanda ovvero, entro il medesimo termine, comunica al datore di lavoro il rigetto", ["--note","'trenta' (30) is on the previous line, in double brackets (Law 182/2025)"]),
 ("bc-12", "normattiva-tui-art27quater", "In the first 12 months a change of employer needs prior authorisation from the labour office", "I cambiamenti di datore di lavoro nel corso dei primi dodici mesi sono soggetti all'autorizzazione preliminare", []),
 ("bc-fam", "normattiva-tui-art27quater", "A Blue Card holder can bring family regardless of permit length", "indipendentemente dalla durata del suo permesso di soggiorno", []),
 # Art 26 self-employment
 ("a26-res", "normattiva-tui-art26", "A self-employed applicant must show adequate resources, the professional requirements, and a certificate from the competent authority no older than three months", "di essere in possesso di una attestazione dell'autorità competente in data non anteriore a tre mesi", []),
 ("a26-inc", "normattiva-tui-art26", "They must show suitable housing and lawful annual income above the health-charge exemption threshold", "di un reddito annuo, proveniente da fonti lecite", []),
 ("a26-120", "normattiva-tui-art26", "The self-employment visa is decided within 120 days and must be used within 180 days of issue", "deve essere rilasciato o negato entro centoventi giorni", []),
 # Embassy / VFS
 ("emb-susp", "ambdhaka-news-2804", "In October 2024 Italy suspended all nulla osta issued to Bangladeshis pending verification because of a high number of false documents; the Embassy returned passports from 20 October 2024", "Due to the high number of false and counterfeit documents, the Italian Government has suspended the validity of all", []),
 ("emb-noexp", "ambdhaka-news-2804", "Suspended work nulla osta do not expire while awaiting SUI confirmation", "Work Nulla Osta will not expire pending confirmation", []),
 ("emb-askemp", "ambdhaka-news-2804", "The Embassy says verification is done in Italy and holders should ask their employer for updates", "Nulla Osta holders might want to contact their prospective employers in Italy for updates", []),
 ("amb-10k", "ambdhaka-ambassador-interview-kalerkantho-2026-09", "About 10,000 work visas were issued to Bangladeshis in 2025, with a similar number expected in 2026", "Approximately 10,000 work visas were issued in 2025, and we expect a similar number in 2026", []),
 ("amb-fast", "ambdhaka-ambassador-interview-kalerkantho-2026-09", "Fresh authorisations for Bangladeshis are processed in a relatively short time", "fresh authorisations issued to Bangladeshi citizens are being processed within a relatively short period of time", []),
 ("amb-rej", "ambdhaka-ambassador-interview-kalerkantho-2026-09", "Rejection rate on fresh authorisations is very small", "In fact, the rejection rate is very small, and processing times are limited", []),
 ("amb-old", "ambdhaka-ambassador-interview-kalerkantho-2026-09", "Old authorisations suspended in October 2024 were put on hold and eventually rejected in large numbers", "were put on hold for some time and eventually rejected in large numbers", []),
 ("amb-apost", "ambdhaka-ambassador-interview-kalerkantho-2026-09", "Bangladesh and Italy are both parties to the Apostille Convention", "the Apostille Convention", []),
 ("amb-train", "ambdhaka-ambassador-interview-kalerkantho-2026-09", "Pre-departure vocational training projects run in Bangladesh; several hundred Bangladeshi workers a year now go legally through this route", "several hundred Bangladeshi workers are now going to Italy legally every year", []),
 ("amb-fam", "ambdhaka-ambassador-interview-kalerkantho-2026-09", "About 12,000 to 13,000 family reunification visas are issued each year", "approximately 12,000 to 13,000 being issued every year", []),
 ("mou2025", "ambdhaka-political-consultations-2026-08", "Italy and Bangladesh signed a Memorandum of Understanding on migration and mobility in 2025; Decreto Flussi is the framework for regular channels", "the Memorandum of Understanding on migration and mobility signed in 2025", []),
 ("vfs-only", "ambdhaka-where-to-apply", "Visa applications for Italy are filed only at VFS Global (info.itbd@vfshelpline.com, +880 9606777666)", "Visa Applications for Italy can be filed exclusively at the VFS Global", []),
 ("vfs-dhaka", "ambdhaka-where-to-apply", "VFS Dhaka: Nafi Tower (4th and 5th floor), 53 South Gulshan Avenue, Gulshan 1", "Nafi Tower (4th & 5th Floor), 53, South Gulshan Avenue, Gulshan 1, Dhaka 1212", []),
 ("vfs-ctg", "ambdhaka-where-to-apply", "VFS Chattogram: World Trade Center, 102/103 Agrabad CA", "World Trade Center Chittagong, (Quinto Piano), 102/103 Agrabad CA", []),
 ("vfs-syl", "ambdhaka-where-to-apply", "VFS Sylhet: Nirvana Inn Complex, Ramer Dighir Par, Mirzajungle Road", "Nirvana Inn Complex, Ramer Dighir Par, Mirzajungle Road, Sylhet- 3100", []),
 ("vfs-hrs", "ambdhaka-where-to-apply", "Visa applications are taken Sunday to Thursday, 9:00 to 12:00", "Sundays to Thursdays from 9:00 AM to  12:00 PM", []),
 ("vfs-tr", "ambdhaka-where-to-apply", "The Embassy lists authorised translators: Tradusoft (01776015230), EXINSO Ltd (01797-412712), Prof. Stefania Chiapello", "Tradusoft.com Translation Agency", []),
 ("vfs-forg", "ambdhaka-where-to-apply", "Forging documents, signatures and seals is a prosecuted crime", "The forgery of documents, signatures and seals is a crime prosecuted", []),
 ("emb-mail", "ambdhaka-where-to-apply", "Visa procedure questions: visti.dhaka@esteri.it", "visti.dhaka@esteri.it", []),
 ("fee-d", "ambdhaka-visa-cost", "A national (type D) visa costs EUR 116, paid in cash in taka", "**National Visas (Type “D”):** 116 euros", ["--visa","Decreto Flussi","--field","visa fee","--value","EUR 116 in BDT cash"]),
 ("fee-bdt", "ambdhaka-visa-cost", "Visa fees are paid in cash in local currency", "For all visas the payment is processed in cash in local currency (BDT)", []),
 ("ck-df", "ambdhaka-choose-visa", "The Embassy lists separate checklists for Decreto Flussi, seasonal, Blue Card, Art. 23 and self-employment work visas", "Decreto Flussi (Decree on Immigration Flows)", []),
 ("ck-form", "ambdhaka-checklist-decreto-flussi-2026-07", "Decreto Flussi visa: original national (D) visa form in English or Italian, signed", "National (\"D\"-Type) visa application form, original", []),
 ("ck-photo", "ambdhaka-checklist-decreto-flussi-2026-07", "One recent ICAO photo, 3.5 x 4.0 cm, white background, taken in the last 6 months", "Photos must be ICAO format (3.5 x4.0 cm, color photo with white background, taken", []),
 ("ck-pass", "ambdhaka-checklist-decreto-flussi-2026-07", "Passport valid at least 3 months beyond the visa's expiry, with two blank pages, plus a copy of the bio page", "Passport must be valid for at least additional three months from the date of expiry of the", []),
 ("ck-no", "ambdhaka-checklist-decreto-flussi-2026-07", "Copy of the nulla osta; check name, surname, gender and date of birth are correct to avoid long delays", "applicant are correct on the aforesaid \"Nulla Osta\" (name, surname, gender and date of", []),
 ("ck-exp", "ambdhaka-checklist-decreto-flussi-2026-07", "Proof of work experience or qualification for the job sector", "Documents and certificates related to the job sector the applicant is going to work in Italy.", []),
 ("ck-conf", "ambdhaka-checklist-decreto-flussi-2026-07", "After the visa application, the SUI asks the employer to confirm the job offer, within 15 days", "and must be provided within 15 days.", []),
 ("ck-one", "ambdhaka-checklist-decreto-flussi-2026-07", "One applicant cannot submit more than one visa application at a time, even with two passports", "The same applicant cannot submit more than one visa application at the same time", []),
 ("ck-extra", "ambdhaka-checklist-decreto-flussi-2026-07", "The Embassy may ask for extra documents", "The Embassy reserves itself the right to request any supplementary document not", []),
 ("bcck-18", "ambdhaka-checklist-bluecard-2026-07", "Blue Card visa: passport valid at least 18 months", "Passport must be valid for at least 18 months from the date of application", []),
 ("bcck-dov", "ambdhaka-checklist-bluecard-2026-07", "Blue Card visa: a 3-year degree with dichiarazione di valore or CIMEA certificate, or 5 years' experience proven by translated and apostilled contracts or payslips", "least three years. The documentation must be accompanied by the declaration of value issued by the Italian", []),
 ("bcck-only", "ambdhaka-checklist-bluecard-2026-07", "This visa is strictly reserved for highly qualified workers recruited for highly qualified jobs", "Important advise: this particular type of visa is strictly reserved for highly qualified workers, who are", []),
 ("a23ck", "ambdhaka-checklist-art23-2026-07", "Art. 23 visa needs proof of completing vocational and civic-language training in Bangladesh under programmes approved by Italian ministries", "training and civic-linguistic activities in their country of origin as provided for by", []),
 ("seck-q", "ambdhaka-checklist-selfemployment-2026-07", "Self-employment visa (consultants): a Questura nulla osta issued within 90 days before applying", "that must have been issued before 90 days prior of submission of the visa application", []),
 ("seck-3y", "ambdhaka-checklist-selfemployment-2026-07", "The Italian company must have been active at least three years", "Statement that the company has been active for at least the last three years according", []),
 ("seck-8500", "ambdhaka-checklist-selfemployment-2026-07", "The company must guarantee pay of at least EUR 8,500", "applicant a wage of minimum UR 8.500", []),
 ("seck-bank", "ambdhaka-checklist-selfemployment-2026-07", "Applicant needs 6 months of personal bank statements from a bank in Bangladesh", "Personal bank statement issued by any bank operating in Bangladesh covering the last 6", []),
 ("seck-nikah", "ambdhaka-checklist-selfemployment-2026-07", "Married applicants: nikahnama translated into English and apostilled, only one apostille per document", "For married applicants: marriage certificate (e.g. \"Nikah Nama\" for Muslims or marriage act", []),
 ("webform", "vfs-italy-bd-notice-work-visa-webform-2025-03", "Since 3 April 2025 Decreto Flussi work visa applicants with a nulla osta issued on or after 22 October 2024 register on VFS's webform", "work visa applications will start on 3rd April 2025, through the new webform system for Italy in Bangladesh", [ "--note", VFSNOTE]),
 ("webform-exp", "vfs-italy-bd-notice-work-visa-webform-2025-03", "Successful registration on the webform suspends the expiry of the nulla osta", "successful registration on the portal will suspend the expiration of the Nulla Osta", ["--note", VFSNOTE]),
 ("webform-old", "vfs-italy-bd-notice-work-visa-webform-2025-03", "Holders of nulla osta issued before 22 October 2024 request an appointment by email at work.appointment@vfsglobal.com with name, date of birth, passport, mobile, email and nulla osta number", "Applicants with Nulla Osta issued before this date can still request an appointment via email", ["--note", VFSNOTE]),
 ("webform-url", "vfs-italy-bd-webform-login", "The webform (vfseu.mioot.com/forms/ITABDE) uses an email one-time password, and lets applicants check status after submission", "If you have not registered yet, please enter you email id to receive the OTP", ["--note", VFSNOTE]),
 ("ln-walk", "vfs-italy-bd-ln-nulla-osta-walkin-2026-08", "Since August 2026, holders of an L/N (Article 27) nulla osta walk in to a VFS centre with a hard copy of the nulla osta and a passport copy; the Embassy verifies it before giving an appointment", "Applicants may visit the Visa Application Centre on a walk-in basis and submit", ["--note", VFSNOTE]),
 ("ln-verify", "vfs-italy-bd-ln-nulla-osta-walkin-2026-08", "Once the Embassy validates the L/N nulla osta the applicant gets an email with the submission date", "Once the Embassy has validated the Nulla Osta, applicants will receive an email", ["--note", VFSNOTE]),
 ("vfsbc", "vfs-italy-bd-bluecard-2026-02", "VFS checklist warns the L/N visa is only for highly qualified workers (Embassy communique of 31 August 2025)", "Important advise: this particular type of visa is strictly reserved for highly qualified workers", ["--note", VFSNOTE]),
 # Questura kit
 ("kit-docs", "questure-poliziadistato-kit-postale-documenti", "First work permit kit: contract of stay, codice fiscale copy, hospitality declaration and rental contract, passport copy (all pages with data, visas, stamps)", "contratto di soggiorno stipulato presso lo Sportello Unico per l'Immigrazione", []),
 ("kit-bollo", "questure-poliziadistato-kit-postale-documenti", "The kit needs a EUR 16 revenue stamp (marca da bollo)", "marca da bollo da  16", []),
 ("kit-fee", "questure-poliziadistato-kit-postale-documenti", "Postal payment slip: EUR 70.46 for permits up to 1 year, EUR 80.46 for over 1 and up to 2 years", "Bollettino postale di  70,46 per permessi di soggiorno di durata inferiore o pari ad", ["--visa","Decreto Flussi","--field","permit fee","--value","EUR 70.46 (<=1y) / 80.46 (1-2y) + EUR 16 stamp"]),
 ("kit-fee2", "questure-poliziadistato-kit-postale-documenti", "EUR 80.46 for permits over 1 year up to 2 years", "80,46 per permessi di soggiorno di durata superiore ad 1", []),
 ("kit-lt", "questure-poliziadistato-kit-postale-documenti", "Long-term EU permit kit: EUR 130.46 slip plus Italian language test, housing suitability certificate and income", "Bollettino postale  130,46", []),
 ("kit-unilav", "questure-poliziadistato-kit-postale-documenti", "Work permit kit includes the UNILAV (hiring notice) and tax return or CUD", "copia modello UNILAV", []),
 # integrazionemigranti
 ("im-confirm", "integrazionemigranti-ingressi-soggiorno-lavoro-novita", "The SUI sends the employer a PEC (certified email) asking it to confirm the hiring; only a positive confirmation lets the visa go ahead", "trasmette al datore di lavoro via PEC una richiesta di conferma", []),
 ("im-60from", "integrazionemigranti-ingressi-soggiorno-lavoro-novita", "Since DL 146/2025 the 60-day term runs from allocation to the quota, which happens when the Ministry of Labour splits quotas (within 10 days of click day)", "dalla data di imputazione della stessa alle quote", []),
 ("im-cs-ali", "integrazionemigranti-ingressi-soggiorno-lavoro-novita", "The signed contract of stay is uploaded to the SUI on the ALI portal", "Il contratto va poi trasmesso al SUI,", []),
 ("im-chron", "integrazionemigranti-ingressi-soggiorno-lavoro-novita", "On click day applications are mostly handled in order of arrival", "essendo le stesse prevalentemente trattate in ordine cronologico di arrivo", []),
 ("im-receipt", "integrazionemigranti-ingressi-soggiorno-lavoro-novita", "With the post-office receipt for a permit application the worker is lawfully present and may work while waiting", "il lavoratore straniero vada considerato regolarmente soggiornante nel territorio dello Stato e possa svolgere attivit", []),
 ("im-23-30", "integrazionemigranti-ingressi-soggiorno-lavoro-novita", "For Article 23 trained workers the nulla osta deadline is 30 days and the visa can be requested up to 12 months after the course (to end-2027)", "a **12 mesi** del tempo utile, dopo la fine del corso, per chiedere il visto", []),
 ("im-60days", "integrazionemigranti-ingressi-soggiorno-lavoro-novita", "The portal states permits are issued, renewed or converted within 60 days", "il permesso di soggiorno va rilasciato, rinnovato o convertito entro sessanta giorni dalla data in cui", ["--status","conflict","--note","conflicts with normattiva-tui-art5 (90 days after D.Lgs. 83/2026); this page predates that change"]),
]

IMGFACTS = [
 ("ln-hundreds", "ambdhaka-communique-ln-bluecard-2025-08", "The Embassy received hundreds of work visa applications with an L/N (Article 27, Blue Card) nulla osta; very few succeeded because applicants were not highly qualified", "Very few applicants of this type of visa in Bangladesh have so far been successful."),
 ("ln-brokers", "ambdhaka-communique-ln-bluecard-2025-08", "The Embassy warns against agents and brokers selling an 'L/N code carta blu' nulla osta; a valid L/N nulla osta does not guarantee a visa", "We advise the public not to become prey of agents and illegal brokers who promise a \"Nulla Osta L/N code - carta blu\""),
 ("susp-944", "ambdhaka-communique-suspended-nulla-osta-2025-09", "In September 2025, 944 suspended nulla osta had been confirmed for Bangladeshis who had not applied for a visa; VFS published the codes and ran walk-in days on 16 and 23 September 2025", "A total of 944 Nulla Osta have been confirmed by the competent Provincial Immigration Offices in Italy"),
]

def run(args):
    r = subprocess.run([sys.executable, T] + args, capture_output=True, text=True, encoding="utf-8")
    out = (r.stdout + r.stderr).strip()
    return r.returncode, out

if "--sources" in sys.argv:
    for n, pub, title, off, d in SOURCES:
        print(n, run(["source", "--name", n, "--publisher", pub, "--title", title, "--official", off, "--page-date", d]))
    sys.exit()

ids = {}
for key, n, claim, quote, extra in FACTS:
    status = st(D[n])
    if "--status" in extra:
        i = extra.index("--status"); status = extra[i+1]; extra = extra[:i] + extra[i+2:]
    args = ["add", "--prefix", "W", "--name", n, "--claim", claim, "--quote", quote, "--page-date", D[n], "--status", status] + extra
    code, out = run(args)
    print(key, code, out[-200:])
for key, n, claim, quote in IMGFACTS:
    args = ["add", "--prefix", "W", "--name", n, "--claim", claim, "--quote", quote, "--page-date", D[n], "--status", st(D[n]), "--no-quote-check", "--note", IMG.replace("<name>", n)]
    code, out = run(args)
    print(key, code, out[-200:])
