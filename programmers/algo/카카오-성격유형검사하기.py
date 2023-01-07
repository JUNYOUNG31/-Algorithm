# 성격 유형 검사하기

def solution(survey, choices):
    answer = ''
    arr = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(len(survey)):
        if choices[i] < 4:
            # print(survey[i][0])
            arr[survey[i][0]] += abs(4-choices[i])
        elif choices[i] > 4:
            arr[survey[i][1]] += abs(4-choices[i])
            # print(survey[i][1])
    # print(arr)
    if arr.get('R') >= arr.get('T'):
        answer += 'R'
    else:
        answer += 'T'
    if arr.get('C') >= arr.get('F'):
        answer += 'C'
    else:
        answer += 'F'
    if arr.get('J') >= arr.get('M'):
        answer += 'J'
    else:
        answer += 'M'
    if arr.get('A') >= arr.get('N'):
        answer += 'A'
    else:
        answer += 'N'
    return answer


ans = solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5])
print(ans)