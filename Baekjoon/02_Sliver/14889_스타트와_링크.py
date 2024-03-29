# 스타트와 링크

# 오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다.
# 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과
# 링크 팀으로 사람들을 나눠야 한다. BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고,
# 아래와 같은 능력치를 조사했다. 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다.
# 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이
# 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.


# 첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다.
# 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고,
# 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.
from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
num = [int(i) for i in range(N)]
ans = 123456789
combination = set(combinations(num, N//2))
for team in combination:
    A = 0
    B = 0
    for r in range(N):
        for c in range(N):
            check1 = 0
            check2 = 0
            if r in team:
                check1 = 1
            if c in team:
                check2 = 1

            if check1 == 1 and check2 == 1:
                A += S[r][c]
            elif check1 == 0 and check2 == 0:
                B += S[r][c]
    temp = abs(A - B)
    if temp < ans:
        ans = temp
    if temp == 0:
        ans = 0
        break
print(ans)