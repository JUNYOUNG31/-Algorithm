# 주사위

s1, s2, s3 = map(int, input().split())
arr = []
cnt = []
for i in range(1, s1 + 1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            arr.append(i + j + k)
arr.sort()
list_ans = list(set(arr))
for i in list_ans:
    cnt.append(arr.count(i))
ans = list_ans[cnt.index(max(cnt))]
print(ans)