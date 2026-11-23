"""Log checked second-pass claims as facts in the knowledge base.

Usage: python3 add_facts2.py <set> [<set> ...]    e.g. libya-1 abroad-2
Run from anywhere. For each set it reads drafts-<set>.json (for target_section) and every
checked-<set>-*.json. Claims whose target starts with "MALAYSIA DOC:" go to countries/malaysia,
all others to cross-country. Sources are saved under each folder's sources/ as pa-<date>-<slug>.md.
Writes keymap2.json next to this file: key -> {ids, claim, folder, target_section, placement}.
"""
import csv, glob, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ARCH = os.path.dirname(os.path.dirname(HERE))
KB = "/Users/rarba/Programming/brac/bits-migration/kb-scam-cases"
TOOLS = os.path.join(KB, "tools")
PREFIXES = {"malaysia": "MP", "saudi-arabia": "SP", "cross-country": "CQ"}

src = {}
for l in open(os.path.join(ARCH, "migration-stories.jsonl")):
    d = json.loads(l); src[d["id"]] = d
head_en = {}
for f in glob.glob(os.path.join(ARCH, "extract", "gout", "*.jsonl")):
    for l in open(f):
        r = json.loads(l); head_en[r["id"]] = r.get("headline_en") or ""
for l in open(os.path.join(ARCH, "extract", "scam-cases.jsonl")):
    r = json.loads(l); head_en.setdefault(r["id"], r.get("headline_en") or "")

def run(folder, args):
    p = subprocess.run([sys.executable] + args, capture_output=True, text=True, cwd=folder)
    return p.returncode, (p.stdout + p.stderr).strip()

def fetchlog(folder):
    with open(os.path.join(folder, "sources", "_fetchlog.csv"), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def ensure_source(folder, aid):
    d = src[aid]; url = d["url"]
    for r in fetchlog(folder):
        if r["url"].rstrip("/") == url.rstrip("/") and r["http_status"].startswith("2") and r["name"].startswith("pa-"):
            return r["name"]
    name = f"pa-{d['published'][:10]}-{url.rstrip('/').split('/')[-1]}".lower()
    if any(r["name"] == name for r in fetchlog(folder)):
        return name
    path = os.path.join(folder, "sources", name + ".md")
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {d['headline'].strip()}\n\nSource: Prothom Alo, {url}\n\nPublished: {d['published']}\n\n")
            f.write("Saved 2026-11-23 from Prothom Alo's public story API (article text only, no page furniture).\n\n---\n\n")
            f.write(d["text"].strip() + "\n")
    rc, out = run(folder, [os.path.join(TOOLS, "fetch.py"), "--log", url, name, "manual"])
    if rc: sys.exit(f"fetch --log failed for {name}: {out}")
    title = d["headline"].strip() + (f" ({head_en[aid]})" if head_en.get(aid) else "")
    rc, out = run(folder, [os.path.join(TOOLS, "facts.py"), "source", "--name", name, "--publisher", "Prothom Alo",
                           "--title", title, "--official", "no", "--page-date", d["published"][:10]])
    if rc: sys.exit(f"facts source failed for {name}: {out}")
    return name

kp = os.path.join(HERE, "keymap3.json")
keymap = json.load(open(kp)) if os.path.exists(kp) else {}
for s in sys.argv[1:]:
    country = "malaysia" if s.startswith("my") else "saudi-arabia"
    drafts = {x["key"]: x for x in json.load(open(os.path.join(HERE, f"drafts-{s}.json")))["drafts"]}
    checked = []
    for cf in sorted(glob.glob(os.path.join(HERE, f"checked-{s}.json"))):
        checked += json.load(open(cf))
    if not checked:   # set not pre-checked: use the draft as is; the final check covers it
        checked = [{"key": k, "article_id": d["article_id"], "verdict": "unchecked", "corrected_claim": d["claim"], "quotes": d["quotes"]} for k, d in drafts.items()]
    added = skipped = failed = 0
    if True:
        for c in checked:
            key = c["key"]
            if key in keymap: continue
            if c["verdict"] not in ("supported", "partly", "unchecked") or not c.get("quotes") or not c.get("corrected_claim"):
                skipped += 1; continue
            dr = drafts.get(key, {})
            tgt = dr.get("target_section", "")
            folder = os.path.join(KB, "cross-country") if tgt.startswith("CROSS-COUNTRY") else os.path.join(KB, "countries", country)
            name = ensure_source(folder, c["article_id"])
            ids = []
            for i, q in enumerate(c["quotes"]):
                claim = c["corrected_claim"] if i == 0 else c["corrected_claim"] + f" (supporting passage {i+1})"
                rc, out = run(folder, [os.path.join(TOOLS, "facts.py"), "add", "--prefix", PREFIXES[os.path.basename(folder)], "--name", name,
                                       "--claim", claim, "--quote", q, "--page-date", src[c["article_id"]]["published"][:10],
                                       "--status", "unofficial", "--note",
                                       f"Prothom Alo archive pass 2; claim {key} ({c['verdict']}) from the country pass"])
                m = re.search(rf"\b{PREFIXES[os.path.basename(folder)]}\d{{4}}\b", out)
                if rc or not m:
                    print("FAILED", key, i, out[:200]); failed += 1; continue
                ids.append(m.group(0))
            if ids:
                keymap[key] = {"ids": ids, "claim": c["corrected_claim"], "verdict": c["verdict"],
                               "folder": os.path.basename(folder), "target_section": tgt,
                               "placement": dr.get("placement", ""), "why_new": dr.get("why_new", ""),
                               "article_id": c["article_id"], "published": src[c["article_id"]]["published"][:10]}
                added += 1
            json.dump(keymap, open(kp, "w"), ensure_ascii=False, indent=1)
    print(f"{s}: added {added}, skipped {skipped}, quote failures {failed}")
