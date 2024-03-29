# 알파벳 찾기

# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서,
# 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

S = list(input())                                                               # 단어 S
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',    # 알파벳리스트
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ans = [-1] * 26                                                                 # -1 로 구성된 정답리스트
for i in range(len(alphabet)):                      # 알파벳의 길이 만큼 반복해서
    for j in range(len(S)):                         # 단어의 길이 만큼 반복하고
        if S[j] == alphabet[i] and ans[i] == -1:    # 값이 같으면 알파벳의 인덱스를 가져오고 정답리스트에서 -1 이 아니면
            ans[i] = j                              # 인덱스를 단어의 순번으로 바꾸기
print(*ans)