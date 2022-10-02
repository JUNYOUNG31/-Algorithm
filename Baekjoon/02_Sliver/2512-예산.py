# 예산

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

arr.sort()
start = 0
end = arr[-1]
while start <= end:
    mid = (start + end) // 2
    hap = 0
    for i in arr:
        if i >= mid:
            hap += mid
        else:
            hap += i
    if hap <= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)