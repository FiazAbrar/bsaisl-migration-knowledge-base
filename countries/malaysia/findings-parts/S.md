# Part S findings: Student Pass; changing visa type; asylum; children born in Malaysia

Researcher: part S. Accessed 6 Nov 2026. Ledger: `ledger-parts/S.csv` (S0001-S0143), facts: `ledger-parts/S.facts.csv`.

**Method notes.**
- EMGS (Education Malaysia Global Services, the company under the Ministry of Higher Education that runs student-visa applications) and IMI (Immigration Department) pages fetch with curl. Several EMGS URLs (`/student-visa`, `/apply-student-visa-online`, `/social-visit-pass`, `/apply-for-online-distance-learning`, `/step-1-...`) return only the EMGS login page: the application form sits behind an account.
- pandoc drops HTML tables and `<option>` lists (they show as `[TABLE]`). For those pages I made a full text copy from the saved HTML (`raw/<name>.txt`, first line "TEXT COPY of ...") so quotes from tables/options can be checked: emgs-fees-calculator, emgs-faq, emgs-insurance-2026, emgs-registered-clinic, emgs-refund-policy, emgs-track-application, emgs-visa-home, emgs-contact, imi-student-pass, imi-faq-graduate-svp, mqa-mqr-search, jpn-*.
- UNHCR sites block curl (403); four help.unhcr.org/malaysia pages were scraped with Firecrawl and saved as excerpts (relevant sections verbatim). Dates come from each page's `helpsearch-lastupdated` timestamp.
- Almost all EMGS, IMI and JPN pages are undated, so most rows are `possibly-outdated`. JPN pages carry a site-wide footer "Tarikh Kemaskini: 6 November 2026" that looks auto-generated; treated as undated. The EMGS Schedule of Fees PDF is dated 23 June 2026 (verified). UNHCR pages are dated May-Oct 2026 (verified).
- I also cited pages other parts had already fetched: imi-ltsvp, imi-plks, imi-svp-short-term, esd-dependant-pass, esd-online-guidebook-v6-2025, bdhckl-consular-services, imi-semakan-online.

---

## 1. Student Pass (feeds the "Student visa" H2)

