# 크로아티아 알파벳

# 첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
# 단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.




word = str(input())          # 문자 입력
list_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']  # 알파벳
cnt = 0                      # 갯수
for i in list_alpha:         # 크로아티아 알파벳이
    if i in word:            # 단어안에 있다면
        cnt += word.count(i) # 그단어의 수만큼 +
print(len(word)-cnt)         # 전체 길이에서 그만큼 빼기





# word = str(input())               # 문자 입력
# cnt = 0                           # 크로아티아 문자 갯수
# for i in range(len(word)+1):      # 반복
#     cnt += 1                      # 1씩증가
#     if i == len(word)-1:          # 인덱스 에러 방지
#         break
#     if word[i] == 'c' and word[i+1] == ('=' or '-'):
#         cnt -= 1
#     if word[i] == 'd' and word[i+1] == 'z' and word[i+2] == '=':
#         cnt -= 2
#     if word[i] == 'd' and word[i+1] == '-':
#         cnt -= 1
#     if word[i] == 'l' and word[i+1] == 'j':
#         cnt -= 1
#     if word[i] == 'n' and word[i+1] == 'j':
#         cnt -= 1
#     if word[i] == 's' and word[i+1] == '=':
#         cnt -= 1
#     if word[i] == 'z' and word[i+1] == '=' and word[i-1] != 'd':
#         cnt -= 1
#
# print(cnt)