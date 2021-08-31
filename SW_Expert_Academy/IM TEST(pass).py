def change(i):                      # 배수에 해당하는 값을 바꿔준다.
    for j in range(i, N+1, i):      # i 부터 N + 1 까지 i만큼 점프하면서
        if LED[j] == 0:             # LED 가 꺼져 있으면
            LED[j] = 1              # 켜주고
        else:                       # LED 가 켜져 있으면
            LED[j] = 0              # 꺼준다
                                    # 바뀔게 없으면 자동 종료 됨


T = int(input())                    # case 수
for tc in range(1, T+1):            # case 반복
    N = int(input())                # 스위치의 개수
    LED = [-1] + [0] * N            # LED의 초기 상태 0으로 N 개 설정. 0번 인덱스를 -1 로 줘서 스위치 번호와 인덱스를 일치 시킨다.
    P = [-1] + list(map(int, input().split()))  # 패턴 입력
    cnt = 0                         # 변경 수
    for i in range(1, N + 1):       # 1번 스위치 부터 반복
        if P[i] == 1:               # 패턴이 켜진 상태이고
            if LED[i] == 0:         # LED 가 꺼져있다면
                change(i)           # LED 상태 변경
                cnt += 1            # cnt 1 증가
        elif P[i] == 0:             # 패턴이 꺼진 상태이고
            if LED[i] == 1:         # LED가 켜져있다면
                change(i)           # LED 상태 변경
                cnt += 1            # cnt 1 증가

    print("#{} {}".format(tc, cnt)) # 출력