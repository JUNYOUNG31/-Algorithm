# 싱기한 네자리 숫자란, [1000,9999]인 10진수 숫자중에서,  다음의 조건을 만족하는 숫자를 말한다.
# 숫자를 10진수, 12진수, 16진수로 나타낸 다음, 각각의 숫자에 대해,
# 각 숫자의 자리수를 더했을 때, 세 값이 모두 같아야 한다.
# 여러분은 싱기한 네자리 숫자를 모두 출력해야 한다.

# 입력은 주어지지 않는다.
for num in range(1000,10000):  # 네자리수의 범위 num
    num_10 = 0                 # 10진수의 각자리 숫자의 합
    num_12 = 0                 # 12진수의 각자리 숫자의 합
    num_16 = 0                 # 16진수의 각자리 숫자의 합
    
    number = num               # 다음 반복문에서 사용할 num 값을 변수로 받아서 사용
    for i in range(len(str(number))): # num 의 길이만큼 반복
        num_10 += number % 10  # 10으로 나누었을때 나머지의 합  = 각자리 숫자의 합
        number = number // 10  # 기존의 값을 10으로 나눈후 반복      
    number = num               # 변수의 초기화
    for i in range(4):
        num_12 += number % 12
        number = number // 12      
    number = num
    for i in range(4):
        num_16 += number % 16
        number = number // 16    

    if num_10 == num_12 == num_16 : # 3개의 합이 같을때 출력
        print(num)