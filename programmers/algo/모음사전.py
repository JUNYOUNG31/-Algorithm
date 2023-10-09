# 모음사전

def solution(word):
    ans = 0
    words = []
    word = "AEIOU"

    def check(cnt, w):
        if cnt == 5:
            return
        for i in range(len(words)):
            words.append(w + words[i])
            check(cnt + 1, w + words[i])

    check(0, "")

    return words.index(word) + 1