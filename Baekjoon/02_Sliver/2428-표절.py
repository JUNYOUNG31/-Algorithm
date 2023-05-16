# 표절

N = int(input())
size = list(map(int, input().split()))
size.sort()

ans = 0
for i in range(N):
    left = i
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        if size[i] >= size[mid] * 0.9:
            left = mid + 1
        else:
            right = mid - 1
    ans += left - i - 1

print(ans)