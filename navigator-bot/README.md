# Navigator bot

WhatsApp, Telegram and web chat bot that answers questions about working abroad from the BSAISL knowledge base.
One TypeScript app on [Chat SDK](https://chat-sdk.dev) (the channels) and the [AI SDK](https://ai-sdk.dev)
(the AI step, through OpenRouter), shipped as one Docker container plus a settings file.

## Run on a PC

Needs Node 26 (`winget install OpenJS.NodeJS.LTS`) and, for WhatsApp and Telegram, ngrok.

1. `npm ci` once, then copy `.env.example` to `.env` and fill it in (Meta setup: [docs/SETUP-META.md](docs/SETUP-META.md)).
2. Double-click `start.bat`, or run `.\start.ps1` in PowerShell. It builds the web page if needed, opens the
   ngrok tunnel to `PUBLIC_DOMAIN`, and starts the bot on port 8000.
3. Check `http://localhost:8000/health`. Without ngrok, `npm run dev` runs the bot alone (web chat at
   http://localhost:8000/, reloads on code changes).

The bot reads the guides from the repository it sits in and keeps its memory in an embedded database
(`data/pglite`). Nothing to install besides Node.

## Commands

| Command | What it does |
|---|---|
| `npm run dev` | Run the bot locally, reloading on changes (reads `.env`) |
| `npm start` | Run the bot (servers and Docker; settings come from the environment) |
| `npm run check` | Lint (Biome), type-check (tsc) and test (Vitest): what CI runs |
| `npm run build:web` | Build the web chat page into `web/dist` (`npm run dev:web` for live editing) |
| `npm run kb:index` | Read every guide and print its section count |
| `npm run kb:check -- --base origin/main` | The pull-request check: would the bot refuse this version of the guides? |
| `npm run eval` | Evaluation questions: search hit rate, or with an AI key, graded answers per model |
| `npm run db:generate` | After changing `src/db/schema.ts`: write the migration (applied at start-up) |

## How a message is answered

Every channel goes through the same steps (`src/conversation/pipeline.ts`):

1. Not text (voice, photo) → "please send text" in Bangla and English.
2. Commands: `reset`, `delete my data` (also in Bangla, and `/start`, `/reset`, `/delete` on Telegram).
3. Messages over 500 characters are refused; then the abuse limits (`src/guard/guard.ts`).
4. Phone, NID, passport and card numbers are removed before anything is stored or sent to the AI.
5. The guide is the country named in the message, or the one chosen earlier.
6. The answer: with `OPENROUTER_API_KEY` set, the AI searches and reads the guides and answers following
   `prompts/system.md`; without it, test mode lists the closest guide sections.
7. A new person's first reply ends with the privacy notice (using the bot means agreeing to it).

Fixed texts (welcome, refusals, errors) are in English and Bangla (`src/conversation/i18n.ts`): Bangla script
gets Bangla, anything else English. AI answers follow the person's language and script.

**Memory**, the way Claude Code manages its own context (`src/conversation/context.ts`, `src/ai/memory.ts`):
the AI sees a short profile card about the person, a running summary of older messages, and as many recent
messages as fit `CONTEXT_TOKEN_BUDGET`. After each reply, a small model updates the profile card and folds
messages that no longer fit into the summary. Guide text is never kept in the history; it is searched fresh
for every question. Retention: messages 90 days, the person (profile, summary, chosen guide) 12 months after
their last message, checked daily. "delete my data" removes everything at once. See `docs/PRIVACY.md`
(also served at `/privacy`).

**Reliability.** Each message is written to an inbox before it is answered and removed once the reply is
sent; after a restart, anything left from the last hour is answered. Meta's repeat deliveries are ignored
for 7 days. Messages sent while one is being answered are answered together.

## The AI step

Set `OPENROUTER_API_KEY` and `LLM_MODEL` (an OpenRouter model id). The model works with read-only tools only
(`search_guides`, `list_guide_sections`, `read_section`), never the web. Safeguards in code:

- **Number check:** every amount, phone number and year in an answer must appear in the guide text the AI
  read for it; otherwise it is asked once to correct or remove them (`src/ai/numbers.ts`).
- At most 8 tool steps, `LLM_MAX_OUTPUT_TOKENS`, a timeout (`LLM_TIMEOUT_MS`), and `LLM_FALLBACK_MODEL` if the
  main model fails.
- Only OpenRouter providers that don't keep data (`data_collection: deny`).
- Each reply's cost (reported by OpenRouter) counts against the channel's daily budget. Also set a credit limit
  on the OpenRouter key itself.

**Comparing models:** set `EVAL_MODELS=model-a,model-b` and run `npm run eval`: each model answers every
question in `evals/questions.csv` and a judge model grades it against `must_include` and `must_not`. Results go
to `evals/results/` (not committed). Every run costs money; the summary prints the total.

## Telegram

### Create the bot (once, about 2 minutes)

1. In Telegram, open a chat with **@BotFather** (the official one has a blue tick) and send `/newbot`.
2. **Name** (shown in chats, can be changed later): e.g. `Migration Navigator`.
3. **Username** (permanent, must end in `bot`): e.g. `bsaisl_navigator_bot`.
4. BotFather replies with a token like `123456789:AA...`. Paste it into `.env` after `TELEGRAM_BOT_TOKEN=`
   and nowhere else (never in chat, git or screenshots). If it leaks, send `/revoke` to @BotFather.
5. Optional: `/setdescription` and `/setuserpic`.

As it starts, the bot points Telegram at `https://<PUBLIC_DOMAIN>/telegram` (skipped when already set) and adds
the `/start`, `/reset` and `/delete` menu in English and Bangla. Then open `t.me/<username>` and press **Start**.

- Telegram signs each delivery with a secret derived from the token; anything else is refused.
- Only private chats are answered; groups are ignored.
- One token has one webhook address: whichever copy of the bot started last (a PC or the cloud) gets the
  messages. Use a second test bot on a PC if the cloud copy must keep running.

## Web chat

A chat page at `https://<PUBLIC_DOMAIN>/` with no login, for people who use neither WhatsApp nor Telegram.
The page (`web/`) is plain TypeScript, no framework, about 10 KB of script, built with Vite. Replies stream in
over the AI SDK's message stream protocol (`src/server.ts` → Chat SDK's web adapter).

- **Bot check.** Before going public, create a free Cloudflare Turnstile widget for the domain (Cloudflare
  dashboard > Turnstile > Add widget, mode "Managed") and set `TURNSTILE_SITE_KEY` and `TURNSTILE_SECRET_KEY`.
- **Sessions.** A visitor gets a signed cookie (`nav_sid`, 24 hours, HttpOnly, SameSite=Strict). Each session
  counts as one user for limits and memory. "New chat" and "Delete my data" work like `reset` and
  `delete my data`. Requests from other websites are refused.
- **Behind a proxy** (Render, ngrok, Cloudflare) set `PROXY_IP_HEADER`, or every visitor shares one IP limit.
  The header is believed only from `TRUSTED_PROXIES` (default: this machine and private networks).
- **Turn it off** with `WEB_CHAT=off`.

## Abuse limits and AI budgets

Every message on every channel is checked before anything is answered. **The defaults are lenient, for
testing.** Before a public launch, set the public values (names in `.env.example`).

| Limit | Testing default | Suggested public |
|---|---|---|
| Web, per session | 20 a minute, 200 a day | 6 a minute, 40 a day |
| WhatsApp, per number | 30 a minute, 500 a day | 20 a minute, 150 a day |
| Telegram, per account | 30 a minute, 500 a day | 15 a minute, 100 a day |
| Web, per IP address (IPv6: per /64 block) | 1,000 a day, 60 new sessions an hour | 200 a day, 20 sessions an hour |
| Web, all visitors together | 200 a minute | 60 a minute |

- Refused messages don't count. On WhatsApp and Telegram a person over a limit is told once; further messages in
  that window get no reply.
- At most 4 web answers are worked on at once, so the open page can't hold up WhatsApp.
- `reset` and `delete my data`: 30 a minute, never blocked for the day.
- AI spending per day: web $3, WhatsApp $10, Telegram $3. When one channel's budget is spent, only that
  channel pauses. Sentry gets a warning at 80%. Days reset at midnight Bangladesh time.
- Counters live in the database and are counted atomically, so several copies of the bot share them exactly.

## The knowledge base

The bot never edits the guides. A guide is any folder with a `doc.md`; folders under `countries/` are
destinations, the rest apply to every country. New guides need no code change. The rules the team keeps to are
in `../CLAUDE.md` ("What the bot reads"). Country names people type (English, Bangla, Banglish, cities) are in
`src/kb/countries.ts`.

On a server, `KB_REPO` makes the bot fetch the guides from GitHub: a shallow, sparse copy of only the files it
reads (each `doc.md`, `facts.csv`, `sources.csv`; never the `sources/` archives), refreshed every
`KB_SYNC_MINUTES`. A knowledge-base push goes live within 15 minutes, with no redeploy.

**Safe swap.** A new version replaces the old one only if no guide disappeared and none with 20 or more sections
lost more than half of them. Otherwise the bot keeps answering from the last good version, shows why on
`/health` (`kb_sync.index_refused`) and alerts Sentry. The last good commit is kept in the database, so the
check survives restarts. To accept a deliberate removal or rename, set `KB_ACCEPT_COMMIT` to that commit
(first 7 characters) and remove it once `/health` shows it. The pull-request check
(`.github/workflows/bot-kb-check.yml`) catches the same problems before they reach `main`.

## Run in the cloud

The image holds only the bot's code: `docker build -t navigator-bot .` (or `docker compose up -d --build`).
`.env` and `data/` never go in. The agreed free setup is **Render** (web service, Docker, Singapore) + **Neon**
(Postgres, Singapore) + **UptimeRobot** (pings `/health` every 5 minutes so Render's free plan doesn't sleep).

**Render settings:** root directory `navigator-bot`, runtime Docker, region Singapore, health check path
`/health`, build filter `navigator-bot/**` (so guide pushes don't redeploy; they arrive through `KB_REPO`).
Enter each value from `.env.example` as an environment variable on Render:

- Required: `USER_HASH_SECRET`, `KB_REPO`, `DATABASE_URL` (Neon's pooled address), `PUBLIC_DOMAIN` (the Render
  host, without https://), `PROXY_IP_HEADER=X-Forwarded-For`, `NODE_ENV=production`.
- WhatsApp: `WHATSAPP_PHONE_NUMBER_ID`, `WHATSAPP_ACCESS_TOKEN`, `WHATSAPP_APP_SECRET`, `WHATSAPP_VERIFY_TOKEN`
  (keep the same verify token), `WHATSAPP_BUSINESS_ACCOUNT_ID`.
- Telegram: `TELEGRAM_BOT_TOKEN`. Web: `TURNSTILE_SITE_KEY`, `TURNSTILE_SECRET_KEY`, the public `GUARD_*` values.
- Recommended: `SENTRY_DSN`. Later: `OPENROUTER_API_KEY`, `LLM_MODEL`.

**Switching Meta to the new address.** In the Meta app: WhatsApp > Configuration > Webhook > Edit. Callback URL
`https://<host>/webhook`, the same verify token, Verify and save; check the `messages` field is subscribed.
Telegram re-registers itself from `PUBLIC_DOMAIN`. Then test `/health`, Meta's Verify, and a "hi" on each channel
with the PC off. WhatsApp is open to everyone only once a real number replaces Meta's test number.

**Handing over to BRAC IT:** run the same image on their server or host with their own values: their Meta app
and number, Telegram token, OpenRouter key, Postgres address and Sentry project. The code doesn't change.

## Layout

- `src/main.ts` start-up and shutdown · `src/app.ts` builds the bot · `src/server.ts` HTTP routes · `src/config.ts` settings
- `src/channels/` Chat SDK bot (WhatsApp, Telegram, web), message handler, Telegram webhook registration
- `src/conversation/` the pipeline, commands, Bangla/English texts, safeguards, context builder
- `src/kb/` guide discovery, parsing, search, country names, GitHub sync and safe swap, the PR check
- `src/memory/` people and messages (hashed, with retention), the restart inbox
- `src/guard/` abuse limits and daily AI budgets · `src/ai/` model, tools, prompt, number check, memory updates
- `src/db/` database schema and connection (migrations in `drizzle/`) · `src/ops/` logging and Sentry
- `src/web/` web session security · `web/` the chat page · `prompts/` the system prompt · `evals/` questions and runner
- `test/` Vitest tests: unit, database (embedded Postgres) and end-to-end channel tests with Meta and Telegram faked
