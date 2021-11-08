# 모의고사

# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
# 번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌
# 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.


def solution(answers):
    answer = []                           # 정답 리스트
    num1 = [1,2,3,4,5]                    # 1번 수포자
    num2 = [2,1,2,3,2,4,2,5]              # 2번 수포자
    num3 = [3,3,1,1,2,2,4,4,5,5]          # 3번 수포자
    cnt1 = 0                              # 1번 수포자의 맞은 수
    cnt2 = 0                              # 2번 수포자의 맞은 수
    cnt3 = 0                              # 3번 수포자의 맞은 수
    cnt = len(answers)                    # 문제수
    cnt_list = []                         # 맞은 수 리스트
    for i in range(cnt):                  # 문제수 만큼 돌려서
        if answers[i] == num1[i % 5]:     # 1번 수포자 맞은 문제
            cnt1 += 1
        if answers[i] == num2[i % 8]:     # 2번 수포자 맞은 문제
            cnt2 += 1
        if answers[i] == num3[i % 10]:    # 3번 수포자 맞은 문제
            cnt3 += 1
    cnt_list.append(cnt1)                 # 추가추가추가
    cnt_list.append(cnt2)
    cnt_list.append(cnt3)
    cnt_max = max(cnt_list)               # 최댓값
    for i in range(3):                    # 같은사람있는지 확인하고
        if cnt_max == cnt_list[i]:
            answer.append(i+1)            # 인덱스니깐 1추가해서 추가
    return answer


# answers = [1,2,3,4,5]
answers = [1,3,2,4,2]

print(solution(answers))