# 요세푸스 문제 0

N, K = map(int, input().split())
queue = list(range(1, N + 1, 1))
res = []
i = 0
while queue:
    i += 1
    tmp = queue.pop(0)
    if i % K != 0:
        queue.append(tmp)
    else:
        res.append(tmp)
ans = ", ".join(map(str, res))
print('<' + ans + '>')