# 이차원 배열과 연산

# 크기가 3×3인 배열 A가 있다. 배열의 인덱스는 1부터 시작한다. 1초가 지날때마다 배열에 연산이 적용된다.
# R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다. 행의 개수 ≥ 열의 개수인 경우에 적용된다.
# C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우에 적용된다.
# 한 행 또는 열에 있는 수를 정렬하려면, 각각의 수가 몇 번 나왔는지 알아야 한다. 그 다음, 수의 등장 횟수가 커지는 순으로,
# 그러한 것이 여러가지면 수가 커지는 순으로 정렬한다. 그 다음에는 배열 A에 정렬된 결과를 다시 넣어야 한다.
# 정렬된 결과를 배열에 넣을 때는, 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저이다.
# 예를 들어, [3, 1, 1]에는 3이 1번, 1가 2번 등장한다. 따라서, 정렬된 결과는 [3, 1, 1, 2]가 된다.
# 다시 이 배열에는 3이 1번, 1이 2번, 2가 1번 등장한다. 다시 정렬하면 [2, 1, 3, 1, 1, 2]가 된다.
# 정렬된 결과를 배열에 다시 넣으면 행 또는 열의 크기가 달라질 수 있다. R 연산이 적용된 경우에는
# 가장 큰 행을 기준으로 모든 행의 크기가 변하고, C 연산이 적용된 경우에는 가장 큰 열을 기준으로 모든 열의 크기가 변한다.
# 행 또는 열의 크기가 커진 곳에는 0이 채워진다. 수를 정렬할 때 0은 무시해야 한다. 예를 들어,
# [3, 2, 0, 0]을 정렬한 결과는 [3, 2]를 정렬한 결과와 같다.
# 행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.
# 배열 A에 들어있는 수와 r, c, k가 주어졌을 때, A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간을 구해보자.
from collections import defaultdict

def make_row(arr):
    cnt_num = defaultdict(int)
    for num in (arr):
        if num == 0:
            continue
        cnt_num[num] += 1

    cnt_num_list = []
    for num, cnt in cnt_num.items():
        cnt_num_list.append((num, cnt))

    cnt_num_list.sort(key=lambda x: (x[1], x[0]))  # 정렬하기

    new_row = []
    for i in range(len(cnt_num_list)):     # 새로운 배열에
        new_row.append(cnt_num_list[i][0])    # num
        new_row.append(cnt_num_list[i][1])    # cnt

    return new_row[:100] # 100개까지만 가져오기


def R(A):
    new_A = [[0 for i in range(100)] for _ in range(100)]

    for i in range(100):
        row = A[i]
        new_row = make_row(row)

        for j in range(len(new_row)):
            new_A[i][j] = new_row[j]

    return new_A


def C(A):
    new_A = [[0 for i in range(100)] for _ in range(100)]

    for i in range(100):
        col = []
        for j in range(100):
            col.append(A[j][i])

        new_col = make_row(col)
        for j in range(len(new_col)):
            new_A[j][i] = new_col[j]

    return new_A


def max_len(A):
    max_row = 0
    max_col = 0

    for i in range(100):
        while max_row < 100 and A[max_row][i] != 0:
            max_row += 1

    for i in range(100):
        while max_col < 100 and A[i][max_col] != 0:
            max_col += 1

    return (max_row, max_col)


r, c, k = map(int, input().split())
A = [[0 for i in range(100)] for j in range(100)]
a = [list(map(int, input().split())) for _ in range(3)]
for i in range(3):
    for j in range(3):
        A[i][j] = a[i][j]

# for i in range(3):
#     print(A[i])

time = 0
while time <= 100:
    if A[r-1][c-1] == k:
        break

    len_row, len_col = max_len(A)
    if len_row >= len_col:
        A = R(A)
    else:
        A = C(A)
    time += 1

if time > 100:
    time = -1
print(time)






