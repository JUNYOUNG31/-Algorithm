# 원상복구

N, K = map(int, input().split())

S = list(map(int, input().split()))
D = list(map(int, input().split()))

ans = S

for i in range(K):
    tmp = list(range(N))
    for j in range(N):
        go = D[j]
        tmp[go-1] = ans[j]
    ans = tmp

print(*ans)