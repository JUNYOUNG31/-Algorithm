# 소수 구하기

# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오

# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000)
# M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

def prime_list(n):                           # 에라토스테네스의 체 구하는 법
    sieve = [True] * n          # n 만큼 TRUE 만들기
    sieve[0] = False                         # 예외 처리
    sieve[1] = False
    m = int(n ** 0.5)                        # 제곱근 값
    for i in range(2, m + 1):                # 2부터 제곱근까지 
        if sieve[i] == True:                 # i가 소수인 경우
            for j in range(i + i, n, i):     # i이후 i의 배수들을 False 판정
                sieve[j] = False
    return [i for i in range(M, n) if sieve[i] == True] # M 부터 n 까지 의 약수 리턴


M, N = map(int, (input().split()))           # M N 입력
ans = prime_list(N+1)                        # 정답에 저장
for i in range(len(ans)):                    # 길이만큼 반복해서
    print(ans[i])                            # 출력



