# 인구 이동

# N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며,
# r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1×1 크기이기 때문에,
# 모든 국경선은 정사각형 형태이다. 오늘부터 인구 이동이 시작되는 날이다.
# 인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.
# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
# 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 연합을 해체하고, 모든 국경선을 닫는다.
# 각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.
from collections import deque


N, L, R = map(int, input().split())
nara = [[0] * N for _ in range(N)]
for i in range(N):
    nara[i] = list(map(int, input().split()))

# for i in range(N):
#     print(nara[i])

dx = [1, 0, -1, 0]                     # 우 상 좌 하
dy = [0, -1, 0, 1]
day = 0                                # 이동일
while 1:
    visited = [[0] * N for _ in range(N)]       # 방문처리
    flag = False                                # 빠져나오기
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:              # 방문안했으면
                visited[i][j] = 1               # 방문처리하고
                # queue = deque()                 # q 에 넣고
                # queue.append((i, j))
                queue = deque([(i, j)])
                hap = nara[i][j]                # 인구 더할꺼
                cnt = 1                         # 나라수
                people_avg = [[i, j]]           # 위치
                # print(queue)
                while queue:                    # 반복
                    x, y = queue.popleft()      # 빼고
                    for d in range(4):          # 4방향 탐색
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:    # 범위안이고
                            if L <= abs(nara[x][y] - nara[nx][ny]) <= R:            # 두개의 차
                                visited[nx][ny] = 1                     # 방문처리
                                queue.append((nx, ny))                  # 추가
                                hap += nara[nx][ny]                     # 인구수 더해주고
                                cnt += 1                                # 나라수 더해주고
                                people_avg.append([nx, ny])             # 위치 추가해주고
                if cnt > 1:         # 나라수가 1보다 크면
                    flag = True     # 인구이동 가능
                    for r, c in people_avg:  # 위치 돌면서
                        nara[r][c] = hap // cnt   # 평균값 넣어주고
    if flag == True:               # 이동했으면
        day += 1                   # 날추가하고
    else:           # 아니면
        break       # 멈춰
# for i in range(N):
#     print(nara[i])
print(day)

