# 동전 1

n, k = map(int, input().split())

arr = []

for i in range(n):
    x = int(input())
    arr.append(x)
arr.sort()

dp = [0 for _ in range(k+1)]
dp[0] = 1

for i in arr:
    for j in range(i, k+1):
        dp[j] += dp[j-i]
# print(dp)
# print(arr)
print(dp[k])

