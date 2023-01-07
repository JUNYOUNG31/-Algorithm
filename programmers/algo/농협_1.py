# 농협 1

def solution(m, y1, y2, accounts):
    answer = []
    for i in accounts:
        if i <= m:
            temp = i * y1 * 0.01
            answer.append(temp)
        if i > m:
            temp = i * y2 * 0.01
            answer.append(temp)

    return answer


