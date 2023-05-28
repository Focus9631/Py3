bank={1000:5,500:4,100:3,50:1,10:2}
n=int(input(''))
s=''
for k in bank.keys():
    i=n//k
    if i>0:
        bank[k]-=i
        n-=i*k
        s+=('+ %d * %d'%(i,k))
if n>0: print('Операция не может быть выполнена')
else: print(s[1:])
