"""Flag which harvested stories are about Bangladeshis going abroad to work, and tag them.

Reads stories.jsonl; writes migration-stories.jsonl (relevant stories, full text) and
index.csv (one row per relevant story, no text). Rule-based: see STRONG below.
"""
import csv, json, os, re, sys, collections, unicodedata
N = lambda x: unicodedata.normalize("NFC", x)
HERE = os.path.dirname(os.path.abspath(__file__))
S = r"[\s\-–—‘’'\"]*"
STRONG = {  # name -> pattern; each is a phrase that on its own signals labour migration
 "recruiting_agency": "রিক্রুটিং|জনশক্তি রপ্তানি|জনশক্তি রফতানি|বায়রা|জনশক্তি প্রেরণ",
 "bmet_ministry": "বিএমইটি|জনশক্তি, কর্মসংস্থান ও প্রশিক্ষণ|প্রবাসীকল্যাণ|প্রবাসী কল্যাণ|বৈদেশিক কর্মসংস্থান|বোয়েসেল|ওয়েজ আর্নার্স",
 "going_abroad": "বিদেশগামী|বিদেশ"+S+"গমনেচ্ছু|বিদেশে? (?:পাঠানো|পাঠিয়ে|পাঠানোর|নেওয়ার|নিয়ে যাওয়ার|যাওয়ার জন্য|যেতে)|বিদেশযাত্রা(?!\\S* নিষেধাজ্ঞা)|কর্মী পাঠানো|কর্মী পাঠাতে|শ্রমিক পাঠানো|কর্মী নেওয়া|কর্মী নিতে|কর্মী নিয়োগ|শ্রমিক নেওয়া",
 "migrant_worker": "প্রবাসী"+S+"(?:কর্মী|শ্রমিক)|অভিবাসী"+S+"(?:কর্মী|শ্রমিক)|বাংলাদেশি"+S+"(?:কর্মী|শ্রমিক)|অভিবাসনপ্রত্যাশী|অভিবাসন"+S+"প্রত্যাশী|অভিবাসন"+S+"ব্যয়|অভিবাসন"+S+"খরচ|নিরাপদ অভিবাসন|শ্রম অভিবাসন",
 "returnee": "বিদেশ"+S+"ফেরত|প্রবাস"+S+"ফেরত|বাংলাদেশিকে ফেরত|বাংলাদেশি\\S* (?:\\S+ ){0,2}ফেরত পাঠ",
 "trafficking": "মানব"+S+"পাচার|পাচারের শিকার",
 "sea_route": "ভূমধ্যসাগর|লিবিয়া|নৌকাডুবি|অবৈধভাবে (?:ইতালি|ইউরোপ|মালয়েশিয়া|সাগরপথ)|সাগরপথে|গেমঘর|‘গেম’",
 "labour_market": "(?:বিদেশের?|বৈদেশিক|আন্তর্জাতিক|মালয়েশিয়ার?|সৌদি\\S*|মধ্যপ্রাচ্যের?|ওমানের?|আমিরাতের?|কুয়েতের?|কাতারের?|ইউরোপের?|জাপানের?|নতুন|বিকল্প) শ্রমবাজার|শ্রমবাজার (?:খুল|বন্ধ|উন্মুক্ত|চালু)",
 "work_visa": "কাজের ভিসা|কর্মী ভিসা|শ্রমিক ভিসা|ওয়ার্ক"+S+"পারমিট|ওয়ার্ক ভিসা|ভিসা"+S+"প্রতারণা|ভুয়া ভিসা|জাল ভিসা|ফ্রি ভিসা|ইকামা|আকামা|কফিল|কাফালা|ভিজিট ভিসায়|ভ্রমণ ভিসায়|ই-ভিসা|ওয়ার্ক পারমিট",
 "broker": "দালাল(?:ের|দের|েরা|কে|চক্র)?",
 "remit_worker": "রেমিট্যান্স"+S+"যোদ্ধা|প্রবাসী আয়|প্রবাসী আয়",
 "abroad_job_fraud": "চাকরি দেওয়ার কথা বলে|চাকরির প্রলোভন|ওভারসিজ|ওভারসীজ|নিয়োগপত্র ও ভিসা|ভিসা ও নিয়োগপত্র|ভুয়া নিয়োগপত্র|ভিসা\\S* (?:\\S+ )?ভুয়া|বিদেশে (?:চাকরি|কাজ|ভালো বেতন)|বিদেশে নেওয়ার কথা বলে|বিদেশ নেওয়ার|(?:পাঠানোর|নেওয়ার) (?:কথা বলে|নামে|প্রলোভন)",
}
LAB = "সৌদি|মালয়েশিয়া|আমিরাত|দুবাই|আবুধাবি|শারজাহ|কাতার|ওমান|কুয়েত|বাহরাইন|সিঙ্গাপুর|মালদ্বীপ|জর্ডান|লেবানন|লিবিয়া|ইতালি|গ্রিস|রোমানিয়া|সার্বিয়া|ক্রোয়েশিয়া|রাশিয়া|কিরগিজ|ব্রুনেই|কম্বোডিয়া|ইরাক|মরিশাস|মধ্যপ্রাচ্য|দক্ষিণ কোরিয়া|জাপান|পর্তুগাল|পোল্যান্ড|মাল্টা|সাইপ্রাস"
STRONG["expat_in_destination"] = "(?:" + LAB + ")\\S*" + S + "(?:প্রবাসী|\\S+ \\S*বাংলাদেশি|বাংলাদেশি)|প্রবাসী\\S* \\S* ?(?:" + LAB + ")|(?:" + LAB + ")\\S* (?:\\S+ ){0,4}(?:বাংলাদেশি|প্রবাসী)\\S* (?:\\S+ ){0,3}(?:নিহত|মৃত্যু|মারা|আটক|গ্রেপ্তার|কারাদণ্ড|মৃত্যুদণ্ড|ফেরত|কর্মী|শ্রমিক)"
STRONG = {k: re.compile(N(v)) for k, v in STRONG.items()}
BROKER_CTX = re.compile(N("বিদেশ|ভিসা|প্রবাস|ইতালি|লিবিয়া|মালয়েশিয়া|সৌদি|দুবাই|ওমান|কাতার|কুয়েত|ইউরোপ|পাসপোর্ট"))
COUNTRIES = {"Saudi Arabia":"সৌদি","Malaysia":"মালয়েশিয়া","UAE":"আরব আমিরাত|দুবাই|আবুধাবি|শারজাহ","Qatar":"কাতার","Oman":"ওমান","Kuwait":"কুয়েত","Bahrain":"বাহরাইন",
 "Singapore":"সিঙ্গাপুর","Maldives":"মালদ্বীপ","Jordan":"জর্ডান","Lebanon":"লেবানন","Libya":"লিবিয়া","Italy":"ইতালি","Greece":"গ্রিস","Romania":"রোমানিয়া","Serbia":"সার্বিয়া",
 "Croatia":"ক্রোয়েশিয়া","Portugal":"পর্তুগাল","Poland":"পোল্যান্ড","Hungary":"হাঙ্গেরি","Malta":"মাল্টা","Cyprus":"সাইপ্রাস","Russia":"রাশিয়া","Kyrgyzstan":"কিরগিজ","Azerbaijan":"আজারবাইজান",
 "Japan":"জাপান","South Korea":"দক্ষিণ কোরিয়া|কোরিয়া","Brunei":"ব্রুনেই","Cambodia":"কম্বোডিয়া","Thailand":"থাইল্যান্ড","Vietnam":"ভিয়েতনাম","Laos":"লাওস","Myanmar":"মিয়ানমার",
 "Iraq":"ইরাক","Mauritius":"মরিশাস","Seychelles":"সেশেলস","UK":"যুক্তরাজ্য","USA":"যুক্তরাষ্ট্র","Canada":"কানাডা","Australia":"অস্ট্রেলিয়া","Germany":"জার্মানি","France":"ফ্রান্স","Spain":"স্পেন",
 "Tunisia":"তিউনিসিয়া","Algeria":"আলজেরিয়া","Egypt":"মিসর","Turkey":"তুরস্ক","Iran":"ইরান","India":"ভারত","Fiji":"ফিজি","Kazakhstan":"কাজাখস্তান","Uzbekistan":"উজবেকিস্তান","Albania":"আলবেনিয়া","North Macedonia":"মেসিডোনিয়া","Bosnia":"বসনিয়া"}
