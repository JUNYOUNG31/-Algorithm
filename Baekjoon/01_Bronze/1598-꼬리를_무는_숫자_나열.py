# 꼬리를 무는 숫자 나열

num1, num2 = map(int, input().split())
x1 = (num1-1) // 4 + 1
y1 = (num1-1) % 4
x2 = (num2-1) // 4 + 1
y2 = (num2-1) % 4
print(abs(x2-x1) + abs(y2-y1))