import logging
import os

from waitress import serve

from app import create_app
from app.kb_sync import start_background_sync

app = create_app()

if __name__ == "__main__":
    start_background_sync()  # only with KB_REPO set (servers): pull the guides from GitHub, keep them fresh
    port = int(os.getenv("PORT") or 8000)  # cloud platforms set PORT; locally it is 8000
    logging.info("Navigator bot listening on port %s", port)
    serve(app, host="0.0.0.0", port=port, threads=8)
