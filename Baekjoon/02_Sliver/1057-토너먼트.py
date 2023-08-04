# 토너먼트

N, x, y = map(int, input().split())

cnt = 0
while x != y:
    x -= y // 2
    x -= y // 2
    cnt += 1

print(cnt)