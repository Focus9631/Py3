def ces(i,x):
    i += 1
    code = ''
    for j in x:
        if j.isalpha():
            code += chr(ord(j)+i)
        else:
            code += j
    return code
with open('hello.txt') as fil:
    for i,x in enumerate(fil.readlines()):
        print(ces(i,x))
