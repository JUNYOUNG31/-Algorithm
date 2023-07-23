# 적록색약

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