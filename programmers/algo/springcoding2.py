# 스프링 코딩2

import sys
sys.setrecursionlimit(1000000)
# 재귀 설정

def solution(grid):
    num1 = len(grid)
    num2 = len(grid[0])
    pan = []
    for i in grid:
        pan.append(list(i))
    new_grid = [[0 for _ in range(num2)] for _ in range(num1)]
    visited = [[0 for _ in range(num2)] for _ in range(num1)]
    for i in range(num1):
        for j in range(num2):
            if pan[i][j] == "#":
                new_grid[i][j] = 1
            if pan[i][j] == ".":
                new_grid[i][j] = 0
    # 맨윗
    for j in range(num2):
        if new_grid[0][j] == 0:
            check(new_grid,visited, 0, j)
    # 맨오른
    for i in range(num1):
        if new_grid[i][num2-1] == 0:
            check(new_grid, visited, i, num2-1)
    # 맨아래
    for j in range(num2-1,0,-1):
        if new_grid[num1-1][j] == 0:
            check(new_grid, visited, num1-1, j)
    # 맨왼
    for i in range(num1-1,0,-1):
        if new_grid[i][0] == 0:
            check(new_grid, visited, i, 0)

    for i in new_grid:
        print(i)

    answer = 0
    for i in range(num1):
        for j in range(num2):
            if new_grid[i][j] != 99:
                answer += 1

    return answer


def check(new_grid, visited, r, c):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    new_grid[r][c] = 99
    visited[r][c] = 1
    for d in range(4):
        nx = r + dx[d]
        ny = c + dy[d]
        if 0 <= nx < len(new_grid) and 0 <= ny < len(new_grid[0]):
            if new_grid[nx][ny] == 0:
                if visited[nx][ny] == 0:
                    check(new_grid, visited, nx, ny)






grid = [".....####", "..#...###", ".#.##..##", "..#..#...", "..#...#..", "...###..."]
solution(grid)
