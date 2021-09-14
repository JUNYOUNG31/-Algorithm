# 단어 공부

# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이
# 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

word = input()                     # 단어입력
x = word.upper()                   # 단어를 대문자로 다 바꿔
set_word = list(set(x))            # 중복값을 제거해
count = []                         # set 한 값의 개수 리스트
            
for i in set_word:                 # 몇개인지 확인하기
    cnt = 0                        # 카운트 0
    for j in x:                    # 대문자로 바꾼 리스트를 반복해서
        if j == i:                 # 같은게 잇다면
            cnt += 1               # cnt 1 더하고
    count.append(cnt)              # 다돌면 각 인덱스에 cnt 추가

max_cnt = max(count)               # 그중 최대값 저장
check = 0                          # 중복확인
for i in count:                    # count 리스트 반복해서
    if i == max_cnt:               # 최대값이라면
        check += 1                 # check 에 1 추가  (2면 중복되니깐 ? 출력)
        
if check == 1:                     # check 가 1 이라면 
    max_idx = count.index(max_cnt) # 최대값의 인덱스를 뽑아서
    print(set_word[max_idx])       # 해당하는 대문자 뽑기
else:                              # 아니면 중복값이 2개이상이니깐
    print('?')                     # ? 출력

