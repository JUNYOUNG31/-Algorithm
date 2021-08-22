# 단어 정렬

# 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐
# 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

N = int(input())                # 갯수
list_word = []                  # 빈리스트
for i in range(N):              # N 번 반복
    word = str(input())         # 문자열
    list_word.append(word)      # 추가

set_word = list(set(list_word)) # 중복값을 제거
set_word.sort()                 # 한번더 정렬안하면 오류....
set_word.sort(key=len)          # 문자의 길이에 따라 정렬

for i in range(len(set_word)):  # 정렬된값을 출력
    print(set_word[i])