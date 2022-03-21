# 미로 만들기

# 홍준이는 미로 안의 한 칸에 남쪽을 보며 서있다. 미로는 직사각형 격자모양이고, 각 칸은 이동할 수 있거나,
# 벽을 포함하고 있다. 모든 행과 열에는 적어도 하나의 이동할 수 있는 칸이 있다. 홍준이는 미로에서 모든
# 행과 열의 이동할 수 있는 칸을 걸어다녔다. 그러면서 자신의 움직임을 모두 노트에 쓰기로 했다.
# 홍준이는 미로의 지도를 자기 노트만을 이용해서 그리려고 한다.
# 입력으로 홍준이가 적은 내용이 주어진다. 문자열로 이루어져 있으며, 모든 문자 하나는 한 번의 움직임을 말한다.
# ‘F’는 앞으로 한 칸 움직인 것이고, ‘L'과 ’R'은 방향을 왼쪽 또는 오른쪽으로 전환한 것이다. 즉, 90도를 회전하면서,
# 위치는 그대로인 것이다.

# 첫째 줄에 홍준이가 적은 내용의 길이가 주어진다. 길이는 0보다 크고, 50보다 작다. 둘째 줄에 그 내용이 주어진다.

dr = [1, 0, -1, 0]      # 하좌상우
dc = [0, -1, 0, 1]


N = int(input())
way = list(input())

d = 0                                   # 방향
r = 0                                   # 행좌표
c = 0                                   # 열좌표
maze = [[0, 0]]
for i in way:
    if i == 'F':
        nr = r + dr[d]
        nc = c + dc[d]
        maze.append([nr, nc])

    elif i == 'R':
        d = (d + 1) % 4

    elif i == 'L':
        d = (d + 3) % 4

max_r = 0
min_r = 100
max_c = 0
min_c = 100

for i in range(len(maze)):
    if max_r < maze[i][0]:
        max_r = maze[i][0]
    if min_r > maze[i][0]:
        min_r = maze[i][0]

for i in range(len(maze)):
    if max_c < maze[i][1]:
        max_c = maze[i][1]
    if min_c > maze[i][1]:
        min_c = maze[i][1]

visited = [[0] * ((max_r - min_r)+1) for _ in range((max_c - min_c)+1)]

# print(max_r, min_r)
# print(max_c, min_c)
# print(visited)
# print(maze)

for i, j in maze:
    visited[i][j] = '.'

for i in range(len(visited)):
    print(*visited[i])