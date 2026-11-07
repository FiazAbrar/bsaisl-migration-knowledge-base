"""Find a real date for sources marked undated or older than 6 Nov 2025.

For each such source in sources.csv it looks in the saved file for page-level date metadata
(article:modified_time / published_time, og:updated_time, JSON-LD dateModified / datePublished, <time datetime>,
"Tarikh Kemaskini", "Last updated", Bangla "কনটেন্টটি শেষ হাল-নাগাদ" (content updated; the site-wide
"সাইটটি শেষ হাল-নাগাদ" is ignored)), and asks the server for the Last-Modified header (HEAD only, no re-download).
Dates within 2 days of the access date are reported but flagged "same-day", since many servers generate them.

Writes raw/_datepass.csv (one row per source and candidate) for review. It changes nothing else.
  python3 ../../tools/datepass.py
"""
import csv, datetime, email.utils, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import BASE, RAW, CUTOFF  # noqa: E402
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
BN = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")
BN_MONTHS = {"জানুয়ারি": 1, "ফেব্রুয়ারি": 2, "মার্চ": 3, "এপ্রিল": 4, "মে": 5, "জুন": 6, "জুলাই": 7, "আগস্ট": 8,
             "সেপ্টেম্বর": 9, "অক্টোবর": 10, "নভেম্বর": 11, "ডিসেম্বর": 12}
EN_MONTHS = {m: i + 1 for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split())}
MS_MONTHS = {"januari": 1, "februari": 2, "mac": 3, "april": 4, "mei": 5, "jun": 6, "julai": 7, "ogos": 8,
             "september": 9, "oktober": 10, "november": 11, "disember": 12}


def iso(s):
    m = re.search(r"(20\d\d)-(\d\d)-(\d\d)", s)
    return f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else None


def dmy(text):
    t = text.translate(BN)
    m = re.search(r"(\d{1,2})\s*([A-Za-z\u0980-\u09FF]+)[,\s]+(20\d\d)", t)
    if not m:
        return iso(t)
    d, mon, y = int(m.group(1)), m.group(2).lower(), m.group(3)
    mo = BN_MONTHS.get(m.group(2)) or EN_MONTHS.get(mon[:3]) or MS_MONTHS.get(mon)
    return f"{y}-{mo:02d}-{d:02d}" if mo and 1 <= d <= 31 else None


def candidates(path):
    out = []
    try:
        s = open(path, encoding="utf-8", errors="replace").read()
    except Exception:
        return out
    pats = [
        ("meta-modified", r'(?:article:modified_time|og:updated_time|dateModified|last-modified)["\']?\s*(?:content=|:)\s*["\']?([0-9T:\-+ ]{10,})'),
        ("meta-published", r'(?:article:published_time|datePublished)["\']?\s*(?:content=|:)\s*["\']?([0-9T:\-+ ]{10,})'),
        ("time-tag", r'<time[^>]*datetime=["\']([0-9T:\-+ ]{10,})'),
    ]
    for kind, p in pats:
        for m in re.finditer(p, s, re.I):
            d = iso(m.group(1))
            if d:
                out.append((kind, d, m.group(0)[:80]))
    for kind, p in [("text-kemaskini", r"Tarikh\s*Kemaskini[^0-9\n]{0,20}([^\n<]{6,40})"),
                    ("text-updated", r"(?:Last\s*updated|Last\s*Update[d]?|Updated\s*on|Kemaskini\s*Terakhir)[^0-9A-Za-z\n]{0,10}([^\n<]{6,40})"),
                    ("text-bn-content", r"কনটেন্টটি শেষ হাল-নাগাদ করা হয়েছে[:\s]*([^\n<]{6,60})"),
                    ("text-published", r"(?:Published|Diterbitkan|Tarikh\s*Terbit|Posted\s*on)[^0-9A-Za-z\n]{0,10}([^\n<]{6,40})")]:
        for m in re.finditer(p, s, re.I):
            d = dmy(m.group(1))
            if d:
                out.append((kind, d, m.group(0)[:80]))
    return out


def head(url):
    p = subprocess.run(["curl", "-s", "-I", "-L", "-A", UA, "--max-time", "20", url], capture_output=True, text=True)
    lm = None
    for line in p.stdout.splitlines():
        if line.lower().startswith("last-modified:"):
            try:
                lm = email.utils.parsedate_to_datetime(line.split(":", 1)[1].strip()).date().isoformat()
            except Exception:
                pass
    return lm


def main():
    srcs = list(csv.DictReader(open(os.path.join(BASE, "sources.csv"), encoding="utf-8", newline="")))
    todo = [s for s in srcs if not s["page_date"] or s["page_date"] == "undated"
            or (s["page_date"] + "-01-01"[len(s["page_date"]) - 4:]) < CUTOFF]
    rows = []
    for i, s in enumerate(todo):
        files = [f for f in os.listdir(RAW) if f.startswith(s["raw"] + ".")]
        cands = []
        for f in files:
            if f.endswith((".html", ".md", ".txt")):
                cands += [(k, d, ev, f) for k, d, ev in candidates(os.path.join(RAW, f))]
        lm = head(s["url"]) if s["url"].startswith("http") else None
        if lm:
            cands.append(("http-last-modified", lm, "Last-Modified header", ""))
        if not cands:
            rows.append({"raw": s["raw"], "current": s["page_date"], "kind": "", "date": "", "flag": "", "evidence": "", "file": ""})
        seen = set()
        for k, d, ev, f in cands:
            if (k, d) in seen:
                continue
            seen.add((k, d))
            acc = datetime.date.fromisoformat(s["access_date"])
            try:
                same = abs((datetime.date.fromisoformat(d) - acc).days) <= 2
            except ValueError:
                continue
            rows.append({"raw": s["raw"], "current": s["page_date"], "kind": k, "date": d,
                         "flag": "same-day" if same else "", "evidence": ev.replace("\n", " "), "file": f})
        print(f"{i + 1}/{len(todo)} {s['raw']}: {len(cands)} candidates", file=sys.stderr)
    with open(os.path.join(RAW, "_datepass.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["raw", "current", "kind", "date", "flag", "evidence", "file"])
        w.writeheader(); w.writerows(rows)
    print(f"{len(todo)} sources checked; see raw/_datepass.csv")


if __name__ == "__main__":
    main()
