
survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = 	[5, 3, 2, 7, 5]

def solution(survey, choices):
    list_one = [['R', 0], ['T', 0], ['C', 0], ['F', 0], ['J', 0], ['M', 0], ['A', 0], ['N', 0]]
    answer = ''
    for i in range(len(survey)):
        a = list(survey[i])
        if choices[i] == 1:
            for j in list_one:
                if j[0] == a[0]:
                    j[1] += 3
        if choices[i] == 2:
            for j in list_one:
                if j[0] == a[0]:
                    j[1] += 2
        if choices[i] == 3:
            for j in list_one:
                if j[0] == a[0]:
                    j[1] += 1
        if choices[i] == 4:
            for j in list_one:
                if j[0] == a[0]:
                    j[1] += 0
        if choices[i] == 5:
            for j in list_one:
                if j[0] == a[1]:
                    j[1] += 1
        if choices[i] == 6:
            for j in list_one:
                if j[0] == a[1]:
                    j[1] += 2
        if choices[i] == 7:
            for j in list_one:
                if j[0] == a[1]:
                    j[1] += 3

    if list_one[0][1] >= list_one[1][1]:
        answer += 'R'
    else:
        answer += 'T'
    if list_one[2][1] >= list_one[3][1]:
        answer += 'C'
    else:
        answer += 'F'
    if list_one[4][1] >= list_one[5][1]:
        answer += 'J'
    else:
        answer += 'M'
    if list_one[6][1] >= list_one[7][1]:
        answer += 'A'
    else:
        answer += 'N'
    return answer

print(solution(survey, choices))

