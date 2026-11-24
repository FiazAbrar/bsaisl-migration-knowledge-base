import sys
home=set(l.strip() for l in open(sys.argv[1],encoding='utf-8'))
for f in sys.argv[2:]:
    print("=====",f)
    for l in open(f,encoding='utf-8'):
        s=l.strip()
        if s and s not in home: print(s)
