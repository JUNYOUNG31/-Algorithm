# 반복수열

A, P = map(int, input().split())
arr = [A]
while True:
  ans = 0
  for i in str(arr[-1]):
    ans += int(i) ** P
  if ans in arr :
    break
  arr.append(ans)


print(arr.index(ans))