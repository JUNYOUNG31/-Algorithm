# 과제 안 내신 분

arr = [0] * 31
for _ in range(28):
    num = int(input())
    arr[num] = 1
for i in range(1, 31):
    if arr[i] == 0:
        print(i)