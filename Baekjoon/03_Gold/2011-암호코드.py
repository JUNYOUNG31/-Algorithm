# 암호코드

num = list(str(input().strip()))
dp = [0 for _ in range(len(num) + 1)]
dp[0], dp[1] = 1, 1
if num[0] == '0':
    print(0)
else:
    for i in range(2, len(num)+1):
        if int(num[i-1]) > 0:
            dp[i] += dp[i-1]
        temp = int(num[i-2] + num[i-1])
        if 10 <= temp <= 26:
            dp[i] += dp[i-2]
    print(dp[-1] % 1000000)

# print(dp)
# 26을 넘어가면 2자리수를 만들수 없음
