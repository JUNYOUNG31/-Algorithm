# 플러그
import sys

N = int(sys.stdin.readline())
ans = 0
for i in range(N):
    ans += int(sys.stdin.readline())
print(ans - (N - 1))