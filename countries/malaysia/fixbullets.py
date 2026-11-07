import zipfile,sys,shutil
for f in sys.argv[1:]:
    zin=zipfile.ZipFile(f); tmp=f+'.tmp'; zout=zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED)
    for i in zin.infolist():
        d=zin.read(i.filename)
        if i.filename=='word/numbering.xml': d=d.replace('w:lvlText w:val="–"'.encode(),'w:lvlText w:val="•"'.encode())
        zout.writestr(i,d)
    zout.close(); shutil.move(tmp,f)
