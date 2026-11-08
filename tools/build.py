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
    # Section numbers (2, 2.1, 2.1.1 ...) down to NUMBER_DEPTH heading levels below H1; 0 turns them off.
    depth = int(os.environ.get("NUMBER_DEPTH", "3"))
    lines, heads, used, inref = s.split("\n"), [], {}, False
    count = [0] * 7
    for n, ln in enumerate(lines):
        m = re.match(r"^(#{1,6}) (.+?)\s*$", ln)
        if not m:
            continue
        lvl = len(m.group(1))
        if lvl == 2:
            inref = m.group(2) == "References"
        shown = m.group(2)
        if depth and 2 <= lvl <= depth + 1 and not inref and m.group(2) != "Contents":
            count[lvl] += 1
            for k in range(lvl + 1, 7):
                count[k] = 0
            shown = ".".join(str(count[k]) for k in range(2, lvl + 1)) + " " + m.group(2)
            lines[n] = m.group(1) + " " + shown
        base = re.sub(r"[^\w\- ]", "", m.group(2).lower()).replace(" ", "-")  # stable: numbers never change the link
        k = used.get(base, 0)
        used[base] = k + 1
        hid = base if k == 0 else f"{base}-{k}"
        heads.append({"n": n, "lvl": lvl, "text": m.group(2), "shown": shown, "id": hid, "ref": inref})

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

    # Anchors on the numbered items of each step, so "Step 1, item 4" can link to the item itself.
    items = {}
    for h in sorted(heads, key=lambda h: -h["lvl"]):  # deepest headings first, so a parent never claims a child's list
        if h["ref"]:
            continue
        # A heading's own list is the first numbered list before its first sub-heading; if there is none there,
        # the first one anywhere inside the heading's section that no other heading has claimed.
        end = next((g["n"] for g in heads if g["n"] > h["n"]), len(lines))
        if not any(re.match(r"^1\. \*\*", lines[n]) for n in range(h["n"] + 1, end)):
            end = next((g["n"] for g in heads if g["n"] > h["n"] and g["lvl"] <= h["lvl"]), len(lines))
        expect = 1  # only the step's own list: 1, 2, 3... in order; stop when another list restarts at 1
        for n in range(h["n"] + 1, end):
            m = re.match(r"^(\d+)\. \*\*(.+?)\*\*", lines[n])
            if m and n not in hmap and int(m.group(1)) == 1 and expect > 2:
                break
            if m and n not in hmap and int(m.group(1)) == expect:
                expect += 1
                aid = f"{h['id']}-item-{m.group(1)}"
                items[(h["id"], m.group(1))] = (aid, m.group(2).strip().rstrip(".,:;"))
                lines[n] = lines[n].replace(f"{m.group(1)}. ", f"{m.group(1)}. \x00A{aid}\x00", 1)

    LINK = re.compile(r"\[[^\]]*\]\([^)]*\)|<[^>]+>|\x00C\d+\x00|\x00A[^\x00]+\x00")

    def link_refs(seg, sec):
        def step(m):
            # "Tourist visa, Step 6": the step of the named H2, not of the section the reference sits in
            sec_ = sec
            pre = re.search(r'("[^"]{4,80}"|[^,;()\[\]"]{3,80}), $', m.string[:m.start()])
            if pre:
                g = pre.group(1)
                for st in ([0] if g.startswith('"') else [k.start() for k in re.finditer(r"\b[A-Z]", g)]):
                    hid0 = find(g[st:], sec)
                    h0 = next((g for g in heads if g["id"] == hid0 and g["lvl"] == 2), None) if hid0 else None
                    if h0:
                        sec_ = h0["n"]
                        break
            h = next((h for h in by_sec.get(sec_, []) if re.match(rf"Step {m.group(1)}\b", h["text"])), None) \
                or next((h for h in heads if not h["ref"] and re.match(rf"Step {m.group(1)}\b", h["text"])), None)
            if not h:
                return m.group(0)
            if m.group(2) and (h["id"], m.group(2)) in items:
                aid, label = items[(h["id"], m.group(2))]
                return f"[Step {m.group(1)}, item {m.group(2)}{m.group(3) or ''}: {label}](#{aid})"
            title = h["text"] if m.group(2) is None else f"Step {m.group(1)}, item {m.group(2)}"
            return f"[{title}](#{h['id']})"
        seg = re.sub(r"\bStep (\d+)(?:, item (\d+)((?:\.\d+)*))?\b", step, seg)
        def named_item(m):
            hid = find(m.group(1), sec)
            if hid and (hid, m.group(2)) not in items:
                # the list may sit under one of the heading's sub-headings: use it if exactly one has that item
                h0 = next(h for h in heads if h["id"] == hid)
                end = next((g["n"] for g in heads if g["n"] > h0["n"] and g["lvl"] <= h0["lvl"]), len(lines))
                subs = [g["id"] for g in heads if h0["n"] < g["n"] < end and (g["id"], m.group(2)) in items]
                if len(subs) == 1:
                    aid, label = items[(subs[0], m.group(2))]
                    return f"[{m.group(1)}, item {m.group(2)}{m.group(3)}: {label}](#{aid})"
            if hid and (hid, m.group(2)) in items:
                aid, label = items[(hid, m.group(2))]
                return f"[{m.group(1)}, item {m.group(2)}{m.group(3)}: {label}](#{aid})"
            return m.group(0)
        seg = re.sub(r"(?<![\[\w])([A-Z][^,;()\[\]]{2,60}?), item (\d+)((?:\.\d+)*)\b", named_item, seg)
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

    toc = "".join("  " * (h["lvl"] - 2) + f"- [{h['shown']}](#{h['id']})\n"
                  for h in heads if h["lvl"] in (2, 3, 4) and h["text"] != "Contents" and not (h["ref"] and h["lvl"] > 2))

    def render(gh):
        out = list(lines)
        for h in heads:
            out[h["n"]] = (f'<a id="{h["id"]}"></a>\n\n' + out[h["n"]]) if gh else (out[h["n"]] + f" {{#{h['id']}}}")
        t = "\n".join(out).replace("\x00TOC\x00", toc.rstrip("\n"))
        def c(m):
            items = cites[int(m.group(1))]
            if gh:
                return "<sup>" + ", ".join(f"[{a}]({b})" for a, b in items) + "</sup>"
            return "^" + ",\\ ".join(f"[{a.replace(' ', chr(92) + ' ')}]({b})" for a, b in items) + "^"
        t = re.sub(r"\x00A([^\x00]+)\x00", (lambda m: f'<a id="{m.group(1)}"></a>') if gh else (lambda m: f"[]{{#{m.group(1)}}}"), t)
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
