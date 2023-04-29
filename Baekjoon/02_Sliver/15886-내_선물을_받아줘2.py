# 내 선물을 받아줘 2

N = int(input())
arr = list(input())
idx = 0
# print(arr)
for i in range(N):
    if arr[i] == "E":
        if arr[i+1] == "W":
            idx += 1

print(idx)