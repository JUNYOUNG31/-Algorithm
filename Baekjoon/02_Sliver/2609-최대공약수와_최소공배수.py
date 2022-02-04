# 최대공약수와 최소공배수

# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.


a, b = map(int, input().split())


def high(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def low(a, b):
    return a * b // high(a, b)


print(high(a, b))
print(low(a, b))