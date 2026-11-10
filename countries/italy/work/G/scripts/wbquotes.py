import sys,re
sys.path.insert(0,'../../../../tools')
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/..')
from facts import norm
t=norm(open('sources/worldbank-rpw-italy-bangladesh.md',encoding='utf-8').read())
for firm,end in [('poste italiane via western union','total cost (%) 2.982.98'),('janata exchange company','total cost (%) 4.814.81'),('national exchange company firm type','total cost (%) 4.574.57'),('poste italiane via moneygram','total cost (%) 5.465.46'),('extrabanca','total cost (%) 22.2422.24'),('banca intesa sanpaolo','total cost (%) 33.5733.57')]:
    i=t.find(firm); j=t.find(end,i)
    print(firm, i, j, j-i); print(repr(t[i:j+len(end)][:900])); print()
for k in ['data collected on: aug 08, 2025 - sep 03, 2025','total average third quarter 2025 9.559.55','total average third quarter 2025 6.346.34','140.00 eur200.00 usd','345.00 eur500.00 usd','market reference rate 146.78']:
    print(k, k in t)
