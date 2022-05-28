# 대칭 차집합

num1, num2 = map(int, input().split())
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))
print(len(A - B) + len(B - A))