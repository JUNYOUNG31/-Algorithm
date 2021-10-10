# 이진 탐색

# 서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장한다. 그런 다음 리스트 B에 저장된 M개의 정수에
# 대해 A에 들어있는 수인지 이진 탐색을 통해 확인하려고 한다.전체 탐색 구간의 시작과 끝 인덱스를 l과 r이라고 하면,
# 중심 원소의 인덱스 m=(l+r)//2 이고, 이진 탐색의 왼쪽 구간은 l부터 m-1, 오른쪽 구간은 m+1부터 r이 된다.
# 이때 B에 속한 어떤 수가 A에 들어있으면서, 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게
# 되는 숫자의 개수를 알아보려고 한다. 이때 m에 찾는 원소가 있는 경우 방향을 따지지 않는다.
# M개의 정수 중 조건을 만족하는 정수의 개수를 알아내는 프로그램을 만드시오.

# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50 다음 줄부터 테스트 케이스의 별로 A와 B에
# 속한 정수의 개수 N, M이 주어지고, 두 줄에 걸쳐 N개와 M개의 백만 이하의 양의 정수가 주어진다.
# 1<=N, M<=500,000
def binarySearch(S, low, high, key):                # 이진탐색
    global flag_arr1, flag_arr2, cnt                #
    if low > high:                                  # 교재에잇는데 뭔지 까먹음
        return
    else:
        mid = (low + high) // 2                     # 중간값
        if key == S[mid]:                           # 찾는게 중간값이면
            cnt += 1                                # cnt +1
            return
        elif key < S[mid]:                          # 작고
            if not flag_arr1:                       # 방향과 다르면
                flag_arr1 = 1                       # 방향을 바꿔준다
                flag_arr2 = 0
                binarySearch(S, low, mid-1, key)    # 다시 돌리고
        elif key > S[mid]:                          # 크고
            if not flag_arr2:                       # 방향이 다르면
                flag_arr1 = 0                       # 방향 바꾸고
                flag_arr2 = 1
                binarySearch(S, mid+1, high, key)   # 진행


T = int(input())                                    # case 입력
for tc in range(1, T+1):                            # case 반복
    N, M = map(int, input().split())                # 반복 입력
    arr1 = list(map(int, input().split()))          # 리스트 1
    arr2 = list(map(int, input().split()))          # 리스트 2
    arr1.sort()                                     # 정렬하고
    arr2.sort()                                 
    cnt = 0 
    for i in arr2:                                  # B에서 
        flag_arr1 = 0                               # 방향 변수 설정
        flag_arr2 = 0
        binarySearch(arr1, 0, N-1, i)               # 돌린다
    print("#{} {}".format(tc, cnt))