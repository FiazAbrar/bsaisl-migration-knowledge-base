"""Country names people may type, in English and Bangla, mapped to knowledge-base folder names."""
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
]


def strip_countries(text: str) -> str:
    """Remove country names so they don't skew a search inside that country's guide."""
    out = text
    for names in ALIASES.values():
        for name in sorted(names, key=len, reverse=True):
            pattern = rf"\b{re.escape(name)}\b" if name.isascii() else re.escape(name)
            out = re.sub(pattern, " ", out, flags=re.I)
    out = re.sub(r"\b(arabia|arab)\b", " ", out, flags=re.I)
    return re.sub(r"\s+", " ", out).strip()


def detect_country(text: str) -> str | None:
    """Return the knowledge-base slug of the first country named in the text, if any."""
    low = text.lower()
    best = None
    for slug, names in ALIASES.items():
        for name in names:
            # Latin names must match as whole words ("male" not in "female"); Bangla as substrings.
            pattern = rf"\b{re.escape(name)}\b" if name.isascii() else re.escape(name)
            m = re.search(pattern, low)
            if m and (best is None or m.start() < best[0]):
                best = (m.start(), slug)
    return best[1] if best else None
