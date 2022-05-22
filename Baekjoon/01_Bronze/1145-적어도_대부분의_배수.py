# 적어도 대부분의 배수

arr = list(map(int, input().split()))
n = 1
while True:
    cnt = 0
    for i in arr:
        if n % i == 0:
            cnt += 1
    if cnt >= 3:
        print(n)
        break
    n += 1