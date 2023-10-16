# 금민수의 합
from collections import deque

N = int(input())
arr = []
temp = set()
q = deque(['4', '7'])
while q:
    num = q.popleft()
    n = int(num)
    if n <= N:
        temp.add(n)
        q.append(num + '4')
        q.append(num + '7')

arr = sorted(list(temp))
print(arr)
print(len(arr))

ans = []
visited = set()
dq = deque()
# (합, 더한 숫자 리스트)
dq.append((0, []))
while dq:
    hap, dist = dq.popleft()
    if hap == N:
        ans = dist
        break
    for num in arr:
        now_hap = hap + num
        if now_hap <= N and now_hap not in visited:
            visited.add(now_hap)
            dq.append((now_hap, dist + [num]))


ans.sort()
if ans:
    print(' '.join(map(str, ans)))
else:
    print(-1)