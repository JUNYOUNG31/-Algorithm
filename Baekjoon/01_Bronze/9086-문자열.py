# 문자열

T = int(input())

for _ in range(T):
    x = list(input())
    ans = x[0] + x[-1]
    print(ans)