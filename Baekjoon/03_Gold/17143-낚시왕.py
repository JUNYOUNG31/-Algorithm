# 낚시왕


# 낚시왕이 오른쪽으로 한 칸 이동
# 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡기
# 상어를 잡으면 잡은 상어 지우기
# 상어 이동

R, C, M = map(int, input().split())
pan = [[0 for _ in range(C)] for _ in range(R)]

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    pan[r-1][c-1] = (z, s, d)

# 각자의 속도를 가지고 이동
# 벽을 만나면 반대로 이동
# 이동후 2개가 겹치면 큰것만 남김

# 1은 위 2는 아래 3은 오른 4는 왼
dis = [[0, 0], [-1, 0], [1, 0], [0, 1], [0, -1]]


def move():
    new_pan = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(C):
        for j in range(R):
            if pan[j][i] != 0:
                z, s, d = pan[j][i] # 크기 속도 방향
                nj = j
                ni = i
                while s > 0:
                    nj += dis[d][0]
                    ni += dis[d][1]
                    if 0 <= nj < R and 0 <= ni < C:
                        s -= 1
                    else:
                    # 범위 밖이면 반대로 움직이는건데..
                    # 원상복구하고
                        nj -= dis[d][0]
                        ni -= dis[d][1]
                        if d == 1:
                            d = 2
                        elif d == 2:
                            d = 1
                        elif d == 3:
                            d = 4
                        elif d == 4:
                            d = 3
                # 다옮기고
                if new_pan[nj][ni] == 0:
                    new_pan[nj][ni] = (z, pan[j][i][1], d)
                if new_pan[nj][ni] != 0:
                    if new_pan[nj][ni][0] < z:
                        new_pan[nj][ni] = (z, pan[j][i][1], d)
    return new_pan


cnt = 0
for i in range(C):
    for j in range(R):
        if pan[j][i] != 0:
            cnt += pan[j][i][0]
            pan[j][i] = 0
            # print(cnt)
            break

    pan = move()

print(cnt)


