# 가희와 3단 고음

import sys
input = sys.stdin.readline
N, A, D = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
x = 0
for i in range(N):
    if arr[i] == A + (x*D):
        cnt += 1
        x += 1
print(cnt)