# 접미사 배열

# 접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬해 놓은 배열이다.
# baekjoon의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n 으로 총 8가지가 있고,
# 이를 사전순으로 정렬하면, aekjoon, baekjoon, ekjoon, joon, kjoon, n, on, oon이 된다.
# 문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력하는 프로그램을 작성하시오.

# 첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000보다 작거나 같다.

word = list(input())              # 리스트로 쪼개기
suffix = []                       # 접미사 배열
for _ in range(len(word)):        # 단어의 길이만큼 반복
    suffix.append(''.join(word))  # 한자리로 되있으니깐 붙여서 추가
    word.pop(0)                   # 첫글자 삭제
suffix.sort()                     # 다돌고 정렬하기
for i in suffix:                  # 반복해서 출력
    print(i)

