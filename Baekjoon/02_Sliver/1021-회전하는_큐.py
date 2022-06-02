# 회전하는 큐

from collections import deque


N, M = map(int, input().split())
arr = deque(range(1, N+1))
q = deque(map(int, input().split()))
cnt = 0

while q:
    mid = len(arr)//2
    if arr.index(q[0]) > mid:
        while q[0] != arr[0]:
            arr.appendleft(arr.pop())
            cnt += 1
        arr.popleft()
        q.popleft()
    else:
        while q[0] != arr[0]:
            arr.append(arr.popleft())
            cnt += 1
        arr.popleft()
        q.popleft()

print(cnt)