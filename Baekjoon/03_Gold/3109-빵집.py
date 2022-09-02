# 빵집

dx = [-1, 0, 1]


R, C = map(int, input().split())
zido = []
for i in range(R):
    x = list(input())
    zido.append(x)

visited = [[0 for _ in range(C)]for _ in range(R)]


cnt = 0
flag = False
def dfs(x, y):
    global cnt, flag
    if y == C-1:
        cnt += 1
        flag = True
        return

    for d in range(3):
        nx = x + dx[d]
        ny = y + 1
        if 0 <= nx < R and 0 <= ny < C:
            if zido[nx][ny] != 'x' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx, ny)

        if flag:
            return


for i in range(R):
    flag = False
    dfs(i, 0)


# for i in zido:
#     print(i)
#
# for i in visited:
#     print(i)

print(cnt)