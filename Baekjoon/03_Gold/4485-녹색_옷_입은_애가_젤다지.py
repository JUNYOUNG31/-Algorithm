# 녹색 옷 입은 애가 젤다지

from heapq import heappush, heappop
import sys
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

INF = 99999999999999
input = sys.stdin.readline

cnt = 1


def func(cnt):
    dp = [[INF] * N for _ in range(N)]
    q = []
    heappush(q, [arr[0][0], 0, 0])
    dp[0][0] = 0
    while q:
        w, x, y = heappop(q)
        if x == N-1 and y == N-1:
            print("Problem {0}: {1}".format(cnt, w))
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                nw = w + arr[nx][ny]
                if nw < dp[nx][ny]:
                    dp[nx][ny] = nw
                    heappush(q, [nw, nx, ny])


while True:
    N = int(input())
    if N == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    func(cnt)
    cnt += 1