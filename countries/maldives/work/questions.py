"""Write questions.md: every Need to know in doc.md, grouped by H2/H3, citations stripped."""
import re
lines = open('doc.md', encoding='utf-8').read().splitlines()
out = ["# Maldives open questions", "",
       "These are the questions the Maldives migration guide can't yet answer, grouped by the guide's sections.", ""]
h2 = h3 = None
printed = set()
count = 0
inblock = False
for ln in lines:
    m = re.match(r"^(#{2,4}) (.*)", ln)
    if m:
        lvl, t = len(m.group(1)), m.group(2).strip()
        if lvl == 2:
            h2, h3 = t, None
        elif lvl == 3:
            h3 = t
        inblock = False
        continue
    s = ln.strip()
    if s.startswith("> **Need to know**"):
        inblock = True
        continue
    if inblock and s.startswith("> - "):
        q = s[4:]
        q = re.sub(r"\s*\[[A-Z]{1,2}\d{4}(?:, ?[A-Z]{1,2}\d{4})*\]", "", q).strip()
        if h2 not in printed:
            out += [f"## {h2}", ""]
            printed.add(h2)
        key = (h2, h3)
        if h3 and key not in printed:
            out += [f"### {h3}", ""]
            printed.add(key)
        out.append(f"- {q}")
        count += 1
        continue
    if inblock and not s.startswith(">"):
        inblock = False
        out.append("")
txt = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"
open('questions.md', 'w', encoding='utf-8').write(txt)
print(count, "questions")
