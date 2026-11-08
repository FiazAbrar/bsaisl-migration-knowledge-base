import sys, json
p = sys.argv[2] if len(sys.argv) > 2 else 'doc.md'
s = open(p, encoding='utf-8').read()
R = json.load(open(sys.argv[1], encoding='utf-8'))
bad = 0
for a, b in R:
    n = s.count(a)
    if n != 1:
        print("MISS", n, a[:100]); bad += 1; continue
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8').write(s)
print("applied", len(R) - bad, "missed", bad)
