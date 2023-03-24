# 케빈 베이컨의 6단계 법칙

N, M = map(int, input().split())

arr = [[9999999999] * (N+1) for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    arr[A][B] = 1
    arr[B][A] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            arr[i][j] = 0

for f in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            arr[i][j] = min(arr[i][j], arr[i][f] + arr[f][j])

bacon = 9999999999
ans = 0
for i in range(N, 0, -1):
    temp = sum(arr[i][1:])
    if bacon >= temp:
        bacon = temp
        ans = i

print(ans)
