# 알약

dp = [[0 for _ in range(31)] for _ in range(31)]
# 약 30개

# 반알만 남으면 경우의 수는 1개
for i in range(31):
    dp[0][i] = 1

for w in range(1, 31):
    for h in range(30):
        if h == 0:  # 반알없으면
            dp[w][h] = dp[w-1][h+1] # 한알을 먹고 반알을 추가
        if h != 0:  # 반알이 있으면
            dp[w][h] = dp[w][h-1] + dp[w-1][h+1] # 반알먹는거랑 한알먹고 반알추가하는걸 더하기

while True:
    drug = int(input())
    if drug == 0:
        break
    print(dp[drug][0])


for i in dp:
    print(i)