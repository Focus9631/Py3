print("=== Задание 3: Однозвучный подстановочный шифр ===") 
original = list(input("Введите исходное сообщение: ")) 
 
table = { 
"a": ['10','78','45',0], "b": ['46','25','75',0], "c": ['34','40','09',0], "d": ['65','76','41',0], "e": ['56','35','03',0], 
"f": ['06','66','17',0], "g": ['02','39','13',0], "h": ['58','62','31',0], "i": ['16','73','71',0], "j": ['07','52','64',0], 
"k": ['27','44','60',0], "l": ['67','63','24',0], "m": ['19','42','53',0], "n": ['74','49','26',0], "o": ['57','70','43',0], 
"p": ['55','32','18',0], "q": ['15','36','08',0], "r": ['12','01','48',0], "s": ['30','61','77',0], "t": ['47','21','33',0], 
"u": ['22','04','51',0], "v": ['50','72','28',0], "w": ['23','29','05',0], "x": ['69','38','59',0], "y": ['68','11','20',0], 
"z": ['37','54','14',0] 
} 
 
def encryption(): 
    global code 
for i in original: 
if ord(i) >= 97 and ord(i) <= 122: 
index = table[i][3] 
code += table[i][index] 
table[i][3] = (index + 1) % 3 
else: 
code += i 
 
def decryption(start, end): 
 
global original 
for letter in range(97, 123): #Проход по ячейкам словаря 
for i in range(3): #Проход внутри ячеек 
if table[chr(letter)][i] == code[start:end]: 
original += chr(letter) 
decryption(start + 2, end + 2) 
if end > len(code) - 1: 
break 
 
code = "" 
encryption() 
 
print("\n\n=== Произведено шифрование ===") 
print("Зашифрованное сообщение: " + code) 
 
start = 0 
end = 2 
original = "" 
decryption(start, end) 
 
print("\n\n=== Произведено дешифрование ===") 
print("Исходное сообщение: " + original)
