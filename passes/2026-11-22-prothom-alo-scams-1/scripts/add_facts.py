"""Save the Prothom Alo articles behind checked claims as sources in the knowledge base and log each claim as a fact.

Run from inside the knowledge-base folder that owns the doc (e.g. cross-country/):
  python3 /path/to/add_facts.py A B C D
Reads checked-<set>.json next to this file; writes keymap.json (claim key -> fact ids) next to this file.
Only claims with verdict supported or partly are added, using the checker's corrected_claim.
"""
import csv, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ARCH = os.path.dirname(os.path.dirname(HERE))
TOOLS = os.path.join(os.path.dirname(os.getcwd()), "tools")
RAW = os.path.join(os.getcwd(), "sources")
PREFIX = "PA"

src = {}
for l in open(os.path.join(ARCH, "migration-stories.jsonl")):
    d = json.loads(l); src[d["id"]] = d
head_en = {}
for l in open(os.path.join(ARCH, "extract", "scam-cases.jsonl")):
    r = json.loads(l); head_en[r["id"]] = r.get("headline_en") or ""

def fetchlog():
    with open(os.path.join(RAW, "_fetchlog.csv"), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def run(args):
    p = subprocess.run([sys.executable] + args, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip()

def ensure_source(aid):
    d = src[aid]
    url = d["url"]
    for r in fetchlog():
        if r["url"].rstrip("/") == url.rstrip("/") and r["http_status"].startswith("2"):
            return r["name"], False
    slug = url.rstrip("/").split("/")[-1]
    name = f"pa-{d['published'][:10]}-{slug}".lower()
    path = os.path.join(RAW, name + ".md")
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {d['headline'].strip()}\n\n")
            f.write(f"Source: Prothom Alo, {url}\n\nPublished: {d['published']}\n\n")
            f.write("Saved 2026-11-22 from Prothom Alo's public story API (article text only, no page furniture).\n\n---\n\n")
            f.write(d["text"].strip() + "\n")
    rc, out = run([os.path.join(TOOLS, "fetch.py"), "--log", url, name, "manual"])
    if rc: sys.exit(f"fetch --log failed for {name}: {out}")
    title = d["headline"].strip() + (f" ({head_en[aid]})" if head_en.get(aid) else "")
    rc, out = run([os.path.join(TOOLS, "facts.py"), "source", "--name", name, "--publisher", "Prothom Alo",
                   "--title", title, "--official", "no", "--page-date", d["published"][:10]])
    if rc: sys.exit(f"facts source failed for {name}: {out}")
    return name, True

keymap_path = os.path.join(HERE, "keymap.json")
keymap = json.load(open(keymap_path)) if os.path.exists(keymap_path) else {}
added = skipped = failed = newsrc = 0
for s in sys.argv[1:]:
    for c in json.load(open(os.path.join(HERE, f"checked-{s}.json"))):
        key = c["key"]
        if key in keymap: continue
        if c["verdict"] not in ("supported", "partly") or not c.get("quotes") or not c.get("corrected_claim"):
            skipped += 1; continue
        name, new = ensure_source(c["article_id"]); newsrc += new
        ids = []
        for i, q in enumerate(c["quotes"]):
            claim = c["corrected_claim"] if i == 0 else c["corrected_claim"] + f" (supporting passage {i+1})"
            rc, out = run([os.path.join(TOOLS, "facts.py"), "add", "--prefix", PREFIX, "--name", name, "--claim", claim,
                           "--quote", q, "--page-date", src[c["article_id"]]["published"][:10], "--status", "unofficial",
                           "--note", f"Prothom Alo archive pass; claim {key} checked against the full article by an independent verifier"])
            m = re.search(rf"\b{PREFIX}\d{{4}}\b", out)
            if rc or not m:
                print("FAILED", key, i, out[:200]); failed += 1; continue
            ids.append(m.group(0))
        if ids:
            keymap[key] = {"ids": ids, "claim": c["corrected_claim"], "verdict": c["verdict"], "source": name}
            added += 1
        json.dump(keymap, open(keymap_path, "w"), ensure_ascii=False, indent=1)
print(f"claims added {added}, skipped {skipped}, quote failures {failed}, new sources {newsrc}")
