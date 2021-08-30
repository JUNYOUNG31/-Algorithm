# 진기의 최고급 붕어빵
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    time_come = list(map(int, input().split()))
    time_come.sort()
    ans = 'Possible'
    cnt = 0
    for i in range(N):
        bread = (time_come[i] // M) * K
        if bread - cnt <= 0:
            ans = 'Impossible'
            break
        else:
            cnt += 1

    print("#{} {}".format(tc + 1, ans))