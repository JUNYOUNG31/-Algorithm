# 선 긋기

# 매우 큰 도화지에 자를 대고 선을 그으려고 한다. 선을 그을 때에는 자의 한 점에서 다른 한 점까지 긋게 된다.
# 선을 그을 때에는 이미 선이 있는 위치에 겹쳐서 그릴 수도 있는데, 여러 번 그은 곳과 한 번 그은 곳의 차이를 구별할 수 없다고 하자
# 이와 같은 식으로 선을 그었을 때, 그려진 선(들)의 총 길이를 구하는 프로그램을 작성하시오. 선이 여러 번 그려진 곳은 한 번씩만 계산한다.

import sys  # 시간초과때문에 추가

N = int(input())
line = []
hap = 0
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    line.append((x, y))

line.sort()
start = line[0][0]  # 초기값
end = line[0][1]

for i in range(1, N):
    temp_x = line[i][0]
    temp_y = line[i][1]
    if temp_x <= end:    # 새로운 시작이 끝보다 앞이면
        end = max(temp_y, end)  # 끝만 갱신
    else:
        hap += end-start    # 아니면 선을 추가
        start = temp_x
        end = temp_y

hap += end - start

print(hap)

