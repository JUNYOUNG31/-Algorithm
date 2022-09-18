# 불켜기

from collections import deque
from collections import defaultdict
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
q = deque()
switch = defaultdict(list)
for i in range(M):
    x, y, a, b = map(int, input().split())
    switch[x-1,y-1].append((a-1,b-1))

# print(switch)
def bfs(a, b):
    on = [[0 for _ in range(N)] for _ in range(N)]
    move = [[0 for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    q.append((a, b))
    cnt = 1
    on[a][b] = 1
    while q:                                                  # q 를 반복하느데
        x, y = q.popleft()                                    # 하나를 빼서
        for i, j in switch[x, y]:                             # 그리고 그 불킨 방의 스위치를 돌면서
            if on[i][j] == 0:
                cnt += 1                                       # cnt 증가1
            on[i][j] = 1                                      # 불을 킨다

        for d in range(4):                                    # 그리고 4방향 돌면서
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:                   # 범위안이면
                move[nx][ny] = 1

        for r in range(N):
            for c in range(N):
                if on[r][c] == 1 and move[r][c] == 1 and visited[r][c] == 0:
                    visited[r][c] = 1
                    q.append((r, c))


        # for i in on:
        #     print(i)
    return cnt


ans = bfs(0, 0)
print(ans)