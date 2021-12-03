# 동철이의 일 분배

# 동철이가 차린 전자회사에는 N명의 직원이 있다. 그런데 어느 날 해야할 일이 N개가 생겼다.
# 동철이는 직원들에게 공평하게 일을 하나씩 배분하려고 한다. 직원들의 번호가 1부터 N까지 매겨져 있고,
# 해야 할 일에도 번호가 1부터 N까지 매겨져 있을 때,i번 직원이 j번 일을 하면 성공할 확률이 Pi, j이다.
# 여기서 우리는 동철이가 모든 일이 잘 풀리도록 도와주어야 한다.
# 직원들에게 해야 할 일을 하나씩 배분하는 방법은 여러 가지다.
# 우리는 여러 방법 중에서 생길 수 있는 “주어진 일이 모두 성공할 확률”의 최댓값을 구하는 프로그램을 작성해야 한다.

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다. 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1 ≤ N ≤ 16)이 주어진다.
# 다음 N개의 줄의 i번째 줄에는 N개의 정수 Pi, 1, … , i, N(0 ≤ Pi, j ≤ 100)이 주어진다.
# Pi, j는 i번 사람이 j번 일을 성공할 확률을 퍼센트 단위로 나타낸다.
def works(idx, x):                                  # 작업
    global ans                                      # 작업의 최대값
    if ans >= x:                                    # 최대값이 크거나 같으면 반환
        return
    if idx == N:                                    # 인덱스를 다돌면
        if ans <= x:                                # 최대값 갱신하고
            ans = x
        return                                      # 반환
    for i in range(N):                              # N 만큼돌아서
        if visited[i] == 0:                         # 방문안했으면
            visited[i] = 1                          # 방문처리하고
            works(idx + 1, x * work[idx][i] / 100)  # 확률이니깐 100으로 나눈다
            visited[i] = 0


T = int(input())                                    # case 수
for tc in range(1, T+1):                            # case 반복
    N = int(input())                                # 입력
    work = list(list(map(int, input().split())) for _ in range(N)) # 작업 입력
    visited = [0] * N                               # 방문처리
    ans = 0                                         # 최대값
    works(0, 1)                                     # 함수 돌리고
    ans = round(ans * 100, 6)                       # 6번째자리까지
    print("#{} {:.6f}".format(tc, ans))             # 출력