"""Flag doc.md sentences whose numbers don't appear in any cited fact (claim+quote+value+note).
Usage: python numcheck.py <country_dir>"""
import csv, re, sys, os
C = sys.argv[1]
F = {r["id"]: r for r in csv.DictReader(open(os.path.join(C, "facts.csv"), encoding="utf-8"))}
doc = open(os.path.join(C, "doc.md"), encoding="utf-8").read().splitlines()
CIT = re.compile(r"\[([A-Z]{1,2}\d{4}(?:, ?[A-Z]{1,2}\d{4})*)\]")
NUM = re.compile(r"(?<![A-Z\d])(\d[\d,\.]*\d|\d)(?![\d])")
bn = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")
def nums(t):
    t = t.translate(bn)
    out = set()
    for m in NUM.findall(t):
        v = m.replace(",", "").rstrip(".")
        if v and len(v.replace(".", "")) >= 2:
            out.add(v)
    return out
missing_ids, flags = set(), 0
for ln, line in enumerate(doc, 1):
    if line.startswith("#"):
        continue
    # split into segments ending in a citation
    pos = 0
    for m in CIT.finditer(line):
        seg = line[pos:m.start()]
        pos = m.end()
        ids = [i.strip() for i in m.group(1).split(",")]
        for i in ids:
            if i not in F:
                missing_ids.add(i)
        seg_clean = re.sub(r"\]\([^)]*\)", "]", seg)          # drop link targets
        seg_clean = re.sub(r"https?://\S+|[\w\.]+\.(?:mv|bd|com|org|gov)\S*", " ", seg_clean)
        seg_clean = re.sub(r"\((?:Step|see)[^)]*\)", " ", seg_clean)
        seg_clean = re.sub(r"Step \d+(, item \d+)?", " ", seg_clean)
        need = nums(seg_clean)
        if not need:
            continue
        have = set()
        for i in ids:
            r = F.get(i)
            if r:
                have |= nums(" ".join([r["claim"], r["quote"], r.get("value", ""), r.get("note", "")]))
        # normalise: 1,15,000 -> 115000 handled by comma strip; also lakh
        miss = [n for n in need if n not in have and n.split(".")[0] not in have]
        if miss:
            flags += 1
            print(f"L{ln} [{','.join(ids)}] missing {miss}: ...{seg_clean[-140:].strip()}")
print("UNKNOWN IDS:", sorted(missing_ids))
print("flags:", flags)
