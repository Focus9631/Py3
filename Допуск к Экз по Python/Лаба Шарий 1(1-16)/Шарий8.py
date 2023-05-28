from random import randint
n=randint(1,10000)
for x in range(n):
    if x**2>n:
        break
s=[randint(1,100) if i<n else 0 for i in range(x**2)]
print(s)
