"""Build a country doc. Run from inside the country folder:

  cd countries/<country> && python3 ../../tools/build.py

It reads the one <name>.src.md in the folder and writes:
  README.md        the doc as GitHub shows it (commit it)
  <Country>.docx   the editable Word file, named from the "# <Country>: ..." title (commit it)
  pandoc.md        a build file pandoc turns into the .docx (not committed)

Citations in the source take one of two forms, depending on what the folder has:
  ledger.csv present  cite ledger ids, e.g. [W0012] or [W0012, L0003]. Each id maps to its saved source
                      (raw file -> sources.csv); official sources become [n], others [Nn].
  otherwise           cite keys from refs.md, e.g. [12] (official) or [N104] (news).
Either way the build numbers sources in order of first use, adds the year to sources dated before 2025
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


# ---------- ledger mode ----------

def ledger_sources():
    L = {r["id"]: r for r in load("ledger.csv")}
    S = {r["raw"]: r for r in load("sources.csv")}
    WB = {r["name"]: r for r in load("raw/_wayback.csv")} if os.path.exists("raw/_wayback.csv") else {}

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
        """ledger id -> (source key, official?, year tag, reference text)"""
        if key not in L:
            errors.append(f"unknown ledger id {key}")
            return None
        f = L[key]["raw_file"].split(";")[0]
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

    return r"[A-Z]\d{4}", resolve


# ---------- refs.md mode ----------

def refs_sources():
    text = open("refs.md", encoding="utf-8").read()
    off, news = text.split("## Needs an official source")
    O = {m.group(1): m.group(2) for m in re.finditer(r"^(\d+)\. (.*)$", off, re.M)}
    N = {m.group(1): m.group(2) for m in re.finditer(r"^- N(\d+)\. (.*)$", news, re.M)}

    def tag(t):
        m = re.search(r"\b(19|20)\d\d\b", t.split("[")[0])
        return f" ({m.group(0)})" if m and int(m.group(0)) < 2025 else ""

    def resolve(key, errors):
        d, k = (N, key[1:]) if key.startswith("N") else (O, key)
        if k not in d:
            errors.append(f"citation [{key}] has no entry in refs.md")
            return None
        return key, not key.startswith("N"), tag(d[k]), d[k]

    return r"N?\d+", resolve


# ---------- build ----------

def main():
    srcs = glob.glob("*.src.md")
    if len(srcs) != 1:
        sys.exit(f"expected one *.src.md in this folder, found {srcs}")
    text = open(srcs[0], encoding="utf-8").read()
    country = re.match(r"# ([^:\n]+)", text).group(1).strip()
    pat, resolve = ledger_sources() if os.path.exists("ledger.csv") else refs_sources()

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

    body = re.sub(rf"\[({pat}(?:, ?{pat})*)\](?!\()", rep, text)
    if errors:
        print("\n".join(sorted(set(errors))))
        sys.exit(f"{len(set(errors))} citation errors; fix the source")

    refs = "\n## References\n\n### Official sources\n\n" + "".join(
        f"{i + 1}. []{{#o{i + 1}}}{ref[k]}\n" for i, k in enumerate(om))
    if nm:
        refs += "\n### Needs an official source\n\n" + NEWS_NOTE + "\n\n" + "".join(
            f"- []{{#n{i + 1}}}N{i + 1}. {ref[k]}\n" for i, k in enumerate(nm))
    s = body + refs

    def slug(h):
        return re.sub(r"\s+", "-", re.sub(r"[^\w\s-]", "", h.lower()).strip())
    toc = "## Contents\n\n" + "".join(f"- [{h}](#{slug(h)})\n" for h in re.findall(r"^## (.+)$", s, re.M)) + "\n"
    i = s.index("\n## ") + 1
    s = s[:i] + toc + s[i:]

    open("pandoc.md", "w", encoding="utf-8").write(s)
    # GitHub doesn't render pandoc's []{#id} anchors, so README.md uses HTML anchors.
    open("README.md", "w", encoding="utf-8").write(re.sub(r"\[\]\{#(\w+)\}", r'<a id="\1"></a>', s))

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
    print(f"README.md and {docx}: {len(om)} official sources, {len(nm)} news or third-party")


if __name__ == "__main__":
    main()
