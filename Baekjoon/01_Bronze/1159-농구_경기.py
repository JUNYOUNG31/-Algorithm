# 농구 경기

N = int(input())
name = []
ans = []
for _ in range(N):
    temp = input()
    name.append(temp[0])
first = set(name)
for i in first:
    if name.count(i) >= 5:
        ans.append(i)
if len(ans) > 0:
    print(''.join(sorted(ans)))
else:
    print('PREDAJA')