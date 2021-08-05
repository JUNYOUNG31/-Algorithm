# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
# 1.X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2.X가 2로 나누어 떨어지면, 2로 나눈다.
# 3.1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
# 연산을 사용하는 횟수의 최솟값을 출력하시오.

# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

N = int(input())
count = 0
num =[N]
if N == 1:    # N이 1일 경우 연산할 필요가 없으므로 0 출력
    print(0) 

else:         # 3가지 방법을 이용하는 경우의 수를 모두 탐색
    while True:
        count +=1
        list_n = []

        for n in num:
            if n % 3 == 0 :     # 1번 연산
                list_n.append(n//3)
            
            if n % 2 == 0 :     # 2번 연산
                list_n.append(n//2)
            
            list_n.append(n-1)  # 3번 연신

        if 1 in list_n:  #연산의 결과가 1이 되는 순간 while 탈출
            break

        num = list(set(list_n)) # 중복된 값을 제거
    
    print(count)
