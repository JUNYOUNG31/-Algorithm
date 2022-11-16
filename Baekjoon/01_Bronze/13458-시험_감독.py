# 시험 감독

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ans = 0

for i in A:
    i -= B
    cnt = 1
    if i > 0:
        cnt += i // C
        if i % C != 0:
            cnt += 1
    ans += cnt


print(ans)