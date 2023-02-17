# N Queen
# pypy로 하면 맞음

N = int(input())
ans = 0
row = [0] * N


def is_promising(x):
    for i in range(x):
        # row[i] = j 퀸을 [i, j]에 위치
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def n_queens(x):
    global ans
    if x == N:
        ans += 1
        return
    else:
        for i in range(N):
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)


n_queens(0)
print(ans)