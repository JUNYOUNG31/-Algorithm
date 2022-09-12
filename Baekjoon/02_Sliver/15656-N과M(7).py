# N과 M(7)


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []


def function():
    if len(ans) == M:
        print(*ans)
        return
    for i in range(N):
            ans.append(arr[i])
            function()
            ans.pop()


function()