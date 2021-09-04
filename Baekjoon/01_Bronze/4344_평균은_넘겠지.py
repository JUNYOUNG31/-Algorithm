# 평균은 넘겠지

# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
# 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

C = int(input())                                # 케이스 수
for i in range(C):                              # 케이스 반복
    hap = 0                                     # 점수 합
    avg = 0                                     # 평균 값
    cnt = 0                                     # 평균넘은 학생 수
    percent = 0                                 # 의 비율
    score = list(map(int, input().split()))     # 맨앞의 학생 수 까지 포함한 점수를 리스트화
    for j in range(1, len(score)):              # 인덱스르 1부터 돌린다
        hap += score[j]                         # 총합 구하고
    avg = hap / score[0]                        # 평균 구하고
    for k in range(1, len(score)):              # 평균을 넘는 사람의 수 확인하기
        if score[k] > avg:                      # 넘으면
            cnt += 1                            # 학생수 + 1
    percent = cnt / score[0] * 100              # percent 니깐 * 100
    print("{:.3f}%".format(round(percent, 3)))  # 소수 3째자리까지 표시 하고 반올림

