# 링


def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1


N = int(input())
rings = list(map(int, input().split()))
for i in range(1, N):
    gcd_val = gcd(rings[0], rings[i])
    print('{}/{}'.format(rings[0]//gcd_val, rings[i]//gcd_val))