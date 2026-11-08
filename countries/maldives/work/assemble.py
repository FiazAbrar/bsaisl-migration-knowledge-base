import os,re,sys
D=r"C:/Users/User/Desktop/Github/bsaisl-migration-knowledge-base/countries/maldives/drafts/"
def L(x,a,b):
    t=open(D+x+"-findings.md",encoding="utf-8").read().splitlines()
    return "\n".join(t[a-1:b]).strip("\n")+"\n"
parts=[]
P=parts.append
P("# Maldives: migration guide\n\n<<INTRO>>\n\n## Background\n\n### In one minute\n\n<<ONEMINUTE>>\n")
P(L("N",9,56))          # Is it open now ... What closed it before
P(L("N",57,142))        # How a job reaches you; What you pay
P("### What ties you to the employer\n\n<<TIES>>\n")
P(L("N",143,158))       # What goes wrong
P(L("V",7,14))          # Visas not open
P("## Work visa: company worker (construction, resort, shop)\n\n<<W-INTRO>>\n")
P(L("B",15,118).replace("### Work visa: company worker, Step 1:","### Step 1:"))
P("### Step 2: The job offer and contract\n\n<<W-STEP2>>\n")
P("### Step 3: The employer gets your work permit and entry pass\n\n<<W-STEP3>>\n")
P(L("B",120,155).replace("### Work visa: company worker, Step 4:","### Step 4:"))
P("### Step 5: Check your permit and visa are real\n\n<<W-STEP5>>\n")
P(L("B",157,188).replace("### Work visa: company worker, Step 6:","### Step 6:"))
P("### Step 7: After arrival\n\n<<W-STEP7>>\n")
P(L("L",11,102))        # rights
P("### How long you can stay\n\n<<W-STAY>>\n")
P(L("L",104,208))       # jailed, not paid, change employer, leaving
P(L("U",9,34).replace("### (goes under \"Work visa: company worker\") ","### "))
P(L("L",210,219))       # going home on leave
P(L("F",9,15).replace("### (under Work visa: company worker) ","### "))
P(L("N",160,173).replace("### Scams (Work visa: company worker)","### Scams"))
P("## Work visa: professional (teachers, doctors, nurses, engineers)\n\n<<W-PROF>>\n")
P(L("F",158,190))       # domestic
P(L("U",38,99))         # regularisation
P(L("V",16,138))        # tourist
P(L("V",140,166))       # business, meeting
P(L("F",19,65))         # dependent
P(L("F",69,113))        # marriage
P(L("F",117,125))       # resident
P(L("V",168,218))       # student, transit
P(L("V",220,229))       # changing visa type
P(L("F",129,139))       # asylum
P(L("F",143,154))       # child
P(L("G",37,80))         # sending money
P(L("U",104,153))       # going home without papers
P(L("L",223,262))       # dies
P("## Coming home\n\n"+L("G",21,31)+"\n"+L("B",248,256))
P("## High Commission services\n\n"+L("B",192,244))
P("## Contacts\n\n"+L("B",260,274))
txt="\n".join(parts)
txt=re.sub(r"\n---\n","\n",txt)
txt=re.sub(r"\n{3,}","\n\n",txt)
open(r"C:/Users/User/Desktop/Github/bsaisl-migration-knowledge-base/countries/maldives/doc.md","w",encoding="utf-8").write(txt)
print(len(txt.splitlines()))
