# lcs 2

import sys
sys.setrecursionlimit(10**6)


X = list(str(input()))
Y = list(str(input()))


def lcs(x, y): # dp
    x, y = [' '] + x, [' '] + y
    m, n = len(x), len(y)
    c = [[0 for _ in range(n)] for _ in range(m)]
    d = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1] + 1
                d[i][j] = 1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])
                d[i][j] = 2 if (c[i][j-1] > c[i-1][j]) else 3

    for i in c:
        print(i)
    print()
    for i in d:
        print(i)
    return c, d


def get_lcs(i, j, d, x):
    if i == 0 or j == 0:
        return ""
    else:
        if d[i][j] == 1:     # 대각으로 가기 == 공통 부분 원소
            return get_lcs(i-1, j-1, d, x) + x[i]
        elif d[i][j] == 2:   # 옆으로
            return get_lcs(i, j-1, d, x)
        elif d[i][j] == 3:   # 위로roy
            return get_lcs(i-1, j, d, x)


c, d = lcs(X,Y)
ans = get_lcs(len(X), len(Y), d, [' '] + X)
print(c[-1][-1])
print(ans)