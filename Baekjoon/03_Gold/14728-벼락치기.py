# 벼락치기

N, T = map(int, input().split())
time = []
score = []
for i in range(N):
    K, S = map(int, input().split())
    time.append(K)
    score.append(S)


dp = [[0 for _ in range(T+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, T+1):
        if j >= time[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time[i]] + score[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][T])