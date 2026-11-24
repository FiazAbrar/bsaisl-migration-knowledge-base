import subprocess, sys, importlib.util, os
here = os.path.dirname(os.path.abspath(__file__))
which = sys.argv[1]
spec = importlib.util.spec_from_file_location("d", os.path.join(here, which))
d = importlib.util.module_from_spec(spec); spec.loader.exec_module(d)
for name, claim, quote, date, status, note in d.F:
    args = [sys.executable, "../../../../tools/facts.py", "add", "--prefix", "N", "--name", name, "--claim", claim,
            "--quote", quote, "--page-date", date, "--status", status]
    if note:
        args += ["--note", note]
    r = subprocess.run(args, capture_output=True, text=True, encoding="utf-8")
    out = (r.stdout + r.stderr).strip().replace("\n", " | ")
    print(out[:200], "<<", claim[:60])
