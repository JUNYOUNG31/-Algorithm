# 진짜 공간

N = int(input())
file = list(map(int, input().split()))
size = int(input())
sum = 0
for i in file:
    if i % size == 0:
        sum += i // size
    else:
        sum += i // size + 1
print(sum * size)