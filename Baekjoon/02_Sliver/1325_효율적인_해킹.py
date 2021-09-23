# 효율적인 해킹

# 해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다.
# 김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.
# 이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는
# B를 해킹하면, A도 해킹할 수 있다는 소리다.
# 이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의
# 번호를 출력하는 프로그램을 작성하시오.

# 첫째 줄에, N과 M이 들어온다. N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다.
# 둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다.
# 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.
import sys
from collections import deque


def bfs(i):                                  # bfs
    visited = [0 for _ in range(N + 1)]      # 방문할 dfs 배열
    q = deque()                              # q 에 넣고
    q.append(i)                              # i 추가하고
    visited[i] = 1                           # 방문처리
    cnt = 0
    while q:                                 # 반복해서
        i = q.popleft()                      # i 를 pop하고
        for j in tree[i]:                    # 트리의 각 요소를 탐색해서
            if visited[j] == 0:              # 방문안하면
                q.append(j)                  # q 에 추가하고
                visited[j] = 1               # 방문처리
                cnt += 1
    return cnt


N, M = list(map(int, sys.stdin.readline().split()))       # 개수와 노드 입력
tree = [[] for _ in range(N+1)]                           # 트리
cnt_list = {}                                             # cnt 딕셔너리
for i in range(M):                                        # 노드반복
    A, B = list(map(int, sys.stdin.readline().split()))   # 노드 입력
    tree[B].append(A)                                     # 트리에 단방향으로 추가
# print(tree)
for i in range(1, N+1):                                   # 개수만큼 cnt 딕셔너리에 추가
    cnt_list[i] = bfs(i)                                  # bfs return 값이 cnt
# print(cnt_list)
ans = []                                                  # 정답리스트
for i in cnt_list.keys():                                 # 키값중에서
    if cnt_list[i] == max(cnt_list.values()):             # max 값만 저장
        ans.append(i)

print(*ans)                                               # 출력
