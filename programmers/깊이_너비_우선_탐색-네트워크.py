# 네트워크

# 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어,
# 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때
# 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두
# 같은 네트워크 상에 있다고 할 수 있습니다. 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가
# 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

def solution(n, computers):
    answer = 0
    visit = [0] * n
    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            bfs(i, visit, computers)
            answer += 1
    return answer


def bfs(i, visit, computers):
    queue = []
    queue.append(i)
    while len(queue) != 0:
        com = queue.pop(0)
        for i in range(len(computers)):
            if computers[com][i] == 1 and visit[i] == 0:
                queue.append(i)
                visit[i] = 1

















# dr = [1, 0, -1, 0]                      # 하좌상우
# dc = [0, -1, 0, 1]
#
# def solution(n, computers):
#     answer = 0
#     visited = [[0]*n for _ in range(n)]
#     for i in range(n):  # 전체 탐색해서
#         for j in range(n):
#             if visited[i][j] == 0 and computers[i][j] == 1:  # 방문안했으면
#                 computers[i][j] = 0
#                 bfs(i, j, visited, n, computers)  # bfs 돌리고
#                 answer += 1  # 카운트 추가
#                 for k in range(n):
#                     print(visited[k])
#                 print(answer)
#     return answer
#
#
# def bfs(r, c, visited, n, computers):
#     queue = []
#     queue.append((r, c))
#     while queue:
#         r, c = queue.pop(0)
#         # visited[r][c] = 1
#         for d in range(4):
#             nr = r + dr[d]
#             nc = c + dc[d]
#             if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
#                 if computers[nr][nc] == 1:
#                     visited[nr][nc] = 1
#                     queue.append((nr, nc))




n = 5
computers = [[1, 1, 1, 0, 0], [ 1, 1, 0, 0, 0], [ 1, 0, 1, 0, 0 ],[0, 0, 0, 1, 1],[  0, 0, 0, 1, 1]]



print(solution(n, computers))