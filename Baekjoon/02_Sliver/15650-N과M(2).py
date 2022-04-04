# N과 M

N, M = map(int, input().split())

visited = [False] * (N + 1)
answer = []


def dfs(start, a):
    if a == 0:
        print(" ".join(map(str, answer)))
        return

    for i in range(start, N + 1):
        if not visited[i]:
            answer.append(i)
            visited[i] = True
            dfs(i, a - 1)
            answer.pop()
            visited[i] = False


dfs(1, M)