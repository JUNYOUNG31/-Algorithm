# 자두나무

T, W = map(int, input().split())
arr = []
dp = [[0 for _ in range(T)] for _ in range(W+1)]
for _ in range(T):
    x = int(input())
    arr.append(x)



# print(arr)

for i in range(T):
    for j in range(W+1):
        if j == 0:          # 한번도 움직이지 않을 때 1번 위치
            if arr[i] == 1:     # 자두가 1번에서 떨어질때
                dp[0][i] = dp[0][i-1] + 1
            else:
                dp[0][i] = dp[0][i-1]

        else:               # 움직이는데
            if j % 2 == 1:  # 홀수번 움직이면 2번위치 이고
                if arr[i] == 1:   # 자두는 1번에서 떨어질때
                    dp[j][i] = max(dp[j][i-1], dp[j-1][i-1])# 그대로
                if arr[i] == 2:   # 자두는 2번에서 떨어질때
                    dp[j][i] = max(dp[j][i-1], dp[j-1][i-1]) + 1  # 1증가
            if j % 2 == 0:  # 짝수번 움직이면 1번위치 이고
                if arr[i] == 1:   # 자두는 1번에서 떨어지때
                    dp[j][i] = max(dp[j][i-1], dp[j-1][i-1]) + 1# 1중가
                if arr[i] == 2:   # 자두는 2번에서 떨어질때
                    dp[j][i] = max(dp[j][i-1], dp[j-1][i-1])# 그대로

ans = []
for i in dp:
    ans.append(max(i))
for i in dp:
    print(i)
print(max(ans))


