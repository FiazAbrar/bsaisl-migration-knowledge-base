"""Write questions.md from the Need to know blocks in doc.md (run from countries/italy)."""
import re
lines = open("doc.md", encoding="utf-8").read().splitlines()
out = ["# Italy open questions", "", "These are the questions the Italy migration guide can't yet answer, grouped by the guide's sections.", ""]
h2 = h3 = None; inblock = False; n = 0; last = None
for ln in lines:
    m = re.match(r"^(#{2,3}) (.*)", ln)
    if m:
        if m.group(1) == "##": h2, h3 = m.group(2), None
        else: h3 = m.group(2)
        continue
    if ln.startswith("> **Need to know**"): inblock = True; continue
    if inblock and ln.startswith("> - "):
        key = (h2, h3)
        if key != last:
            if h2 and (last is None or last[0] != h2): out += [f"## {h2}", ""]
            if h3: out += [f"### {h3}", ""]
            last = key
        out.append("- " + ln[4:]); n += 1; continue
    if inblock and not ln.startswith(">"): inblock = False; out.append("")
open("questions.md", "w", encoding="utf-8").write(re.sub(r"\n{3,}", "\n\n", "\n".join(out)) + "\n")
print(n, "questions")
