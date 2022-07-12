# 학생 번호

N = int(input())
numbers = [input() for _ in range(N)]
i = 1
while 1:
    check = set()
    for number in numbers:
        check.add(number[-i:])
    if len(check) == N:
        break
    i += 1
print(i)