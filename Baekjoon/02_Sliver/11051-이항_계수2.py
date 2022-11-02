# 이항 계수 2

n, k = map(int, input().split())
dp = []

for i in range(n + 1):
    temp = [1] * (i + 1)
    dp.append(temp)

for i in range(2, n + 1):
    for j in range(1, i):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007

print(dp[n][k])