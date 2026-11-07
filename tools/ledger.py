"""Evidence ledger helper. Every claim written in the doc needs a row here.

Each research topic writes its own part file (ledger-parts/<P>.csv) so parallel work never collides;
merge.py later joins them into ledger.csv and facts.csv.

Add a row (the quote is checked against the saved raw file; the run fails if it is not found):
  python3 ../../tools/ledger.py add --part W --raw imi-plks-2026 \
      --claim "PLKS is valid for up to 12 months at a time" \
      --quote "exact words copied from raw/imi-plks-2026.md" \
      --page-date 2026-03-01|undated \
      --status verified|possibly-outdated|conflict|unofficial|lead \
      [--visa PLKS --field validity --value "12 months"]   (adds a facts.csv row; official facts only)
      [--note "free text, e.g. conflicts with W0012"]
      [--no-quote-check --note "why"]                     (only for garbled Bangla PDF text: quote by page)

Register a source once (publisher/title feed the reference list):
  python3 ../../tools/ledger.py source --raw imi-plks-2026 --publisher "Immigration Department of Malaysia" \
      --title "Temporary Employment Visit Pass" --official yes|no|archived|news-archived [--page-date 2026-03-01|undated]
  (archived = an official page saved from the Wayback Machine by tools/wayback.py; source_type official-archived)

Status rules:
  verified            official source, page dated within the last 12 months
  possibly-outdated   official source, page older than 12 months or undated
  conflict            official sources disagree: add a row for EACH source with status conflict and a note naming the other id
  lead                news/NGO/agency fact, used only after an official search failed; cited as [N] under
                      "Needs an official source". Never for exact facts (fees, eligibility, documents, processing
                      times, legal rules): those become "Need to know" in the doc
  unofficial          news/NGO/agency report of what happens in practice, or an exact fact reported only
                      unofficially; written in the doc labelled "unofficial, not verified"
  source_type (official/news) is filled in from sources.csv: register the source BEFORE adding rows

  python3 ../../tools/ledger.py show --part W        list a part
"""
import argparse, csv, html, os, re, sys, unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import BASE, RAW, CUTOFF  # noqa: E402
PARTS = os.path.join(BASE, "ledger-parts")
LCOLS = ["id", "claim", "quote", "url", "access_date", "raw_file", "page_date", "source_type", "status", "note"]
FCOLS = ["visa_type", "field", "value", "ledger_id"]
SCOLS = ["raw", "url", "publisher", "title", "official", "page_date", "access_date"]
STATUSES = {"verified", "possibly-outdated", "conflict", "unofficial", "lead"}


def norm(s):
    s = unicodedata.normalize("NFKC", html.unescape(s))
    s = re.sub(r"\]\([^)]*\)", "]", s)          # drop markdown link targets
    s = re.sub(r"[\*_#>|\\\[\]`\"“”‘’' ​‌‍]", " ", s)
    s = s.replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", s).strip().lower()


def fetchlog():
    p = os.path.join(RAW, "_fetchlog.csv")
    with open(p, newline="", encoding="utf-8") as f:
        return {r["name"]: r for r in csv.DictReader(f)}


def text_files(raw):
    out = []
    for f in sorted(os.listdir(RAW)):
        if f.startswith(raw + ".") and f.rsplit(".", 1)[-1] in ("md", "txt"):
            out.append(f)
    return out


def rows(path, cols):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_row(path, cols, row):
    new = not os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        if new:
            w.writeheader()
        w.writerow(row)


