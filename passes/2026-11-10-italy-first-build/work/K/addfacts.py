import subprocess, sys
T = "../../../../tools/facts.py"

# name, publisher, title, official, page_date
SOURCES = [
    ("poste-guida-permesso-di-soggiorno", "Poste Italiane", "Permessi di soggiorno: come richiedere il permesso o la carta di soggiorno", "yes", "undated"),
    ("poliziadistato-articolo-225-permesso", "Polizia di Stato", "Il rilascio del permesso di soggiorno", "yes", "undated"),
    ("questure-poliziadistato-rilascio-ps-kit-postale-2024-05", "Polizia di Stato, Questura di Treviso (Ufficio Immigrazione)", "Documenti per il primo rilascio del permesso di soggiorno elettronico tramite kit postale", "yes", "2024-05-16"),
    ("vfs-italy-bd-visa-info", "VFS Global (Italy visa centre, Bangladesh)", "Italy visa information Bangladesh: visa types, fees and service charges", "yes", "undated"),
    ("normattiva-tui-art4bis-accordo-integrazione", "Normattiva", "D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 4-bis (Accordo di integrazione), text in force 10 Nov 2026", "yes", "2026-11-10"),
    ("normattiva-tui-art34-ssn", "Normattiva", "D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 34 (health service enrolment), text in force 10 Nov 2026", "yes", "2026-11-10"),
    ("normattiva-tui-art6", "Normattiva", "D.Lgs. 286/1998 (Testo Unico Immigrazione), art. 6, text in force 10 Nov 2026", "yes", "2026-11-10"),
    ("normattiva-dpr-179-2011-accordo-integrazione", "Normattiva", "D.P.R. 14 settembre 2011, n. 179 (Regolamento sull'accordo di integrazione), art. 1, text in force 10 Nov 2026", "yes", "2026-11-10"),
    ("normattiva-dpr-179-2011-art2", "Normattiva", "D.P.R. 179/2011 (accordo di integrazione), art. 2, text in force 10 Nov 2026", "yes", "2026-11-10"),
    ("normattiva-dpr-179-2011-art3", "Normattiva", "D.P.R. 179/2011 (accordo di integrazione), art. 3, text in force 10 Nov 2026", "yes", "2026-11-10"),
    ("normattiva-dpr-179-2011-art5", "Normattiva", "D.P.R. 179/2011 (accordo di integrazione), art. 5, text in force 10 Nov 2026", "yes", "2026-11-10"),
    ("normattiva-dpr-179-2011-art6", "Normattiva", "D.P.R. 179/2011 (accordo di integrazione), art. 6, text in force 10 Nov 2026", "yes", "2026-11-10"),
    ("agenziaentrate-mini-guida-codice-fiscale-stranieri", "Agenzia delle Entrate", "Mini guida codice fiscale per stranieri (page with the guide in 17 languages)", "yes", "undated"),
    ("agenziaentrate-codice-fiscale-stranieri-guida-en-2023", "Agenzia delle Entrate", "Tax code for foreign nationals (mini guide, English)", "yes", "2023-03-08"),
    ("comune-roma-iscrizione-anagrafica-come-presentare", "Roma Capitale", "Iscrizione anagrafica: come presentare richiesta", "yes", "2024-05-21"),
    ("comune-roma-iscrizione-anagrafica-extracomunitari", "Roma Capitale", "Iscrizione anagrafica cittadini extra comunitari", "yes", "2024-05-21"),
    ("comune-milano-residenza-documenti-extraue", "Comune di Milano", "Dichiarazione di residenza, Allegato A: documentazione per l'iscrizione anagrafica di cittadini di Stati non UE", "yes", "undated"),
    ("comune-milano-residenza-stranieri-modulistica", "Comune di Milano", "Modulistica: richiesta di residenza per persone straniere provenienti dall'estero", "yes", "2026-06-16"),
    ("comune-milano-residenza-stranieri-estero", "Comune di Milano", "Cambio di residenza per persone straniere provenienti dall'estero", "yes", "2026-07-27"),
    ("salute-assistenza-cittadini-extra-ue", "Ministry of Health (Italy)", "Assistenza ai cittadini dei Paesi extra UE in Italia", "yes", "2024-12-23"),
    ("aslroma1-assistenza-sanitaria-extracomunitari", "ASL Roma 1 (local health authority)", "Assistenza sanitaria ai cittadini non comunitari", "yes", "undated"),
    ("auslmodena-modulo-iscrizione-ssn-stranieri", "AUSL di Modena (local health authority)", "Modulo di iscrizione al SSN e scelta del medico per cittadini stranieri non UE", "yes", "undated"),
    ("aslroma3-iss-accesso-cure-persona-straniera", "Istituto Superiore di Sanita and Ministry of Health (Italy)", "L'accesso alle cure della persona straniera: indicazioni operative", "yes", "2013-12-31"),
    ("comune-roma-carta-identita-destinatari", "Roma Capitale", "Carta d'identita (maggiorenni): destinatari del servizio", "yes", "2026-06-03"),
    ("comune-roma-carta-identita-costi", "Roma Capitale", "Carta d'identita (maggiorenni): tempi di risposta e costi", "yes", "2026-06-03"),
    ("comune-roma-carta-identita-maggiorenni", "Roma Capitale", "Carta d'identita (maggiorenni): descrizione del servizio", "yes", "2026-06-03"),
    ("homobile-supporto-attivazione-sim", "ho. Mobile (mobile operator)", "SIM ho. Mobile: come la attivo", "no", "undated"),
    ("news-bdpratidin-italy-work-visa-vfs-registration-2025-12", "Bangladesh Pratidin (English)", "Italian embassy in Dhaka issues guidelines for work visa appointments", "no", "2025-12-08"),
    ("news-tbs-italy-seasonal-visa-backlogs", "The Business Standard", "Italy's seasonal work visa processing resumes for Bangladeshis amid backlogs", "no", "2025-08-11"),
    ("ngo-oxfamitalia-tempi-permessi-soggiorno-2024-03", "Oxfam Italia and 18 Florence organisations", "Siano ridotti i tempi per i permessi di soggiorno dei cittadini stranieri (press release)", "no", "2024-03-07"),
    ("ngo-openmigration-file-questure", "Open Migration", "Le file fuori al freddo per un diritto", "no", "2025-02-19"),
]

