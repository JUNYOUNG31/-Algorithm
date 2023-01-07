# 기능 개발

# 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고,
# 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열
# speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.


def solution(progresses, speeds):
    answer = []
    day = 0                                   # 일수
    while progresses:                         # 반복
        cnt = 0                               # 총 완료된 개수
        while progresses[0] < 100:            # 첫 작업이 100보다 작으면
            for i in range(len(progresses)):  # 각 인덱스의 값들을
                progresses[i] += speeds[i]    # 스피드 값과 더하기
            day += 1                          # 일수 늘리기
        # print(day)
        # print(progresses)
        # print(speeds)
        while progresses:                     # 반복
            if progresses[0] >= 100:          # 첫 작업이 100보다 크면
                cnt += 1                      # 1 추가
                progresses.pop(0)             # 작업 팝하기
                speeds.pop(0)                 # 스피드 팝하기
            else:                             # 멈춰
                break                         
        answer.append(cnt)                    # 여기 추가 될때는 다음작업이 100안된거  
    return answer                             # 리턴


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))