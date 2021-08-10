# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 
# 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다.
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과,
# N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.
# 이름은 띄어쓰기 없이 영어 소문자로만 이루어지며, 그 길이는 20 이하이다.
# N, M은 500,000 이하의 자연수이다.
import sys                      # 응답시간를 줄이기 위한 방법
input = sys.stdin.readline      # 응답시간을 줄이기 위한 방법

N , M = map(int, input().split()) # 사람수 지정
list_N = []                       # 듣도 못한사람 모음
list_M = []                       # 보도 못한사람 모음
list_ans=[]                       # 정렬한 답 리스트
# count = 0
for _ in range(N):                # list에 추가
    n = input().strip()
    list_N.append(n)
for _ in range(M):                # list에 추가
    m = input().strip()
    list_M.append(m)

list_ans = list(set(list_N)&set(list_M))    # set 을 이용해서 중복되는 값을 찾기
                                            
# for i in range(N):                        # 이코드는 완전탐색으로 시간이 오래걸리는것같다.
#     for j in range(M):
#         if list_N[i] == list_M[j]:
#             count+=1
#             list_ans.append(list_N[i])
list_ans.sort()                             # 정렬하고
print(len(list_ans))                        # 개수 출력
for i in list_ans:                          # 값 출력
    print(i)      
# print(count)
# for i in range(len(list_ans)):
#     print(list_ans[i])

