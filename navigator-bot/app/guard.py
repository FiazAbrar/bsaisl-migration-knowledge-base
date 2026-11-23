"""Abuse limits and daily spending caps, shared by every channel (web, WhatsApp, Telegram).

Every message goes through check() before any answer is worked out, so a flood of messages
costs almost nothing. Counters live in data/state.sqlite, next to the conversation memory,
and survive restarts. Days run on Bangladesh time (midnight to midnight, UTC+6).

Limits (override any of them with the environment variable in brackets). The defaults are LENIENT,
set for the testing phase; tighten them in .env before a public launch (suggested public values in
brackets after each default).
- Per user, by channel. WhatsApp and Telegram users are real phone numbers, so they get more room
  than an anonymous web session:
  web       20 a minute [GUARD_WEB_PER_MINUTE], 200 a day [GUARD_WEB_PER_DAY]             (public: 6 / 40)
  whatsapp  30 a minute [GUARD_WHATSAPP_PER_MINUTE], 500 a day [GUARD_WHATSAPP_PER_DAY]   (public: 20 / 150)
  telegram  30 a minute [GUARD_TELEGRAM_PER_MINUTE], 500 a day [GUARD_TELEGRAM_PER_DAY]   (public: 15 / 100)
- Web only, per IP address: 1,000 messages a day [GUARD_IP_PER_DAY] (public: 200) and 60 new chat
  sessions an hour [GUARD_SESSIONS_PER_HOUR] (public: 20). Loose even then: Bangladeshi mobile
  operators put many customers behind one shared IP address.
- Web only, all visitors together: 200 messages a minute [GUARD_WEB_ALL_PER_MINUTE] (public: 60),
  so even many sessions can't spend the day's budget in minutes.
- "reset" and "delete my data": 30 a minute per user [GUARD_COMMANDS_PER_MINUTE]. They never count
  toward the daily limit, so people can always delete their data.
- AI spending per channel per day, in US dollars: BUDGET_WEB_USD (3), BUDGET_WHATSAPP_USD (10),
  BUDGET_TELEGRAM_USD (3). When one channel's budget is spent, only that channel pauses, so an
  attack on the open web page can't stop WhatsApp. add_cost() records spending once the AI step
  is connected; until then nothing is spent and the budgets never trip.

Callers pass users and IP addresses already hashed (store.user_key); nothing raw is stored here.
"""
import logging
import os
import sqlite3
import threading
import time
from contextlib import closing
from dataclasses import dataclass

from app.store import DB_PATH

BD_OFFSET = 6 * 3600  # Bangladesh is UTC+6: days reset at midnight in Dhaka
MINUTE, HOUR, DAY = 60, 3600, 86400
MAX_CHARS = 500  # longest message accepted on any channel

DEFAULTS = {
    # Testing-phase values (lenient); see the docstring for suggested public values.
    "GUARD_WEB_PER_MINUTE": 20,
    "GUARD_WEB_PER_DAY": 200,
    "GUARD_WHATSAPP_PER_MINUTE": 30,
    "GUARD_WHATSAPP_PER_DAY": 500,
    "GUARD_TELEGRAM_PER_MINUTE": 30,
    "GUARD_TELEGRAM_PER_DAY": 500,
    "GUARD_IP_PER_DAY": 1000,
    "GUARD_SESSIONS_PER_HOUR": 60,
    "GUARD_WEB_ALL_PER_MINUTE": 200,
    "GUARD_COMMANDS_PER_MINUTE": 30,
    "BUDGET_WEB_USD": 3,
    "BUDGET_WHATSAPP_USD": 10,
    "BUDGET_TELEGRAM_USD": 3,
}

HELP = "For urgent help, call 16135 (free from Bangladesh) or +880 9610102030 from abroad."
REFUSALS = {
    "minute": "You're sending messages very fast. Please wait a minute, then ask again.",
    "day": f"You've reached today's limit of questions. Please come back tomorrow. {HELP}",
    "ip": f"Too many questions are coming from your network today. Please try again tomorrow. {HELP}",
    "budget": f"The Navigator is very busy today. Please try again tomorrow. {HELP}",
    "busy": f"The Navigator is very busy right now. Please try again in a minute. {HELP}",
    "too_long": f"Please send a shorter question, under {MAX_CHARS} characters.",
}

_lock = threading.Lock()
_last_purge = 0.0


@dataclass
class Decision:
    ok: bool
    reason: str = ""      # minute, day, ip, sessions, busy or budget
    retry_after: int = 0  # seconds until the limit resets
    notify: bool = True   # False after the first refusal in a window, so a flood gets no replies


def limit(name: str) -> float:
    """A limit from the environment, or its default. Read on every call, so .env changes need no code."""
    try:
        return float(os.getenv(name) or DEFAULTS[name])
    except ValueError:
        return float(DEFAULTS[name])


def refusal_text(d: Decision) -> str:
    return REFUSALS.get(d.reason, REFUSALS["minute"])


def _db() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(DB_PATH, timeout=10)
    db.executescript("""
        CREATE TABLE IF NOT EXISTS guard_counts (key TEXT PRIMARY KEY, n INTEGER, expires REAL);
        CREATE TABLE IF NOT EXISTS guard_spend (channel TEXT, day INTEGER, usd REAL, PRIMARY KEY (channel, day));
    """)
    return db


