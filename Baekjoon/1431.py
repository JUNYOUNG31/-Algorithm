# 다솜이는 기타를 많이 가지고 있다. 그리고 각각의 기타는 모두 다른 시리얼 번호를 가지고 있다.
#  다솜이는 기타를 빨리 찾아서 빨리 사람들에게 연주해주기 위해서 기타를 시리얼 번호 순서대로 정렬하고자 한다.
# 모든 시리얼 번호는 알파벳 대문자 (A-Z)와 숫자 (0-9)로 이루어져 있다.
# 시리얼번호 A가 시리얼번호 B의 앞에 오는 경우는 다음과 같다.
# A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
# 만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
# 만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.
# 시리얼이 주어졌을 때, 정렬해서 출력하는 프로그램을 작성하시오.

# 첫째 줄에 기타의 개수 N이 주어진다. N은 1,000보다 작거나 같다. 둘째 줄부터 N개의 줄에 시리얼 번호가 하나씩 주어진다. 
# 시리얼 번호의 길이는 최대 50이고, 알파벳 대문자 또는 숫자로만 이루어져 있다. 시리얼 번호는 중복되지 않는다.

N = int(input())                     # N : 기타의 개수
serial_add = []                      # serial 의 리스트
for n in range(N):          
    serial = input()                 # 시리얼 값을 N 만큼 입력
    serial_add += [serial]           # 리스트에 더해준다.

serial_sort = []                     # 정렬된 시리얼 값
for i in range(0,len(serial)-1):     # index i : 0 부터 끝 앞까지
    for j in range(i+1,len(serial)): # index j : i 다음부터 끝까지
        # 1. A와 B의 길이가 다르면
        if len(serial[i]) > len(serial[j]): # i번째 값의 길이가 j번째 값의 길이보다 클때
            serial[i],serial[j] = serial[i],serial[j] # 두수의 자리 바꾸기
        # 2. 만약 서로 길이가 같다면
        elif len(serial[i]) == len(serial[j]): #i,j번째 값이 같을때
            sum_i = 0
            sum_j = 0
            result = filter(int,serial)

            if sum_i > sum_j:
                serial[i],serial[j] = serial[i],serial[j]

        # 3. 만약 1,2번 둘 조건으로도 비교할 수 없으면
        else:
            serial_sort = sorted(serial_add)
        
print(serial_sort)
