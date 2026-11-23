import logging
import threading

from flask import Flask

from app.config import configure_logging, load_configurations
from .telegram_views import telegram_blueprint
from .utils.telegram_utils import register_webhook
from .views import webhook_blueprint
from .web_views import web_blueprint


def create_app():
    app = Flask(__name__)
    load_configurations(app)
    configure_logging()
    app.register_blueprint(webhook_blueprint)
    app.register_blueprint(telegram_blueprint)
    app.register_blueprint(web_blueprint)
    if app.config["WEB_CHAT"].lower() not in {"off", "false", "0", "no"} and not app.config["TURNSTILE_SECRET_KEY"]:
        logging.warning("Web chat is on without a bot check: set TURNSTILE_SITE_KEY and TURNSTILE_SECRET_KEY before going public.")
    # Telegram is optional: with a token, point its webhook at PUBLIC_DOMAIN in the background.
    if app.config["TELEGRAM_BOT_TOKEN"] and app.config["PUBLIC_DOMAIN"]:
        threading.Thread(
            target=register_webhook,
            args=(app.config["TELEGRAM_BOT_TOKEN"], app.config["PUBLIC_DOMAIN"]),
            daemon=True,
        ).start()
    return app
