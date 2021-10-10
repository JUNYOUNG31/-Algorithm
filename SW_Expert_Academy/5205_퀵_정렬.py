# 퀵 정렬

# 퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고, A[N//2]에 저장된 값을 출력하는 프로그램을 만드시오.

# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 정수의 개수 N이 주어지고, 다음 줄에 N개의 정수 ai가 주어진다.
# 5<=N<=1,000,000, 0 <= ai <= 1,000,000
def quickSort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quickSort(A, l, s-1)
        quickSort(A, s+1, r)


def partition(A, l , r):
    p = A[l]
    i = l
    j = r
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i <= j :
            A[i], A[j] = A[j], A[i]

    A[l], A[j] = A[j], A[l]
    return j


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quickSort(arr, 0, N-1)
    print("#{} {}".format(tc, arr[N // 2]))