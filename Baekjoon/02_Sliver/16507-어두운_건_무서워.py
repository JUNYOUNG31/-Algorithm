# 어두운 건 무서워

R, C, Q = map(int, input().split())
pan = []
for _ in range(R):
    temp = list(map(int, input().split()))
    pan.append(temp)

hap = [[0 for _ in range(C+1)] for _ in range(R+1)]
for i in range(R):
    for j in range(C):
        hap[i+1][j+1] = hap[i][j+1] + hap[i+1][j] - hap[i][j] + pan[i][j]

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    temp = (r2-r1+1) * (c2-c1+1)
    print((hap[r2][c2] - hap[r2][c1-1] - hap[r1-1][c2] + hap[r1-1][c1-1]) // temp)