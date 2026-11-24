"""Rebuild the backlog part of MANUAL-DOWNLOADS.md: every page a doc's notes.md lists as blocked or not
downloadable, minus pages that doc has since saved. Run from the repo root: python3 tools/manual_downloads.py
The hand-kept "Get these first" part above the marker line is left as it is."""
import csv, glob, os, re

csv.field_size_limit(10**9)
MARK = "<!-- generated backlog below: python3 tools/manual_downloads.py -->"
HEAD = re.compile(r"(?im)^(#+) +[^\n]*(could not download|couldn.t download|blocked|to download|not retrievable)[^\n]*$")
BOLD = re.compile(r"(?im)^\*\*[^\n]*(could not download|pages we could not)[^\n]*\*\*[^\n]*$")
out = []
for notes in sorted(glob.glob("countries/*/notes.md") + glob.glob("global/*/notes.md") + ["agencies/notes.md"]):
    d = os.path.dirname(notes)
    s = open(notes, encoding="utf-8").read()
    saved = set()
    for path, key in ((f"{d}/sources/_fetchlog.csv", "url"), (f"{d}/sources.csv", "url")):
        if os.path.exists(path):
            for r in csv.DictReader(open(path, encoding="utf-8")):
                if path.endswith("_fetchlog.csv") and not str(r.get("http_status", "")).startswith("2"):
                    continue
                saved.add((r.get(key) or "").rstrip("/"))
    urls = []
    for m in list(HEAD.finditer(s)) + list(BOLD.finditer(s)):
        seg = s[m.end():]
        if m.group(0).startswith("#"):
            nxt = re.search(r"(?m)^#{1,%d} " % len(m.group(1)), seg)
        else:
            nxt = re.search(r"(?m)^(#+ |\*\*)", seg)
        seg = seg[:nxt.start()] if nxt else seg
        urls += [u.rstrip(".;:") for u in re.findall(r"https?://[^\s)\]>,`*\"']+", seg)]
    urls = [u for u in dict.fromkeys(urls) if u.rstrip("/") not in saved]
    if urls:
        out.append(f"### {d} ({len(urls)})\n\nWhat each page should prove is in `{notes}`.\n\n" + "\n".join(f"- {u}" for u in urls) + "\n")
p = "MANUAL-DOWNLOADS.md"
top = open(p, encoding="utf-8").read().split(MARK)[0] if os.path.exists(p) else ""
total = sum(int(re.search(r"\((\d+)\)", o).group(1)) for o in out)
open(p, "w", encoding="utf-8").write(top.rstrip() + "\n\n" + MARK + "\n\n## Full backlog (" + str(total) + " pages)\n\nGenerated from the docs' notes; pages a doc has since saved are left out. Many are older and lower priority than the list above.\n\n" + "\n".join(out))
print(f"{total} pages in {len(out)} docs")
