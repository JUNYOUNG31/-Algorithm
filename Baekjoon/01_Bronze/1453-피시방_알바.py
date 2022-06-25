# 피시방 알바

N = int(input())
arr = map(int, input().split())
seat = [0] * 101
num = 0
for i in arr:
    if seat[i] != 0:
        num += 1
    else:
        seat[i] += 1
print(num)