### Who it is for and which institutions count
- A Student Pass is an Immigration pass to stay legally to study at an approved institution [S0023].
- Eligible: an offer from a public university (UA), or from a private higher education institution (IPTS) that KPT (Ministry of Higher Education) approved, whose programme MQA (Malaysian Qualifications Agency) accredited, and that has KDN (Home Ministry) permission to take international students; language, training/skills and accredited centres need KPM/KESUMA approval plus KDN permission [S0001].
- Entry level: 12 years of schooling and a recognised exam [S0043]. Full-time only (except mobility programmes), one degree at a time [S0042].
- Public universities go through the same EMGS/STARS route (IMI's rule covers UA and IPTS together; the fee calculator has "New Application for IPTA" RM1,728) [S0002, S0060]. Public-university students can do the medical at the university clinic [S0066].
- **Checking the course:** the MQR (Malaysian Qualifications Register, www2.mqa.gov.my/mqr) lists only accredited programmes, tied to the campus named; "no record" can mean provisional accreditation only (check www2.mqa.gov.my/pasp), never accredited, or failed; search by qualification name and type [S0084-S0087].
- **Need to know:** a public, searchable official register of IPTS registered with KPT and holding KDN permission to recruit international students (jpt.mohe.gov.my "IPT Swasta" page is empty; MOHE links only an internal directory app). Searched mohe.gov.my, jpt.mohe.gov.my, educationmalaysia.gov.my; Malay "senarai IPTS berdaftar", "semakan status IPTS".

### Steps
1. Offer letter, accepted [S0024, S0047].
2. Apply from **outside Malaysia only**, online via EMGS STARS (visa.educationmalaysia.gov.my, EMGS HUB app) or by the institution [S0002, S0024].
3. EMGS academic screening and "Approval to Study"; complete files go to Immigration HQ's Student Pass Unit for eVAL with travel-document and security checks [S0003]. Missing documents within 14 working days of EMGS returning the file [S0020]. Stages list [S0025].
4. eVAL (electronic Visa Approval Letter) issued; valid 6 months; no entry before it [S0027, S0028]. EMGS charter: 14 working days for a complete application [S0026].
5. Single Entry Visa: Bangladesh on EMGS's SEV list; apply on eVISA (malaysiavisa.imi.gov.my), not possible from inside Malaysia; EMGS lists Dhaka as the mission [S0004, S0005, S0029, S0053, S0054]. RM20 [S0065].
6. Arrive: EMGS ISAC counter (24 hours) at KLIA T1 (Level 3 arrival hall, before immigration) and T2 (Level 3A after the Skybridge) [S0082, S0083].
7. Report to the institution and do the post-arrival medical at an EMGS panel clinic within 7 days (EMGS says 7 working days); without it EMGS cannot start the endorsement; failed medical can be appealed at the same clinic within 3 days [S0006, S0055, S0056, S0030]. Panel clinic list on EMGS site and app [S0058].
8. Institution applies for the sticker with: original passport, its request letter, EMGS sticker support letter, stamped Personal Bond, 12-month Malaysian insurance [S0017]; then the pass is issued at the immigration office for the institution's address [S0006].

### Documents
Photo 35x45mm white background; passport data page, visa pages, observation page; passport valid 18+ months (EMGS recommends 12 months beyond the course for a one-off pass; IMI: copy of all pages incl. cover); offer letter; Health Declaration Form; certificates and transcripts; English certificate (MUET, IELTS, TOEFL, PTE, Cambridge, Linguaskill, OET, ELS CIEP; without it the pass will not cover the whole course) [S0045-S0048, S0050, S0019].

### Costs
- EMGS fee calculator: new application RM1,728 (IPTS or IPTA; RM1,600 + 8% service tax), short course RM864, private education institute (IPS, e.g. language centre) RM540, IPTS renewal RM270; medical RM340 (Sarawak RM350); Student Pass RM60; eVAL RM159; i-Kad RM50 (self-collect) or RM60.60 (courier); insurance RM498-644 a year or own policy via the institution; multiple-entry visa for Bangladesh RM20; course fees not included; 8% tax on processing fees since 1 Mar 2024 [S0060-S0066]. IMI: Student Pass RM60 [S0007].
- Personal bond, Bangladesh band: RM750, lodged with the institution, returned at completion or withdrawal if no immigration breach [S0059, S0049].
- EMGS schedule of fees, updated 23 Jun 2026 [S0068, S0069].
- Refunds: first-year processing and eVAL fees not refundable once invoiced; students can claim only for applications they created themselves; immigration fees refunded only if the pass was not issued [S0077-S0079].

### Insurance
Compulsory and bought locally; EMGS insurance covers from date of entry; top up if it ends before the pass [S0031, S0075, S0076].

### Validity, renewal, attendance, stopping study
- Usually up to 1 year at a time; renew before expiry, ideally 3 months before [S0032, S0033].
- Renewal needs CGPA 2.0 and 80% attendance, else an explanation letter from the institution; the renewal file includes results and attendance record [S0051, S0018]. No new medical for renewal [S0057].
- Changing course: Variation once, within 18 months after the first semester, Bachelor's level or above, with a release letter from the old institution; otherwise the institution shortens the pass with a Check Out Memo and the student must leave before reapplying; if no Student Pass yet, the student must leave [S0034-S0036, S0052]. Progression within 3 months of finishing [S0037].
- Breaking any condition: Immigration may cancel the Student Pass [S0016].
- **Need to know:** the official penalty for working or otherwise breaching pass conditions (Immigration Regulations 1963 reg. 39; employer offence Immigration Act s.55B). Blocked; see below.

### Can students work?
- IMI: only students at public universities and IPTS; not language, training or accredited centres [S0012]. Semester and festive breaks only, max 20 hours a week, at restaurants, petrol stations, mini markets, hotels, or on campus [S0013]; no front-desk work; never act as a student-recruitment agent [S0014].
- EMGS: 20 hours a week "ONLY during semester breaks or holidays of more than 7 days", with prior Immigration approval; not as cashiers; in hotels not as singers, masseurs, musicians or GROs (guest relations officers); nothing immoral [S0039, S0040].
- How: through the institution; the student goes in person with an institution representative to Immigration (Student Pass Unit at HQ or a state office) with the job offer, the institution's letter with semester-break dates, academic and attendance reports, passport and valid pass, and the employer's Labour Department (JTK) approval under section 60K of the Employment Act [S0041, S0015].

### Family of students
- IMI: only Master's or PhD students at UA/IPTS can bring dependants (spouse; children under 18 incl. step and adopted; disabled children of any age; parents; parents-in-law) on a Long-Term Social Visit Pass; language/training-centre students cannot; dependants may not work or do business [S0008-S0011]. Fee RM90 (IMI) [S0007]; EMGS processing RM250 new, RM140 renewal; dependant buys own insurance [S0067].
- EMGS FAQ: postgraduates can; Bachelor's students only from 17 listed countries, and Bangladesh is not one [S0038].
- **Conflict S0008 / S0038** (Master's/PhD vs "postgraduate" plus an undergraduate country list). For a Bangladeshi Bachelor's student both mean no.
- Applications go through STARS; relationship documents attested by the applicant's own embassy in Malaysia; foreign-language documents need a certified translation [S0021, S0022].

### How to check it is real
- EMGS Track My Application (visa.educationmalaysia.gov.my, menu Student Visa > Track My Application): enter passport (travel document) number and nationality, tick the terms box, press Track My Application [S0080]. IMI's own "Semakan Online" page sends Student Pass status checks to EMGS [S0081].
- **Need to know:** how to verify an eVAL PDF itself (QR/reference check), and whether IMI's pass-validity checker (imigresen-online.imi.gov.my/eservices/checkEpassValid) shows Student Pass stickers. Not on any EMGS/IMI page fetched.

### Scams (leads and unofficial practice only)
- Agents charging BDT 6-8 lakh or more and steering students to barely functioning colleges [S0134]; students told a student visa lets them work freely [S0135]. KPT reportedly closed colleges and tightened scrutiny of Bangladeshi applications; Bangladeshi enrolment reportedly up 45% to 11,000+ [S0136, S0137 leads]. (Prothom Alo op-ed, Sept 2026.)
- 2017 R.AGE/The Star: colleges with no real classes, students working illegally or paying agents to renew student visas to keep working; 26 institutions lost licences [S0138, S0139]; Dhaka Tribune 2017: agents took over RM20,000 [S0140].
- **Need to know:** any official warning from KPT/MOHE, EMGS, IMI, BD High Commission KL or the Bangladesh Ministry of Education about fake colleges or student-visa agents (none found on fetched pages; searched mohe.gov.my media statements, EMGS notices, bdhckl notices); an official list of institutions whose international-student permission was revoked.

### Graduate Pass (not open to Bangladeshis)
Social Visit Pass for 12 months after a Bachelor's or higher, work in permitted sectors without an employer; Malaysian sponsor earning RM1,500+ needed; RM600 plus RM600 per dependant plus MEV; cannot be extended; only 32 nationalities and **Bangladesh is not one** [S0044, S0070-S0074].

---

## 2. Changing visa type

- **Visit pass to work:** a short-term Social Visit Pass covers a list of social activities, none of them work, and is extended only for illness, accident or war [S0088, S0089]. A PLKS worker must be outside Malaysia while the employer's VDR/PLKS is processed and enters only after approval [S0090]. **Need to know:** an explicit official sentence that a Social Visit Pass cannot be converted to a work pass (not found in those words on IMI/ESD pages).
- **Visit pass to student:** the Student Pass applicant must be outside Malaysia when applying [S0002].
- **Student to work:** no automatic post-study route; the employer must apply for a work pass such as an Employment Pass [S0100]; Graduate Pass excludes Bangladesh [S0044]. **Need to know:** whether a Student Pass holder can switch to an Employment Pass inside Malaysia; any graduate route into RP-T (Residence Pass-Talent).
- **PLKS to anything else:** no change of sector or employer without KDN permission [S0091]; PLKS workers may not marry locals or other foreign workers [S0092]. **Need to know:** whether a PLKS worker can ever move to an Employment Pass.
- **Dependant to work:** Dependant Pass holders must get their own Employment Pass [S0093, S0094]; LTSVP family of EP holders may not work or study without converting [S0141]; student dependants may not work [S0011].
- **Spouse of a Malaysian citizen:** LTSVP up to 5 years; may work or run a business without changing pass, once the permission is endorsed in the passport; apply together with the Malaysian spouse at the Visa, Pass and Permit Division of the state where working, with documents including an RM10-stamped contract [S0095-S0099].

## 3. Asylum

- Malaysia is not party to the 1951 Refugee Convention and has no national asylum system; UNHCR does refugee status determination [S0101]; UNHCR recognition gives no legal immigration status [S0142].
- Refugees are treated as undocumented migrants: may be arrested, detained, fined, deported; no legal right to work formally; UNHCR cannot grant status or work permits or stop arrests [S0106-S0108].
- Leaving for work or study does not make someone a refugee [S0102].
- Process: request on UNHCR's My Services portal; no letters; paying anyone does not help; long wait [S0109, S0110]. A UNHCR card is not a visa [S0111]. Registration priority: requests from 2022 or earlier and vulnerable people [S0112]. Interviews only for priority cases; no timeline [S0103]. One appeal within 30 days, then the case closes [S0104]. Must tell the truth [S0105]. Services are free; anyone asking money is lying [S0143]. Unregistered pregnant women pay full foreigner fees [S0113].
- **Need to know:** UNHCR Malaysia figures by nationality (any Bangladeshis recognised); Immigration Act text (blocked).

## 4. Children born in Malaysia

- Register within 60 days at a JPN (National Registration Department) office; free [S0114, S0115]. Who may report [S0121]. Documents include form JPN.LM01 and the hospital birth confirmation; parents' ID or passports and marriage documents (original and copy) [S0116-S0118].
- Late (after 60 days): RM50 and many more documents; sponsors and witnesses may identify with a passport or UNHCR card [S0119, S0120]. Replacement extract RM5 [S0122].
- Citizenship: JPN confirms the status of a person born in Malaysia from the parents' citizenship [S0123]; a child born before the marriage was registered follows the mother [S0124]. **Need to know:** the Federal Constitution text (Second Schedule Part II: born in Malaysia is a citizen only if a parent is a citizen or permanent resident) — blocked; the non-citizen certificate marking (news lead only).
- Bangladesh side: a birth abroad must be registered with the mission (Births and Deaths Registration Act 2004) [S0127]. At the BD High Commission KL: JPN certificate attested by Malaysia's Foreign Ministry; parents' passport copies; e-apostilled marriage certificate; printed online form; 2 photos; child and both parents in person [S0125, S0126]. **Need to know:** the fee (blank on the page).
- Child's Bangladeshi e-passport: RM545 (48 pages, 5 years) or RM817 (64 pages, 5 years) in cash at Maybank, receipt in the child's name; Bangladeshi birth registration must show Malaysia as birthplace; parents' NIDs; marriage certificate attested by the Law Ministry, Foreign Ministry and High Commission; child must come; ESKL appointment compulsory [S0128-S0133] (page dated 28 May 2024, possibly outdated).
- **Need to know:** official position on children of undocumented parents (can JPN register them, does registration trigger enforcement, can the child get a pass). No official page found.

---

## Draft steps (for the writer)

### Student visa
1. **Check the course and institution before paying anyone.** On www2.mqa.gov.my/mqr type the course name in "Name of Qualification", choose the level and press Search; only accredited programmes at the campus listed appear [S0084-S0087]. The institution must be KPT-approved and have Home Ministry permission to take international students [S0001]. Need to know: where to check that permission.
2. **Get an offer letter** [S0047]. You need 12 years of schooling plus a recognised exam, and an English test certificate [S0043, S0050].
3. **Apply from Bangladesh**, yourself on visa.educationmalaysia.gov.my (or the EMGS HUB app) or through the institution [S0002, S0024]. Upload a 35x45mm white-background photo, passport pages (18+ months valid), offer letter, Health Declaration Form, certificates and English certificate [S0045-S0048, S0050]. Pay about RM1,728 processing, RM159 eVAL, RM340 medical, RM60 pass, RM20 visa, RM50 i-Kad and RM498-644 insurance [S0060-S0065]; lodge the RM750 personal bond with the institution (refundable) [S0059, S0049]. Send any missing papers within 14 working days [S0020]. If you apply yourself you can claim a refund before the institution decides; first-year processing and eVAL fees are not refundable once invoiced [S0077, S0078].
4. **Track it yourself** with your passport number and nationality on EMGS Track My Application [S0080]; complete files take about 14 working days [S0026].
5. **Get the eVAL** (valid 6 months) and then the Single Entry Visa on eVISA [S0028, S0029, S0053]. Never travel before the eVAL [S0027].
6. **Arrive** and use the ISAC counter at KLIA [S0082, S0083].
7. **Within 7 working days do the medical** at an EMGS panel clinic; appeal within 3 days if failed [S0055, S0056, S0030].
8. **The institution gets your sticker** with your passport, stamped bond and insurance [S0017].
9. **Keep the pass:** 80% attendance and CGPA 2.0; renew 3 months early; keep insurance valid [S0051, S0033, S0076].
10. **Work only as allowed:** university/IPTS students only, breaks only, 20 hours, listed workplaces, approved by Immigration through your institution [S0012-S0015, S0039-S0041]. Otherwise the pass can be cancelled [S0016].
11. **Family:** only Master's/PhD students; the spouse cannot work [S0008-S0011, S0038].
12. **Scams:** a promise of work on a student visa is false [S0039, S0135 unofficial]; reported agent fees BDT 6-8 lakh [S0134 unofficial].

### Changing visa type, asylum, children
As in sections 2-4 above (each bullet already cites its rows).

## Need to know (summary)
- Official register of KPT-registered IPTS with KDN permission for international students; list of revoked institutions (student visa, step 1).
- How to verify an eVAL; whether IMI's pass checker shows Student Pass (student visa, check step).
- Penalty text for working in breach of pass conditions (Immigration Regulations 1963 reg. 39; Immigration Act s.55B) — blocked.
- Official warnings (KPT, EMGS, IMI, BD HC KL, BD Ministry of Education) about student-visa scams.
- Student to Employment Pass inside Malaysia; graduate route to RP-T; PLKS to EP.
- Explicit official statement that a visit pass cannot become a work pass.
- Federal Constitution citizenship-by-birth text — blocked. Children of undocumented parents (official position).
- Birth registration fee at BD High Commission KL.
- UNHCR Malaysia statistics by nationality.

## Conflicts
- S0008 (IMI: dependants only for Master's/PhD students) vs S0038 (EMGS: postgraduates, plus undergraduates from 17 listed countries). Both exclude Bangladeshi Bachelor's students.

## Blocked
See `blocked-parts/S.md`.
