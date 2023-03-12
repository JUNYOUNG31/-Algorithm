# 빗물

H, W = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(1, W-1):
    left = max(arr[:i])
    right = max(arr[i+1:])
    temp = min(left, right)
    if arr[i] < temp:
        ans += temp - arr[i]

print(ans)