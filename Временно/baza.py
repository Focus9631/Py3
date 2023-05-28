q={'surname':{},'car':{},'number':{}}
n=int(input('Введите количество добавляемых объектов '))
for i in range(n):
    q['surname'][i]=input('Введите фамилию ')
    q['car'][i]=input('Марка ')
    q['number'][i]=input('Номер ')
    print (q['surname'][i])
    print (q['car'][i])
    print ( q['number'][i])
    a=sorted(q.items())
print(a)


