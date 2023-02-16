# 타일 장식물

n = int(input())
dp1 = 4     # 피보나치?
dp2 = 6
ans = 0

if n == 1:
    ans = dp1
elif n == 2:
    ans = dp2
else:
    for i in range(2, n):
        ans = dp1 + dp2
        dp1 = dp2
        dp2 = ans
print(ans)