# 벽부수고 이동하기

import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()


def bfs(a, b):
    queue.append([a, b, 0])   # 좌표 , 벽뿌
    while queue:
        x, y, cnt = queue.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][cnt]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny][cnt] == 0 and wall[nx][ny] == 0:
                    visited[nx][ny][cnt] = visited[x][y][cnt]+1
                    queue.append((nx, ny, cnt))
                elif visited[nx][ny][cnt] == 0 and cnt < K and wall[nx][ny] == 1:
                    visited[nx][ny][cnt+1] = visited[x][y][cnt] + 1
                    queue.append([nx, ny, cnt+1])
    return -1


N, M, K = map(int, input().split())
wall = [list(map(int, list(input().strip()))) for _ in range(N)]
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1  # 시작도 1로 한다
print(bfs(0, 0))
# for i in wall:
#     print(i)
#
# for i in visited:
#     print(i)
