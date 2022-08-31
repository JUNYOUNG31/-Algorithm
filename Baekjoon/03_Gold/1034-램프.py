# 램프

N, M = map(int, input().split())
ramp = []
for i in range(N):
    x = list(input())
    ramp.append(x)
K = int(input())
cnt = [0] * N
for i in range(N):
    zero = ramp[i].count('0')  # 0의 개수
    if zero <= K:  # K 보다 작고
        if zero % 2 != 0:  # 0의개수가 홀수이면서
            if K % 2 != 0:  # K 도 홀수면
                for j in range(N):  # 똑같은게 있는지 찾아본다
                    if ramp[i] == ramp[j]:
                        cnt[i] += 1
        elif zero % 2 == 0: # 0의 개수가 짝수면서
            if K % 2 == 0:     # K 도 짝수면
                for j in range(N):
                    if ramp[i] == ramp[j]:
                        cnt[i] += 1
# print(cnt)
print(max(cnt))
# for i in ramp:
#     print(i)