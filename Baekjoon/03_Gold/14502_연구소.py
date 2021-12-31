# 연구소

# 인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고,
# 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.
# 연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다.
# 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
# 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다.
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

# 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
# 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다.
# 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
# 빈 칸의 개수는 3개 이상이다.
from collections import deque
import copy

dr = [1, 0, -1, 0]                      # 하좌상우
dc = [0, -1, 0, 1]


def bfs():                              # bfs 함수
    queue = deque()
    for i in range(N):
        for j in range(M):
            if land[i][j] == 2:
                queue.append((i, j))
    while queue:                        # q 가 있으면
        r, c = queue.popleft()          # pop 하고
        for d in range(4):              # 방향 정해서
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and land[nr][nc] == 0:  # 값이 0 일때
                land[nr][nc] = 2                                   # 바이러스 확산
                queue.append((nr, nc))                             # q 에 추가 하고


def wall(cnt):
    global max_cnt
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if land[i][j] == 0:
                land[i][j] = 1
                wall(cnt + 1)
                land[i][j] = 0


N, M = map(int, input().split())
land = []
for i in range(N):
    l = list(map(int, input().split()))
    land.append(l)
wall(0)

max_cnt = 0

