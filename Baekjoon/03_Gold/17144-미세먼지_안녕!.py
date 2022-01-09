# 미세먼지 안녕!

# 미세먼지를 제거하기 위해 구사과는 공기청정기를 설치하려고 한다. 공기청정기의 성능을 테스트하기 위해 구사과는 집을
# 크기가 R×C인 격자판으로 나타냈고, 1×1 크기의 칸으로 나눴다. 구사과는 뛰어난 코딩 실력을 이용해 각 칸 (r, c)에 있는
# 미세먼지의 양을 실시간으로 모니터링하는 시스템을 개발했다. (r, c)는 r행 c열을 의미한다.
# 공기청정기는 항상 1번 열에 설치되어 있고, 크기는 두 행을 차지한다. 공기청정기가 설치되어 있지 않은 칸에는 미세먼지가
# 있고, (r, c)에 있는 미세먼지의 양은 Ar,c이다.
# 1초 동안 아래 적힌 일이 순서대로 일어난다.

# 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
# (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
# 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
# 확산되는 양은 Ar,c/5이고 소수점은 버린다.
# (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
# 공기청정기가 작동한다.
# 공기청정기에서는 바람이 나온다.
# 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
# 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
# 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
# 다음은 확산의 예시이다.

# 공기청정기의 바람은 다음과 같은 방향으로 순환한다.
# 방의 정보가 주어졌을 때, T초가 지난 후 구사과의 방에 남아있는 미세먼지의 양을 구해보자.

R, C, T = map(int, input().split())
room = [[int(i) for i in input().split()] for _ in range(R)]

# for i in range(R):
#     print(room[i])

cleaner = []
flag = False
for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            flag = True
            cleaner = [[i, j], [i+1, j]]
            break
    if flag == True:
        break
# print(cleaner)


def dust():
    copyroom = [[0]*C for _ in range(R)]   # 새로운 배열
    dx = [1, 0, -1, 0]  # 우 상 좌 하
    dy = [0, -1, 0, 1]
    for i in range(R):
        for j in range(C):
            if room[i][j] != 0 and room[i][j] != -1:  # 미세먼지가 잇으면
                temp = room[i][j]
                for k in range(4):      # 4방향을 확인하고
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C: # 범위안에 있고
                        if room[nx][ny] != -1:     # 청소기가 아니면
                            copyroom[nx][ny] += (room[i][j]//5)  # 새로운 배열에 확산값을 더해주고
                            temp -= (room[i][j]//5)        # 기존 값은 확산된값을 빼주고
                copyroom[i][j] += temp                     # 4방향 다 확산하면 기존값을 갱신
    for i, j in cleaner:
        copyroom[i][j] = -1

    return copyroom


def wind(room):
    # 위쪽 바람
    for i in range(cleaner[0][0]-1, 0, -1):  # 위에서 아래로
        room[i][0] = room[i-1][0]
    room[0][0] = 0

    for i in range(0, C-1):             # 왼쪽으로
        room[0][i] = room[0][i+1]
    room[0][C - 1] = 0

    for i in range(0, cleaner[0][0]):     # 위로
        room[i][C-1] = room[i+1][C-1]
    room[cleaner[0][0]][C-1] = 0

    for i in range(C-1, 1, -1):         # 오른쪽으로 부는 바람
        room[cleaner[0][0]][i] = room[cleaner[0][0]][i-1]
    room[cleaner[0][0]][1] = 0

    # 아래바람
    for i in range(cleaner[1][0]+2, R): # 위로 부는 바람
       room[i-1][0] = room[i][0]
    room[R-1][0] = 0

    for i in range(0, C-1):     # 왼쪽으로 부는 바람
        room[R-1][i] = room[R-1][i + 1]
    room[R-1][C-1] = 0

    for i in range(R-1, cleaner[1][0], -1):    # 아래로 부는 바람
        room[i][C-1] = room[i-1][C-1]
    room[cleaner[1][0]][C-1] = 0

    for i in range(C-1, 1, -1): # 오른쪽으로 부는 바람
        room[cleaner[1][0]][i] = room[cleaner[1][0]][i-1]
    room[cleaner[1][0]][1] = 0


for i in range(T):
    room = dust()
    wind(room)
    # for j in range(R):
    #     print(room[j])


ans = 0
for i in range(R):
    for j in range(C):
        ans += room[i][j]

ans += 2

print(ans)