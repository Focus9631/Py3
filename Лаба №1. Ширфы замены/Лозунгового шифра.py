alpharus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
key = input('Слово-ключ:').lower()
text = input('Шифруемое слово:').lower()
nkey = ''
for i in range(len(key)):
    if nkey.find(key[i]) == -1 and key[i] != ' ':
        nkey += key[i]
alpha = alpharus
for i in nkey:
    alpha = alpha.replace(i, '')
alpha = nkey + alpha
en = ''
de = ''
for i in text:
    en += alpha[alpharus.index(i)]
print('Зашифрованое слово: ' + en)
for i in en:
    de += alpharus[alpha.index(i)]
print('Дешифрованое слово: ' + de)
