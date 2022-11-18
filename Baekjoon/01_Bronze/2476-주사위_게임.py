# 주사위 게임

N = int(input())
ans = 0
for i in range(N):
    a, b, c = map(int, input().split())
    if a == b == c:
        ans = max(ans, 10000 + a * 1000)
    elif a != b and b != c and c != a:
        ans = max(ans, max(a, b, c) * 100)
    elif a == b != c:
        ans = max(ans, 1000 + a*100)
    elif a != b == c:
        ans = max(ans, 1000 + b*100)
    elif a == c != b:
        ans = max(ans, 1000 + a*100)

print(ans)