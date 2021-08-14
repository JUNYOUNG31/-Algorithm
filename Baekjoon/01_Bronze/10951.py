# A + B -4
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
while True:
    try:                                   # try 문으로 예외발생시 멈추기
        A, B = map(int, input().split())   # 입력 2개 를 받아서
        print(A + B)                       # 두개의 합을 출력
    except:
        break
