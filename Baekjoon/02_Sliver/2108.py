# 통계학

# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다.
# 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다.
# 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다.
import sys
N = int(input())
list_N = []
for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    list_N.append(num)

ans1 = round(sum(list_N) / N)       # 산술 평균

ans_2 = sorted(list_N)              # 중앙값
ans2 = ans_2[N//2]

obj = {}
for i in list_N:
    try:
        obj[i] += 1
    except:
        obj[i] = 1

items = sorted(obj.items())
ans_3 = sorted(items, key=lambda x: x[1], reverse=True)
if len(ans_3) == 1:
    ans3 = ans_3[0][0]
elif ans_3[0][1] == ans_3[1][1]:
    ans3 = ans_3[1][0]
elif ans_3[0][1] != ans_3[1][1]:
    ans3 = ans_3[0][0]

ans_4 = sorted(list_N)              # 범위
ans4 = ans_4[-1] - ans_4[0]         # 정렬해서 큰수 - 작은수

print(ans1)
print(ans2)
print(ans3)
print(ans4)



