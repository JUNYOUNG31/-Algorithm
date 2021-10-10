# 전기버스 2

# 충전지를 교환하는 방식의 전기버스를 운행하려고 한다. 정류장에는 교체용 충전지가 있는 교환기가 있고,
# 충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있다.
# 충전지가 방전되기 전에 교체하며 운행해야 하는데 교체하는 시간을 줄이려면 최소한의 교체 횟수로 목적지에 도착해야 한다.
# 정류장과 충전지에 대한 정보가 주어질 때, 목적지에 도착하는데 필요한 최소한의 교환횟수를 출력하는 프로그램을 만드시오.
# 단, 출발지에서의 배터리 장착은 교환횟수에서 제외한다.

# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50 다음 줄부터 테스트 케이스의 별로 한
# 줄에 정류장 수 N, N-1개의 정류장 별 배터리 용량 Mi가 주어진다. 3<=N<=100, 0 ＜ Mi ＜ N
def e_bus(idx, cnt):                             # 전기버스
    global ans
    if ans < cnt:                                # 가지치기
        return
    if idx + station[idx] >= N:                   # idx에 배터리를 더한값이 정류장 수를 넘으면
        if ans > cnt:                             # 종점까지 가니깐
            ans = cnt                             # 갱신
    for i in range(idx + station[idx], idx, -1):  # 뒤에서 탐색해서
        cnt += 1                                  # 배터리를 1늘리고
        e_bus(i, cnt)                             # 가지는지 확인
        cnt -= 1                                  # 다시 백


T = int(input())                                  # case 입력
for tc in range(1, T+1):                          # case 반복
    station = list(map(int, input().split()))     # 정류장수랑 충전량
    N = station[0]                                # 정류장 수
    ans = 132456                                  # 최소 변경 수
    e_bus(1, 0)
    print("#{} {}".format(tc, ans))
