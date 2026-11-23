"""Save a Prothom Alo article from the archive as a source in a doc folder, and register it.
Usage: python3 save_pa.py <doc folder> <article id>   -> prints the source name (pa-<date>-<slug>)
Then log facts from inside the folder: python3 ../../tools/facts.py add --prefix XX --name <source name> ...
"""
import csv, json, os, subprocess, sys
ARCH = "/Users/rarba/Programming/brac/bits-migration/prothom-alo-archive"
folder, aid = os.path.abspath(sys.argv[1]), sys.argv[2]
TOOLS = os.path.join(os.path.dirname(os.path.dirname(folder)), "tools")  # countries/<c> and global/<m> are both two levels below the repo
d = next((json.loads(l) for l in open(os.path.join(ARCH, "migration-stories.jsonl")) if json.loads(l)["id"] == aid), None)
if d is None:  # stories the filter rejected but a later triage found useful
    d = next(json.loads(l) for l in open(os.path.join(ARCH, "stories.jsonl")) if aid in l and json.loads(l)["id"] == aid)
url = d["url"]
def log():
    p = os.path.join(folder, "sources", "_fetchlog.csv")
    return list(csv.DictReader(open(p, newline="", encoding="utf-8"))) if os.path.exists(p) else []
for r in log():
    if r["url"].rstrip("/") == url.rstrip("/") and r["http_status"].startswith("2") and r["name"].startswith("pa-"):
        print(r["name"]); sys.exit(0)
name = f"pa-{d['published'][:10]}-{url.rstrip('/').split('/')[-1]}".lower()
if any(r["name"] == name for r in log()):
    print(name); sys.exit(0)
path = os.path.join(folder, "sources", name + ".md")
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w", encoding="utf-8") as f:
    f.write(f"# {d['headline'].strip()}\n\nSource: Prothom Alo, {url}\n\nPublished: {d['published']}\n\n")
    f.write("Saved from Prothom Alo's public story API (article text only, no page furniture).\n\n---\n\n")
    f.write(d["text"].strip() + "\n")
def run(args):
    p = subprocess.run([sys.executable] + args, capture_output=True, text=True, cwd=folder)
    if p.returncode: sys.exit(f"failed: {args[0]}: {p.stdout}{p.stderr}")
run([os.path.join(TOOLS, "fetch.py"), "--log", url, name, "manual"])
run([os.path.join(TOOLS, "facts.py"), "source", "--name", name, "--publisher", "Prothom Alo",
     "--title", d["headline"].strip(), "--official", "no", "--page-date", d["published"][:10]])
print(name)
