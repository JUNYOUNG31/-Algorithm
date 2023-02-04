

def solution(macaron):
    answer = []
    pan = [[0 for _ in range(6)] for _ in range(6)]
    for i, j in macaron:
        pan[0][i - 1] = j
        down(pan)
        for x in range(5, -1, -1):
            for y in range(5, -1, -1):
                if pan[x][y] != 0:
                    visited = [[0 for _ in range(6)] for _ in range(6)]
                    check(pan, visited, x, y, 1)
                    pang(pan, visited)

    for i in range(6):
        temp1 = []
        for j in range(6):
            temp = str(pan[i][j])
            temp1.append(temp)
        temp2 = ''.join(temp1)
        answer.append(temp2)
    return answer


def down(pan):
    for i in range(5):
        for j in range(6):
            if pan[i + 1][j] == 0:
                pan[i + 1][j] = pan[i][j]
                pan[i][j] = 0
    return pan


def check(pan, visited, i, j, cnt):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    temp = pan[i][j]
    visited[i][j] = 1
    if cnt >= 3:
        for x in range(6):
            for y in range(6):
                if visited[x][y] != 0:
                    visited[x][y] = 99
    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]
        if 0 <= nx < 6 and 0 <= ny < 6:
            if visited[nx][ny] == 0:
                if temp == pan[nx][ny]:
                    check(pan,visited, nx, ny, cnt + 1)



def pang(pan, visited):
    for i in range(6):
        for j in range(6):
            if visited[i][j] == 99:
                pan[i][j] = 0
    down(pan)


macaron = [[1, 1], [2, 1], [1, 2], [3, 3], [6, 4], [3, 1], [3, 3], [3, 3], [3, 4], [2, 1]]

solution(macaron)