# 가장 먼 노드

# n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장
# 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의
# 개수가 가장 많은 노드들을 의미합니다. 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가
# 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.
from collections import deque

def solution(n, edge):
    answer = 0
    tree = [[] for _ in range(n + 1)]                 # 트리 생성
    visited = [0] * (n+1)
    for a, b in edge:                               # 노드 입력

        tree[a].append(b)
        tree[b].append(a)  # 추가
    # print(tree)

    queue = deque([1])
    visited[1] = 1
    while queue:
        q = queue.popleft()
        for i in tree[q]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[q] + 1

    print(visited)
    max_cnt = max(visited)
    answer = visited.count(max_cnt)
    return answer




n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n,edge))