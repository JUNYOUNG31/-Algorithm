# 트리의 지름

V = int(input())
tree = [[] for _ in range(V+1)]
for i in range(V):
    temp = list(map(int, input().split()))
    for j in range(1, len(temp), 2):
        if temp[j] == -1:
            break
        tree[temp[0]].append((temp[j], temp[j+1]))


max_1 = [-1 for _ in range(V + 1)]
max_1[1] = 0


def dfs(start, tree, max_1):
    for node, dis in tree[start]:
        if max_1[node] == -1:
            max_1[node] = max_1[start] + dis
            dfs(node, tree, max_1)


dfs(1, tree, max_1)
temp = max(max_1)
ans = [temp, max_1.index(temp)]


max_2 = [-1 for _ in range(V+1)]
max_2[ans[1]] = 0
dfs(ans[1], tree, max_2)

print(max(max_2))