# 구간 합 구하기 5
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


# for i in arr:
#     print(i)

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + arr[i][j]

# for i in dp:
#     print(i)

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1] - dp[x1-1][y1-1])
    # C = ALL - ( A + B - (A와 B의 겹치는부분))
    print(ans)