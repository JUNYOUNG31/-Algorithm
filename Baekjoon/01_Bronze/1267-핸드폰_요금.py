# 핸드폰 요금

N = int(input())
time = map(int, input().split())
Y = 0
M = 0
for i in time:
    Y += i // 30 * 10 + 10
    M += i // 60 * 15 + 15
if Y < M:
    print('Y %d' % Y)
elif Y > M:
    print('M %d' % M)
else:
    print('Y M %d' % M)
