# 구명보트
# 무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고,
# 무게 제한도 있습니다.예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이
# 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로
# 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.
# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.
# 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때,
# 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

def solution(people, limit):
    answer = 0
    heavy_people = sorted(people, reverse=True)                  # 무거운 순으로 정렬
    # print(heavy_people)
    max_p = 0                                                    # 제일 무거운사람
    min_p = len(people)-1                                        # 제일 가벼운사람
    while max_p <= min_p:                                        # 반복
        if heavy_people[max_p] + heavy_people[min_p] <= limit:   # 제일무거운사람 + 가벼운사람 이 리미트 보다 작으면
            min_p -= 1                                           # 인덱스 줄이고
            max_p += 1                                           # 인덱스 늘리고
            answer += 1                                          # 보트 1추가
        else:                                                    # 넘엇으면 무거운사람만 타라
            max_p += 1                                           # 탓으면 다음사람
            answer += 1                                          # 보트 추가
    return answer


people = [70, 50, 80, 50]
limit = 100

print(solution(people, limit))