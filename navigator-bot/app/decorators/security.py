import hashlib
import hmac
import logging
from functools import wraps

from flask import current_app, jsonify, request


def validate_signature(payload: bytes, signature: str) -> bool:
    """Meta signs each webhook body with the app secret (X-Hub-Signature-256)."""
    expected = hmac.new(
        current_app.config["META_APP_SECRET"].encode("utf-8"),
        msg=payload,
        digestmod=hashlib.sha256,
    ).hexdigest()
    return hmac.compare_digest(expected, signature)


def signature_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        header = request.headers.get("X-Hub-Signature-256", "")
        signature = header[7:] if header.startswith("sha256=") else ""
        if not validate_signature(request.get_data(), signature):
            logging.warning("Signature verification failed")
            return jsonify({"status": "error", "message": "Invalid signature"}), 403
        return f(*args, **kwargs)

    return decorated_function
