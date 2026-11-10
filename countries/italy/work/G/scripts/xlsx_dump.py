import zipfile, re, sys, xml.etree.ElementTree as ET
ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
z=zipfile.ZipFile(sys.argv[1])
ss=[]
root=ET.fromstring(z.read('xl/sharedStrings.xml'))
for si in root.findall('m:si',ns):
    ss.append(''.join(t.text or '' for t in si.iter('{%s}t'%ns['m'])))
wb=ET.fromstring(z.read('xl/workbook.xml'))
names=[s.get('name') for s in wb.find('m:sheets',ns)]
pat=sys.argv[2] if len(sys.argv)>2 else None
out=[]
for i,nm in enumerate(names,1):
    sh=ET.fromstring(z.read(f'xl/worksheets/sheet{i}.xml'))
    out.append(f'=== SHEET {nm}')
    for r_i,row in enumerate(sh.iter('{%s}row'%ns['m'])):
        vals=[]
        for c in row.findall('m:c',ns):
            v=c.find('m:v',ns); t=c.get('t')
            if v is None:
                isel=c.find('m:is',ns)
                vals.append(''.join(x.text or '' for x in isel.iter('{%s}t'%ns['m'])) if isel is not None else ''); continue
            val=v.text
            if t=='s': val=ss[int(val)]
            vals.append(val)
        line=' | '.join(vals)
        if r_i<12 or (pat and re.search(pat,line,re.I)):
            out.append(line)
print('\n'.join(out))
