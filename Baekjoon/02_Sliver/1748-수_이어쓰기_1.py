# 수 이어쓰기 1

N = input()
cnt = len(N) - 1
c = 0
i = 0
while i < cnt:
    c += 9 * (10 ** i) * (i + 1)
    i += 1
c += ((int(N) - (10 ** cnt)) + 1) * (cnt + 1)
print(c)