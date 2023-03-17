# 필터

R, C = map(int, input().split())
arr = []
for r in range(R):
    arr.append(list(map(int, input().split())))
T = int(input())
J = []
cnt = 0
for r in range(R-2):
    for c in range(C-2):
        Filter = []
        for i in range(r, r+3):
            for j in range(c, c+3):
                Filter.append(arr[i][j])

        Filter.sort()
        J.append(Filter[4])

for k in J:
    if k > T or k == T:
        cnt += 1

print(cnt)