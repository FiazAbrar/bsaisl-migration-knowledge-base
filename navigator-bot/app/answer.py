"""Turns a user's message into a reply.

For now this is a search-only placeholder: it finds the closest sections of the right country guide.
When the OpenRouter key is set, the AI step goes here (search -> read sections -> answer).
"""
from app import kb_index, store
from app.countries import detect_country, strip_countries

FORGET_WORDS = {"delete my data", "forget me", "আমার তথ্য মুছে দিন"}
RESET_WORDS = {"reset", "start over", "new question"}


def is_memory_command(text: str) -> bool:
    return text.strip().lower() in FORGET_WORDS | RESET_WORDS


SHARED_GUIDES = {"agencies", "cross-country"}  # apply to every country, not destinations


def _country_list() -> str:
    names = [c["title"].split(":")[0] for c in kb_index.list_countries() if c["slug"] not in SHARED_GUIDES]
    return ", ".join(names)


def welcome() -> str:
    """First message for a new user (Telegram /start)."""
    return ("Hello! I answer questions about going abroad to work, from BRAC's guides for Bangladeshi workers.\n"
            f"I have guides for: {_country_list()}.\n"
            "Tell me the country, then ask your question, for example: *Saudi Arabia*, then *medical check cost*.\n"
            "Send *reset* to start over, or *delete my data* to erase your history.")


def respond(user: str, text: str) -> str:
    """Reply to one message and keep the conversation memory. Every channel calls this.

    `user` is already hashed (store.user_key). Returns Markdown-style text (*bold*);
    each channel converts it to its own format.
    """
    remember = not is_memory_command(text)  # don't store "delete my data" itself
    if remember:
        store.add_turn(user, "user", text)
    out = reply(user, text)
    if remember:
        store.add_turn(user, "bot", out)
    return out


def reply(user: str, text: str) -> str:
    low = text.strip().lower()
    if low in FORGET_WORDS:
        store.forget(user)
        return "Your conversation history with this bot has been deleted."
    if low in RESET_WORDS:
        store.forget(user)
        return "OK, let's start again. Which country are you asking about?"

    slug = detect_country(text)
    if slug:
        store.set_country(user, slug)
    else:
        slug = store.get_country(user)
    if not slug:
        return ("Which country are you asking about? I have guides for: "
                f"{_country_list()}.")

    guide = next(c["title"].split(":")[0] for c in kb_index.list_countries() if c["slug"] == slug)
    query = strip_countries(text)
    header = "(Test mode: AI answers are not connected yet.)\n"
    if not query:
        return f"{header}OK, the *{guide}* guide. What would you like to know?"
    hits = kb_index.search(query, slug, limit=3)
    if not hits:
        return (f"{header}Guide: *{guide}*. I couldn't match your words to a section yet; "
                "for now only English words can be matched.")
    lines = [f"{header}Closest sections in the *{guide}* guide:"]
    for i, h in enumerate(hits, 1):
        lines.append(f"{i}. *{h['path']}*\n   {h['snippet'].strip()}")
    return "\n".join(lines)
