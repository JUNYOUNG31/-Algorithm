# 모음의 개수

arr = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    string = input()
    if string == '#':
        break
    cnt = 0
    for i in string:
        if i in arr:
            cnt += 1
    print(cnt)