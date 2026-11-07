"""Recount the agency activity figures in agencies/doc.md from agencies/activity.csv.

  cd agencies && python3 ../tools/agency_counts.py [country] [--top N]

activity.csv has one row per entry in BMET's list of permission letters (bmet.gov.bd/pages/miscellaneous-infos),
with a link to each letter's PDF. A letter counts if it is a permission (entry_type "permission") and not a
repost of an earlier entry (dup_of_entry empty). Workers are the posts the letter approves, using new_workers,
which leaves out permission IDs already counted in an earlier entry. Workers approved is not workers sent.
"""
import csv, sys
from collections import defaultdict

args = [a for a in sys.argv[1:] if not a.startswith("--")]
top = int(sys.argv[sys.argv.index("--top") + 1]) if "--top" in sys.argv else 10
want = args[0].lower() if args else None
if want and want.isdigit():
    want = None

rows = [r for r in csv.DictReader(open("activity.csv", encoding="utf-8", newline=""))
        if r["entry_type"] == "permission" and not r["dup_of_entry"]]
by = defaultdict(lambda: defaultdict(lambda: [0, 0, ""]))
for r in rows:
    c = r["country"] or "(country unreadable)"
    a = by[c][r["rl"]]
    a[0] += 1
    a[1] += int(r["new_workers"] or 0)
    a[2] = r["agency"]
dates = sorted(r["date"] for r in rows if r["date"])
print(f"{len(rows)} letters, {dates[0]} to {dates[-1]}\n")
for c in sorted(by, key=lambda c: -sum(v[1] for v in by[c].values())):
    if want and c.lower() != want:
        continue
    ags = by[c]
    print(f"{c}: {sum(v[0] for v in ags.values())} letters, {sum(v[1] for v in ags.values()):,} workers, {len(ags)} agencies")
    for rl, (n, w, name) in sorted(ags.items(), key=lambda kv: -kv[1][1])[:top]:
        print(f"  {rl} {name}: {n} letters, {w:,} workers")
    print()
