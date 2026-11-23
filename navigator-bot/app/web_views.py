"""Web chat: the page at / and its small JSON API. Same answers, memory and limits as WhatsApp and Telegram.

No login. A visitor first gets a signed session cookie (POST /api/session), after a bot check
(Cloudflare Turnstile) whenever TURNSTILE_SECRET_KEY is set. Every message then needs that cookie
and passes app.guard before anything is answered. Turn the page off with WEB_CHAT=off.

  GET  /              the chat page (app/static/web/)
  GET  /api/config    what the page needs to start: bot-check site key, longest message
  POST /api/session   {"turnstile_token": "..."} -> sets the nav_sid cookie
  POST /api/chat      {"message": "..."} -> {"reply": "..."}
"""
import hashlib
import hmac
import ipaddress
import logging
import re
import secrets
import threading
import time
from pathlib import Path
from urllib.parse import urlsplit

import requests
from flask import Blueprint, abort, current_app, jsonify, request, send_from_directory

from . import answer, guard, kb_index, store
from .countries import DISPLAY

web_blueprint = Blueprint("web", __name__)

PAGE_DIR = Path(__file__).resolve().parent / "static" / "web"
COOKIE = "nav_sid"
SESSION_SECONDS = 24 * 3600
MAX_BODY = 4096  # bytes; a 500-character Bangla message is about 1,500
CONTROL_RE = re.compile(r"[\x00-\x08\x0b-\x1f\x7f]")
MAX_WEB_IN_FLIGHT = 4  # web answers worked on at once, so web traffic can't hold every thread WhatsApp needs
_in_flight = threading.BoundedSemaphore(MAX_WEB_IN_FLIGHT)
# Proxies whose PROXY_IP_HEADER is believed: this machine and private networks (where a cloud host's own
# load balancer sits). Anyone connecting straight to the server can't pick their own address.
DEFAULT_TRUSTED = "127.0.0.0/8,::1/128,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16,fc00::/7"
TURNSTILE_VERIFY = "https://challenges.cloudflare.com/turnstile/v0/siteverify"
CSP = "; ".join([
    "default-src 'self'",
    "script-src 'self' https://challenges.cloudflare.com",
    "frame-src https://challenges.cloudflare.com",
    "connect-src 'self'",
    "style-src 'self'",
    "img-src 'self' data:",
    "object-src 'none'",
    "base-uri 'none'",
    "form-action 'none'",
    "frame-ancestors 'none'",
])


def _enabled() -> bool:
    return current_app.config.get("WEB_CHAT", "").lower() not in {"off", "false", "0", "no"}


def _secret() -> bytes:
    """Key for signing session cookies: WEB_SESSION_SECRET, or the Meta app secret if that isn't set."""
    return (current_app.config.get("WEB_SESSION_SECRET") or current_app.config["META_APP_SECRET"]).encode("utf-8")


def _sign(sid: str, ts: str) -> str:
    key = hmac.new(_secret(), b"navigator-web-session", hashlib.sha256).digest()
    return hmac.new(key, f"{sid}.{ts}".encode("ascii"), hashlib.sha256).hexdigest()


def _new_cookie() -> str:
    sid, ts = secrets.token_urlsafe(18), str(int(time.time()))
    return f"{sid}.{ts}.{_sign(sid, ts)}"


def _session_id() -> str | None:
    """The visitor's session id, if their cookie is ours and less than a day old."""
    parts = request.cookies.get(COOKIE, "").split(".")
    if len(parts) != 3 or not all(p.isascii() for p in parts) or not parts[1].isdigit():
        return None
    sid, ts, sig = parts
    if not hmac.compare_digest(sig, _sign(sid, ts)):
        return None
    return sid if 0 <= time.time() - int(ts) < SESSION_SECONDS else None


def _trusted(addr: str) -> bool:
    nets = current_app.config.get("TRUSTED_PROXIES", "") or DEFAULT_TRUSTED
    try:
        ip = ipaddress.ip_address(addr)
        return any(ip in ipaddress.ip_network(n.strip(), strict=False) for n in nets.split(",") if n.strip())
    except ValueError:
        return False


def _client_ip() -> str:
    """The visitor's address. Behind a proxy (ngrok, Cloudflare, a cloud host), set PROXY_IP_HEADER,
    or every visitor looks like the proxy and shares one IP limit. The header is believed only when the
    connection comes from a trusted proxy (TRUSTED_PROXIES), so nobody can choose their own address."""
    peer = request.remote_addr or ""
    header = current_app.config.get("PROXY_IP_HEADER", "")
    if not header or not _trusted(peer):
        return peer
    value = request.headers.get(header, "")
    if header.lower() == "x-forwarded-for":
        value = value.split(",")[-1]  # the entry added by our own proxy; earlier ones can be forged
    return value.strip() or peer


def _ip_key() -> str:
    """Hashed address for the limits. IPv6 counts by its /64 block: one machine usually holds a whole
    block and could otherwise use a new address for every request."""
    ip = _client_ip()
    try:
        addr = ipaddress.ip_address(ip)
        if addr.version == 6:
            ip = str(ipaddress.ip_network(f"{addr}/64", strict=False))
    except ValueError:
        pass
    return store.user_key(f"ip:{ip}", current_app.config["META_APP_SECRET"])


def _https() -> bool:
    return request.is_secure or request.headers.get("X-Forwarded-Proto", "").split(",")[0].strip() == "https"


