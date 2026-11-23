"""Apply checker fix files (old_str -> new_str) to the guide files. Usage: python3 apply_fixes.py fix-a.json ..."""
import json, os, sys
KB = "/Users/rarba/Programming/brac/bits-migration/kb-scam-cases"
HERE = os.path.dirname(os.path.abspath(__file__))
done_path = os.path.join(HERE, "fixes-applied.json")
done = json.load(open(done_path)) if os.path.exists(done_path) else []
for f in sys.argv[1:]:
    ok = skip = 0
    for x in json.load(open(os.path.join(HERE, f))):
        doc = x["doc"] if x["doc"].startswith("/") else x["doc"].replace("kb-scam-cases/", "")
        path = doc if doc.startswith("/") else os.path.join(KB, doc)
        s = open(path, encoding="utf-8").read()
        n = s.count(x["old_str"])
        if n != 1:
            print(f"{f}: SKIP ({n} matches) {x['old_str'][:90]!r}"); skip += 1; continue
        s = s.replace(x["old_str"], x["new_str"])
        if x["new_str"] == "":
            s = s.replace("\n\n\n", "\n\n")
        open(path, "w", encoding="utf-8").write(s)
        done.append({"file": f, "section": x.get("section"), "problem": x.get("problem")}); ok += 1
    print(f"{f}: applied {ok}, skipped {skip}")
json.dump(done, open(done_path, "w"), ensure_ascii=False, indent=1)
