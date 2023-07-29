# 최소비용 구하기2

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n = int(input())
m = int(input())

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)


graph = [[] for i in range(n + 1)]
# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


first, last = map(int, input().split())

# print(first, last)
# for i in graph:
#     print(i)

root = [0] * (n + 1)


def dijkstra(first):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, first))
    distance[first] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for next_node, next_cost in graph[now]:
            new_cost = dist + next_cost
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                root[next_node] = now
                heapq.heappush(q, (new_cost, next_node))

# 다익스트라 알고리즘을 수행

dijkstra(first)
print(distance[last])
# print(root)

# 경로 파악하기
check = [last]
temp = last
while temp != first:
    temp = root[temp]
    check.append(temp)

print(len(check))
print(*check[::-1])
