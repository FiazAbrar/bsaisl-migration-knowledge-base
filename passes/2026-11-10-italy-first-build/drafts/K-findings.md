# K findings: gaps in Decreto Flussi Step 5 (VFS fee, appointment, checks) and Step 7 (after arrival)

Agent K, 10 November 2026. Staging folder: `countries/italy/work/K/` (facts.csv K0001-K0117, sources.csv 31 sources: 25 official, 2 news, 2 NGO, 1 operator, 1 VFS counted as official per W's convention). `addfacts.py` logged K0001-K0111; K0112-K0117 were added by a one-off call. **Do not re-run `addfacts.py`** (it appends; a double run was already deduplicated once).

This file fills the gaps W left. Step 5 below gives only the additions to W's Step 5 (insert where marked). Step 7 is a full replacement for W's Step 7: it keeps W's facts (W ids) and adds K's. Section b explains the merges.

## a. Draft doc text

### Step 5: The visa at the Italian Embassy in Dhaka, and checking it is real

**Insert in W's item 1 ("Register on VFS's work-visa webform"), after sub-step 3:**

   4. After you register, the Embassy checks the nulla osta and then gives you an appointment; in December 2025 it said this takes a few days for a 2025 nulla osta [K0010, W0126]. Holders of a 2023 or 2024 nulla osta were told to wait until the immigration office in Italy finished its review, after which VFS contacts them [K0011].

   > **Need to know**
   > - In 2026, how many days pass between registering a nulla osta on the VFS webform and getting the appointment email?
   > - Does VFS sell paid "premium" or "prime time" appointment slots for Italian work visas in Dhaka, and do brokers resell them?

**Replace the last paragraph of W's item 2 ("You may file only one visa application ... cash in taka") with:**

   You may file only one visa application at a time, even with two passports [W0116]. At VFS you pay, in cash in taka [W0107, W0108]:

   - the visa fee: BDT 16,240 (EUR 116) [K0002, W0107];
   - the VFS service charge: BDT 5,320 (EUR 38), VAT included [K0001, K0004];
   - a bank draft charge: BDT 270 [K0003].

   That is BDT 21,830 in all, at the Embassy's rate of 1 euro = 140 taka [K0002, K0001, K0003, K0005]. The VFS charge already includes SMS and email notifications, photocopies, the photo booth and help filling in the form [K0006]. You do not give fingerprints for a long-term (D) visa [K0008]. Bring four recent colour photos, 4.0 x 3.5 cm, white background [K0009].

   **Scams:** the Embassy says only the official fees apply, and that paying intermediaries risks cancellation of the visa and legal action [K0012].

   > **Need to know**
   > - Which applicants pay the lower visa fee of BDT 12,600 (EUR 90) that VFS also lists for work visas?
   > - What do Dhaka agents charge in 2026 to "book" a VFS appointment or fill in the visa form, on top of the BDT 21,830?

**Add to W's "Check it is real" list:**

5. **VFS messages.** Notifications about your application come from VFS by SMS and email, included in the service charge [K0006].

> **Need to know**
> - Can a worker check a visa sticker's number online (as with the Schengen VIS), or only by writing to visti.dhaka@esteri.it?
> - Can the worker (not the employer) see the nulla osta's status on the Interior Ministry's ALI portal or at the SUI, and how?

### Step 7: After arrival

You have 8 working days from entry to apply for the permesso di soggiorno (residence permit), and 15 days to sign the contratto di soggiorno (contract of stay) [W0060, K0040, W0041].

1. **Sign the contratto di soggiorno within 15 days of entering Italy.** You and the employer sign it, digitally or you by hand, and the employer uploads it to the SUI on the ALI portal within the same 15 days [W0041, W0042, W0141, W0019]. You may work on the nulla osta while it is being signed [W0043]. If it is not sent in time the nulla osta is revoked, unless the delay was not your fault [W0038].

   > **Need to know**
   > - Do SUIs still call workers in person after arrival (for the integration agreement, the codice fiscale and the kit), or is everything now done online by the employer?

2. **Get your codice fiscale (tax code).** The codice fiscale is a 16-character code that identifies you to every public office; you need it to enrol with the health service and choose a doctor [K0054]. For a worker coming on a nulla osta, the SUI (Sportello Unico per l'Immigrazione, the immigration desk at the Prefettura) gives it [K0051].

   1. The SUI first gives a provisional code made only of numbers [K0052].
   2. The permanent code, of letters and numbers, is assigned when your permit is issued [K0053]. It never expires [K0055].
   3. If your details produce the same code as someone else's, the SUI sends you to any Agenzia delle Entrate (tax agency) office for a permanent one [K0056].

   If you have no codice fiscale at all, go to any Agenzia delle Entrate office with form AA4/8, filled in and signed, and your passport with visa or your permit [K0057]. The Agenzia publishes its guide to the codice fiscale for foreigners in Bengali [K0058].

   > **Need to know**
   > - With only the provisional numeric code from the SUI, do banks, phone shops and the comune accept it, or do they ask for the permanent code?

3. **Apply for the permesso di soggiorno through the SUI and the post office.** If you have a nulla osta, the SUI fills in the permit application and hands it to you in an envelope; you then take it to a post office with a Sportello Amico (the post-office counter that accepts permit applications) [K0015, K0016]. Comuni and patronati (union-linked advice offices) can also fill in the yellow-band kit free of charge [K0018, K0017]. Only you can hand it in, not a lawyer or agent [K0032].

   You'll need [W0133, W0138, K0034, K0035, K0036, K0020]:

   - the application from the SUI (or the yellow-band kit, one per person);
   - a copy of the nulla osta and of the signed contratto di soggiorno;
   - proof of where you live: a residence certificate, or a dichiarazione di ospitalità (the host's declaration that you live with them) with the rental contract and a copy of the host's ID;
   - a copy of your codice fiscale, if you already have it;
   - A4 copies of every passport page with your details, visas and stamps;
   - a copy of the UNILAV (the employer's hiring notice to the job centre);
   - money, below.

   **What it costs** [K0021, K0022, K0023, K0047, K0048, K0033, W0135, W0136]:

   - EUR 16 revenue stamp (marca da bollo), bought at a tabaccheria (tobacconist);
   - EUR 30 paid to the post office clerk when you hand in the envelope;
   - one postal payment slip (bollettino) for EUR 30.46 (the permit card) plus a contribution: EUR 40 for a permit up to 1 year (slip total EUR 70.46), EUR 50 for a permit over 1 and up to 2 years (slip total EUR 80.46).

   A permanent contract gives a permit of up to 2 years, a fixed-term one up to 1 year, so expect EUR 126.46 or EUR 116.46 in all [W0057, W0058, K0021, K0022, W0136, W0135].

   1. **Book a slot** at a Sportello Amico post office on poste.it or the Poste Italiane app (optional, saves queueing) [K0031]. The list of Sportello Amico offices is on poste.it, or call 800.200.309 free, Monday to Saturday, 8:00 to 20:00 [K0030].
   2. **Fill in the bollettino** for the card plus contribution; slips are at every post office [K0024].
   3. **Hand in the envelope open,** with your passport for identification and all copies [K0019, K0020].
   4. **Keep the two papers the clerk gives you** [K0025, K0027]:
      - the ricevuta (receipt), with codes to follow your application on portaleimmigrazione.it;
      - the letter calling you to the Questura (the provincial police immigration office), with date, time and place; if no date can be set yet, the letter says it will come by registered post to the Italian address you gave [K0028].
   5. **Go to the Questura on the date** for fotosegnalamento (photo and fingerprints) [K0041, K0029]. Bring the original passport and originals of every document copied into the kit, the post-office receipt, the appointment letter and 4 passport-size photos [K0117, K0038, K0037].
   6. **Check when the card is ready** on poliziadistato.it after the fingerprint appointment [K0029]. The card shows your photo, fingerprints, codice fiscale and reason for stay [K0041, K0042].

   **What the receipt allows:** with the receipt of a first work-permit application you have the same rights as a permit holder, you are lawfully present and you may work while you wait, unless the police notify you and your employer of a reason to refuse [K0044, W0143, K0045]. Keep it with your passport: it lets you move around in Italy [K0026].

   **How long it takes:** by law the permit is issued within 90 days [W0063, W0064]. In practice Questure are far slower in some cities: in March 2024 Florence organisations reported first appointments being set for September 2025, and in February 2025 protesters there put the average wait to collect a permit at 1 year, 6 months and 15 days [K0108, K0109]. In January 2025 a man died of cold outside the Rome Questura's immigration office, where people queue overnight for appointments [K0110].

   > **Need to know**
   > - How long after the post-office kit are Questura fingerprint appointments being set in Rome, Milan, Venice, Bologna and Naples in November 2026?
   > - How long after fingerprints does a first work permit actually arrive in those cities in 2026?
   > - Can a worker holding only the first-issue receipt fly to Bangladesh and back (direct flight to Italy), and what do Questure tell Bangladeshi workers in 2026?

4. **Sign the Accordo di integrazione (integration agreement).** Every newcomer over 16 asking for a permit of at least one year signs it with the state, at the SUI for a work permit; without it the permit is not issued [K0092, K0046, K0039, K0090]. You get a copy in a language you choose, or in English [K0093].

   - **How it works:** you start with 16 credits and must reach 30 credits within two years, including spoken Italian at level A2 and basic knowledge of the Constitution and civil life (health, school, work, tax) [K0095, K0099, K0105, K0096, K0097]. If you have children, you commit to send them to school [K0098].
   - **The civic course:** a free session of 5 to 10 hours, within three months of signing; missing it costs 15 of your 16 credits [K0100, K0101, K0102].
   - **Earning credits:** without certificates, the SUI can test you, also at a CPIA (public adult-education centre) [K0103]. Enrolling with the health service and choosing a doctor gives 4 credits (item 6) [K0082].
   - **The check:** one month before the two years end, the SUI asks you to send documents within 15 days and offers a free test [K0104]. 30 credits or more closes the agreement; 1 to 29 extends it one year; zero or less means the permit is revoked or not renewed and you are expelled [K0105, K0106, K0107, K0091].

   > **Need to know**
   > - Do Prefetture in 2026 actually call Bangladeshi workers to the civic session, and is it in person or online?
   > - Has any Bangladeshi worker had a permit refused for failing the integration agreement check?

5. **Register your residence at the comune (iscrizione anagrafica).** Every non-EU citizen with a regular permit who lives in a comune must register in its anagrafe (population register), on the same terms as Italians [K0059, K0073]. You can register before the permit card arrives [K0062, K0071].

   You'll need (Rome and Milan lists for a worker awaiting the first work permit) [K0061, K0062, K0112, K0113, K0070, K0114, K0115, K0116]:

   - valid passport;
   - the post-office receipt of the permit application;
   - the SUI nulla osta, the contratto di soggiorno and the permit application filed at the SUI;
   - codice fiscale (Milan asks for original and copy);
   - if others already live in the flat, a declaration from the resident accepting you, with a copy of their ID [K0063].

   1. **Rome:** fill in the ministerial residence form, sign it, and hand it to the anagrafe office of your Municipio in person, by PEC (certified email) or ordinary email, or by registered letter, with a copy of your ID [K0064]. It is free [K0065]. The office registers you within two working days, and registration counts from the day you declared [K0060].
   2. **Milan:** apply online on the comune's form "Cambio di residenza per persone straniere provenienti dall'estero" and upload the documents; files sent by email are ignored, and each file may be up to 7MB [K0068, K0069]. If you live as a guest, upload the host's consent declaration with the host's details and the rental or ownership references [K0072].

   After every permit renewal, renew your declaration of residence at the anagrafe within 60 days, or you are removed from the register one year after the permit expires [K0066, K0067].

   > **Need to know**
   > - Do comuni with many Bangladeshis (Rome Municipio V and VI, Milan, Venice-Mestre, Monfalcone, Palermo) accept a "residenza" at a shared flat where the landlord refuses to sign, and what do brokers charge for a residence address?

6. **Enrol with the health service (SSN) and choose a doctor.** As an employed worker you must enrol in the SSN (Servizio Sanitario Nazionale, the national health service) and you get the same care as Italians; your dependent family members are covered too [K0078, K0079]. Go to the ASL (Azienda Sanitaria Locale, local health authority) of your comune of residence, or if not yet resident, of the address on your permit [K0081, K0080].

   You'll need [K0085, K0086, K0083, K0054]:

   - your permit or the post-office receipt of the application;
   - with only the receipt: your employment contract or last payslip;
   - codice fiscale;
   - a signed undertaking to report any change in your status.

   1. **Choose your medico di base** (family doctor) at the ASL counter; this also earns 4 integration credits [K0082].
   2. **Collect the tessera sanitaria** (health card). With only the receipt, it is given on showing your passport and visa, and enrolment lasts up to 3 months, extendable [K0087, K0088]. Enrolment ends when the permit expires or is revoked [K0084].

   > **Need to know**
   > - In Rome and Milan in 2026, does the ASL enrol a newly arrived worker with only the post-office receipt and the provisional numeric codice fiscale?

7. **Get an identity card (carta d'identità), if you want one.** Once registered as a resident, you can ask the comune for an electronic identity card (CIE); for non-EU residents it is valid only as ID in Italy, not for travel abroad [K0074]. In Rome, show a valid ID and your permit, book on prenotazionicie.interno.gov.it, and pay EUR 22.21; the card comes by post within 6 days [K0075, K0077, K0111, K0076].

8. **SIM card and bank account.** Phone operators ask for your name, surname and codice fiscale and check your ID document when you activate a SIM [K0089]. For opening a bank or post-office account, see Sending money home.

   > **Need to know**
   > - Which operators' shops in Rome and Milan sell a SIM to a worker with only a passport and the provisional codice fiscale, and what do they charge?

## b. Notes (for notes.md)

**Searched:** poste.it (permit guide, Italian and English), poliziadistato.it (articolo 225 PDF; questure.poliziadistato.it Treviso kit guide, May 2024), Normattiva (TUI arts 4-bis, 6, 34; DPR 179/2011 arts 1-6), agenziaentrate.gov.it (mini guide page, EN guide PDF; Bengali PDF exists), salute.gov.it (extra-UE page), ASL Roma 1, AUSL Modena form, ASL Roma 3 (ISS/Ministry 2013 leaflet), comune.roma.it (anagrafe and CIE pages), comune.milano.it (Firecrawl: residence form, extra-UE document list), VFS one-pager (copied from F's folder after a 403 on my fetch), ho-mobile support. Searches in English, Italian and Bangla ("ইতালি ভিসা ভিএফএস অ্যাপয়েন্টমেন্ট নুলাওস্তা ২০২৬", "tempi di attesa questura permesso di soggiorno 2026", "iscrizione anagrafica ricevuta primo rilascio", "codice fiscale stranieri sportello unico", "attivare SIM straniero codice fiscale").

**Key findings and conflicts:**
- The EUR 30 post fee is confirmed officially by Poste Italiane (K0022): W's open question answered. The task brief's "EUR 30.46 post fee" is a mix-up: EUR 30.46 is the card, EUR 30.00 the post-office fee. Full first-permit cost: EUR 116.46 (1-year permit) or EUR 126.46 (2-year).
- Deadline: Poste says "8 giorni" (K0014), Polizia and the TUI "8 giorni lavorativi" (K0040, W0060). Draft uses 8 working days.
- Permit issue time: Polizia page says "in media 60 giorni" (K0043, logged as conflict with W0063, 90 days after D.Lgs. 83/2026). Draft uses W0063.
- Poste (K0015): for a nulla osta holder the SUI fills in the permit application. This sits oddly with the 2025-26 digital contratto di soggiorno (W0041): if workers no longer visit the SUI, who fills the kit? Kept as Need to know in item 1.
- VFS lists a work visa fee of "16240/12600" (116/90 EUR); the Embassy's cost page (W0107) gives EUR 116 for a D visa. Draft uses 116 and asks who pays 90.
- Codice fiscale: the Agenzia guide (2023) says the SUI gives a provisional numeric code for work entries and the permanent one comes with the permit; answers W's question.
- Residence with only the receipt: Rome (circular 43/2007) and Milan both list the receipt + contratto di soggiorno + nulla osta, so registration before the card is officially possible (answers W's question for anagrafe). For the SSN, AUSL Modena's form accepts the receipt plus contract or payslip, and the ISS/Ministry leaflet (2013) says the tessera sanitaria is issued on the receipt for up to 3 months.
- Integration agreement: DPR 179/2011 as in force 10 Nov 2026 (16 credits, A2, 30-credit threshold, 5-10 hour session within 3 months, 15 credits lost if missed). Salute.gov.it: choosing a GP gives 4 credits.
- Questura waits: no official data found; only NGO/news evidence from Florence and Rome (K0108-K0110). These are mostly renewals/asylum queues; first-issue work permits may be faster.

**Facts logged but not used:** K0007 (nulla osta mandatory, duplicates W), K0013 (TBS: 8,000 of 40,000 pending cases resolved by Aug 2025, for N), K0014 (Poste "8 giorni", conflicts in wording), K0043 (conflict, 60 days average), K0049 (EUR 100 contribution for long-term/art. 27 permits: useful to W's Blue Card and long-term sections), K0050 (permits up to 3 years for permanent work, circular 2023: W may want it in Your residence permit), K0094 (agreement signed with the permit application at SUI or Questura; K0039 used instead).

**Practice:** Florence Questura appointments set 18 months ahead (2024); people sleeping in queues outside Questure; Milan moved asylum bookings to NGOs/unions. No 2026 data on first-issue work permits.

## c. Blocked pages

- https://visa.vfsglobal.com/one-pager/italy/bangladesh/english/ : 403 for me; F fetched it on 10 Nov 2026 (copied as `vfs-italy-bd-visa-info`). The lead's merge will see identical files.
- https://prefettura.interno.gov.it/sites/default/files/13/2024-04/accordo_di_integrazione.docx : `prefettura-accordo-integrazione-modulo` (403; Wayback not tried). Would show the agreement form a worker signs.
- https://www.salute.gov.it/new/it/tema/assistenza-sanitaria-paesi-extra-ue/ "Come fare l'iscrizione obbligatoria al SSN" (JS tab; link not resolvable with curl): `salute-iscrizione-obbligatoria-ssn` would give the Ministry's own document list.
- https://www.portaleimmigrazione.it/ (JS): status check with the receipt's username/password; would prove what the worker sees.
- https://questure.poliziadistato.it/stranieri/ (JS): permit-status check by the Questura.
- https://ambdhaka.esteri.it/wp-content/uploads/2025/05/Work-1-of-2.png and Work-2-of-2.png (listed by W): Embassy "Information for work visa applicants" may state appointment rules and waits.
- The Embassy's 8 December 2025 notice itself (reported in K0010-K0011 by Bangladesh Pratidin): not found on ambdhaka.esteri.it; likely an image or Facebook post. Suggested name `ambdhaka-notice-work-visa-appointments-2025-12`.
- Operator pages (tim.it, windtre.it, iliad.it) on documents for foreigners: none found that state the rule; the legal source (the identification duty for SIM sales) was not located.

## d. Insider questions

- In 2026, how many days from VFS webform registration to the appointment email?
- Does VFS Dhaka sell premium appointment slots for Italian work visas, and do brokers resell them?
- Who pays the BDT 12,600 (EUR 90) work visa fee that VFS also lists?
- What do Dhaka agents charge in 2026 to book a VFS appointment or fill the form?
- Can a worker check an Italian visa sticker online, or only by email to the Embassy?
- Can the worker (not the employer) see the nulla osta's status on ALI or at the SUI?
- Do SUIs still call workers in person after arrival, and who fills in the permit kit if the contract of stay is signed online?
- Do banks, phone shops and comuni accept the provisional numeric codice fiscale?
- How long after the kit are Questura fingerprint appointments set in Rome, Milan, Venice, Bologna and Naples in November 2026?
- How long after fingerprints does a first work permit arrive in those cities in 2026?
- Can a worker with only the first-issue receipt fly to Bangladesh and back?
- Do Prefetture call Bangladeshi workers to the civic session in 2026, in person or online?
- Has any Bangladeshi worker lost a permit over the integration agreement check?
- Do comuni with many Bangladeshis accept residence at a shared flat without the landlord's signature, and what do brokers charge for a residence address?
- Does the ASL in Rome and Milan enrol a new worker with only the receipt and provisional codice fiscale?
- Which phone shops in Rome and Milan sell a SIM with only passport and provisional codice fiscale, and at what price?
