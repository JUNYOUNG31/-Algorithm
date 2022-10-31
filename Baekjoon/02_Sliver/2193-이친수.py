# 이친수

N = int(input())

dp = [0, 1, 1]
for i in range(3, 91):
    temp = dp[i-1] + dp[i-2]
    dp.append(temp)

print(dp[N])
