"""Print ledger claims for ids cited in a text range: python tools/claims.py malaysia.src.md [start_line] [end_line]"""
import csv, re, sys
L = {r["id"]: r for r in csv.DictReader(open("ledger.csv", encoding="utf-8", newline=""))}
lines = open(sys.argv[1], encoding="utf-8").read().splitlines()
a = int(sys.argv[2]) if len(sys.argv) > 2 else 1
b = int(sys.argv[3]) if len(sys.argv) > 3 else len(lines)
seen = []
for ln in lines[a - 1:b]:
    for grp in re.findall(r"\[([A-Z]\d{4}(?:, ?[A-Z]\d{4})*)\]", ln):
        for i in grp.split(","):
            i = i.strip()
            if i not in seen: seen.append(i)
for i in seen:
    r = L.get(i)
    print(f"{i} [{r['status'][:4]}|{r['page_date']}] {r['claim'][:230]}" if r else f"{i} MISSING")
