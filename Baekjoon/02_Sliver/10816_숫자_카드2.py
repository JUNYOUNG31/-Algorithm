# 숫자 카드 2

# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.


# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
# 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는
# -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고
# 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다.
# 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
import sys

N = int(sys.stdin.readline())                            # 가지고 있는 카드 수
card_N = list(map(int, sys.stdin.readline().split()))    # 가지고 잇는 카드
M = int(sys.stdin.readline())                            # 몇개 가지고 있는 지 확인 할 카드 수
card_M = list(map(int, sys.stdin.readline().split()))    # 확인할 카드

count = dict()
for i in card_N:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in card_M:
    if i in count:
        print(count[i], end=" ")
    else:
        print(0, end=" ")

# # 이진탐색
# def binarySearch(a, key):               # 2진 탐색 함수
#     start = 1                           # 시작은 1페이지
#     end = a                             # 끝 페이지
#     cnt = 0                             # 2진 탐색한 횟수
#     while start <= end:                 # 1부터 400까지
#         middle = int((start + end)/2)   # c= int((l+r)/2)
#         cnt += 1                        # 카운트 1 증가
#         if middle == key:               # 그값이 같다면
#             return cnt                  # 횟수 반환
#         elif middle > key:              # 중간값이 찾는 값보다 크면
#             end = middle                # 끝값이 중간값
#         else:                           # 중간값이 찾는 값보다 작으면
#             start = middle              # 시작값이 중간값
#     return cnt                          # cnt 반환