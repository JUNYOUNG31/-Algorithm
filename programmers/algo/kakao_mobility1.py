# 1번 문제
def solution(flowers):
    arr = [0] * 366
    for i in flowers:
        for j in range(i[0], i[1]):
            arr[j] = 1
    answer = 366 - arr.count(0)
    return answer


flowers = [[2, 5], [3, 7], [10, 11]]

print(solution(flowers))


# [[3, 4], [4, 5], [6, 7], [8, 10]]
# [[3, 4], [4, 5], [6, 7], [8, 10], [100, 200]]

# 6
# 5