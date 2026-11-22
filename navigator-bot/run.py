import logging

from waitress import serve

from app import create_app

app = create_app()

if __name__ == "__main__":
    logging.info("Navigator bot listening on http://localhost:8000")
    serve(app, host="0.0.0.0", port=8000, threads=8)
