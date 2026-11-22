#!/bin/sh
# Container start: make data/ writable, drop root, then start the bot. run.py pulls the guides from
# GitHub (KB_REPO) and builds the index before it starts answering.
set -e
cd /srv/navigator-bot
mkdir -p data

# Mounted volumes usually arrive owned by root: hand data/ to the app user, then drop root.
if [ "$(id -u)" = "0" ]; then
    chown -R app:app data
    exec setpriv --reuid=app --regid=app --init-groups "$0" "$@"
fi

if [ -z "$KB_REPO" ] && [ ! -d ../countries ]; then
    echo "KB_REPO is not set: set it to the knowledge-base repository's GitHub URL (see .env.example)." >&2
    exit 1
fi

exec python run.py
