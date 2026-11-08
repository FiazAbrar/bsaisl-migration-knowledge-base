"""Merge countries/maldives/work/<X>/ staging folders into countries/maldives/.
Usage: python merge.py <country_dir> [letters...]
- copies sources, renames clashing names (different content) to <name>-<x>
- appends sources.csv, _fetchlog.csv, _wayback.csv, facts.csv (dedupe by name / id)
- re-checks every merged fact's quote against its final saved file
Idempotent: skips letters already listed in <country>/work/_merged.txt
"""
import csv, os, shutil, sys, re, html, unicodedata

C = sys.argv[1]
letters = sys.argv[2:] or sorted(d for d in os.listdir(os.path.join(C, "work")) if os.path.isdir(os.path.join(C, "work", d)))
SRC = os.path.join(C, "sources")
os.makedirs(SRC, exist_ok=True)
FC = ["id", "claim", "quote", "saved_file", "url", "page_date", "access_date", "source_type", "status", "visa", "field", "value", "note"]
SC = ["name", "url", "publisher", "title", "official", "page_date", "access_date"]
LC = ["name", "url", "access_date", "http_status", "content_type", "method", "files"]


def norm(s):
    s = unicodedata.normalize("NFKC", html.unescape(s))
    s = re.sub(r"\]\([^)]*\)", "]", s)
    s = re.sub(r"[\*_#>|\\\[\]`\"“”‘’' ​‌‍]", " ", s)
    s = s.replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", s).strip().lower()


def rows(p):
    if not os.path.exists(p):
        return []
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write(p, cols, rs):
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rs:
            w.writerow({k: r.get(k, "") for k in cols})


def text_of(d, name):
    out = ""
    for f in sorted(os.listdir(d)):
        if f.startswith(name + ".") and f.rsplit(".", 1)[-1] in ("md", "txt"):
            out += open(os.path.join(d, f), encoding="utf-8", errors="replace").read()
    return out


done_p = os.path.join(C, "work", "_merged.txt")
done = set(open(done_p).read().split()) if os.path.exists(done_p) else set()
facts = rows(os.path.join(C, "facts.csv"))
sources = rows(os.path.join(C, "sources.csv"))
log = rows(os.path.join(SRC, "_fetchlog.csv"))
wb = rows(os.path.join(SRC, "_wayback.csv"))
wbcols = list(wb[0].keys()) if wb else None
fid = {r["id"] for r in facts}
sname = {r["name"]: r for r in sources}
lname = {r["name"]: r for r in log}
problems = []

for X in letters:
    if X in done:
        print("skip (already merged)", X)
        continue
    W = os.path.join(C, "work", X)
    WS = os.path.join(W, "sources")
    wlog = {r["name"]: r for r in rows(os.path.join(WS, "_fetchlog.csv"))}
    wsrc = rows(os.path.join(W, "sources.csv"))
    wfacts = rows(os.path.join(W, "facts.csv"))
    used = {r["name"] for r in wsrc}
    rename = {}
    for name in sorted(used):
        new = name
        if name in lname:
            same = norm(text_of(SRC, name)) == norm(text_of(WS, name))
            if not same:
                new = f"{name}-{X.lower()}"
                k = 2
                while new in lname:
                    new = f"{name}-{X.lower()}{k}"; k += 1
                rename[name] = new
        files = [f for f in os.listdir(WS) if f.startswith(name + ".") and not f.endswith((".part", ".hdr"))]
        if not files:
            problems.append(f"{X}: source {name} has no files")
        for f in files:
            dst = os.path.join(SRC, new + f[len(name):])
            if new != name or not os.path.exists(dst):
                shutil.copy2(os.path.join(WS, f), dst)
        if new not in lname:
            lr = dict(wlog.get(name) or {"name": name, "url": "", "method": "manual"})
            lr["name"] = new
            lr["files"] = ";".join(new + f[len(name):] for f in sorted(files))
            log.append(lr); lname[new] = lr
    for r in wsrc:
        r = dict(r); r["name"] = rename.get(r["name"], r["name"])
        if r["name"] not in sname:
            sources.append(r); sname[r["name"]] = r
    for r in rows(os.path.join(WS, "_wayback.csv")):
        r = dict(r); r["name"] = rename.get(r.get("name", ""), r.get("name", ""))
        wbcols = wbcols or list(r.keys())
        if not any(x.get("name") == r["name"] for x in wb):
            wb.append(r)
    for r in wfacts:
        if r["id"] in fid:
            problems.append(f"{X}: duplicate fact id {r['id']} skipped")
            continue
        r = dict(r)
        parts = r["saved_file"].split(";")
        nm = None
        for old, new in rename.items():
            if any(p.startswith(old + ".") for p in parts):
                parts = [new + p[len(old):] if p.startswith(old + ".") else p for p in parts]
        r["saved_file"] = ";".join(parts)
        facts.append(r); fid.add(r["id"])
    done.add(X)
    print(f"merged {X}: {len(wsrc)} sources, {len(wfacts)} facts, renamed {rename}")

# quote re-check
cache = {}
bad = 0
for r in facts:
    if any(k in r.get("note", "").lower() for k in ("garbled", "transcribed", "no-quote-check", "page image")) or not r["quote"].strip():
        continue
    files = [p for p in r["saved_file"].split(";") if p]
    txt = ""
    for p in files:
        if p not in cache:
            fp = os.path.join(SRC, p)
            cache[p] = norm(open(fp, encoding="utf-8", errors="replace").read()) if os.path.exists(fp) else ""
        txt += cache[p]
    if norm(r["quote"]) not in txt:
        bad += 1
        problems.append(f"quote not found: {r['id']} in {r['saved_file']}")
    stem = files[0].rsplit(".", 1)[0] if files else ""
    if stem and stem not in sname:
        problems.append(f"fact {r['id']}: source {stem} not in sources.csv")

write(os.path.join(C, "facts.csv"), FC, facts)
write(os.path.join(C, "sources.csv"), SC, sources)
write(os.path.join(SRC, "_fetchlog.csv"), LC, log)
if wb:
    write(os.path.join(SRC, "_wayback.csv"), wbcols, wb)
open(done_p, "w").write("\n".join(sorted(done)))
print(f"TOTAL facts {len(facts)}, sources {len(sources)}; problems {len(problems)}")
for p in problems[:200]:
    print(" -", p)
