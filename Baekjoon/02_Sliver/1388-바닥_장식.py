# 바닥 장식

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))
cnt = 0

for i in range(N):
    temp = ''
    for j in range(M):
        if graph[i][j] == '-':
            if graph[i][j] != temp:
                cnt += 1
        temp = graph[i][j]

for j in range(M):
    temp = ''
    for i in range(N):
        if graph[i][j] == '|':
            if graph[i][j] != temp:
                cnt += 1
        temp = graph[i][j]

print(cnt)



