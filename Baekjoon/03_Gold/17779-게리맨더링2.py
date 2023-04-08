# 게리맨더링2

N = int(input())
A = []
for i in range(N):
    temp = list(map(int, input().split()))
    A.append(temp)

# 구역을 5개로 나눠야함
# 각 구역은 5개중 하나에 포함
# 선거구 끼리는 모두 연결

# 5번 먼저 그리고 나머지를 하면될듯?

# 인덱스 맞추게


def check(x,y,d1,d2):
    pan = [[0 for _ in range(N+1)] for _ in range(N+1)]
    # 5번 구역 경계선은 했는데
    pan[x][y] = 5
    for i in range(1, d1+1):
        # (x, y), (x + 1, y - 1), ..., (x + d1, y - d1)
        pan[x+i][y-i] = 5
        # (x + d2, y + d2), (x + d2 + 1, y + d2 - 1), ..., (x + d2 + d1, y + d2 - d1)
        pan[x+d2+i][y+d2-i] = 5
    for i in range(1, d2+1):
        # (x, y), (x + 1, y + 1), ..., (x + d2, y + d2)
        pan[x+i][y+i] = 5
        # (x + d1, y - d1), (x + d1 + 1, y - d1 + 1), ...(x + d1 + d2, y - d1 + d2)
        pan[x+d1+i][y-d1+i] = 5
    # 경계선 안은 어떻게?
    # 나머지 1234를 채우고 빈곳은 5? 오류남 흠 5번 경계부터해서 그런가
    # 1    선거구: 1 ≤ r < x + d1, 1 ≤ c ≤ y
    for r in range(1, x+d1):
        for c in range(1, y+1):
            if pan[r][c] == 5:
                break
            pan[r][c] = 1
    # 2    선거구: 1 ≤ r ≤ x + d2, y < c ≤ N
    for r in range(1, x+d2+1):
        for c in range(N, y, -1):
            if pan[r][c] == 5:
                break
            pan[r][c] = 2
    # 3    선거구: x + d1 ≤ r ≤ N, 1 ≤ c < y - d1 + d2
    for r in range(x+d1, N+1):
        for c in range(1, y-d1+d2):
            if pan[r][c] == 5:
                break
            pan[r][c] = 3
    # 4    선거구: x + d2 < r ≤ N, y - d1 + d2 ≤ c ≤ N
    for r in range(x+d2+1, N+1):
        for c in range(N, y-d1+d2-1, -1):
            if pan[r][c] == 5:
                break
            pan[r][c] = 4

    for r in range(1, N+1):
        for c in range(1, N+1):
            if pan[r][c] == 0:
                pan[r][c] = 5

    hap = [0,0,0,0,0]
    for r in range(1, N+1):
        for c in range(1, N+1):
            if pan[r][c] == 1:
                hap[0] += A[r-1][c-1]
            elif pan[r][c] == 2:
                hap[1] += A[r-1][c-1]
            elif pan[r][c] == 3:
                hap[2] += A[r-1][c-1]
            elif pan[r][c] == 4:
                hap[3] += A[r-1][c-1]
            elif pan[r][c] == 5:
                hap[4] += A[r-1][c-1]
    ans = max(hap) - min(hap)
    # if ans == 18:
    #     for i in range(N+1):
    #         print(pan[i])
    # if ans == 17:
    #     for i in range(N+1):
    #         print(pan[i])
    return ans


min_ans = 1000
for x in range(1, N+1):
    for y in range(1, N + 1):
        for d1 in range(1, N + 1):
            for d2 in range(1, N + 1):
                if 1 <= x < x+d1+d2 <= N and 1 <= y-d1 < y < y+d2 <= N:
                    # print(x,y,d1,d2)
                    # 각 구역의 합을 구하고 큰거랑 작은거를 뺀거 중에 가장 작은값
                    min_ans = min(min_ans, (check(x,y,d1,d2)))


print(min_ans)