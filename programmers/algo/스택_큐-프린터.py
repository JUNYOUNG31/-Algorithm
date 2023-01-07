# 프린터

# 일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다.
# 이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다.
# 이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.
# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.
# 예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고 중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.
# 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다. 위의 예에서 C는 1번째로, A는 3번째로 인쇄됩니다.
# 현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의
# 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지
# return 하도록 solution 함수를 작성해주세요.


def solution(priorities, location):
    answer = 1
    index = [0] * len(priorities)                 # index 리스트
    index[location] = 1                           # 찾을 인덱스 표시
    while True:
        if priorities[0] == max(priorities):      # 0번 인덱스값이 중요도가 제일 낮다면( 값이 제일 크다면)
            if index[0] == 1:                     # 인덱스의 값이 1 이면
                return answer                     # 찾는 숫자이므로 카운트 출력
            answer += 1                           # 아니면 cnt 1증가하고
            priorities.pop(0)                     # 중요도가 작은 순서니깐 pop
            index.pop(0)                          # index 1개 pop
        else:                                     # 중요도가 제일 낮지않으면 맨뒤로 보내기
            priorities.append(priorities.pop(0))  # pop 하고 append
            index.append(index.pop(0))            # index도 pop 하고 append 해서 맞추기
        print(priorities)


priorities = [2, 1, 3, 2]
# priorities = [1, 1, 9, 1, 1, 1]
location = 2
# location = 0
print(solution(priorities, location))