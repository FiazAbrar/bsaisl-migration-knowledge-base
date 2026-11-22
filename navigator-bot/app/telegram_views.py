"""Telegram webhook (/telegram). Served by the same app as WhatsApp's /webhook."""
import hmac
import logging
import threading

from flask import Blueprint, current_app, jsonify, request

from . import store
from .utils.telegram_utils import WEBHOOK_PATH, extract_message, process_message, webhook_secret

telegram_blueprint = Blueprint("telegram", __name__)


def _process_in_background(config: dict, msg: dict):
    try:
        process_message(config, msg)
    except Exception:
        logging.exception("Failed to process Telegram update %s", msg.get("update_id"))


@telegram_blueprint.route(WEBHOOK_PATH, methods=["POST"])
def telegram_post():
    token = current_app.config["TELEGRAM_BOT_TOKEN"]
    if not token:
        return jsonify({"status": "error", "message": "Telegram is not configured"}), 404
    sent = request.headers.get("X-Telegram-Bot-Api-Secret-Token", "")
    if not hmac.compare_digest(sent, webhook_secret(token)):
        logging.warning("Telegram secret check failed")
        return jsonify({"status": "error", "message": "Invalid secret"}), 403
    msg = extract_message(request.get_json(silent=True) or {})
    # Telegram retries until it gets a 200; the store remembers update ids so each is answered once.
    if msg and msg["update_id"] is not None and store.first_time(f"tg:{msg['update_id']}"):
        logging.info("Telegram update %s received", msg["update_id"])
        config = dict(current_app.config)
        threading.Thread(target=_process_in_background, args=(config, msg), daemon=True).start()
    return jsonify({"status": "ok"}), 200
