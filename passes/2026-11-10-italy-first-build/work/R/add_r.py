import subprocess, sys

T = "../../../../tools/"
def run(args):
    r = subprocess.run([sys.executable] + args, capture_output=True, text=True, encoding="utf-8")
    print(" ".join(args[:3])[:80], "->", (r.stdout + r.stderr).strip()[:300])

SOURCES = [
    # name, url, publisher, title, official, page_date
    ("esteri-ambdhaka-checklist-study-university-2026", "https://ambdhaka.esteri.it/wp-content/uploads/2026/07/Study-University-pre-enrolment.pdf",
     "Embassy of Italy in Dhaka", "Check-list for study visa (university pre-enrolment)", "yes", "2026-07"),
    ("vfs-bgd-ita-study-university-checklist", "https://www.vfsglobal.com/one-pager/italy/bangladesh/english/pdf/STUDY-VISA-University-pre-enrolment_updated.pdf",
     "Embassy of Italy in Dhaka (VFS Global)", "Check-list for study visa (university pre-enrolment), VFS Global copy", "yes", "undated"),
    ("prefettura-elenco-documenti-ricongiungimento-2024", "https://prefettura.interno.gov.it/sites/default/files/3/2024-03/elenco_documenti_per_il_ricongiungimento.pdf",
     "Ministero dell'Interno (posted by a Prefettura)", "Elenchi documentazione e modulistica per il rilascio del nulla osta al ricongiungimento familiare (modelli SM e GN)", "yes", "2024-03-01"),
    ("comune-roma-idoneita-alloggiativa", "https://www.comune.roma.it/web/it/scheda-servizi.page?contentId=INF41416",
     "Roma Capitale", "Idoneita alloggiativa per immigrati", "yes", "undated"),
    ("esteri-ambdhaka-family-reunion-sui-2026-07", "https://ambdhaka.esteri.it/wp-content/uploads/2026/07/Family-reunion-SUI.pdf",
     "Embassy of Italy in Dhaka", "Check-list for Family Reunion Visa (Family-reunion-SUI.pdf, uploaded July 2026)", "yes", "2026-07-01"),
    ("ambdhaka-checklist-bluecard-2026-07", "https://ambdhaka.esteri.it/wp-content/uploads/2026/07/Bluecard-L-N.pdf",
     "Embassy of Italy in Dhaka", "Check-list for Qualified Work VISA L/N ART 27 (D type), Blue Card", "yes", "2026-09-14"),
    ("inps-malattia-visite-controllo", "https://www.inps.it/it/it/dettaglio-approfondimento.schede-informative.indennit--di-malattia-e-visite-mediche-di-controllo.html",
     "INPS", "Indennita di malattia e visite mediche di controllo", "yes", "2026-09-21"),
    ("poste-guida-abf", "https://www.poste.it/resources/bancoposta/pdf/trasparenza/guida_arbitro_finanziario.pdf",
     "Arbitro Bancario Finanziario / Banca d'Italia (guide distributed by Poste Italiane)", "ABF in parole semplici", "yes", "undated"),
    ("news-domani-dacca-roma-solo-andata", "https://www.editorialedomani.it/fatti/dacca-roma-solo-andata-la-vita-sospesa-dei-migranti-pldhr6v6",
     "Domani", "Dacca-Roma solo andata: la vita sospesa dei migranti", "no", "2025-11-17"),
]

