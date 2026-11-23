"""Split cross-country/ into four global modules under global/. Run from the repo root.
Each module gets doc.md (its H2 part, headings promoted one level), the facts it cites (plus uncited facts
whose source it uses most), the sources those facts need, and its part of notes.md and questions.md."""
import csv, os, re, shutil, subprocess, collections, sys
csv.field_size_limit(10**9)
OLD = "cross-country"
LEGEND = ('A raised number such as 3 is an official source; N3 is a news, NGO (non-governmental organisation), research '
          'or guide source, listed under "Needs an official source"; a year, like N3 (2022), marks a source older than 2025. '
          '"Need to know" marks a point no source has yet confirmed.')
MODS = [  # folder, H2 prefix in old doc, notes H2 prefix, new title, intro
 ("faq", "## Frequently asked questions", "## Frequently asked questions", "Going abroad: frequently asked questions",
  "The questions people in Bangladesh ask most before, during and after working abroad, answered for every country, as of November 2026. Each country's own doc, in the `countries` folder, answers them for that country."),
 ("dalal-scams", "## Dalal scams", "## Dalal scams", "Dalal scams",
  "The tricks brokers (dalals) and fake agencies use on people going abroad from Bangladesh, how to spot each one, and where to complain, as of November 2026. Each country's own doc gives the scams specific to that country."),
 ("departure", "## Departure bottlenecks", "## Departure bottlenecks", "Departure bottlenecks",
  "Where people going abroad from Bangladesh get stuck, offloaded or asked for bribes: passports and police clearance, the Gulf medical, attestation, BMET clearance, the airport, entry at the destination and coming back, as of November 2026. Each country's own doc gives the steps for that country."),
 ("illegal-routes", "## Illegal routes", "## Illegal routes", "Illegal routes",
  "The irregular routes people from Bangladesh are sold, what happens on them and how they end, and the law and help in Bangladesh, as of November 2026. Each country's own doc covers irregular entry to that country."),
]
def parts(text, prefixes):
    lines = text.split("\n"); idx = {}
    for i, l in enumerate(lines):
        for p in prefixes:
            if l.startswith(p) and l.startswith("## "): idx[p] = i
    order = sorted(idx.items(), key=lambda x: x[1]); out = {}
    for k, (p, i) in enumerate(order):
        j = order[k+1][1] if k+1 < len(order) else len(lines)
        out[p] = lines[i:j]
    return out, lines[:order[0][1]]
doc = open(f"{OLD}/doc.md", encoding="utf-8").read()
dparts, _ = parts(doc, [m[1] for m in MODS])
notes = open(f"{OLD}/notes.md", encoding="utf-8").read()
nparts, nhead = parts(notes, [m[2] for m in MODS])
general_notes = "\n".join(nhead[1:]).strip()
qtext = open(f"{OLD}/questions.md", encoding="utf-8").read()
qparts, _ = parts(qtext, [m[1] for m in MODS])
facts = list(csv.DictReader(open(f"{OLD}/facts.csv", encoding="utf-8", newline="")))
FCOLS = list(facts[0].keys())
srcs = {r["name"]: r for r in csv.DictReader(open(f"{OLD}/sources.csv", encoding="utf-8", newline=""))}
SCOLS = list(next(iter(srcs.values())).keys())
flog = list(csv.DictReader(open(f"{OLD}/sources/_fetchlog.csv", encoding="utf-8", newline="")))
LCOLS = list(flog[0].keys())
fact_src = {f["id"]: f["saved_file"] for f in facts}
def src_name(saved):
    f = (saved or "").split(";")[0]
    c = [k for k in srcs if f.startswith(k + ".")]
    return max(c, key=len) if c else re.sub(r"\.(md|txt|html|pdf)$", "", f)
body = {}; cited = {}
for m in MODS:
    seg = dparts[m[1]]
    b = []
    for l in seg[1:]:
        if re.match(r"#{3,6} ", l): l = l[1:]
        b.append(l)
    body[m[0]] = "\n".join(b).strip("\n")
    cited[m[0]] = set(re.findall(r"\b([A-Z]{1,2}\d{3,5})\b", body[m[0]])) & set(fact_src)
# uncited facts: to the module that cites most facts from the same source; else faq
src_mod = collections.defaultdict(collections.Counter)
for mod, ids in cited.items():
    for i in ids: src_mod[src_name(fact_src[i])][mod] += 1
assign = {m[0]: set(cited[m[0]]) for m in MODS}
unc = collections.Counter()
for f in facts:
    if not any(f["id"] in cited[m] for m in cited):
        c = src_mod.get(src_name(f["saved_file"]))
        mod = c.most_common(1)[0][0] if c else "faq"
        assign[mod].add(f["id"]); unc[mod] += 1
lognames = {r["name"]: r for r in flog}
need = {}
for mod, ids in assign.items():
    need[mod] = {src_name(fact_src[i]) for i in ids}
# a source whose files hold several captures: keep by fetchlog name
users = collections.Counter(n for mod in need for n in need[mod])
for m in MODS:
    mod = m[0]; d = f"global/{mod}"; os.makedirs(f"{d}/sources", exist_ok=True)
    open(f"{d}/doc.md", "w", encoding="utf-8").write(f"# {m[3]}\n\n{m[4]} {LEGEND}\n\n{body[mod]}\n")
    with open(f"{d}/facts.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, FCOLS); w.writeheader()
        for r in facts:
            if r["id"] in assign[mod]: w.writerow(r)
    names = need[mod]
    with open(f"{d}/sources.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, SCOLS); w.writeheader()
        for n, r in srcs.items():
            if n in names: w.writerow(r)
    with open(f"{d}/sources/_fetchlog.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, LCOLS); w.writeheader()
        for r in flog:
            if r["name"] in names: w.writerow(r)
    for n in names:
        files = (lognames[n]["files"].split(";") if n in lognames and lognames[n]["files"] else [])
        files = set(files) | {x for x in os.listdir(f"{OLD}/sources") if x.startswith(n + ".")}
        for fn in files:
            s = f"{OLD}/sources/{fn}"
            if os.path.exists(s): shutil.copy2(s, f"{d}/sources/{fn}")
    nseg = nparts.get(m[2], [])
    nb = "\n".join(("#" + l[2:] if False else (l[1:] if re.match(r"#{3,6} ", l) else l)) for l in nseg[1:]).strip()
    open(f"{d}/notes.md", "w", encoding="utf-8").write(
        f"# {m[3]}: research notes\n\nThis doc was part of the cross-country doc \"Going abroad from Bangladesh\" until 23 Nov 2026, when it was split into four global modules (faq, dalal-scams, departure, illegal-routes). Its fact ids keep their original prefixes.\n\n## How the cross-country doc was put together\n\n{general_notes.split(chr(10),1)[1].strip() if general_notes.startswith('## ') else general_notes}\n\n## This part\n\n{nb}\n")
    qseg = qparts.get(m[1], [])
    qb = "\n".join(qseg[1:]).strip()
    open(f"{d}/questions.md", "w", encoding="utf-8").write(
        f"# {m[3]}: open questions\n\nQuestions this doc can't yet answer. Each is a \"Need to know\" in `doc.md`.\n\n{qb}\n")
    print(mod, "facts", len(assign[mod]), "(uncited", unc[mod], ") sources", len(names), "doc KB", len(body[mod])//1000)
print("sources used by >1 module:", sum(1 for v in users.values() if v > 1), "sources never needed:", len(set(srcs) - set(users)))
