# TV 크기

D, H, W = map(int, input().split())
num = D / ((H ** 2 + W ** 2) ** 0.5)
print(int(H * num), int(W * num))