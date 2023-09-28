# 목장 건설하기

M, N = map(int, input().split())
arr = []
for i in range(M):
    temp = list(map(int, input().split()))
    arr.append(temp)

# for i in arr:
#     print(i)


dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
# 가장 긴 길이
l = 0


for i in range(1, M+1):
    for j in range(1, N+1):
        # 0 이 빈땅 1이 나무 2가 바위
        if arr[i-1][j-1] == 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            l = max(l, dp[i][j])
    # for j in dp:
    #     print(j)
    # print('---------------')

# for i in dp:
#     print(i)
print(l)
