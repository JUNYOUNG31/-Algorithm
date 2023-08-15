# 여러분의 다리가 되어 드리겠습니다!
# union find


def find(x):
    if island[x] != x:
        island[x] = find(island[x])
    return island[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        island[y] = x
    else:
        island[x] = y


N = int(input())
island = [i for i in range(N+1)]

# 연결된 섬들 먼저 체크
for i in range(N-2):
    a, b = map(int, input().split())
    union(a, b)

# print(island)

ans = [0, 0]
for i in range(1, N+1):
    if i == island[i]:
        ans[0] = i
        for j in range(i, N+1):
            if j == island[j]:
                if i != j:
                    ans[1] = j
                    print(*ans)
                    exit()
