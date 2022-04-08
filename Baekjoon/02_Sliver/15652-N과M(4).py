# N과M(4)

N, M = map(int, input().split())
arr = []

def dfs(d, idx, N, M):
    if d == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(idx, N):
        arr.append(i+1)
        dfs(d+1, i, N, M)
        arr.pop()

dfs(0, 0, N, M)
