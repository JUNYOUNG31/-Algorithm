# LCS

def lcs1(x, y): # 재귀적
    m, n = len(x), len(y)
    if m == 0 or n == 0:
        return 0
    else:
        if x[-1] == y[-1]:
            return lcs1(x[:(m-1)], y[:(n-1)]) + 1
        else:
            return max(lcs1(x[:m], y[:(n-1)]), lcs1(x[:(m-1)], y[:n]))


def lcs2(x, y): # dp
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
    return c, d


def get_lcs(i, j, d, x):
    if i == 0 or j == 0:
        return ""
    else:
        if d[i][j] == 1: # 대각으로 가기 == 공통 부분 원소
            return get_lcs(i-1, j-1, d, x) + x[i]
        elif d[i][j] == 2: # 옆으로
            return get_lcs(i, j-1, d, x)
        elif d[i][j] == 3: # 위로
            return get_lcs(i-1, j, d, x)
