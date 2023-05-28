from random import seed,randint
import datetime
c=[i for i in range(1,17)]
dates=['14/09/2016','28/09/2016','12/10/2016']
matches=[[],[],[]]
seed()
d=randint(0,2)
a=[[],[],[],[]]
for i in a:
    for x in range(4):
        b=randint(0,len(c)-1)
        i.append(c[b])
        c.pop(b)
for i in a:
    print(1)
    for q in range(len(i)):
        for w in range(q+1,len(i)):
            while i[q] in matches[d] or i[w] in matches[d]:
                d=randint(0,2)
            print('%s vs %s at %s, %H:%M' %(i[q],i[w],dates[d],randint(12,23),randint(0,60)))
            matches[d].extend([i[q],i[w]])
