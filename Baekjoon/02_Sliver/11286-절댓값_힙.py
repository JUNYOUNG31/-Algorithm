# 절댓값 힙

import sys
import heapq
input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    N = int(input())
    if N == 0:
        if len(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(N), N))