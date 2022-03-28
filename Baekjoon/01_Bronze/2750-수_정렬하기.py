# 수 정렬하기


N = int(input())
arr = []
for i in range(N):
    num = int(input())
    arr.append(num)
arr.sort()

for i in range(N):
    print(arr[i])

