# 1번문제
# 6종류(1원, 5원, 10원, 50원, 100원, 500원)의 동전을 생산하는 공장이 있습니다. 특정 금액만큼 동전을 생산해달라는 의뢰가 들어왔을 때, 최소 비용으로 그 금액만큼 동전을 생산하고자 합니다.
#
# 화폐 단위(원)	생산 단가(원)
# 1	1
# 5	4
# 10	99
# 50	35
# 100	50
# 500	1000
# 만약 각 동전의 생산 단가가 위의 표와 같고, 의뢰받은 금액이 4578원이라면, 최소의 비용으로 4578원어치의 동전을 생산하는 방법은 다음과 같습니다.
#
# 화폐 단위(원)	생산 단가(원)	생산 수량(개)	생산 비용(원)	생산 화폐 가치(원)
# 1	1	3	1 x 3 = 3	1 x 3 = 3
# 5	4	5	4 x 5 = 20	5 x 5 = 25
# 10	99	0	99 x 0 = 0	10 x 0 = 0
# 50	35	1	35 x 1 = 35	50 x 1 = 50
# 100	50	45	50 x 45 = 2250	100 x 45 = 4500
# 500	1000	0	1000 x 0 = 0	500 x 0 = 0
# 총 비용			3 + 20 + 35 + 2250 = 2308
# 총 화폐 가치				3 + 25 + 50 + 4500 = 4578
# 즉, 1원짜리 동전을 3개, 5원짜리 동전을 5개, 50원짜리 동전을 1개, 100원짜리 동전을 45개 생산하면 2308원이라는 최소 비용으로 4578원어치의 동전을 생산할 수 있습니다. 2308원보다 적은 비용으로 4578원어치의 동전을 생산할 수 있는 방법은 없습니다.
#
# 공장이 생산해야 하는 금액을 나타내는 정수 money, 6종류 동전의 생산 단가를 나타내는 1차원 정수 배열 costs가 매개변수로 주어집니다. money원만큼의 동전을 최소 비용으로 생산했을 때, 그 최소 비용을 return 하도록 solution 함수를 완성해주세요.

def solution(money, costs):
    answer = 0
    # 5원의 생산가격이 1원의 5개 가격보다 비쌀때
    if costs[1] > 5*costs[0]:
        # 5원의 생산가격을 1원의 5개 가격으로 바꾸기
        costs[1] = 5 * costs[0]
    # 10원의 생산가격이 5원의 2개 가격보다 비쌀때
    if costs[2] > 2 *costs[1]:
        # 10원의 생산가격을 5원의 2개 가격으로 바꾸기
        costs[2] = 2 * costs[1]
    # 50원의 생산가격이 10원의 5개 가격보다 비쌀때
    if costs[3] > 5 * costs[2]:
        # 50원의 생산가격을 10원의 5개 가격으로 바꾸기
        costs[3] = 5 * costs[2]
    # 100원의 생산가격이 50원의 2개 가격보다 비쌀때
    if costs[4] > 2 *costs[3]:
        # 100원의 생산가격을 50원의 2개 가격으로 바꾸기
        costs[4] = 2 * costs[3]
    # 500원의 생산가격이 100원의 5개 가격보다 비쌀때
    if costs[5] > 5 * costs[4]:
        # 500원의 생산가격을 100원의 5개 가격으로 바꾸기
        costs[5] = 5 * costs[4]

    # 500원 동전의 개수와 최소 비용 갱신
    a = money // 500
    money = money - 500 * a
    answer += costs[5] * a
    # 100원 동전의 개수와 최소 비용 갱신
    b = money // 100
    money = money - 100 * b
    answer += costs[4] * b
    # 50원 동전의 개수와 최소 비용 갱신
    c = money // 50
    money = money - 50 * c
    answer += costs[3] * c
    # 10원 동전의 개수와 최소 비용 갱신
    d = money // 10
    money = money - 10 * d
    answer += costs[2] * d
    # 5원 동전의 개수와 최소 비용 갱신
    e = money // 5
    money = money - 5 * e
    answer += costs[1] * e
    # 1원 동전의 개수와 최소 비용 갱신
    f = money // 1
    money = money - 1 * f
    answer += costs[0] * f

    return answer



money = 4578
costs = [1, 4, 99, 35, 50, 1000]

ans = solution(money, costs)

print(ans)