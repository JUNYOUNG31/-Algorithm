# 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 
# 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

# 첫째 줄에 N의 진짜 약수의 개수가 주어진다. 이 개수는 50보다 작거나 같은 자연수이다.
# 둘째 줄에는 N의 진짜 약수가 주어진다.
# 1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.

T = int(input())                     # 약수의 개수
A = list(map(int , input().split())) # 약수 나열
max_A = max(A)                       # 약수 중 제일 큰 값
min_A = min(A)                       # 약수 중 제일 작은 값
N = max_A * min_A                    # 작은값 곱하기 큰값은 N 자신
for a in A:                          # 약수 들 중
    if N%a != 0:                     # N을 약수로 나눴을때 0이 아니면
        N = False                    # 약수가 아니므로 Flase
        break                        # 끝
print(N)                             