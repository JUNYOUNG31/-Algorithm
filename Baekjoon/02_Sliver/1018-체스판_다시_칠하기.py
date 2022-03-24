# 체스판 다시 칠하기

N, M = map(int, input().split())
board = []
ans = []

for _ in range(N):
    board.append(input())

for i in range(N - 7):
    for j in range(M - 7):
        idx1 = 0
        idx2 = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (l + k) % 2 == 0:
                    if board[k][l] != 'W':
                        idx1 += 1
                    if board[k][l] != 'B':
                        idx2 += 1
                else:
                    if board[k][l] != 'B':
                        idx1 += 1
                    if board[k][l] != 'W':
                        idx2 += 1
        ans.append(idx1)
        ans.append(idx2)

print(min(ans))