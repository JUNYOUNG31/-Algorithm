# 텀 프로젝트

import sys
sys.setrecursionlimit(100001)


def dfs(x):
    global ans
    visited[x] = 1
    team.append(x)
    temp = arr[x]
    if visited[temp]:
        if temp in team:
            ans += team[team.index(temp):]
        return
    else:
        dfs(temp)


T = int(input())
for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [1] + [0] * n
    ans = []
    for i in range(1, n + 1):
        if not visited[i]:
            team = []
            dfs(i)
    print(n - len(ans))