COUNTRIES = {k: re.compile(N(v)) for k, v in COUNTRIES.items()}
TOPICS = {
 "fraud": "প্রতারণা|প্রতারক|প্রতারিত|আত্মসাৎ|হাতিয়ে|ভুয়া|জাল (?:ভিসা|পাসপোর্ট|কাগজ)|উধাও",
 "trafficking": "মানব"+S+"পাচার|পাচারকারী|জিম্মি|মুক্তিপণ|নির্যাতন",
 "death_injury": "মৃত্যু|মারা (?:গেছেন|যান)|নিহত|লাশ|মরদেহ|নিখোঁজ|নৌকাডুবি",
 "arrest_case": "গ্রেপ্তার|মামলা|কারাদণ্ড|র‍্যাব|আদালত|রিমান্ড",
 "return_deport": "ফেরত|দেশে ফির|প্রত্যাবাসন|বহিষ্কার|আটক",
 "policy_market": "শ্রমবাজার|সমঝোতা স্মারক|চুক্তি|নীতিমালা|সিন্ডিকেট|মন্ত্রণালয়|উপদেষ্টা|নিষেধাজ্ঞা",
 "cost_money": "লাখ টাকা|হাজার টাকা|অভিবাসন"+S+"ব্যয়|ঋণ|সুদ",
 "remittance": "রেমিট্যান্স|প্রবাসী আয়|প্রবাসী আয়",
}
TOPICS = {k: re.compile(N(v)) for k, v in TOPICS.items()}
BD = re.compile("বাংলাদেশ")
FRAUD = re.compile(N("প্রতারণা|প্রতারক|প্রতারিত|আত্মসাৎ|উধাও|হাতিয়ে"))
VISA = re.compile(N("ভিসা|পাসপোর্ট"))
BDI = re.compile(N("বাংলাদেশি(?!\\S* (?:টাকা|পণ্য|পোশাক|মুদ্রা|ক্রিকেট|দল|সিনেমা|ব্যাংক))"))
MISSION = re.compile(N("দূতাবাস|হাইকমিশন|কনসাল|রাষ্ট্রদূত|কনস্যুলেট"))
ANYC = re.compile(N("|".join(p.pattern for k, p in COUNTRIES.items() if k not in ("India", "Myanmar"))))

