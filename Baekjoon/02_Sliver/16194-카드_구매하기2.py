# 카드 구매하기2

N = int(input())
p = [0] + list(map(int, input().split()))
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, i+1):
        if dp[i] == 0:
            dp[i] = dp[i-j]+p[j]
        else:
            dp[i] = min(dp[i], dp[i-j]+p[j])

print(dp[N])