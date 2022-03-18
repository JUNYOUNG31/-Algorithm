# 베르트랑 공준

N = 123456 * 2 + 1

arr = [True] * N
for i in range(2, int(N**0.5)+1):
    if arr[i]:
        for j in range(2*i, N, i):
            arr[j] = False


def prime_cnt(n):
    cnt = 0
    for i in range(n + 1, n * 2 + 1):
        if arr[i]:
            cnt += 1
    return cnt

while True:
    n = int(input())
    if n == 0:
        break
    ans = prime_cnt(n)
    print(ans)