from typing import List
from collections import defaultdict


def solution(queries: List[List[int]]) -> int:
    arr = defaultdict(list)
    cnt = 0
    for i, j in queries:
        if i in arr:
            if arr[i][0] >= arr[i][1] + j:
                arr[i][1] += j
            else:
                if arr[i][1] != 0:
                    cnt += arr[i][1]
                arr[i][1] += j
                for k in range(100):
                    temp = 2**k
                    if temp >= arr[i][1]:
                        arr[i][0] = temp
                        break
        else:
            arr[i] = [0, j]  # 크기, 원소
            for k in range(100):
                temp = 2 ** k
                if temp >= arr[i][1]:
                    arr[i][0] = temp
                    break
    return cnt


queries = [[2, 10], [7, 1], [2, 5], [2, 9], [7, 32]]

ans = solution(queries)
print(ans)