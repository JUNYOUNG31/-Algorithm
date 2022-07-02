# 완전 제곱수

M = int(input())
N = int(input())
arr = []
for i in range(M, N + 1):
    temp = int(i ** 0.5)
    if i == temp ** 2:
        arr.append(i)

if arr == []:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))
