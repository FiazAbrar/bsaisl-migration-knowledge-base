import re,sys
src=open('saudi-ref-list.md').read()
ref=src.split('## References')[1]
off,news=ref.split('### Needs an official source')
O={m.group(1):m.group(2) for m in re.finditer(r'^(\d+)\. (.*)$',off,re.M)}
N_extra=('30','Daily Ittefaq, 31 May 2025. [Saudi visa suspended for 14 countries including Bangladesh](https://en.ittefaq.com.bd/12131/saudi-visa-suspended-for-14-countries-including)')
O['43']='MHRSD. [MHRSD signs memorandum with Takamol for Business Services](https://www.hrsd.gov.sa/en/media-center/news/74125800)'
N={m.group(1):m.group(2) for m in re.finditer(r'^- N(\d+)\. (.*)$',news,re.M)}
N[N_extra[0]]=N_extra[1]
N['33']=O['32']
O['44']='Gulf Health Council. [ghc.sa](https://ghc.sa/en/)'
N['31']='Gulf News, 21 Jan 2023, citing MHRSD and Labour Law Article 40. [Expat workers\' fees must be borne by employer](https://gulfnews.com/world/gulf/saudi/saudi-arabia-all-expat-workers-fees-must-be-borne-by-employer-1.93366924)'
N['32']='Gulf News, 2020. [Domestic workers excluded from labour reforms](https://gulfnews.com/world/gulf/saudi/saudi-arabia-domestic-workers-excluded-from-labour-reforms-1.75073670)'
from refs_extra import O2,N2
assert not set(O2)&set(O),'O clash'
assert not set(N2)&set(N),'N clash'
O.update(O2); N.update(N2)
def yr(t):
    m=re.search(r'\b(19|20)(\d\d)\b',t.split('[')[0]); return int(m.group(0)) if m else None
def tag(t):
    y=yr(t); return ' (%d)'%y if y and y<2025 else ''
def build(inp,out):
    s=open(inp).read()
    om,nm=[],[]
    def rep(m):
        out=[]
        for k in [x.strip() for x in m.group(1).split(',')]:
            if k.startswith('N'):
                k=k[1:]; assert k in N,k
                if k not in nm: nm.append(k)
                out.append('[N%d%s](#n%d)'%(nm.index(k)+1,tag(N[k]),nm.index(k)+1))
            else:
                assert k in O,k
                if k not in om: om.append(k)
                out.append('[%d%s](#o%d)'%(om.index(k)+1,tag(O[k]),om.index(k)+1))
        return '\\['+', '.join(out)+'\\]'
    s=re.sub(r'\[((?:N?\d+)(?:, ?N?\d+)*)\](?!\()',rep,s)
    s+='\n## References\n\n### Official sources\n\n'+''.join('%d. []{#o%d}%s\n'%(i+1,i+1,O[k]) for i,k in enumerate(om))
    if nm:
        s+='\n### Needs an official source\n\nThese facts come only from news or third-party sites. Each needs an official source, or a reviewer\'s confirmation, before the Navigator uses it.\n\n'+''.join('- []{#n%d}N%d. %s\n'%(i+1,i+1,N[k]) for i,k in enumerate(nm))
    import unicodedata
    heads=re.findall(r'^## (.+)$',s,re.M)
    def slug(h):
        h=re.sub(r'[^\w\s-]','',h.lower()).strip(); return re.sub(r'\s+','-',h)
    toc='## Contents\n\n'+''.join('- [%s](#%s)\n'%(h,slug(h)) for h in heads)+'\n'
    i=s.index('\n## ')+1; s=s[:i]+toc+s[i:]
    open(out,'w').write(s); print(out,len(om),len(nm))
build('saudi.src.md','Saudi Arabia.md')
#build('lb.src.md','Leaving Bangladesh.md')
