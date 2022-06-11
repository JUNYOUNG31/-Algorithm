# 팰린드롬수

while True:
    num = input()
    if num == '0':
        break
    ans = 'no'
    if num[::-1] == num:
        ans = 'yes'
    print(ans)


