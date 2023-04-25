# 2+1 세일

N = int(input())
C = []
for i in range(N):
    C.append(int(input()))
C.sort(reverse=True)

hap = 0
for i in range(N):
    if i % 3 != 2:
        hap += C[i]

print(hap)