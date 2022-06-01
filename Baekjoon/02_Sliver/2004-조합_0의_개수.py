# 조합 0의 개수

N, M = map(int, input().split())

def function(n, x):
    cnt = 0
    while n:
        n //= x
        cnt += n
    return cnt


five = function(N, 5) - function(M, 5) - function(N - M, 5)
two = function(N, 2) - function(M, 2) - function(N - M, 2)

ans = min(five, two)
print(ans)