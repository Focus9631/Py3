import sys,os,shutil,time
a=sys.argv
source=(a[a.index('--source')+1])
days=int(a[a.index('--days')+1])
size=int(a[a.index('--size')+1])
for f in os.listdir(source):
    if not os.path.isdir(source+'\\'+f):
        if os.path.getsize(source+'\\'+f)<size:
            if not os.path.exists(source+'\\Small'):
                os.mkdir(source+'\\Small')
            shutil.move(source+'\\'+f,source+'\\Small\\'+f)
        elif (time.time()/(24*3600)-os.path.getmtime(source+'\\'+f))/(24*3600)>days:
            if not os.path.exists(source+'\\Archive'):
                os.mkdir(source+'\\Archive')
            shutil.move(source+'\\'+f,source+'\\Archive\\'+f)
