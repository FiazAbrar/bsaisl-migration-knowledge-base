"""Conversation memory and duplicate checks, in the bot's database (app/db.py: a local SQLite file,
or Postgres when DATABASE_URL is set).

- Users are stored only as a keyed hash of their WhatsApp or Telegram id, never the raw id.
- Conversation turns and remembered countries are deleted after RETENTION_DAYS.
- Message ids are kept 7 days so Meta's retries are never answered twice, even after a restart.
"""
import hashlib
import hmac
import threading
import time

from app import db

DB_PATH = db.SQLITE_PATH  # kept for older imports
RETENTION_DAYS = 30
DEDUPE_DAYS = 7

SCHEMA = [
    'CREATE TABLE IF NOT EXISTS processed (message_id TEXT PRIMARY KEY, ts DOUBLE PRECISION)',
    'CREATE TABLE IF NOT EXISTS turns ("user" TEXT, role TEXT, text TEXT, ts DOUBLE PRECISION)',
    'CREATE INDEX IF NOT EXISTS turns_user ON turns ("user", ts)',
    'CREATE TABLE IF NOT EXISTS users ("user" TEXT PRIMARY KEY, country TEXT, ts DOUBLE PRECISION)',
]

_lock = threading.Lock()
_last_purge = 0.0


def _ready():
    db.ensure("store", SCHEMA)


def user_key(raw_id: str, secret: str) -> str:
    return hmac.new(secret.encode("utf-8"), raw_id.encode("utf-8"), hashlib.sha256).hexdigest()[:32]


def first_time(message_id: str) -> bool:
    """True the first time a message id is seen; False for Meta's repeat deliveries."""
    _ready()
    changed = db.execute("INSERT INTO processed VALUES (?, ?) ON CONFLICT (message_id) DO NOTHING",
                         (message_id, time.time()))
    return changed == 1


def add_turn(user: str, role: str, text: str):
    _ready()
    db.execute('INSERT INTO turns ("user", role, text, ts) VALUES (?,?,?,?)', (user, role, text, time.time()))
    _maybe_purge()


def recent_turns(user: str, n: int = 10) -> list[dict]:
    _ready()
    rows = db.all('SELECT role, text FROM turns WHERE "user"=? ORDER BY ts DESC LIMIT ?', (user, n))
    return [{"role": r, "text": t} for r, t in reversed(rows)]


def set_country(user: str, slug: str):
    _ready()
    db.execute('INSERT INTO users ("user", country, ts) VALUES (?,?,?) '
               'ON CONFLICT ("user") DO UPDATE SET country = excluded.country, ts = excluded.ts',
               (user, slug, time.time()))


def get_country(user: str) -> str | None:
    _ready()
    row = db.one('SELECT country FROM users WHERE "user"=?', (user,))
    return row[0] if row else None


def forget(user: str):
    """Delete everything stored about one user (for 'delete my data' requests)."""
    _ready()
    db.execute('DELETE FROM turns WHERE "user"=?', (user,))
    db.execute('DELETE FROM users WHERE "user"=?', (user,))


def _maybe_purge():
    global _last_purge
    with _lock:
        if time.time() - _last_purge < 3600:
            return
        _last_purge = time.time()
    now = time.time()
    db.execute("DELETE FROM turns WHERE ts < ?", (now - RETENTION_DAYS * 86400,))
    db.execute("DELETE FROM users WHERE ts < ?", (now - RETENTION_DAYS * 86400,))
    db.execute("DELETE FROM processed WHERE ts < ?", (now - DEDUPE_DAYS * 86400,))
