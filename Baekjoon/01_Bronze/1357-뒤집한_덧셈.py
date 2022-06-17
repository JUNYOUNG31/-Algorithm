# 뒤집힌 덧셈

x, y = map(str, input().split())
num = str(int(x[::-1]) + int(y[::-1]))
print(int(num[::-1]))