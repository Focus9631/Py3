import os,re,shutil
folder=os.path.dirname(os.path.realpath(__file__))+'\\3'
with open(folder+'\\names.txt') as names:
    a=names.readlines()
for i in os.listdir(folder):
    for n in a:
        if re.search(i[:i.rfind('.')],n.strip()):
            e=i[i.rfind('.'):]
            shutil.move(os.path.join(folder,i),os.path.join(folder,n.strip()+e))
