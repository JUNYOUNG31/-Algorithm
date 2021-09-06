# 한수

# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고,
# N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

def hansu(n):                              # 함수 설정
    cnt = 0                                # 개수
    for i in range(1, n+1):                # 1부터 N 까지
        num_list = []                      # 리스트화
        for j in list(str(i)):             # str 로 바꾸고 각자리의 값을
            num_list.append(int(j))        # 숫자로 변환해서 리스트에 추가
        if i < 100:                        # 100보다 작으면
            cnt += 1                       # +1
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]: # 리스트의 첫번째 두번째수의 차이 = 두번째 3번째의 차이
            cnt += 1                       # +1
    return cnt                             # cnt 반환


N = int(input())                           # 입력
print(hansu(N))                            # 출력
