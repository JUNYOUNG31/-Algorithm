# 정수 삼각형

n = int(input())

dp = []
for i in range(n):
    a = list(map(int, input().split()))
    dp.append(a)

for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i][j]+dp[i-1][j]
        elif j == len(dp[i])-1:
            dp[i][j] = dp[i][j]+dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+dp[i][j]
print(max(dp[n-1]))