# 상자 넣기

n = int(input())
box = list(map(int, input().split()))
dp = [1]
for i in range(1, n):
    d = []
    for j in range(i):
        if box[i] > box[j]:
            d.append(dp[j] + 1)
    if not d:
        dp.append(1)
    else:
        dp.append(max(d))
print(max(dp))