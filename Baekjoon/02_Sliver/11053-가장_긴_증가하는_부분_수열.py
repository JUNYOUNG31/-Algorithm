# 가장 긴 증가하는 부분 수열

N = int(input())
arr = list(map(int, input().split()))
dp = [0 for i in range(N)]
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))