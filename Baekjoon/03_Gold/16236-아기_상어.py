# 아기 상어

# N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다.
# 한 칸에는 물고기가 최대 1마리 존재한다.아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다.
# 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.
# 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.아기 상어는 자신의
# 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
# 아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.
# 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
# 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
# 아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 즉, 아기 상어가 먹을 수 있는 물고기가
# 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.
# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
# 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다. 공간의 상태가 주어졌을 때,
# 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.
from collections import deque
dx = [0, 0, -1, 1]  #  상 좌 하 후
dy = [-1, 1, 0, 0]

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

shark = []
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            shark = [i, j]


time = 0
shark_size = 2

def bfs(r, c):
    q = deque()
    q.append([r, c, 0])  # 위치랑 거리
    visited = [[0] * N for _ in range(N)]  # 방문처리
    visited[r][c] = 1
    eat = []
    while q:
        r, c, cnt = q.popleft()     # 팝
        for i in range(4):          # 4방향 탐색
            nx = r + dx[i]
            ny = c + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:  # 범위안에 있고 방문안하고
                if sea[nx][ny] <= shark_size:       # 상어가 더 크면
                    q.append([nx, ny, cnt+1])       # q에 추가하고
                    visited[nx][ny] = 1             # 방문처리하고
                    if sea[nx][ny] < shark_size and sea[nx][ny] != 0:   # 상어가 더크고 0 이 아니면
                        eat.append([nx, ny, cnt+1])     #먹어
    # for c in range(len(visited)):
    #     print(visited[c])
    return eat

eat_cnt = 0

while True:
    ans = bfs(shark[0], shark[1])     # 상어 위치부터 돌려
    ans.sort(key=lambda x: (x[2], x[0], x[1]))
    # for i in range(len(ans)):
    #     print(ans[i])
    if len(ans) == 0:  # 먹이없음
        break
    eat_cnt += 1  # 물고기 먹은횟수
    sea[ans[0][0]][ans[0][1]] = 0  # 먹은 물고기 0으로 변경

    time += ans[0][2]       # 이동거리 = 시간추가

    sea[shark[0]][shark[1]] = 0  # 처음 상어 위치 0으로 주고
    shark = [ans[0][0], ans[0][1]]  # 상어 위치 갱신하고

    if eat_cnt == shark_size:  # 물고기 먹은수랑 상어크키랑 비교해서
        shark_size += 1        # 상어 크기 늘리고
        eat_cnt = 0            # 먹은 수 초기화

print(time)
