# 감시

# 스타트링크의 사무실은 1×1크기의 정사각형으로 나누어져 있는 N×M 크기의 직사각형으로 나타낼 수 있다.
# 사무실에는 총 K개의 CCTV가 설치되어져 있는데, CCTV는 5가지 종류가 있다. 각 CCTV가 감시할 수 있는 방법은 다음과 같다.
# 1번 CCTV는 한 쪽 방향만 감시할 수 있다. 2번과 3번은 두 방향을 감시할 수 있는데, 2번은 감시하는 방향이 서로 반대방향이
# 어야 하고, 3번은 직각 방향이어야 한다. 4번은 세 방향, 5번은 네 방향을 감시할 수 있다.
# CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시할 수 있다. 사무실에는 벽이 있는데, CCTV는 벽을 통과할 수 없다.
# CCTV가 감시할 수 없는 영역은 사각지대라고 한다.
# CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향으로 해야 하며, 감시하려고 하는 방향이 가로 또는 세로 방향이어야 한다.
# 사무실의 크기와 상태, 그리고 CCTV의 정보가 주어졌을 때, CCTV의 방향을 적절히 정해서, 사각 지대의 최소 크기를 구하는 프로그램을 작성하시오.
from copy import deepcopy

dx = [1, 0, -1, 0]  # 우 상 좌 하
dy = [0, -1, 0, 1]
direction = [[],
            [[0],[1] ,[2], [3]]   ,
            [[0, 2], [1, 3]]       ,
            [[0, 1], [1, 2], [2, 3], [3, 0]]   ,
            [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]] ,[[0, 1, 2, 3]]      ]


def dfs(room, cnt):
    copy_room = deepcopy(room)          # 복사하기
    global ans              
    if cnt == cctv_cnt:         # cctv 수 맞춰서 탈출
        dark_num = 0            # 0의 개수
        for i in range(N):          
            for j in range(M):
                if copy_room[i][j] == 0: # 완탐해서 0이면
                    dark_num += 1        # 1 증가
        ans = min(ans, dark_num)        # 최솟값 저장
        # for i in range(N):
        #     print(room[i])
        return

    x, y, = cctv[cnt]               # x,y 좌표
    num = room[x][y]                # cctv 번호
    for i in direction[num]:        # 방향의 개수 찾기
        check(x, y, copy_room, i)       # 0 체크
        dfs(copy_room, cnt + 1)         # dfs 추가로 
        copy_room = deepcopy(room)      # 원상복구


def check(x, y, room, d):        # 체크 하기
    for i in d:            # 방향에 따라서
        nx = x
        ny = y
        while True:
            nx += dx[i]   # 방향바꿔주고
            ny += dy[i]
            if 0 <= nx < N and 0 <= ny < M:    # 범위안이고
                if room[nx][ny] == 0:          #  0이면
                    room[nx][ny] = "#"         # # 표시
                elif room[nx][ny] == 6:        # 6이면
                    break                      # 멈춰
            else:           # 범위 밖이면 
                break        # 멈춰


N, M = map(int, input().split())
room = [[int(i) for i in input().split()] for _ in range(N)]
cctv = []
cctv_cnt = 0
ans = 987654321

# visited = [[0] * M for _ in range(N)]       # 방문처리?
for i in range(N):
    for j in range(M):
        if room[i][j] != 0 and room[i][j] != 6:   # 0 아니고 6아니면
            cctv.append([i, j])         # cctv좌표 추가
            cctv_cnt += 1               # cctv 개수 증가


# for i in range(N):
#     print(room[i])
dfs(room, 0)        # dfs 돌기

print(ans)

# cctv 1

# cctv 2

# cctv 3

# cctv 4

# cctv 5
