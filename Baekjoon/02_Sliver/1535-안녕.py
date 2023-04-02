# 안녕

N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1 = [0] + arr1
arr2 = [0] + arr2
dp = [[0 for _ in range(101)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, 101):
        if arr1[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr1[i]] + arr2[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][99])