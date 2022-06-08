# 성지키기

N, M = map(int,input().split())
arr = []
row = []
col = []
for _ in range(N):
    arr.append(input())
for i in range(N):
    row.append("X" not in arr[i])
for j in range(M):
    col.append("X" not in [arr[i][j] for i in range(M)])
ans = max(sum(row), sum(col))
print(ans)