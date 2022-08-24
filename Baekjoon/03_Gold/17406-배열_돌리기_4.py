# 배열 돌리기 4
import copy
from itertools import permutations

N, M, K = map(int, input().split())

A = []
for i in range(N):
    temp = list(map(int, input().split()))
    A.append(temp)
# for i in A:
#     print(i)

turn = []
for i in range(K):
    r, c, s = map(int, input().split())
    turn.append([r, c, s])
# for i in turn:
#     print(i)

turn_arr = list(permutations(turn, K))


def turned(arr, r, c, s):
    if s == 0:
        return
    r, c = r-1, c-1
    s_r, s_c = r-s, c-s
    e_r, e_c = r+s, c+s

    temp = arr[s_r][s_c]

    for i in range(s_r, e_r):
       arr[i][s_c] = arr[i+1][s_c]
    for i in range(s_c, e_c):
        arr[e_r][i] = arr[e_r][i+1]
    for i in range(e_r, s_r, -1):
        arr[i][e_c] = arr[i-1][e_c]
    for i in range(e_c, s_c, -1):
        arr[s_r][i] = arr[s_r][i-1]

    arr[s_r][s_c+1] = temp
    turned(arr, r+1, c+1, s-1)


ans = []
for i in turn_arr:
    arr = copy.deepcopy(A)
    min_list = []
    for r, c, s in i:
        # print(r,c,s)
        turned(arr, r, c, s)

    for j in arr:
        temp = sum(j)
        min_list.append(temp)
    ans.append(min(min_list))

    # for x in arr:
    #     print(x)
    # print()

print(min(ans))