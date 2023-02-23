# 시간복잡도 4

A = []
def MenOfPassion(A, n):
    hap = 0
    for i in range(n):
        for j in range(i, n):
            hap = hap + A[i] + A[j]
    return hap

n = int(input())

print((n*(n-1))//2)
print(2)