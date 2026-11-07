"""Build Malaysia.md from malaysia.src.md.

In the source, cite ledger ids: [W0012] or [W0012, L0003, B0101]. Every cited id must exist in ledger.csv
(run tools/merge.py first). The build:
  - maps each ledger id to its source (raw file -> sources.csv) and numbers sources in order of first use;
    official sources become [n], unofficial ones [Nn]; several ids from one source collapse to one number;
  - adds the year to sources dated before 2025, e.g. [N3 (2022)];
  - refuses an 'unofficial' row outside a paragraph containing "unofficial, not verified";
  - refuses an official-status row (verified / possibly-outdated / conflict) whose source is not official;
  - writes the reference list (with access dates, and "possibly outdated" for undated or pre-6-Nov-2025 pages)
    and the Contents list; writes malaysia-ref-list.md; lists any paragraph with no citation.

  python build.py
  pandoc "Malaysia.md" -o "Malaysia.docx"
  python fixbullets.py "Malaysia.docx"
"""
import csv, re, sys

CUTOFF = "2025-11-06"
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def load(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


L = {r["id"]: r for r in load("ledger.csv")}
S = {r["raw"]: r for r in load("sources.csv")}


def src_of(rid):
    f = L[rid]["raw_file"].split(";")[0]
    cands = [k for k in S if f.startswith(k + ".")]
    if not cands:
        sys.exit(f"{rid}: source for '{f}' not registered in sources.csv")
    return max(cands, key=len)


def nice(d):
    if not d or d == "undated":
        return ""
    p = d.split("-")
    if len(p) == 3:
        return f"{int(p[2])} {MONTHS[int(p[1]) - 1]} {p[0]}"
    if len(p) == 2:
        return f"{MONTHS[int(p[1]) - 1]} {p[0]}"
    return p[0]


def old(d):
    if not d or d == "undated":
        return True
    full = d + "-01-01"[len(d) - 4:]
    return full < CUTOFF


def year_tag(d):
    return f" ({d[:4]})" if d and d != "undated" and int(d[:4]) < 2025 else ""


def ref_line(stem):
    s = S[stem]
    date = nice(s["page_date"])
    acc = nice(s["access_date"])
    flag = " Undated: possibly outdated." if (not s["page_date"] or s["page_date"] == "undated") else (
        " Possibly outdated." if old(s["page_date"]) else "")
    arch = ""
    if True:
        wb = {r["name"]: r for r in load("raw/_wayback.csv")}.get(stem)
        if wb:
            arch = f" Archived copy, Wayback Machine, {nice(wb['archive_date'])}: [{wb['archive_url']}]({wb['archive_url']})."
    return f"{s['publisher']}{', ' + date if date else ''}. [{s['title']}]({s['url']}). Accessed {acc}.{arch}{flag}"


def build(inp, out):
    text = open(inp, encoding="utf-8").read()
    om, nm, errors = [], [], []
    paras = re.split(r"\n\s*\n", text)
    built = []
    for para in paras:
        def rep(m):
            nums, seen = [], set()
            for rid in [x.strip() for x in m.group(1).split(",")]:
                if rid not in L:
                    errors.append(f"unknown ledger id {rid}")
                    continue
                st = L[rid]["status"]
                if st == "unofficial" and "unofficial, not verified" not in para:
                    errors.append(f"{rid} is unofficial but the paragraph lacks 'unofficial, not verified': {para[:80]}...")
                if L[rid]["source_type"] == "news" and L[rid]["status"] in ("verified", "possibly-outdated"):
                    errors.append(f"{rid}: news source with official status")
                stem = src_of(rid)
                official = S[stem]["official"].lower() in ("yes", "y", "archived")
                if st in ("verified", "possibly-outdated") and not official:
                    errors.append(f"{rid} has status {st} but source {stem} is not official")
                if stem in seen:
                    continue
                seen.add(stem)
                tag = year_tag(S[stem]["page_date"])
                if official:
                    if stem not in om: om.append(stem)
                    i = om.index(stem) + 1
                    nums.append(f"[{i}{tag}](#o{i})")
                else:
                    if stem not in nm: nm.append(stem)
                    i = nm.index(stem) + 1
                    nums.append(f"[N{i}{tag}](#n{i})")
            return "\\[" + ", ".join(nums) + "\\]"
        built.append(re.sub(r"\[([A-Z]\d{4}(?:, ?[A-Z]\d{4})*)\](?!\()", rep, para))
    s = "\n\n".join(built)
    uncited = [p.strip()[:90] for p in paras
               if p.strip() and not p.lstrip().startswith(("#", "|", "<!--")) and not re.search(r"\[[A-Z]\d{4}", p)
               and len(p.strip()) > 40]
    if errors:
        print("\n".join(sorted(set(errors))))
        sys.exit(f"{len(set(errors))} citation errors; fix the source")
    refs = "\n## References\n\n### Official sources\n\n" + "".join(
        f"{i + 1}. []{{#o{i + 1}}}{ref_line(k)}\n" for i, k in enumerate(om))
    if nm:
        refs += ("\n### Needs an official source\n\nThese facts come only from news, NGO, research or agency sources, "
                 "used after an official search failed. Each needs an official source, or a reviewer's confirmation, "
                 "before the Navigator uses it. Exact facts (fees, eligibility, documents, processing times, legal rules) "
                 "found only here are written as \"Need to know\" and labelled \"unofficial, not verified\".\n\n"
                 + "".join(f"- []{{#n{i + 1}}}N{i + 1}. {ref_line(k)}\n" for i, k in enumerate(nm)))
    s += refs
    heads = re.findall(r"^## (.+)$", s, re.M)

    def slug(h):
        h = re.sub(r"[^\w\s-]", "", h.lower()).strip()
        return re.sub(r"\s+", "-", h)
    toc = "## Contents\n\n" + "".join(f"- [{h}](#{slug(h)})\n" for h in heads) + "\n"
    i = s.index("\n## ") + 1
    s = s[:i] + toc + s[i:]
    open(out, "w", encoding="utf-8").write(s)
    open("malaysia-ref-list.md", "w", encoding="utf-8").write("# Malaysia: reference list" + refs)
    print(f"{out}: {len(om)} official sources, {len(nm)} unofficial")
    if uncited:
        print(f"{len(uncited)} paragraphs without a citation:")
        for u in uncited:
            print("  -", u)


build("malaysia.src.md", "Malaysia.md")
