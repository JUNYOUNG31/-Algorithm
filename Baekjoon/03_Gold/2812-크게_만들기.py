# 크게 만들기


N, K = map(int, input().split())
num = str(input())

ans = ''

arr = []
for i in num:
    while arr and i > arr[-1]:
        if K > 0:
            arr.pop()
            K -= 1
        else:
            break
    arr.append(i)
if K > 0:
    for i in range(K):
        arr.pop()

ans = ''.join(arr)

print(ans)