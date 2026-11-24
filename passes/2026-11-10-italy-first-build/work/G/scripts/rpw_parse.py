import re,sys
t=open(sys.argv[1],encoding='utf-8').read()
blocks=t.split('[Firm](https://remittanceprices.worldbank.org/corridor/Italy/Bangladesh?order=title&sort=asc#tab-1)')
for b in blocks[1:]:
    L=[x.strip() for x in b.split('\n') if x.strip()]
    if not L or L[0].startswith('Payment instrument') : 
        if 'Total Average' in b: print('AVG', re.findall(r'Total Average[^|]*',b)[:3])
        continue
    name=L[0]
    ftype=next((x for x in L if x.startswith('Firm type')),'')
    def after(lbl):
        for i,x in enumerate(L):
            if x.startswith(lbl): return L[i+1]
        return ''
    speed=re.findall(r'speed_actual/([a-z_0-9]+)\.png',b)
    recv=re.findall(r'pick_up_method/([a-z_0-9]+)\.png',b)
    pay=re.findall(r'product/([a-z_0-9-]+)\.png',b)
    fee=after('[Fee]'); 
    tot=after('[Total cost (%)]')
    ref=re.findall(r'reference rate ([0-9.]+) and',b)
    print(f"{name} | {ftype[11:]} | pay={pay} access={after('Access point')} | speed={speed} | recv={recv} | fee={fee} | total%={tot} | ref={ref}")
