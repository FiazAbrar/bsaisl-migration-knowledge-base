import csv,sys
fix={
"L0004":"The contract must state the workplace where the work is done",
"L0012":"Within 5 working days of a written request, the employer must give a current or former worker certified copies of documents about the job",
"L0017":"When one side proposes in writing to end the contract by agreement, the other must answer in writing within 3 working days",
"L0038":"Leave for the first year can be taken after 11 months' continuous work with the employer",
"L0045":"The bank-transfer (cashless) wage rule covers individual entrepreneurs paying foreign citizens",
"L0054":"During temporary inability to work (sickness) the employer pays a sickness benefit",
"L0056":"The employer's liability for work injury includes travel to or from work in transport the employer provides",
"L0090":"A foreigner without valid papers pays 5,500 som for up to 1 month, 10,000 for 1-3 months, 15,000 for 3-6 months, 17,500 for 6-12 months and 20,000 for over a year",
"L0092":"If a written order to fix a migration violation is not obeyed within 30 days, a court orders expulsion",
"L0100":"The inviting party must explain to the foreigner his rights and duties in time",
"L0104":"Exit visa after overstaying 1 to 2 years: 192,500 som / USD 2,200",
"L0116":"The Register of Bad-Faith Employers covers breaches of labour and migration law such as unpaid wages or breached working conditions",
"L0118":"An employer is removed from the Register after one calendar year",
"L0121":"The resident card is refused or cancelled when tax and social contributions go unpaid for 3 months or more",
"L0123":"An exit visa (type L), valid up to 10 days, is issued to leave the country with the overstay period made good",
"L0126":"A free emergency exit visa (type E) is issued for serious illness or a critical condition that stops the person leaving alone",
"L0133":"Drug crimes in especially large amounts, or sale to a child: 12 to 15 years' prison with confiscation",
"L0144":"Documents: a copy of the Bangladesh embassy's certificate (NOC) or the death certificate",
"L0145":"The Board gives a Tk 35,000 cheque for body transport and burial",
"L0147":"To bring a body home, the Board takes the family's wishes and sends them to the embassy or high commission concerned",
"L0152":"A committee views the worker on a WhatsApp video call",
"L0164":"In the first half of 2026 labour inspectors recovered 4.4 million som of unpaid wages for workers",
"L0165":"Presidential decree No. 362 of 26 October 2026 widens the powers of the Service for Control and Supervision of Labour Legislation under the Ministry of Labour, giving it migration control over foreign labour",
"L0166":"A complaint is sent in writing to the labour inspection's local office where the employer is located",
"L0170":"The complaint should state the breach, for example 'wages for May not paid'",
"L0171":"After a complaint the inspection issues an order to fix the breach",
"L0172":"180 Bangladeshis who had gone to Kyrgyzstan for promised garment and construction jobs, found no work or were cheated, returned home",
"L0174":"A welder's visa expired the day after he arrived; he worked seven months unpaid, was caught and served three months in jail",
"L0179":"A worker said his employer paid him Tk 10,000 in the first month and deducted Tk 7,000, saying he had paid the broker to bring them",
"L0181":"Garment workers were paid by the number of pieces sewn",
}
rows=list(csv.DictReader(open('facts.csv',encoding='utf-8')))
for r in rows:
    if r['id'] in fix: r['claim']=fix.pop(r['id'])
assert not fix, fix
w=csv.DictWriter(open('facts.csv','w',newline='',encoding='utf-8'),fieldnames=list(rows[0].keys()))
w.writeheader(); [w.writerow(r) for r in rows]
print("ok")
