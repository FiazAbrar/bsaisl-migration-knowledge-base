"""All settings come from environment variables (.env). Moving to another
Meta account or model means changing .env only, never the code."""
import logging
import os
import sys

from dotenv import load_dotenv

SETTINGS = [
    "KB_DIR",
    "WHATSAPP_PHONE_NUMBER_ID",
    "WHATSAPP_BUSINESS_ACCOUNT_ID",
    "WHATSAPP_ACCESS_TOKEN",
    "META_APP_SECRET",
    "WHATSAPP_VERIFY_TOKEN",
    "GRAPH_API_VERSION",
    "PUBLIC_DOMAIN",
    "LLM_BASE_URL",
    "LLM_API_KEY",
    "LLM_MODEL",
    "TEST_RECIPIENT",
    "TELEGRAM_BOT_TOKEN",
    "WEB_CHAT",
    "TURNSTILE_SITE_KEY",
    "TURNSTILE_SECRET_KEY",
    "PROXY_IP_HEADER",
    "TRUSTED_PROXIES",
    "WEB_SESSION_SECRET",
]
REQUIRED = [
    "WHATSAPP_PHONE_NUMBER_ID",
    "WHATSAPP_ACCESS_TOKEN",
    "META_APP_SECRET",
    "WHATSAPP_VERIFY_TOKEN",
]


def load_configurations(app):
    load_dotenv()
    for name in SETTINGS:
        app.config[name] = (os.getenv(name) or "").strip()
    app.config["GRAPH_API_VERSION"] = app.config["GRAPH_API_VERSION"] or "v27.0"
    app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024  # no webhook or chat message comes near 1 MB
    missing = [n for n in REQUIRED if not app.config[n]]
    if missing:
        raise RuntimeError(f"Missing settings in .env: {', '.join(missing)}")


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        stream=sys.stdout,
    )
