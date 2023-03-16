# 캡틴 이다솜

N = int(input())
arr = []
b = 0
i = 1

while b < N:
    b += (i*(i+1))//2
    arr.append(b)
    i += 1

dp = [99999999999999] * (N+1)

for i in range(1, N+1):
    for b in arr:
        if b >= i:
            if b == i:
                dp[i] = 1
            break
        dp[i] = min(dp[i], 1 + dp[i-b])

print(dp[N])