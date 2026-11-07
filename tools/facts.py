"""Log the evidence behind the doc. Run from inside the country folder.

Every fact in doc.md needs a row in facts.csv, backed by a source saved in sources/ (use fetch.py first).

1. Register a source once (publisher and title go into the doc's reference list):
  python3 ../../tools/facts.py source --name imi-plks-2026 --publisher "Immigration Department of Malaysia" \
      --title "Temporary Employment Visit Pass" --official yes|no|archived|news-archived [--page-date 2026-03-01|undated]
  (archived = an official page saved from the Wayback Machine by wayback.py)

2. Add a fact. The quote is checked against the saved text copy; the run fails if it isn't found:
  python3 ../../tools/facts.py add --prefix W --name imi-plks-2026 \
      --claim "PLKS is valid for up to 12 months at a time" \
      --quote "exact words copied from sources/imi-plks-2026.md" \
      --page-date 2026-03-01|undated \
      --status verified|possibly-outdated|conflict|unofficial|lead \
      [--visa PLKS --field validity --value "12 months"]   (structured fields the chatbot can use)
      [--note "free text, e.g. conflicts with W0012"]
      [--no-quote-check --note "why"]                     (only for garbled Bangla PDF text: quote by page)
  It prints the new id (e.g. W0013); cite it in doc.md as [W0013]. --prefix is one or two capital letters;
  when several people or agents work at once, give each its own letter so ids never clash.

Status:
  verified            official source, page dated within the last 12 months
  possibly-outdated   official source, page older than 12 months or undated
  conflict            sources disagree: add a row for each, with a note naming the other id
  lead                news, NGO or agency source, used only after an official search failed (cited [N] in the doc)
  unofficial          news, NGO or agency report of what happens in practice (cited [N] in the doc)

3. Check what a stretch of the doc cites:
  python3 ../../tools/facts.py cited doc.md [start_line] [end_line]
"""
import argparse, csv, html, os, re, sys, unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import BASE, RAW, CUTOFF  # noqa: E402

FACTS = os.path.join(BASE, "facts.csv")
SOURCES = os.path.join(BASE, "sources.csv")
FCOLS = ["id", "claim", "quote", "saved_file", "url", "page_date", "access_date", "source_type", "status",
         "visa", "field", "value", "note"]
SCOLS = ["name", "url", "publisher", "title", "official", "page_date", "access_date"]
STATUSES = {"verified", "possibly-outdated", "conflict", "unofficial", "lead"}


def norm(s):
    s = unicodedata.normalize("NFKC", html.unescape(s))
    s = re.sub(r"\]\([^)]*\)", "]", s)          # drop markdown link targets
    s = re.sub(r"[\*_#>|\\\[\]`\"“”‘’' ​‌‍]", " ", s)
    s = s.replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", s).strip().lower()


def fetchlog():
    with open(os.path.join(RAW, "_fetchlog.csv"), newline="", encoding="utf-8") as f:
        return {r["name"]: r for r in csv.DictReader(f)}


def text_files(name):
    return [f for f in sorted(os.listdir(RAW)) if f.startswith(name + ".") and f.rsplit(".", 1)[-1] in ("md", "txt")]


