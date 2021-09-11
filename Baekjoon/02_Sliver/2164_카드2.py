# 카드2

# N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며,
# 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
# 이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다.
# 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# 예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다.
# 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고,
# 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.
# N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

# 첫째 줄에 정수 N(1 ≤ N ≤ 500,000)이 주어진다.
# import sys
# N = int(sys.stdin.readline())                 # 카드의 수
# list_N = []                      # 리스트
# for i in range(1, N+1):          # 카드를 1부터 N까지 넣기
#     list_N.append(str(i))        # list 에 추가
#
# while len(list_N) > 1:          # 1개남을때까지 반복
#     list_N.pop(0)                # 제일 처음 삭제
#     list_N.append(list_N.pop(0)) # 제일처음껄 삭제하고 맨뒤에 추가
#
# print(int(list_N[0]))            # 하나 남으니깐 0 인덱스 출력


from collections import deque
import sys

N = int(sys.stdin.readline())
d = deque()
for i in range(1, N+1):
    d.append(i)
while len(d) > 1:
    d.popleft()
    d.append(d.popleft())
print(*d)