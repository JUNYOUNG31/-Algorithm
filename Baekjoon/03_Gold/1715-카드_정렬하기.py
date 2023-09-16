# 카드 정렬하기
import heapq

N = int(input())
arr = []
for i in range(N):
    num = int(input())
    arr.append(num)

arr.sort()
# print(arr)
ans = 0
if N > 1:
    while len(arr) > 1:
        temp1 = heapq.heappop(arr)
        temp2 = heapq.heappop(arr)
        # print(temp1, temp2)
        heapq.heappush(arr, temp1 + temp2)
        ans += temp1+temp2
    print(ans)
elif N == 1:
    print(0)