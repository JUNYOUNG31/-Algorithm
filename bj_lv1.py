# A + B ?
a, b , c= map(int, input().split())
print(a + b + c)

# A - B ?
a, b = map(int, input().split())
print(a - b)

# A * B ?
a, b = map(int, input().split())
print(a * b)

# A / B ?
a, b = map(int, input().split())
print(a / b)

# 사칙연산
a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)

#나머지
a, b, c = map(int, input().split())
print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c) * (b%c))%c)

# 곱셈
a = int(input())
b = int(input())
print((a*(b%10)))
print(a*((b//10)%10))
print(a*(b//100))
print(a*b)