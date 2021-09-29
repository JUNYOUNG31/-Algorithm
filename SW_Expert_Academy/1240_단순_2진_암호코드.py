# 단순 2진 암호코드

num = {              # 바꿀 번호
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

T = int(input())                                 # case 입력
for tc in range(1, T+1):                         # case 반복
    N, M = map(int, input().split())             # 크기입력
    real_code = []                               # 진짜 코드 담기
    for i in range(N):                           # 코드수만큼 반복
        code = list(input())                     # code 입력받아서
        if '1' in code:                          # 그안에 1 이 있다면
            real_code = code                     # 진짜코드다
    list_code = []                               # 이코드들을
    for i in range(len(real_code)-1,-1,-1):      # 뒤에서 부터 찾아서
        if real_code[i] == '1':                  # 1이 나오면
            list_code = real_code[i-55:i+1]      # 그앞의 56자리를 가져온다
            break                                # 그리고 스톱
    code_7 = []                                  # 56 자리를 7자리로 커트
    for i in range(len(list_code) // 7):         # 길이를 7로 나눈 만큼 반복
        code_s = []                              # 임시 리스트
        for j in range(7):                       # 7만큼 반복
            code_s.append(list_code.pop(0))
        code_7.append(''.join(code_s))           # 7자리 수로 리스트 담기
    code_8 = []                                  # 10진수로 바꿔서 정렬할 리스트
    for i in code_7:                             # 위의 바꿀 숫자들을
        code_8.append(num[i])                    # 찾아서 넣기
    # 홀수자리 합 X3 + 짝수자리 합 + 검증코드 합
    hap = (code_8[0] + code_8[2] + code_8[4] + code_8[6])*3 + (code_8[1] + code_8[3] + code_8[5]) + code_8[7]
    if hap % 10 == 0:                            # 10으로 나눠서 0 이면
        print("#{} {}".format(tc, sum(code_8)))  # 검증코드니깐 각자리 합
    else:                                        # 아니면
        print("#{} {}".format(tc, 0))            # 틀려서 0 출력