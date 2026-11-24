"""Apply verifier fixes: python work/apply.py verify/r1-*.md  (run from countries/cambodia)"""
import re, sys, glob
doc = open("doc.md", encoding="utf-8").read()
ok = miss = 0
for p in sorted(set(sum([glob.glob(a) for a in sys.argv[1:]], []))):
    t = open(p, encoding="utf-8").read()
    for blk in re.split(r"^### FAIL", t, flags=re.M)[1:]:
        mo = re.search(r"^old:\s?(.*?)\s*$", blk, re.M); mn = re.search(r"^new:\s?(.*?)\s*$", blk, re.M)
        if not mo or not mn:
            continue
        old, new = mo.group(1).strip(), mn.group(1).strip()
        if new.lower() in ("(delete)", "delete"):
            new = ""
        if old and doc.count(old) >= 1:
            doc = doc.replace(old, new, 1); ok += 1
        else:
            miss += 1; print("NOT FOUND", p, old[:90])
doc = re.sub(r"[ \t]+\n", "\n", doc); doc = re.sub(r"(?<=\S)  +", " ", doc)
open("doc.md", "w", encoding="utf-8").write(doc)
print(f"applied {ok}, not found {miss}")
# coverage auditor: " NEEDTOKNOW: question" at the end of a line -> Need to know block after that line
lines = open("doc.md", encoding="utf-8").read().split("\n"); out = []
for ln in lines:
    m = re.search(r"\s*NEEDTOKNOW:\s*(.+)$", ln)
    if m:
        out += [ln[:m.start()], "", "> **Need to know**", "> - " + m.group(1).strip()]
    else:
        out.append(ln)
open("doc.md", "w", encoding="utf-8").write("\n".join(out))
