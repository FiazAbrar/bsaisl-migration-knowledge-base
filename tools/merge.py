"""Join the per-topic research parts into the files the project asks for.

  ledger-parts/*.csv        -> ledger.csv   (id | claim | quote | url | access_date | raw_file | page_date | source_type | status | note)
  ledger-parts/*.facts.csv  -> facts.csv    (visa_type | field | value | ledger_id | source_type | last_verified | status | page_date | url)
  findings-parts/*.md       -> findings.md
  blocked-parts/*.md        -> blocked.md

Run from inside the country folder:  python3 ../../tools/merge.py
"""
import csv, glob, os



def key(p):
    return os.path.basename(p)


def read(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    led, facts = [], []
    for p in sorted(glob.glob("ledger-parts/*.csv"), key=key):
        if p.endswith(".facts.csv"):
            continue
        led += read(p)
    ids = [r["id"] for r in led]
    dup = {i for i in ids if ids.count(i) > 1}
    assert not dup, f"duplicate ledger ids {dup}"
    byid = {r["id"]: r for r in led}
    for p in sorted(glob.glob("ledger-parts/*.facts.csv"), key=key):
        for r in read(p):
            l = byid[r["ledger_id"]]
            facts.append({**r, "source_type": l["source_type"], "last_verified": l["access_date"],
                          "status": l["status"], "page_date": l["page_date"], "url": l["url"]})
    cols = ["id", "claim", "quote", "url", "access_date", "raw_file", "page_date", "source_type", "status", "note"]
    with open("ledger.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(led)
    fcols = ["visa_type", "field", "value", "ledger_id", "source_type", "last_verified", "status", "page_date", "url"]
    with open("facts.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fcols); w.writeheader(); w.writerows(facts)
    country = os.path.basename(os.getcwd()).replace("-", " ").title()
    for src, out, head in (("findings-parts", "findings.md", f"# {country}: research findings"),
                           ("blocked-parts", "blocked.md", f"# {country}: pages we could not fetch")):
        parts = sorted(glob.glob(f"{src}/*.md"), key=key)
        with open(out, "w", encoding="utf-8") as f:
            f.write(head + "\n\nMerged from the per-topic notes in `" + src + "/`. Ledger ids like [W0012] point to rows in ledger.csv.\n")
            for p in parts:
                f.write("\n\n" + open(p, encoding="utf-8").read().strip() + "\n")
    st = {}
    for r in led:
        st[r["status"]] = st.get(r["status"], 0) + 1
    print(f"ledger.csv {len(led)} rows {st}; facts.csv {len(facts)} rows")


if __name__ == "__main__":
    main()