FACTS = [
    # name, claim, quote, page_date, status
    ("esteri-ambdhaka-checklist-study-university-2026",
     "Study visa (university): the Embassy accepts a DoV already issued by it, or the receipt of the DoV application, or a verifiable CIMEA certificate",
     "Include Declaration of Value (DoV) already issued by the Embassy of Italy in Dhaka or the receipt of your DoV application (or, where applicable, by another Italian Consulate) OR a",
     "2026-07", "verified"),
    ("esteri-ambdhaka-checklist-study-university-2026",
     "Study visa (university): travel health insurance must be valid for the whole Schengen area and cover the whole stay",
     "Insurance must be valid for the whole Schengen area and cover the whole period of stay within the Schengen area.",
     "2026-07", "verified"),
    ("vfs-bgd-ita-study-university-checklist",
     "Study visa (university): the insurance must cover medical, hospital and repatriation costs for at least EUR 30,000",
     "deve coprire eventuali spese mediche, di ricovero ospedaliero e di rimpatrio per un minimo di 30.000 Euro",
     "undated", "possibly-outdated"),
    ("prefettura-elenco-documenti-ricongiungimento-2024",
     "Family reunification: if the sponsor owns the home, the purchase contract (contratto di compravendita) is the housing document",
     "SE DI PROPRIETÀ: 1) contratto di compravendita;",
     "2024-03-01", "possibly-outdated"),
    ("comune-roma-idoneita-alloggiativa",
     "In Rome the housing certificate request is filled in online at http://servizi.utgroma.it/ria/richiesta/nuova (Prefettura di Roma)",
     "compilare on-line allink della Prefettura di Roma - UTG http://servizi.utgroma.it/ria/richiesta/nuova",
     "undated", "possibly-outdated"),
    ("comune-roma-idoneita-alloggiativa",
     "Rome housing certificate: the applicant gives an email address to be told when the Municipio has informed the Prefettura of the documents delivered and of the outcome",
     "indicare anche l'indirizzo e-mail del richiedente per essere avvisato, non appena il Municipio abbia comunicato alla Prefettura la consegna della documentazione e l'esito della procedura",
     "undated", "possibly-outdated"),
    ("esteri-ambdhaka-family-reunion-sui-2026-07",
     "Family reunion visa: one ICAO photo, 3.5 x 4.0 cm, colour, white background, taken within the last 6 months",
     "Photo must be ICAO format (3.5 x4.0 cm, color photo with white background, taken within the last 6 months).",
     "2026-07-01", "verified"),
    ("ambdhaka-checklist-bluecard-2026-07",
     "Blue Card (L/N Art. 27) visa: original national D visa form, filled in in English or Italian and signed by the applicant",
     "National (\"D\"-Type) visa application form, original Form must be duly filled in English or Italian, and signed by the applicant",
     "2026-09-14", "verified"),
    ("ambdhaka-checklist-bluecard-2026-07",
     "Blue Card (L/N Art. 27) visa: copy of the SUI nulla osta; check name, surname, gender and date of birth on it to avoid long visa delays",
     "Copy of the \"Nulla Osta\" issued by the SUI (Sportello Unico per l'Immigrazione) In order to avoid long delays in the issuance of the visa, make sure the data the applicant are correct on the aforesaid communication of issuance of the \"Nulla Osta\" (name, surname, gender and date of birth)",
     "2026-09-14", "verified"),
    ("inps-malattia-visite-controllo",
     "Colf and badanti are collaboratori familiari (domestic workers)",
     "collaboratori familiari (colf e badanti)",
     "2026-09-21", "verified"),
    ("poste-guida-abf",
     "More information on the ABF, including the panels' decisions, is at www.arbitrobancariofinanziario.it",
     "puoi consultare il sito www.arbitrobancariofinanziario.it",
     "undated", "possibly-outdated"),
    ("news-domani-dacca-roma-solo-andata",
     "In Bucharest the Bangladeshi worker was offered undeclared construction work, 12 hours a day, 7 days a week",
     "gli hanno offerto un lavoro in nero in edilizia. «Dodici ore al giorno sette giorni su sette",
     "2025-11-17", "unofficial"),
    ("news-domani-dacca-roma-solo-andata",
     "He refused and had to pay another EUR 300 for the nulla osta Romania requires to look for another job",
     "per ottenere il nullaosta, necessario nel sistema romeno per cercare un altro lavoro, ho dovuto pagare altri 300 euro",
     "2025-11-17", "unofficial"),
    ("news-domani-dacca-roma-solo-andata",
     "He then flew to Italy to join a cousin, Romania now being in the Schengen area",
     "ha preferito raggiungere un cugino in Italia con un volo, ora che la Romania è dentro l’area Schengen",
     "2025-11-17", "unofficial"),
]

for n, url, pub, title, off, pd in SOURCES:
    run([T + "fetch.py", "--log", url, n, "manual"])
    run([T + "facts.py", "source", "--name", n, "--publisher", pub, "--title", title, "--official", off, "--page-date", pd])
for n, claim, quote, pd, st in FACTS:
    run([T + "facts.py", "add", "--prefix", "R", "--name", n, "--claim", claim, "--quote", quote, "--page-date", pd, "--status", st])
