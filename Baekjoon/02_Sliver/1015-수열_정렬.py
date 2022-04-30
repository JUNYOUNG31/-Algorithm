# 수열 정렬

N = int(input())
A = list(map(int, input().split()))

B = A.copy()
B.sort()
ans = []
for i in A:
    cnt = 0
    while True:
        if B.index(i) + cnt in ans:
            cnt += 1
        else:
            break
    ans.append(B.index(i)+cnt)

print(*ans)