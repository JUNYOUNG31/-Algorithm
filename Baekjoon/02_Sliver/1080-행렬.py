# 행렬

N, M = map(int, input().split())
A = []
B = []
for i in range(N):
    temp = list(map(int, input().rstrip()))
    A.append(temp)
for i in range(N):
    temp = list(map(int, input().rstrip()))
    B.append(temp)
cnt = 0


def reversed(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            A[x][y] = 1 - A[x][y]


for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            reversed(i, j)
            cnt += 1
        if A == B:
            break
    if A == B:
        break

if A != B:
    print(-1)
else:
    print(cnt)