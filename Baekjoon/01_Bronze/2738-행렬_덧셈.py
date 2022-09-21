# 행렬 덧셈

N, M = map(int, input().split())
A = []
B = []
for i in range(N):
    temp = list(map(int, input().split()))
    A.append(temp)

for i in range(N):
    temp = list(map(int, input().split()))
    B.append(temp)

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=' ')
    print()
