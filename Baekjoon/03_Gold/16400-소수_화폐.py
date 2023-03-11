# 소수 화폐

import math


def prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


n = int(input())
arr = []
for i in range(2, n + 1):
    if prime(i):
        arr.append(i)
dp = [0 for _ in range(n + 1)]
dp[0] = 1
for p in arr:
    for i in range(p, n + 1):
        dp[i] = (dp[i] + dp[i - p]) % 123456789
print(dp[n])