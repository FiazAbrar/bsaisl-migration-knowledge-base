# Navigator bot

WhatsApp bot that answers questions about working abroad from the BSAISL knowledge base.
Built on the structure of [daveebbelaar/python-whatsapp-bot](https://github.com/daveebbelaar/python-whatsapp-bot) (MIT, see LICENCE.txt).

## Run

1. Fill in `.env` (Meta setup: [docs/SETUP-META.md](docs/SETUP-META.md)).
2. Double-click `start.bat`, or run `.\start.ps1` in PowerShell.
   It creates the Python environment on first run, builds the knowledge-base index if missing,
   opens the ngrok tunnel and starts the bot on port 8000.
3. Check `https://<PUBLIC_DOMAIN>/health`: it shows when the index was built.

## Telegram

The same app also answers on Telegram, from the same index and the same reply logic (`app/answer.py`).
Only the channel layer differs: `app/telegram_views.py` (route `/telegram`) and `app/utils/telegram_utils.py`.

### Create the bot (once, about 2 minutes)

1. In Telegram, open a chat with **@BotFather** (the official one has a blue tick) and send `/newbot`.
2. **Name** (shown in chats, can be changed later): e.g. `Migration Navigator`.
3. **Username** (permanent, must end in `bot`, must be free): e.g. `bsaisl_navigator_bot`. If taken, try another.
4. BotFather replies with a token like `123456789:AA...`. That token is the bot's password:
   paste it into `navigator-bot/.env` after `TELEGRAM_BOT_TOKEN=` and nowhere else (never in chat, git or screenshots).
   If it leaks, send `/revoke` to @BotFather, choose the bot, and paste the new token.
5. Optional, in @BotFather: `/setdescription` (text shown before a user presses Start) and `/setuserpic`.

### Run it

Restart with `start.bat` / `.\start.ps1`. As it starts, the bot tells Telegram to send messages to
`https://<PUBLIC_DOMAIN>/telegram` (skipped when already set) and adds the `/start`, `/reset` and `/delete` menu.
To register by hand instead: `.venv\Scripts\python.exe -m app.utils.telegram_utils`.
Then open `t.me/<username>` and press **Start**.

- Telegram signs each delivery with a secret derived from the token (`X-Telegram-Bot-Api-Secret-Token`); anything else gets 403.
- Telegram user ids are stored only as keyed hashes, like WhatsApp numbers, and share the 30-day memory and "delete my data".
- Only private chats are answered; group messages are ignored.
- One token has one webhook address: whichever copy of the bot started last (your laptop or the cloud) gets the Telegram messages.
  Use a second test bot (its own token) on your laptop if the cloud copy must keep running.
- Leave `TELEGRAM_BOT_TOKEN` empty to run WhatsApp only.

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
- `app/telegram_views.py` and `app/utils/telegram_utils.py`: Telegram webhook, formatting (HTML) and sending
- `app/kb_index.py`: builds and searches `data/kb.sqlite` from each guide's `doc.md`
- `app/store.py`: conversation memory and duplicate checks in `data/state.sqlite` (users stored as hashes, deleted after 30 days)
- `app/answer.py`: turns a message into a reply for every channel (search-only test mode until the AI is connected)
- `app/countries.py`: country names in English and Bangla

Users can send "delete my data" to erase their history, or "reset" to start over.
