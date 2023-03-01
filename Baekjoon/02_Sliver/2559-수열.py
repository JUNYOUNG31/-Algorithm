# 수열

import sys
input = sys.stdin.readline
arr = []
N, K = map(int, input().split())
temp = list(map(int, input().split()))
for i in range(N-K+1):
    arr.append(sum(temp[i:i + K]))
print(max(arr))