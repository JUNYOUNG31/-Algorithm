# 공유기 설치

N, C = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()
start = 1
end = arr[-1] - arr[0]
ans = 0


def binary_search(arr, start, end):
    global ans
    while start <= end:
        mid = (start + end) // 2
        now = arr[0]
        cnt = 1
        for i in range(1, len(arr)):
            if arr[i] >= now + mid:
                cnt += 1
                now = arr[i]
        if cnt >= C:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1


binary_search(arr, start, end)
print(ans)