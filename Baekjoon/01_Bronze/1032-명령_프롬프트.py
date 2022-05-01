# 명령 프롬프트

N = int(input())
word = list(input())
length = len(word)
for i in range(N - 1):
    txt = list(input())
    for j in range(length):
        if word[j] != txt[j]:
            word[j] = '?'
print(''.join(word))