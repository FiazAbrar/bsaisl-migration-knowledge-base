"""Merge the per-agent work folders (work/<X>/) into countries/kyrgyzstan/{sources/, sources.csv, facts.csv}.

Run from countries/kyrgyzstan:  python work/merge.py [letters...]   (default: every work/<X>/ folder)
Rebuilds the merged files from scratch each run (only this script writes them during research).
A source name used by two agents with different content is renamed <name>-<x> for the later agent,
and that agent's facts are repointed. Every quote is re-checked against the merged text copies.
"""
import csv, hashlib, os, re, shutil, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "tools")))
from facts import norm, FCOLS, SCOLS  # noqa: E402

BASE = os.getcwd()
WORK = os.path.join(BASE, "work")
RAW = os.path.join(BASE, "sources")
LCOLS = ["name", "url", "access_date", "http_status", "content_type", "method", "files"]


def rows(p):
    if not os.path.exists(p):
        return []
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def h(p):
    return hashlib.md5(open(p, "rb").read()).hexdigest()


def files_of(d, name):
    return sorted(f for f in os.listdir(d) if f.startswith(name + ".") and not f.startswith("_"))


letters = sys.argv[1:] or sorted(x for x in os.listdir(WORK) if os.path.isdir(os.path.join(WORK, x)))
if os.path.isdir(RAW):
    shutil.rmtree(RAW)
os.makedirs(RAW)
log_out, src_out, fact_out = [], {}, {}
owner, problems = {}, []
for X in letters:
    d = os.path.join(WORK, X, "sources")
    if not os.path.isdir(d):
        continue
    ren = {}
    log = rows(os.path.join(d, "_fetchlog.csv"))
    for r in log:
        name = r["name"]
        fs = files_of(d, name)
        if not fs:
            if not name.endswith("FAILED"):
                problems.append(f"{X}: {name} in fetch log but no files")
            continue
        new = name
        if name in owner:
            prev = owner[name]
            same = [f for f in fs if os.path.exists(os.path.join(RAW, f)) and h(os.path.join(RAW, f)) == h(os.path.join(d, f))]
            if same and len(same) == len(fs):
                continue  # identical copy already merged
            new = f"{name}-{X.lower()}"
            ren[name] = new
            problems.append(f"renamed {X}:{name} -> {new} (clash with {prev})")
        owner[new] = X
        for f in fs:
            shutil.copy2(os.path.join(d, f), os.path.join(RAW, new + f[len(name):]))
        r = dict(r, name=new, files=";".join(new + f[len(name):] for f in fs))
        log_out.append({k: r.get(k, "") for k in LCOLS})
    for r in rows(os.path.join(WORK, X, "sources.csv")):
        n = ren.get(r["name"], r["name"])
        if n not in src_out:
            src_out[n] = dict(r, name=n)
    for r in rows(os.path.join(WORK, X, "facts.csv")):
        if r["id"] in fact_out:
            problems.append(f"duplicate fact id {r['id']} ({X})")
            continue
        sf = []
        for f in r["saved_file"].split(";"):
            for old, new in ren.items():
                if f.startswith(old + "."):
                    f = new + f[len(old):]
            sf.append(f)
        fact_out[r["id"]] = dict(r, saved_file=";".join(sf))

with open(os.path.join(RAW, "_fetchlog.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=LCOLS); w.writeheader(); w.writerows(log_out)
with open(os.path.join(BASE, "sources.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=SCOLS); w.writeheader(); w.writerows({k: r.get(k, "") for k in SCOLS} for r in src_out.values())
facts = sorted(fact_out.values(), key=lambda r: (re.match(r"[A-Z]+", r["id"]).group(), r["id"]))
with open(os.path.join(BASE, "facts.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=FCOLS); w.writeheader(); w.writerows({k: r.get(k, "") for k in FCOLS} for r in facts)

# re-check quotes
cache, bad, unchecked = {}, 0, 0
for r in facts:
    texts = []
    for f in r["saved_file"].split(";"):
        p = os.path.join(RAW, f)
        if not os.path.exists(p):
            problems.append(f"{r['id']}: saved file missing {f}")
            continue
        if p not in cache:
            cache[p] = norm(open(p, encoding="utf-8", errors="replace").read())
        texts.append(cache[p])
    q = norm(r["quote"])
    if texts and q and not any(q in t for t in texts):
        if r["note"].strip():
            unchecked += 1
        else:
            bad += 1
            problems.append(f"{r['id']}: quote not found ({r['saved_file']})")
    f0 = r["saved_file"].split(";")[0]
    src = max((n for n in src_out if f0.startswith(n + ".")), key=len, default=f0)
    if src not in src_out:
        problems.append(f"{r['id']}: source {src} not registered")

off = sum(1 for r in facts if r["source_type"].startswith("official"))
print(f"letters {letters}: {len(log_out)} saved sources, {len(src_out)} registered, {len(facts)} facts ({off} official), {bad} bad quotes, {unchecked} unchecked (no-quote-check with note)")
for p in problems:
    print(" -", p)
