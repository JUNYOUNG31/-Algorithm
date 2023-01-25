# 연결 요소의 개수

import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N + 1)
cnt = 0


def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)


for i in range(1, N + 1):
    if visited[i] == 0:
        if not graph[i]:
            cnt += 1
            visited[i] = 1
        else:
            bfs(i)
            cnt += 1

print(cnt)