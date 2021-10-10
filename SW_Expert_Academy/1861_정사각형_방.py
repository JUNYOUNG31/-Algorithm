# 정사각형 방

# N2개의 방이 N×N형태로 늘어서 있다.
# 위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N2 이하의 수 Ai,j가 적혀 있으며, 이 숫자는 모든 방에 대해 서로 다르다.
# 당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.
# 물론 이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
# 처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라.

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N (1 ≤ N ≤ 103)이 주어진다.
# 다음 N개의 줄에는 i번째 줄에는 N개의 정수 Ai, 1, … , Ai, N (1 ≤ Ai, j ≤ N2) 이 공백 하나로 구분되어 주어진다.
# Ai, j는 모두 서로 다른 수이다.

dr = [1, 0, -1, 0]                      # 하좌상우
dc = [0, -1, 0, 1]


def check(r, c):                                                # 한칸이동가능한지 여부 확인하기
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and room[nr][nc] == room[r][c] + 1:
            visited[room[i][j]] = 1                             # 방문 체크


T = int(input())                                                # case 입력
for tc in range(1, T+1):                                        # case 반복
    N = int(input())                                            # 방의 크기
    room = [list(map(int, input().split())) for _ in range(N)]  # 방입력
    visited = [0] * (N**2 + 1)                                  # 방문 확인
    for i in range(N):                                          # 전체탐색
        for j in range(N):
            check(i, j)                                         # 방문체크하고
    cnt = 1                                                     # 인덱스
    max_cnt = 0                                                 # 최대 이동수
    min_nums = 0                                                # 최대방의 번호중 작은거
    for i in range(N**2, -1, -1):                               # 뒤에서 탐색
        if visited[i]:                                          # 값이있으면 이동가능
            cnt += 1                                            # cnt  증가
        else:                                                   # 값이없으면 이동불가
            if max_cnt <= cnt:                                  # 현재 인덱스값이 최대값인지 확인
                max_cnt = cnt                                   # 갱신
                min_nums = i + 1                                # 현재의 숫자는 index + 1
            cnt = 1                                             # cnt 갱신
    print("#{} {} {}".format(tc, min_nums, max_cnt))