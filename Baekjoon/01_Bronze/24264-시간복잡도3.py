# 시간복잡도 3

A = []
def MenOfPassion(A, n):
    hap = 0
    for i in range(n):
        for j in range(n):
            hap = hap + A[i] + A[j]
    return hap

n = int(input())

print(n*n)
print(2)