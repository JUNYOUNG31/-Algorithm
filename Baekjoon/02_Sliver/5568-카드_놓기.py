# 카드 놓기

from itertools import permutations

n = int(input())
k = int(input())
arr = []

for _ in range(n):
    arr.append(input().strip())

arr2 = list(permutations(arr, k))
ans = []
for i in arr2:
    temp = ''
    for j in range(k):
        temp += i[j]
    if temp not in ans:
        ans.append(temp)

print(len(ans))