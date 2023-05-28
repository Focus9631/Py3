import re
qwe = input("Введите название файла ")
with open (qwe, "r") as file:
    q = file.read()
    artem = re.findall(r'\d{1,3}\b[.]\d{1,3}\b[.]\d{1,3}\b[.]\d{1,3}', q)
    sanya=re.findall(r'[(]\d{3}\b[)]\d{7}|[(]\d{3}\b[)]\d{3}-\d{2}-\d{2}', q)
    print('artem= ',artem)
    print('sanya= ',sanya)

