# 별찍기 10

N = int(input())


def star(x):
    if x == 3:
        return ['***', '* *', '***']
    arr = star(x//3)
    stars = []
    for i in arr:
        stars.append(i*3)
    for i in arr:
        stars.append(i+' '*(x//3)+i)
    for i in arr:
        stars.append(i*3)
    return stars


print('\n'.join(star(N)))