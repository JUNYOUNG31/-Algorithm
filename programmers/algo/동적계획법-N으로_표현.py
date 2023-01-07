# N으로 표현

# 아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.
# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5
# 5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
# 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중
# N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.


def solution(N, number):
    answer = 0
    all_numbers = [0]  # 모든수
    # 각 숫자 붙은거 추가
    for i in range(1, 9):
        dp = set()
        dp.add(int(str(N) * i))
        print(dp)
        # 3일때 1 2 2 1
        # 4일때 1 3 22 3 1
        for j in range(1, i):
            for x in all_numbers[j]:
                for y in all_numbers[i-j]:
                    dp.add(x+y)
                    dp.add(x-y)
                    dp.add(x*y)
                    if y != 0:
                        dp.add(x//y)
        if number in dp:
            answer = i
            break
        # 모든수에 추가
        all_numbers.append(dp)
    if answer == 0:
        answer = -1
    print(all_numbers)
    return answer


N = 5
number = 12

print(solution(N, number))