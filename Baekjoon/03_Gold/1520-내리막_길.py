# 내리막 길

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
cnt = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cnt[M-1][N-1] = 1


def dfs(x, y):
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= ny < M and 0 <= nx < N:
            if graph[ny][nx] < graph[y][x]:
                if cnt[ny][nx] == 0:
                    if visited[ny][nx] == 0:
                        dfs(nx, ny)
                    visited[ny][nx] = 1
                cnt[y][x] += cnt[ny][nx]


dfs(0, 0)
ans = cnt[0][0]
print(ans)
for i in graph:
    print(i)
print('--------------------')
for i in cnt:
    print(i)
print('--------------------')
for i in visited:
    print(i)

