# 뱀

# 'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다.
# 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
# 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다.
# 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.
# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다.
# 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.
# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)
# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터
# X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며,
# 방향 전환 정보는 X가 증가하는 순으로 주어진다.
from collections import deque

dr = [0, 1, 0, -1]                      # 우 하 좌 상
dc = [1, 0, -1, 0]


def gogo():                             # 함수
    r, c = 0, 0                         # 초기값 0, 0
    queue = deque()                     # Q
    queue.append((r, c))                # q 에 추가
    time = 0                            # 시간
    d = 0                               # 첫 번째 방향
    i = 0                               # 명령어 인덱스
    apple[r][c] = 9                     # 방문시 9로 바꾸기
    while queue:                        # q 가 있으면
        if time == cmd[i][0]:           # 만약 명령어의 시간과 같다면
            if cmd[i][1] == "L":        # 왼쪽이면
                d = (d-1) % 4             # 왼쪽으로 90도
                i += 1                  # 다음명령어로
            elif cmd[i][1] == "D":      # 오른쪽이면
                d = (d+1) % 4             # 오른쪽으로 90도
                i += 1                  # 다음명령어
        time += 1                       # 시간을 추가
        nr = r + dr[d]                  # 한칸 전진
        nc = c + dc[d]                  # 한칸 전진
        # for q in range(6):
        #     print(apple[q])
        # print(time)
        # print("-------------------------")
        if 0 <= nr < N and 0 <= nc < N and apple[nr][nc] == 1:    # 1이있다면 (사과)
            apple[nr][nc] = 9                                     # 방문처리
            queue.append((nr, nc))                                # q 에 추가
            r = nr                                                # 초기화
            c = nc                                                # 초기화
        elif 0 <= nr < N and 0 <= nc < N and apple[nr][nc] == 0:  # 0이면 (사과없으면)
            apple[nr][nc] = 9                                     # 방문체크
            queue.append((nr, nc))                                # q 에 추가
            tail_a, tail_b = queue.popleft()                      # 맨앞 팝( 꼬리지우기)
            apple[tail_a][tail_b] = 0                             # 0으로 바꾸기
            r = nr                                                # 초기화
            c = nc                                                # 초기화
        else:
            return time                                           # 시간을 리턴


N = int(input())                                                  # 맵의 크기 입력
K = int(input())                                                  # 사과의 개수
apple = [[0]*N for _ in range(N)]                                 # 맵 입력
for i in range(K):                                                # 사과 입력
    r, c = map(int, input().split())
    apple[r-1][c-1] = 1

L = int(input())                                                  # 명령어 개수
cmd = [] * L                                                      # 명령어
for i in range(L):                                                # 명령어 입력
    X, C = input().split()                              
    cmd.append([int(X), C])
cmd.append([0, 0])                                                # index 에러나서 맨뒤에 한개 추가
# print(cmd)
ans = gogo()                                                      # 함수돌리기
# for i in range(6):
#     print(apple[i])
print(ans)                                                        # 시간 출력
