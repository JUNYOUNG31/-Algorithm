# 미로 탐색

# N×M크기의 배열로 표현되는 미로가 있다.미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
# 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의
# 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다.
# 각각의 수들은 붙어서 입력으로 주어진다.

dr = [1, 0, -1, 0]      # 하좌상우
dc = [0, -1, 0, 1]

N, M = list(map(int, input().split()))                             # 지도의 크기
visited = [[0]*M for _ in range(N)]                                # 방문처리
maze = []               
for _ in range(N):                                                 # 지도 생성
    m = list(input())
    maze.append(m)
# print(maze)
queue = [[0, 0]]                                                   # bfs 써야해서 q 로 0,0 추가
visited[0][0] = 1                                                  # 초기값 1로 주고 1씩 더해가기
while queue:                                                       # 반복
    r, c = queue.pop(0)
    for d in range(4):
        nr = r + dr[d]                                             # 방향전환
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:   # 벽을 만나지 고
            if maze[nr][nc] == '1':                                # 1 이면
                visited[nr][nc] = visited[r][c] + 1                # 방문을 + 1 더해준다.
                queue.append((nr, nc))                             # q 에 추가해주고

print(visited[N-1][M-1])                                           # 마지막 값 불러오기