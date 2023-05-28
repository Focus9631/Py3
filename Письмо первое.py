n = 7

a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][i] = 1
        a[n-i-1][i] = 1
    for j in range(i + 1, n):
        a[i][j] = 0
    for j in range(0, i):
        a[i][j] = 2


for row in a:
    print(' '.join([str(elem) for elem in row]))
