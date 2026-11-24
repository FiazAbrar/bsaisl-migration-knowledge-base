import json,sys
d=json.load(open(sys.argv[1],encoding='utf-8'))
open(sys.argv[2],'w',encoding='utf-8').write(d['markdown'])
