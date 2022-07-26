# A와 B

S = list(input())
T = list(input())
same = False

while T:
    if T[-1] == 'A':     # 맨뒤가 A면 A를 pop
        T.pop()
    elif T[-1] == 'B':   # 맨뒤가 B 면 B를 pop 하고 뒤집기
        T.pop()
        T.reverse()
    if S == T:           # 이러다가 같으면 멈춰
        same = True
        break

if same:
    print(1)
else:
    print(0)