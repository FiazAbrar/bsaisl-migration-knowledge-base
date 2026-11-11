import json
S=[["bmet-permission-kh-rl1527-2023-11-20","BMET","Recruitment permission KH-RL1527-2023-0010414 (M/S T.K. Enterprise, RL1527, Cambodia, 33 construction workers)","yes","2023-11-20"],
["bmet-permission-kh-rl0696-2025-01-13","BMET","Permission to process emigration clearance: Sams Company (RL0696), 18 construction workers for Cambodia","yes","2025-01-12"],
["bmet-permission-kh-rl2648-2025-03-24","BMET","Permission to process emigration clearance: Puspita Overseas (RL2648), 144 construction workers for Cambodia","yes","2025-03-24"],
["bmet-permission-kh-rl2594-2025-06-25","BMET","Permission to process emigration clearance: Fahim Recruiting Agency (RL2594), 96 construction workers for Cambodia","yes","2025-06-25"],
["bmet-permission-kh-rl2527-2025-08-31","BMET","Approval to process emigration clearance: Mongol Global Services Limited (RL2527), 144 workers for Cambodia","yes","2025-08-31"],
["bmet-permission-kh-rl1203-2025-09-11","BMET","Permission to process emigration clearance: SAM International (RL1203), 100 male workers for Cambodia","yes","2025-09-10"]]
P="possibly-outdated"
F=[]
def f(n,c,q,d,nq=None,s=P):
    x={"n":n,"c":c,"q":q,"d":d,"s":s}
    if nq: x["nq"]=True; x["note"]=nq
    F.append(x)
