# 그림

# 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라.
# 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이
# 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

# 첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다.
# 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며,
# 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)
from collections import deque


def bfs(r, c):                          # bfs 함수
    hap = 1                             # 넓이 구하기
    queue = deque()                     # q
    queue.append((r, c))                # q 에 추가
    while queue:                        # q 가 있으면
        r, c = queue.popleft()          # pop 하고
        for d in range(4):              # 방향 정해서
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and picture[nr][nc] == 1: # 값이 1일때
                picture[nr][nc] = 0     # 0으로 바꾸고
                queue.append((nr, nc))  # q 에 추가 하고
                hap += 1                # 넓이 + 1
    return hap


dr = [1, 0, -1, 0]                      # 하좌상우
dc = [0, -1, 0, 1]
n, m = map(int, input().split())        # 크기 입력
picture = []                            # 그림 리스트
for i in range(n):                      # 그림 만들기
    gif = list(map(int, input().split()))
    picture.append(gif)
cnt = []                                # 넓이 값들 추가할 리스트
for i in range(n):                      # 그림을 다 뒤져서
    for j in range(m):
        if picture[i][j] == 1:          # 1 이 있다면
            picture[i][j] = 0           # 0 으로 바꿔주고
            cnt.append(bfs(i, j))       # bfs 돌린다
print(len(cnt))                         # 그림 총 개수
if cnt:
    print(max(cnt))                     # 그림이있으면 max 값 출력
else:
    print(0)                            # 없으면 0 출력