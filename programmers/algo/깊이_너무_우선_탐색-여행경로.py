# 여행경로

# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.
# 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
# 제한사항
# 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
# 주어진 공항 수는 3개 이상 10,000개 이하입니다.
# tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
# 주어진 항공권은 모두 사용해야 합니다.
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
# 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

def solution(tickets):
    answer = []
    routes = {}                                            # 경로
    for i in tickets:                                       # 티켓을 반복
        if i[0] in routes:                                  # 출발지가 루트에 잇으면
            routes[i[0]].append(i[1])                       # 출발지에 도착지 추가
        else:                                               # 없으면
            routes[i[0]] = [i[1]]                           # 출발지랑 도착지 추가
    for i in routes.keys():                                 # 역순으로 정렬
        routes[i].sort(reverse=True)
    stack = ["ICN"]                                         # 스택
    while stack:                                            # 스택
        first = stack[-1]                                   # 처음
        if first not in routes or len(routes[first]) == 0:  # 경로에 없고 남은게 없으면 
            answer.append(stack.pop())                      # 정답에 추가
        else:                                               # 
            stack.append(routes[first].pop())               # 스텍에 루트에서 빼서 추가
    return answer[::-1]                                     # 반전


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))