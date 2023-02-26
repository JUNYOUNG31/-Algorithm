# 바구니 뒤집기

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().strip().split())
    arr = arr[0:i-1] + arr[i-1:j][::-1] + arr[j:]

print(" ".join(str(i) for i in arr))