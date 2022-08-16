
import sys
sys.setrecursionlimit(10**6)

X = list(str(input()))
Y = list(str(input()))


def lcs(x, y): # dp
    x, y = [' '] + x, [' '] + y
    m, n = len(x), len(y)
    c = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])
    return c


c = lcs(X,Y)
print(c[-1][-1])