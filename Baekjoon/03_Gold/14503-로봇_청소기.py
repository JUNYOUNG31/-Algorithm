# 로봇 청소기

# 로봇 청소기가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.
# 로봇 청소기가 있는 장소는 N×M 크기의 직사각형으로 나타낼 수 있으며, 1×1크기의 정사각형 칸으로 나누어져 있다.
# 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북중 하나이다.
# 지도의 각 칸은 (r, c)로 나타낼 수 있고, r은 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로 부터 떨어진 칸의 개수이다.
# 로봇 청소기는 다음과 같이 작동한다.
# 현재 위치를 청소한다.
# 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸을 탐색한다.
# 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
# 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
# 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
# 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
# 로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.


dr = [-1, 0, 1, 0]  # 북 서 남 동
dc = [0, -1, 0, 1]

N, M = map(int, input().split())                # 맵의 크기
land = [[] * M for _ in range(N)]               # 맵 입력할 리스트
r, c, d = map(int, input().split())             # 현재위치와 방향

for i in range(N):
    land[i] = list(map(int, input().split()))   # 맵 입력

# for i in range(N):
#     print(land[i])

visited = [[0] * M for _ in range(N)]           # 방문 기록
# land[r][c] = 1    
visited[r][c] = 1                               # 방문처리하고
cnt = 1                                         # 청소한 개수

if d == 1:
    d = 3
elif d == 3:
    d = 1


def left():                                     # 왼쪽으로 돌기
    global d                    
    d += 1                                      # 방향 바꾸기
    if d == 4:                                 # 인덱스 처리
        d = 0


turn = 0                                        # 방향
while True:                                     
    left()                                      # 방향전환
    nr = r + dr[d]                              # 전진
    nc = c + dc[d]                              # 전진
    if visited[nr][nc] == 0 and land[nr][nc] == 0:  # 방문안하고 빈곳이면
        visited[nr][nc] = 1                         # 방문 처리
        # land[nr][nc] = 1
        r = nr                                      # 이동
        c = nc                                      # 이동
        cnt += 1                                    # 청소 추가
        turn = 0                                    # 방향 그대로
        # for i in range(N):
        #     print(visited[i])
        # print("-------------visit-----------------")
        # for i in range(N):
        #     print(land[i])
        # print("-------------land-----------------")
        continue
    else:
        turn += 1                                   # 빈곳이 아니면 방향전환

    if turn == 4:                                   # 4방향 다돌아도 갈곳없으면
        nr = r + dr[(d+2) % 4]                              # 뒤로 가기
        nc = c + dc[(d+2) % 4]                              # 뒤로 가기
        if land[nr][nc] == 0:                       # 뒤에가 청소안한곳이면
            r = nr                                  # 이동하고
            c = nc
        else:                                       # 아니면
            break                                   # 멈춰
        turn = 0

print(cnt)