def rows(path):
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
    if not re.fullmatch(r"[A-Z]{1,2}", a.prefix):
        sys.exit("--prefix must be one or two capital letters")
    if a.status not in STATUSES:
        sys.exit(f"status must be one of {sorted(STATUSES)}")
    log = fetchlog()
    if a.name not in log:
        sys.exit(f"'{a.name}' is not in sources/_fetchlog.csv; save it with fetch.py first")
    files = text_files(a.name)
    if not files:
        sys.exit(f"no sources/{a.name}.md or .txt text copy found")
    if not a.no_quote_check:
        q = norm(a.quote)
        if len(q) < 12:
            sys.exit("quote too short; copy a full phrase or sentence")
        if not any(q in norm(open(os.path.join(RAW, f), encoding="utf-8", errors="replace").read()) for f in files):
            sys.exit(f"QUOTE NOT FOUND in {files}. Copy it exactly from the saved file (whitespace and markdown are ignored).")
    elif not a.note:
        sys.exit("--no-quote-check needs --note explaining why (e.g. 'garbled Bangla text layer, p.3')")
    pd = a.page_date
    if pd != "undated" and not re.fullmatch(r"\d{4}(-\d{2}(-\d{2})?)?", pd):
        sys.exit("--page-date must be YYYY, YYYY-MM, YYYY-MM-DD or 'undated'")
    full = pd + "-01-01"[len(pd) - 4:] if pd != "undated" else ""
    if a.status == "verified" and (pd == "undated" or full < CUTOFF):
        sys.exit(f"page date {pd} is undated or before {CUTOFF}: status must be possibly-outdated")
    src = [r for r in rows(SOURCES) if r["name"] == a.name]
    if not src:
        sys.exit(f"register the source first: python3 ../../tools/facts.py source --name {a.name} ...")
    o = src[0]["official"].lower()
    stype = ("official" if o.startswith("y") else "official-archived" if o == "archived"
             else "news-archived" if o == "news-archived" else "news")
    if stype.startswith("news") and a.status in ("verified", "possibly-outdated"):
        sys.exit("a news source can only be lead, unofficial or conflict")
    if stype.startswith("official") and a.status in ("lead", "unofficial"):
        sys.exit("an official source should be verified, possibly-outdated or conflict")
    if any([a.visa, a.field, a.value]) and not all([a.visa, a.field, a.value]):
        sys.exit("give all of --visa --field --value, or none")
    n = max([int(r["id"][len(a.prefix):]) for r in rows(FACTS) if re.fullmatch(a.prefix + r"\d{4}", r["id"])] or [0]) + 1
    fid = f"{a.prefix}{n:04d}"
    write_row(FACTS, FCOLS, {"id": fid, "claim": a.claim, "quote": a.quote, "saved_file": ";".join(files),
                             "url": log[a.name]["url"], "page_date": pd, "access_date": log[a.name]["access_date"],
                             "source_type": stype, "status": a.status, "visa": a.visa or "", "field": a.field or "",
                             "value": a.value or "", "note": a.note or ""})
    print(fid)


def source(a):
    log = fetchlog()
    if a.name not in log:
        sys.exit(f"'{a.name}' is not in sources/_fetchlog.csv; save it with fetch.py first")
    if any(r["name"] == a.name for r in rows(SOURCES)):
        print("already registered")
        return
    write_row(SOURCES, SCOLS, {"name": a.name, "url": log[a.name]["url"], "publisher": a.publisher, "title": a.title,
                               "official": a.official, "page_date": a.page_date or "", "access_date": log[a.name]["access_date"]})
    print("registered", a.name)


def cited(a):
    F = {r["id"]: r for r in rows(FACTS)}
    lines = open(a.file, encoding="utf-8").read().splitlines()
    start, end = a.start or 1, a.end or len(lines)
    seen = []
    for ln in lines[start - 1:end]:
        for grp in re.findall(r"\[([A-Z]{1,2}\d{4}(?:, ?[A-Z]{1,2}\d{4})*)\]", ln):
            for i in (x.strip() for x in grp.split(",")):
                if i not in seen:
                    seen.append(i)
    for i in seen:
        r = F.get(i)
        print(f"{i} [{r['status']}|{r['page_date']}] {r['claim'][:230]}  <{r['saved_file']}>" if r else f"{i} MISSING")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd")
    x = sub.add_parser("add")
    for k in ("prefix", "name", "claim", "page-date", "status"):
        x.add_argument("--" + k, required=True)
    x.add_argument("--quote", default="")
    for k in ("visa", "field", "value", "note"):
        x.add_argument("--" + k)
    x.add_argument("--no-quote-check", action="store_true")
    s = sub.add_parser("source")
    for k in ("name", "publisher", "title", "official"):
        s.add_argument("--" + k, required=True)
    s.add_argument("--page-date")
    c = sub.add_parser("cited")
    c.add_argument("file")
    c.add_argument("start", nargs="?", type=int)
    c.add_argument("end", nargs="?", type=int)
    a = p.parse_args()
    {"add": add, "source": source, "cited": cited}.get(a.cmd, lambda _: print(__doc__))(a)
