# s-check-sc: lines 1229-1602 (changed lines only)

### 1. UNSUPPORTED
- line: 1335
- old: the education authority's approval certificate (the university gets it);
- new: the Ministry of Education's or the emirate education authority's approval certificate;
- why: F0073 (icp-issue-residency-permit.md l.123) lists the certificate as a document; F0071 (regulation Art. 47-48) makes approval a condition. Neither source says the university obtains it.

### 2. FORMAT (wrong page name)
- line: 1339, 1381, 1452
- old: GDRFA's Visa Status page for Dubai (see Tourist visa, Step 4) / check the permit on GDRFA's Visa Status page (Dubai) / or GDRFA's Visa Status page (see Tourist visa, Step 4)
- new: replace "Visa Status page" with "Status Inquiry page" in all three
- why: V0188 (uae-portal-track-visa-validity.md l.6, l.11) links GDRFA's StatusInquiry_New.aspx; Tourist visa Step 4 (line 887) calls it the "GDRFA Status Inquiry page". "Visa Status" is not a name used by the source.

### 3. FORMAT (numbering)
- line: 1376
- old:    3. Or go to a GDRFA Customer Happiness Centre or an Amer centre, take a ticket and hand in the application and papers [SC0001].
- new: (drop the number; put it as an unnumbered line after the two online steps) Or go to a GDRFA Customer Happiness Centre or an Amer centre, take a ticket and hand in the application and papers [SC0001].
- why: SC0001 (gdrfa-green-visa-skilled.md) gives the centre route as an alternative channel to the online steps, not a third step after them. Numbered "3." reads as a step you do after paying online.

### 4. UNSUPPORTED
- line: 1427
- old: a work certificate showing your retirement and years of service, and either the municipality's property ownership and valuation certificates or a bank certificate of fixed annual income with 6 months' statements, plus health insurance [SC0009].
- new: a work certificate showing your retirement and years of service, and either the municipality's property ownership certificate with a valuation certificate from the competent authority or a bank certificate of fixed annual income with 6 months' statements, plus health insurance [SC0009].
- why: icp-issue-residency-permit.md l.150-160: ownership certificate is "issued by the municipality", but the valuation is "A certificate from the competent authority assessing the property value(s), or a mortgaged title deed...". (Note: the work-certificate line also offers an alternative "or a birth ..." that is cut off in the saved file; not flagged.)

### 5. UNSUPPORTED (minor)
- line: 1240
- old: through ICP's "Visa Extension" service (see Tourist visa, Step 6) [V0056, V0058].
- new: through the authority that issued it (ICP's "Visa Extension" service outside Dubai; see Tourist visa, Step 6) [V0056, V0058].
- why: V0056 (icp-visa-extension.md): the treatment permit "may be extended by the issuing authority". A Dubai-sponsored patient's visa is issued by GDRFA (line 1234), so "ICP's service" does not cover every patient.

### 6. UNSUPPORTED (minor)
- line: 1600
- old: Have the worker's passport copy, visa, UAE workplace and home address, the agency's name and address and the employer's mobile number [G0039].
- new: To ask the Ministry to help bring the worker home, have the worker's passport copy, visa, UAE workplace and home address, the agency's name and address and the employer's mobile number [G0039].
- why: G0039 (ministry-citizen-charter-2026.txt) lists these papers for the Ministry's repatriation help. It does not list them for the Welfare Board's legal help application (G0027), which is what the step is about.

Checked with no problems: medical steps (SB0003/SB0007/SB0008, fees 200/500 + VAT, deposit 1,000/2,000), ICP medical category (SB0004/V0029), companion rules (V0144/V0145), student docs and 60 days, MDX example (F0076), green visa docs, steps, AED 200 + 5% VAT + 520 (500+10+10), 48 hours (SC0001-SC0005), ICP 100/100/100 fees (F0093/F0107), golden visa links (SC0010), docs (SC0007), 6-month entry visa (F0103), remote work docs and fees (SC0011/SC0012), retirement service names (SC0013), change of status AED 500 (SC0008/F0014/F0019), 30-day grace (G0067), detained section phones, emails, travel permit form and WEWB items (G0079/G0089/G0086/L0210/G0112/G0131/G0036/G0040/B0061). All cross-references point to real sections. List nesting renders correctly. No leftover instructions.

TOTAL: 6 problems in lines 1229-1602
