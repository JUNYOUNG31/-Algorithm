# 시간복잡도 5

A = []
def MenOfPassion(A, n):
    hap = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                hap = hap + A[i] * A[j] * A[k]
    return hap

n = int(input())

print(n**3)
print(3)
