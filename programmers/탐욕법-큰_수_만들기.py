# 큰 수 만들기

# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다. 예를 들어,
# 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.
# 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를
# 제거했을때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.
from itertools import combinations


def solution1(number, k):
    answer = ''
    list_num = []
    num = [i for i in number]
    length = len(num) - k
    # print(length)
    combination = list(combinations(num, length))
    # print(combination)
    for i in range(len(combination)):
        list_num.append(int(''.join(combination[i])))
    # print(list_num)
    answer = str(max(list_num))
    # print(type(answer))
    return answer


def solution(number, k):
    answer = ''
    num = []                        # 저장될 리스트
    for i in number:                # number 만큼 반복
        # print(i)
        while num and i > num[-1]:  # 넘의 마지막값보다 크면
            if k > 0:               # 제거할 숫자의 수가 0이상이면
                num.pop()           # 마지막꺼 팝하고
                k -= 1              # 제거할숫자 1개 제거
            else:                   # 0보다 작으면 멈춰
                break
        num.append(i)               # 그리고 추가
    if k > 0:                       # 0 보다 크 면
        for i in range(k):          # 반복해서
            num.pop()               # 팝하고 
    answer = ''.join(num)           # join 해주고
    return answer                   # 출력


number = "1231234"
k = 3

print(solution1(number, k))