# Saudi Arabia: pages we could not fetch

Merged from the per-topic notes in `blocked-parts/`. Ledger ids like [W0012] point to rows in ledger.csv.


- https://v.mc.gov.sa/Verification/PageVerify.aspx?lang=en -> manual/mc-cr-verify.pdf : old CR verification page; curl failed and Firecrawl reports DNS failure. Replaced by mc.gov.sa "Query about commercial registration data" (saved). Need a screenshot of a sample result (which fields show) from https://mc.gov.sa/en/eservices/Pages/Commercial-data.aspx.
- https://my.gov.sa/en/services/18443 -> manual/mygovsa-cr-query.pdf : 403 to curl; same CR query service, wanted for the result fields.
- https://www.linkedin.com/posts/helvetasbangladesh_safemigration-migrantrights-onlinecomplaint-activity-7490969164367630336-uAbo -> manual/helvetas-oep-complaint-module.pdf : curl failed, Firecrawl does not support LinkedIn. Need the steps (menu path) for filing a complaint in OEP's Online Complaint Management Module.
- https://www.facebook.com/probashi.gov.bd/posts/1505340118300034/ -> manual/mewoe-fb-online-complaint.pdf : ministry Facebook post on the OEP complaint module; Firecrawl does not support Facebook. Need the how-to text or images.
- https://www.facebook.com/HelvetasBangladesh/posts/1493009212868771/ -> manual/helvetas-fb-oep-complaint.pdf : Bangla how-to post for the OEP complaint module.
- https://employee.oep.gov.bd/ -> manual/oep-complaint-screens.pdf : JavaScript app behind login; need screenshots of the complaint form path inside a worker's OEP account.
- https://hrsd.gov.sa/en/news/hrsd-launches-%E2%80%9Cprofessional-verification%E2%80%9D-program-ensure-competence-skilled-workers-saudi-labor -> manual/mhrsd-pvp-2021.pdf : page saved (raw/mhrsd-professional-verification-2021) but the article body did not render; wanted for an official source on SVP certificate validity (5 years) and 50% pass mark.


# Blocked sources, part B (Work visa: company worker steps 4-9)

- https://vc.tasheer.com/appointment -> manual/tasheer-appointment.pdf : curl 403; Firecrawl returns only the cookie shell (JavaScript app). Need the Bangladesh booking flow (country Bangladesh, visa type Work).
- https://vc.tasheer.com/static/documentrequired -> manual/tasheer-documents-bangladesh-work.pdf : select Bangladesh, Dhaka centre, Work visa; need the official document list.
- https://vc.tasheer.com/static/visafees -> manual/tasheer-fees-bangladesh.pdf : select Bangladesh; need Tasheer's service fee for a work visa applicant.
- https://services.ksavisa.sa/home/DisplayAction/1 -> manual/ksavisa-permanent-work-visa.pdf : login wall; need the official permanent work visa requirements and documents.
- https://www.biman-airlines.com/manage-booking -> manual/biman-manage-booking.pdf : curl 403, Firecrawl redirected; need Biman's booking-check page (booking reference + last name).
- https://www.baira.org.bd/media/notice/PUi0gB2d4f8YoCsNlFdj.pdf : scanned, no text layer and no Bangla OCR on this machine; transcribed by hand into raw/baira-pdo-validity-3months.ocr.txt.
- https://objectstorage.ap-dcc-gazipur-1.oraclecloud15.com/.../office-probashi/2026/8/5786d973-....pdf (welfare fee circular): scanned; transcribed by hand into raw/ministry-welfare-fee-circular-2026-09.ocr.txt.
- https://rmp.gov.bd/pages/news/...পুলিশ-ক্লিয়ারেন্স-ফি... -> manual/rmp-pcc-fee-notice.jpg : notice body is an image; need the re-fixed police clearance fee amount and date.


- https://www.prothomalo.com/bangladesh/fc49bzl96y -> manual/prothomalo-visa-trading-2023.pdf : Prothom Alo 27 Mar 2023 on visa trading and unverified appointment letters (curl failed; not retried with Firecrawl because Bonik Barta 2024 covers the same scam)
- https://www.amnesty.org/fr/wp-content/uploads/2024/11/MDE2386872024ENGLISH.pdf -> manual/amnesty-saudi-2024.pdf : downloaded but no text layer (5 bytes); need a readable copy for reality check on wage insurance
- https://www.chi.gov.sa/en/ServicesDirectory/Pages/Eservices-CheckInsurance.aspx?servicename=checkinsurance -> manual/chi-check-insurance.pdf : live page and Firecrawl failed; Wayback copy (Jan 2026) saved, but it does not show which ID the form asks for


- https://www.arabianbusiness.com/abnews/saudi-family-visa-new-rules-2026 -> manual/arabianbusiness-family-visa-rules-2026.html : curl 403, Firecrawl not tried; not needed (official SPA text used), kept for completeness
- https://thefinancialexpress.com.bd/national/haab-announces-three-private-hajj-packages -> manual/fe-hajj-2027-private-packages.html : saved HTML has no article text; need the three private Hajj 2027 package prices
- HRSD "File a domestic labour lawsuit" (رفع دعوى عمالة منزلية) service page -> manual/hrsd-domestic-labour-lawsuit.html : URL not found by search; need the link, steps and whether a worker without Absher can file
- https://vc.tasheer.com/static/visafees -> manual/tasheer-visa-fees.html : curl 403; Firecrawl returned only the cookie banner (JS page); need Tasheer's Bangladesh fee table (service fee per visa type: family residence, family visit, business, student)
- https://probashi.gov.bd/pages/notices -> manual/probashi-notices.html : Firecrawl returns empty JS shell; need the ministry's notice list to find all approval orders for agencies sending women domestic workers


- https://amiprobashi.com/brac-service : DNS failure (curl 000, Firecrawl DNS error). Wanted: BRAC returnee services and the 16768 helpline. Ask a teammate to save the page.
- https://www.facebook.com/bcgjksa/ : Firecrawl doesn't support Facebook. Wanted: Jeddah consulate address and main phone (consulate site's address page is not_found).
- https://my.gov.sa/en/services/263551 : all Firecrawl engines failed. Wanted: official transit visa terms (fee, whether work is allowed).
- https://help.unhcr.org/ksa/en/contact-us/ and https://migrantprotection.iom.int/.../prottasha-leaflet.pdf : curl 403; read with Firecrawl (saved as *-fc.md).
- https://www.bb.org.bd/en/index.php/services/cipc_procedure : curl copy is a captcha page; read with Firecrawl (bb-cipc-procedure-fc.md).
