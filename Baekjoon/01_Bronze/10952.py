# A + B -5
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
ans = 0                                # 반복조건
while ans == 0:                        # 0이라면
    A, B = map(int, input().split())   # 입력 2개 를 받아서
    if A != 0 and B != 0:              # 만약 두값이 0이 아니라면
        print(A + B)                   # 두개의 합을 출력
    else:                              # 둘다 0 이면
        ans = 1                        # 반복문을 종료하기위해 1로 변경