a = input()
f = a.find('f')
s = a[f + 1:].find('f')
if f == -1:
    print(-2)
elif s == -1:
    print(-1)
else:
    print(f + s + 1)

