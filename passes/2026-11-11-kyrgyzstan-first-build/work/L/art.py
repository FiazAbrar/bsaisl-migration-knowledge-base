import sys,re
sys.stdout.reconfigure(encoding="utf-8")
t=open(sys.argv[1],encoding='utf-8').read()
parts=re.split(r'\n(?=\*\*Статья \d+\\.)',t)
want=set(sys.argv[2].split(','))
for p in parts:
    m=re.match(r'\*\*Статья (\d+)\\.',p)
    if m and m.group(1) in want:
        s=re.sub(r'\n\s*\n','\n',p)
        print(s[:int(sys.argv[3]) if len(sys.argv)>3 else 6000]); print('-----')
