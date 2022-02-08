# 이항 계수1

# 자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수
# \(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

N, K = map(int, input().split())
def fact(N):
    if N <= 1:
        return 1
    return N * fact(N-1)
print(fact(N) // (fact(N-K) * fact(K)))