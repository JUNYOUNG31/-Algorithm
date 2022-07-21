# 유진수

N = input()
cnt = len(N)
flag = 0
for i in range(cnt - 1):
    left = 1
    right = 1
    for j in range(i + 1):
        left *= int(N[j])

    for k in range(i + 1, cnt):
        right *= int(N[k])

    if left == right:
        print("YES")
        flag = 1
        break
if flag == 0:
    print("NO")