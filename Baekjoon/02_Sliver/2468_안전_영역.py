# 안전 영역

# 재난방재청에서는 많은 비가 내리는 장마철에 대비해서 다음과 같은 일을 계획하고 있다. 먼저 어떤 지역의 높이
# 정보를 파악한다. 그 다음에 그 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개가
# 만들어 지는 지를 조사하려고 한다. 이때, 문제를 간단하게 하기 위하여, 장마철에 내리는 비의 양에 따라
# 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정한다.
# 어떤 지역의 높이 정보는 행과 열의 크기가 각각 N인 2차원 배열 형태로 주어지며 배열의 각 원소는 해당
# 지점의 높이를 표시하는 자연수이다. 어떤 지역의 높이 정보가 주어졌을 때,
# 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하시오.

# 첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다.
# N은 2 이상 100 이하의 정수이다. 둘째 줄부터 N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지
# 순서대로 한 행씩 높이 정보가 입력된다. 각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N개의 높이 정보를
# 나타내는 자연수가 빈 칸을 사이에 두고 입력된다. 높이는 1이상 100 이하의 정수이다.
from collections import deque

dr = [1, 0, -1, 0]                      # 하좌상우
dc = [0, -1, 0, 1]


def bfs(r, c, rain):                                                  # bfs 함수
    queue.append((r, c))                                              # q 에  추가
    while queue:                                                      # q 가 있으면
        r, c = queue.popleft()                                        # pop 하고
        for d in range(4):                                            # 방향 정해서
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:  # 방문안했고
                if land[nr][nc] > rain:                               # 강수량보다 크면
                    visited[nr][nc] = 1                               # 방문처리하고  q 에 추가
                    queue.append((nr, nc))


N = int(input())                                            # 크기
land = [list(map(int, input().split())) for _ in range(N)]  # 지역 입력
visited = [[0] * N for _ in range(N)]                       # 방문처리 리스트
queue = deque()                                             # q
max_land = max(max(land))                                   # 최대 지형
min_land = min(min(land))                                   # 최소 지형

# print(max_land)
# print(min_land)
max_cnt = 0                                                 # 구역의  max 값
for i in range(min_land-1, max_land+1):                     # 최소부터 최대까지 돌면서
    visited = [[0] * N for _ in range(N)]                   # 방문처리 초기화해주고
    cnt = 0                                                 # 구역 수
    for j in range(N):                                      # 전체 탐색해서
        for k in range(N):
            if land[j][k] > i and visited[j][k] == 0:       # 강수량보다 크고 방문안했으면
                visited[j][k] = 1                           # 방문처리하고
                bfs(j, k, i)                                # bfs 돌린다.
                cnt += 1                                    # 구역 추가하고
    if max_cnt < cnt:                                       # 구역의 최대값 갱신하기
        max_cnt = cnt
print(max_cnt)                                              # 최대 출력
