# 테트로미노

# 폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.
# 정사각형은 서로 겹치면 안 된다.
# 도형은 모두 연결되어 있어야 한다.
# 정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
# 정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.
# 아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며,
# 각각의 칸에는 정수가 하나 쓰여 있다.
# 테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.
# 테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

dr = [0, 0, -1, 1]  # 동 서 북 남
dc = [1, -1, 0, 0]

dx = [[0, 1, 1, 2], [0, 1, 1, 2], [0, 1, 1, 1], [0, -1, -1, -1]]
dy = [[0, 0, -1, 0], [0, 0, 1, 0], [0, 0, -1, 1], [0, 0, -1, 1]]

N, M = map(int, input().split())
pan = []
for i in range(N):
    a = list(map(int, input().split()))
    pan.append(a)
# print(pan)

visited = [[0] * M for _ in range(N)]
max_hap1 = 0


def dfs1(r, c, hap, cnt):
    global max_hap1
    if cnt == 4:
        if max_hap1 < hap:
            max_hap1 = hap
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            dfs1(nr, nc, hap+pan[nr][nc], cnt+1)
            visited[nr][nc] = 0


def dfs2(r, c):
    max_hap = []
    for i in range(4):
        cnt = 0
        hap = pan[r][c]
        for j in range(1, 4):
            nr = r + dx[i][j]
            nc = c + dy[i][j]
            if 0 <= nr < N and 0 <= nc < M:
                hap += pan[nr][nc]
                cnt += 1
        max_hap.append(hap)
    # print(max(max_hap))
    return max(max_hap)


for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs1(i, j, pan[i][j], 1)
        visited[i][j] = 0

max_hap2 = 0
for i in range(N):
    for j in range(M):
        a = dfs2(i, j)
        if max_hap2 < a:
            max_hap2 = a
# print(max_hap2)
ans = max(max_hap1, max_hap2)

print(ans)