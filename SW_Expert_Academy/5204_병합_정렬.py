# 병합 정렬

# 알고리즘 교수님은 학생들에게 병합 정렬을 이용해 오름차순으로 정렬하는 과제를 내려고 한다.
# 정렬 된 결과만으로는 실제로 병합 정렬을 적용했는지 알 수 없기 때문에 다음과 같은 제약을 주었다.
# N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할 한다.
# 병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.
# 정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다.
# 알고리즘 교수님의 조건에 따라 병합 정렬을 수행하는 프로그램을 만드시오.

# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 정수의 개수 N이 주어지고, 다음 줄에 N개의 정수 ai가 주어진다.
# 5<=N<=1,000,000, 0 <= ai <= 1,000,00

def merge_sort(arr):                # merge_sort 함수
    if len(arr) == 1:               # 1이하면
        return arr                  # 리턴
    mid = len(arr) // 2             # 중간값
    l = arr[:mid]                   # 왼쪽에 넣고
    r = arr[mid:]                   # 오른쪽에 넣고
    left = merge_sort(l)            # 정렬 돌리고
    right = merge_sort(r)           # 정렬 돌리고
    return merge(left, right)       # 두개를 병합


def merge(left, right):                          # 병합
    global cnt                                # 답
    ans = []
    idx_left = 0                                 # 인덱스 변수
    idx_right = 0                                # 인덱스 변수
    if left[len(left)-1] > right[len(right)-1]:  # 왼쪽마지막 값이 오른쪽 마지막 값보다 크면 답 + 1
        cnt += 1

    while len(left) > idx_left and len(right) > idx_right:  # 반복문
        if left[idx_left] < right[idx_right]:               # 왼쪽 값이 작으면
            ans.append(left[idx_left])                      # 정답 리스트에 추가
            idx_left += 1                                   # 인덱스 증가
        else:                                               # 오른쪽이 더크면
            ans.append(right[idx_right])                    # 정답리스트에 추가
            idx_right += 1                                  # 인덱스 증가

    while idx_left < len(left):                             # 인덱스가 길이보다 작으면
        ans.append(left[idx_left])                          # 값 추가하고
        idx_left += 1                                       # 인덱스 증가

    while idx_right < len(right):                           # 인덱스가 길이보다 작으면
        ans.append(right[idx_right])                        # 값 추가하고
        idx_right += 1                                      # 인덱스 증가

    return ans                                              # 정답 리턴


T = int(input())                                            # case 수
for tc in range(1, T+1):                                    # case 반복
    N = int(input())                                        # 개수 입력
    L = list(map(int, input().split()))                     # 리스트 입력
    cnt = 0                                                 # cnt
    result = merge_sort(L)                                  # 함수 실행
    print("#{} {} {}".format(tc, result[N//2], cnt))