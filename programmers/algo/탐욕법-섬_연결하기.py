# 섬 연결하기

# n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때
# 필요한 최소 비용을 return 하도록 solution을 완성하세요.다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고
# 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

def solution1(n, costs):
    answer = 0
    adj_arr = [[987654321] * (n) for _ in range(n)]
    for i in range(len(costs)):
        n1 = costs[i][0]
        n2 = costs[i][1]
        w = costs[i][2]
        adj_arr[n1][n2] = w
    print(adj_arr)
    dist = [98756321] * (n)
    visited = [0] * (n)
    dist[0] = 0
    for _ in range(n-1):
        min_idx = -1
        min_value = 987654321
        for i in range(n):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = True
        for i in range(n):
            if not visited[i] and dist[i] > dist[min_idx] + adj_arr[min_idx][i]:
                dist[i] = dist[min_idx] + adj_arr[min_idx][i]
    return dist[n-1]


def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    p = list(range(n))
    ans = 0
    pick = 0
    idx = 0

    def find_set(x):
        if p[x] != x:
            p[x] = find_set(p[x])
        return p[x]

    def union(x, y):
        p[find_set(y)] = find_set(x)

    while pick < n - 1:
        x = costs[idx][0]
        y = costs[idx][1]

        if find_set(x) != find_set(y):
            union(x, y)
            pick += 1
            ans += costs[idx][2]

        idx += 1
    return ans















n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

print(solution(n,costs))