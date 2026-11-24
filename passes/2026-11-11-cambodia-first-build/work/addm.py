import subprocess, sys, json
T = "../../../../tools/facts.py"
def run(args):
    r = subprocess.run([sys.executable, T] + args, capture_output=True, text=True, encoding="utf-8")
    print((r.stdout + r.stderr).strip())
spec = json.load(open(sys.argv[1], encoding="utf-8"))
for s in spec.get("sources", []):
    run(["source", "--name", s[0], "--publisher", s[1], "--title", s[2], "--official", s[3], "--page-date", s[4]])
for f in spec.get("facts", []):
    args = ["add", "--prefix", spec["prefix"], "--name", f["n"], "--claim", f["c"], "--quote", f["q"], "--page-date", f["d"], "--status", f["s"]]
    if "v" in f: args += ["--visa", f["v"][0], "--field", f["v"][1], "--value", f["v"][2]]
    if "note" in f: args += ["--note", f["note"]]
    run(args)
