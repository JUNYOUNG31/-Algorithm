# 암호제작

P, K = map(int, input().split())
ans = True
for i in range(2, K):
    if P % i == 0:
        print('BAD', i)
        ans = False
        break
if ans:
    print('GOOD')