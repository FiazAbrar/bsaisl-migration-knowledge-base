"""Sending to and reading from the Telegram Bot API.

Only the channel lives here: the reply itself comes from app/answer.py, like WhatsApp's.
The webhook is registered with a secret derived from the bot token, so the only setting
is TELEGRAM_BOT_TOKEN (plus PUBLIC_DOMAIN for the address).
"""
import hashlib
import html
import logging
import re

import requests

API = "https://api.telegram.org/bot{token}/{method}"
LIMIT = 4096        # Telegram's maximum message length
CHUNK = 3500        # split the text below the limit, leaving room for HTML tags
WEBHOOK_PATH = "/telegram"

# Telegram commands mapped to what the shared reply logic understands.
COMMANDS = {"/reset": "reset", "/delete": "delete my data"}
MENU = [
    {"command": "start", "description": "Welcome and list of countries"},
    {"command": "reset", "description": "Start over"},
    {"command": "delete", "description": "Delete my conversation history"},
]


def call(token: str, method: str, payload: dict | None = None) -> dict | None:
    try:
        r = requests.post(API.format(token=token, method=method), json=payload or {}, timeout=15)
    except requests.RequestException as e:
        # The exception text can contain the URL, and so the token: log the type only.
        logging.error("Telegram %s failed: %s", method, type(e).__name__)
        return None
    data = r.json() if r.headers.get("content-type", "").startswith("application/json") else {}
    if not data.get("ok"):
        logging.error("Telegram %s error %s: %s", method, r.status_code, str(data.get("description"))[:300])
    return data


def webhook_secret(token: str) -> str:
    """Secret Telegram sends back in X-Telegram-Bot-Api-Secret-Token on every update."""
    return hashlib.sha256(f"navigator-telegram-webhook:{token}".encode()).hexdigest()


def webhook_url(domain: str) -> str:
    return f"https://{domain}{WEBHOOK_PATH}"


def register_webhook(token: str, domain: str) -> bool:
    """Point Telegram at this deployment. Skips the call if it already points here."""
    url = webhook_url(domain)
    info = (call(token, "getWebhookInfo") or {}).get("result") or {}
    if info.get("url") == url:
        logging.info("Telegram webhook already set to %s", url)
        return True
    ok = (call(token, "setWebhook", {
        "url": url,
        "secret_token": webhook_secret(token),
        "allowed_updates": ["message"],
    }) or {}).get("ok", False)
    call(token, "setMyCommands", {"commands": MENU})
    logging.info("Telegram webhook %s %s", "set to" if ok else "could NOT be set to", url)
    return bool(ok)


def extract_message(update: dict) -> dict | None:
    """The private-chat message in an update, or None (edits, groups, channels are ignored)."""
    m = update.get("message")
    if not m or (m.get("chat") or {}).get("type") != "private":
        return None
    return {
        "update_id": update.get("update_id"),
        "chat_id": m["chat"]["id"],
        "user_id": (m.get("from") or {}).get("id") or m["chat"]["id"],
        "text": m.get("text") or "",
    }


def to_telegram_html(text: str) -> str:
    """Markdown-style reply (*bold*, **bold**, _italic_, `code`, [link](url), # heading) to Telegram HTML."""
    out = html.escape(text, quote=False)
    out = re.sub(r"^#{1,6}\s+(.+)$", r"<b>\1</b>", out, flags=re.M)
    out = re.sub(r"`([^`\n]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\[([^\]\n]+)\]\((https?://[^)\s]+)\)",
                 lambda m: f'<a href="{m[2].replace(chr(34), "%22")}">{m[1]}</a>', out)
    out = re.sub(r"\*\*(?!\s)([^*\n]+?)(?<!\s)\*\*", r"<b>\1</b>", out)
    out = re.sub(r"(?<![\w*])\*(?!\s)([^*\n]+?)(?<!\s)\*(?![\w*])", r"<b>\1</b>", out)
    out = re.sub(r"(?<![\w_])_(?!\s)([^_\n]+?)(?<!\s)_(?![\w_])", r"<i>\1</i>", out)
    return out.strip()


def split_text(text: str, size: int = CHUNK) -> list[str]:
    """Split at paragraph, then line, then word boundaries, so formatting isn't cut in half."""
    chunks, rest = [], text.strip()
    while len(rest) > size:
        cut = max(rest.rfind("\n\n", 0, size), rest.rfind("\n", 0, size), rest.rfind(" ", 0, size))
        if cut <= 0:
            cut = size
        chunks.append(rest[:cut].strip())
        rest = rest[cut:].strip()
    if rest:
        chunks.append(rest)
    return chunks


def send_text(token: str, chat_id: int, text: str):
    """Send a Markdown-style reply as HTML; falls back to plain text if Telegram rejects the markup."""
    for chunk in split_text(text):
        res = call(token, "sendMessage", {
            "chat_id": chat_id,
            "text": to_telegram_html(chunk)[:LIMIT],
            "parse_mode": "HTML",
            "link_preview_options": {"is_disabled": True},
        })
        if not (res or {}).get("ok"):
            call(token, "sendMessage", {"chat_id": chat_id, "text": chunk[:LIMIT]})


def process_message(config: dict, msg: dict):
    from app import answer, guard, store  # imported here to keep this module free of app state

    token = config["TELEGRAM_BOT_TOKEN"]
    call(token, "sendChatAction", {"chat_id": msg["chat_id"], "action": "typing"})
    text = msg["text"].strip()
    if not text:
        send_text(token, msg["chat_id"], "Please send your question as a text message.")
        return
    command = text.split()[0].split("@")[0].lower() if text.startswith("/") else ""
    if command == "/start":
        send_text(token, msg["chat_id"], answer.welcome())
        return
    text = COMMANDS.get(command, text)
    # Hashed with the same key as WhatsApp ids; the prefix keeps the two channels' ids apart.
    user = store.user_key(f"telegram:{msg['user_id']}", config["META_APP_SECRET"])
    if not answer.is_memory_command(text):  # "reset" and "delete my data" always work
        if len(text) > guard.MAX_CHARS:
            send_text(token, msg["chat_id"], guard.REFUSALS["too_long"])
            return
        d = guard.check("telegram", user)
        if not d.ok:
            if d.notify:  # tell them once; a flood gets no further replies
                send_text(token, msg["chat_id"], guard.refusal_text(d))
            return
    send_text(token, msg["chat_id"], answer.respond(user, text))


if __name__ == "__main__":
    # One-off: python -m app.utils.telegram_utils  (registers the webhook at PUBLIC_DOMAIN)
    import os
    import sys

    from dotenv import load_dotenv

    load_dotenv()
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    tok, dom = (os.getenv("TELEGRAM_BOT_TOKEN") or "").strip(), (os.getenv("PUBLIC_DOMAIN") or "").strip()
    if not tok or not dom:
        sys.exit("Set TELEGRAM_BOT_TOKEN and PUBLIC_DOMAIN in .env first.")
    sys.exit(0 if register_webhook(tok, dom) else 1)
