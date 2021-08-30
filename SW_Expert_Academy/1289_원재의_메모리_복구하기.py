# 원재의 메모리 복구하기
T = int(input())
for tc in range(1, T+1):
    memory = input()
    cnt = 0
    check = 0
    for i in range(len(memory)):
        if check == 0 and memory[i] == '1':
            check = 1
            cnt += 1
        elif check == 1 and memory[i] == '0':
            check = 0
            cnt += 1
    print('#{} {}'.format(tc, cnt))