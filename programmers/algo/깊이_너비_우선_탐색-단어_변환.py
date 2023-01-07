# 단어 변환

# 두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여
# begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.

# 예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.
# 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐
# begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

answer = []                             # 정답 리스트
def solution(begin, target, words):
    global answer
    cnt = 0                                    # 횟수
    if target not in words:                    # 단어가없으면 0
        return 0
    if target == begin:                        # 시작이랑 같으면 0
        return 0
    visited = [0] * len(words)                 # 방문 처리
    dfs(begin, target, words, visited, cnt)    # dfs
    # print(answer)
    answer = min(answer)                       # 최솟값
    return answer


def dfs(begin, target, words, visited, cnt):         # dfs
    global answer
    if begin == target:                              # 같은거면
        return answer.append(cnt)                    # cnt 를 정답에 추가
    possible_word = []                               # 가능한 단어 리스트
    for word in words:                               # 전체를 돌려서
        cnt_change = 0                               # 바뀐단어의 개수
        for i in range(len(target)):                 # 단어길이만큼 돌아서
            if begin[i] != word[i]:                  # 자리가 같지않으면
                cnt_change += 1                      # 1씩 추가
            if cnt_change >= 2:                      # 2이상은
                break                                # 멈춰
        if cnt_change == 1:                          # 단어 한개만 다른거
            possible_word.append(word)               # 추가
    for i in possible_word:                          # 1개만 다른 단어들 중에서
        if not visited[words.index(i)]:              # 방문하지않았으면
            visited[words.index(i)] = 1              # 방문처리하고
            dfs(i, target, words, visited, cnt + 1)  # 그단어로 다시 dfs
            visited[words.index(i)] = 0              # 방문취소


begin = "hit"
target = "cog"	
words = ["hot", "dot", "dog", "lot", "log", "cog"]


print(solution(begin, target, words))
# begin = "hit"
# target = "cog"
# words = ["hot", "dot", "dog", "lot", "log"]
