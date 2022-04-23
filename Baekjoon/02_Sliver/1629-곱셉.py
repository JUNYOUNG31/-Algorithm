# 곱셈

def function(a, b, c):
    if b == 1:
        return a % c

    if b % 2 == 0:
        return (function(a, b // 2, c) ** 2) % c
    else:
        return ((function(a, b // 2, c) ** 2) * a) % c


A, B, C = map(int, input().split())

print(function(A, B, C))