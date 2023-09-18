# 소수의 연속합

N = int(input())
arr = []


def prime_list(n):                           # 에라토스테네스의 체 구하는 법
    sieve = [True] * n                       # n 만큼 TRUE 만들기
    sieve[0] = False                         # 예외 처리
    sieve[1] = False
    m = int(n ** 0.5)                        # 제곱근 값
    for i in range(2, m + 1):                # 2부터 제곱근까지
        if sieve[i] == True:                 # i가 소수인 경우
            for j in range(i + i, n, i):     # i이후 i의 배수들을 False 판정
                sieve[j] = False
    return [i for i in range(n) if sieve[i] == True]  # M 부터 n 까지 의 약수 리턴


arr = prime_list(4000000)

hap = 0  # 누적 합
now = 0  # 현재 idx
cnt = 0
print(arr[:13])

# 처음부터 탐색
for i in range(len(arr)):
    # 누적 합이 현재 값보다 작으면
    # i 부터 계속 더 해보기
    while hap < N:
        hap += arr[now]
        now += 1

    # 현재 값이랑 같으면 추가
    if hap == N:
        cnt += 1
        # print(now, hap)

    # 커졌으면 처음꺼 빼고 다음거 부터 다시 시작
    hap -= arr[i]
    # print(hap)
print(cnt)
