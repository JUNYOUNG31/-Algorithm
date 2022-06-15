# 집 주소

while True:
    arr = []
    N = input()
    if N == '0':
        break
    for i in N:
        arr.append(i)
    cnt = 0
    for i in arr:
        cnt += 1
        if i == '0':
            cnt += 4
        elif i == '1':
            cnt += 2
        else:
            cnt += 3
    cnt += 1
    print(cnt)