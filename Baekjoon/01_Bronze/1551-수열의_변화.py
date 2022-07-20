# 수열의 변하

N, K = map(int, input().split())
A = list(map(int, input().split(',')))

for i in range(K):
    arr = []
    for j in range(len(A)-1):
        arr.append(A[j+1] - A[j])
    A = arr
print(','.join(map(str, A)))