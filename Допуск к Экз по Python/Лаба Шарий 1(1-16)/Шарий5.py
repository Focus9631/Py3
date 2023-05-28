a=(input('Введите слова с клавиатуры:'))
a=a.split()
a=[i.upper() if i.istitle() else i for i in a]
print(' '.join(a))
