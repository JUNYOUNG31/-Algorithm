# 터렛

# 조규현과 백승환은 터렛에 근무하는 직원이다. 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다.
# 다음은 조규현과 백승환의 사진이다. 이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다.
# 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다. 조규현의 좌표 (x1, y1)와 백승환의 좌표
# (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때,
# 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

T = int(input())
for tc in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = (((x1-x2)**2) + ((y1-y2)**2)) ** 0.5

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue
    if r1 > d + r2 or r2 > d + r1 or d > r1 + r2:  # 반지름을 더한 값보다 작을떄, 한원이 다른 원을 포함할떄
        print(0)
    elif r1 == d + r2 or r2 == d + r1 or r1 + r2 == d:  # 외저 ㅂ내접
        print(1)
    else:
        print(2)