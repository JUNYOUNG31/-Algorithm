# 영역 구하기

import sys
sys.setrecursionlimit(10 ** 6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
cnt = 0

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1


def dfs(x, y):
    global cnt
    if x < 0 or x >= M or y < 0 or y >= N:
        return 0
    if graph[x][y] == 1:
        return 0
    graph[x][y] = 1
    cnt += 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        dfs(nx, ny)
    return cnt


ans = []
for i in range(M):
    for j in range(N):
        temp = dfs(i, j)
        if temp:
            ans.append(temp)
            cnt = 0

ans.sort()
print(len(ans))

for i in ans:
    print(i, end=' ')