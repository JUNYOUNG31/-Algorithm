# 동전0

N, K = map(int, input().split())
arr = []
cnt = 0
for i in range(N):
    A = int(input())
    arr.append(A)
arr.sort(reverse=True)
for i in arr:
    if i > K:
        continue
    else:
        while i <= K:
            K -= i
            cnt += 1
print(cnt)