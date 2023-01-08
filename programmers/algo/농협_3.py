# 농협 3

def solution(blocks):
    answer = [[]]
    y = len(blocks)
    x = len(blocks[0])
    for i in range(y):
        print(blocks[i])

    def move():
        for i in range(y-1, 0, -1):
            for j in range(x-1, -1, -1):
                if blocks[i-1][j] == 1:
                    if blocks[i][j] == 1:
                        continue
                    if blocks[i][j] == 2:
                        continue
                    if blocks[i][j] == 3:
                        continue
                    if blocks[i-2][j] == 3:
                        continue
                    if blocks[i-1][j-1] == 3:
                        continue
                    if blocks[i-1][j+1] == 3:
                        continue
                    blocks[i][j] = blocks[i-1][j]
                    blocks[i-1][j] = 0

    for i in range(y):
        move()

    answer = blocks
    return answer



print(solution([[1,1,0,1],[0,1,1,2],[3,0,0,1],[0,1,0,2],[0,0,0,0]]))
