# 한국이 그릴울땐 서버를 접속하지

import sys
input = sys.stdin.readline

n = int(input)
yes, no = "DA", "NE"
first, second = map(str, input().strip().split("*"))
for _ in range(n):
    d = input().strip()
    if first == d[:len(first)]:
        d = d[len(first):]
    else:
        print(no)
        continue
    if second == d[-len(second):]:
        print(yes)
    else:
        print(no)
