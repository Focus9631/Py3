alpha = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
s = input().strip()
res = ''
res1 = ''
for c in s:
    res += alpha[(alpha.index(c) + n) % len(alpha)]
print('Result: "' + res + '"')
for c in res:
    res1 += alpha[(alpha.index(c) - n) % len(alpha)]
print('Decode: "' + res1 + '"')
