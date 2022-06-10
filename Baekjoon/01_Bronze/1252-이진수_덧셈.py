# 이진수 덧셈

n, m = map(str, input().split())
n = int(n, 2)
m = int(m, 2)
ans = n + m

print(bin(ans)[2:])