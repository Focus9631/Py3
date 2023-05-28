import re
with open(input('')+'.txt') as f:
    a=f.readlines()
for i in range(len(a)):
    s=re.findall('\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}',a[i])
    if s: print(i,' ',' '.join(s))

