"""Register the 10 hand-saved sources and log facts with prefix P. Run once from work/P."""
import subprocess, sys

T = "../../../../tools/facts.py"
OUT = []


def run(args):
    r = subprocess.run([sys.executable, T] + args, capture_output=True, text=True, encoding="utf-8")
    msg = (r.stdout + r.stderr).strip()
    OUT.append(msg)
    print(msg)
    return msg


SOURCES = [
    ("interno-circolare-7185-2026-flussi-2027", "Ministry of the Interior, Ministry of Labour and Social Policies, Ministry of Agriculture, Ministry of Tourism",
     "Joint circular prot. 7185 of 1 October 2026: DPCM 2 October 2025, year 2027, entry quotas, pre-filling and click days", "yes", "2026-10-01"),
    ("gu-dl-146-2025", "Gazzetta Ufficiale della Repubblica Italiana",
     "Decree-Law 3 October 2025, n. 146 (original text, GU n. 230 of 3 October 2025): regular entry of foreign workers and management of migration", "yes", "2025-10-03"),
    ("interno-cruscotto-2024-12-31", "UNHCR (based on Ministry of the Interior figures)",
     "Italy Sea arrivals dashboard, December 2024 (with 2024 focus)", "no", "2025-04-11"),
    ("interno-cruscotto-2025-12-31", "UNHCR (based on Ministry of the Interior figures)",
     "Italy Sea arrivals dashboard, December 2025", "no", "2026-03-06"),
    ("unhcr-sea-arrivals-dashboard-2025-08", "UNHCR (based on Ministry of the Interior figures)",
     "Italy Sea arrivals dashboard, August 2025", "no", "2025-10-24"),
    ("interno-avr-2026", "Ministry of the Interior, Department for Civil Liberties and Immigration (Central Directorate for Civil Services for Immigration and Asylum)",
     "Decree of 28 May 2026 extending the FAMI 2021-2027 system action for assisted voluntary return and reintegration (RVA&R) run by IOM", "yes", "2026-05-28"),
    ("interno-it-decreto-flussi", "Ministry of the Interior",
     "Entry mode (Modalita d'ingresso: decreto flussi page, English version)", "yes", "undated"),
    ("vfs-italy-bd-family-reunion-checklist", "VFS Global (Italy visa centre, Bangladesh)",
     "Check-list for Family Reunion Visa (update 02/12/24, legalisation by MOFA and Embassy)", "yes", "2024-12-02"),
    ("vfs-italy-bd-family-sui-bn", "VFS Global (Italy visa centre, Bangladesh)",
     "Check-list for Family Reunion Visa (FAMILY-SUI updated, apostille; English, Italian and Bangla)", "yes", "undated"),
    ("vfs-italy-bd-selfemployment", "VFS Global (Italy visa centre, Bangladesh)",
     "Check-list for Self-employment visa: consultants of existing companies", "yes", "undated"),
]

C = "interno-circolare-7185-2026-flussi-2027"
D = "gu-dl-146-2025"
U24 = "interno-cruscotto-2024-12-31"
U25 = "interno-cruscotto-2025-12-31"
UA = "unhcr-sea-arrivals-dashboard-2025-08"
AVR = "interno-avr-2026"
FL = "interno-it-decreto-flussi"
FR = "vfs-italy-bd-family-reunion-checklist"
FS = "vfs-italy-bd-family-sui-bn"
SE = "vfs-italy-bd-selfemployment"

DATES = {s[0]: s[4] for s in SOURCES}
STAT = {C: "verified", D: "possibly-outdated", U24: "unofficial", U25: "unofficial", UA: "unofficial",
        AVR: "verified", FL: "possibly-outdated", FR: "possibly-outdated", FS: "possibly-outdated", SE: "possibly-outdated"}

