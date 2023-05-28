def frange(a,b,c):
    while a<b:
        yield a
        a+=c
for i in frange(1,5,0.1):
    print(i)
