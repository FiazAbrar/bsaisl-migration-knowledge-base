"""Build a country doc. Run from inside the country folder:

  cd countries/<country> && python3 ../../tools/build.py

It reads doc.md and writes:
  README.md        the doc as GitHub shows it (commit it)
  <Country>.docx   the editable Word file, named from the "# <Country>: ..." title (commit it)
  <Country>.pdf    a PDF of the Word file, if LibreOffice is installed (not committed: it's large and rebuilt often)
  pandoc.md        a build file pandoc turns into the .docx (not committed)

In doc.md, cite fact ids from facts.csv, e.g. [W0012] or [W0012, L0003]. Each id maps to its saved source
(sources.csv); official sources become [n], others [Nn]. The build numbers sources in order of first use, adds the year to sources dated before 2025
(e.g. [N3 (2022)]), links each citation to its reference, writes the reference list and the Contents
list, and stops if a citation has no source.
"""
import csv, glob, os, re, subprocess, sys, zipfile, shutil

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import CUTOFF  # noqa: E402

MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
NEWS_NOTE = ("These facts come only from news or third-party sources. Each needs an official source, "
             "or a reviewer's confirmation, before the Navigator uses it.")


def load(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# ---------- sources ----------

def load_sources():
    L = {r["id"]: r for r in load("facts.csv")}
    S = {r["name"]: r for r in load("sources.csv")}
    WB = {r["name"]: r for r in load("sources/_wayback.csv")} if os.path.exists("sources/_wayback.csv") else {}

    def nice(d):
        if not d or d == "undated":
            return ""
        p = d.split("-")
        if len(p) == 3:
            return f"{int(p[2])} {MONTHS[int(p[1]) - 1]} {p[0]}"
        if len(p) == 2:
            return f"{MONTHS[int(p[1]) - 1]} {p[0]}"
        return p[0]

    def ref_line(stem):
        s = S[stem]
        date, acc = nice(s["page_date"]), nice(s["access_date"])
        pd = s["page_date"]
        if not pd or pd == "undated":
            flag = " Undated: possibly outdated."
        elif (pd + "-01-01"[len(pd) - 4:]) < CUTOFF:
            flag = " Possibly outdated."
        else:
            flag = ""
        wb = WB.get(stem)
        arch = f" Archived copy, Wayback Machine, {nice(wb['archive_date'])}: [{wb['archive_url']}]({wb['archive_url']})." if wb else ""
        return f"{s['publisher']}{', ' + date if date else ''}. [{s['title']}]({s['url']}). Accessed {acc}.{arch}{flag}"

    def resolve(key, errors):
        """fact id -> (source key, official?, year tag, reference text)"""
        if key not in L:
            errors.append(f"unknown fact id {key}")
            return None
        f = L[key]["saved_file"].split(";")[0]
        cands = [k for k in S if f.startswith(k + ".")]
        if not cands:
            errors.append(f"{key}: source for '{f}' not registered in sources.csv")
            return None
        stem = max(cands, key=len)
        official = S[stem]["official"].lower() in ("yes", "y", "archived")
        if L[key]["status"] in ("verified", "possibly-outdated") and not official:
            errors.append(f"{key} has status {L[key]['status']} but source {stem} is not official")
        pd = S[stem]["page_date"]
        tag = f" ({pd[:4]})" if pd and pd != "undated" and int(pd[:4]) < 2025 else ""
        return stem, official, tag, ref_line(stem)

    return r"[A-Z]{1,2}\d{4}", resolve


# ---------- build ----------

def main():
    if not os.path.exists("doc.md"):
        sys.exit("no doc.md here; run this from inside a country folder")
    text = open("doc.md", encoding="utf-8").read()
    country = re.match(r"# ([^:\n]+)", text).group(1).strip()
    pat, resolve = load_sources()

    om, nm, ref, errors = [], [], {}, []

    def rep(m):
        nums, seen = [], set()
        for key in [x.strip() for x in m.group(1).split(",")]:
            r = resolve(key, errors)
            if not r or r[0] in seen:
                continue
            stem, official, tag, line = r
            seen.add(stem)
            ref[stem] = line
            lst, a, pre = (om, "o", "") if official else (nm, "n", "N")
            if stem not in lst:
                lst.append(stem)
            i = lst.index(stem) + 1
            nums.append(f"[{pre}{i}{tag}](#{a}{i})")
        return "\\[" + ", ".join(nums) + "\\]"

    cites = []

    def hold(m):
        r = rep(m)
        cites.append(re.findall(r"\[([^\[\]]+)\]\((#[on]\d+)\)", r))
        return f"\x00C{len(cites) - 1}\x00"

    body = re.sub(rf"\[({pat}(?:, ?{pat})*)\](?!\()", hold, text)
    if errors:
        print("\n".join(sorted(set(errors))))
        sys.exit(f"{len(set(errors))} citation errors; fix the source")

    refs = "\n## References\n\n### Official sources\n\n" + "".join(
        f"{i + 1}. []{{#o{i + 1}}}{ref[k]}\n" for i, k in enumerate(om))
    if nm:
        refs += "\n### Needs an official source\n\n" + NEWS_NOTE + "\n\n" + "".join(
            f"- []{{#n{i + 1}}}N{i + 1}. {ref[k]}\n" for i, k in enumerate(nm))
    s = body + refs

    # "Sources checked up to": the latest access date among the sources cited.
    acc = {r["name"]: r["access_date"] for r in load("sources.csv")} if os.path.exists("sources.csv") else {}
    dates = sorted(acc[k] for k in om + nm if acc.get(k))
    if dates:
        y, mo, d = dates[-1].split("-")
        line = f"Sources checked up to {int(d)} {MONTHS[int(mo) - 1]} {y}."
        t = s.index("\n") + 1
        s = s[:t] + "\n" + line + "\n" + s[t:]

    i = s.index("\n## ") + 1
    s = s[:i] + "## Contents\n\n\x00TOC\x00\n\n" + s[i:]

    # Heading ids as GitHub makes them (duplicates get -1, -2, ...); pandoc gets the same ids explicitly.
    lines, heads, used, inref = s.split("\n"), [], {}, False
    for n, ln in enumerate(lines):
        m = re.match(r"^(#{1,6}) (.+?)\s*$", ln)
        if not m:
            continue
        base = re.sub(r"[^\w\- ]", "", m.group(2).lower()).replace(" ", "-")
        k = used.get(base, 0)
        used[base] = k + 1
        hid = base if k == 0 else f"{base}-{k}"
        lvl = len(m.group(1))
        if lvl == 2:
            inref = m.group(2) == "References"
        heads.append({"n": n, "lvl": lvl, "text": m.group(2), "id": hid, "ref": inref})

    # Section of each line: index of the H2 it sits under.
    h2_of, cur = [], -1
    hmap = {h["n"]: h for h in heads}
    for n in range(len(lines)):
        if n in hmap and hmap[n]["lvl"] == 2:
            cur = n
        h2_of.append(cur)
    by_sec = {}
    for h in heads:
        if not h["ref"]:
            by_sec.setdefault(h2_of[h["n"]], []).append(h)

    def find(title, sec, prefix=False):
        t = title.strip().strip('"').lower()
        if len(t) < 4:
            return None
        ok = (lambda h: h["text"].lower().startswith(t)) if prefix else (lambda h: h["text"].lower() == t)
        local = [h for h in by_sec.get(sec, []) if ok(h)]
        if len(local) == 1:
            return local[0]["id"]
        glob = [h for h in heads if not h["ref"] and ok(h)]
        return glob[0]["id"] if len(glob) == 1 else None

    LINK = re.compile(r"\[[^\]]*\]\([^)]*\)|<[^>]+>|\x00C\d+\x00")

    def link_refs(seg, sec):
        def step(m):
            hid = None
            for h in by_sec.get(sec, []):
                if re.match(rf"Step {m.group(1)}\b", h["text"]):
                    hid = h["id"]
                    break
            return f"[{m.group(0)}](#{hid})" if hid else m.group(0)
        seg = re.sub(r"\bStep (\d+)\b", step, seg)
        def see(m):
            hid = find(m.group(2), sec) or (len(m.group(2)) >= 15 and find(m.group(2), sec, prefix=True))
            return f"{m.group(1)}[{m.group(2)}](#{hid})" if hid else m.group(0)
        seg = re.sub(r'(\bsee |\()("[^"]{4,80}"|[A-Z][^,;.()\[\]]{2,80}?)(?=[,;.)])', see, seg)
        return seg

    for n, ln in enumerate(lines):
        if n in hmap or h2_of[n] < 0 or "\x00TOC\x00" in ln:
            continue
        if any(h["ref"] for h in heads if h["n"] == h2_of[n]):
            continue
        parts, last, out = [], 0, []
        for m in LINK.finditer(ln):
            out.append(link_refs(ln[last:m.start()], h2_of[n]))
            out.append(m.group(0))
            last = m.end()
        out.append(link_refs(ln[last:], h2_of[n]))
        lines[n] = "".join(out)

    toc = "".join("  " * (h["lvl"] - 2) + f"- [{h['text']}](#{h['id']})\n"
                  for h in heads if h["lvl"] in (2, 3, 4) and h["text"] != "Contents" and not (h["ref"] and h["lvl"] > 2))

    def render(gh):
        out = list(lines)
        if not gh:
            for h in heads:
                out[h["n"]] = out[h["n"]] + f" {{#{h['id']}}}"
        t = "\n".join(out).replace("\x00TOC\x00", toc.rstrip("\n"))
        def c(m):
            items = cites[int(m.group(1))]
            if gh:
                return "<sup>" + ", ".join(f"[{a}]({b})" for a, b in items) + "</sup>"
            return "^" + ",\\ ".join(f"[{a.replace(' ', chr(92) + ' ')}]({b})" for a, b in items) + "^"
        return re.sub(r"\x00C(\d+)\x00", c, t)

    # pandoc needs a blank quote line before a list inside a quote block (GitHub doesn't).
    pdoc = re.sub(r"(?m)^( *> \*\*Need to know\*\*)\n( *)> - ", lambda m: f"{m.group(1)}\n{m.group(2)}>\n{m.group(2)}> - ", render(False))
    open("pandoc.md", "w", encoding="utf-8").write(pdoc)
    # GitHub doesn't render pandoc's []{#id} anchors, so README.md uses HTML anchors.
    open("README.md", "w", encoding="utf-8").write(re.sub(r"\[\]\{#(\w+)\}", r'<a id="\1"></a>', render(True)))

    docx = f"{country}.docx"
    subprocess.run(["pandoc", "pandoc.md", "-o", docx], check=True)
    # pandoc uses "–" for nested bullets; make every level "•".
    tmp = docx + ".tmp"
    with zipfile.ZipFile(docx) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for it in zin.infolist():
            d = zin.read(it.filename)
            if it.filename == "word/numbering.xml":
                d = d.replace('w:lvlText w:val="–"'.encode(), 'w:lvlText w:val="•"'.encode())
            zout.writestr(it, d)
    shutil.move(tmp, docx)
    # PDF from the .docx, if LibreOffice is installed.
    soffice = shutil.which("soffice") or "/Applications/LibreOffice.app/Contents/MacOS/soffice"
    made = ""
    if os.path.exists(soffice):
        r = subprocess.run([soffice, "--headless", "--convert-to", "pdf", docx], capture_output=True, text=True)
        made = f", {country}.pdf" if r.returncode == 0 else " (PDF failed: " + r.stderr.strip()[:200] + ")"
    print(f"README.md, {docx}{made}: {len(om)} official sources, {len(nm)} news or third-party")


if __name__ == "__main__":
    main()
