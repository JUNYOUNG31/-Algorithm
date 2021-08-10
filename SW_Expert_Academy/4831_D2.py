# 전기버스
T = int(input())
for case in range(T):
    K, N, M = map(int, input().split())
    charging = map(int, input().split())

    station = [0]*N
    for i in charging:
        station[i] = 1


