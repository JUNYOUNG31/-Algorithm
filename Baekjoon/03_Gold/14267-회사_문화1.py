# 회사 문화 1
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import defaultdict

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dic = defaultdict(list)

for i in range(n):
    dic[arr[i]].append(i+1)

dp = [0] * (n+1)
# print(dic)


def dfs(i):
    for x in dic[i]:
        dp[x] += dp[i]
        dfs(x)
        # print(x)


for i in range(m):
    i, w = map(int, input().split())
    dp[i] += w

dfs(1)


print(*dp[1:])