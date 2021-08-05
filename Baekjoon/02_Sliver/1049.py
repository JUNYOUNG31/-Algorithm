# Day Of Mourning의 기타리스트 강토가 사용하는 기타에서 N개의 줄이 끊어졌다.
#  따라서 새로운 줄을 사거나 교체해야 한다. 강토는 되도록이면 돈을 적게 쓰려고 한다.
#  6줄 패키지를 살 수도 있고, 1개 또는 그 이상의 줄을 낱개로 살 수도 있다.
# 끊어진 기타줄의 개수 N과 기타줄 브랜드 M개가 주어지고, 
# 각각의 브랜드에서 파는 기타줄 6개가 들어있는 패키지의 가격,# 낱개로 살 때의 가격이 주어질 때, 
# 적어도 N개를 사기 위해 필요한 돈의 수를 최소로 하는 프로그램을 작성하시오.

#첫째 줄에 N과 M이 주어진다. 
# N은 100보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다.
# 둘째 줄부터 M개의 줄에는 각 브랜드의 패키지 가격과 낱개의 가격이 공백으로 구분하여 주어진다. 
# 가격은 0보다 크거나 같고, 1,000보다 작거나 같은 정수이다.


N , M = map(int , input().split())      # N : 기타줄 수  M : 브랜드 수
list_price =[]                          # 가격의 리스트 변수
box_price = []                          # 패키지의 가격 리스트 변수
one_price = []                          # 낱개의 가격 리스트 변수
min_money = 0                           # 최소 가격
for _ in range(M):                      # 브랜드만큼 반복
    price= list(map(int , input().split())) # 패키지와 낱개의 가격을 리스트화
    list_price+=[price]                     # 가격 리스트에 추가
for i in list_price:                        # 가격 리스트 반복
    box_price.append(i[0])                  # 인덱스 0 의 값들을 패키지 리스트로 변환
    one_price.append(i[1])                  # 인덱스 1 의 값들을 낱개 리스트로 변환
min_box = min(box_price)                    # 패키지중 최소가격
min_one = min(one_price)                    # 낱개중 최소가격

if min_box /6 < min_one :                   # 패키지의 1개 값이 낱개보다 저렴할 경우
    min_money = (min_box * (N//6)) + min(min_box,(N%6)*min_one) # 최소값은 N 개줄을 6개로 나눈 후 패키지값을 곱하고 남은 가격에서
                                                                # 패키지 1개 가격과 낱개가격의 나머지만큼 곱한 값의 최소값을 더한다.
else:    # 아닐 경우는 낱개가격이 패키지 가격보다 저렴하므로 낱개가격 곱하기 N 개
    min_money = min_one * N
    
print(min_money)

# if N%6 == 0 : #6의 배수일경우
#     if (min_box * (N//6)) <= (min_one * N) :
#         min_money = (min_box * (N//6))
#     else :
#         min_money = (min_one * N)
# elif N%6 != 0:
#     if (min_box * ((N//6)+1)) <= ((min_box * (N//6))+(min_one * (N%6))) :
#         min_money = (min_box * ((N//6)+1))
#     else:
#         min_money = ((min_box * (N//6))+(min_one * (N%6)))

