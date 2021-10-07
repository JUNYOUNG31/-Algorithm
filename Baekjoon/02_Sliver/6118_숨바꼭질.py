# 숨바꼭질

# 재서기는 수혀니와 교외 농장에서 숨바꼭질을 하고 있다. 농장에는 헛간이 많이 널려있고 재서기는 그 중에 하나에
# 숨어야 한다. 헛간의 개수는 N(2 <= N <= 20,000)개이며, 1 부터 샌다고 하자.
# 재서기는 수혀니가 1번 헛간부터 찾을 것을 알고 있다. 모든 헛간은 M(1<= M <= 50,000)개의 양방향
# 길로 이어져 있고, 그 양 끝을 A_i 와 B_i(1<= A_i <= N; 1 <= B_i <= N; A_i != B_i)로 나타낸다.
# 또한 어떤 헛간에서 다른 헛간으로는 언제나 도달 가능하다고 생각해도 좋다.
# 재서기는 발냄새가 지독하기 때문에 최대한 냄새가 안나게 숨을 장소를 찾고자 한다. 냄새는 1번 헛간에서의
# 거리(여기서 거리라 함은 지나야 하는 길의 최소 개수이다)가 멀어질수록 감소한다고 한다. 재서기의 발냄새를
# 최대한 숨길 수 있는 헛간을 찾을 수 있게 도와주자!

# 첫 번째 줄에는 N과 M이 공백을 사이에 두고 주어진다.
# 이후 M줄에 걸쳐서 A_i와 B_i가 공백을 사이에 두고 주어진다.
from collections import deque


def bfs(i):                                         # bfs
    queue = deque()                                 # q
    queue.append(i)                                 # q 에 추가
    visited[i] = 1                                  # 방문처리
    while queue:                                    # 반복
        i = queue.popleft()                         # pop
        for j in tree[i]:                           # 해당 인덱스의 트리안에서 돌기
            if visited[j] == 0:                     # 방문하지않았다면
                visited[j] = visited[i]+1           # 기존의 값에 1 추가
                queue.append(j)                     # q 에 추가


N, M = map(int, input().split())                    # 헛간개수 길개수
tree = [[] for _ in range(N+1)]                     # 트리 생성
for i in range(M):                                  # 노드 입력
    A, B = list(map(int, input().split()))
    tree[A].append(B)                               # 양방향
    tree[B].append(A)
visited = [0 for _ in range(N+1)]                   # 방문체크
bfs(1)                                              # bfs 반복
max_cnt = max(visited)                              # 길이의 최대값
idx = visited.index(max_cnt)                        # idx 찾고
cnt = visited.count(max_cnt)                        # 카운트 하고
# for i in range(N, 0, -1):
#     if visited[i] == max_cnt:
#         cnt += 1
#         idx = i
#         if cnt == max_cnt:
#             break
print("{} {} {}".format(idx, max_cnt-1, cnt))       # 출력
# print(tree)
# print(visited)