# 주식가격

# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를
# return 하도록 solution 함수를 완성하세요.

def solution(prices):
    N = len(prices)                      # 주식의 시간길이
    answer = [0] * N                     # 정답 리스트
    for i in range(N):                   # 완탐
        for j in range(i+1, N):          # 그다음 인덱스부터 탐색
            if prices[i] <= prices[j]:   # 다음 값이 크면
                answer[i] += 1           # 안떨어지니깐 1 추가
            elif prices[i] > prices[j]:  # 떨어지면
                answer[i] += 1           # 떨어지는데까지 1초라서 1 추가
                break                    # 멈춰
    return answer



from collections import deque


def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        time = 0
        price = q.popleft()
        for i in q:
            time += 1
            if i < price:
                break
        answer.append(time)
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))