def score(d):
    head = N((d.get("headline") or "") + " " + (d.get("subheadline") or ""))
    text = head + " " + N(d["text"])
    sig = {}
    for k, p in STRONG.items():
        n = len(p.findall(text))
        if k == "broker" and n and not BROKER_CTX.search(text): n = 0
        if n: sig[k] = n
    if FRAUD.search(text) and VISA.search(text) and ANYC.search(text):
        sig["visa_fraud_combo"] = 2
    if len(BDI.findall(text)) >= 2 and MISSION.search(text) and ANYC.search(text):
        sig["bangladeshis_abroad"] = 2
    hs = [k for k, p in STRONG.items() if p.search(head)]
    if BDI.search(head) and ANYC.search(head): hs.append("bangladeshis_abroad")
    return sig, hs, text

def classify(d):
    sig, hs, text = score(d)
    kinds = len(sig); total = sum(sig.values())
    s = kinds * 2 + min(total, 10) + 3 * len(hs)
    foreign_politics = d["sections"] and d["sections"][0] in ("যুক্তরাষ্ট্র","ইউরোপ","ভারত","পাকিস্তান","মধ্যপ্রাচ্য","এশিয়া","আফ্রিকা","লাতিন আমেরিকা","বিশ্ব","চীন") and len(BD.findall(text)) < 2
    digest = re.search(N("সারা দিনের খবর|আলোচিত \\S+ খবর|একনজরে|সংক্ষিপ্ত বিশ্ব"), d.get("headline") or "")
    if (kinds >= 3 or (kinds >= 2 and total >= 4) or (hs and total >= 2)) and s >= 8: level = "core"
    elif (kinds >= 2 and total >= 3) or (hs and kinds >= 1): level = "related"
    else: level = "no"
    if foreign_politics or digest: level = "no"
    return level, s, sig, text

if __name__ == "__main__":
    rows = [json.loads(l) for l in open(os.path.join(HERE, "stories.jsonl"))]
    keep = []; lv = collections.Counter()
    for d in rows:
        level, s, sig, text = classify(d)
        lv[level] += 1
        if level == "no": continue
        d2 = dict(d, level=level, score=s, signals=sorted(sig),
                  countries=[c for c, p in COUNTRIES.items() if p.search(text)],
                  topics=[t for t, p in TOPICS.items() if p.search(text)])
        keep.append(d2)
    keep.sort(key=lambda d: d["published"], reverse=True)
    with open(os.path.join(HERE, "migration-stories.jsonl"), "w") as f:
        for d in keep: f.write(json.dumps(d, ensure_ascii=False) + "\n")
    with open(os.path.join(HERE, "index.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["published","level","score","headline","url","section","countries","topics","signals","tags","words","author"])
        for d in keep:
            w.writerow([d["published"][:10], d["level"], d["score"], d["headline"], d["url"], (d["sections"] or [""])[0],
                        "; ".join(d["countries"]), "; ".join(d["topics"]), "; ".join(d["signals"]), "; ".join(d["tags"]),
                        len(d["text"].split()), d["author"]])
    print("all", len(rows), dict(lv))
