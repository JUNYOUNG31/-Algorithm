# 도둑질

# 도둑이 어느 마을을 털 계획을 하고 있습니다. 이 마을의 모든 집들은 아래 그림과 같이 동그랗게 배치되어 있습니다.
# 각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.
# 각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.


def solution(money):
    answer = []                          # 정답 리스트
    house = [0] * len(money)             # 집의 개수
    house[0] = money[0]                  # 0번집부터 털 경우
    for i in range(2, len(house)-1):     # 2번집부터 마지막 집 앞까지
        # 최대값(전집의 결과값 ,  1칸 뛴집의 결과값 + 현재집의 돈, 2칸 뛴집의 결과값 + 현재집의 돈)
        house[i] = max(house[i-1], house[i-2] + money[i], house[i-3] + money[i])
    answer.append(max(house))            # 최대값 추가

    house1 = [0] * len(money)            # 새로운 집의 개수
    house1[1] = money[1]                 # 1번집부터 털 경우
    for i in range(3, len(house1)):      # 3번집부터 마지막 집까지
        house1[i] = max(house1[i - 1], house1[i - 2] + money[i], house1[i-3] + money[i])
    answer.append(max(house1))


    house2 = [0] * len(money)            # 새로운 집의 개수
    house2[2] = money[2]                 # 2번집부터 털 경우
    for i in range(4, len(house2)):      # 4번집부터 마지막 집까지
        house2[i] = max(house2[i - 1], house2[i - 2] + money[i], house2[i - 3] + money[i])
    answer.append(max(house2))

    # print(house)
    # print(house1)
    # print(house2)

    return max(answer)




money = [1, 2, 3, 1]
# print(solution([11,0,2,5,100,100,85,1]), 198)
print(solution([10, 2, 2, 100, 2]))
# print(solution(money))