import hashlib
import os

unique = dict()
for root, dirs, files in os.walk("E:\Универ\Python PROG\Допуск к Экз по Python\Лаба Шарий 2(2)"):
    for file in files:
        path = os.path.join(root, file)
        if os.path.isfile(path):
            filehash = hashlib.md5(open(path, 'rb').read()).hexdigest()
            print(filehash)
            if filehash not in unique:
                unique[filehash] = path
            else:
                print(path + ' is a duplicate of ' + unique[filehash])
