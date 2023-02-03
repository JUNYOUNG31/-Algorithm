# N번째 큰 수

import heapq

heap = []
N = int(input())

for _ in range(N):
    num = map(int, input().split())
    for i in num:
        if len(heap) < N:
            heapq.heappush(heap, i)
        else:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
print(heap[0])