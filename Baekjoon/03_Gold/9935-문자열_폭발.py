# 문자열 폭발

arr = list(input())
boom = list(input())
stack = []
num = len(boom)
for i in arr:
    stack.append(i)
    if num <= len(stack):
        if boom == stack[-num:]:
            for j in range(num):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")