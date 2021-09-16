# 수 찾기

# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데,
# 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -2**31 보다 크거나 같고 2**31보다 작다.
import sys


def binary_search(num):                 # 이분 탐색
    start = 0                           # 시작값
    end = N - 1                         # 끝값
    while start <= end:                 # 시작이 끝보다 작거나 같을때까지
        mid = (start + end) // 2        # 중간값 인덱스
        if A[mid] == num:               # 중간값이 찾는 값과 같으면
            return 1                    # 1을 반환
        elif A[mid] < num:              # 더 크면
            start = mid + 1             # 시작을 중간값보다 1큰 값으로
        elif A[mid] > num:              # 작으면
            end = mid - 1               # 끝을 중간값보다 1작은 값으로
    return 0


N = int(sys.stdin.readline())                           # 숫자의 개수
A = list(map(int, sys.stdin.readline().split()))        # 숫자의 리스트
A.sort()                                                # 정렬 한번 해주고
M = int(sys.stdin.readline())                           # 찾을 숫자의 개수
check = list(map(int, sys.stdin.readline().split()))    # 찾는 숫자
for i in range(M):                                      # 반복해서
    print(binary_search(check[i]))                      # 출력



