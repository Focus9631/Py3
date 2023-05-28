try:
    a=float(input('a= '))
    if a<0:
        raise Exception
    b=int(a)
    e=int(a*100%100)
    print('{} рублей {} коп.'.format(b,e))
except:
    print('Неправильно!')
