# N과M(9)


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [0] * N
ans = []


def function(now):
    if len(ans) == M:
        print(*ans)
        return
    temp = 0
    for i in range(N):
        if not visited[i] and temp != arr[i]:
            visited[i] = 1
            ans.append(arr[i])
            temp = arr[i]
            function()
            visited[i] = 0
            ans.pop()


function()