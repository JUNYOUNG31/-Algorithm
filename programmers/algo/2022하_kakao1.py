import datetime

def solution(today, terms, privacies):
    answer = []
    term = {}

    date = list(map(int, today.split('.')))
    time = datetime.date(date[0], date[1], date[2])
    for i in terms:
        term[i[:1]] = int(i[2:])
    pri = []
    for i in privacies:
        temp = list(map(str, i.split()))
        pri.append([list(map(int, temp[0].split('.'))), temp[1]])
    for i, j in pri:
        i[1] += term[j]
        if i[1] > 12:
            i[0] += i[1] // 12
            i[1] %= 12
            if i[1] == 0:
                i[1] = 12
                i[0] -= 1
        i[2] -= 1
        if i[2] == 0:
            i[2] = 28
            i[1] -= 1
            if i[1] == 0:
                i[1] = 12
                i[0] -= 1
    # print(pri)
    # print(time)
    for i in range(len(pri)):
        limit = datetime.date(pri[i][0][0], pri[i][0][1], pri[i][0][2])
        if time > limit:
            answer.append(i+1)

    return answer




print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))