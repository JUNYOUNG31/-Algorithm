#

def solution(paths):
    answer = []
    paths.sort()
    start = []
    end = []
    arr = [0 for _ in range(100001)]
    for i, j in paths:
        arr[i] = j

    for i in range(100001):
        if arr[i] != 0:
            answer.append(i)
            temp = arr[i]
            print(temp)
            flag = True
            while flag:
                temp1 = arr[temp]
                if temp1 == 0:
                    flag = False
                else:
                    temp = arr[temp1]
            answer.append(temp)


    for i in range(11):
        print(arr[i])
    return answer



paths = [[1, 2], [4, 5], [10, 9], [3, 4]]


print(solution(paths))