def add(a):
    if a.status not in STATUSES:
        sys.exit(f"status must be one of {sorted(STATUSES)}")
    log = fetchlog()
    if a.raw not in log:
        sys.exit(f"raw '{a.raw}' is not in raw/_fetchlog.csv; fetch it (or --log it) first")
    files = text_files(a.raw)
    if not files:
        sys.exit(f"no raw/{a.raw}.md or .txt text copy found")
    if not a.no_quote_check:
        q = norm(a.quote)
        if len(q) < 12:
            sys.exit("quote too short; copy a full phrase or sentence")
        found = any(q in norm(open(os.path.join(RAW, f), encoding="utf-8", errors="replace").read()) for f in files)
        if not found:
            sys.exit(f"QUOTE NOT FOUND in {files}. Copy it exactly from the saved file (whitespace and markdown are ignored).")
    elif not a.note:
        sys.exit("--no-quote-check needs --note explaining why (e.g. 'garbled Bangla text layer, p.3')")
    pd = a.page_date
    if pd != "undated" and not re.fullmatch(r"\d{4}(-\d{2}(-\d{2})?)?", pd):
        sys.exit("--page-date must be YYYY, YYYY-MM, YYYY-MM-DD or 'undated'")
    # partial dates count from the start of the period (conservative): 2025-11 -> 2025-11-01
    full = pd + "-01-01"[len(pd) - 4:] if pd != "undated" else ""
    if a.status == "verified" and (pd == "undated" or full < CUTOFF):
        sys.exit(f"page date {pd} is undated or before {CUTOFF}: status must be possibly-outdated")
    src = [r for r in rows(os.path.join(BASE, "sources.csv"), SCOLS) if r["raw"] == a.raw]
    if not src:
        sys.exit(f"register the source first: python3 ../../tools/ledger.py source --raw {a.raw} ...")
    o = src[0]["official"].lower()
    stype = ("official" if o.startswith("y") else "official-archived" if o == "archived"
             else "news-archived" if o == "news-archived" else "news")
    if stype.startswith("news") and a.status in ("verified", "possibly-outdated"):
        sys.exit("a news source can only be lead, unofficial or conflict")
    if stype.startswith("official") and a.status in ("lead", "unofficial"):
        sys.exit("an official source should be verified, possibly-outdated or conflict")
    os.makedirs(PARTS, exist_ok=True)
    path = os.path.join(PARTS, a.part + ".csv")
    existing = rows(path, LCOLS)
    n = max([int(r["id"][len(a.part):]) for r in existing] or [0]) + 1
    rid = f"{a.part}{n:04d}"
    write_row(path, LCOLS, {"id": rid, "claim": a.claim, "quote": a.quote, "url": log[a.raw]["url"],
                            "access_date": log[a.raw]["access_date"], "raw_file": ";".join(files),
                            "page_date": pd, "source_type": stype, "status": a.status, "note": a.note or ""})
    if a.visa or a.field or a.value:
        if not (a.visa and a.field and a.value):
            sys.exit("give all of --visa --field --value (row was added without a fact)")
        if True:
            write_row(os.path.join(PARTS, a.part + ".facts.csv"), FCOLS,
                      {"visa_type": a.visa, "field": a.field, "value": a.value, "ledger_id": rid})
    print(rid)


def source(a):
    log = fetchlog()
    if a.raw not in log:
        sys.exit(f"raw '{a.raw}' not in fetch log")
    path = os.path.join(BASE, "sources.csv")
    if any(r["raw"] == a.raw for r in rows(path, SCOLS)):
        print("already registered")
        return
    write_row(path, SCOLS, {"raw": a.raw, "url": log[a.raw]["url"], "publisher": a.publisher, "title": a.title,
                            "official": a.official, "page_date": a.page_date or "", "access_date": log[a.raw]["access_date"]})
    print("registered", a.raw)


def show(a):
    for r in rows(os.path.join(PARTS, a.part + ".csv"), LCOLS):
        print(f"{r['id']} [{r['status']}] {r['claim']}  <{r['raw_file']}>")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd")
    x = sub.add_parser("add")
    for k in ("part", "raw", "claim", "page-date", "status"):
        x.add_argument("--" + k, required=True)
    x.add_argument("--quote", default="")
    for k in ("visa", "field", "value", "note"):
        x.add_argument("--" + k)
    x.add_argument("--no-quote-check", action="store_true")
    s = sub.add_parser("source")
    for k in ("raw", "publisher", "title", "official"):
        s.add_argument("--" + k, required=True)
    s.add_argument("--page-date")
    sh = sub.add_parser("show")
    sh.add_argument("--part", required=True)
    a = p.parse_args()
    {"add": add, "source": source, "show": show}.get(a.cmd, lambda _: print(__doc__))(a)
