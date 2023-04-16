# 카드 놓기

from collections import deque

N = int(input())
arr = list(map(int, input().split()))
q = deque()
arr.reverse()

for i in range(N):
    if arr[i] == 1:
        q.appendleft(i+1)
    elif arr[i] == 2:
        temp = q.popleft()
        q.appendleft(i+1)
        q.appendleft(temp)
    elif arr[i] == 3:
        q.append(i+1)

print(*q)