# 나누기

N = int(input())
F = int(input())
num = N // 100
ans = num * 100

while ans % F != 0:
    ans += 1
print(str(ans)[-2:])