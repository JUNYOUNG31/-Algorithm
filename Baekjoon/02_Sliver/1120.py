# 문자열

# 길이가 N으로 같은 문자열 X와 Y가 있을 때, 두 문자열 X와 Y의 차이는 X[i] ≠ Y[i]인 i의 개수이다.
# 예를 들어, X=”jimin”, Y=”minji”이면, 둘의 차이는 4이다.
# 두 문자열 A와 B가 주어진다. 이때, A의 길이는 B의 길이보다 작거나 같다. 이제 A의 길이가 B의 길이와 같아질 때
# 까지 다음과 같은 연산을 할 수 있다.
# A의 앞에 아무 알파벳이나 추가한다.
# A의 뒤에 아무 알파벳이나 추가한다.
# 이때, A와 B의 길이가 같으면서, A와 B의 차이를 최소로 하는 프로그램을 작성하시오.

# 첫째 줄에 A와 B가 주어진다. A와 B의 길이는 최대 50이고, A의 길이는 B의 길이보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.

A, B = map(str, input().split())  # A 가 B 보다 작다
min_cnt = 123                     # cnt 최솟값
for i in range(len(B)-len(A)+1):  # A를 B 안에서 탐색
    cnt = 0                       # 카운트
    for j in range(len(A)):       # a 를 반복
        if A[j] != B[j+i]:        # 다른글자가 있으면
            cnt += 1              # 카운트 + 1
    if cnt < min_cnt:             # 최솟값 반환
        min_cnt = cnt
print(min_cnt)
