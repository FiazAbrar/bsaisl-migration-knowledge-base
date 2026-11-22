"""Build and search the knowledge-base index.

The bot only reads the knowledge base (KB_DIR); it never changes it. Each country's doc.md
(and agencies/doc.md) is split into sections at its headings and stored in a SQLite full-text
index at data/kb.sqlite, together with each cited fact's source (from facts.csv).

Rebuild after every knowledge-base update:
    python -m app.kb_index
"""
import csv
import hashlib
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "kb.sqlite"
MAX_WORDS = 900  # longer sections are split into parts so the AI reads only what it needs

CITE_RE = re.compile(r"\s?\[((?:[A-Z]{1,3}\d{3,5})(?:\s*,\s*[A-Z]{1,3}\d{3,5})*)\]")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
STOPWORDS = set(
    "a an the and or of to in on for with from by at is are was were be been can do does did how what "
    "when where which who whom why will would should could i me my we our you your he she it they them "
    "this that these those there here about into as if not no yes any all".split()
)


# ---------- building ----------

def _kb_dir() -> Path:
    """Where the knowledge base is. Default: the repository this bot folder sits in (its parent).
    KB_DIR in .env overrides it; a relative KB_DIR is taken relative to this bot folder."""
    load_dotenv(ROOT / ".env")
    kb = os.getenv("KB_DIR", "").strip()
    path = Path(kb) if kb else ROOT.parent
    if not path.is_absolute():
        path = (ROOT / path).resolve()
    if not (path / "countries").is_dir():
        sys.exit(f"No knowledge base (countries folder) found at: {path}. Set KB_DIR in .env.")
    return path


def _clean(lines: list[str]) -> tuple[str, list[str], bool]:
    """Turn a section's markdown into plain text for the AI; collect fact ids; mark open questions."""
    out, facts, open_q, in_ntk = [], [], False, False
    for line in lines:
        facts += [f.strip() for m in CITE_RE.finditer(line) for f in m.group(1).split(",")]
        text = CITE_RE.sub("", line).rstrip()
        stripped = text.lstrip("> ").strip()
        if text.startswith(">") and "need to know" in stripped.lower():
            in_ntk, open_q = True, True
            out.append("OPEN QUESTIONS (not confirmed; never state these as facts):")
            continue
        if in_ntk and text.startswith(">"):
            out.append("  " + stripped)
            continue
        in_ntk = False
        out.append(text)
    body = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()
    return body, list(dict.fromkeys(facts)), open_q


def _split(body: str) -> list[str]:
    if len(body.split()) <= MAX_WORDS:
        return [body]
    blocks = []
    for block in body.split("\n\n"):
        # A long list with no blank lines is one block: split it by line instead.
        blocks += block.split("\n") if len(block.split()) > MAX_WORDS else [block]
    parts, cur, count = [], [], 0
    for block in blocks:
        n = len(block.split())
        if cur and count + n > MAX_WORDS:
            parts.append("\n\n".join(cur))
            cur, count = [], 0
        cur.append(block)
        count += n
    if cur:
        parts.append("\n\n".join(cur))
    return parts


