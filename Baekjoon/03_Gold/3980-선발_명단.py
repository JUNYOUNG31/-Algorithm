# 선발 명단

C = int(input())
ans = 0


def dfs(pan, visited, deep, hap):
    global ans
    if deep == 11:
        ans = max(ans, hap)
        return
    for score, a, b in pan[deep]:
        if a == deep and not visited[b]:
            visited[b] = 1
            dfs(pan, visited, deep+1, hap+score)
            visited[b] = 0
    return


while True:
    ans = 0
    pan = [[] for _ in range(11)]
    arr = []
    visited = [0] * 11
    for i in range(11):
        temp = list(map(int, input().split()))
        arr.append(temp)
        for j in range(11):
            if arr[i][j] != 0:
                pan[j].append((arr[i][j], j, i))
    dfs(pan, visited, 0, 0)
    print(ans)
    C -= 1
    if C == 0:
        break



