# 팀 이름 정하기

name = input()
N = int(input())
arr = [input() for i in range(N)]
arr.sort()
max_num = 0
ans = 0
for i in range(N):
    L = name.count("L") + arr[i].count("L")
    O = name.count("O") + arr[i].count("O")
    V = name.count("V") + arr[i].count("V")
    E = name.count("E") + arr[i].count("E")
    num = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    if max_num < num:
        max_num = num
        ans = i
print(arr[ans])