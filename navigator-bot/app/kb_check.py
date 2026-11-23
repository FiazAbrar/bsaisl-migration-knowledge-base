"""Can the bot still read every guide? Run on every pull request (.github/workflows/bot-kb-check.yml).

Compares the guides in this checkout with those on the base branch, using the same rules the live
bot uses before it swaps in a new index (app/kb_index.py):
- a guide that is on the base branch must still exist (same folder, with its doc.md);
- a guide with 20 or more sections must keep at least half of them;
- every guide must have text under its headings.
Fails with a plain message pointing to KB-STRUCTURE.md. Warnings (no facts.csv, for example) don't fail.

    cd navigator-bot && python -m app.kb_check --base origin/main
"""
import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

from app.kb_index import ROOT, SKIP_DIRS, compare, discover, parse_doc

KB = ROOT.parent


def _head_counts() -> tuple[dict, list[str]]:
    counts, problems = {}, []
    for slug, _, path in discover(KB):
        try:
            _, sections = parse_doc(path, slug)
        except (OSError, UnicodeDecodeError) as e:
            problems.append(f"{path.relative_to(KB)}: can't be read ({type(e).__name__})")
            continue
        if not sections:
            problems.append(f"{path.relative_to(KB)}: has no text under its headings")
        counts[slug] = len(sections)
    return counts, problems


def _base_counts(base: str) -> dict:
    """Section counts of every guide on the base branch, read straight from git."""
    files = subprocess.run(["git", "-C", str(KB), "ls-tree", "-r", "--name-only", base],
                           capture_output=True, text=True, check=True).stdout.split("\n")
    paths = [f for f in files if f.endswith("/doc.md")
             and not any(part in SKIP_DIRS or part.startswith(".") for part in f.split("/")[:-1])]
    folders = [tuple(p.split("/")[:-1]) for p in paths]
    names = [f[-1] for f in folders]
    counts = {}
    with tempfile.TemporaryDirectory() as tmp:
        for path, folder in zip(paths, folders):
            slug = folder[-1] if names.count(folder[-1]) == 1 else "-".join(folder)
            text = subprocess.run(["git", "-C", str(KB), "show", f"{base}:{path}"],
                                  capture_output=True, check=True).stdout
            copy = Path(tmp) / "doc.md"
            copy.write_bytes(text)
            counts[slug] = len(parse_doc(copy, slug)[1])
    return counts


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="origin/main", help="git ref to compare with")
    args = ap.parse_args()

    head, problems = _head_counts()
    problems += compare(_base_counts(args.base), head)
    print(f"Guides the bot can read: {len(head)} ({sum(head.values())} sections)")
    for slug, n in sorted(head.items()):
        print(f"  {slug:28} {n:5} sections")
    if problems:
        print("\nThe bot would refuse this version of the knowledge base:")
        for p in problems:
            print(f"  - {p}")
        print("\nIf a guide was moved or renamed on purpose, say so in the pull request; the bot picks up the "
              "new folder by itself, but the check flags the old one as gone. The structure the bot expects "
              "is in KB-STRUCTURE.md.")
        return 1
    print("\nOK: every guide on the base branch is still there and readable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
