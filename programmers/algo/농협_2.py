# 농협 2

def solution(num1, num2):
    answer = 0
    for a in range(1, num1+1):
        for b in range(1, num2 + 1):
            flag = 1
            c = a * b
            A = list(str(a))
            B = list(str(b))
            C = list(str(c))
            hap = A + B
            for i in C:
                if not i in hap:
                    flag = 0
            if flag == 1:
                answer += 1

    return answer


print(solution(29, 32))
