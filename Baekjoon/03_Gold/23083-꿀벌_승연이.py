# 꿀벌 승연이

from collections import deque

even = [(-1,1), (0,1), (1,0)]
odd = [(0,1), (1,1), (1,0)]

N, M = map(int, input().split())
arr = [[0 for _ in range(M)] for _ in range(N)]

K = int(input())
for i in range(K):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1

# for i in arr:
#     print(i)

dp = [[0 for _ in range(M)] for _ in range(N)]
# for i in range(N):
#     if arr[i][0] != 1:
#         dp[i][0] = 1

dp[0][0] = 1

for j in range(M):
    for i in range(N):
        if arr[i][j] != 1:
            if j % 2 == 1:
                for d in range(3):
                    ni = i + odd[d][0]
                    nj = j + odd[d][1]
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 1:
                        dp[ni][nj] += dp[i][j]
            if j % 2 == 0:
                for m in range(3):
                    ni = i + even[m][0]
                    nj = j + even[m][1]
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 1:
                        dp[ni][nj] += dp[i][j]

            # print(i,j)

#
# for k in dp:
#     print(k)
print(dp[-1][-1] % (10**9 + 7))