def parse_doc(path: Path, slug: str) -> tuple[str, list[dict]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    title, stack, sections, cur = slug, {}, [], {"heading": "Introduction", "level": 1, "lines": []}

    def flush():
        body, facts, open_q = _clean(cur["lines"])
        if not body:
            return
        path_parts = [stack[k] for k in sorted(stack) if k < cur["level"]] + [cur["heading"]]
        for i, part in enumerate(_split(body), 1):
            sections.append({
                "path": " > ".join(path_parts),
                "heading": cur["heading"],
                "level": cur["level"],
                "part": i,
                "text": part,
                "facts": facts,
                "open_q": open_q,
            })

    for line in lines:
        m = HEADING_RE.match(line)
        if not m:
            cur["lines"].append(line)
            continue
        level, heading = len(m.group(1)), CITE_RE.sub("", m.group(2)).strip()
        if level == 1:
            title = heading
            continue
        flush()
        stack = {k: v for k, v in stack.items() if k < level}
        stack[level] = heading
        cur = {"heading": heading, "level": level, "lines": []}
    flush()
    return title, sections


def _load_facts(folder: Path, slug: str) -> list[tuple]:
    facts_csv, sources_csv = folder / "facts.csv", folder / "sources.csv"
    if not facts_csv.exists():
        return []
    publishers = {}
    if sources_csv.exists():
        with open(sources_csv, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                publishers[r.get("url", "")] = r.get("publisher", "")
    rows = []
    with open(facts_csv, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            rows.append((r["id"], slug, r.get("url", ""), publishers.get(r.get("url", ""), ""),
                         r.get("source_type", ""), r.get("status", ""), r.get("page_date", "")))
    return rows


def build(kb: Path | None = None, extra_meta: dict | None = None) -> dict:
    """Index the guides in kb (default: KB_DIR or the repository this bot sits in)."""
    kb = kb or _kb_dir()
    docs = [(p.parent.name, p) for p in sorted((kb / "countries").glob("*/doc.md"))]
    for shared in ("agencies", "cross-country"):  # guides that apply to every country
        if (kb / shared / "doc.md").exists():
            docs.append((shared, kb / shared / "doc.md"))

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = DB_PATH.with_suffix(".building")
    tmp.unlink(missing_ok=True)
    db = sqlite3.connect(tmp)
    db.executescript("""
        CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT);
        CREATE TABLE countries (slug TEXT PRIMARY KEY, title TEXT, doc_sha1 TEXT, doc_modified TEXT);
        CREATE TABLE sections (id INTEGER PRIMARY KEY, slug TEXT, path TEXT, heading TEXT, level INT,
                               part INT, text TEXT, facts TEXT, open_q INT, words INT);
        CREATE VIRTUAL TABLE sections_fts USING fts5(path, text, content='sections', content_rowid='id',
                                                     tokenize='porter unicode61');
        CREATE TABLE facts (id TEXT, slug TEXT, url TEXT, publisher TEXT, source_type TEXT, status TEXT,
                            page_date TEXT, PRIMARY KEY (slug, id));
    """)
    summary = {}
    for slug, path in docs:
        title, sections = parse_doc(path, slug)
        raw = path.read_bytes()
        modified = datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(timespec="seconds")
        db.execute("INSERT INTO countries VALUES (?,?,?,?)",
                   (slug, title, hashlib.sha1(raw).hexdigest(), modified))
        for s in sections:
            db.execute(
                "INSERT INTO sections (slug,path,heading,level,part,text,facts,open_q,words) VALUES (?,?,?,?,?,?,?,?,?)",
                (slug, s["path"], s["heading"], s["level"], s["part"], s["text"], ",".join(s["facts"]),
                 int(s["open_q"]), len(s["text"].split())))
        db.executemany("INSERT OR REPLACE INTO facts VALUES (?,?,?,?,?,?,?)", _load_facts(path.parent, slug))
        summary[slug] = len(sections)
    db.execute("INSERT INTO sections_fts(sections_fts) VALUES ('rebuild')")
    db.executemany("INSERT INTO meta VALUES (?,?)", [
        ("built_at", datetime.now(timezone.utc).isoformat(timespec="seconds")),
        ("kb_dir", str(kb)),
        *(extra_meta or {}).items(),
    ])
    db.commit()
    db.close()
    os.replace(tmp, DB_PATH)  # atomic swap: the running bot never sees a half-built index
    return summary


# ---------- searching (used by the bot) ----------

def _connect() -> sqlite3.Connection:
    if not DB_PATH.exists():
        raise FileNotFoundError("Knowledge-base index missing: run  python -m app.kb_index")
    db = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    db.row_factory = sqlite3.Row
    return db


def list_countries() -> list[dict]:
    with _connect() as db:
        return [dict(r) for r in db.execute("SELECT slug, title FROM countries ORDER BY slug")]


def get_contents(slug: str) -> list[dict]:
    """The headings of one guide, for the AI to pick sections from."""
    with _connect() as db:
        return [dict(r) for r in db.execute(
            "SELECT id, path, part, words, open_q FROM sections WHERE slug=? ORDER BY id", (slug,))]


def get_section(section_id: int) -> dict | None:
    with _connect() as db:
        r = db.execute("SELECT s.*, c.title AS guide FROM sections s JOIN countries c USING(slug) WHERE s.id=?",
                       (section_id,)).fetchone()
        return dict(r) if r else None


def search(query: str, slug: str | None = None, limit: int = 6) -> list[dict]:
    """Full-text search; headings weigh more than body text. Works best with English queries."""
    words = [w for w in re.findall(r"\w+", query.lower()) if len(w) > 1 and w not in STOPWORDS]
    if not words:
        return []
    fts_query = " OR ".join(f'"{w}"' for w in dict.fromkeys(words))
    sql = """SELECT s.id, s.slug, s.path, s.part, s.open_q,
                    snippet(sections_fts, 1, '', '', ' … ', 24) AS snippet,
                    bm25(sections_fts, 4.0, 1.0) AS score
             FROM sections_fts JOIN sections s ON s.id = sections_fts.rowid
             WHERE sections_fts MATCH ?"""
    args: list = [fts_query]
    if slug:
        sql += " AND s.slug = ?"
        args.append(slug)
    sql += " ORDER BY score LIMIT ?"
    args.append(limit)
    with _connect() as db:
        return [dict(r) for r in db.execute(sql, args)]


def sources_for(slug: str, fact_ids: list[str]) -> list[dict]:
    if not fact_ids:
        return []
    with _connect() as db:
        q = f"SELECT * FROM facts WHERE slug=? AND id IN ({','.join('?' * len(fact_ids))})"
        return [dict(r) for r in db.execute(q, [slug, *fact_ids])]


def info() -> dict:
    with _connect() as db:
        meta = dict(db.execute("SELECT key, value FROM meta").fetchall())
        meta["sections"] = db.execute("SELECT COUNT(*) FROM sections").fetchone()[0]
        return meta


if __name__ == "__main__":
    counts = build()
    for slug, n in counts.items():
        print(f"{slug:24} {n:5} sections")
    print(f"Index written to {DB_PATH}  ({sum(counts.values())} sections)")
