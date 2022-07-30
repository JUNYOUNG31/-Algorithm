# 공항
import sys


def find(n):
    if gate[n] == n:
        return n
    else:
        gate[n] = find(gate[n])
        return gate[n]


def union(a, b):
    x = find(a)
    y = find(b)
    gate[x] = y
    return


G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
arr = []
gate = [i for i in range(G + 1)]
cnt = 0
for _ in range(P):
    g = int(input())
    park = find(g)
    if park == 0:
        break
    union(park, park-1)
    cnt += 1
print(cnt)