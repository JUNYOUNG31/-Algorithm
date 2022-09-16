# N과M(8)


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []


def function(now):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(now, N):
            ans.append(arr[i])
            function(i)
            ans.pop()


function(0)