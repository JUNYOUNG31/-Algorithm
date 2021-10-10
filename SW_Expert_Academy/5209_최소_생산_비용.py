# 최소 생산 비용

# A사는 여러 곳에 공장을 갖고 있다. 봄부터 새로 생산되는 N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산하려고 한다.
# 각 제품의 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산하는 프로그램을 만드시오.
# 예를 들어 3개의 제품을 생산하려는 경우 각 공장별 생산비용은 다음과 같이 주어진다..
# 이때 1-C, 2-A, 3-B로 제품별 생산 공장을 정하면 생산 비용이 21+11+31=63으로 최소가 된다.

# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 제품 수 N이 주어지고, 이후 제품당 한 줄 씩 N개의 줄에 걸쳐 공장별
# 생산비용 Vij가 주어진다. 3<=N<=15,   1<=Vij<=99
def min_price(idx, x):                                  # 최소값
    global hap                                          # 합
    if hap <= x:                                        # 가지치기
        return
    if idx == N:                                        # 탐색 완료후
        hap = min(x, hap)                               # 최소값을 저장
    for i in range(N):                                  # N 번반복
        if visited[i] == 0:                             # 방문안한행은
            visited[i] = 1                              # 방문체크
            min_price(idx + 1, x + prices[idx][i])      # 최값 검사
            visited[i] = 0                              # 방문체크 해제


T = int(input())                                    # case 입력
for tc in range(1, T+1):                            # case 반복
    N = int(input())                                # 입력
    prices = []                                     # 가격 리스트
    for i in range(N):                              # 가격 추가
        price = list(map(int, input().split()))
        prices.append(price)
    visited = [0] * N                               # 방문처리
    hap = 10000                                     # min 구해야하니깐 높게 설정
    min_price(0, 0)                                 # idx 랑 값 변수
    print("#{} {}".format(tc, hap))