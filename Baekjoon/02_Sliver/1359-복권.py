# 복권
from itertools import combinations

N, M, K = map(int, input().split())
cnt1 = 0
cnt2 = 0
arr = []
for i in range(1, N+1):
    arr.append(i)
for x in combinations(arr, M):
    for y in combinations(arr, M):
        cnt1 += 1
        if len(set(x) & set(y)) >= K:
            cnt2 += 1

print(cnt2/cnt1)