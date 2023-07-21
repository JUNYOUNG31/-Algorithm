# 최소직사각형

def solution(sizes):
    x = []
    y = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            x.append(sizes[i][0])
            y.append(sizes[i][1])
        else:
            y.append(sizes[i][0])
            x.append(sizes[i][1])

    return max(x) * max(y)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))