# 줄세우기

import sys
input = sys.stdin.readline

N = int(input())

d = [1]*(N+1)
num = [0]
for i in range(N):
    num.append(int(input()))


for i in range(1, N+1):
    for j in range(1, i):
        if num[j] < num[i]:
            d[i] = max(d[i], d[j]+1)


print(N-max(d))