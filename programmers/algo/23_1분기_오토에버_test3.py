# 3번
# 일의 보상의 최대치 구하기
# 연속으로 근무하거나 근무하지 않거나
import sys
input = sys.stdin.readline()


N = int(input())
work = list(map(int, input().split()))
no_work = list(map(int, input().split()))

dp = [0] * N

left_1 = 0
left_2 = 0
right_1 = sum(work)
right_2 = sum(no_work)

for i in range(N):
    left_1 += work[i]
    right_1 -= work[i]
    left_2 += no_work[i]
    right_2 -= no_work[i]
    dp[i] = max(left_1 + right_2, left_2 + right_1)

print(max(dp))