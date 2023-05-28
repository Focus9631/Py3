S=input('Строка:')
a=input('Какую букву заменить:')
b=input('На какую:')
S=max(S.split(), key=len)
print(S.replace(a, b))

