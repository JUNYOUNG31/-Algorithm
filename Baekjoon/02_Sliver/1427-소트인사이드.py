# 소트 인사이드

num = input()
num = [int(n)  for n in num]

sort_num = sorted(num, reverse=True)

for n in sort_num :
    print(n, end="")