G="garbled Bangla text layer; read from the page image, p.%d"
T="Bangla text stripped from the text layer; read from the page image, p.%d"
a="bmet-permission-kh-rl0696-2025-01-13"; d="2025-01-12"
f(a,"BMET permission (Jan 2025, Sams Company RL0696): 18 male construction workers for North Asian Construction Co. Ltd., Cambodia","Employer name           NORTH ASIAN CONSTRUCTION CO. LTD.",d)
f(a,"BMET permission (Jan 2025): construction worker salary USD 420 a month, contract 2 years","Constructio CONSTRUCTIO      11      420.0",d)
f(a,"BMET permission (Jan 2025, Cambodia): workers aged 20-45; food, housing, transport and medical care free; 8-hour day, 6 days a week; return airfare for leave paid by the employer","বয়স: ২০-৪৫ বছর, খাওয়া, বাসস্থান, যাতায়াত, ও চিকিৎসা ফ্রি, কর্মঘন্টা: ৮ ঘন্টা, সপ্তাহে কর্মদিবস ৬ দিন, ছুটিকালীন বিমানভাড়া উভয়পথ নিয়োগকর্তার",d,G%1)
f(a,"BMET permission conditions (Jan 2025, Cambodia): all costs until arrival in Cambodia (levy, airfare etc.) are borne by the employer; once visa and flight are confirmed the agency may take at most Tk 80,770 from the worker as migration cost, by cheque, bank draft or pay order","কম্বোডিয়ায় পৌঁছার প্রারম্ভে সকল ব্যয় (লেভি, বিমানভাড়া ইত্যাদি) নিয়োগকারী বহন করবেন; কর্মীর ভিসা এবং ফ্লাইট নিশ্চিত হওয়া সাপেক্ষে রিক্রুটিং এজেন্সি কর্তৃক অভিবাসন ব্যয় বাবদ কর্মীর নিকট হতে সর্বোচ্চ ৮০,৭৭০/-(আশি হাজার সাতশত সত্তর টাকা) অর্থ চেক/ব্যাংক ড্রাফট/পে-অর্ডার এর মাধ্যমে গ্রহণ করতে পারবেন",d,G%1)
f(a,"BMET permission conditions (Cambodia): the agency must pick workers from BMET's database (Overseas Employment and Migrants Act 2013, s.19(3))","বৈদেশিক কর্মসংস্থান ও অভিবাসী আইন ২০১৩ এর ১৯(৩) ধারা অনুযায়ী রিক্রুটিং এজেন্সিকে বিএমইটির চলমান ডাটাবেজ থেকে কর্মী নির্বাচন করতে হবে",d,G%1)
f(a,"BMET permission conditions (Cambodia): after each group arrives in Cambodia the agency reports to the Ministry, BMET and the Bangladesh Embassy in Bangkok, Thailand","প্রত্যেক গ্রুপে বাংলাদেশী কর্মী কম্বোডিয়ায় পৌঁছার পর রিক্রুটিং এজেন্সি মন্ত্রণালয়, বিএমইটি এবং বাংলাদেশ দূতাবাস/কনস্যুলেট জেনারেল অব বাংলাদেশ, ব্যাংকক, থাইল্যান্ডে প্রতিবেদন দাখিল করবে",d,G%1)
f(a,"BMET permission conditions (Cambodia): the contract is signed with each worker before clearance, and each worker gets an attested Bangla translation","কর্মী নিয়োগ চুক্তি পত্রের বাংলায় অনুবাদকৃত সত্যায়ন কপি প্রত্যেক কর্মীকে প্রদান নিশ্চিত করতে হবে",d,G%1)
f(a,"BMET permission conditions (Cambodia): approved workers must get the job; if anything goes wrong the agency pays the worker's food and lodging, return airfare and compensation, under a Tk 300 non-judicial stamp undertaking","অনুমোদিত কর্মীরা উক্ত কোম্পানিতে অবশ্যই চাকুরী পাবেন",d,G%1)
f(a,"BMET permission conditions (Cambodia): an agency representative must be at the Cambodian airport to receive the workers on every flight","প্রতি ফ্লাইটে রিক্রুটিং এজেন্সির একজন প্রতিনিধি কর্মীদের সাথে কম্বোডিয়ায় বিমান বন্দরে কর্মীদের গ্রহণ করার জন্য আবশ্যিকভাবে উপস্থিত থাকবেন",d,G%2)
f(a,"BMET permission conditions (Cambodia): once flights are confirmed the agency sends the flight schedule and worker list to the Bangladesh Embassy in Bangkok and to BMET","কর্মীর ফ্লাইট নিশ্চিত হওয়ার পর সংশ্লিষ্ট রিক্রুটিং এজেন্সি কর্তৃক ফ্লাইট সিডিউল ও কর্মীর তালিকা বাংলাদেশ দূতাবাস, ব্যাংকক, থাইল্যান্ডে এবং বিএমইটিতে দাখিল করতে হবে",d,G%2)
f(a,"BMET's Cambodia permission letters are copied to the Counsellor (Labour), Bangladesh Embassy, Bangkok","কাউন্সেলর (শ্রম), বাংলাদেশ দূতাবাস/কনস্যুলেট জেনারেল অব বাংলাদেশ, ব্যাংকক, থাইল্যান্ড",d,G%2)
b="bmet-permission-kh-rl2648-2025-03-24"; d="2025-03-24"
f(b,"BMET permission (24 Mar 2025, Puspita Overseas RL2648): 144 male construction workers for six Phnom Penh employers (Chip Hong Insee Ltd., Sim Sia Cambodia, Sok Hang Group, Vain SR Construction, Phanimex Group); pay USD 420 a month","বেতন ভাতাদি: ৪২০ ইউএসডি",d,G%1)
f(b,"BMET permission (24 Mar 2025, Cambodia): contract 2 years, ages 20-45, 8 hours a day Monday to Saturday","কর্ম ঘন্টা: প্রতিদিন ০৮ ঘন্টা, (সোমবার থেকে শনিবার)",d,G%1)
f(b,"BMET permission (24 Mar 2025): migration cost for Cambodia Tk 80,770","৮০,৭৭০/- (আশি হাজার সাতশত সত্তর)",d,G%1)
f(b,"Employer named in the Mar 2025 Cambodia letter: Chip Hong Insee Ltd., 137 Mao Tse Toung Blvd, Phnom Penh","Chip Hong Insee Ltd.",d,G%1)
c="bmet-permission-kh-rl2594-2025-06-25"; d="2025-06-25"
f(c,"BMET permission (25 Jun 2025, Fahim Recruiting Agency RL2594): 96 construction workers for China State Construction (Cambodia) Co. Ltd. and Asbic Construction Company Ltd., Phnom Penh; USD 420; migration cost Tk 1,05,000","অভিবাসন ব্যয় ১,০৫,০০০/- (এক লক্ষ পাঁচ হাজার) টাকা",d,"PDF has no text layer; read from the page image, p.1")
f(c,"BMET permission (Jun 2025, Cambodia): the employer pays the visa fee in advance and later deducts it from the worker's salary","ভিসা ফি নিয়োগকর্তা অগ্রীম পরিশোধ করবে এবং পরবর্তীতে কর্মীর বেতন থেকে তা কর্তন করবে",d,"PDF has no text layer; read from the page image, p.1")
c2="bmet-permission-kh-rl2527-2025-08-31"; d="2025-08-31"
f(c2,"BMET approval (31 Aug 2025, Mongol Global Services RL2527): 144 male construction workers for three Phnom Penh firms; USD 420; migration cost Tk 1,55,450","১,৫৫,৪৫০/- (এক লক্ষ পঞ্চান্ন হাজার চারশত পঞ্চাশ) টাকা",d,T%1)
f(c2,"BMET approval (Aug 2025, Cambodia): the employer pays the work permit and visa fees in advance and later deducts them from the worker's salary","ওয়ার্ক পারমিট ও ভিসা ফি নিয়োগকর্তা অগ্রীম পরিশোধ করবেন এবং পরবর্তীতে কর্মীর বেতন থেকে তা কর্তন করবে",d,T%1)
f(c2,"BMET approval conditions (Aug 2025, Cambodia): within 3 months of departure the agency must submit the workers' Work Permits to BMET","বহির্গমনের ০৩ (তিন) মাসের মধ্যে সংশ্লিষ্ট রিক্রুটিং এজেন্সি কর্মীদের Work Permit BMET বরাবরে দাখিল করবে",d,T%1)
f(c2,"Employers named in the Aug 2025 Cambodia approval include Xin Caifu (Cambodia) Co., Ltd., Sangkat Chom Chao II, Khan Por Sen Chey, Phnom Penh","XIN CAIFJ (COMBODIA) CO.,",d)
e="bmet-permission-kh-rl1203-2025-09-11"; d="2025-09-10"
f(e,"BMET permission (10 Sep 2025, SAM International RL1203): 100 male construction workers for four Phnom Penh firms; USD 420; 2 years; migration cost Tk 80,770","৮০,৭৭০/- (আশি হাজার সাতশত সত্তর) টাকা",d,T%1)
f(e,"Employers in the Sep 2025 letter include Royal Bengol Engineering and Constructors Co. Ltd., Trapeang Krasang, Posen Chey, Phnom Penh","Royal Bengol",d)
f(e,"BMET permission conditions (Sep 2025, Cambodia): after starting work, the agency reports the E type (Business) visa extension and regular salary payment to BMET and the Bangladesh Embassy in Bangkok (labour welfare wing)","কম্বোডিয়ায় কর্মে নিয়োজিত হওয়ার পর E type (Business) ভিসা Extension এবং কর্মীদের নিয়মিত বেতন প্রাপ্তির প্রতিবেদন BMET ও বাংলাদেশ দূতাবাস, ব্যাংকক (শ্রম কল্যাণ উইং), থাইল্যান্ড বরাবরে দাখিল করবে",d,T%2)
f(e,"BMET permission conditions (Sep 2025, Cambodia): the agency must inform the Ministry and BMET within 14 days of completing the recruitment","এ নিয়োগ সম্পন্ন করে ১৪ দিনের মধ্যে প্রবাসী কল্যাণ ও বৈদেশিক কর্মসংস্থান মন্ত্রণালয় ও বিএমইটিকে অবহিত করতে হবে",d,T%2)
f(e,"BMET permission conditions (Sep 2025, Cambodia): an agency representative flies with the workers or receives them at the Cambodian airport on every flight","প্রতি ফ্লাইটে রিক্রুটিং এজেন্সির একজন প্রতিনিধি কর্মীদের সাথে কম্বোডিয়া যাবেন অথবা কম্বোডিয়া বিমানবন্দরে একজন প্রতিনিধি কর্মীদের গ্রহণ করার জন্য উপস্থিত থাকবেন",d,T%2)
f(e,"BMET permission conditions (Sep 2025, Cambodia): the agency must take the migration cost only by cheque, bank draft or pay order once visa and flight are confirmed, and submit proof to BMET's Director General","কর্মীর ভিসা এবং ফ্লাইট নিশ্চিত হওয়া সাপেক্ষে রিক্রুটিং এজেন্সি কর্তৃক অভিবাসন ব্যয়বাবদ নির্ধারিত অর্থ চেক/ব্যাংক ড্রাফট/পে-অর্ডার এর মাধ্যমে গ্রহণ করতে পারবেন",d,T%2)
g="bmet-permission-kh-rl1527-2023-11-20"; d="2023-11-20"
f(g,"BMET permission (20 Nov 2023, T.K. Enterprise RL1527): 33 construction workers for Rafa Construction Co. Ltd., Phnom Penh; visa attested","Employer name           RAFA CONSTRUCTION CO. LTD.",d)
f(g,"BMET permission (Nov 2023): 33 construction workers at USD 420 a month, 2-year contract","Constructio CONSTRUCTIO      33      420.0",d)
json.dump({"prefix":"B","sources":S,"facts":F},open("b3.json","w",encoding="utf-8"),ensure_ascii=False,indent=0)
print(len(F))
