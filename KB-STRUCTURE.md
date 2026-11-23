# What the bot reads

The Migration Navigator bot (WhatsApp, Telegram and the web chat, in `navigator-bot/`) reads the guides straight from `main` on GitHub. It checks for new commits every 15 minutes, so a merged change reaches people within about 15 minutes, with no redeploy. Keep to the structure below, and the bot picks up every change by itself.

## The files it reads

- **A guide is any folder with a `doc.md`.** Today:
  - `countries/<country>/doc.md`: one per destination;
  - `agencies/doc.md`;
  - `global/<topic>/doc.md`: faq, dalal-scams, departure, illegal-routes, money, services, other-destinations.
- **What kind of guide it is:**
  - every folder directly under `countries/` is a destination;
  - every other guide applies to all countries.
  - The folder name is the guide's id (`saudi-arabia`, `faq`), so don't rename folders casually.
- **Beside each `doc.md`:** `facts.csv` and `sources.csv`. The bot uses them to tell official facts from news reports and to show each fact's date.
- **What it ignores:** `README.md`, the `.docx` files, `notes.md`, `questions.md`, `sources/`, `passes/`, `datasets/`, `tools/`, `official-pdfs/` and `data/`.

## Inside `doc.md`

- **Headings:** one `#` title, then `##`, `###` and `####` headings. The bot splits each guide into sections at the headings, and the heading path is what it searches and quotes, so headings should say what the section is about.
- **Citations:** in square brackets, like `[A0123]` or `[A0123, N0045]`. The ids must match the `id` column of `facts.csv` beside the doc.
- **Open questions:** in a quote block that starts `> **Need to know**`. The bot never states these as facts.
- **Title:** for a country guide, starts with the country's name (`# Saudi Arabia: migration guide`). The bot uses it as the country's name in chats and on the web page.

## `facts.csv`

The bot reads these columns: `id`, `url`, `source_type` (`official`, `news`, `official-archived`, `news-archived`), `status` and `page_date` (`YYYY-MM-DD`, `YYYY-MM` or `undated`). Other columns are free to change.

## Changes that need care

- **New country:** add `countries/<country>/` with `doc.md`, `facts.csv` and `sources.csv`. Nothing else to do. To add Bangla names or city names people type for it (like "দুবাই" for the UAE), edit `ALIASES` and `DISPLAY` in `navigator-bot/app/countries.py`.
- **Renaming, moving, splitting or deleting a guide:** the check on the pull request ("Bot can read the guides") will flag the old guide as gone. Say in the pull request that it's on purpose. Once merged, the live bot refuses the new version until someone confirms it (on the server: `python -m app.kb_index --force`), so tell the bot team first.
- **Cutting a large part of a guide:** the same check fails if a guide with 20 or more sections loses more than half of them.

## What protects the live bot

- **Before merging:** the pull-request check builds the bot's index from the pull request and compares it with `main`.
- **On the server:** a new version replaces the old one only if no guide vanished or lost most of its sections. Otherwise the bot keeps answering from the last good version.
- **Reporting:** `https://<bot address>/health` shows the commit the bot is using, how many guides it loaded, and any warning.
