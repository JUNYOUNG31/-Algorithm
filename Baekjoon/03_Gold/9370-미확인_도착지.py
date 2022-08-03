# 미확인 도착지

import heapq
import sys
input = sys.stdin.readline


def dijkstra(start):
    q = []
    distance = [987654321] * (n + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


T = int(input())
for tc in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for i in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    goals = []
    for _ in range(t):
        x = int(input())
        goals.append(x)
    s_dist = dijkstra(s)
    g_dist = dijkstra(g)
    h_dist = dijkstra(h)
    # print(s_dist)
    # print(g_dist)
    # print(h_dist)
    ans = []
    for i in goals:
        if s_dist[g] + g_dist[h]+h_dist[i] == s_dist[i] or s_dist[h] + h_dist[g]+g_dist[i] == s_dist[i]:
            ans.append(i)
    ans.sort()
    print(*ans)
