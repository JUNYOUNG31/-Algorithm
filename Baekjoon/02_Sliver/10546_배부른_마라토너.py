# 배부른 마라토너

# 마라토너라면 국적과 나이를 불문하고 누구나 참가하고 싶어하는 백준 마라톤 대회가 열린다.
# 42.195km를 달리는 이 마라톤은 모두가 참가하고 싶어했던 만큼 매년 모두가 완주해왔다. 단, 한 명만 빼고!
# 모두가 참가하고 싶어서 안달인데 이런 백준 마라톤 대회에 참가해 놓고 완주하지 못한 배부른 참가자 한 명은 누굴까?

# 첫째 줄에는 참가자 수 N이 주어진다. (1 ≤ N ≤ 105) N개의 줄에는 참가자의 이름이 주어진다.
# 추가적으로 주어지는 N-1개의 줄에는 완주한 참가자의 이름이 쓰여져 있다.
# 참가자들의 이름은 길이가 1보다 크거나 같고, 20보다 작거나 같은 문자열이고, 알파벳 소문자로만 이루어져 있다.
# 참가자들 중엔 동명이인이 있을 수도 있다.
import sys
N = int(sys.stdin.readline())                   # 입력
names = {}                                      # 딕서너리로 바꾸기
for i in range(N):                              # 반복
    name = sys.stdin.readline().rstrip()        # 사람 입력
    if name in names:                           # 만약  딕셔너리에 있다면
        names[name] += 1                        # value 1 증가
    else:                                       # 없으면
        names[name] = 1                         # 1
for i in range(N-1):                            # 반복
    finish_name = sys.stdin.readline().rstrip() # 입력
    if finish_name in names:                    # 이름이 있다면
        names[finish_name] -= 1                 # 완주했으니 1빼서 0으로 만들기

for i in names.keys():                          # 다돌아서
    if names[i] == 1:                           # 1이있으면 완주안한 사람
        print(i)
