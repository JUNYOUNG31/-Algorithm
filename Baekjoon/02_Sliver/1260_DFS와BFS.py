# dfs와 bfs

# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
# 입력으로 주어지는 간선은 양방향이다.
from collections import deque


def dfs(i):                                  # dfs
    tree[i].sort()                           # 작은거 부터 넣어야하니깐 정렬
    visited_dfs[i] = 1                       # 방문체크 1
    ans_dfs.append(i)                        # i 를 정답에 추가
    for j in tree[i]:                        # 트리의 각 요소를 탐색해서
        if visited_dfs[j] == 0:              # 방문한게 없다면            
            dfs(j)                           # j 를 다시해서 탐색을 계속한다.


def bfs(i):                                  # bfs
    tree[i].sort()                           # 이것도 정렬
    q = deque()                              # q 에 넣고
    q.append(i)                              # i 추가하고   
    visited_bfs[i] = 1                       # 방문처리
    while q:                                 # 반복해서
        i = q.popleft()                      # i 를 pop하고
        ans_bfs.append(i)                    # i 를 정답리스트에 추가
        for j in tree[i]:                    # 트리의 각 요소를 탐색해서
            if visited_bfs[j] == 0:          # 방문안하면
                q.append(j)                  # q 에 추가하고
                visited_bfs[j] = 1           # 방문처리


N, M, V = list(map(int, input().split()))    # 정점수 노드수 시작점

tree = [[] for _ in range(N+1)]              # 트리 
visited_dfs = [0 for _ in range(N+1)]        # 방문할 dfs 배열
visited_bfs = [0 for _ in range(N+1)]        # 방문할 bfs 배열   
ans_dfs = []                                 # dfs 정답 리스트
ans_bfs = []                                 # bfs 정답 리스트
for i in range(M):                           # 노드 입력
    a, b = list(map(int, input().split()))
    tree[a].append(b)                        # 트리에 양방향으로 추가
    tree[b].append(a)
dfs(V)                                       # dfs
bfs(V)                                       # bfs
print(*ans_dfs)                              # 출력
print(*ans_bfs)