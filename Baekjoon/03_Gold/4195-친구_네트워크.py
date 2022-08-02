# 친구 네트워크


def find(n):
    if net[n] == n:
        return n
    else:
        net[n] = find(net[n])
        return net[n]


def union(a, b):
    x = find(a)
    y = find(b)
    if y != x:          # 없으면
        net[x] = y      # 연결시키고
        cnt[y] += cnt[x]    # cnt  증가
    return


T = int(input())

for tc in range(T):
    net = {}
    cnt = {}
    F = int(input())

    for i in range(F):
        x, y = map(str, input().split())

        if x not in net:
            net[x] = x  # 추가하고
            cnt[x] = 1  # 카운트 초기화
        if y not in net:
            net[y] = y      # 추가하고
            cnt[y] = 1      # 카운트 초기화

        union(x, y)
        # print(net)
        # print(cnt)
        ans = cnt[find(x)]
        print(ans)

