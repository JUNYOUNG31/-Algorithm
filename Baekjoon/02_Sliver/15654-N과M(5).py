# N과 M 5
from itertools import permutations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

# def dfs(d, idx, N, M):
#     if d == M:
#         print(' '.join(map(str, arr)))
#         return
#     for i in range(idx, N):
#         arr.append(i+1)
#         dfs(d+1, i, N, M)
#         arr.pop()
#
# dfs(0, 0, N, M)
ans = []
ans = list(permutations(arr, M))

if M == 1:
    for i in ans:
        print(i[0])
else:
    for i in ans:
        temp = []
        for j in range(M):
            print(i[j], end=" ")
        print()
