"""Apply checker fixes (old_str -> new_str) to doc.md files. Usage: python3 apply_fixes.py checks/fix-x.json ...
Logs each applied fix to checks/fixes-applied.json; skips (and reports) any old_str that doesn't occur exactly once."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
log_p = os.path.join(HERE, "checks", "fixes-applied.json")
done = json.load(open(log_p)) if os.path.exists(log_p) else []
for f in sys.argv[1:]:
    ok = skip = 0
    for x in json.load(open(f)):
        p = x["doc"]; s = open(p, encoding="utf-8").read(); n = s.count(x["old_str"])
        if n != 1:
            print(f"SKIP ({n}) {x.get('section','')}: {x['old_str'][:80]!r}"); skip += 1; continue
        s = s.replace(x["old_str"], x["new_str"])
        if not x["new_str"]: s = s.replace("\n\n\n", "\n\n")
        open(p, "w", encoding="utf-8").write(s); ok += 1
        done.append({"file": os.path.basename(f), "doc": p, "section": x.get("section"), "problem": x.get("problem")})
    print(f"{os.path.basename(f)}: applied {ok}, skipped {skip}")
json.dump(done, open(log_p, "w"), ensure_ascii=False, indent=1)
