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

r, c, k = map(int, input().split())
A = [[0]*101 for _ in range(101)]
for i in range(3):
    x, y, z = list(map(int, input().split()))
    A[i][0] = x
    A[i][1] = y
    A[i][2] = z

for i in range(3):
    print(A[i])

# B = []  # 전치행렬
# for i in zip(*A):
#     B.append(list(i))
# for i in range(3):
#     print(B[i])
def B(A):
    new_A = []
    length = 0
    for i in range(len(A)):
        row = A[i]
        a = []
        for num in set(row):
            if num == 0:
                continue
            cnt = row.count(num)
            a.append((num, cnt))
        a = sorted(a, key=lambda x:[x[1], x[0]])

        print(a)
        for j in range(50):
            if j < len(a):
                A[i][j * 2] = a[j][0]
                A[i][j * 2 + 1] = a[j][1]
            else:
                A[i][j * 2] = 0
                A[i][j * 2 + 1] = 0
        print(A[:3])
    return A

def C(A):
    C = []
    A = B(A)
    for i in zip(*A):
        C.append(list(i))
    return C


flag = True
for i in range(101):
    if A[r-1][c-1] == k:
        print(i)
        flag = False
        break

    row_cnt = 0
    for j in range(101):
        for k in range(101):
            if A[k][j] == 0:
                row_cnt = max(row_cnt, k)
                break

    col_cnt = 0
    for j in range(101):
        for k in range(101):
            if A[j][k] == 0:
                col_cnt = max(col_cnt, k)
                break

    print(row_cnt)
    print(col_cnt)
    if row_cnt >= col_cnt:
        A = B(A)
    else:
        A = C(A)

    if flag == True:
        print(-1)
