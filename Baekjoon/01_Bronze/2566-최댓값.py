# 최댓값

pan = [list(map(int, input().split())) for _ in range(9)]

max_num = 0
max_r, max_c = 0, 0
for r in range(9):
    for c in range(9):
        if max_num <= pan[r][c]:
            max_r = r + 1
            max_c = c + 1
            max_num = pan[r][c]

print(max_num)
print(max_r, max_c)