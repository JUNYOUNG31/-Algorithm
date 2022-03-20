# 덩치

N = int(input())
arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

for c in arr:
    rank = 1
    for n in arr:
        if (c[0] != n[0]) & (c[1] != n[1]):
            if (c[0] < n[0]) & (c[1] < n[1]):
                rank += 1
    print(rank)