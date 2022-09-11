# 용액

N = int(input())
arr = list(map(int, input().split()))

ans = 2147483647

start, end = 0, N-1
num1 = 0
num2 = 0
while start < end:
    temp = arr[start] + arr[end]
    if abs(temp) < ans:
        ans = abs(temp)
        num1 = arr[start]
        num2 = arr[end]

    if temp < 0:
        start += 1
    if temp > 0:
        end -= 1
    if temp == 0:
        break

print(num1, num2)