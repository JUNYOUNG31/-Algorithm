# 적록색약

# 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이
# 보는 그림과는 좀 다를 수 있다.
# 크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로
# 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는
# 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100) 둘째 줄부터 N개 줄에는 그림이 주어진다.

from collections import deque

dr = [1, 0, -1, 0]                      # 하좌상우
dc = [0, -1, 0, 1]


def bfs(r, c):                                                     # bfs 함수
    queue.append((r, c))                                           # q 에 배추 추가
    while queue:                                                   # q 가 있으면
        r, c = queue.popleft()                                     # pop 하고
        for d in range(4):                                         # 방향 정해서
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:  # 방문안했고
                if pan[nr][nc] == pan[r][c]:                          # 이전과 같은색이면
                    visited[nr][nc] = 1                               # 방문처리하고  q 에 추가
                    queue.append((nr, nc))


N = int(input())                                     # 크기
pan = [list(map(str, input())) for _ in range(N)]    # 판입력
visited = [[0] * N for _ in range(N)]                # 방문처리 리스트
queue = deque()                                      # q
cnt_1 = 0                                            # 적록색약 아닌구역 수
for i in range(N):                                   # 전체 탐색해서
    for j in range(N):
        if visited[i][j] == 0:                       # 방문안했으면
            bfs(i, j)                                # bfs 돌리고
            cnt_1 += 1                               # 카운트 추가
for i in range(N):                                   # 적록색약인걸 처리하기위해
    for j in range(N):
        if pan[i][j] == 'G':                         # 초록 부분을
            pan[i][j] = 'R'                          # 빨간색으로 다 바꾸기
visited = [[0] * N for _ in range(N)]                # 방문처리도 초기화하고
cnt_2 = 0                                            # 적록색약인 구역 수
for i in range(N):                                   # 전체 탐색
    for j in range(N):
        if visited[i][j] == 0:                       # 방문안했으면
            bfs(i, j)                                # bfs 돌리고
            cnt_2 += 1                               # 카운트 추가
print(cnt_1, cnt_2)                                  # 카운트 두개 출력