# 로마 숫자 만들기

N = int(input())
# roma = [1, 5, 10, 50]
# arr = []
# hap = [0] * 1001

arr = set()
for i in range(N+1):
    for j in range(N+1-i):
        for k in range(N+1-i-j):
            t = N-i-j-k
            n = i + 5*j + 10*k + 50*t
            arr.add(n)

print(len(arr))