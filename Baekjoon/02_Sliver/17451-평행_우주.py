# 평행 우주


n = int(input())
arr = list(map(int, input().split()))
v = arr[-1]

for i in range(n-2, -1, -1):
  if arr[i] < v:
    if v % arr[i] == 0:
      continue
    v = ((v // arr[i])+1) * arr[i]
  else:
    v = arr[i]

print(v)