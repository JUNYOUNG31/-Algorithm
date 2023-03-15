# 음식물 피하기

import sys
sys.setrecursionlimit(1000000)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ans = []

for i in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1


def dfs(x, y):
    global num
    num += 1
    visited[x][y] = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                dfs(nx, ny)
    return num


for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            num = 0
            ans.append(dfs(i, j))

print(max(ans))