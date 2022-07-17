# 새

N = int(input())
ans = 0
temp = 1

while N > 0:
    if N < temp:
        temp = 1
    N -= temp
    temp += 1
    ans += 1

print(ans)