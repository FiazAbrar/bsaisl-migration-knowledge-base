"""Get an archived copy of a blocked page from the Wayback Machine (web.archive.org) and save it to raw/.

  python3 ../../tools/wayback.py <original-url> <name> <official|news>

It asks the Wayback CDX index for the newest capture with HTTP 200 (trying the URL with and without "www."),
downloads the original bytes of that capture (the "id_" form, without the archive's toolbar), and saves and
converts it exactly like fetch.py (raw/<name>.pdf + .txt, or .html + .md + .txt).

Logging:
  raw/_fetchlog.csv  url = the ORIGINAL url, method = "wayback:<archive timestamp>"
  raw/_wayback.csv   name, original_url, archive_url, archive_date, source_type (official-archived / news-archived)
Register the source afterwards with ledger.py source --official archived (or news-archived).
"""
import csv, json, os, subprocess, sys, urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fetch  # noqa: E402

fetch.UA = "curl/8.9.1"  # web.archive.org answers 429 to the browser user agent fetch.py normally sends

WB = os.path.join(fetch.RAW, "_wayback.csv")


def cdx(url):
    p = urllib.parse.urlsplit(url)
    host = p.netloc
    alts = [host] + ([host[4:]] if host.startswith("www.") else ["www." + host])
    for h in alts:
        q = urllib.parse.urlunsplit(("", h, p.path, p.query, "")).lstrip("/")
        api = ("https://web.archive.org/cdx/search/cdx?url=" + urllib.parse.quote(q, safe="")
               + "&output=json&filter=statuscode:200&limit=-1")
        r = subprocess.run(["curl", "-s", "--max-time", "60", api], capture_output=True, text=True)
        try:
            rows = json.loads(r.stdout or "[]")
        except ValueError:
            rows = []
        if len(rows) > 1:
            head, last = rows[0], rows[-1]
            rec = dict(zip(head, last))
            return rec["timestamp"], rec["original"]
    return None, None


def main(url, name, kind):
    ts, orig = cdx(url)
    if not ts:
        print(f"NO CAPTURE for {url}")
        return 1
    snap = f"https://web.archive.org/web/{ts}id_/{orig}"
    before = len(fetch.read_log())
    fetch.fetch(snap, name)
    log = fetch.read_log()
    if len(log) == before or log[-1]["name"] != name:
        print(f"DOWNLOAD FAILED for capture {snap}")
        return 1
    # rewrite the last log row so it records the original URL and the archive date
    log[-1]["url"] = url
    log[-1]["method"] = f"wayback:{ts}"
    with open(fetch.LOG, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fetch.FIELDS)
        w.writeheader(); w.writerows(log)
    new = not os.path.exists(WB)
    with open(WB, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["name", "original_url", "archive_url", "archive_date", "source_type"])
        if new:
            w.writeheader()
        w.writerow({"name": name, "original_url": url, "archive_url": f"https://web.archive.org/web/{ts}/{orig}",
                    "archive_date": f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}",
                    "source_type": "official-archived" if kind == "official" else "news-archived"})
    print(f"ARCHIVED {ts[:8]} {name}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[3] not in ("official", "news"):
        print(__doc__); sys.exit(2)
    sys.exit(main(*sys.argv[1:]))
