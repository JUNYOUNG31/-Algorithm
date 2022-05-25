# 숫자 카드

N = int(input())
card = list(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))
card.sort()
for i in range(M):
    small, big = 0, N-1
    while small <= big:
        mid = (small + big) // 2
        if card[mid] == num[i]:
            print(1, end=" ")
            break
        elif card[mid] < num[i]:
            small = mid + 1
        else:
            big = mid - 1
        if small > big:
            print(0, end=" ")
            break