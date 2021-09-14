# 문자열 반복

# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
# S에는 QR Code "alphanumeric" 문자만 들어있다.
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8),
# 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다.

T = int(input())                  # 케이스 수
for tc in range(T):               # 케이스 반복
    R, S = list(input().split())  # 반복할 수 와 문자열
    ans = ''                      # 정답 문자열
    for i in S:                   # S 의 단어를 반복해서
        ans += int(R)*i           # 정답에 R 만큼 반복해서 넣기

    print(ans)
