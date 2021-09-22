# 두수의 합

# n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고,
# 1000000보다 작거나 같은 자연수이다. 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는
# (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

# 첫째 줄에 수열의 크기 n이 주어진다. 다음 줄에는 수열에 포함되는 수가 주어진다.
# 셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)
import sys

n = int(sys.stdin.readline())                        # 수열의 크기
num = list(map(int, sys.stdin.readline().split()))   # 수열 입력
x = int(sys.stdin.readline())                        # 두수의 합
num.sort()                                           # 정렬
cnt = 0                                              # 개수
i = 0                                                # 처음수
j = len(num) - 1                                     # 맨 뒷수
while i != j:                                        # 둘이 같으면 스톱
    if num[i] + num[j] == x:                         # 합이 x 면
        cnt += 1                                     # cnt + 1
        i += 1                                       # 작은 수 증가 
    elif num[i] + num[j] < x:                        # x 보다 작으면
        i += 1                                       # 작은수를 크게
    elif num[i] + num[j] > x:                        # x 보다 크면
        j -= 1                                       # 큰수를 작게

print(cnt)