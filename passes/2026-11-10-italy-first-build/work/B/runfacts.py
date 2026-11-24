"""Run facts.py add for a list of facts in a JSON-like python module. Usage: python runfacts.py batch1"""
import subprocess, sys, importlib
mod = importlib.import_module(sys.argv[1])
for row in mod.F:
    n, c, q, d, s = row[:5]
    x = row[5] if len(row) > 5 else []
    cmd = ["python", "../../../../tools/facts.py", "add", "--prefix", "B", "--name", n, "--claim", c,
           "--quote", q, "--page-date", d, "--status", s] + x
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    out = (r.stdout + r.stderr).strip().replace("\n", " ")
    print(out[-160:], "<-", c[:70])
