"""Fetch one URL into sources/ in the current country folder and log it, so nothing is fetched twice.

Usage (run from anywhere):
  python3 ../../tools/fetch.py <url> <name>            fetch with curl, save sources/<name>.html|.pdf, plus a text copy
  python3 ../../tools/fetch.py --log <url> <name> <method>
                                          only log a file you saved yourself (e.g. a Firecrawl
                                          scrape written to sources/<name>.md); method = firecrawl|manual
  python3 ../../tools/fetch.py --find <text>           search the fetch log for a URL or name

Text copies: HTML -> sources/<name>.md (pandoc, gfm), PDF -> sources/<name>.txt (pdftotext -layout).
Quotes in facts.csv must be copied from the text copy (or the .md you saved).
"""
import csv, datetime, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RAW  # noqa: E402
LOG = os.path.join(RAW, "_fetchlog.csv")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
TODAY = datetime.date.today().isoformat()
FIELDS = ["name", "url", "access_date", "http_status", "content_type", "method", "files"]


def read_log():
    if not os.path.exists(LOG):
        return []
    with open(LOG, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def append_log(row):
    new = not os.path.exists(LOG)
    with open(LOG, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if new:
            w.writeheader()
        w.writerow(row)


def check_name(name):
    if not re.fullmatch(r"[a-z0-9][a-z0-9._-]{2,90}", name):
        sys.exit("name must be lowercase letters, digits, . _ - (e.g. imi-plks-main-2026-11)")


def already(url, name):
    for r in read_log():
        if r["url"] == url and r["http_status"].startswith("2"):
            return r
        if r["name"] == name:
            sys.exit(f"name '{name}' already used for {r['url']}; pick another name")
    return None


def fetch(url, name):
    check_name(name)
    prev = already(url, name)
    if prev:
        print(f"ALREADY FETCHED as '{prev['name']}' on {prev['access_date']}: files {prev['files']}")
        return
    tmp = os.path.join(RAW, name + ".part")
    hdr = os.path.join(RAW, name + ".hdr")
    cmd = ["curl", "-s", "-L", "--compressed", "-A", UA, "--max-time", "60",
           "-D", hdr, "-o", tmp, "-w", "%{http_code}|%{content_type}", url]
    p = subprocess.run(cmd, capture_output=True, text=True)
    status, _, ctype = (p.stdout or "000|").partition("|")
    if os.path.exists(hdr):
        os.remove(hdr)
    if not status.startswith("2") or not os.path.exists(tmp) or os.path.getsize(tmp) == 0:
        if os.path.exists(tmp):
            os.remove(tmp)
        print(f"FAILED {status} {p.stderr.strip()[:200]} -> try Firecrawl scrape, then list it under 'Pages we could not download' in notes.md")
        append_log({"name": name + "-FAILED", "url": url, "access_date": TODAY, "http_status": status,
                    "content_type": ctype, "method": "curl", "files": ""})
        return
    with open(tmp, "rb") as f:
        head = f.read(5)
    files = []
    if "pdf" in ctype.lower() or head.startswith(b"%PDF"):
        pdf = os.path.join(RAW, name + ".pdf")
        os.replace(tmp, pdf)
        txt = os.path.join(RAW, name + ".txt")
        subprocess.run(["pdftotext", "-layout", pdf, txt])
        files = [name + ".pdf", name + ".txt"]
    else:
        html = os.path.join(RAW, name + ".html")
        os.replace(tmp, html)
        md = os.path.join(RAW, name + ".md")
        clean = os.path.join(RAW, name + ".clean.tmp.html")
        try:
            from bs4 import BeautifulSoup
            with open(html, "rb") as f:
                soup = BeautifulSoup(f.read(), "html.parser")
            for t in soup(["script", "style", "noscript", "svg", "iframe", "nav", "button"]):
                t.decompose()
            # Some sites (e.g. mom.gov.sg) wrap the whole page body in one <form>: keep its contents.
            for t in soup.find_all("form"):
                t.unwrap()
            for img in soup.find_all("img"):
                if (img.get("src") or "").startswith("data:"):
                    img.decompose()
            # keep the page's own date metadata visible in the text copy
            metas = [f"{m.get('property') or m.get('name')}: {m.get('content')}" for m in soup.find_all("meta")
                     if re.search(r"(date|modified|published|updated)", (m.get('property') or m.get('name') or ''), re.I)]
            with open(clean, "w", encoding="utf-8") as f:
                f.write(("<p>PAGE META: " + " | ".join(metas) + "</p>" if metas else "") + str(soup))
            src = clean
        except Exception as e:
            print("bs4 clean failed, converting raw html:", e)
            src = html
        subprocess.run(["pandoc", "-f", "html", "-t", "gfm-raw_html", "--wrap=none", src, "-o", md])
        files = [name + ".html", name + ".md"]
        # pandoc drops some tables and dropdowns; keep a plain-text copy too so quotes from them can be checked
        try:
            from bs4 import BeautifulSoup
            with open(src, "rb") as f:
                t = BeautifulSoup(f.read(), "html.parser").get_text("\n")
            t = re.sub(r"\n\s*\n+", "\n\n", t)
            with open(os.path.join(RAW, name + ".txt"), "w", encoding="utf-8") as f:
                f.write(t)
            files.append(name + ".txt")
        except Exception as e:
            print("plain-text copy failed:", e)
        if os.path.exists(clean):
            os.remove(clean)
    append_log({"name": name, "url": url, "access_date": TODAY, "http_status": status,
                "content_type": ctype, "method": "curl", "files": ";".join(files)})
    sizes = ", ".join(f"{f} ({os.path.getsize(os.path.join(RAW, f))} B)" for f in files if os.path.exists(os.path.join(RAW, f)))
    print(f"OK {status} {ctype} -> {sizes}")


def log_only(url, name, method):
    check_name(name)
    files = sorted(f for f in os.listdir(RAW) if f.startswith(name + "."))
    if not files:
        sys.exit(f"no file sources/{name}.* found; save it first")
    append_log({"name": name, "url": url, "access_date": TODAY, "http_status": "200",
                "content_type": "", "method": method, "files": ";".join(files)})
    print("logged", files)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--log" and len(a) == 4:
        log_only(a[1], a[2], a[3])
    elif a and a[0] == "--find" and len(a) == 2:
        for r in read_log():
            if a[1].lower() in (r["url"] + r["name"]).lower():
                print(r)
    elif len(a) == 2:
        fetch(a[0], a[1])
    else:
        print(__doc__)
