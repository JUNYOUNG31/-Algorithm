# 양팔저울

num = int(input())
gram = list(map(int, input().split()))
check_num = int(input())
check_gram = list(map(int, input().split()))

dp = [0 for _ in range(40001)]
dp[0] = 1

for i in range(num):
    arr = [0 for _ in range(40001)]
    for j in range(40000, -1, -1):
        if dp[j]:
            arr[j] = 1
            arr[j + gram[i]] = 1
            if gram[i] - j >= 0:
                arr[gram[i] - j] = 1
            if j - gram[i] >= 0:
                arr[j - gram[i]] = 1
    dp = arr[:]

for i in check_gram:
    if dp[i]:
        print("Y", end=" ")
    else:
        print("N", end=" ")