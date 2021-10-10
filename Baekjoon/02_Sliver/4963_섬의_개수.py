# 섬의 개수

# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.
# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다.
# 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다.
# w와 h는 50보다 작거나 같은 양의 정수이다.
# 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
# 입력의 마지막 줄에는 0이 두 개 주어진다.
from collections import deque
   
dr = [1, 0, -1, 0, -1, 1, 1, -1]                                   # 원점을 기준으로 8방
dc = [0, -1, 0, 1, 1, 1, -1, -1]


def bfs(r, c):                                                     # bfs 함수
    queue = deque()
    queue.append((r, c))                                           # q 에  추가
    while queue:                                                   # q 가 있으면
        r, c = queue.popleft()                                     # pop 하고
        for d in range(8):                                         # 방향 정해서
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < h and 0 <= nc < w and land[nr][nc] == 1:  # 땅이면
                land[nr][nc] = 0                                   # 0으로 바꾸고  q 에 추가
                queue.append((nr, nc))


while True:                                                        # 무한반복문
    w, h = list(map(int, input().split()))                         # 지도 크기 설정
    if w == 0 and h == 0:                                          # 반복문 종료 조건
        break   
    land = [list(map(int, input().split())) for _ in range(h)]     # 지도 입력
    cnt = 0                                                        # 섬의 개수
    for i in range(h):                                             # 전체 탐색해서
        for j in range(w):  
            if land[i][j] == 1:                                    # 땅이면
                bfs(i, j)                                          # bfs 돌리고
                cnt += 1                                           # 섬의 개수 추가
    print(cnt)