def st(name, date, off):
    if off == "no":
        return "unofficial"
    if date == "undated":
        return "possibly-outdated"
    return "verified" if date >= "2025-11-10" else "possibly-outdated"

D = {s[0]: (s[4], s[3]) for s in SOURCES}

FACTS = [
 # --- VFS fees and appointment (Step 5)
 ("vfs-fee", "vfs-italy-bd-visa-info", "For an Italian work visa applied for in Bangladesh, VFS Global charges a service charge of BDT 5,320 (EUR 38) on top of the visa fee", "| VFS Global Service Charge | 5320                  | 38           |", ["--visa","Decreto Flussi","--field","VFS service charge","--value","BDT 5320 (EUR 38)"]),
 ("vfs-visafee", "vfs-italy-bd-visa-info", "VFS lists the work visa fee as BDT 16,240 (EUR 116) or BDT 12,600 (EUR 90)", "| Visa Fee                  | 16240/12600           | 116/90       |", []),
 ("vfs-draft", "vfs-italy-bd-visa-info", "VFS lists a bank draft charge of BDT 270 for the work visa", "| Bank Draft Charge         | 270                   |              |", []),
 ("vfs-vat", "vfs-italy-bd-visa-info", "The VFS service fee includes 15% VAT", "VFS service fee is inclusive 15% VAT", []),
 ("vfs-rate", "vfs-italy-bd-visa-info", "VFS converts euro fees at the Embassy's rate, shown as 1 euro = 140 taka", "Exchange rate - 1 Euro = 140", []),
 ("vfs-logistic", "vfs-italy-bd-visa-info", "The VFS fee includes free SMS and email notification, photocopies, photo booth and form-filling help", "Logistic fee includes free SMS, e-mail notification, photocopy, photobooth,, form filling assistance", []),
 ("vfs-nulla", "vfs-italy-bd-visa-info", "A nulla osta is mandatory to apply for an Italian work visa", "A Nulla Osta as the authorization of applying for this visa is a mandatory document.", []),
 ("vfs-biom", "vfs-italy-bd-visa-info", "Applicants for a long-term (D) visa are exempt from giving fingerprints at VFS", "Applicants applying for long term visa are exempted from giving fingerprints.", []),
 ("vfs-photos", "vfs-italy-bd-visa-info", "VFS asks for four recent 4.0 x 3.5 cm colour photos with white background", "Four recent 4.0\\*3.5 cm size color photograph", []),
 ("bdp-register", "news-bdpratidin-italy-work-visa-vfs-registration-2025-12", "In December 2025 the Embassy said holders of a 2025 work nulla osta must register on the VFS portal and upload the nulla osta; the Embassy verifies it and gives an appointment within a few days", "After registration, the embassy will verify the Nulosta and provide an appointment within a few days.", []),
 ("bdp-2324", "news-bdpratidin-italy-work-visa-vfs-registration-2025-12", "Holders of a 2023 or 2024 nulla osta were told to wait for the Italian immigration office's review; VFS contacts them afterwards", "Once the review is concluded, VFS Global will reach out to those applicants for further steps.", []),
 ("tbs-fees", "news-tbs-italy-seasonal-visa-backlogs", "The Embassy reminded migrants that only official fees apply and that paying intermediaries risks visa cancellation and legal action", "The Italian Embassy reminded migrants that only official fees apply.", []),
 ("tbs-backlog", "news-tbs-italy-seasonal-visa-backlogs", "By August 2025 over 8,000 of nearly 40,000 pending nulla osta cases had been resolved", "over 8,000 of nearly 40,000 pending cases are resolved", []),
 # --- Permit kit (Step 7)
 ("po-8days", "poste-guida-permesso-di-soggiorno", "A non-EU national staying over three months must apply for the permesso di soggiorno within 8 days of entering Italy", "entro 8 giorni dal tuo ingresso in Italia", []),
 ("po-sui", "poste-guida-permesso-di-soggiorno", "A worker with a nulla osta applying for a first work permit goes to the SUI at the Prefettura, which fills in the application and hands it over in an envelope", "Se hai il nullaosta e chiedi il rilascio del permesso di soggiorno per lavoro o per motivi di famiglia, rivolgiti allo Sportello Unico Immigrazione (SUI) presso la Prefettura. Una volta compilata la domanda te ne consegneranno una copia", []),
 ("po-post", "poste-guida-permesso-di-soggiorno", "The completed application is then handed in at a post office in the Sportello Amico network", "dovrai presentarla domanda presso uno degli Uffici Postali abilitati", []),
 ("po-kitgialla", "poste-guida-permesso-di-soggiorno", "The application kit has a yellow band and is available at all post offices; only one kit per person", "kit a banda gialla disponibile in tutti gli Uffici Postali", []),
 ("po-patronati", "poste-guida-permesso-di-soggiorno", "Some comuni and authorised patronati fill in the kit free of charge", "Chiedere l’assistenza gratuita e qualificata di alcuni Comuni e Patronati abilitati alla compilazione", []),
 ("po-open", "poste-guida-permesso-di-soggiorno", "The kit is handed in open, with passport and copies of all documents", "La domanda compilata deve essere consegnata in busta aperta", []),
 ("po-copies", "poste-guida-permesso-di-soggiorno", "Copies of the passport pages with personal data and entry/exit visas must be attached in A4 format", "sono necessarie le pagine contenenti i dati anagrafici", []),
 ("po-16", "poste-guida-permesso-di-soggiorno", "Costs: EUR 16 revenue stamp (marca da bollo), bought at tobacconists", "**16 euro** per la marca da bollo", ["--visa","Decreto Flussi","--field","permit revenue stamp","--value","EUR 16"]),
 ("po-30", "poste-guida-permesso-di-soggiorno", "Costs: EUR 30.00 paid to the post office clerk when handing in the application", "**30,00 euro** all'operatore dell'ufficio postale", ["--visa","Decreto Flussi","--field","post office fee for permit kit","--value","EUR 30.00"]),
 ("po-3046", "poste-guida-permesso-di-soggiorno", "Costs: EUR 30.46 for producing the electronic permit card, plus any contribution due", "**30,46 euro** per la produzione di Permesso o Carta di Soggiorno", ["--visa","Decreto Flussi","--field","permit card production fee","--value","EUR 30.46"]),
 ("po-onebollettino", "poste-guida-permesso-di-soggiorno", "The card fee and contribution are paid together on one postal payment slip (bollettino) per applicant, available at post offices", "dovrai utilizzare un unico ed apposito bollettino di conto corrente per ogni richiedente", []),
 ("po-receipt", "poste-guida-permesso-di-soggiorno", "The clerk gives a receipt proving the application, with codes to follow it on PortaleImmigrazione.it", "Una ricevuta di presentazione della domanda", []),
 ("po-circolare", "poste-guida-permesso-di-soggiorno", "The receipt lets the holder move around in Italy and must be kept with the passport", "Questa ricevuta ti consente di circolare in Italia", []),
 ("po-convoc", "poste-guida-permesso-di-soggiorno", "The clerk also gives a letter calling the worker to the Questura with date, time and place", "Una lettera di convocazione in Questura", []),
 ("po-racc", "poste-guida-permesso-di-soggiorno", "If no Questura appointment can be set, the letter says it will be sent by registered post to the Italian address in the application", "che ti verrà inviata una raccomandata, all’indirizzo italiano che ha dichiarato nella domanda", []),
 ("po-status", "poste-guida-permesso-di-soggiorno", "After the fingerprint appointment the permit's status can be checked on poliziadistato.it", "successivamente al giorno dell’appuntamento in Questura in cui saranno effettuati i rilievi fotodattiloscopici (impronte digitali)", []),
 ("po-tel", "poste-guida-permesso-di-soggiorno", "Free number 800.200.309 (Monday to Saturday, 8:00-20:00) gives Sportello Amico addresses and application status", "attivo dal lunedì al sabato, esclusi i festivi, dalle 8:00 alle 20:00", []),
 ("po-booking", "poste-guida-permesso-di-soggiorno", "A post office slot can be booked on poste.it or the Poste Italiane app", "prenota su poste.it o su App Poste Italiane", []),
 ("po-only", "poste-guida-permesso-di-soggiorno", "The post office accepts only applications presented by the person concerned", "esclusivamente dai soggetti direttamente interessati", []),
 ("tv-contrib", "questure-poliziadistato-rilascio-ps-kit-postale-2024-05", "For a work permit with a visa from abroad, the postal slip covers the EUR 30.46 card plus a contribution of EUR 40 (permit up to 1 year) or EUR 50 (over 1 and up to 2 years)", "per permessi di soggiorno di durata superiore ad 1 anno o pari a 2 anni", ["--visa","Decreto Flussi","--field","permit contribution","--value","EUR 40 (<=1 yr) / EUR 50 (1-2 yrs)"]),
 ("tv-docs", "questure-poliziadistato-rilascio-ps-kit-postale-2024-05", "Work-permit kit (visa from abroad) must include a copy of the nulla osta and of the contratto di soggiorno signed at the SUI", "copia del contratto di soggiorno stipulato presso lo Sportello Unico per l'Immigrazione della Prefettura-", []),
 ("tv-dimora", "questure-poliziadistato-rilascio-ps-kit-postale-2024-05", "Every kit needs proof of current address: a residence certificate or a hospitality declaration (dichiarazione di ospitalita/cessione di fabbricato)", "certificazione attestante l'attuale dimora", []),
 ("tv-cf", "questure-poliziadistato-rilascio-ps-kit-postale-2024-05", "A copy of the codice fiscale is needed only if already held", "copia del codice fiscale solo se gi", []),
 ("tv-photos", "questure-poliziadistato-rilascio-ps-kit-postale-2024-05", "At the Questura appointment bring the original postal receipt, the appointment, 4 passport photos, the original passport and originals of all copied documents", "4 fototessere del richiedente", []),
 ("tv-receipt", "questure-poliziadistato-rilascio-ps-kit-postale-2024-05", "Bring the original receipt of the insured post (assicurata) used to send the kit", "originale della ricevuta dell'assicurata postale della spedizione del kit", []),
 ("tv-accordo", "questure-poliziadistato-rilascio-ps-kit-postale-2024-05", "For a work permit the integration agreement is signed at the SUI", "E' prevista la stipula dell'Accordo di Integrazione presso lo Sportello Unico per l'Immigrazione", []),
 ("pz-8lav", "poliziadistato-articolo-225-permesso", "Someone arriving for the first time has 8 working days from entry to apply for the permesso di soggiorno", "8 giorni lavorativi dal suo ingresso", []),
 ("pz-fingers", "poliziadistato-articolo-225-permesso", "The permit is an electronic card with the holder's photo and fingerprints, issued by the Questura after identity checks", "l'immagine del volto anche le impronte", []),
 ("pz-cf", "poliziadistato-articolo-225-permesso", "The card shows the holder's codice fiscale and the reason for stay", "q il codice fiscale;", []),
 ("pz-60", "poliziadistato-articolo-225-permesso", "Polizia di Stato says first issue and renewal take on average 60 days from application", "avviene, in media, in 60 giorni dalla data di", ["--status","conflict","--note","average stated by Polizia; legal maximum is now 90 days under art. 5 TUI after D.Lgs. 83/2026 (see W0063)"]),
 ("pz-rights", "poliziadistato-articolo-225-permesso", "The receipt for a first work-permit application gives the same rights as holding the permit", "ha i medesimi diritti connessi al possesso del permesso di soggiorno", []),
 ("pz-work", "poliziadistato-articolo-225-permesso", "While waiting for the first work permit the worker may work unless the police notify grounds for refusal, to the worker and the employer", "lavorativa fino ad un'eventuale comunicazione, da parte dell'Autorit", []),
 ("pz-accordo", "poliziadistato-articolo-225-permesso", "Anyone applying for a permit of at least one year must sign an integration agreement with the Italian state", "tenuto a stipulare con lo Stato italiano un accordo di integrazione", []),
 ("pz-40", "poliziadistato-articolo-225-permesso", "Contribution set by decree of 5 May 2017: EUR 40 for permits over 3 months up to 1 year", "40,00 per i permessi di soggiorno di durata superiore a tre mesi e inferiore o pari a un anno", []),
 ("pz-50", "poliziadistato-articolo-225-permesso", "Contribution: EUR 50 for permits over 1 year up to 2 years", "euro 50,00 per i permessi di soggiorno di durata superiore a un anno e inferiore o pari a due", []),
 ("pz-100", "poliziadistato-articolo-225-permesso", "Contribution: EUR 100 for the EU long-term permit and for managers and specialised workers under art. 27", "euro 100,00 per il rilascio del permesso di soggiorno UE", []),
 ("pz-3y", "poliziadistato-articolo-225-permesso", "Permits for permanent employment can last up to three years (circular of 1 June 2023)", "fino a tre anni per lavoro autonomo, per lavoro subordinato a tempo indeterminato", []),
 # --- Codice fiscale
 ("cf-sui", "agenziaentrate-codice-fiscale-stranieri-guida-en-2023", "Foreign nationals coming for work or family reunification get their tax code from the SUI (Immigration Desk) at the Prefecture", "by the Immigration Desk, operating in every", []),
 ("cf-prov", "agenziaentrate-codice-fiscale-stranieri-guida-en-2023", "The SUI assigns a provisional numerical tax code; the permanent one (letters and numbers) comes when the permit is issued", "The Immigration Desk will assign a provisional", []),
 ("cf-prov2", "agenziaentrate-codice-fiscale-stranieri-guida-en-2023", "The permanent code is assigned when the residence permit is issued", "issued, the foreign national is then assigned the", []),
 ("cf-asl", "agenziaentrate-codice-fiscale-stranieri-guida-en-2023", "The tax code is needed to register with the local health authority (ASL) and choose a general practitioner", "the Local Health Authority (ASL) and choose the", []),
 ("cf-noexp", "agenziaentrate-codice-fiscale-stranieri-guida-en-2023", "The tax code is valid only when issued by the Revenue Agency and does not expire", "by the Revenue Agency and does not expire.", []),
 ("cf-dup", "agenziaentrate-codice-fiscale-stranieri-guida-en-2023", "If two people's data produce the same code, the SUI or Questura sends the person to any Revenue Agency office for a permanent code", "will invite the citizen in question to go to any office", []),
 ("cf-aa48", "agenziaentrate-codice-fiscale-stranieri-guida-en-2023", "Legally resident foreigners without a tax code apply at any Revenue Agency office with form AA4/8 and a valid permit or passport with visa", "to submit the form AA4/8, filled in and signed, and", []),
 ("cf-bn", "agenziaentrate-mini-guida-codice-fiscale-stranieri", "The Revenue Agency publishes its tax-code guide for foreigners in Bengali, among 17 languages", "Mini guida codice fiscale per stranieri (bengalese)", []),
 # --- Residence registration
 ("rm-obbligo", "comune-roma-iscrizione-anagrafica-extracomunitari", "Non-EU citizens with a regular permit who live habitually in Rome must request registration in the anagrafe (population register)", "che hanno la propria dimora abituale nel territorio di Roma Capitale, hanno l’obbligo di richiedere l’iscrizione anagrafica", []),
 ("rm-2days", "comune-roma-iscrizione-anagrafica-extracomunitari", "The registrar records the registration within two working days; legal effects start from the date of the declaration", "nei due giorni lavorativi successivi alla presentazione delle dichiarazioni", []),
 ("rm-docs-waiting", "comune-roma-iscrizione-anagrafica-come-presentare", "A worker who has applied for but not yet received the work permit registers with: valid passport, permit-application receipt, SUI nulla osta, contratto di soggiorno signed at the SUI, and codice fiscale", "contratto di soggiorno stipulato presso lo Sportello unico per l’immigrazione;", []),
 ("rm-receipt", "comune-roma-iscrizione-anagrafica-come-presentare", "Rome lists the permit-application receipt among documents for people who have applied but not received the permit", "coloro che hanno chiesto il permesso di soggiorno ma non lo hanno ancora ricevuto", []),
 ("rm-host", "comune-roma-iscrizione-anagrafica-come-presentare", "If other people already live in the flat, the existing resident must declare acceptance (with ID copy) or come to the counter", "dichiarazione di accettazione al domicilio", []),
 ("rm-how", "comune-roma-iscrizione-anagrafica-come-presentare", "The ministerial residence form can be handed in at the Municipio in person, by PEC or ordinary email, or by registered letter", "tramite Posta Elettronica Certificata o posta elettronica ordinaria", []),
 ("rm-free", "comune-roma-iscrizione-anagrafica-come-presentare", "Residence registration in Rome is free", "Costo del servizio:", []),
 ("rm-renew", "comune-roma-iscrizione-anagrafica-come-presentare", "After each permit renewal, residents must renew their declaration of habitual residence within 60 days in person", "entro 60 giorni devono rinnovare all’ufficiale di anagrafe la dichiarazione di dimora abituale", []),
 ("rm-cancel", "comune-roma-iscrizione-anagrafica-come-presentare", "Failure to renew leads to removal from the register one year after the permit expires, after a 30-day warning", "trascorso un anno dalla scadenza del permesso di soggiorno, previo avviso da parte dell’ufficio a provvedere nei successivi 30 giorni, la cancellazione", []),
 ("mi-online", "comune-milano-residenza-stranieri-estero", "In Milan, people arriving from abroad apply for residence online, uploading the documents", "che ti serviranno da inserire nella domanda online e poi procedi con la richiesta", []),
 ("mi-email", "comune-milano-residenza-stranieri-modulistica", "Milan does not accept documents sent by email; files up to 7MB are uploaded on the platform", "eventuali file inviati via e-mail non verranno presi in considerazione", []),
 ("mi-waiting", "comune-milano-residenza-documenti-extraue", "Milan list for a worker awaiting the first work permit: passport, contratto di soggiorno, post-office receipt, the permit application filed at the SUI, and codice fiscale", "Cittadino in attesa del rilascio del primo permesso di soggiorno per lavoro subordinato", []),
 ("mi-receipt", "comune-milano-residenza-documenti-extraue", "Milan requires the post-office receipt proving the permit application", "ricevuta rilasciata dall’ufficio postale attestante l’avvenuta presentazione della richiesta di", []),
 ("mi-guest", "comune-milano-residenza-stranieri-modulistica", "A guest attaches the host's or landlord's consent declaration with the host's details and the rental or ownership references", "Indicare i dati anagrafici del soggetto che ospita", []),
 ("tui6-anag", "normattiva-tui-art6", "Residence registration of lawfully staying foreigners follows the same conditions as for Italian citizens", "Le iscrizioni e variazioni anagrafiche dello straniero regolarmente soggiornante sono effettuate alle medesime condizioni dei cittadini italiani", []),
 # --- ID card
 ("cie-who", "comune-roma-carta-identita-destinatari", "Non-EU residents of Rome can get an identity card, valid only as ID and not for travel abroad", "ha esclusivamente valore di documento di riconoscimento e non costituisce titolo per l'espatrio", []),
 ("cie-docs", "comune-roma-carta-identita-destinatari", "Non-EU residents must show a valid ID document and an unexpired permit", "il permesso di soggiorno non scaduto, rilasciato dalla Questura competente", []),
 ("cie-cost", "comune-roma-carta-identita-costi", "In Rome the electronic identity card costs EUR 22.21 (EUR 16.79 state fee plus EUR 5.42 municipal charges)", "Il costo totale del rilascio è di € 22,21", ["--visa","All residents","--field","CIE cost Rome","--value","EUR 22.21"]),
 ("cie-6days", "comune-roma-carta-identita-costi", "The card is posted to the home address within 6 days", "a mezzo posta, entro 6 giorni", []),
 ("cie-book", "comune-roma-carta-identita-maggiorenni", "Appointments are booked on the Interior Ministry platform prenotazionicie.interno.gov.it", "https://www.prenotazionicie.interno.gov.it", []),
 # --- Health
 ("ssn-oblig", "normattiva-tui-art34-ssn", "Lawfully staying foreigners in employed or self-employed work must enrol in the SSN, with equal treatment to Italian citizens", "Hanno l'obbligo di iscrizione al Servizio sanitario nazionale", []),
 ("ssn-family", "normattiva-tui-art34-ssn", "Health cover extends to lawfully staying dependent family members", "L'assistenza sanitaria spetta altres", []),
 ("ssn-asl", "normattiva-tui-art34-ssn", "The insured foreigner is enrolled at the ASL of the comune where they live", "iscritto nella azienda sanitaria locale del comune in cui dimora", []),
 ("sal-where", "salute-assistenza-cittadini-extra-ue", "Enrol at the ASL of the comune of residence, or if not yet resident, of the address on the permit", "se non sei ancora residente, al Comune di domicilio effettivo indicato nel permesso di soggiorno", []),
 ("sal-4cred", "salute-assistenza-cittadini-extra-ue", "Enrolling lets you choose a GP (medico di base) and earns 4 credits for the integration agreement", "attribuzione di 4 crediti riconoscibili ai fini dell'accordo di integrazione", []),
 ("rm1-docs", "aslroma1-assistenza-sanitaria-extracomunitari", "ASL Roma 1 asks for: valid permit (or renewal application), self-certification of residence or address on the permit, codice fiscale, an undertaking to report changes, and the reason for the permit", "dichiarazione di impegno a comunicare ogni variazione del proprio status", []),
 ("rm1-dur", "aslroma1-assistenza-sanitaria-extracomunitari", "Enrolment ends when the permit expires or is revoked", "termina alla scadenza o revoca del permesso di soggiorno", []),
 ("mo-receipt", "auslmodena-modulo-iscrizione-ssn-stranieri", "AUSL Modena enrols a worker holding only the receipt of a work-permit application, with the employment contract or last payslip", "contratto di lavoro o ultima busta paga", []),
 ("mo-cf", "auslmodena-modulo-iscrizione-ssn-stranieri", "AUSL Modena asks for the codice fiscale issued by the Agenzia delle Entrate", "il codice fiscale rilasciato dall'Agenzia delle Entrate", []),
 ("iss-ts", "aslroma3-iss-accesso-cure-persona-straniera", "The tessera sanitaria (health card) is also given to a foreigner presenting the postal receipt of the permit application, with passport and visa", "postale attestante l'avvenuta presentazione della richiesta", []),
 ("iss-3m", "aslroma3-iss-accesso-cure-persona-straniera", "With only the receipt, enrolment is for up to 3 months, extendable", "per un periodo massimo di 3 mesi, prorogabili.", []),
 # --- SIM
 ("sim-cf", "homobile-supporto-attivazione-sim", "To activate a SIM online the operator asks for name, surname and codice fiscale and a video selfie with the ID document", "Inserisci i tuoi dati anagrafici (Nome, Cognome, Codice Fiscale)", []),
 # --- Integration agreement
 ("ai-cond", "normattiva-tui-art4bis-accordo-integrazione", "Signing the integration agreement, organised in credits, is a necessary condition for the permit", "rappresenta condizione necessaria per il rilascio del permesso di soggiorno", []),
 ("ai-loss", "normattiva-tui-art4bis-accordo-integrazione", "Losing all credits means revocation of the permit and expulsion (family-permit and long-term holders excepted)", "La perdita integrale dei crediti determina la revoca del permesso di soggiorno", []),
 ("ai-16", "normattiva-dpr-179-2011-accordo-integrazione", "The agreement applies to foreigners over 16 entering for the first time and applying for a permit of at least one year", "superiore ai sedici anni che fa ingresso per la prima volta nel territorio nazionale", []),
 ("ai-lang", "normattiva-dpr-179-2011-art2", "The worker gets a copy translated into a language they choose, or English, French, Spanish, Arabic, Chinese, Albanian, Russian or Filipino", "tradotto nella lingua da lui indicata", []),
 ("ai-sign", "normattiva-dpr-179-2011-art2", "The agreement is signed at the SUI or Questura when applying for the permit", "contestualmente alla presentazione della medesima istanza, stipula con lo Stato un accordo di integrazione", []),
 ("ai-16cred", "normattiva-dpr-179-2011-art2", "On signing, the worker is given 16 credits (A1 spoken Italian and basic civic knowledge)", "sono assegnati allo straniero sedici crediti", ["--visa","All permits of 1 year or more","--field","integration agreement starting credits","--value","16"]),
 ("ai-a2", "normattiva-dpr-179-2011-art2", "The worker commits to reach spoken Italian at least at level A2", "equivalente almeno al livello A2", []),
 ("ai-civ", "normattiva-dpr-179-2011-art2", "The worker commits to learn basics of the Constitution, public institutions and civil life (health, school, social services, work, tax)", "con particolare riferimento ai settori della sanità, della scuola, dei servizi sociali, del lavoro e agli obblighi fiscali", []),
 ("ai-kids", "normattiva-dpr-179-2011-art2", "The worker commits to send children to compulsory school", "garantire l'adempimento dell'obbligo di istruzione da parte dei figli minori", []),
 ("ai-2y", "normattiva-dpr-179-2011-art2", "The agreement lasts two years, extendable by one", "L'accordo ha la durata di due anni prorogabile di un altro anno", []),
 ("ai-session", "normattiva-dpr-179-2011-art3", "The free civic training and information session must be attended within three months of signing and lasts 5 to 10 hours", "entro i tre mesi successivi a quello di stipula dell'accordo", []),
 ("ai-hours", "normattiva-dpr-179-2011-art3", "The session lasts no less than five and no more than ten hours", "non inferiore a cinque e non superiore a dieci ore", []),
 ("ai-miss", "normattiva-dpr-179-2011-art3", "Missing the session costs 15 of the 16 starting credits", "perdita di quindici dei sedici crediti", []),
 ("ai-test", "normattiva-dpr-179-2011-art5", "Without certificates, credits can be earned through a test run by the SUI, also at adult-education centres (CPIA)", "a seguito di un apposito test effettuato a cura dello sportello unico", []),
 ("ai-check", "normattiva-dpr-179-2011-art6", "One month before the two years end, the SUI starts the check and gives 15 days to send documents; a free test is offered", "invitandolo a presentare, entro quindici giorni", []),
 ("ai-30", "normattiva-dpr-179-2011-art6", "With 30 or more credits plus A2 Italian and civic sufficiency, the agreement is fulfilled", "fissata in trenta crediti", ["--visa","All permits of 1 year or more","--field","integration agreement pass mark","--value","30 credits + A2"]),
 ("ai-ext", "normattiva-dpr-179-2011-art6", "Between 1 and 29 credits, or missing levels, the agreement is extended by one year", "la proroga dell'accordo per un anno alle medesime condizioni", []),
 ("ai-zero", "normattiva-dpr-179-2011-art6", "Zero or fewer credits means the agreement is dissolved, with permit revocation or refusal of renewal and expulsion", "la revoca del permesso di soggiorno o il rifiuto del suo rinnovo e l'espulsione", []),
 # --- Questura waits (practice)
 ("ox-2025", "ngo-oxfamitalia-tempi-permessi-soggiorno-2024-03", "In March 2024 Florence organisations reported first Questura appointments being set for September 2025", "vengono fissati primi appuntamenti al settembre 2025", []),
 ("om-wait", "ngo-openmigration-file-questure", "In February 2025 protesters in Florence said the average wait to collect a permit was 1 year, 6 months and 15 days", "1 anno, 6 mesi, 15 giorni e 2 ore", []),
 ("om-rome", "ngo-openmigration-file-questure", "People sleep in queues outside Questure in several cities to get appointments; a man died of cold outside the Rome Questura immigration office in January 2025", "un uomo è morto di freddo all’esterno dell’Ufficio Immigrazione della Questura di Roma", []),
]

def run(args):
    r = subprocess.run([sys.executable, T] + args, capture_output=True, text=True, encoding="utf-8")
    return r.returncode, (r.stdout + r.stderr).strip()

if "--sources" in sys.argv:
    for n, pub, title, off, d in SOURCES:
        print(n, run(["source", "--name", n, "--publisher", pub, "--title", title, "--official", off, "--page-date", d]))
    sys.exit()

only = sys.argv[1:]
for key, n, claim, quote, extra in FACTS:
    if only and key not in only:
        continue
    d, off = D[n]
    status = st(n, d, off)
    extra = list(extra)
    if "--status" in extra:
        i = extra.index("--status"); status = extra[i+1]; extra = extra[:i] + extra[i+2:]
    args = ["add", "--prefix", "K", "--name", n, "--claim", claim, "--quote", quote, "--page-date", d, "--status", status] + extra
    code, out = run(args)
    print(key, code, out[-220:].replace("\n", " | "))
