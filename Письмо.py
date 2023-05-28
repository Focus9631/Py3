n = 13
a = [[0] * n for i in range(n)]

for i in range(n):
    for j in reversed (range(0, i)):
        a[j][i] = 2
    for j in range(n):
        a[i][j] = 1
        a[n-i-1][i] = 1
    for j in range(i + 1, n):
        a[i][j] = 0
for row in a:
    print(' '.join([str(elem) for elem in row]))
