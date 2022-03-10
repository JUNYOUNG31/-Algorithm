# 탑 보기

# 일직선으로 다양한 높이의 건물이 총 $N$개가 존재한다. 각 건물 옥상에서 양 옆에 존재하는 건물의 옆을 몇 개 볼
# 수 있는지 궁금해졌다.
# i번쨰 건물 기준으로 i - 1, i - 2, ..., 1번째 건물은 왼쪽에, i + 1, i + 2, ..., N번째 건물은 오른쪽에 있다.
# 각 건물 사이의 거리는 다 동일하다. 현재 있는 건물의 높이가 L이라고 가정하면 높이가 L보다 큰 곳의 건물만 볼 수 있다.
# 바라보는 방향으로 높이가 L인 건물 뒤에 높이가 L이하인 건물이 있다면 가려져서 보이지 않는다.
# 번호	                    1   	2	    3         	4	    5	        6	    7	        8
# 높이                    	3	    7	    1	        6	    3	        5	    1	        7
# 보이는 건물 번호	        2	    x	    2, 4, 8	    2, 8	2,4,6,8	    2,4,8	2,4,6,8	    x
# 각 건물에서 볼 수 있는 건물들이 어떤것이 있는지 구해보자.

N = int(input())
top = list(map(int, input().split()))
stack = []
ans = [[0, 0] for _ in range(N+1)]
for i in range(N):
    print(i+1, top[i])
    while stack and stack[-1][1] <= top[i]:                # 스택이 있을때만 돌리고
        stack.pop()               # 그탑은 지우고 그다음왼쪽탑
    stack.append([i+1, top[i]])             # 끝나면 이번꺼 추가가
    print(stack)
    if stack:                       # 스택이 남아있으면 맨오른쪽 스택이 수신기
        ans[i][0] += len(stack)

stack = []

for i in range(N):
    print(i+1, top[i])
    while stack and stack[-1][1] <= top[i]:                # 스택이 있을때만 돌리고
        stack.pop()               # 그탑은 지우고 그다음왼쪽탑
    stack.append([i+1, top[i]])             # 끝나면 이번꺼 추가가
    print(stack)
    if stack:                       # 스택이 남아있으면 맨오른쪽 스택이 수신기
        ans[i][0] += len(stack)

