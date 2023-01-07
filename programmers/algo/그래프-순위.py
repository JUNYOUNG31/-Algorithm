# 순위

# n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 권투 경기는 1대1 방식으로 진행이 되고,
# 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 심판은 주어진 경기 결과를 가지고 선수들의
# 순위를 매기려 합니다. 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.
# 선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는 선수의 수를
# return 하도록 solution 함수를 작성해주세요.

def solution(n, results):
    answer = 0
    tree = [[0]*(n+1) for _ in range(n+1)]  # 트리 생성
    # visited = [0] * (n + 1)
    for a, b in results:  # 노드 입력
        tree[a][b] = 1      # 승리
        tree[b][a] = -1  # 패배
    for i in range(n + 1):
        print(tree[i])
    print('-------------------------------------')
    for i in range(1, n+1):
        for j in range(1, n+1):
            if tree[i][j] == 1:  # i 가 j 에게 이김
                for k in range(1, n+1):
                    if tree[j][k] == 1 and tree[i][k] == 0:  # j 가 k 에게 이기고 i 와 k 가 대결을 안해도
                        tree[i][k] = 1          # i 가 k 를 이김
                        tree[k][i] = -1         # k 가 i  한테 짐
            elif tree[i][j] == -1:  # i 가 j 에게 지면
                for k in range(1, n+1):
                    if tree[j][k] == -1 and tree[i][k] == 0:  # j 가 k 에게 지고 i 와 k 가 대결을 안해도
                        tree[i][k] = -1        # i 가 k 한테 짐
                        tree[k][i] = 1         # k 가 i 를 이김
    for i in range(n+1):
        print(tree[i])
    for i in range(n+1):    # 0의 개수 가 1개면 자기빼고 대결완료
        if tree[i].count(0) == 2:
            answer += 1

    return answer



n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(5 ,[[1, 2], [4, 5], [3, 4], [2, 3]]))
# print(solution(n, results))