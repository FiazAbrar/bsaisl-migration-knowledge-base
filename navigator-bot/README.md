# Navigator bot

WhatsApp bot that answers questions about working abroad from the BSAISL knowledge base.
Built on the structure of [daveebbelaar/python-whatsapp-bot](https://github.com/daveebbelaar/python-whatsapp-bot) (MIT, see LICENCE.txt).

## Run

1. Fill in `.env` (Meta setup: [docs/SETUP-META.md](docs/SETUP-META.md)).
2. Double-click `start.bat`, or run `.\start.ps1` in PowerShell.
   It creates the Python environment on first run, builds the knowledge-base index if missing,
   opens the ngrok tunnel and starts the bot on port 8000.
3. Check `https://<PUBLIC_DOMAIN>/health`: it shows when the index was built.

## Where the knowledge base comes from

The bot lives in the knowledge-base repository and reads the guides from the folder above it
(`../countries/*/doc.md`, `../agencies/doc.md`, `../cross-country/doc.md`). It never edits them.
To use a copy somewhere else, set `KB_DIR` in `.env`.

## When the knowledge base changes

`git pull`, then restart with `.\start.ps1 -Reindex`
(or run `python -m app.kb_index` while the bot keeps running; the new index is swapped in at once).

## Files that never go to git

`.env` (keys), `.venv/` (rebuilt by `start.ps1`) and `data/` (index and chat memory) are listed in `.gitignore`.
Copy `.env.example` to `.env` and fill it in on each machine that runs the bot.

## Layout

- `app/views.py`: webhook (Meta verification, signature check, answers in the background)
- `app/utils/whatsapp_utils.py`: reading and sending WhatsApp messages
- `app/kb_index.py`: builds and searches `data/kb.sqlite` from each guide's `doc.md`
- `app/store.py`: conversation memory and duplicate checks in `data/state.sqlite` (users stored as hashes, deleted after 30 days)
- `app/answer.py`: turns a message into a reply (search-only test mode until the AI is connected)
- `app/countries.py`: country names in English and Bangla

Users can send "delete my data" to erase their history, or "reset" to start over.
