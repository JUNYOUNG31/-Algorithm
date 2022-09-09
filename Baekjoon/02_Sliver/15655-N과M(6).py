# N과 M(6)

from itertools import combinations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()


ans = []
ans = list(combinations(arr, M))

# print(ans)

if M == 1:
    for i in ans:
        print(i[0])
else:
    for i in ans:
        temp = []
        for j in range(M):
            print(i[j], end=" ")
        print()
