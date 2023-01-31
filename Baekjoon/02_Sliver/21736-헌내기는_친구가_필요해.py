# 헌내기는 친구가 필요해

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1234568)

N, M = map(int, input().split())  # 캠퍼스 크기 크기 결정
box = []                          # 캠퍼스 맵
r = 0                             # 주인공 위치 row y 좌표
c = 0                             # 주인공 위치 column x 좌표
cnt = 0                           # 사람의 수
for i in range(N):
    line = list(input())
    box.append(line)
    if 'I' in line:               # 현재 주인공 위치
        c = line.index('I')       #  x좌표
        r = i                     #  y좌표

visit = [[False] * M for _ in range(N)]  #지나간곳은 다시가지않기위한 map
def function(R,C):                       # row column
    global cnt                           # 위의 변수와 리스트 사용
    visit[R][C] = True                   # 지나간 자리가 있다면 True
    if box[R][C] == 'P':
        cnt+=1
    moving = [[1,0],[-1,0],[0,1],[0,-1]] #상하좌우
    for j in moving:
        move_c = C+j[1]
        move_r = R+j[0]
        if (0 <= move_r < N and 0 <= move_c < M) and box[move_r][move_c] != 'X':
            if visit[move_r][move_c] == False:
                function(move_r, move_c)

function(r,c)


if cnt == 0:
    cnt ='TT'
print(cnt)


