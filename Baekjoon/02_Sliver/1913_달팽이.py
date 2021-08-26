# 달팽이

# 홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N2까지의 자연수를 달팽이 모양으로 N×N의 표에 채울 수 있다.

# 첫째 줄에 홀수인 자연수 N(3 ≤ N ≤ 999)이 주어진다. 둘째 줄에는 위치를 찾고자 하는 N2 이하의 자연수가 하나 주어진다.

#     하 우 상 좌
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

N = int(input())
find = int(input())
arr = [[0] * N for _ in range(N)]
d = 0                                   # 방향
r = 0                                   # 행좌표
c = 0                                   # 열좌표
num = N**2                              # 숫자 입력
while num >= 1:                         # 숫자범위
    arr[r][c] = num                     # 처음에는 마지막수
    if find == num:                     # 찾는 숫자의 위치
        ans1, ans2 = r + 1, c + 1       # index 값이므로 1씩 주가
    num -= 1                            # 1씩 감소
    nr = r + dr[d]                      # 아래쪽으로 이동
    nc = c + dc[d]
    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:   # 벽을 만나지 않으면
        r, c = nr, nc                   # 그방향으로 쭉 이등
    else:                               # 벽을 만나면
        d = (d+1) % 4                   # 0 부터 4 까지 반복하기위해서 4로 나눈 나머지
        r += dr[d]                      # 방향 전환 (반시계 방향)
        c += dc[d]

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()
print(ans1, ans2)