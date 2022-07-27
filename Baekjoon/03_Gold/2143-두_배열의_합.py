# 두 배열의 합
from collections import Counter

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

list_A = A  # 부분집합 넣을거
list_B = B  # 부분집합 넣을거

for i in range(n):  # 완탐하면서 각원소를 더하면서 추가
    hap = A[i]
    for j in range(i+1, n):
      hap += A[j]
      list_A.append(hap)

for i in range(m):
    hap = B[i]
    for j in range(i+1, m):
      hap += B[j]
      list_B.append(hap)

cnt = 0
num = Counter(list_B)
print(num)
print(list_A)
for i in range(len(list_A)):
    cnt += num[T-list_A[i]]
print(cnt)