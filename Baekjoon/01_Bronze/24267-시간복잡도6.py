# 시간복잡도 6

A = []
def MenOfPassion(A, n):
    hap = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                hap = hap + A[i] * A[j] * A[k]
    return hap

n = int(input())

print((n*(n-1)*(n-2))//6)
print(3)
