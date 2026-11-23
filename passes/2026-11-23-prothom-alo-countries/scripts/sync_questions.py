"""Add to questions.md every "Need to know" bullet in doc.md that the file lacks, under the doc's H2 section.
Creates questions.md for a doc that has none. Usage: python3 sync_questions.py <doc folder> [...]"""
import os, re, sys, unicodedata
N = lambda s: re.sub(r"\s+", " ", unicodedata.normalize("NFC", re.sub(r"\s*\[[^\]]*\]", "", s))).strip().rstrip("?").lower()
for folder in sys.argv[1:]:
    doc = open(os.path.join(folder, "doc.md"), encoding="utf-8").read().split("\n")
    title = doc[0].lstrip("# ").split(":")[0].strip()
    qs, h2 = [], "Background"
    for l in doc:
        if l.startswith("## "): h2 = l[3:].strip()
        m = re.match(r">\s*-\s+(.*)", l)
        if m: qs.append((h2, re.sub(r"\s*\[[^\]]*\]", "", m.group(1)).strip()))
    qp = os.path.join(folder, "questions.md")
    text = open(qp, encoding="utf-8").read() if os.path.exists(qp) else \
        f"# {title} open questions\n\nThese are the questions the {title} doc can't yet answer, grouped by the doc's sections. Each is a \"Need to know\" in `doc.md`.\n"
    extra = open(qp + ".basehave", encoding="utf-8").read() if os.path.exists(qp + ".basehave") else ""
    have = {N(l.lstrip()[2:]) for l in (text + "\n" + extra).split("\n") if l.lstrip().startswith("- ")}
    new = [(h, q) for h, q in qs if N(q) not in have]
    lines = text.rstrip("\n").split("\n")
    added = 0
    for h, q in new:
        try:
            i = lines.index(f"## {h}")
            j = i + 1
            while j < len(lines) and not lines[j].startswith("## "): j += 1
            while lines[j - 1].strip() == "": j -= 1
            lines.insert(j, f"- {q}")
        except ValueError:
            lines += ["", f"## {h}", "", f"- {q}"]
        added += 1
    open(qp, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"{folder}: {len(qs)} in doc, {added} added")
