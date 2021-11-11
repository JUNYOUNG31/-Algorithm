# 체육복

# 점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을
# 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을
# 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면
# 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.
# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴
# 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

def solution(n, lost, reserve):
    real_reserve = []               # 제거된 여유있는 사람
    real_lost = []                  # 제거된 도난당한 사람
    for i in reserve:               # 반복해서  없으면 추가
        if i not in lost:
            real_reserve.append(i)
    for i in lost:                  # 반복해서 있으면 추가
        if i not in reserve:
            real_lost.append(i)
    # print(real_reserve)
    # print(lost)
    # real_lost.sort()                # 정렬
    # real_reserve.sort()
    for i in real_reserve:          # 여유분을 반복해서
        if i-1 in real_lost:        # -1 한값이 도난에 붙어잇다면
            real_lost.remove(i-1)   # i-1 값을 삭제
        elif i+1 in real_lost:      # +1 한값이 도난에 붙어있다면
            real_lost.remove(i+1)   # 제거
    answer = n - len(real_lost)     # 총사람수 - 남은 도난당한사람
    return answer


n = 5
lost = [2, 4]
reserve = [1, 3, 5]

print(solution(n, lost, reserve))
