"""Country names people may type, in English and Bangla, mapped to knowledge-base folder names.

ALIASES and DISPLAY add nicknames, cities and Bangla names for the countries we know. A country guide
added later (a new folder under countries/) works without touching this file: its folder name and its
doc.md title are recognised automatically, and it gets a button on the web page under its English name.
"""
import re

ALIASES = {
    "saudi-arabia": ["saudi", "ksa", "riyadh", "jeddah", "সৌদি", "সৌদি আরব"],
    "malaysia": ["malaysia", "malaysian", "kuala lumpur", "মালয়েশিয়া", "মালয়েশিয়া", "মালয়শিয়া", "মালেশিয়া"],
    "qatar": ["qatar", "doha", "কাতার"],
    "united-arab-emirates": ["uae", "emirates", "dubai", "abu dhabi", "sharjah", "দুবাই", "আমিরাত", "আরব আমিরাত"],
    "singapore": ["singapore", "সিঙ্গাপুর", "সিংগাপুর"],
    "kuwait": ["kuwait", "কুয়েত", "কুয়েত", "কুয়েত"],
    "oman": ["oman", "muscat", "ওমান"],
    "maldives": ["maldives", "male", "মালদ্বীপ"],
    "jordan": ["jordan", "amman", "জর্ডান"],
    "italy": ["italy", "italia", "rome", "ইতালি"],
    "cambodia": ["cambodia", "phnom penh", "কম্বোডিয়া", "কম্বোডিয়া"],
    "kyrgyzstan": ["kyrgyzstan", "kyrgyz", "bishkek", "কিরগিজস্তান", "কিরগিস্তান"],
    "brunei": ["brunei", "bandar seri begawan", "ব্রুনাই"],
    "japan": ["japan", "tokyo", "জাপান"],
    "south-korea": ["south korea", "korea", "seoul", "eps korea", "দক্ষিণ কোরিয়া", "দক্ষিণ কোরিয়া", "কোরিয়া", "কোরিয়া"],
    "canada": ["canada", "toronto", "কানাডা"],
    "greece": ["greece", "athens", "গ্রিস", "গ্রীস"],
    "india": ["india", "ভারত", "ইন্ডিয়া"],
    "lebanon": ["lebanon", "beirut", "লেবানন"],
    "united-kingdom": ["uk", "united kingdom", "england", "britain", "london", "যুক্তরাজ্য", "ইংল্যান্ড", "লন্ডন", "বিলেত"],
    "united-states": ["usa", "united states", "america", "আমেরিকা", "যুক্তরাষ্ট্র"],
}

# Names shown on the web page's country buttons, in the order shown there.
DISPLAY = [
    ("saudi-arabia", "Saudi Arabia", "সৌদি আরব"),
    ("malaysia", "Malaysia", "মালয়েশিয়া"),
    ("united-arab-emirates", "UAE", "সংযুক্ত আরব আমিরাত"),
    ("qatar", "Qatar", "কাতার"),
    ("oman", "Oman", "ওমান"),
    ("kuwait", "Kuwait", "কুয়েত"),
    ("singapore", "Singapore", "সিঙ্গাপুর"),
    ("maldives", "Maldives", "মালদ্বীপ"),
    ("jordan", "Jordan", "জর্ডান"),
    ("italy", "Italy", "ইতালি"),
    ("south-korea", "South Korea", "দক্ষিণ কোরিয়া"),
    ("japan", "Japan", "জাপান"),
    ("brunei", "Brunei", "ব্রুনাই"),
    ("cambodia", "Cambodia", "কম্বোডিয়া"),
    ("kyrgyzstan", "Kyrgyzstan", "কিরগিজস্তান"),
    ("united-kingdom", "United Kingdom", "যুক্তরাজ্য"),
    ("united-states", "United States", "যুক্তরাষ্ট্র"),
    ("canada", "Canada", "কানাডা"),
    ("greece", "Greece", "গ্রিস"),
    ("lebanon", "Lebanon", "লেবানন"),
    ("india", "India", "ভারত"),
]


def _indexed_countries() -> list[dict]:
    from . import kb_index  # here, not at the top, so this module loads even without an index
    try:
        return kb_index.list_countries("country")
    except Exception:  # no index yet: the fixed lists still work
        return []


def all_aliases() -> dict[str, list[str]]:
    """ALIASES plus, for every country guide in the index, its folder name and its title."""
    out = {slug: list(names) for slug, names in ALIASES.items()}
    for c in _indexed_countries():
        names = out.setdefault(c["slug"], [])
        for name in (c["slug"].replace("-", " "), c["title"].split(":")[0].strip().lower()):
            if name and name not in names:
                names.append(name)
    return out


def display() -> list[tuple[str, str, str]]:
    """Country buttons for the web page: DISPLAY first, then any newer country guide by its English title."""
    known = {slug for slug, _, _ in DISPLAY}
    extra = [(c["slug"], c["title"].split(":")[0].strip(), c["title"].split(":")[0].strip())
             for c in _indexed_countries() if c["slug"] not in known]
    return DISPLAY + extra


def strip_countries(text: str) -> str:
    """Remove country names so they don't skew a search inside that country's guide."""
    out = text
    for names in all_aliases().values():
        for name in sorted(names, key=len, reverse=True):
            pattern = rf"\b{re.escape(name)}\b" if name.isascii() else re.escape(name)
            out = re.sub(pattern, " ", out, flags=re.I)
    out = re.sub(r"\b(arabia|arab)\b", " ", out, flags=re.I)
    return re.sub(r"\s+", " ", out).strip()


def detect_country(text: str) -> str | None:
    """Return the knowledge-base slug of the first country named in the text, if any."""
    low = text.lower()
    best = None
    for slug, names in all_aliases().items():
        for name in names:
            # Latin names must match as whole words ("male" not in "female"); Bangla as substrings.
            pattern = rf"\b{re.escape(name)}\b" if name.isascii() else re.escape(name)
            m = re.search(pattern, low)
            if m and (best is None or m.start() < best[0]):
                best = (m.start(), slug)
    return best[1] if best else None
