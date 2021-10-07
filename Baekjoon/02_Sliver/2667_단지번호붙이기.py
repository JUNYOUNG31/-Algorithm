# 단지번호붙이기

# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서
# 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는
# 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고,
# 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
# 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

from collections import deque

dr = [1, 0, -1, 0]                      # 하좌상우
dc = [0, -1, 0, 1]


def bfs(r, c):                                                     # bfs 함수
    global ans                                                     # 정답 리스트 불러오기
    queue.append((r, c))                                           # q 에 추가
    cnt = 1                                                        # 집의 수
    gido[r][c] = 0                                                 # 현재위치를 0으로 바꾸기     
    while queue:                                                   # q 가 있으면
        r, c = queue.popleft()                                     # pop 하고
        for d in range(4):                                         # 방향 정해서
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and gido[nr][nc] == 1:  # 1이있다면
                gido[nr][nc] = 0                                   # 0으로 바꾸고 q 에 추가
                queue.append((nr, nc))
                cnt += 1                                           # 집 수 1증가
    ans.append(cnt)                                                # 정답 리스트에 추가


N = int(input())                                                   # 지도 크기
gido = [list(map(int, input())) for _ in range(N)]                 # 지도 입력
queue = deque()                                                    # q
ans = []                                                           # 정답 리스트
for i in range(N):                                                 # 전체 탐색
    for j in range(N):
        if gido[i][j] == 1:                                        # 1있으면
            bfs(i, j)                                              # bfs 돌고
count = len(ans)                                                   # 단지의 개수
ans.sort()                                                         # 정렬해서
print(count)                                                       # 단지수 출력
for i in range(count):                                             # 단지별 집수 출력
    print(ans[i])

