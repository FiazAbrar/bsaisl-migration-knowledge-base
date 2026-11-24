import subprocess,os
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/..')
F=['python','../../../../tools/facts.py','add','--prefix','G']
q1=open('sources/bb-fx-rate-sheet-2026-11-10.txt',encoding='utf-8').read()
i=q1.find('Weighted Average Exchange Rate'); j=q1.find('124.4200')+8
r=subprocess.run(F+['--name','bb-fx-rate-sheet-2026-11-10','--claim','Bangladesh Bank weighted average exchange rate on 10 November 2026: USD 1 = Tk 124.42','--quote',q1[i:j],'--page-date','2026-11-10','--status','verified','--visa','all','--field','usd_bdt_rate_2026_11_10','--value','124.42'],capture_output=True,text=True,encoding='utf-8');print(r.stdout,r.stderr)
q2=open('sources/bb-remittance-cost-italy.txt',encoding='utf-8').read()
i=q2.find('Italy                                    2.51'); j=q2.find('1.57',i)+4
r=subprocess.run(F+['--name','bb-remittance-cost-italy','--claim','Average cost of sending up to USD 200 from Italy to Bangladesh: 1.36% in January-March 2026 and 1.57% in April-June 2026 (Bangladesh Bank)','--quote',q2[i:j],'--page-date','2026-07','--status','verified','--note','Text layer shifts Table 2 values down one row (Italy label sits on Singapore values); the PDF image shows Italy 1.36 / 1.57, which is the next value line'],capture_output=True,text=True,encoding='utf-8');print(r.stdout,r.stderr)
