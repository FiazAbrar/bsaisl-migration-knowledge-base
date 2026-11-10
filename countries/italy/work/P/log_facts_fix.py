"""Re-run the three facts that failed in log_facts.py (argument errors)."""
import subprocess, sys
T = "../../../../tools/facts.py"
A = "interno-avr-2026"
rows = [
    ["--name", "gu-dl-146-2025", "--claim", "The special permit for victims of violence or serious exploitation (TUI art. 18(4)) now lasts one year instead of six months",
     "--quote", "sostituite dalle seguenti: �un anno� e dopo le parole", "--page-date", "2025-10-03", "--status", "possibly-outdated",
     "--note", "Art. 4(1)(a)(1): 'sei mesi' replaced by 'un anno'; the U+FFFD characters are garbled guillemets in the text copy"],
    ["--name", A, "--claim", "Italy's national AVR project (RVA&R system action) is run by IOM (Organizzazione Internazionale per le Migrazioni, OIM), which started it on 2 January 2024 for 36 months",
     "--quote", "Organizzazione Internazionale per le Migrazioni (OIM) in data 13 dicembre 2023", "--page-date", "2026-05-28", "--status", "verified",
     "--visa", "Assisted voluntary return", "--field", "operator", "--value", "IOM (OIM)"],
    ["--name", A, "--claim", "Counselling, pre-departure and return assistance under the IOM AVR project run until 2 February 2027",
     "--quote", "pre-partenza e assistenza al ritorno fino al 2 febbraio 2027", "--page-date", "2026-05-28", "--status", "verified",
     "--visa", "Assisted voluntary return", "--field", "applications/departures end date", "--value", "2 February 2027"],
]
for r in rows:
    p = subprocess.run([sys.executable, T, "add", "--prefix", "P"] + r, capture_output=True, text=True, encoding="utf-8")
    print((p.stdout + p.stderr).strip(), "|", r[3][:80])
