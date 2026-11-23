# Navigator bot

WhatsApp, Telegram and web chat bot that answers questions about working abroad from the BSAISL knowledge base.
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

## Web chat

The same app also serves a chat page at `https://<PUBLIC_DOMAIN>/`, with no login, for people who use
neither WhatsApp nor Telegram (it also opens from links shared in imo or Facebook). It uses the same index,
reply logic, memory and limits. Code: `app/web_views.py` (routes) and `app/static/web/` (the page: plain
HTML, CSS and JavaScript, no framework, no build step).

- **Bot check.** Before going public, create a free Cloudflare Turnstile widget for the domain
  (Cloudflare dashboard > Turnstile > Add widget, mode "Managed") and put its keys in `TURNSTILE_SITE_KEY`
  and `TURNSTILE_SECRET_KEY`. Visitors then pass an (almost always invisible) check before their chat starts.
  Without the keys the page works, and the bot logs a warning at start.
- **Sessions.** A visitor gets a signed cookie (`nav_sid`, 24 hours, HttpOnly, SameSite=Strict). Each
  session counts as one user for the limits and the 30-day memory; "New chat" and "Delete my data" work as
  "reset" and "delete my data" do on WhatsApp.
- **Behind a proxy** (ngrok, Cloudflare, a cloud host), set `PROXY_IP_HEADER`, or every visitor shares one
  IP limit. The header is believed only from `TRUSTED_PROXIES` (default: this machine and private networks).
  On a server of your own, publish the port only to the proxy (e.g. `127.0.0.1:8000:8000` in
  docker-compose.yml), so nobody can skip the proxy and fake the header.
- **Turn it off** with `WEB_CHAT=off`.

## Abuse limits and AI budgets

`app/guard.py` checks every message on every channel before anything is answered, so a flood costs almost
nothing. **The defaults are lenient, for the testing phase.** Before a public launch, set the public values
in `.env` (names and suggested values in `.env.example`).

| Limit | Testing default | Suggested public |
|---|---|---|
| Web, per session | 20 a minute, 200 a day | 6 a minute, 40 a day |
| WhatsApp, per number | 30 a minute, 500 a day | 20 a minute, 150 a day |
| Telegram, per account | 30 a minute, 500 a day | 15 a minute, 100 a day |
| Web, per IP address (IPv6: per /64 block) | 1,000 a day, 60 new sessions an hour | 200 a day, 20 sessions an hour |
| Web, all visitors together | 200 a minute | 60 a minute |

- WhatsApp and Telegram get more room than the web because each user is a real phone number; the web page
  has no identity at all. Per-IP limits stay loose because mobile operators put many people behind one address.
- At most 4 web answers are worked on at once, so web traffic can't hold up WhatsApp.
- "reset" and "delete my data": 30 a minute, never blocked for the day.
- Messages longer than 500 characters are refused with a short note.
- AI spending per day: web $3, WhatsApp $10, Telegram $3. When one channel's budget is spent, only that
  channel pauses. The AI step must call `guard.add_cost()` for every reply, or the budgets never trip. Also
  set a credit limit on the OpenRouter key itself, as a ceiling the code can't exceed.
- On WhatsApp and Telegram, a user over a limit is told once; further messages in that window get no reply.

Today's spending: `python -m app.guard` on the server (kept off the public `/health` page so an attacker
can't watch a budget drain). A warning is logged when a channel reaches 80%. Days reset at midnight
Bangladesh time.

## Where the knowledge base comes from

The bot lives in the knowledge-base repository and reads the guides from the folder above it
(`../countries/*/doc.md`, `../agencies/doc.md`, `../global/*/doc.md`). It never edits them.
To use a copy somewhere else, set `KB_DIR` in `.env`. On a server, `KB_REPO` makes the bot fetch the
guides from GitHub instead (see Run in the cloud).

## When the knowledge base changes

`git pull`, then restart with `.\start.ps1 -Reindex`
(or run `python -m app.kb_index` while the bot keeps running; the new index is swapped in at once).

## Run in the cloud (Docker)

The bot runs anywhere Docker runs, so it doesn't need this PC or ngrok.

