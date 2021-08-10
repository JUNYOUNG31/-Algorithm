# 2020년에 입학한 헌내기 도연이가 있다. 도연이는 비대면 수업 때문에 학교에 가지 못해
# 학교에 아는 친구가 없었다. 드디어 대면 수업을 하게 된 도연이는 어서 캠퍼스 내의
# 사람들과 친해지고 싶다. 
# 도연이가 다니는 대학의 캠퍼스는  크기이며 캠퍼스에서 이동하는 방법은
# 벽이 아닌 상하좌우로 이동하는 것이다. 예를 들어, 도연이가 (, )에 있다면
# 이동할 수 있는 곳은 (, ), (, ), (, ), (, )이다. 단, 캠퍼스의 밖으로 이동할 수는 없다.
# 불쌍한 도연이를 위하여 캠퍼스에서 도연이가 만날 수 있는 사람의 수
# 를 출력하는 프로그램을 작성해보자.

# 첫째 줄에는 캠퍼스의 크기를 나타내는 두 정수  (),  ()이 주어진다.
# 둘째 줄부터 개의 줄에는 캠퍼스의 정보들이 주어진다.
# O는 빈 공간, X는 벽, I는 도연이, P는 사람이다. I가 한 번만 주어짐이 보장된다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1234568)
#백준에서 제시한 문제는 600 * 600으로 재귀 1000번 리미트 제한을 넘어버린다.....
# 그래서 이문제는 재귀를 사용하는 DFS가 아니라 BFS로 풀어야한다......쉣!
#위의 3줄은 그 한계를 임의로 푸는 구문이고 입출력 속도를 빠르게 해주는 구문

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
    if box[R][C] == 'P':                 # 현재위치가 P 이면 
        cnt+=1                           # cnt +1
    moving = [[1,0],[-1,0],[0,1],[0,-1]] #상하좌우
    for j in moving:                        
        move_c = C+j[1]                  # 기존의 위치를 이동한다.    
        move_r = R+j[0]       
        if (0 <= move_r < N and 0 <= move_c < M) and box[move_r][move_c] != 'X':
        # 범위안에 있고 and X 가 아니라면
            if visit[move_r][move_c] == False: # 지나간 자리가 아니라면
                function(move_r, move_c)       # 현재위치에서 다시 상하좌우 움직인다. 

function(r,c)

if cnt == 0:
    cnt ='TT'
print(cnt)