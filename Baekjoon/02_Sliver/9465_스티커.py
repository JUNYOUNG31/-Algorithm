# 스티커

# 상근이의 여동생 상냥이는 문방구에서 스티커 2n개를 구매했다. 스티커는 그림 (a)와 같이 2행 n열로 배치되어 있다.
# 상냥이는 스티커를 이용해 책상을 꾸미려고 한다.
# 상냥이가 구매한 스티커의 품질은 매우 좋지 않다. 스티커 한 장을 떼면, 그 스티커와 변을 공유하는 스티커는
# 모두 찢어져서 사용할 수 없게 된다. 즉, 뗀 스티커의 왼쪽, 오른쪽, 위, 아래에 있는 스티커는 사용할 수 없게 된다.
# 모든 스티커를 붙일 수 없게된 상냥이는 각 스티커에 점수를 매기고, 점수의 합이 최대가 되게 스티커를 떼어내려고 한다.
# 먼저, 그림 (b)와 같이 각 스티커에 점수를 매겼다. 상냥이가 뗄 수 있는 스티커의 점수의 최댓값을 구하는 프로그램을
# 작성하시오. 즉, 2n개의 스티커 중에서 점수의 합이 최대가 되면서 서로 변을 공유 하지 않는 스티커 집합을 구해야 한다.

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 n (1 ≤ n ≤ 100,000)이 주어진다.
# 다음 두 줄에는 n개의 정수가 주어지며, 각 정수는 그 위치에 해당하는 스티커의 점수이다.
# 연속하는 두 정수 사이에는 빈 칸이 하나 있다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

T = int(input())                                   # case 입력
for tc in range(T):                                # case 반복
    n = int(input())                               # 스티커 개수
    num1 = list(map(int, input().split()))         # 1번줄
    num2 = list(map(int, input().split()))         # 2번줄
    if n == 1:                                     # n이 1일때
        print(max(num1[0], num2[0]))               # 그냥 max 값
    elif n == 2:                                   # n이 2일떄
        max_dp1 = [num1[0], num2[0] + num1[1]]     # 대각선끼리의 합의 max 값
        max_dp2 = [num2[0], num1[0] + num2[1]]
        print(max(max(max_dp1), max(max_dp2)))
    else:                                          # 3부터는 dp로 값을 추가해주면서 max 값 찾기
        max_dp1 = [num1[0], num2[0] + num1[1]]     # dp 에 추가
        max_dp2 = [num2[0], num1[0] + num2[1]]
        for i in range(2, n):
            dp1 = max(max_dp2[i-1], max_dp2[i-2])+num1[i]  # 2의 dp 2개 값이랑 자신이랑 더햇을때의 max
            dp2 = max(max_dp1[i-1], max_dp1[i-2])+num2[i]  # 1의 dp 2개 값이랑 자신이랑 더햇을때의 max
            max_dp1.append(dp1)                            # dp1 에 추가
            max_dp2.append(dp2)                            # dp2 에 추가
        # print(max_dp1)
        # print(max_dp2)
        max_dp = max(max_dp1[-1], max_dp2[-1])           # max 값중에서 max 값
        print(max_dp)

