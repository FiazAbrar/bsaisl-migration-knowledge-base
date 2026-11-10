import subprocess, os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
F = ['python', '../../../../tools/facts.py']
S = [
 ('bb-fx-rate-sheet-2026-11-10', 'Bangladesh Bank', 'Foreign exchange rate sheet, 10/11/2026', 'yes', '2026-11-10'),
 ('bb-fx-rate-sheet-2026-11-09', 'Bangladesh Bank', 'Foreign exchange rate sheet, 09/11/2026', 'yes', '2026-11-09'),
 ('ecb-eurofxref-90d-2026-11-10', 'European Central Bank', 'Euro foreign exchange reference rates, last 90 days (XML)', 'yes', '2026-11-09'),
 ('ecb-eur-usd-reference-rate-2026-11', 'European Central Bank', 'US dollar (USD) reference rate chart page', 'yes', '2026-11-09'),
 ('bancaditalia-daily-rates-2026-11-09', "Banca d'Italia", 'Daily exchange rates against the euro, 9 November 2026 (all currencies, CSV)', 'yes', '2026-11-09'),
 ('bb-remittance-top30-countries-italy', 'Bangladesh Bank', "Workers' Remittance Inflows: Top 30 Countries, July-September 2026", 'yes', '2026-10'),
 ('bb-remittance-cost-italy', 'Bangladesh Bank', "Simple average cost of wage earners' remittances, Jan-Mar and Apr-Jun 2026", 'yes', '2026-07'),
 ('bb-remittance-monthly-report-2026-08-italy', 'Bangladesh Bank', 'Monthly report on remittance, August 2026 (Annex III, country-wise yearly)', 'yes', '2026-09-01'),
 ('bancaditalia-rimesse-immigrati', "Banca d'Italia", "Rimesse verso l'estero dei lavoratori stranieri (second quarter 2026)", 'yes', '2026-10-09'),
 ('bancaditalia-rimesse-xlsx-2026-10', "Banca d'Italia", "Rimesse verso l'estero dei lavoratori stranieri, data file rimesse.xlsx (Bangladesh rows)", 'yes', '2026-10-09'),
 ('news-ilsole24ore-remittances-2025-bangladesh-first', 'Il Sole 24 Ore', "Migrants' remittances rise to 8.6 billion: Bangladesh in the lead, India second", 'no', '2026-04-11'),
 ('cespi-osservatorio-rimesse-2026-04', 'CeSPI', "Osservatorio nazionale sull'inclusione finanziaria dei migranti: rimesse, aprile 2026", 'no', '2026-04'),
 ('news-bdnews24-bangla-italy-remittance-2026-05', 'bdnews24.com (Bangla)', 'Italy remittance: Bangladeshis first again', 'no', '2026-05-25'),
 ('bkash-remittance-mts-italy', 'bKash Limited', 'Money Transfer Service (remittance partners by country)', 'no', 'undated'),
 ('worldbank-rpw-italy-bangladesh', 'World Bank', 'Remittance Prices Worldwide: sending money from Italy to Bangladesh (Q3 2025 survey)', 'no', '2025-09-03'),
 ('hoganlovells-italy-repeals-money-transfer-tax', 'Hogan Lovells', 'Italian Government repeals money transfer tax', 'no', '2021-01'),
 ('news-fiscalfocus-bilancio-2021-abroga-imposta-money-transfer', 'Fiscal Focus', "La Legge di Bilancio 2021 abroga l'imposta sul money transfer", 'no', '2021-01-14'),
 ('news-qds-hawala-bangladesh-roma-2020', 'QdS / Italpress', 'Trasferimenti illeciti verso il Bangladesh per 20 mln, sequestri', 'no', '2020-07-30'),
 ('news-skytg24-conti-base-2026-08', 'Sky TG24', "Conti di base, cosa sono e perche la Banca d'Italia vuole promuoverli?", 'no', '2026-08-05'),
 ('news-avvenire-conto-gratuito-banche', 'Avvenire', "Il conto corrente gratuito c'e. Ma le banche non lo dicono", 'no', '2026-08'),
 ('asgi-conto-corrente-stranieri', 'ASGI', "Diritto all'apertura di un conto corrente bancario (leaflet)", 'no', '2022'),
 ('inl-nota-5828-2018-stipendi-contanti', 'Ispettorato Nazionale del Lavoro', 'Nota prot. 5828 del 4 luglio 2018: divieto di pagamento in contanti delle retribuzioni', 'yes', '2018-07-04'),
 ('poste-guida-abf', "Arbitro Bancario Finanziario / Banca d'Italia (guide distributed by Poste Italiane)", 'ABF in parole semplici', 'yes', 'undated'),
 ('news-ecnews-irpef-2026-aliquote', 'EC News', 'Legge di bilancio 2026: revisione delle aliquote IRPEF', 'no', '2026-01'),
 ('inps-messaggio-698-2025-detrazioni', 'INPS (copy hosted by informazionefiscale.it)', 'Messaggio n. 698 del 26-02-2025: detrazioni per carichi di famiglia (Legge 207/2024)', 'yes', '2025-02-26'),
 ('news-cafinforma-detrazioni-familiari-stranieri', 'CAF Informa', 'Detrazioni per familiari a carico negate ai contribuenti stranieri', 'no', '2024-10'),
 ('normattiva-tuir-art12-detrazioni-familiari', 'Normattiva', 'DPR 917/1986 (TUIR) art. 12 (page shell only; article text not captured)', 'yes', '2026-11-10'),
 ('eu-youreurope-carrying-cash', 'European Union (Your Europe)', 'Rules for travelling with cash when entering or leaving the EU', 'yes', 'undated'),
 ('adm-circolare-12-2024-denaro-contante', 'Agenzia delle Dogane e dei Monopoli', 'Circolare 12/2024 on cash entering and leaving Italy', 'yes', '2024-05-07'),
 ('hsia-customs', 'Hazrat Shahjalal International Airport (Customs House, Dhaka)', 'Customs, HSIA (baggage rules for passengers)', 'yes', 'undated'),
 ('mof-budget-speech-2026-27', 'Finance Division, Ministry of Finance, Bangladesh', 'National Budget Speech FY2026-27', 'yes', '2026-06-01'),
 ('news-tbs-bfiu-14000-mfs-hundi', 'The Business Standard', 'BFIU to freeze 14,000 more MFS accounts over online gambling, hundi links', 'no', '2026-08-03'),
 ('tbs-why-hundi-2024', 'The Business Standard', 'As remittance grows, can hundi be reined in?', 'no', '2024-12-05'),
 ('nsd-wage-earner-development-bond', 'Department of National Savings, Bangladesh', 'Wage Earner Development Bond', 'yes', '2026-04-14'),
]
for name, pub, title, off, date in S:
    r = subprocess.run(F + ['source', '--name', name, '--publisher', pub, '--title', title, '--official', off, '--page-date', date],
                       capture_output=True, text=True, encoding='utf-8')
    print(name, '->', (r.stdout + r.stderr).strip()[-160:])
