# 평범한 배낭

N, K = map(int, input().split())
dp = [[0] * (K+1) for _ in range(N+1)]
bag = [[0, 0]]

for i in range(N):
    W, V = map(int, input().split())
    bag.append([W, V])

for i in range(1, N+1):
    W = bag[i][0]
    V = bag[i][1]
    for j in range(1, K+1):
        if j < W:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-W] + V, dp[i-1][j])

print(dp[N][K])
