# 물건 팔기

arr = dict()
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    if a not in arr:
        arr[a] = [b]
    else:
        arr[a].append(b)
ans = 0
top = 0
for i in sorted(list(arr.keys())):
    t = 0
    for j in arr:
        for k in arr[j]:
            if i-k > 0:
                t += i-k
    del arr[i]
    if top < t:
        top = t
        ans = i

print(ans)