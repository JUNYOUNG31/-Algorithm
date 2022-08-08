# 회의준비


def find(n):
    if group[n] == n:
        return n
    else:
        group[n] = find(group[n])
        return group[n]


def union(a, b):
    x = find(a)
    y = find(b)
    if x != y:
        group[x] = y
    return


N = int(input())
M = int(input())
INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]
group = [i for i in range(N + 1)]

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    union(a, b)

for k in range(1, N +1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


arr = [INF] * (N + 1)
ans = [0] * (N + 1)
for a in range(1, N + 1):
    maxx = -1
    for b in range(1, N + 1):
        if graph[a][b] == INF:
            continue
        if maxx < graph[a][b]:
            maxx = graph[a][b]
    # print(maxx)
    if arr[find(a)] > maxx:
        arr[find(a)] = maxx
        ans[find(a)] = a


for a in range(N + 1):
    for b in range(N + 1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()

# print(arr)
print(ans)
cnt = ans.count(0)
print(N + 1 - cnt)
ans.sort()
for i in ans:
    if i != 0:
        print(i)

