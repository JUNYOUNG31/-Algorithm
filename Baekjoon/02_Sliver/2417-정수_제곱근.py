# 정수 제곱근

n = int(input())

ans = 0
num = n

while ans <= num:
    mid = (ans + num) // 2
    if mid ** 2 < n:
        ans = mid + 1
    else:
        num = mid - 1

print(ans)