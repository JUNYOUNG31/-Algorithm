# 슈퍼 마리오

arr = []
cnt = 0
for i in range(10):
    arr.append(int(input()))
for i in arr:
    cnt += i
    if cnt >= 100:
        if cnt - 100 > 100 - (cnt - i):
            cnt -= i
        break
print(cnt)