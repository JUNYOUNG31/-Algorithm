# 수 정렬하기2
import sys
N = int(sys.stdin.readline())
arr = []
for i in range(N):
    num = int(sys.stdin.readline())
    arr.append(num)
arr.sort()

for i in range(N):
    print(arr[i])