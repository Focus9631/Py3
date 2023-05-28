a=(input('Введите слова с клавиатуры:')).split()
for i in a:
    if len(i) > 7:
        print(i)
for i in a:
    if len(i) in range(4, 8):
        print(i)
for i in a:
    if len(i) < 4:
        print(i)

