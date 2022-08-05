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
    if x < y:
        net[y] = x
        cnt[x] += cnt[y]
    elif x > y:
        net[x] = y
        cnt[y] += cnt[x]


# def union(a, b):
#     x = find(a)
#     y = find(b)
#     if y != x:
#         net[x] = y
#         cnt[y] += cnt[x]
#     return

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

