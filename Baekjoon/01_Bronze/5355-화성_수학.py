# 화성 수학

T = int(input())

for tc in range(T):
    arr = list(map(str, input().split()))
    ans = 0
    for i in range(len(arr)):
        if i == 0:
            ans += float(arr[i])
        else:
            if arr[i] == "@":
                ans *= 3
            if arr[i] == "%":
                ans += 5
            if arr[i] == "#":
                ans -= 7
    print("%0.2f" % ans)