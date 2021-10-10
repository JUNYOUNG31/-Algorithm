# 토마토

# 철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이
# 격자모양 상자의 칸에 하나씩 넣은 다음, 상자들을 수직으로 쌓아 올려서 창고에 보관한다.
# 창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면,
# 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
# 하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다.
# 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.
# 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.
# 토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
# 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라
# 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

# 첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다.
# M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다.
# 둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다. 즉,
# 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다. 각 줄에는 상자 가로줄에 들어있는
# 토마토들의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토,
# 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다. 이러한 N개의 줄이 H번 반복하여 주어진다.
# 토마토가 하나 이상 있는 경우만 입력으로 주어진다.

from collections import deque

dy = [1, 0, -1, 0, 0, 0]                      # 하좌상우 위 아래
dx = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():                                             # bfs 함수
    while queue:                                       # q 가 있으면
        x, y, z = queue.popleft()                      # pop 하고
        for d in range(6):                             # 방향 정해서
            ny = y + dy[d]
            nx = x + dx[d]
            nz = z + dz[d]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and tomato[nz][nx][ny] == 0:  # 값이 0 일때
                tomato[nz][nx][ny] = tomato[z][x][y] + 1                                 # 1씩 추가하고
                queue.append((nx, ny, nz))                                               # q 에 추가 하고


M, N, H = map(int, input().split())               # 상자 크기 입력
tomato = []
for j in range(H):                                # 토마토 입력
    mato2 = []
    for i in range(N):
        mato1 = list(map(int, input().split()))
        mato2.append(mato1)
    tomato.append(mato2)
# print(tomato)
queue = deque()                                   # q 를 여기서 안하면 bfs 돌릴때 1이 여러개일때 찾지 못햇음
for k in range(H):
    for i in range(N):                            # 상자를 다돌며
        for j in range(M):
            if tomato[k][i][j] == 1:              # 1 이 있다면
                queue.append((i, j, k))           # q 에 추가
bfs()                                             # bfs 를 돌린다.
# print(tomato)
min_day = 0                                       # 최소 날짜
ans = 0                                           # -1 일 경우
for k in range(H):
    for i in range(N):                            # 상자를 다돌며
        for j in range(M):
            if tomato[k][i][j] == 0:              # 0 이 있다면
                ans = -1                          # 모두 안익어서 -1
                break                             # 멈춰
            else:                                 # 0이 없으면
                min_day = (max(min_day, tomato[k][i][j]))  # 최대값을 갱신하면서 저장한다
if ans == -1:                                     # ans -1 이면
    print(-1)                                     # 모두안익어서 -1 출력
else:
    print(min_day-1)                              # 최소날짜에서 1빼기