"""Coverage ledger: one row per Prothom Alo story that any pass looked at, saying what happened to it.
Writes ledger.csv (id, url, published, headline, relevant, status, docs, fact_ids, passes, reason) and prints totals."""
import csv, glob, json, os, re, collections
K = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))          # extract/kb4
X = os.path.dirname(K)                                                   # extract
A = os.path.dirname(X)                                                   # prothom-alo-archive
flag = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(A, "migration-stories.jsonl"))}
recs = {json.loads(l)["id"]: json.loads(l) for f in glob.glob(os.path.join(X, "gout", "g-*.jsonl")) for l in open(f)}
scam = {json.loads(l)["id"]: json.loads(l) for l in open(os.path.join(X, "scam-cases.jsonl"))}
tri = {t["id"]: t for t in json.load(open(os.path.join(K, "rejected-triage.json")))}
remaining = set(json.load(open(os.path.join(X, "remaining-ids.json"))))
row = collections.defaultdict(lambda: {"docs": set(), "facts": set(), "passes": set(), "reasons": [], "used": False})
def doc_of(path):
    p = path.replace("\\", "/")
    m = re.search(r"(countries|global)/([a-z-]+)/facts\.csv$", p)
    return f"{m.group(1)}/{m.group(2)}" if m else ("agencies" if p.endswith("agencies/facts.csv") else "")
# kb4 ledgers: articles with used/unused
for f in glob.glob(os.path.join(K, "*ledger-*.json")):
    name = os.path.basename(f)
    for a in json.load(open(f)).get("articles", []):
        r = row[a["article_id"]]; r["passes"].add(name)
        if a.get("used"): r["used"] = True; r["facts"].update(a.get("fact_ids") or [])
        elif a.get("reason_if_unused"): r["reasons"].append(a["reason_if_unused"])
        if a.get("held") or a.get("held_for_global"): r["reasons"].append("facts held for another doc (see heldout files)")
# held outcomes
held = {}
for f in glob.glob(os.path.join(K, "held*.json")):
    if os.path.basename(f) == "held-all.json" or os.path.basename(f).startswith("heldout"): continue
    for x in json.load(open(f)): held[x["held_id"]] = x
for f in glob.glob(os.path.join(K, "heldout*.json")):
    for e in json.load(open(f)):
        if not isinstance(e, dict) or e.get("held_id") not in held: continue
        r = row[held[e["held_id"]]["article_id"]]; r["passes"].add(os.path.basename(f))
        if e.get("outcome") == "added": r["used"] = True; r["facts"].update(e.get("fact_ids") or [])
# which doc each fact is in, and earlier passes: scan every facts.csv for pa- sources
csv.field_size_limit(10**9)
url2id = {d["url"].rstrip("/"): i for i, d in flag.items()}
for fc in glob.glob("/Users/rarba/Programming/brac/bits-migration/kb-countries/countries/*/facts.csv") + \
          glob.glob("/Users/rarba/Programming/brac/bits-migration/kb-modules/global/*/facts.csv") + \
          glob.glob("/Users/rarba/Programming/brac/bits-migration/kb-modules/agencies/facts.csv"):
    if True:
        d = doc_of(fc)
        for fr in csv.DictReader(open(fc, encoding="utf-8")):
            u = (fr.get("url") or "").rstrip("/")
            if "prothomalo.com" in u:
                i = url2id.get(u) or next((k for k, v in flag.items() if False), None)
                if i is None:
                    slug = u.split("/")[-1]
                    i = next((k for k, v in flag.items() if v["url"].rstrip("/").endswith(slug)), None) or \
                        next((k for k, v in tri.items() if False), None)
                if i is None: continue
                r = row[i]; r["used"] = True; r["docs"].add(d); r["facts"].add(fr["id"])
ids = set(flag) | {i for i, t in tri.items() if t["verdict"] == "useful"} | set(row)
out = []
for i in sorted(ids):
    d = flag.get(i); r = row[i]
    relevant = (recs.get(i, {}).get("relevant") if i in recs else (scam.get(i, {}).get("relevant") if i in scam else (tri.get(i, {}).get("verdict") == "useful" if i in tri else None)))
    if r["used"]: status = "used"
    elif relevant is False: status = "not relevant"
    elif r["reasons"]: status = "read, nothing new"
    elif i not in remaining and relevant: status = "used in an earlier pass (11-22/23)"
    else: status = "NOT ACCOUNTED"
    out.append({"id": i, "url": d["url"] if d else "", "published": (d or {}).get("published", "")[:10], "headline": (d or {}).get("headline", ""),
                "relevant": relevant, "status": status, "docs": ";".join(sorted(x for x in r["docs"] if x)), "fact_ids": len(r["facts"]),
                "passes": ";".join(sorted(r["passes"])), "reason": " | ".join(dict.fromkeys(r["reasons"]))[:300]})
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ledger.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, list(out[0])); w.writeheader(); w.writerows(out)
c = collections.Counter(o["status"] for o in out); print(len(out), dict(c))
