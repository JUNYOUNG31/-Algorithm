# BABBA

N = int(input())
A = [1]
B = [0]

for i in range(N):
    A.append(B[i])
    B.append(B[i] + A[i])

print(A[-1], B[-1])
