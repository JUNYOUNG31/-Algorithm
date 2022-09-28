# 뿌요뿌요
from collections import deque


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

arr = []
for _ in range(12):
    temp = list(input())
    arr.append(temp)


# 떨어지기
def down():
    for i in range(6):
        for j in range(11, -1, -1):
            for k in range(11, j, -1):
                if arr[k][i] == '.' and arr[j][i] != '.':
                    arr[k][i] = arr[j][i]
                    arr[j][i] = '.'
                    break


# 탐색하기
def bfs(x, y, color):
    puyo = deque()
    puyo.append((x, y))
    q = deque()
    q.append((x, y))
    while q:
        r, c = q.popleft()
        for d in range(4):
            nx = r + dx[d]
            ny = c + dy[d]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if visited[nx][ny] == 0 and arr[nx][ny] == color:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    puyo.append((nx, ny))
    return puyo


cnt = 0
while True:
    visited = [[0] * 6 for _ in range(12)]
    check = 0
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.' and visited[i][j] == 0:
                visited[i][j] = 1
                pypy = bfs(i, j, arr[i][j])
                if len(pypy) >= 4:
                    check = 1
                    for (r, c) in pypy:
                        arr[r][c] = '.'
    if check == 0:
        break
    cnt += 1
    down()



print(cnt)

# for i in arr:
#     print(i)
