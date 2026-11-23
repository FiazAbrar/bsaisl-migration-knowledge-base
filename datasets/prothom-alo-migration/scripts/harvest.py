"""Harvest migration-related stories from Prothom Alo's public search API.

Writes one JSON object per story to stories.jsonl (deduplicated by story id).
Resumable: finished (query, time-window) keys are kept in done.txt.
www.prothomalo.com is blocked in this Mac's /etc/hosts, so each request
resolves the real IP itself; the hosts file is left untouched.
"""
import json, os, re, subprocess, sys, time, urllib.parse, html
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "stories.jsonl")
DONE = os.path.join(HERE, "done.txt")
LOG = os.path.join(HERE, "harvest.log")
IP = "104.17.144.114"
FIELDS = "headline,subheadline,slug,url,published-at,first-published-at,author-name,sections,tags,summary,cards,story-template"
START = int(datetime(2024, 1, 1, tzinfo=timezone.utc).timestamp() * 1000)
END = int(time.time() * 1000)

KEYWORDS = ["অভিবাসন", "অভিবাসী", "জনশক্তি", "মানবপাচার", "পাচার", "বিএমইটি", "প্রবাসীকল্যাণ",
            "ভূমধ্যসাগর", "রিক্রুটিং", "দালাল", "শ্রমবাজার", "বিদেশফেরত", "প্রবাসী", "ভিসা",
            "রেমিট্যান্স", "বিদেশগামী", "প্রবাসফেরত", "লিবিয়া", "বোয়েসেল", "কফিল", "আকামা", "ইকামা"]
TAGS = ["অভিবাসন", "অভিবাসী", "প্রবাসী কর্মী", "প্রবাসী শ্রমিক", "প্রবাসী", "মানবপাচার", "পাচার",
        "জনশক্তি", "ভিসা", "প্রতারণা", "রেমিট্যান্স", "শ্রমবাজার", "দালাল", "প্রবাসী আয়"]

def log(msg):
    line = f"{datetime.now().strftime('%H:%M:%S')} {msg}"
    print(line, flush=True)
    with open(LOG, "a") as f: f.write(line + "\n")

def get(params):
    url = "https://www.prothomalo.com/api/v1/advanced-search?" + urllib.parse.urlencode(params)
    for attempt in range(6):
        p = subprocess.run(["curl", "-sS", "-m", "90", "--compressed", "-A", "Mozilla/5.0",
                            "--resolve", f"www.prothomalo.com:443:{IP}", url],
                           capture_output=True, text=True)
        try:
            d = json.loads(p.stdout)
            if "items" in d: return d
            err = json.dumps(d)[:200]
        except Exception:
            err = (p.stdout[:150] or p.stderr[:150]).replace("\n", " ")
        log(f"  retry {attempt+1}: {err}")
        time.sleep(5 * (attempt + 1))
    raise RuntimeError("giving up on " + url)

def text_of(cards):
    parts = []
    for c in cards or []:
        for e in c.get("story-elements", []):
            if e.get("type") in ("text", "title") and e.get("text"):
                t = re.sub(r"</(p|h\d|li|blockquote|div)>|<br\s*/?>", "\n", e["text"])
                t = html.unescape(re.sub(r"<[^>]+>", "", t))
                t = re.sub(r"[ \t]+", " ", t)
                t = re.sub(r"\s*\n\s*", "\n", t).strip()
                if t: parts.append(t)
    return "\n\n".join(parts)

def iso(ms):
    return datetime.fromtimestamp(ms / 1000, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ") if ms else None

seen = {}
if os.path.exists(OUT):
    with open(OUT) as f:
        for line in f:
            try: seen[json.loads(line)["id"]] = True
            except Exception: pass
done = set(open(DONE).read().split("\n")) if os.path.exists(DONE) else set()
out = open(OUT, "a")
hits = {}  # id -> set of query labels, written to matched.json at the end
MATCHED = os.path.join(HERE, "matched.json")
if os.path.exists(MATCHED):
    hits = {k: set(v) for k, v in json.load(open(MATCHED)).items()}

def save_hits():
    json.dump({k: sorted(v) for k, v in hits.items()}, open(MATCHED, "w"), ensure_ascii=False)

def window(label, base, a, b):
    key = f"{label}|{a}|{b}"
    if key in done: return
    p = dict(base, **{"published-after": a, "published-before": b, "sort": "latest-published",
                      "limit": 1, "fields": "headline"})
    total = get(p)["total"]
    if total > 10000 and b - a > 86400000:
        mid = (a + b) // 2
        window(label, base, a, mid); window(label, base, mid, b)
    else:
        n_new = 0
        for off in range(0, min(total, 10000), 100):
            d = get(dict(base, **{"published-after": a, "published-before": b, "sort": "latest-published",
                                  "limit": 100, "offset": off, "fields": FIELDS}))
            for it in d["items"]:
                sid = it["id"]
                hits.setdefault(sid, set()).add(label)
                if sid in seen: continue
                seen[sid] = True; n_new += 1
                rec = {"id": sid, "url": it.get("url"), "headline": it.get("headline"),
                       "subheadline": it.get("subheadline"), "summary": it.get("summary"),
                       "published": iso(it.get("first-published-at") or it.get("published-at")),
                       "updated": iso(it.get("published-at")), "author": it.get("author-name"),
                       "template": it.get("story-template"),
                       "sections": [s.get("name") for s in it.get("sections") or []],
                       "tags": [t.get("name") for t in it.get("tags") or []],
                       "text": text_of(it.get("cards"))}
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")
            out.flush(); time.sleep(0.6)
            if not d["items"]: break
        log(f"{label} {iso(a)[:10]}..{iso(b)[:10]} total={total} new={n_new} all={len(seen)}")
    done.add(key)
    with open(DONE, "a") as f: f.write(key + "\n")
    save_hits()

if len(sys.argv) > 1:  # second pass: keywords from a file, one per line
    jobs = [("q:" + k, {"q": k}) for k in open(sys.argv[1]).read().split("\n") if k.strip()]
else:
    jobs = [("tag:" + t, {"tag-name": t}) for t in TAGS] + [("q:" + k, {"q": k}) for k in KEYWORDS]
for label, base in jobs:
    window(label, base, START, END)
save_hits()
log(f"FINISHED stories={len(seen)}")
