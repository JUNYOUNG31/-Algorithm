# 앵그리 창영

N, W, H = map(int, input().split())
for i in range(N):
    num = int(input())
    temp = (W ** 2 + H ** 2) ** 0.5
    if num <= temp:
        print("DA")
    else:
        print("NE")