"""Apply writers' REPLACE / NEW blocks to the guide files.

Usage: python3 splice.py out-a.md out-b.md ...   (paths relative to this folder)
Reads the ORIGINAL doc from git (HEAD) only to resolve which occurrence a duplicated heading means.
"""
import os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
KB = "/Users/rarba/Programming/brac/bits-migration/kb-scam-cases"
BLK = re.compile(r'<<<(REPLACE|NEW) doc="([^"]+)" (heading|after)="(.+?)">>>\n(.*?)\n<<<END>>>', re.S)

def level(line):
    m = re.match(r"^(#{1,6}) ", line); return len(m.group(1)) if m else 0

def find(lines, heading, occ=0):
    idx = [i for i, l in enumerate(lines) if l.rstrip() == heading.strip()]
    if not idx: raise SystemExit(f"heading not found: {heading}")
    if len(idx) > 1 and occ is None: raise SystemExit(f"ambiguous heading: {heading} ({len(idx)} times)")
    return idx[occ or 0]

def end_of(lines, i):
    lv = level(lines[i])
    for j in range(i + 1, len(lines)):
        if 0 < level(lines[j]) <= lv: return j
    return len(lines)

def occurrence(docpath, heading, lineno):
    rel = os.path.relpath(docpath, KB)
    orig = subprocess.run(["git", "-C", KB, "show", f"HEAD:{rel}"], capture_output=True, text=True).stdout.split("\n")
    idx = [i + 1 for i, l in enumerate(orig) if l.rstrip() == heading.strip()]
    return idx.index(lineno) if lineno in idx else None

for f in sys.argv[1:]:
    text = open(os.path.join(HERE, f), encoding="utf-8").read()
    for kind, doc, _, head, body in BLK.findall(text):
        path = doc if doc.startswith("/") else os.path.join(KB, re.sub(r"^kb-scam-cases/", "", doc))
        lines = open(path, encoding="utf-8").read().split("\n")
        m = re.match(r"<!-- line (\d+) -->\n", body)
        occ = 0
        if m:
            body = body[m.end():]
            occ = occurrence(path, head, int(m.group(1)))
        elif sum(1 for l in lines if l.rstrip() == head.strip()) > 1:
            occ = None
        i = find(lines, head, occ)
        j = end_of(lines, i)
        new = body.rstrip("\n").split("\n") + [""]
        if kind == "REPLACE":
            if new[0].rstrip() != head.strip(): raise SystemExit(f"{f}: block for {head} starts with {new[0]}")
            lines[i:j] = new
        else:
            lines[j:j] = new
        open(path, "w", encoding="utf-8").write("\n".join(lines))
        print(f"{f}: {kind} {head[:70]}")
