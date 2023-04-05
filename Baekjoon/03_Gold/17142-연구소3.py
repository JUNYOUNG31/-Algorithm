# 연구소 3
from collections import deque
from itertools import combinations
import copy

dr = [1,0,-1,0]
dc = [0,1,0,-1]

N, M = map(int, input().split())
pan = []
time_list = []
for i in range(N):
    temp = list(map(int, input().split()))
    pan.append(temp)

# 바이러스의 위치
virus_list = []
for i in range(N):
    for j in range(N):
        if pan[i][j] == 1:                  # 벽을 -1로 변경
            pan[i][j] = -1
        if pan[i][j] == 2:                  # 바이러스 위치 저장
            virus_list.append((i, j))

M_list = list(combinations(virus_list, M))  # 바이러스 위치 M 개


def bfs(i):
    visitied = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()
    for q in i:                         # q 에 추가
        queue.append(q)
    time = 0                                # 시간
    while True:
        num = len(queue)                    # q 한 싸이클의 길이
        zero_cnt = 0                        # 0이 없는 줄 수
        for i in range(N):
            if 0 not in new_pan[i]:         # 0 이 없다면
                zero_cnt += 1               # 0이 없는 줄 수 +1
        if num == 0 or zero_cnt == N:       # q를 다돌거나 모든 구역에 0 이 없다면
            if zero_cnt == N:               # 0 이없는지 확인
                return time
            else:                           # 0 이 있으면 최대값을 저장
                return 999999999999
        time += 1                           # 사이클 당 시간 +1

        for i in range(num):
            r, c = queue.popleft()
            visitied[r][c] = 1
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < N:  # 범위 안이고
                    if visitied[nr][nc] != 1:
                        if new_pan[nr][nc] == 0:     # 빈칸이면
                            new_pan[nr][nc] = 2      # 바이러스 감염
                            visitied[nr][nc] = 1
                            queue.append((nr, nc))
                        elif new_pan[nr][nc] == 1:   # 비활성 바이러스면
                            new_pan[nr][nc] = 2      # 활성
                            visitied[nr][nc] = 1
                            queue.append((nr, nc))

# 바이러스 비활성 체크
for i in M_list:
    new_pan = copy.deepcopy(pan)     # 새 판
    for j in virus_list:             # 바이러스 리스트에서
        if j not in i:               # 비활성화된 바이러스
            new_pan[j[0]][j[1]] = 1  # 1로 변경
    time = bfs(i)
    time_list.append(time)

answer = min(time_list)              # 시간 최소값
if answer == 999999999999:           # 불가능하면
    answer = -1                      # -1
print(answer)