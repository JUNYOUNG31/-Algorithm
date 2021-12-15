# 완주하지 못한 선수

# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.


def solution(participant, completion):
    answer = ''
    names = {}
    for i in participant:                           # 반복
        if i in names:                              # 만약  딕셔너리에 있다면
            names[i] += 1                           # value 1 증가
        else:                                       # 없으면
            names[i] = 1                            # 1
    for i in completion:                            # 반복
        names[i] -= 1                               # 완주했으니 1빼서 0으로 만들기
    for i in names.keys():                          # 다돌아서
        if names[i] == 1:                           # 1이있으면 완주안한 사람
            answer = i
    return answer


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))