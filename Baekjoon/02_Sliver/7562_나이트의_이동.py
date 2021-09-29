# 나이트의 이동

# 체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다.
# 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

# 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
# 각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다.
# 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다.
# 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.
from collections import deque

dr = [-2, -1, 1, 2, 2, 1, -1, -2]  # 1시 2시 4시 5시 7시 8시 10시 11시
dc = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(r, c):                                                      # bfs 함수
    queue = deque()                                                 # q
    queue.append((r, c))                                            # q 에 추가
    while queue:                                                    # q 가 있으면
        r, c = queue.popleft()                                      # pop 하고
        if r == goal_r and c == goal_c:                             # goal 지점에 도착하면
            print(chess[r][c])                                      # 출력
            return
        for d in range(8):                                          # 방향 정해서
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < l and 0 <= nc < l and chess[nr][nc] == 0:  # 값이 0일때
                chess[nr][nc] = chess[r][c] + 1                     # 1씩 추가
                queue.append((nr, nc))                              # q 에 추가 하고


T = int(input())                                                    # case 입력
for tc in range(1, T+1):                                            # case 반복
    l = int(input())                                                # 체스판 크기
    chess = [[0] * l for _ in range(l)]                             # 0 으로 맵 만들기
    r, c = map(int, input().split())                                # 출발지
    goal_r, goal_c = map(int, input().split())                      # 도착지
    bfs(r, c)                                                       # bfs 시작
