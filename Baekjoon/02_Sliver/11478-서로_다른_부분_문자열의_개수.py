# 서로 다른 부분 문자열의 개수

S = input()
words = set()
for i in range(1, len(S) + 1):
    for j in range(len(S) - i + 1):
        word = S[j:j + i]
        words.add(word)
print(len(words))