**The image holds only the bot's code.** Build it from this folder: `docker build -t navigator-bot .`
(`docker compose up -d --build` does the same and starts it). `.env`, `.venv` and `data/` never go in.

**The knowledge base comes straight from GitHub.** With `KB_REPO` set, the bot clones the repository as it
starts, but only the files it reads (each `doc.md`, `facts.csv` and `sources.csv`, about 28 MB; never the
multi-GB `sources/` archives), builds its index, and starts answering about 10 seconds later. Every
`KB_SYNC_MINUTES` (default 15) it fetches `main` again and rebuilds the index if the commit changed. So a
knowledge-base push goes live within 15 minutes, with no rebuild, redeploy or restart. If GitHub can't be
reached, the bot keeps answering from the last index. `https://<host>/health` shows `kb_commit`: compare it
with the latest commit on GitHub to check an update is live. Code in `app/kb_sync.py`; run one sync by hand
with `python -m app.kb_sync`.

**Settings.** Never upload `.env`. Enter each value as an environment variable or secret in the platform's
settings (or in `.env` on a server of your own, which stays outside git), using the names in `.env.example`:

- Required: `WHATSAPP_PHONE_NUMBER_ID`, `WHATSAPP_ACCESS_TOKEN`, `META_APP_SECRET`, `WHATSAPP_VERIFY_TOKEN`
  (keep the same verify token as before), and `KB_REPO` (the repository's GitHub URL).
- Also set: `WHATSAPP_BUSINESS_ACCOUNT_ID`, `GRAPH_API_VERSION` (v27.0), `PUBLIC_DOMAIN` (the new host name,
  without https://), and the `LLM_*` values once the AI step is on. `TELEGRAM_BOT_TOKEN` only if Telegram is used.
- Optional: `KB_BRANCH` (main), `KB_SYNC_MINUTES` (15), `KB_GITHUB_TOKEN` only if the repository becomes private.
- Leave `KB_DIR` empty. `PORT` is usually set by the platform (8000 if not).

**Keep `data/`.** Mount a persistent volume at `/srv/navigator-bot/data`. Without one the bot still works and
re-fetches the guides at each start, but it forgets the 30-day chat memory and the list of answered message
ids, so a Meta retry arriving just after a restart could be answered twice.

**Pick a host that never sleeps.** Meta retries webhooks that time out, and a cold start makes the first
reply feel broken. Avoid free tiers that spin down when idle, and serverless platforms that pause the CPU
after the response (the bot sends its reply from a background thread after answering Meta).

**When the bot's code changes** (not the knowledge base): rebuild and restart the container
(`git pull` then `docker compose up -d --build` on a server).

**Switching Meta to the new address.** In the Meta app: WhatsApp > Configuration > Webhook > Edit.
Callback URL `https://<new host>/webhook`, the same verify token, then Verify and save. Check that the
`messages` field is still subscribed. Then test: `https://<new host>/health`, the handshake (Meta's Verify
succeeds), and a real WhatsApp "hi" with this PC off.

## Files that never go to git

`.env` (keys), `.venv/` (rebuilt by `start.ps1`) and `data/` (index and chat memory) are listed in `.gitignore`.
Copy `.env.example` to `.env` and fill it in on each machine that runs the bot.

## Layout

- `app/views.py`: webhook (Meta verification, signature check, answers in the background)
- `app/utils/whatsapp_utils.py`: reading and sending WhatsApp messages
- `app/telegram_views.py` and `app/utils/telegram_utils.py`: Telegram webhook, formatting (HTML) and sending
- `app/kb_index.py`: builds and searches `data/kb.sqlite` from each guide's `doc.md`
- `app/kb_sync.py`: on servers, pulls the guides from GitHub into `data/kb-repo` and re-indexes when they change
- `app/store.py`: conversation memory and duplicate checks in `data/state.sqlite` (users stored as hashes, deleted after 30 days)
- `app/answer.py`: turns a message into a reply for every channel (search-only test mode until the AI is connected)
- `app/countries.py`: country names in English and Bangla
- `app/web_views.py` and `app/static/web/`: the web chat page and its API
- `app/guard.py`: message limits and daily AI budgets for every channel

Users can send "delete my data" to erase their history, or "reset" to start over.
