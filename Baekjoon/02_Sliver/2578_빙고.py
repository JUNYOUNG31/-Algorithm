# 빙고
bingo = [list(map(int, input().split())) for _ in range(5)]

line = 0
cnt = 0
visited = [[0] * 5 for _ in range(5)]
calls = [list(map(int, input().split())) for _ in range(5)]
for r in range(5):
    for c in range(5):
        for i in range(5):
            for j in range(5):
                if calls[r][c] == bingo[i][j]:
                    visited[i][j] = 1
                    cnt += 1
                    line = 0
                    if visited[0][0] == 1 and visited[1][1] == 1 and visited[2][2] == 1 and visited[3][3] == 1 and visited[4][4] == 1:
                        line += 1
                    if visited[4][0] == 1 and visited[3][1] == 1 and visited[2][2] == 1 and visited[1][3] == 1 and visited[0][4] == 1:
                        line += 1
                    for row in range(5):
                        if sum(visited[row]) == 5:
                            line += 1
                    for col in range(5):
                        num = 0
                        for rows in range(5):
                            if visited[rows][col] == 1:
                                num += 1
                        if num == 5:
                            line += 1
                    if line >= 3:
                        break
                if line >= 3:
                    break
            if line >= 3:
                break
        if line >= 3:
            break
    if line >= 3:
        print(cnt)
        break