def _bucket(window: int, now: float) -> int:
    return int((now + BD_OFFSET) // window)


def _bucket_end(window: int, now: float) -> float:
    return (_bucket(window, now) + 1) * window - BD_OFFSET


def _count(db, key: str, expires: float) -> int:
    db.execute("INSERT INTO guard_counts VALUES (?, 1, ?) ON CONFLICT(key) DO UPDATE SET n = n + 1",
               (key, expires))
    return db.execute("SELECT n FROM guard_counts WHERE key = ?", (key,)).fetchone()[0]


def _refuse(db, reason: str, key: str, window: int, now: float) -> Decision:
    end = _bucket_end(window, now)
    first = _count(db, f"refused:{key}", end + 60) == 1
    return Decision(False, reason, max(1, int(end - now)), first)


def _apply(rules: list[tuple[str, int, float, str]], now: float, channel: str = "") -> Decision:
    """rules: (key, window in seconds, limit, reason). Refuses at the first rule already at its limit;
    otherwise counts the message against every rule."""
    with _lock, closing(_db()) as db, db:
        if channel and _spent(db, channel, now) >= limit(f"BUDGET_{channel.upper()}_USD"):
            return _refuse(db, "budget", f"budget:{channel}:{rules[0][0]}", DAY, now)
        keys = [(f"{key}:{window}:{_bucket(window, now)}", window, lim, reason) for key, window, lim, reason in rules]
        for k, window, lim, reason in keys:
            row = db.execute("SELECT n FROM guard_counts WHERE key = ?", (k,)).fetchone()
            if row and row[0] >= lim:
                return _refuse(db, reason, k, window, now)
        for k, window, _, _ in keys:
            _count(db, k, _bucket_end(window, now) + 60)
    _maybe_purge(now)
    return Decision(True)


def check(channel: str, user: str, ip: str = "") -> Decision:
    """Call before answering one message. channel: web, whatsapp or telegram; user and ip are hashes."""
    now = time.time()
    rules = [
        (f"{channel}:u:{user}", MINUTE, limit(f"GUARD_{channel.upper()}_PER_MINUTE"), "minute"),
        (f"{channel}:u:{user}", DAY, limit(f"GUARD_{channel.upper()}_PER_DAY"), "day"),
    ]
    if ip:
        rules.append((f"{channel}:ip:{ip}", DAY, limit("GUARD_IP_PER_DAY"), "ip"))
    if channel == "web":
        rules.append(("web:all", MINUTE, limit("GUARD_WEB_ALL_PER_MINUTE"), "busy"))
    return _apply(rules, now, channel)


def command(channel: str, user: str) -> Decision:
    """Call before "reset" or "delete my data": a loose per-minute limit that never blocks them for the day."""
    return _apply([(f"{channel}:cmd:{user}", MINUTE, limit("GUARD_COMMANDS_PER_MINUTE"), "minute")], time.time())


def new_session(ip: str) -> Decision:
    """Call before giving a web visitor a new chat session. ip is a hash."""
    return _apply([(f"sessions:ip:{ip}", HOUR, limit("GUARD_SESSIONS_PER_HOUR"), "sessions")], time.time())


def _spent(db, channel: str, now: float) -> float:
    row = db.execute("SELECT usd FROM guard_spend WHERE channel = ? AND day = ?",
                     (channel, _bucket(DAY, now))).fetchone()
    return row[0] if row else 0.0


def add_cost(channel: str, usd: float):
    """Record what one AI reply cost (the AI service reports it with each reply). Must be called for every
    AI reply once the AI step is connected: without it the budgets never trip."""
    if usd <= 0:
        return
    now = time.time()
    with _lock, closing(_db()) as db, db:
        before = _spent(db, channel, now)
        db.execute("INSERT INTO guard_spend VALUES (?, ?, ?) ON CONFLICT(channel, day) DO UPDATE SET usd = usd + ?",
                   (channel, _bucket(DAY, now), usd, usd))
    budget = limit(f"BUDGET_{channel.upper()}_USD")
    if before < 0.8 * budget <= before + usd:
        logging.warning("%s has used 80%% of today's AI budget ($%.2f of $%.2f)", channel, before + usd, budget)


def status() -> dict:
    """Today's spending against each channel's budget. Kept off the public /health page so an attacker
    can't watch a budget drain; on the server run `python -m app.guard` to see it."""
    now = time.time()
    with _lock, closing(_db()) as db:
        return {ch: {"spent_usd": round(_spent(db, ch, now), 4), "budget_usd": limit(f"BUDGET_{ch.upper()}_USD")}
                for ch in ("web", "whatsapp", "telegram")}


def _maybe_purge(now: float):
    global _last_purge
    if now - _last_purge < HOUR:
        return
    _last_purge = now
    with _lock, closing(_db()) as db, db:
        db.execute("DELETE FROM guard_counts WHERE expires < ?", (now,))
        db.execute("DELETE FROM guard_spend WHERE day < ?", (_bucket(DAY, now) - 60,))


if __name__ == "__main__":
    import json

    from dotenv import load_dotenv

    load_dotenv()
    print(json.dumps(status(), indent=2))
