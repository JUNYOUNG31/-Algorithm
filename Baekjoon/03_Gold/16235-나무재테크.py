# 나무 재테크

from collections import deque
from collections import defaultdict

import sys
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M, K = map(int, input().split())
A = []
for i in range(N):
    temp = list(map(int, input().split()))
    A.append(temp)

tree = defaultdict(deque)

for i in range(M):
    x, y, z = map(int, input().split())
    tree[x-1, y-1].append(z)

feed = [[5]*N for _ in range(N)]


def ssw():
    for i in range(N):
        for j in range(N):
            live = deque()
            addfeed = 0
            for k in tree[i, j]:             # tree[i, j][k] 인덱스로 돌지 않고 값으로 바로 접근하는게 시간이 빠르다.....
                if k <= feed[i][j]:          # 봄
                    feed[i][j] -= k

                    live.append(k+1)         # append가 pop보다 빠르다....?
                # 여름
                else:                        # 여기는 여름이라서 계절 봄이 끝나고 진행해야하는부분
                    addfeed += k//2          # 2로나눠서 양분에 추가
            tree[i, j] = live
            feed[i][j] += addfeed
            # 겨울
            feed[i][j] += A[i][j]            # A 배열만큼 양분 추가

    return


def a():                                               # 가을
    for i in range(N):
        for j in range(N):
            for k in tree[i, j]:
                if k % 5 == 0:                              # 5의 배수인지 확인
                    for d in range(8):                      # 팔방
                        nx = i + dx[d]
                        ny = j + dy[d]
                        if 0 <= nx < N and 0 <= ny < N:
                            tree[nx, ny].appendleft(1)      # deque의 맨앞에 추가
    return


for tc in range(K):
    ssw()
    a()

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(tree[i, j])

# print(tree)
print(ans)