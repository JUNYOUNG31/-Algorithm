# 텀 프로젝트

def dfs(x):
    global cnt
    visited[x] = 1
    i = arr[x]
    if not visited[i]:  # 방문안했으면 dfs
        dfs(i)
    else:               # 방문 했으면
        if i not in team:  # 팀에 없으면
            cnt += 1       #  
            temp = i
            while temp != x:
                cnt += 1
                temp = arr[temp]
    team.append(x)


T = int(input())
for tc in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    team = []
    cnt = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
    ans = n - cnt
    print(ans)