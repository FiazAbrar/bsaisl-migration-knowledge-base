"""Fail if work changed the knowledge base without a LOG.md entry.

Usage (from the repo root): python3 tools/check_log.py [base]   (base defaults to origin/main)
Compares the current branch with base. Exit code 1 if any file under a watched folder changed
but LOG.md did not, or if LOG.md's newest entry doesn't follow the shape shown at its top.
"""
import re, subprocess, sys

WATCHED = ("countries/", "global/", "agencies/", "tools/", "data/", "datasets/", "cross-country/")
base = sys.argv[1] if len(sys.argv) > 1 else "origin/main"
changed = subprocess.run(["git", "diff", "--name-only", f"{base}...HEAD"], capture_output=True, text=True, check=True).stdout.split()
watched = [f for f in changed if f.startswith(WATCHED)]
if not watched:
    print("No watched folders changed; no log entry needed."); sys.exit(0)
if "LOG.md" not in changed:
    print("These files changed but LOG.md did not:")
    print("\n".join("  " + f for f in watched[:20]) + ("\n  ..." if len(watched) > 20 else ""))
    print("Add an entry at the top of LOG.md (shape shown in the file) and commit it with the work.")
    sys.exit(1)
log = open("LOG.md", encoding="utf-8").read().split("\n---\n", 1)[-1]
first = re.search(r"^## (\d{4}-\d{2}-\d{2}[^\n]*) · [^\n]+ · [^\n]+$", log, re.M)
if not first or "**Done:**" not in log[first.start():first.start() + 4000]:
    print("LOG.md changed, but its newest entry doesn't start with '## YYYY-MM-DD · what · who' followed by a '**Done:**' line.")
    sys.exit(1)
print(f"Log entry found: {first.group(0)[3:]}")