def _same_site() -> bool:
    """Refuse requests sent by another website's page (cross-site request forgery)."""
    if request.headers.get("Sec-Fetch-Site", "") == "cross-site":
        return False
    origin = request.headers.get("Origin")
    if not origin:
        return True  # not sent by a browser page; the cookie and the bot check still apply
    allowed = {h for h in (request.host, current_app.config.get("PUBLIC_DOMAIN", "")) if h}
    return urlsplit(origin).netloc in allowed


def _json_body() -> tuple[dict | None, tuple | None]:
    if request.content_length is None or request.content_length > MAX_BODY:
        return None, (jsonify(error="too_large"), 413)
    data = request.get_json(silent=True) if request.is_json else None
    if not isinstance(data, dict):
        return None, (jsonify(error="bad_request"), 400)
    return data, None


def _guard_preflight():
    if not _enabled():
        abort(404)
    if not _same_site():
        return jsonify(error="forbidden"), 403
    return None


def _turnstile_ok(secret: str, token: str) -> bool:
    try:
        res = requests.post(TURNSTILE_VERIFY, data={"secret": secret, "response": token,
                                                    "remoteip": _client_ip()}, timeout=8)
        data = res.json()
        domain = current_app.config.get("PUBLIC_DOMAIN", "")
        return data.get("success") is True and (not domain or data.get("hostname") == domain)
    except Exception:
        logging.exception("Turnstile check failed")
        return False


@web_blueprint.route("/", methods=["GET"])
def index():
    if not _enabled():
        abort(404)
    resp = send_from_directory(PAGE_DIR, "index.html")
    resp.headers["Cache-Control"] = "no-cache"
    return resp


@web_blueprint.route("/api/config", methods=["GET"])
def config():
    if not _enabled():
        abort(404)
    try:
        have = {c["slug"] for c in kb_index.list_countries()}
        updated = kb_index.info().get("guides_updated") or kb_index.info().get("built_at", "")[:10]
    except FileNotFoundError:
        have, updated = set(), ""
    countries = [{"slug": s, "en": en, "bn": bn} for s, en, bn in DISPLAY if s in have]
    return jsonify(turnstile_site_key=current_app.config.get("TURNSTILE_SITE_KEY", ""), max_chars=guard.MAX_CHARS,
                   countries=countries, guides_updated=updated)


@web_blueprint.route("/api/session", methods=["POST"])
def new_session():
    refused = _guard_preflight()
    if refused:
        return refused
    body, error = _json_body()
    if error:
        return error
    secret = current_app.config.get("TURNSTILE_SECRET_KEY", "")
    token = body.get("turnstile_token")
    # A request without a usable token is refused before it counts, so nobody can use up a shared
    # network's session allowance with empty requests.
    if secret and (not isinstance(token, str) or not token or len(token) > 2048):
        return jsonify(error="bot_check"), 403
    d = guard.new_session(_ip_key())
    if not d.ok:
        return jsonify(error="rate_limited", scope=d.reason, retry_after=d.retry_after), 429
    if secret and not _turnstile_ok(secret, token):
        return jsonify(error="bot_check"), 403
    resp = jsonify(ok=True)
    resp.set_cookie(COOKIE, _new_cookie(), max_age=SESSION_SECONDS, httponly=True, secure=_https(),
                    samesite="Strict", path="/")
    return resp


@web_blueprint.route("/api/chat", methods=["POST"])
def chat():
    refused = _guard_preflight()
    if refused:
        return refused
    body, error = _json_body()
    if error:
        return error
    sid = _session_id()
    if not sid:
        return jsonify(error="no_session"), 401
    message = body.get("message")
    if not isinstance(message, str):
        return jsonify(error="empty"), 400
    text = CONTROL_RE.sub("", message.replace("\r\n", "\n").replace("\r", "\n")).strip()
    if not text:
        return jsonify(error="empty"), 400
    if len(text) > guard.MAX_CHARS:
        return jsonify(error="too_long", max_chars=guard.MAX_CHARS), 400

    user = store.user_key(f"web:{sid}", current_app.config["META_APP_SECRET"])
    if answer.is_memory_command(text):  # "reset" and "delete my data": a loose limit, never the daily one
        d = guard.command("web", user)
    else:
        d = guard.check("web", user, _ip_key())
    if not d.ok:
        status = 503 if d.reason in {"budget", "busy"} else 429
        return jsonify(error="busy" if status == 503 else "rate_limited",
                       scope=d.reason, retry_after=d.retry_after), status
    if not _in_flight.acquire(blocking=False):
        return jsonify(error="busy", scope="busy", retry_after=5), 503
    try:
        reply = answer.respond(user, text)
    except Exception:
        logging.exception("Web chat answer failed")
        return jsonify(error="server"), 500
    finally:
        _in_flight.release()
    return jsonify(reply=reply, country=store.get_country(user))


@web_blueprint.after_app_request
def security_headers(resp):
    resp.headers.setdefault("X-Content-Type-Options", "nosniff")
    resp.headers.setdefault("Referrer-Policy", "no-referrer")
    resp.headers.setdefault("X-Frame-Options", "DENY")
    resp.headers.setdefault("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
    if _https():
        resp.headers.setdefault("Strict-Transport-Security", "max-age=31536000")
    if resp.mimetype == "text/html":
        resp.headers["Content-Security-Policy"] = CSP
    if request.path.startswith("/api/"):
        resp.headers["Cache-Control"] = "no-store"
    return resp
