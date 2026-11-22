"""Small local database (data/state.sqlite) for conversation memory and duplicate checks.

- Users are stored only as a keyed hash of their WhatsApp or Telegram id, never the raw id.
- Conversation turns and remembered countries are deleted after RETENTION_DAYS.
- Message ids are kept 7 days so Meta's retries are never answered twice, even after a restart.
"""
import hashlib
import hmac
import sqlite3
import threading
import time
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "state.sqlite"
RETENTION_DAYS = 30
DEDUPE_DAYS = 7

_lock = threading.Lock()
_last_purge = 0.0


def _db() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(DB_PATH, timeout=10)
    db.executescript("""
        CREATE TABLE IF NOT EXISTS processed (message_id TEXT PRIMARY KEY, ts REAL);
        CREATE TABLE IF NOT EXISTS turns (user TEXT, role TEXT, text TEXT, ts REAL);
        CREATE INDEX IF NOT EXISTS turns_user ON turns(user, ts);
        CREATE TABLE IF NOT EXISTS users (user TEXT PRIMARY KEY, country TEXT, ts REAL);
    """)
    return db


def user_key(raw_id: str, secret: str) -> str:
    return hmac.new(secret.encode("utf-8"), raw_id.encode("utf-8"), hashlib.sha256).hexdigest()[:32]


def first_time(message_id: str) -> bool:
    """True the first time a message id is seen; False for Meta's repeat deliveries."""
    with _lock, _db() as db:
        try:
            db.execute("INSERT INTO processed VALUES (?, ?)", (message_id, time.time()))
            return True
        except sqlite3.IntegrityError:
            return False


def add_turn(user: str, role: str, text: str):
    with _lock, _db() as db:
        db.execute("INSERT INTO turns VALUES (?,?,?,?)", (user, role, text, time.time()))
    _maybe_purge()


def recent_turns(user: str, n: int = 10) -> list[dict]:
    with _lock, _db() as db:
        rows = db.execute("SELECT role, text FROM turns WHERE user=? ORDER BY ts DESC LIMIT ?", (user, n)).fetchall()
    return [{"role": r, "text": t} for r, t in reversed(rows)]


def set_country(user: str, slug: str):
    with _lock, _db() as db:
        db.execute("INSERT OR REPLACE INTO users VALUES (?,?,?)", (user, slug, time.time()))


def get_country(user: str) -> str | None:
    with _lock, _db() as db:
        row = db.execute("SELECT country FROM users WHERE user=?", (user,)).fetchone()
    return row[0] if row else None


def forget(user: str):
    """Delete everything stored about one user (for 'delete my data' requests)."""
    with _lock, _db() as db:
        db.execute("DELETE FROM turns WHERE user=?", (user,))
        db.execute("DELETE FROM users WHERE user=?", (user,))


def _maybe_purge():
    global _last_purge
    if time.time() - _last_purge < 3600:
        return
    _last_purge = time.time()
    now = time.time()
    with _lock, _db() as db:
        db.execute("DELETE FROM turns WHERE ts < ?", (now - RETENTION_DAYS * 86400,))
        db.execute("DELETE FROM users WHERE ts < ?", (now - RETENTION_DAYS * 86400,))
        db.execute("DELETE FROM processed WHERE ts < ?", (now - DEDUPE_DAYS * 86400,))