# (name, claim, quote, extra dict)
F = [
    # --- Circular 7185 ---
    (C, "For 2027 Italy admits 165,850 non-EU citizens in total for employed (including seasonal) and self-employed work", "complessivamente n. 165.850 cittadini non comunitari", {"visa": "Decreto Flussi", "field": "quota 2027 total", "value": "165,850", "note": "Confirms W0001"}),
    (C, "The 2027 non-seasonal quota is 76,200 entries, of which 14,000 are for domestic and family care work", "n. 76.200 ingressi per lavoro subordinato non stagionale, di cui n. 14.000", {"visa": "Decreto Flussi", "field": "quota 2027 non-seasonal", "value": "76,200 (14,000 care)"}),
    (C, "The 2027 seasonal quota (agriculture and tourism) is 89,000 entries", "n. 89.000 ingressi per lavoro subordinato stagionale nei settori agricolo e", {"visa": "Seasonal", "field": "quota 2027", "value": "89,000"}),
    (C, "The 2027 self-employment quota is 650 entries", "n. 650 ingressi per lavoro autonomo", {"visa": "Self-employment", "field": "quota 2027", "value": "650"}),
    (C, "From 2027 Kenya is added to the countries of origin, after a migration and mobility memorandum signed with Italy on 2 July 2026", "dall'anno 2027 viene ricompreso anche il Kenya con il quale l'Italia ha stipulato il 2 luglio 2026", {}),
    (C, "The other quota breakdowns and reserved quotas of the DPCM of 2 October 2025 stay unchanged for 2027", "Restano ferme le ulteriori articolazioni e riserve delle quote previste dal", {}),
    (C, "Pre-filling of 2027 nulla osta applications is open from 9:00 on 23 October 2026 to 20:00 on 7 December 2026", "dalle ore 9:00 del 23 ottobre 2026 alle ore 20:00 del 7 dicembre 2026", {"visa": "Decreto Flussi", "field": "pre-filling 2027", "value": "23 Oct 2026 09:00 - 7 Dec 2026 20:00", "note": "Confirms W0005"}),
    (C, "Pre-filling is done on the Portale Servizi ALI at portaleservizi.dlci.interno.it, including holidays and at any hour", "compresi i giorni festivi e senza limitazioni di orario", {}),
    (C, "The ALI portal address for pre-filling is https://portaleservizi.dlci.interno.it/AliSportello/ali/home.htm", "https://portaleservizi.dlci.interno.it/AliSportello/ali/home.htm", {}),
    (C, "The Ispettorato Nazionale del Lavoro (labour inspectorate) may check pre-filled applications in advance, under TUI art. 22(2-bis.1)", "Lavoro di effettuare, anche in via anticipata, le verifiche ispettive di competenza sui", {}),
    (C, "Forms for 2027: C-Stag agricolo (seasonal agriculture), C-Stag turistico (seasonal tourism), B2020 (non-seasonal), A-bis in quota (domestic and family care)", "A-bis in quota", {"note": "Form names are listed together in section 2 of the circular"}),
    (C, "Form B2020 is the nulla osta request for non-seasonal employed work in the sectors set by the DPCM", "nulla osta/comunicazione al lavoro subordinato non stagionale nei", {"note": "The line begins with the form name B2020"}),
    (C, "After pre-filling closes, the ALI section reopens from 9:00 on 9 December to 20:00 on 13 December 2026 only to complete and save applications already pre-filled", "dalle ore 9:00 del giorno 9 alle ore 20:00 del giorno 13 dicembre 2026", {}),
    (C, "No new applications can be entered during the 9-13 December 2026 reopening", "Durante tale periodo non sar", {"note": "quote shortened at an accented character"}),
    (C, "The application must be saved so it moves from 'da completare' (to complete) to 'da inviare' (to send), ready for click day", "passaggio della domanda dallo stato \"da completare\" allo stato \"da inviare\"", {}),
    (C, "2027 click day for seasonal agriculture (C-Stag agricolo): 12 January 2027 from 9:00", "12 gennaio 2027, per gli ingressi per lavoro subordinato stagionale nel settore", {"visa": "Seasonal", "field": "click day 2027 agriculture", "value": "12 Jan 2027 09:00"}),
    (C, "2027 click day for seasonal tourism (C-Stag turistico): 9 February 2027", "9 febbraio 2027, per gli ingressi per lavoro subordinato stagionale nel settore", {"visa": "Seasonal", "field": "click day 2027 tourism", "value": "9 Feb 2027 09:00"}),
    (C, "2027 click day for non-seasonal work (B2020): 16 February 2027", "16 febbraio 2027, per gli ingressi per lavoro subordinato non stagionale", {"visa": "Decreto Flussi", "field": "click day 2027 non-seasonal", "value": "16 Feb 2027 09:00"}),
    (C, "2027 click day for domestic and family care work (A-bis): 18 February 2027", "18 febbraio 2027, per gli ingressi per lavoro subordinato non stagionale nel", {"visa": "Domestic and care", "field": "click day 2027", "value": "18 Feb 2027 09:00"}),
    (C, "Click-day applications are accepted from 9:00 on those days", "potranno essere presentate, a decorrere dalle ore 9:00, nei seguenti giorni", {}),
    (C, "All 2027 applications can be sent until 31 December 2027 while quota remains", "Tutte le domande potranno essere presentate fino al 31 dicembre 2027, ferma", {}),
    (C, "Earlier operating rules of joint circular 8047 of 16 October 2025 and circular 8524 of 30 October 2025 still apply where compatible", "circolare congiunta prot. n. 8047 del 16 ottobre 2025 e nella circolare interministeriale prot. n. 8524 del 30 ottobre", {}),
    (C, "The immigration law (D.Lgs. 286/1998) was amended by Decree-Law 146/2025, converted by Law 179 of 1 December 2025, and by Legislative Decree 83 of 16 April 2026", "con modificazioni, dalla legge 1", {"note": "The full sentence: modifiche ... dal decreto legge 3 ottobre 2025, n. 146 convertito, con modificazioni, dalla legge 1 dicembre 2025, n. 179, e dal decreto legislativo 16 aprile 2026, n. 83 (the degree sign after 1 is garbled in the text copy)"}),
    (C, "Under new TUI art. 22(5-quinquies) the employer must confirm the nulla osta request to the SUI within 15 days of being told the visa checks are complete", "a quindici giorni, dalla comunicazione della conclusione degli accertamenti sulla", {"visa": "Decreto Flussi", "field": "employer confirmation deadline", "value": "15 days", "note": "Confirms W0039"}),
    (C, "If the employer does not confirm in time, the request counts as refused and any nulla osta already issued is revoked", "In assenza di conferma entro tale termine, la richiesta si intende rifiutata e il nulla osta, se gi", {}),
    (C, "The employer must promptly inform the foreign worker of every communication it receives about the nulla osta procedure", "l'obbligo in capo al datore di lavoro di informare tempestivamente il cittadino", {}),
    (C, "The contratto di soggiorno (contract of stay) must now be signed by employer and worker within 15 days of the worker's entry into Italy, up from 8 days", "che passa da otto a quindici giorni dalla data di ingresso del lavoratore", {"visa": "Decreto Flussi", "field": "contract of stay deadline", "value": "15 days from entry", "note": "Confirms W0019, W0041"}),
    (C, "Within the same 15 days the employer sends the contract online to the SUI for the permesso di soggiorno request", "Entro il medesimo termine, il datore di lavoro trasmetter", {}),
    (C, "The confirmation and the contract upload can be done by the employer directly or through labour consultants (Law 12/1979) or the main employer organisations it mandates", "dell'area riservata del Portale servizi online, dal datore di lavoro direttamente", {}),
    (C, "For housing proof, circular 9859 of 15 December 2025 applies, following art. 4 of Law 182 of 2 December 2025 on workers housed in hotels or accommodation facilities and in stable construction-site dormitories", "e presso i dormitori stabili dei cantieri", {}),
    (C, "There are no changes in the list of ATECO (sector) codes for 2027", "dell'assenza di modifiche o variazioni nell'elenco dei codici ATECO", {}),

    # --- DL 146/2025 ---
    (D, "Decree-Law 146 of 3 October 2025 on regular entry of foreign workers was published in Gazzetta Ufficiale n. 230 of 3 October 2025 and in force from 4 October 2025", "Vigente al: 4-10-2025", {"note": "Saved file is the original text as published, not the version converted by Law 179/2025"}),
    (D, "The decree's stated aims include fighting caporalato (illegal gangmastering) and labour exploitation in agriculture and the illegal recruitment of foreign workers", "incrementare l'azione di contrasto al caporalato e allo sfruttamento", {}),
    (D, "The time limit for issuing a work nulla osta now runs from the date the request is assigned to the quota, not from its submission", "imputazione della richiesta alle quote di ingresso di cui", {}),
    (D, "For out-of-quota (Article 27) work authorisations, the authorities check the truthfulness of the employer's declarations under DPR 445/2000 art. 71", "al comma 1, le amministrazioni effettuano i controlli di veridicita'", {}),
    (D, "Employers (or employer organisations) who want to apply on click day must first pre-fill the forms on the Interior Ministry portal", "precompilazione dei moduli di domanda, tramite il portale informatico", {}),
    (D, "The authorities check the truthfulness of users' declarations at the moment they access pre-filling", "dagli utenti contestualmente all'accesso alla precompilazione", {}),
    (D, "A private employer may file at most three nulla osta requests for employed work per year", "presentare come utenti privati fino a un massimo di tre richieste di", {"visa": "Decreto Flussi", "field": "max requests per private employer", "value": "3 per year"}),
    (D, "The three-request limit does not apply to requests filed through employer organisations or labour consultants, who must keep the number proportional to the firm's turnover, staff and sector", "presentate sia proporzionale al volume di affari o ai ricavi o", {}),
    (D, "While waiting for the issue, renewal or conversion of a permesso di soggiorno, a foreigner may stay legally and work, even after the 60-day limit, until police notify reasons to refuse", "di sessanta giorni di cui al comma 9, lo straniero puo'", {}),
    (D, "Working while the permit is pending requires the receipt showing the permit request was filed", "ricevuta attestante l'avvenuta presentazione della richiesta di", {}),
    (D, "The special permit for victims of violence or serious exploitation (TUI art. 18(4)) now lasts one year instead of six months", "un anno", {"note": "Art. 4(1)(a)(1): al comma 4, le parole: <<sei mesi>> sono sostituite dalle seguenti: <<un anno>> (guillemets garbled in the text copy, so the quote is short)"}),
    (D, "Holders of art. 18 and art. 18-bis permits may receive the assegno di inclusione (inclusion benefit)", "presente articolo possono beneficiare dell'assegno di inclusione di", {}),
    (D, "The out-of-quota entry of domestic workers to care for the very elderly and people with disabilities (DL 145/2024 art. 2) is extended to each year 2026-2028", "e per ciascuno degli anni dal 2026 al 2028", {"visa": "Domestic and care", "field": "out-of-quota care workers", "value": "2026-2028"}),
    (D, "The SUI's time limit for family reunification nulla osta (TUI art. 29(8)) rises from 90 to 150 days", "centocinquanta giorni", {"visa": "Family reunification", "field": "SUI deadline", "value": "150 days", "note": "Official Gazzetta confirmation of F0020"}),
    (D, "Special measures for the Lampedusa hotspot are extended to 31 December 2027", "Fino al 31 dicembre 2027", {}),
    (D, "The original text of Decree-Law 146/2025 contains no rule on Bangladesh or on 'high-risk' countries; its articles cover nulla osta checks, pre-filling, work while a permit is pending, special permits, care workers, volunteering, family reunification, caporalato, recruitment fund and Lampedusa", "Disposizioni urgenti in materia di ingresso regolare di lavoratori e", {"skip": True}),

    # --- UNHCR Dec 2024 ---
    (U24, "In 2024, 66,617 refugees and migrants arrived in Italy by sea, 58% fewer than the 157,651 of 2023", "In 2024, 66,617 refugees and migrants arrived in Italy by sea, compared to", {"note": "Matches U0006"}),
    (U24, "Bangladesh was the top country of origin of sea arrivals in 2024, with 21%, ahead of Syria (19%) and Tunisia (12%)", "The top six countries of origin were Bangladesh (21%)", {}),
    (U24, "Over 14,200 Bangladeshis reached Italy by sea in 2024, 12% more than in 2023", "over 14,200 Bangladeshis (+12% compared to", {"note": "UNHCR figure; the Ministry cruscotto gives 13,779 (U0007): different counting dates/definitions", "status": "conflict"}),
    (U24, "UNHCR links the rise in Bangladeshi arrivals to smuggling businesses using flight routes to Benina (Benghazi) airport", "rely on flight routes to Benina Benghazi Airport", {}),
    (U24, "Asian nationals reportedly flew to Benghazi before moving to Tripolitania to embark", "traveled by air to Benghazi before moving onward to Tripolitania for embarkation", {}),
    (U24, "On the Libya route in 2024 the top countries of origin were Bangladesh, Syria, Egypt, Pakistan and Eritrea", "Bangladesh, the Syrian Arab Republic, Egypt, Pakistan, and Eritrea", {}),
    (U24, "In December 2024 Bangladeshis were 40% of all sea arrivals and 50% of departures from Libya", "In December, Bangladeshis accounted for 40 per cent of all arrivals by sea", {}),
    (U24, "In December 2024, 50% of people departing Libya were Bangladeshi", "the main nationalities of those departing from Libya were Bangladeshis (50%", {}),
    (U24, "In 2024, 1,718 people died or went missing crossing the central Mediterranean towards Italy, one for every 39 arrivals (IOM Missing Migrants data)", "1,718 refugees and migrants lost their lives or went missing at sea", {}),
    (U24, "Lampedusa received over 45,500 sea arrivals in 2024, 68% of the total", "Lampedusa remained the main port of disembarkation in Italy, with over 45,500 sea arrivals", {}),
    (U24, "In 2024, 63% of sea arrivals departed from Libya (42,279 people)", "63 per cent of the people reaching Italy via sea departed from Libya (42,279 people", {}),
    (U24, "Bangladeshis were the largest group of unaccompanied children arriving in December 2024 (55 of 272)", "main nationalities were Bangladeshi (55)", {}),

    # --- UNHCR Dec 2025 ---
    (U25, "In 2025, 66,316 refugees and migrants arrived in Italy by sea, against 66,617 in 2024", "In 2025, 66,316 refugees and migrants arrived in Italy by sea", {"status": "conflict", "note": "Ministry cruscotto gives 66,296 (U0006)"}),
    (U25, "Bangladeshis were the largest nationality arriving by sea in Italy in 2025, at 20,259", "Bangladesh 20,259", {"status": "conflict", "note": "UNHCR chart; Ministry cruscotto gives 20,164 (U0005). Bangladesh is first either way; Egypt second at 9,115"}),
    (U25, "Egypt was second in 2025 with 9,115 sea arrivals", "Egypt Er itr ea 9,115", {"skip": True}),
    (U25, "In December 2025 Bangladeshis were 31% of all sea arrivals (30% in November)", "Bangladeshi nationals accounted for 31 per cent of all sea arrivals (30% in November)", {}),
    (U25, "In December 2025 Bangladeshis were 39% of people departing from Libya", "the main nationalities of individuals departing from Libya were Bangladeshi nationals at 39 per cent", {}),
    (U25, "In 2025, 88% of sea arrivals left from Libya: 58,408 people in 1,103 landings", "departed from Libya (58,408 persons in 1,103 landings)", {}),
    (U25, "In 2025, 18% of sea arrivals were unaccompanied children and 74% adult men", "males (74%), followed by unaccompanied children (UAC,", {}),
    (U25, "Bangladeshis were the second-largest group of unaccompanied children arriving in December 2025 (99 of 506)", "Bangladeshis (99)", {}),

    # --- UNHCR Aug 2025 ---
    (UA, "From January to August 2025, 42,693 people arrived in Italy by sea, 2% more than the 42,006 of the same period of 2024", "In the first eight months of 2025, 42,693 refugees and migrants arrived in", {}),
    (UA, "Bangladeshis were the largest nationality arriving January-August 2025, with 13,148", "Bangladesh 13,148", {}),
    (UA, "In August 2025 Bangladeshis were 21% of sea arrivals, down from 33% in July", "In August, Bangladeshis accounted for 21 per cent of all sea arrivals (down from 33% in July)", {}),
    (UA, "In August 2025 Bangladeshis were 26% of departures from Libya, down from 37% in July", "Libya were Bangladeshi (26%, down from 37% in July)", {}),
    (UA, "In the first eight months of 2025, 88% of arrivals departed from Libya (37,582 people in 705 landings)", "departed from Libya (37,582 persons in 705", {}),
    (UA, "In August 2025, 122 Bangladeshi unaccompanied children arrived, third after Egyptians and Eritreans", "Bangladeshis (122)", {}),
    (UA, "The dashboard's data are official Ministry of the Interior figures shared with UNHCR, provisional and subject to change", "All data are based on official Ministry of Interior figures shared with UNHCR", {}),

    # --- AVR 2026 ---
    (AVR, "Italy's national assisted voluntary return and reintegration (RVA&R) system action, funded by FAMI 2021-2027 (the EU Asylum, Migration and Integration Fund), funded a single project", "ammettendo al finanziamento un solo progetto", {}),
    (AVR, "The project's total funding is EUR 14,999,999.99", "14.999.999,99", {}),
    (AVR, "The project is run by IOM (Organizzazione Internazionale per le Migrazioni), for 36 months from 2 January 2024", "Organizzazione Internazionale per le Migrazioni (OIM) in data 13 dicembre 2023", {"field": "AVR operator", "value": "IOM (OIM)"}),
    (AVR, "The project activities were planned to last 36 months starting 2 January 2024", "36 mesi decorrenti dal", {}),
    (AVR, "The Ministry found limited progress of the activities at 30 June 2025", "alla luce dei limitati livelli di", {}),
    (AVR, "IOM's counselling, pre-departure and return-assistance activities are extended to 2 February 2027", "attivit", {"skip": True}),
    (AVR, "Counselling, pre-departure and return assistance under the IOM project run until 2 February 2027", "pre-partenza e assistenza al ritorno fino al 2 febbraio 2027", {"field": "AVR counselling/departures end", "value": "2 Feb 2027"}),
    (AVR, "Reintegration and monitoring activities run until 2 August 2027", "di prorogare le attivit", {"skip": True}),
    (AVR, "Reintegration and monitoring activities under the IOM project run until 2 August 2027", "reintegrazione e monitoraggio fino al 2", {}),
    (AVR, "Under the original call, reintegration grants are paid in specific goods and services", "i sussidi di reintegrazione devono essere erogati attraverso prestazioni specifiche", {}),
    (AVR, "From the May 2026 decree, the reintegration grant may also be paid by money transfer or in cash, with monitoring and financial traceability", "del money transfer o del cash etc.) laddove ci", {}),
    (AVR, "Decree-Law 55 of 24 April 2026 introduced a payment, at the end of the procedure, for a representative with a mandate who helps a migrant apply for an RVA&R programme", "decreto-legge 24", {"skip": True}),
    (AVR, "Decree-Law 55 of 24 April 2026 pays a mandated representative who helps a migrant apply for assisted voluntary return, at the end of the procedure", "che introduce un compenso economico, a conclusione del", {}),
    (AVR, "The FAMI project PROG-1174 F.A.S.T.E.R. provides local counselling to prepare departure and reintegration in countries of origin under RVA&R", "F.A.S.T.E.R. - Formazione, Assistenza, Supporto al Territorio per", {}),
    (AVR, "The Ministry wants more RVA&R departures to free reception places for the EU Pact's border-procedure capacity due by 12 June 2026", "di una capacit", {"skip": True}),
    (AVR, "The Ministry treats more voluntary-return departures as essential to free reception places for the accelerated border procedures required by EU Regulation 2024/1348 from 12 June 2026", "come assolutamente essenziale per consentire di realizzare pi", {}),
    (AVR, "The project's maximum duration is extended at no extra cost to 43 months from the start", "a 43 mesi dall'avvio delle attivit", {}),
    (AVR, "The decree was signed on 28 May 2026 by Gennaro Capo, head of the intervention", "28 maggio 2026", {}),

    # --- Interior Ministry flussi page ---
    (FL, "To enter Italy legally a foreigner needs a passport or travel document and an entry visa from the Italian embassy or consulate in the country of origin or residence", "you need a passport or other travel document and", {}),
    (FL, "Short-stay visas are valid up to three months; long-stay visas require a residence permit for the same purpose", "Entry into Italy is permitted with short-term visas, valid", {}),
    (FL, "Staying longer than three months or the period on the visa makes a foreigner irregular and leads to expulsion", "staying longer than three", {}),
    (FL, "Expulsion orders are issued by the Prefettura and carried out by the Questura (police headquarters)", "The expulsion order is issued by the competent prefecture", {}),
    (FL, "An expelled foreigner may not re-enter Italy without special authorisation or until the entry ban expires", "Expelled foreign citizens may not re-enter Italy unless they have special authorization", {}),
    (FL, "Entry for employed, seasonal and self-employed work must fall within the quotas of the periodic flow decrees issued by the Prime Minister", "the so-called \"flow decrees,\" issued by the Prime Minister", {}),
    (FL, "The flow decrees usually reserve quotas for citizens of countries that have agreements with Italy on entry flows and readmission", "reserve for citizens from countries with which the government has", {}),

    # --- VFS family reunion checklist 02/12/24 ---
    (FR, "VFS family reunion checklist (update 2 December 2024): Schengen D-type visa form, original, filled in English or Italian and signed (both parents for a minor)", "Schengen (\"D\"-Type) visa application form, original", {}),
    (FR, "Two recent identical ICAO photos, 4.0 x 3.5 cm, colour, white background, taken within 6 months", "Photos must be ICAO format (4.0 x 3.5 cm, color photo with white background, taken within the last 6", {}),
    (FR, "Passport valid at least three months beyond the visa's expiry, with two blank visa pages, plus a copy of the bio page", "Passport must be valid for at least additional three months from the date of expiry of the visa's validity", {}),
    (FR, "A copy of the SUI's notice that the nulla osta was issued; check that name, surname, gender and date of birth on it are correct to avoid long delays", "make sure the data o f the applicant are", {}),
    (FR, "A one-way flight booking with PNR or reservation number and itinerary", "One way airline ticket booking with Passenger Registration Number", {}),
    (FR, "Spouse, Muslim applicants: marriage certificate and nikahnama in Bengali and English, original, legalised by MOFA and the Italian Embassy", "For Muslim applicants `Marriage Certifiacate\" and \"Nikah Nama\" in Bengali and English", {"note": "Superseded by apostille: see the FAMILY-SUI updated checklist and F0068, F0082"}),
    (FR, "The marriage certificate must show the solemnisation date (nikahnama column 12), registration date (column 24), volume, page and serial number", "Marriage solemnized", {}),
    (FR, "In a second marriage, documents proving the first marriage was legally dissolved (talaknama) are required", "divorce certificate \"Talak Nama\"", {}),
    (FR, "All applicants: a family certificate from the local chairman or commissioner, legalised by MOFA and the Embassy", "FOR ALL APPLICANTS Family certificate issued by local chairman or commissioner legalized", {}),
    (FR, "Minors joining parents: consent of both parents or custodian, parents' passport copies, original birth certificate, and Bangladeshi court papers for a legal guardian", "relevant Bangladeshi Courts for minors legalized", {}),
    (FR, "Optional for a spouse: certified copies of all pages of the Italy-resident spouse's passports since the marriage, and IDs of all wedding witnesses", "Certified copy of all pages of all passports owned by the spouse residing in Italy since the date of the", {}),
    (FR, "For telephone or video marriages, IDs and residence permits of the witnesses in Italy are recommended", "in case of Telephonic/video Marriages", {}),
    (FR, "Only spouses, children under 18, parents under 65 with no other children in Bangladesh and dependent parents over 65 are eligible for the family reunion visa", "Only spouses, children below 18 years, parents below 65 years with no other children in", {"note": "Confirms F0079"}),
    (FR, "Applicants with MOFA-legalised documents could have the Embassy legalise them together with the visa application, paying the visa fee plus legalisation fees", "applicants shall pay the visa application fee + required legalization fees", {"note": "Old procedure; see F0082"}),
    (FR, "The Embassy may ask for documents not on the checklist", "The Embassy reserves itself the right to request any supplementary document", {}),

    # --- VFS FAMILY-SUI updated ---
    (FS, "Updated VFS family reunion checklist: nikahnama and marriage certificate for Muslim applicants in Bengali and English, original and apostilled", "Nikah Nama\" in Bengali and English (original and Apostilled)", {"note": "Confirms F0068"}),
    (FS, "Hindu and other-faith applicants: marriage certificate or true copy of the register book, translated into English, original and apostilled", "register book/marriage translated in English (original and Apostilled)", {}),
    (FS, "All applicants: family certificate from the local chairman or commissioner, original and apostilled", "Family certificate issued by local chairman or commissioner", {}),
    (FS, "Child in Italy: original birth certificate naming the parents, apostilled", "stating the names of the parents Apostilled", {}),
    (FS, "Only one apostille per document is accepted", "ONLY ONE APOSTILLE FOR EACH DOCUMENT WILL BE ACCEPTED", {}),
    (FS, "Applicants are personally responsible for the authenticity and truth of every document, per the Embassy's communique of 19 May 2025", "applicants are responsible for the authenticity and the", {}),
    (FS, "The Embassy's communique on document authenticity is dated 19 May 2025", "19th of May 2025", {}),
    (FS, "The same applicant cannot submit more than one visa application at the same time, even with two different passports", "The same applicant cannot submit more than one visa application at the same time", {}),
    (FS, "The updated checklist is published in English, Italian and Bangla", "Documenti richiesti per visto per RICONGIUNGIMENTO FAMILIARE", {"note": "Bangla text layer is empty in the saved copy"}),

    # --- VFS self-employment ---
    (SE, "Self-employment visa for consultants or officers of existing companies: national D-type visa form, original, filled in English or Italian", "National (\"D\"-Type) visa application form, original", {}),
    (SE, "Passport valid at least 3 months after the planned departure from Schengen, two blank pages, and a copy of all pages", "Passport must be valid for at least 3 months after planned departure date from Schengen area", {}),
    (SE, "A nulla osta from the competent Questura issued within the 120 days before the visa application", "that must have been issued before 120 days prior of submission of the visa application", {"status": "conflict", "note": "Embassy checklist July 2026 says 90 days (W0121); this VFS copy is undated and probably older"}),
    (SE, "A certification from the Direzione Provinciale del Lavoro that the contract is not subordinate employment", "Statement proving that the working contract is not for subordinated work", {}),
    (SE, "A Chamber of Commerce certificate that the company has been active at least three years in the Registro delle imprese", "Statement that the company has been active for at least the last three years", {"note": "Confirms W0122"}),
    (SE, "The Italian company's visura camerale (business registration extract) from the Chamber of Commerce", "Visura Camerale dell'azienda italiana", {}),
    (SE, "A statement from the company's legal representative guaranteeing pay of at least EUR 8,400, the health-charge exemption threshold", "of minimum UR 8.400, which corresponds to the minimum amount foreseen by law", {"status": "conflict", "note": "Embassy checklist July 2026 says EUR 8,500 (W0123); euro sign garbled as 'UR' in the text copy"}),
    (SE, "The company's last filed balance sheet or last tax return proving it can pay the applicant", "proving that the Italian company's revenues are sufficient to pay the", {}),
    (SE, "Personal bank statement from a bank in Bangladesh for the last 6 months, plus any other proof of solvency", "Personal bank statement issued by any bank operating in Bangladesh covering the last 6 months", {"note": "Confirms W0124"}),
    (SE, "Proof of housing: purchase or rental contract, or a housing declaration under Law 15/1968 signed by an Italian or a legally resident foreigner with a copy of their ID", "accommodation statement, made in accordance with art. 2 and 4 of Italian Law 4.1.1968, no.", {}),
    (SE, "Travel insurance valid in the whole Schengen area covering medical, hospital and repatriation costs up to EUR 30,000 for the first 3 months", "hospitalization and repatriation costs up to 30,000 Euros", {}),
    (SE, "Civil status papers: nikahnama or marriage act translated into English; talaknama for divorced applicants; spouse's death certificate for widows and widowers", "For married applicants: marriage certificate (e.g.\"Nika Namah\" for muslims", {}),
    (SE, "A flight booking with PNR or reservation number and itinerary", "Airline ticket booking with Passenger Registration Number or Reservation Number and travel", {}),
]

if __name__ == "__main__":
    for n, pub, title, off, date in SOURCES:
        run(["source", "--name", n, "--publisher", pub, "--title", title, "--official", off, "--page-date", date])
    results = []
    for name, claim, quote, x in F:
        if x.get("skip"):
            continue
        args = ["add", "--prefix", "P", "--name", name, "--claim", claim, "--quote", quote,
                "--page-date", DATES[name], "--status", x.get("status", STAT[name])]
        for k in ("visa", "field", "value", "note"):
            if x.get(k):
                args += ["--" + k, x[k]]
        msg = run(args)
        results.append((name, claim, msg))
    with open("log_facts_out.txt", "w", encoding="utf-8") as f:
        for name, claim, msg in results:
            f.write(f"{msg}\t{name}\t{claim}\n")
