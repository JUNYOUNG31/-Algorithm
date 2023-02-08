# 전깃줄

n = int(input())
w = []
w_b = []
dp = [0 for i in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    w.append([a, b])
w.sort(key=lambda x: x[0])

for i in range(n):
    w_b.append(w[i][1])

for i in range(n):
    for j in range(i):
        if w_b[i] > w_b[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(n - max(dp))