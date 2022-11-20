# 회의실 배정

N = int(input())
arr = []
for i in range(N):
    time = list(map(int, input().split()))
    arr.append(time)
arr.sort(key=lambda x:(x[1], x[0]))
last = 0
cnt = 0
for i, j in arr:
    if i >= last:
        cnt += 1
        last = j
print(cnt)