# 빙산
from collections import deque

N, M = map(int, input().split())
arr = []
for i in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


# 빙산의 개수 체크
def ice(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and arr[nx][ny] != 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


# 그리고 빙산 깍기
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                if arr[nx][ny] == 0 and arr[x][y] > 0:
                    arr[x][y] -= 1
                if arr[nx][ny] > 0:
                    visit[nx][ny] = 1
                    q.append((nx, ny))


time = 0
while 1:
    visit = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0
    # 빙산 녹이기
    # 음 그냥 돌리면 안되니까 위치를 체크하고 나중에 바다의 개수만큼 빼야할듯
    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0 and arr[i][j] != 0:
                bfs(i, j)

    # 빙산의 개수
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and arr[i][j] != 0:
                ice(i, j)
                cnt += 1

    # 1년 +
    time += 1
    if cnt >= 2:
        print(time)
        exit()

    # 다녹아도 안빠져나가면 0을 출력
    flag = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                flag = 1
    if flag == 0:
        print(0)
        exit()