# 과자

K, N, M = list(map(int, input().split()))
ans = K * N - M

if ans <= 0:
    print(0)
else:
    print(ans)