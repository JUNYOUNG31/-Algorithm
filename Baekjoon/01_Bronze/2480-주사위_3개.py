# 주사위 3개


A, B, C = map(int, input().split())
ans = 0
if A == B and B == C:
    ans = 10000 + A * 1000

elif A == B:
    ans = 1000 + A * 100

elif A == C:
    ans = 1000 + A * 100

elif B == C:
    ans = 1000 + B * 100

else:
    ans = 100 * max(A,B,C)

print(ans)