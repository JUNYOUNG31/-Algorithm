# 행렬 곱셈

# N*M크기의 행렬 A와 M*K크기의 행렬 B가 주어졌을 때, 두 행렬을 곱하는 프로그램을 작성하시오.

A = []
N, M = map(int, input().split())
for i in range(N):
    m = list(map(int, input().split()))
    A.append(m)

B = []
M, K = map(int, input().split())
for i in range(M):
    k = list(map(int, input().split()))
    B.append(k)

ans = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            ans[i][j] += A[i][k] * B[k][j]


for i in ans:
    print(*i)