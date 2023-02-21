# 공 바꾸기

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
for i in range(M):
    x, y = map(int, input().split())
    temp = arr[y-1]
    arr[y-1] = arr[x-1]
    arr[x-1] = temp

print(*arr)