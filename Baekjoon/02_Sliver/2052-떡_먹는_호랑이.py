# 떡 먹는 호랑이

D, K = map(int, input().split())

dp = [0 for _ in range(D)]
dp[0] = [1, 0]   # 1A + 0B
dp[1] = [0, 1]   # 0A + 1B

for i in range(2, D):
    dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]]

x, y = dp[-1][0], dp[-1][1]

A, B = 1, 1

while True:
    if x*A + y*B == K:
        print(A)
        print(B)
        break
    elif x*A + y*B < K:
        B += 1
    elif x*A + y*B > K:
        A += 1
        B = A

# print(x, y)