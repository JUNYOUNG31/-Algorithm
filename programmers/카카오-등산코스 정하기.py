# 등산 코스 정하기

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정


def solution(n, paths, gates, summits):
    # 시작 노드 번호를 입력받기
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
    graph = [[] for i in range(n + 1)]
    # 최단 거리 테이블을 모두 무한으로 초기화


    # 모든 간선 정보를 입력받기
    for a, b, c in paths:
        # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
        graph[a].append((b, c))
        graph[b].append((a, c))

    summits.sort()

    def dijkstra():
        q = []
        distance = [INF] * (n + 1)
        for start in gates:
            # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
            heapq.heappush(q, (0, start))
            distance[start] = 0
        while q: # 큐가 비어있지 않다면
            # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(q)
            # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            if distance[now] < dist or now in summits:
                continue
            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            for i in graph[now]:
                cost = max(dist, i[1])
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

        ans = [0, INF]
        for summit in summits:
            if distance[summit] < ans[1]:
                ans[0] = summit
                ans[1] = distance[summit]
        return ans

    # 다익스트라 알고리즘을 수행
    answer = dijkstra()

    return answer








answer = solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5])
print(answer)