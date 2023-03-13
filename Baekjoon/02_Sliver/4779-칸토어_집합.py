# 칸토어 집합

from sys import setrecursionlimit
setrecursionlimit(1000000)


def rec(s, idx):
    ls = len(s)
    if ls == 3 and idx != 1:
        return '- -'
    elif ls >= 3 and idx == 1:
        return s.replace('-', ' ')
    arr = []
    for i in range(0, ls, ls // 3):
        arr.append(string[i:i+ls//3])
    k = rec(arr[0], 0) + rec(arr[1], 1) + rec(arr[2], 2)
    return k


while True:
    k = '-'
    n = input()
    if n == '':
        break
    num = (3 ** int(n))
    if num == 1:
        print('-')
        continue
    string = k * num
    arr = rec(string, 0)
    print(arr)