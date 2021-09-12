# 트리의 부모 찾기

# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
import sys                          # sys 시간초과...
sys.setrecursionlimit(10**6)

def dfs(i):                             # dfs
    visited[i] = 1                      # 방문체크 1
    for j in tree[i]:                   # 트리의 각 요소를 탐색해서
        if visited[j] == 0:             # 방문한게 없다면
            ans[j] = i                  # j 의 부모는 i 로 설정
            dfs(j)                      # j 를 다시해서 탐색을 계속한다.


N = int(sys.stdin.readline())           # 노드의 개수
tree = [-1] + [[] for _ in range(N)]    # 트리를 저장할 배열인데 0인덱스를 -1 설정한다 1부터 시작하니깐
visited = [-1] + [0 for _ in range(N)]  # 방문할 배열도 0인덱스를 -1 로 설정
ans = [-1] + [0 for _ in range(N)]      # 정답 리스트의 0인덱스도 -1 로 설정
for i in range(N - 1):                  # N-1 개만큼 반복해서
    a, b = list(map(int, sys.stdin.readline().split())) # 각노드를 입력받고
    tree[a].append(b)                                   # 트리에 양방향으로 추가
    tree[b].append(a)
dfs(1)                                                  # 1부터 시작하니깐 1부터 넣기
for i in range(2, N+1):                                 # 2번 노트부터 부모를 출력
    print(ans[i])
