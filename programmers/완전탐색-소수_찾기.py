# 소수 찾기

# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지
# return 하도록 solution 함수를 완성해주세요.
from itertools import permutations


def solution(numbers):
    answer = 0                                
    num = [i for i in numbers]                 # 각자리별로 나누기
    N = len(num)                               # 숫자 개수
    permutation = []                           # 수열
    num_list = []                              # 숫자로 만들어 담을 리스트
    for i in range(1, N+1):                    # 숫자 개수 만큼
        permutation += permutations(num, i)    # 1개부터 N 개까지 만들기
    permutation_set = set(permutation)         # 중복 제거
    for i in permutation_set:                  # 제거된거에서
        x = int(''.join(i))                    # 숫자로 만들고
        if x not in num_list:                  # 리스트에 없으면
            num_list.append(x)                 # 추가
    # print(permutation)
    # print(permutation_set)
    # print(num_list)
    for i in num_list:                         # 숫자를 돌려서
        check = 1                              # 췤
        if i < 2:                              # 2보다 작으면
            check = 0                          # 소수아님
        for j in range(2, round(i**0.5 + 1)):  # 제곱근까지 돌려서
            if i % j == 0:                     # 나누어 떨어지면
                check = 0                      # 소수아님
        if check == 1:                         # 다돌고도 췤이면
            answer += 1                        # 개수 추가
    return answer


numbers = "011"
print(solution(numbers))


# def solution(numbers):
#     answer = 0
#     num = [i for i in numbers]
#     N = len(num)
#     sel = [0] * N
#     list_num = []
#     def perm(idx, check: int):
#         # if check == (1 << N) - 1:
#         if idx == N:
#             # print(sel)
#             list_num.append(sel[:])
#             return
#
#         for j in range(N):
#             # 해당 비트자리 사용했는지 쳌
#             if check & (1 << j): continue
#
#             sel[idx] = num[j]  # 값 표시
#             # 해당 자리 썼다라고 포함시키고 내려보내기
#             perm(idx + 1, check | (1 << j))
#     perm(0, 0)
#     print(list_num)
#     return answer