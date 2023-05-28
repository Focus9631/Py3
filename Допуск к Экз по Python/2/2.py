import os,hashlib
m = hashlib.md5()
files={}
def getMD5sum(fileName):
    m = hashlib.md5()
    fd = open(fileName, 'rb')
    b = fd.read()
    m.update(b)
    fd.close()
    return m.hexdigest()
def check(folder):
    for f in os.listdir(folder):
        if os.path.isdir(folder+'\\'+f):
            check(folder+'\\'+f)
        else:
            h=getMD5sum(folder+'\\'+f)
            if h in files:
                print (folder+'\\'+f,files[h])
                files[h]=''
            else:
                files[h]=folder+'\\'+f
check(r'D:\IB2\Labs\2\2')
