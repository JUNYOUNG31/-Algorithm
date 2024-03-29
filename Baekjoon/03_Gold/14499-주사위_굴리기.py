# 주사위 굴리기

# 크기가 N×M인 지도가 존재한다. 지도의 오른쪽은 동쪽, 위쪽은 북쪽이다. 이 지도의 위에 주사위가 하나 놓여져 있으며,
# 주사위의 전개도는 아래와 같다. 지도의 좌표는 (r, c)로 나타내며, r는 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로부터 떨어진 칸의 개수이다.
#   2
# 4 1 3
#   5
#   6
# 주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며, 놓여져 있는 곳의 좌표는
# (x, y) 이다. 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.
# 지도의 각 칸에는 정수가 하나씩 쓰여져 있다. 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의
# 바닥면에 쓰여 있는 수가 칸에 복사된다. 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
# 주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때, 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램을 작성하시오.
# 주사위는 지도의 바깥으로 이동시킬 수 없다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.

dr = [0, 0, 0, -1, 1]  # 동 서 북 남
dc = [0, 1, -1, 0, 0]


dice = [0] * 6

# dic = [[0, 1, 2, 3, 4, 5],
#        [3, 1, 0, 5, 4, 2],
#        [2, 1, 5, 0, 4, 3],
#        [4, 0, 2, 3, 5, 1],
#        [1, 5, 2, 3, 0, 4]
#        ]


def change(run):
    if run == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif run == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif run == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif run == 4:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

        # dice[0] = dice[1]
        # dice[1] = dice[5]
        # dice[4] = dice[0]
        # dice[5] = dice[4]


N, M, x, y, K = map(int, input().split())
zido = []
for i in range(N):
    a = list(map(int, input().split()))
    zido.append(a)

# for i in range(N):
#     print(zido[i])

run = list(map(int, input().split()))
# print(run)
for i in run:
    nr = x + dr[i]
    nc = y + dc[i]
    if 0 <= nr < N and 0 <= nc < M:
        x = nr
        y = nc
        change(i)
        if zido[x][y] != 0:
            dice[5] = zido[x][y]
            zido[x][y] = 0
        else:
            zido[x][y] = dice[5]
    # print(dice)
        print(dice[0])