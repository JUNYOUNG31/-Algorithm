# 부호
import sys

for i in range(3):
    N = int(sys.stdin.readline())
    num = [int(sys.stdin.readline()) for _ in range(N)]
    if sum(num) == 0:
        print(0)
    elif sum(num) > 0:
        print("+")
    else:
        print("-")