"""The bot's small read-write database: conversation memory, duplicate checks and abuse counters.

- On a PC (or a server with a disk): a SQLite file, data/state.sqlite. Nothing to set up.
- On a host whose disk is wiped at every restart (Render's free plan): Postgres, when DATABASE_URL
  is set, e.g. a free Neon database. Then memory and limits survive restarts and redeploys.

Callers write SQL once, with ? placeholders, and SQL both databases accept (no INSERT OR REPLACE:
use ON CONFLICT ... DO UPDATE / DO NOTHING; quote the column "user", a reserved word in Postgres;
use DOUBLE PRECISION for timestamps). The knowledge-base index (data/kb.sqlite) is separate: it is
rebuilt from the guides at every start, so it never needs Postgres.
"""
import logging
import os
import sqlite3
import threading
from pathlib import Path

SQLITE_PATH = Path(__file__).resolve().parent.parent / "data" / "state.sqlite"

_lock = threading.RLock()  # one statement at a time: plenty for this bot, and safe for both databases
_conn = None
_is_pg = False
_schemas: set[str] = set()


def _url() -> str:
    return (os.getenv("DATABASE_URL") or "").strip()


def using_postgres() -> bool:
    return bool(_url())


def _connect():
    global _conn, _is_pg
    url = _url()
    if url:
        import psycopg  # only needed on servers that use Postgres

        _conn = psycopg.connect(url, autocommit=True, connect_timeout=15)
        _is_pg = True
    else:
        SQLITE_PATH.parent.mkdir(parents=True, exist_ok=True)
        _conn = sqlite3.connect(SQLITE_PATH, timeout=10, check_same_thread=False, isolation_level=None)
        _is_pg = False
    _schemas.clear()  # a new connection re-checks the tables (cheap: CREATE TABLE IF NOT EXISTS)
    return _conn


def _sql(sql: str) -> str:
    return sql.replace("?", "%s") if _is_pg else sql


def _run(sql: str, params: tuple, fetch: str):
    """Run one statement; on a dropped connection (Neon closes idle ones), reconnect once and retry."""
    with _lock:
        for attempt in (1, 2):
            conn = _conn or _connect()
            try:
                cur = conn.execute(_sql(sql), params)
                if fetch == "one":
                    return cur.fetchone()
                if fetch == "all":
                    return cur.fetchall()
                return cur.rowcount
            except Exception as e:
                if attempt == 2 or not _is_pg or not _is_connection_error(e):
                    raise
                logging.warning("Database connection lost (%s); reconnecting", type(e).__name__)
                _close()


def _is_connection_error(e: Exception) -> bool:
    import psycopg

    return isinstance(e, (psycopg.OperationalError, psycopg.InterfaceError))


def _close():
    global _conn
    try:
        if _conn is not None:
            _conn.close()
    except Exception:
        pass
    _conn = None


def ensure(name: str, statements: list[str]):
    """Create a module's tables once per connection. statements: CREATE ... IF NOT EXISTS, one each."""
    with _lock:
        if _conn is None:
            _connect()
        if name in _schemas:
            return
        for stmt in statements:
            _run(stmt, (), "none")
        _schemas.add(name)


def execute(sql: str, params: tuple = ()) -> int:
    """Run a write; returns the number of rows changed."""
    return _run(sql, params, "none")


def one(sql: str, params: tuple = ()):
    return _run(sql, params, "one")


def all(sql: str, params: tuple = ()) -> list:
    return _run(sql, params, "all")


def kind() -> str:
    """'postgres' or 'sqlite', for /health."""
    return "postgres" if using_postgres() else "sqlite"
