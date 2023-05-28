pas=input('')
a='qwertyuiopasdfghjklzxcvbnm'
c='123456789'
k=0
j=[]
k+=len(pas)
k+=len(set(pas))
if (a.find(pas)!=-1) or (c.find(pas)!=-1) or (a[::-1].find(pas)!=-1) or (c[::-1].find(pas)!=-1):
    k=0
for i in pas:
    if i.islower() and 1 not in j:
        j.append(1)
    elif i.isupper() and 2 not in j:
        j.append(2)
    elif i.isdigit() and 3 not in j:
        j.append(3)
    elif not i.isalnum() and 4 not in j:
        j.append(4)
if len(j)==2 and k>20:print('хороший пароль')
elif len(j)>=3 and k>20:print('отличный пароль')
elif k<=20:print('плохой пароль')
