# 운동

N, m, M, T, R = map(int, input().split())
cnt = 0
t = 0
now = m
while cnt < N:
    if m+T > M:
        break
    if now + T <= M:
        now += T
        cnt += 1
    else:
        now = max(now-R, m)
    t += 1
if cnt == N:
    print(t)
else:
    print(-1)