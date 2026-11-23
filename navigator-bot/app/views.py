import logging
import threading

from flask import Blueprint, current_app, jsonify, request

from . import db, kb_index, kb_sync, store
from .decorators.security import signature_required
from .utils.whatsapp_utils import app_config, extract_messages, process_message

webhook_blueprint = Blueprint("webhook", __name__)


def _process_in_background(config: dict, msg: dict):
    try:
        process_message(config, msg)
    except Exception:
        logging.exception("Failed to process message %s", msg.get("id"))


@webhook_blueprint.route("/webhook", methods=["GET"])
def webhook_get():
    """Meta's one-time check when you click Verify and save."""
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge", "")
    if mode == "subscribe" and token == current_app.config["WHATSAPP_VERIFY_TOKEN"]:
        logging.info("WEBHOOK_VERIFIED")
        return challenge, 200
    logging.warning("Webhook verification failed")
    return jsonify({"status": "error", "message": "Verification failed"}), 403


@webhook_blueprint.route("/webhook", methods=["POST"])
@signature_required
def webhook_post():
    body = request.get_json(silent=True) or {}
    config = app_config()
    for msg in extract_messages(body):
        # Meta retries deliveries; the store remembers ids so each message is answered once.
        if msg["id"] and store.first_time(msg["id"]):
            logging.info("Message %s received (%s)", msg["id"], msg["type"])
            threading.Thread(target=_process_in_background, args=(config, msg), daemon=True).start()
    # Answer Meta at once; replies are sent from the background thread.
    return jsonify({"status": "ok"}), 200


@webhook_blueprint.route("/health", methods=["GET"])
def health():
    try:
        kb = kb_index.info()
    except FileNotFoundError as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    return jsonify({"status": "ok", "kb_built_at": kb["built_at"], "kb_sections": kb["sections"],
                    "kb_guides": kb["guides"], "kb_commit": kb.get("kb_commit", "local"),
                    "kb_warnings": kb["warnings"], "kb_sync": kb_sync.status,
                    "database": db.kind()}), 200
