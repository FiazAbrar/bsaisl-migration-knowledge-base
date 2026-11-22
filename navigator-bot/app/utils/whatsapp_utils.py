"""Sending to and reading from the WhatsApp Cloud API."""
import logging
import re

import requests
from flask import current_app


def _messages_url(config) -> str:
    return (
        f"https://graph.facebook.com/{config['GRAPH_API_VERSION']}/"
        f"{config['WHATSAPP_PHONE_NUMBER_ID']}/messages"
    )


def _post(config, payload: dict):
    headers = {"Authorization": f"Bearer {config['WHATSAPP_ACCESS_TOKEN']}"}
    try:
        r = requests.post(_messages_url(config), json=payload, headers=headers, timeout=15)
    except requests.RequestException as e:
        logging.error("WhatsApp API request failed: %s", e)
        return None
    if r.status_code >= 400:
        logging.error("WhatsApp API error %s: %s", r.status_code, r.text[:500])
    return r


def extract_messages(body: dict) -> list[dict]:
    """Return the incoming user messages in a webhook body (ignores status updates)."""
    out = []
    for entry in body.get("entry", []):
        for change in entry.get("changes", []):
            value = change.get("value", {})
            contacts = {c.get("user_id") or c.get("wa_id"): c for c in value.get("contacts", [])}
            for m in value.get("messages", []):
                sender_key = m.get("from_user_id") or m.get("from")
                contact = contacts.get(sender_key, {})
                out.append({
                    "id": m.get("id"),
                    "type": m.get("type"),
                    "text": (m.get("text") or {}).get("body", ""),
                    # Phone number may be missing for users with a WhatsApp username;
                    # the business-scoped user id is then the only address.
                    "phone": m.get("from"),
                    "user_id": m.get("from_user_id") or contact.get("user_id"),
                    "name": (contact.get("profile") or {}).get("name", ""),
                })
    return out


def mark_read_and_typing(config, message_id: str):
    _post(config, {
        "messaging_product": "whatsapp",
        "status": "read",
        "message_id": message_id,
        "typing_indicator": {"type": "text"},
    })


def to_whatsapp_format(text: str) -> str:
    """Markdown bold (**x**) becomes WhatsApp bold (*x*)."""
    return re.sub(r"\*\*(.*?)\*\*", r"*\1*", text).strip()


def send_text(config, msg: dict, text: str):
    """Reply to the sender. Splits text over WhatsApp's 4096-character limit."""
    address = {"to": msg["phone"]} if msg.get("phone") else {"recipient": msg["user_id"]}
    for start in range(0, len(text), 4000):
        _post(config, {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            **address,
            "type": "text",
            "text": {"preview_url": False, "body": text[start:start + 4000]},
        })


def process_message(config, msg: dict):
    from app import answer, store  # imported here to keep this module free of app state

    mark_read_and_typing(config, msg["id"])
    if msg["type"] != "text":
        send_text(config, msg, "Please send your question as a text message.")
        return
    user = store.user_key(msg.get("user_id") or msg.get("phone") or "", config["META_APP_SECRET"])
    send_text(config, msg, to_whatsapp_format(answer.respond(user, msg["text"])))


def app_config() -> dict:
    return dict(current_app.config)
